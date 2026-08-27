# External distribution automation

Read this reference completely when the user asks to promote, cross-post, distribute, announce, or publish a project outside GitHub.

Sources and endpoint shapes were reviewed on 2026-08-27. Platform APIs, permissions, pricing, versions, and community rules change. Verify the current official documentation before enabling a live target.

## Outcome

Minimize repeated manual work while keeping one truthful campaign source, platform-native copy, explicit authorization, and a result ledger. Automation applies to content delivery, not engagement: never automate votes, Stars, follows, reviews, comments, account creation, CAPTCHA bypass, or community-rule evasion.

## Distribution modes

Use the narrowest mode that satisfies the request:

1. **Distribution Prepare** — create a separate campaign directory, content variants, manifest, and local queue. Do not contact external platforms.
2. **Distribution Preflight** — run the publisher without `--execute`. Validate files, limits, enabled targets, and credential environment-variable presence. No network mutation occurs.
3. **Distribution Publish** — after the user explicitly approves the named campaign and targets, run enabled official API/Webhook targets with the exact campaign confirmation. Assisted targets remain non-mutating.
4. **Distribution Report** — return remote IDs/URLs, failures, duplicate skips, and remaining assisted targets. Do not treat a successful HTTP request as audience success.

An instruction such as “prepare posts” authorizes only Prepare. An instruction such as “publish this approved campaign to the enabled targets” can authorize Publish. Never reuse approval for a different campaign ID, changed payload, account, community, or destination.

## Deterministic publisher

Use [`scripts/distribution_publisher.py`](../scripts/distribution_publisher.py) for repeated preflight and API delivery. It requires Python 3.10+ and uses only the standard library.

Dry-run is the default:

```bash
python scripts/distribution_publisher.py /path/to/campaign/DISTRIBUTION_MANIFEST.json
```

Live delivery requires both flags:

```bash
python scripts/distribution_publisher.py /path/to/campaign/DISTRIBUTION_MANIFEST.json \
  --execute --confirm exact-campaign-id
```

Useful controls:

- `--target <id>` limits a run; repeat the flag for several targets.
- `--open-assisted` opens the prepared manual submission pages after rendering the local queue.
- `--max-execute <n>` caps API mutations in one run; the default is 20.
- `--allow-republish` is required to reuse a successful target ID with changed content. Prefer a new target ID instead.
- `--allow-http` exists only for local tests. Live endpoint and canonical URLs must use HTTPS.

The command writes `distribution-results/results.json`, `REPORT.md`, `publish-queue.html`, and an idempotency `state.json`. A successful target with the same payload hash is skipped on later runs. Credentials are never written to these files.

## Campaign package

Copy [`assets/DISTRIBUTION_MANIFEST.template.json`](../assets/DISTRIBUTION_MANIFEST.template.json) into the separate launch package as `DISTRIBUTION_MANIFEST.json`, then create every referenced content file.

Rules:

- `campaign_id` is a stable lowercase identifier for this exact campaign.
- `canonical_url` is the final direct project or release URL.
- each target ID is stable and unique;
- `enabled: true` means the user selected that destination, not that the platform approved the content;
- credential fields contain environment-variable names, never tokens or webhook URLs;
- content files must stay inside the campaign directory;
- platform copy must reflect the repository evidence sheet and relevant community norms;
- links, titles, tags, language, account, channel, subreddit, and node must be visible before execution.

## Supported API targets

| Platform | Delivery | Required environment/config | Notes |
|---|---|---|---|
| DEV / Forem | `POST /api/articles` | `api_key_env`, title, content, up to four tags | Can create a draft when `publish` is false; set the current AI-disclosure value when applicable. |
| Hashnode | `https://gql-beta.hashnode.com/` GraphQL `publishPost` | PAT, Pro publication ID, title, content | Current write mutations require an active Pro publication and an authorized role. |
| Mastodon | `POST /api/v1/statuses` | instance URL and access token | Supports visibility, language, scheduling, and idempotency key. Instance limits vary. |
| LinkedIn | Posts API | access token, current API-version environment variable, author URN | Permissions differ for people and organizations; verify current access before enabling. |
| Discord | Incoming Webhook | authorized channel webhook | Only post to a channel the user controls or has permission to automate. Mentions are disabled. |
| Slack | Incoming Webhook | authorized channel webhook | The webhook is bound to an authorized workspace/channel and must remain secret. |
| Telegram | Bot API `sendMessage` | bot token and authorized chat/channel ID | The bot must already be permitted to post in the destination. |
| Generic webhook | JSON POST | approved endpoint environment variable | Use only for a service the user owns or explicitly authorized. |

