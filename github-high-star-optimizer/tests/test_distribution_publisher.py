from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import threading
import unittest
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest import mock


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "distribution_publisher.py"
SPEC = importlib.util.spec_from_file_location("distribution_publisher", SCRIPT_PATH)
assert SPEC and SPEC.loader
publisher = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(publisher)


class FakeClient:
    def __init__(self, responses: list[dict[str, object]]) -> None:
        self.responses = list(responses)
        self.calls: list[tuple[str, str, dict[str, object]]] = []

    def request(self, method: str, url: str, **kwargs: object) -> dict[str, object]:
        self.calls.append((method, url, kwargs))
        return self.responses.pop(0)


class RecordingHandler(BaseHTTPRequestHandler):
    requests: list[dict[str, object]] = []
    response_status = 200
    response_statuses: list[int] = []
    response_body = b'{"id":"remote-1","url":"https://example.test/post/1"}'

    def do_POST(self) -> None:  # noqa: N802
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        type(self).requests.append({"path": self.path, "headers": dict(self.headers), "body": body})
        status = type(self).response_statuses.pop(0) if type(self).response_statuses else type(self).response_status
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(type(self).response_body)

    def log_message(self, _format: str, *_args: object) -> None:
        return


@contextmanager
def recording_server(status: int = 200, body: bytes | None = None, statuses: list[int] | None = None):
    RecordingHandler.requests = []
    RecordingHandler.response_status = status
    RecordingHandler.response_statuses = list(statuses or [])
    RecordingHandler.response_body = body or b'{"id":"remote-1","url":"https://example.test/post/1"}'
    server = ThreadingHTTPServer(("127.0.0.1", 0), RecordingHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/publish"
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()


class DistributionPublisherTests(unittest.TestCase):
    def create_campaign(self, root: Path, endpoint_env: str = "TEST_WEBHOOK_URL") -> Path:
        (root / "content.md").write_text("Truthful launch content", encoding="utf-8")
        manifest = {
            "schema_version": 1,
            "campaign_id": "test-campaign",
            "canonical_url": "https://github.com/example/repo",
            "targets": [
                {
                    "id": "webhook-one",
                    "platform": "generic_webhook",
                    "enabled": True,
                    "endpoint_env": endpoint_env,
                    "content_field": "text",
                    "content_file": "content.md",
                }
            ],
        }
        path = root / "manifest.json"
        path.write_text(json.dumps(manifest), encoding="utf-8")
        return path

    def test_dry_run_never_contacts_endpoint(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir, recording_server() as endpoint:
            root = Path(temp_dir)
            manifest = self.create_campaign(root)
            with mock.patch.dict(os.environ, {"TEST_WEBHOOK_URL": endpoint}, clear=False):
                exit_code = publisher.main([str(manifest), "--allow-http"])
            self.assertEqual(exit_code, 0)
            self.assertEqual(RecordingHandler.requests, [])
            results = json.loads((root / "distribution-results" / "results.json").read_text(encoding="utf-8"))
            self.assertEqual(results["results"][0]["status"], "ready")
            self.assertNotIn(endpoint, json.dumps(results))

    def test_execute_posts_once_and_then_skips_duplicate(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir, recording_server() as endpoint:
            root = Path(temp_dir)
            manifest = self.create_campaign(root)
            args = [str(manifest), "--allow-http", "--execute", "--confirm", "test-campaign", "--retries", "0"]
            with mock.patch.dict(os.environ, {"TEST_WEBHOOK_URL": endpoint}, clear=False):
                first = publisher.main(args)
                second = publisher.main(args)
            self.assertEqual(first, 0)
            self.assertEqual(second, 0)
            self.assertEqual(len(RecordingHandler.requests), 1)
            payload = json.loads(RecordingHandler.requests[0]["body"].decode("utf-8"))
            self.assertEqual(payload["text"], "Truthful launch content")
            results = json.loads((root / "distribution-results" / "results.json").read_text(encoding="utf-8"))
            self.assertEqual(results["results"][0]["status"], "skipped_duplicate")

    def test_confirmation_must_match_campaign(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = self.create_campaign(root)
            with mock.patch.dict(os.environ, {"TEST_WEBHOOK_URL": "https://example.test/hook"}, clear=False):
                exit_code = publisher.main([str(manifest), "--execute", "--confirm", "wrong-campaign"])
            self.assertEqual(exit_code, 2)

    def test_missing_enabled_credential_stops_before_any_request(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir, recording_server() as endpoint:
            root = Path(temp_dir)
            manifest_path = self.create_campaign(root)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["targets"].append(
                {
                    "id": "missing-webhook",
                    "platform": "generic_webhook",
                    "enabled": True,
                    "endpoint_env": "MISSING_TEST_WEBHOOK",
                    "content_file": "content.md",
                }
            )
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            environment = {"TEST_WEBHOOK_URL": endpoint}
            with mock.patch.dict(os.environ, environment, clear=False):
                os.environ.pop("MISSING_TEST_WEBHOOK", None)
                exit_code = publisher.main(
                    [str(manifest_path), "--allow-http", "--execute", "--confirm", "test-campaign", "--retries", "0"]
                )
            self.assertEqual(exit_code, 2)
            self.assertEqual(RecordingHandler.requests, [])

    def test_enabled_manifest_placeholder_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest_path = self.create_campaign(root)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["targets"][0]["static_payload"] = {"channel": "replace-with-channel"}
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            with mock.patch.dict(os.environ, {"TEST_WEBHOOK_URL": "https://example.test/hook"}, clear=False):
                exit_code = publisher.main([str(manifest_path)])
            self.assertEqual(exit_code, 2)

    def test_changed_successful_target_requires_republish_flag(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir, recording_server() as endpoint:
            root = Path(temp_dir)
            manifest = self.create_campaign(root)
            args = [str(manifest), "--allow-http", "--execute", "--confirm", "test-campaign", "--retries", "0"]
            with mock.patch.dict(os.environ, {"TEST_WEBHOOK_URL": endpoint}, clear=False):
                self.assertEqual(publisher.main(args), 0)
                (root / "content.md").write_text("Changed launch content", encoding="utf-8")
                self.assertEqual(publisher.main(args), 2)
            self.assertEqual(len(RecordingHandler.requests), 1)
            state = json.loads((root / "distribution-results" / "state.json").read_text(encoding="utf-8"))
            saved = state["campaigns"]["test-campaign"]["targets"]["webhook-one"]
            self.assertEqual(saved["status"], "success")

    def test_secret_is_redacted_from_failure_results(self) -> None:
        secret_endpoint = "https://hooks.slack.com/services/T/B/SUPERSECRET"
        redacted = publisher.redact(f"failed at {secret_endpoint}", [secret_endpoint])
        self.assertNotIn("SUPERSECRET", redacted)
        self.assertIn("REDACTED", redacted)

    def test_retryable_server_error_is_bounded_and_recovers(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir, recording_server(statuses=[500, 200]) as endpoint:
            root = Path(temp_dir)
            manifest = self.create_campaign(root)
            args = [
                str(manifest),
                "--allow-http",
                "--execute",
                "--confirm",
                "test-campaign",
                "--retries",
                "1",
            ]
            with mock.patch.dict(os.environ, {"TEST_WEBHOOK_URL": endpoint}, clear=False), mock.patch.object(publisher.time, "sleep"):
                exit_code = publisher.main(args)
            self.assertEqual(exit_code, 0)
            self.assertEqual(len(RecordingHandler.requests), 2)

    def test_http_runtime_endpoint_is_rejected_without_test_override(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = self.create_campaign(root)
            with mock.patch.dict(os.environ, {"TEST_WEBHOOK_URL": "http://127.0.0.1:9/publish"}, clear=False):
                exit_code = publisher.main([str(manifest), "--execute", "--confirm", "test-campaign", "--retries", "0"])
            self.assertEqual(exit_code, 2)
            results = json.loads((root / "distribution-results" / "results.json").read_text(encoding="utf-8"))
            self.assertIn("absolute HTTPS URL", results["results"][0]["error"])

    def test_content_path_cannot_escape_campaign(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            outside = root.parent / "outside-distribution-test.md"
            outside.write_text("outside", encoding="utf-8")
            try:
                manifest = {
                    "schema_version": 1,
                    "campaign_id": "escape-test",
                    "canonical_url": "https://example.test/project",
                    "targets": [
                        {
                            "id": "escape",
                            "platform": "assisted",
                            "enabled": True,
                            "publish_url": "https://example.test/submit",
                            "content_file": f"../{outside.name}",
                        }
                    ],
                }
                path = root / "manifest.json"
                path.write_text(json.dumps(manifest), encoding="utf-8")
                self.assertEqual(publisher.main([str(path)]), 2)
            finally:
                outside.unlink(missing_ok=True)

    def test_assisted_queue_escapes_content(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "post.md").write_text("<script>alert('x')</script>", encoding="utf-8")
            manifest = {
                "schema_version": 1,
                "campaign_id": "assisted-test",
                "canonical_url": "https://example.test/project",
                "targets": [
                    {
                        "id": "forum",
                        "platform": "assisted",
                        "enabled": True,
                        "publish_url": "https://example.test/submit",
                        "content_file": "post.md",
                    }
                ],
            }
            path = root / "manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertEqual(publisher.main([str(path)]), 0)
            queue = (root / "distribution-results" / "publish-queue.html").read_text(encoding="utf-8")
            self.assertNotIn("<script>alert", queue)
            self.assertIn("&lt;script&gt;", queue)

    def test_article_adapters_build_expected_official_payloads(self) -> None:
        client = FakeClient(
            [
                {"status": 201, "text": '{"id":7,"url":"https://dev.to/example/post"}', "headers": {}},
                {
                    "status": 200,
                    "text": '{"data":{"publishPost":{"post":{"id":"h1","url":"https://hashnode.test/post"}}}}',
                    "headers": {},
                },
            ]
        )
        campaign = {"canonical_url": "https://github.com/example/repo"}
        with mock.patch.dict(os.environ, {"DEV_KEY": "dev-secret", "HASH_TOKEN": "hash-secret"}, clear=False):
            dev_result = publisher.publish_devto(
                client,
                {
                    "api_key_env": "DEV_KEY",
                    "title": "Launch",
                    "tags": ["github"],
                    "publish": True,
                    "ai_disclosure_level": "some_ai",
                },
                "DEV body",
                campaign,
            )
            hash_result = publisher.publish_hashnode(
                client,
                {
                    "token_env": "HASH_TOKEN",
                    "publication_id": "publication-1",
                    "title": "Launch",
                    "tags": ["github"],
                },
                "Hashnode body",
                campaign,
            )
        self.assertEqual(dev_result["remote_id"], 7)
        dev_payload = client.calls[0][2]["json_body"]
        self.assertEqual(dev_payload["article"]["canonical_url"], campaign["canonical_url"])
        self.assertEqual(dev_payload["article"]["tags"], "github")
        self.assertEqual(dev_payload["article"]["ai_disclosure_level"], "some_ai")
        self.assertEqual(client.calls[0][2]["headers"]["api-key"], "dev-secret")
        self.assertEqual(hash_result["remote_id"], "h1")
        self.assertEqual(client.calls[1][1], "https://gql-beta.hashnode.com/")
        hash_payload = client.calls[1][2]["json_body"]
        self.assertEqual(hash_payload["variables"]["input"]["publicationId"], "publication-1")
        self.assertIn("publishPost", hash_payload["query"])

    def test_social_adapters_build_expected_payloads(self) -> None:
        client = FakeClient(
            [
                {"status": 200, "text": '{"id":"m1","url":"https://social.example/@me/1"}', "headers": {}},
                {"status": 201, "text": "", "headers": {"x-restli-id": "urn:li:share:1"}},
                {
                    "status": 200,
                    "text": '{"ok":true,"result":{"message_id":42}}',
                    "headers": {},
                },
            ]
        )
        with mock.patch.dict(
            os.environ,
            {
                "MASTO_TOKEN": "masto-secret",
                "LI_TOKEN": "li-secret",
                "LI_VERSION": "202604",
                "TG_TOKEN": "tg-secret",
            },
            clear=False,
        ):
            mastodon = publisher.publish_mastodon(
                client,
                {"access_token_env": "MASTO_TOKEN", "instance_url": "https://social.example", "visibility": "public"},
                "Mastodon post",
                "payload-hash",
            )
            linkedin = publisher.publish_linkedin(
                client,
                {"access_token_env": "LI_TOKEN", "api_version_env": "LI_VERSION", "author": "urn:li:person:1"},
                "LinkedIn post",
            )
            telegram = publisher.publish_telegram(
                client,
                {"bot_token_env": "TG_TOKEN", "chat_id": "@channel"},
                "Telegram post",
            )
        self.assertEqual(mastodon["remote_id"], "m1")
        self.assertEqual(client.calls[0][2]["headers"]["Idempotency-Key"], "payload-hash")
        self.assertEqual(linkedin["remote_id"], "urn:li:share:1")
        self.assertEqual(client.calls[1][2]["headers"]["Linkedin-Version"], "202604")
        self.assertEqual(telegram["remote_id"], 42)
        self.assertIn("tg-secret", client.calls[2][1])

    def test_authorized_webhook_adapters_disable_mentions_and_preserve_content(self) -> None:
        client = FakeClient(
            [
                {
                    "status": 200,
                    "text": '{"id":"d1","guild_id":"g1","channel_id":"c1"}',
                    "headers": {},
                },
                {"status": 200, "text": "ok", "headers": {}},
            ]
        )
        with mock.patch.dict(
            os.environ,
            {"DISCORD_HOOK": "https://discord.com/api/webhooks/1/token", "SLACK_HOOK": "https://hooks.slack.com/services/T/B/C"},
            clear=False,
        ):
            discord = publisher.publish_discord(client, {"webhook_env": "DISCORD_HOOK"}, "Discord post")
            slack = publisher.publish_slack(client, {"webhook_env": "SLACK_HOOK"}, "Slack post")
        self.assertEqual(discord["url"], "https://discord.com/channels/g1/c1/d1")
        self.assertEqual(client.calls[0][2]["json_body"]["allowed_mentions"], {"parse": []})
        self.assertTrue(slack["published"])
        self.assertEqual(client.calls[1][2]["json_body"], {"text": "Slack post"})


if __name__ == "__main__":
    unittest.main()
