#!/usr/bin/env python3
"""Publish an approved launch campaign through official APIs and webhooks.

The command is dry-run by default. Live network mutations require both
``--execute`` and an exact ``--confirm <campaign_id>`` value.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path
from typing import Any, Iterable


SCRIPT_VERSION = "1.2.0"
SCHEMA_VERSION = 1
SUPPORTED_PLATFORMS = {
    "devto",
    "hashnode",
    "mastodon",
    "linkedin",
    "discord",
    "slack",
    "telegram",
    "generic_webhook",
    "assisted",
}
API_PLATFORMS = SUPPORTED_PLATFORMS - {"assisted"}
DEFAULT_TIMEOUT_SECONDS = 20
DEFAULT_RETRIES = 2
PLACEHOLDER_PATTERN = re.compile(r"(?i)(replace[-_ ](?:with|before)|\bTODO\b|\bTBD\b|<[^>]{1,80}>)")


class CampaignError(Exception):
    """Raised for an invalid campaign or an unsafe execution request."""


class PublishError(Exception):
    """Raised when an authorized platform request fails."""


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Keep credentials from following an unexpected redirect."""

    def redirect_request(self, req: Any, fp: Any, code: int, msg: str, headers: Any, newurl: str) -> None:
        return None


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CampaignError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CampaignError(f"Invalid JSON in {path}: line {exc.lineno}, column {exc.colno}") from exc
    if not isinstance(value, dict):
        raise CampaignError(f"Expected a JSON object in {path}")
    return value


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def require_string(container: dict[str, Any], key: str, context: str) -> str:
    value = container.get(key)
    if not isinstance(value, str) or not value.strip():
        raise CampaignError(f"{context}.{key} must be a non-empty string")
    return value.strip()


def optional_string(container: dict[str, Any], key: str) -> str | None:
    value = container.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise CampaignError(f"{key} must be a non-empty string when provided")
    return value.strip()


def resolve_campaign_file(base: Path, relative_path: str, context: str) -> Path:
    candidate = (base / relative_path).resolve()
    try:
        candidate.relative_to(base.resolve())
    except ValueError as exc:
        raise CampaignError(f"{context} must stay inside the campaign directory") from exc
    if not candidate.is_file():
        raise CampaignError(f"{context} does not exist: {relative_path}")
    return candidate


def read_target_content(target: dict[str, Any], base: Path) -> str:
    relative = require_string(target, "content_file", f"target[{target.get('id', '?')}]")
    content = resolve_campaign_file(base, relative, "content_file").read_text(encoding="utf-8").strip()
    if not content:
        raise CampaignError(f"target[{target.get('id', '?')}].content_file is empty")
    return content


def credential_env_names(target: dict[str, Any]) -> list[str]:
    platform = target.get("platform")
    keys = {
        "devto": ["api_key_env"],
        "hashnode": ["token_env"],
        "mastodon": ["access_token_env"],
        "linkedin": ["access_token_env", "api_version_env"],
        "discord": ["webhook_env"],
        "slack": ["webhook_env"],
        "telegram": ["bot_token_env"],
        "generic_webhook": ["endpoint_env"],
        "assisted": [],
    }[str(platform)]
    return [require_string(target, key, f"target[{target.get('id', '?')}]" ) for key in keys]