Official references:

- [Forem API](https://developers.forem.com/api/)
- [Hashnode official GraphQL Agent Skill](https://github.com/Hashnode/gql-skill)
- [Mastodon statuses API](https://docs.joinmastodon.org/methods/statuses/)
- [LinkedIn Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api)
- [Discord incoming webhooks](https://docs.discord.com/developers/platform/webhooks)
- [Slack incoming webhooks](https://api.slack.com/messaging/webhooks)
- [Telegram Bot API](https://core.telegram.org/bots/api/#sendmessage)

## Assisted targets

Use `platform: assisted` where a stable official publishing API is absent, account/community judgment is essential, or direct automation would create disproportionate spam risk. The script creates a local copy/open dashboard and can open the exact submission pages, but it does not click the final submit control.

Default assisted channels include Product Hunt, Hacker News, Reddit communities, V2EX nodes, Juejin, Zhihu, SegmentFault, Indie Hackers, Lobsters, and third-party Discord/Slack communities without an authorized webhook.

When the current host has browser control, reduce manual work further:

1. confirm the visible signed-in account and exact destination;
2. re-read the current platform and community rules;
3. fill the approved title, body, tags/flair/node, link, and image from the campaign package;
4. show the final rendered preview;
5. stop before the final submit control unless the user explicitly authorized that exact draft and destination;
6. after an authorized submit, capture the permanent post URL in the result ledger.

Process assisted destinations one at a time. Never bypass CAPTCHA, account checks, posting limits, moderation prompts, or a form whose destination/content differs from the approved preview.

Before enabling an assisted community target, record:

- current rule URL and review date;
- whether self-promotion and direct links are allowed;
- required title prefix, flair, node, tag, or disclosure;
- account-age, karma, reputation, or onboarding requirement;
- whether a canonical article should be summarized rather than duplicated;
- exact destination and why its audience fits.

Product Hunt currently requires a personal account and encourages community preparation; do not ask users directly for an upvote. Hacker News advises becoming a real contributor and posting an occasional `Show HN`. Reddit developer terms prohibit spam and abusive automation, and each community can impose stricter rules.

- [Product Hunt launch guide](https://www.producthunt.com/launch)
- [Show HN guidelines](https://news.ycombinator.com/showhn.html)
- [Reddit developer terms](https://redditinc.com/policies/developer-terms)

## Preflight checklist

Before live execution, show a compact table with:

- campaign ID and canonical URL;
- enabled target ID, platform, account/channel/community, and language;
- title or first line, character limit status, and content-file path;
- required environment-variable names and whether each is present;
- delivery type: API, webhook, or assisted;
- whether the payload has already succeeded according to `state.json`.

Stop before execution if any target has an unsupported claim, unresolved placeholder, missing credential, uncertain community permission, secret in a file, non-HTTPS live endpoint, or changed successful payload without deliberate republish authorization.

## Result handling

- Continue independent targets after one platform fails; do not retry non-retryable 4xx errors.
- Retry 429 and 5xx responses only a small bounded number of times and respect `Retry-After`.
- Save state after every successful target so interruption does not duplicate earlier posts.
- Redact credential values and secret-bearing webhook URLs from console output and reports.
- Return the platform response ID/URL when available; mark missing URLs rather than inventing them.
- Keep assisted targets visible in the report until the user confirms their final post URL.
- Measure visits, useful replies, installation attempts, and issue quality separately from vanity engagement.