def find_manifest_placeholders(value: Any, path: str = "target") -> list[str]:
    matches: list[str] = []
    if isinstance(value, str) and PLACEHOLDER_PATTERN.search(value):
        matches.append(path)
    elif isinstance(value, dict):
        for key, child in value.items():
            if key == "content_file" or str(key).endswith("_env"):
                continue
            matches.extend(find_manifest_placeholders(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            matches.extend(find_manifest_placeholders(child, f"{path}[{index}]"))
    return matches


def secret_values(env_names: Iterable[str]) -> list[str]:
    values: list[str] = []
    for name in env_names:
        value = os.environ.get(name)
        if value:
            values.append(value)
    return sorted(set(values), key=len, reverse=True)


def redact(value: str, secrets: Iterable[str]) -> str:
    redacted = value
    for secret in secrets:
        redacted = redacted.replace(secret, "[REDACTED]")
        redacted = redacted.replace(urllib.parse.quote(secret, safe=""), "[REDACTED]")
    redacted = re.sub(r"https://hooks\.slack\.com/services/[^\s\"']+", "[REDACTED_SLACK_WEBHOOK]", redacted)
    redacted = re.sub(r"https://(?:discord(?:app)?\.com)/api/webhooks/[^\s\"']+", "[REDACTED_DISCORD_WEBHOOK]", redacted)
    redacted = re.sub(r"https://api\.telegram\.org/bot[^/\s]+", "https://api.telegram.org/bot[REDACTED]", redacted)
    return redacted


def validate_https(url: str, allow_http: bool, context: str) -> None:
    parsed = urllib.parse.urlparse(url)
    allowed = {"https"} | ({"http"} if allow_http else set())
    if parsed.scheme not in allowed or not parsed.netloc:
        expected = "HTTPS" if not allow_http else "HTTP(S)"
        raise CampaignError(f"{context} must be an absolute {expected} URL")


def target_payload_hash(target: dict[str, Any], content: str, campaign: dict[str, Any]) -> str:
    safe_target = {key: value for key, value in target.items() if not key.endswith("_env")}
    payload = {
        "schema_version": campaign.get("schema_version"),
        "campaign_id": campaign.get("campaign_id"),
        "canonical_url": campaign.get("canonical_url"),
        "target": safe_target,
        "content": content,
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def validate_campaign(
    campaign: dict[str, Any], base: Path, selected_ids: set[str] | None, allow_http: bool
) -> list[dict[str, Any]]:
    if campaign.get("schema_version") != SCHEMA_VERSION:
        raise CampaignError(f"schema_version must be {SCHEMA_VERSION}")
    campaign_id = require_string(campaign, "campaign_id", "campaign")
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]{2,79}", campaign_id):
        raise CampaignError("campaign_id must be 3-80 lowercase letters, digits, dots, underscores, or hyphens")
    canonical_url = require_string(campaign, "canonical_url", "campaign")
    validate_https(canonical_url, allow_http, "canonical_url")
    targets = campaign.get("targets")
    if not isinstance(targets, list) or not targets:
        raise CampaignError("campaign.targets must be a non-empty array")

    seen_ids: set[str] = set()
    prepared: list[dict[str, Any]] = []
    for index, raw_target in enumerate(targets):
        if not isinstance(raw_target, dict):
            raise CampaignError(f"target[{index}] must be an object")
        target = dict(raw_target)
        target_id = require_string(target, "id", f"target[{index}]")
        if target_id in seen_ids:
            raise CampaignError(f"Duplicate target id: {target_id}")
        seen_ids.add(target_id)
        platform = require_string(target, "platform", f"target[{target_id}]").lower()
        if platform not in SUPPORTED_PLATFORMS:
            raise CampaignError(f"target[{target_id}].platform is unsupported: {platform}")
        target["platform"] = platform
        if "enabled" in target and not isinstance(target["enabled"], bool):
            raise CampaignError(f"target[{target_id}].enabled must be true or false")
        if selected_ids and target_id not in selected_ids:
            continue

        content = read_target_content(target, base)
        if platform == "devto":
            require_string(target, "title", f"target[{target_id}]")
            tags = target.get("tags", [])
            if not isinstance(tags, list) or not all(isinstance(tag, str) and tag.strip() for tag in tags):
                raise CampaignError(f"target[{target_id}].tags must be an array of strings")
            if len(tags) > 4:
                raise CampaignError(f"target[{target_id}].tags supports at most 4 tags")
            disclosure = target.get("ai_disclosure_level")
            if disclosure is not None and disclosure not in {"not_disclosed", "no_ai", "some_ai", "fully_autonomous"}:
                raise CampaignError(f"target[{target_id}].ai_disclosure_level is invalid")
        elif platform == "hashnode":
            require_string(target, "publication_id", f"target[{target_id}]")
            require_string(target, "title", f"target[{target_id}]")
        elif platform == "mastodon":
            instance_url = require_string(target, "instance_url", f"target[{target_id}]").rstrip("/")
            validate_https(instance_url, allow_http, f"target[{target_id}].instance_url")
            target["instance_url"] = instance_url
        elif platform == "linkedin":
            require_string(target, "author", f"target[{target_id}]")
        elif platform == "discord" and len(content) > 2000:
            raise CampaignError(f"target[{target_id}] exceeds Discord's 2000-character content limit")
        elif platform == "telegram" and len(content) > 4096:
            raise CampaignError(f"target[{target_id}] exceeds Telegram's 4096-character content limit")
        elif platform == "telegram":
            require_string(target, "chat_id", f"target[{target_id}]")
        elif platform == "generic_webhook":
            field = target.get("content_field", "text")
            if not isinstance(field, str) or not re.fullmatch(r"[A-Za-z0-9_.-]{1,80}", field):
                raise CampaignError(f"target[{target_id}].content_field is invalid")
        elif platform == "assisted":
            publish_url = require_string(target, "publish_url", f"target[{target_id}]")
            validate_https(publish_url, allow_http, f"target[{target_id}].publish_url")

        env_names = credential_env_names(target)
        missing = [name for name in env_names if not os.environ.get(name)]
        if target.get("enabled", False):
            placeholders = find_manifest_placeholders(target, f"target[{target_id}]")
            if placeholders:
                raise CampaignError(f"Unresolved manifest placeholder(s): {', '.join(placeholders)}")
        prepared.append(
            {
                "target": target,
                "content": content,
                "payload_hash": target_payload_hash(target, content, campaign),
                "credential_env_names": env_names,
                "missing_credentials": missing,
            }
        )

    if selected_ids:
        unknown = selected_ids - seen_ids
        if unknown:
            raise CampaignError(f"Unknown target id(s): {', '.join(sorted(unknown))}")
    if not prepared:
        raise CampaignError("No targets selected")
    return prepared


class HttpClient:
    def __init__(self, timeout: int, retries: int, secrets: Iterable[str], allow_http: bool = False) -> None:
        self.timeout = timeout
        self.retries = retries
        self.secrets = list(secrets)
        self.allow_http = allow_http
        self.opener = urllib.request.build_opener(NoRedirectHandler)

    def request(
        self,
        method: str,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        json_body: dict[str, Any] | None = None,
        form_body: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        validate_https(url, self.allow_http, "runtime endpoint")
        request_headers = {"User-Agent": f"github-high-star-optimizer/{SCRIPT_VERSION}"}
        request_headers.update(headers or {})
        data: bytes | None = None
        if json_body is not None:
            data = json.dumps(json_body, ensure_ascii=False).encode("utf-8")
            request_headers.setdefault("Content-Type", "application/json")
        elif form_body is not None:
            normalized = {key: str(value) for key, value in form_body.items() if value is not None}
            data = urllib.parse.urlencode(normalized).encode("utf-8")
            request_headers.setdefault("Content-Type", "application/x-www-form-urlencoded")

        for attempt in range(self.retries + 1):
            request = urllib.request.Request(url, data=data, headers=request_headers, method=method)
            try:
                with self.opener.open(request, timeout=self.timeout) as response:
                    raw = response.read().decode("utf-8", errors="replace")
                    return {"status": response.status, "text": raw, "headers": dict(response.headers.items())}
            except urllib.error.HTTPError as exc:
                raw = exc.read().decode("utf-8", errors="replace")
                if exc.code == 429 or 500 <= exc.code <= 599:
                    if attempt < self.retries:
                        retry_after = exc.headers.get("Retry-After")
                        delay = min(max(float(retry_after or (attempt + 1)), 0.0), 5.0)
                        time.sleep(delay)
                        continue
                detail = redact(raw[:1200], self.secrets).strip()
                raise PublishError(f"HTTP {exc.code}: {detail or 'request rejected'}") from exc
            except urllib.error.URLError as exc:
                if attempt < self.retries:
                    time.sleep(min(attempt + 1, 3))
                    continue
                raise PublishError(redact(f"Network error: {exc.reason}", self.secrets)) from exc
            except TimeoutError as exc:
                if attempt < self.retries:
                    continue
                raise PublishError("Network timeout") from exc
        raise PublishError("Request failed after retries")


def parse_response_json(response: dict[str, Any], platform: str) -> dict[str, Any]:
    text = response.get("text", "")
    try:
        value = json.loads(text) if text else {}
    except json.JSONDecodeError as exc:
        raise PublishError(f"{platform} returned invalid JSON") from exc
    if not isinstance(value, dict):
        raise PublishError(f"{platform} returned an unexpected response")
    return value


def sanitize_result(result: dict[str, Any], secrets: Iterable[str]) -> dict[str, Any]:
    return {
        key: redact(value, secrets) if isinstance(value, str) else value
        for key, value in result.items()
    }


def publish_devto(client: HttpClient, target: dict[str, Any], content: str, campaign: dict[str, Any]) -> dict[str, Any]:
    api_key = os.environ[require_string(target, "api_key_env", "devto target")]
    article: dict[str, Any] = {
        "title": require_string(target, "title", "devto target"),
        "published": bool(target.get("publish", True)),
        "body_markdown": content,
        "tags": ",".join(str(tag).strip() for tag in target.get("tags", [])),
    }
    if target.get("ai_disclosure_level"):
        article["ai_disclosure_level"] = target["ai_disclosure_level"]
    canonical = optional_string(target, "canonical_url") or optional_string(campaign, "canonical_url")
    if canonical:
        article["canonical_url"] = canonical
    response = client.request(
        "POST",
        "https://dev.to/api/articles",
        headers={"api-key": api_key, "accept": "application/vnd.forem.api-v1+json"},
        json_body={"article": article},
    )
    data = parse_response_json(response, "DEV")
    return {"remote_id": data.get("id"), "url": data.get("url"), "published": article["published"]}


def publish_hashnode(client: HttpClient, target: dict[str, Any], content: str, campaign: dict[str, Any]) -> dict[str, Any]:
    token = os.environ[require_string(target, "token_env", "hashnode target")]
    tags = target.get("tags", [])
    if not isinstance(tags, list):
        raise CampaignError("hashnode tags must be an array")
    input_value: dict[str, Any] = {
        "publicationId": require_string(target, "publication_id", "hashnode target"),
        "title": require_string(target, "title", "hashnode target"),
        "contentMarkdown": content,
        "tags": [{"slug": str(tag).strip()} for tag in tags if str(tag).strip()],
    }
    canonical = optional_string(target, "canonical_url") or optional_string(campaign, "canonical_url")
    if canonical:
        input_value["originalArticleURL"] = canonical
    query = """
mutation PublishPost($input: PublishPostInput!) {
  publishPost(input: $input) { post { id slug url title } }
}
""".strip()
    response = client.request(
        "POST",
        "https://gql-beta.hashnode.com/",
        headers={"Authorization": f"Bearer {token}"},
        json_body={"query": query, "variables": {"input": input_value}},
    )
    data = parse_response_json(response, "Hashnode")
    if data.get("errors"):
        raise PublishError(f"Hashnode GraphQL error: {json.dumps(data['errors'], ensure_ascii=False)[:1000]}")
    post = (((data.get("data") or {}).get("publishPost") or {}).get("post") or {})
    return {"remote_id": post.get("id"), "url": post.get("url"), "published": True}


def publish_mastodon(client: HttpClient, target: dict[str, Any], content: str, payload_hash: str) -> dict[str, Any]:
    token = os.environ[require_string(target, "access_token_env", "mastodon target")]
    form: dict[str, Any] = {
        "status": content,
        "visibility": target.get("visibility", "public"),
        "language": target.get("language"),
        "scheduled_at": target.get("scheduled_at"),
    }
    response = client.request(
        "POST",
        f"{require_string(target, 'instance_url', 'mastodon target').rstrip('/')}/api/v1/statuses",
        headers={"Authorization": f"Bearer {token}", "Idempotency-Key": payload_hash},
        form_body=form,
    )
    data = parse_response_json(response, "Mastodon")
    return {"remote_id": data.get("id"), "url": data.get("url"), "published": not bool(target.get("scheduled_at"))}


def publish_linkedin(client: HttpClient, target: dict[str, Any], content: str) -> dict[str, Any]:
    token = os.environ[require_string(target, "access_token_env", "linkedin target")]
    version = os.environ[require_string(target, "api_version_env", "linkedin target")]
    if not re.fullmatch(r"20\d{4}", version):
        raise CampaignError("LinkedIn API version environment value must use YYYYMM")
    payload = {
        "author": require_string(target, "author", "linkedin target"),
        "commentary": content,
        "visibility": target.get("visibility", "PUBLIC"),
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": bool(target.get("disable_reshare", False)),
    }
    response = client.request(
        "POST",
        "https://api.linkedin.com/rest/posts",
        headers={
            "Authorization": f"Bearer {token}",
            "Linkedin-Version": version,
            "X-Restli-Protocol-Version": "2.0.0",
        },
        json_body=payload,
    )
    headers = {str(key).lower(): value for key, value in response.get("headers", {}).items()}
    return {"remote_id": headers.get("x-restli-id"), "url": None, "published": True}


def publish_discord(client: HttpClient, target: dict[str, Any], content: str) -> dict[str, Any]:
    webhook = os.environ[require_string(target, "webhook_env", "discord target")]
    separator = "&" if "?" in webhook else "?"
    payload: dict[str, Any] = {"content": content, "allowed_mentions": {"parse": []}}
    for key in ("username", "avatar_url", "thread_name"):
        if target.get(key):
            payload[key] = target[key]
    response = client.request("POST", f"{webhook}{separator}wait=true", json_body=payload)
    data = parse_response_json(response, "Discord")
    guild_id, channel_id, message_id = data.get("guild_id"), data.get("channel_id"), data.get("id")
    url = f"https://discord.com/channels/{guild_id}/{channel_id}/{message_id}" if guild_id and channel_id and message_id else None
    return {"remote_id": message_id, "url": url, "published": True}


def publish_slack(client: HttpClient, target: dict[str, Any], content: str) -> dict[str, Any]:
    webhook = os.environ[require_string(target, "webhook_env", "slack target")]
    response = client.request("POST", webhook, json_body={"text": content})
    if response.get("text", "").strip().lower() != "ok":
        raise PublishError(f"Slack returned: {response.get('text', '')[:500] or 'empty response'}")
    return {"remote_id": None, "url": None, "published": True}


def publish_telegram(client: HttpClient, target: dict[str, Any], content: str) -> dict[str, Any]:
    token = os.environ[require_string(target, "bot_token_env", "telegram target")]
    form: dict[str, Any] = {
        "chat_id": require_string(target, "chat_id", "telegram target"),
        "text": content,
        "disable_web_page_preview": str(bool(target.get("disable_web_page_preview", False))).lower(),
        "disable_notification": str(bool(target.get("disable_notification", False))).lower(),
    }
    if target.get("message_thread_id") is not None:
        form["message_thread_id"] = target["message_thread_id"]
    response = client.request("POST", f"https://api.telegram.org/bot{token}/sendMessage", form_body=form)
    data = parse_response_json(response, "Telegram")
    if not data.get("ok"):
        raise PublishError(f"Telegram rejected the message: {data.get('description', 'unknown error')}")
    message = data.get("result") or {}
    return {"remote_id": message.get("message_id"), "url": None, "published": True}


def publish_generic_webhook(client: HttpClient, target: dict[str, Any], content: str) -> dict[str, Any]:
    endpoint = os.environ[require_string(target, "endpoint_env", "generic webhook target")]
    field = str(target.get("content_field", "text"))
    payload: dict[str, Any] = {field: content}
    static = target.get("static_payload", {})
    if static:
        if not isinstance(static, dict):
            raise CampaignError("generic_webhook.static_payload must be an object")
        payload.update(static)
    response = client.request("POST", endpoint, json_body=payload)
    remote_id = None
    result_url = None
    if response.get("text"):
        try:
            data = json.loads(response["text"])
            if isinstance(data, dict):
                remote_id = data.get("id")
                result_url = data.get("url")
        except json.JSONDecodeError:
            pass
    return {"remote_id": remote_id, "url": result_url, "published": True}


def publish_target(
    client: HttpClient, prepared: dict[str, Any], campaign: dict[str, Any]
) -> dict[str, Any]:
    target, content = prepared["target"], prepared["content"]
    platform = target["platform"]
    if platform == "devto":
        return publish_devto(client, target, content, campaign)
    if platform == "hashnode":
        return publish_hashnode(client, target, content, campaign)
    if platform == "mastodon":
        return publish_mastodon(client, target, content, prepared["payload_hash"])
    if platform == "linkedin":
        return publish_linkedin(client, target, content)
    if platform == "discord":
        return publish_discord(client, target, content)
    if platform == "slack":
        return publish_slack(client, target, content)
    if platform == "telegram":
        return publish_telegram(client, target, content)
    if platform == "generic_webhook":
        return publish_generic_webhook(client, target, content)
    raise CampaignError(f"Platform is not API-publishable: {platform}")


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": SCHEMA_VERSION, "campaigns": {}}
    state = load_json(path)
    if state.get("schema_version") != SCHEMA_VERSION or not isinstance(state.get("campaigns"), dict):
        raise CampaignError(f"Invalid state file: {path}")
    return state


def render_queue(path: Path, campaign: dict[str, Any], prepared_targets: list[dict[str, Any]]) -> None:
    cards: list[str] = []
    for item in prepared_targets:
        target, content = item["target"], item["content"]
        title = str(target.get("title") or target.get("id"))
        publish_url = target.get("publish_url") if target["platform"] == "assisted" else None
        action = (
            f'<a class="open" target="_blank" rel="noreferrer" href="{html.escape(str(publish_url), quote=True)}">Open publish page</a>'
            if publish_url
            else '<span class="api">API target</span>'
        )
        cards.append(
            "<section>"
            f"<div class=\"meta\"><strong>{html.escape(title)}</strong> · {html.escape(target['platform'])} · {action}</div>"
            f"<pre>{html.escape(content)}</pre>"
            "<button type=\"button\" onclick=\"copyText(this)\">Copy content</button>"
            "</section>"
        )
    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Distribution queue — {html.escape(str(campaign['campaign_id']))}</title>
<style>
body{{font:15px/1.5 system-ui,sans-serif;max-width:980px;margin:32px auto;padding:0 18px;background:#0d1117;color:#e6edf3}}
section{{border:1px solid #30363d;border-radius:12px;padding:18px;margin:18px 0;background:#161b22}}
.meta{{margin-bottom:12px}} pre{{white-space:pre-wrap;background:#0d1117;padding:14px;border-radius:8px;max-height:360px;overflow:auto}}
button,.open{{display:inline-block;border:0;border-radius:7px;padding:8px 12px;background:#238636;color:white;text-decoration:none;cursor:pointer}}
.api{{color:#8c959f}}
</style></head><body>
<h1>Distribution queue</h1><p>Campaign: <code>{html.escape(str(campaign['campaign_id']))}</code>. This local page does not publish automatically.</p>
{''.join(cards)}
<script>async function copyText(button){{const text=button.parentElement.querySelector('pre').innerText;await navigator.clipboard.writeText(text);button.textContent='Copied';setTimeout(()=>button.textContent='Copy content',1200);}}</script>
</body></html>
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(document, encoding="utf-8", newline="\n")


def write_markdown_report(path: Path, summary: dict[str, Any]) -> None:
    lines = [
        f"# Distribution report — {summary['campaign_id']}",
        "",
        f"Mode: **{summary['mode']}**",
        "",
        "| Target | Platform | Status | Result |",
        "|---|---|---|---|",
    ]
    for result in summary["results"]:
        detail = result.get("url") or result.get("remote_id") or result.get("error") or "—"
        detail = str(detail).replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {result['id']} | {result['platform']} | {result['status']} | {detail} |")
    lines.extend(["", "No credentials are stored in this report.", ""])
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def execute_campaign(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    campaign = load_json(manifest_path)
    selected_ids = set(args.target) if args.target else None
    prepared_targets = validate_campaign(campaign, manifest_path.parent, selected_ids, args.allow_http)
    results_dir = Path(args.results_dir).resolve() if args.results_dir else manifest_path.parent / "distribution-results"
    results_dir.mkdir(parents=True, exist_ok=True)
    queue_path = results_dir / "publish-queue.html"
    render_queue(queue_path, campaign, prepared_targets)

    if args.open_assisted:
        for item in prepared_targets:
            target = item["target"]
            if target["platform"] == "assisted" and target.get("publish_url"):
                webbrowser.open(str(target["publish_url"]))

    all_env_names = [name for item in prepared_targets for name in item["credential_env_names"]]
    secrets = secret_values(all_env_names)
    mode = "execute" if args.execute else "dry-run"
    summary: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "script_version": SCRIPT_VERSION,
        "campaign_id": campaign["campaign_id"],
        "mode": mode,
        "results": [],
    }

    if not args.execute:
        for item in prepared_targets:
            target = item["target"]
            if not target.get("enabled", False):
                status = "disabled"
            elif target["platform"] == "assisted":
                status = "assisted"
            elif item["missing_credentials"]:
                status = "missing_credentials"
            else:
                status = "ready"
            summary["results"].append(
                {
                    "id": target["id"],
                    "platform": target["platform"],
                    "status": status,
                    "required_env": item["credential_env_names"],
                }
            )
        write_json_atomic(results_dir / "results.json", summary)
        write_markdown_report(results_dir / "REPORT.md", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        print(f"\nQueue: {queue_path}")
        return 0

    campaign_id = str(campaign["campaign_id"])
    if args.confirm != campaign_id:
        raise CampaignError(f"Live publishing requires --confirm {campaign_id}")
    enabled_api = [item for item in prepared_targets if item["target"].get("enabled", False) and item["target"]["platform"] in API_PLATFORMS]
    if len(enabled_api) > args.max_execute:
        raise CampaignError(f"Refusing to execute {len(enabled_api)} API targets; --max-execute is {args.max_execute}")
    missing_enabled = [
        f"{item['target']['id']}: {', '.join(item['missing_credentials'])}"
        for item in enabled_api
        if item["missing_credentials"]
    ]
    if missing_enabled:
        raise CampaignError(f"Enabled targets have missing environment variables: {'; '.join(missing_enabled)}")

    state_path = Path(args.state).resolve() if args.state else results_dir / "state.json"
    state = load_state(state_path)
    campaign_state = state["campaigns"].setdefault(campaign_id, {"targets": {}})
    target_states = campaign_state.setdefault("targets", {})
    changed_successes = [
        item["target"]["id"]
        for item in enabled_api
        if target_states.get(item["target"]["id"], {}).get("status") == "success"
        and target_states[item["target"]["id"]].get("payload_hash") != item["payload_hash"]
    ]
    if changed_successes and not args.allow_republish:
        raise CampaignError(
            "Successful target(s) contain changed content; use new target ids or --allow-republish: "
            + ", ".join(changed_successes)
        )
    client = HttpClient(args.timeout, args.retries, secrets, allow_http=args.allow_http)

    for item in prepared_targets:
        target = item["target"]
        result: dict[str, Any] = {"id": target["id"], "platform": target["platform"]}
        if not target.get("enabled", False):
            result["status"] = "disabled"
        elif target["platform"] == "assisted":
            result["status"] = "assisted"
        else:
            previous = target_states.get(target["id"], {})
            if previous.get("status") == "success" and previous.get("payload_hash") == item["payload_hash"]:
                result.update(status="skipped_duplicate", url=previous.get("url"), remote_id=previous.get("remote_id"))
            elif previous.get("status") == "success" and not args.allow_republish:
                result.update(status="failed", error="Target already succeeded with different content; use a new target id or --allow-republish")
            else:
                try:
                    published = sanitize_result(publish_target(client, item, campaign), secrets)
                    result.update(status="success", **published)
                    target_states[target["id"]] = {
                        "status": "success",
                        "payload_hash": item["payload_hash"],
                        "url": published.get("url"),
                        "remote_id": published.get("remote_id"),
                        "published_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    }
                    write_json_atomic(state_path, state)
                except (CampaignError, PublishError, KeyError) as exc:
                    result.update(status="failed", error=redact(str(exc), secrets))
        summary["results"].append(result)

    write_json_atomic(results_dir / "results.json", summary)
    write_markdown_report(results_dir / "REPORT.md", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"\nQueue: {queue_path}")
    failures = [result for result in summary["results"] if result["status"] == "failed"]
    return 2 if failures else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", help="Path to DISTRIBUTION_MANIFEST.json")
    parser.add_argument("--execute", action="store_true", help="Perform enabled API/Webhook mutations")
    parser.add_argument("--confirm", help="Exact campaign_id required with --execute")
    parser.add_argument("--target", action="append", help="Limit processing to a target id; repeat as needed")
    parser.add_argument("--results-dir", help="Output directory for queue, report, results, and default state")
    parser.add_argument("--state", help="Override the idempotency state file")
    parser.add_argument("--open-assisted", action="store_true", help="Open assisted publish pages after rendering the queue")
    parser.add_argument("--allow-republish", action="store_true", help="Allow a successful target id to publish changed content again")
    parser.add_argument("--max-execute", type=int, default=20, help="Maximum enabled API targets per run (default: 20)")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS, help="Request timeout in seconds")
    parser.add_argument("--retries", type=int, default=DEFAULT_RETRIES, help="Retries for 429 and 5xx responses")
    parser.add_argument("--allow-http", action="store_true", help="Allow HTTP endpoints; intended only for local testing")
    parser.add_argument("--version", action="version", version=SCRIPT_VERSION)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.max_execute < 1 or args.timeout < 1 or args.retries < 0:
        parser.error("max-execute and timeout must be positive; retries cannot be negative")
    if args.confirm and not args.execute:
        parser.error("--confirm is only valid with --execute")
    try:
        return execute_campaign(args)
    except CampaignError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
