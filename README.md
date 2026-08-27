# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img
    src="docs/assets/github-high-star-optimizer-readme-hero.png"
    alt="GitHub High-Star Optimizer workflow: Audit, Prepare, Apply, and Publish, with zero code changes."
  />
</p>

> A portable Agent Skill for turning an existing GitHub project into a clearer, credible, launch-ready repository—without changing product code. Structured for Codex, Claude Code, and other Agent Skills-compatible hosts.

[![Release](https://img.shields.io/github/v/release/jamesdffgy-source/github-high-star-optimizer)](https://github.com/jamesdffgy-source/github-high-star-optimizer/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

GitHub High-Star Optimizer improves the publishing surface of a real, existing project: repository naming and search positioning, README structure, evidence-safe visuals, metadata, release notes, localized introductions, and ethical launch materials. It does not promise Stars or manipulate engagement.

## What it optimizes

- **Naming and discovery:** evaluates task-language fit, current GitHub search samples, collision risk, metadata alignment, and rename cost.
- **Clarity:** audience, problem, outcome, differentiator, and one obvious next action.
- **Trust:** claims linked to repository evidence, explicit limitations, and real screenshots or output.
- **Presentation:** README Hero, Social Preview, release artwork, badges, and information hierarchy.
- **Distribution:** platform-native launch copy plus dry-run, approved API/Webhook delivery, assisted forum queues, idempotency, and result capture.
- **Safety:** no source-code, dependency, build, test, CI, runtime, or product-behavior changes.

## Four operating modes

| Mode | What happens | Repository mutation |
|---|---|---|
| **Audit** | Scores the existing publishing surface and prioritizes gaps. | None |
| **Prepare** | Creates a separate launch kit with proposed copy and assets. | None |
| **Apply** | Applies an explicitly approved allowlist of non-code publishing files. | Approved files only |
| **Publish** | Updates GitHub metadata/releases or delivers an approved external campaign through official APIs and authorized webhooks. | Explicitly authorized actions only |

## Quick start

### Codex

Ask the built-in installer:

```text
Use $skill-installer to install the skill from
https://github.com/jamesdffgy-source/github-high-star-optimizer/tree/main/github-high-star-optimizer
```

Then invoke it:

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

### Claude Code

Copy the inner [`github-high-star-optimizer`](github-high-star-optimizer) directory to `~/.claude/skills/github-high-star-optimizer` for personal use or `.claude/skills/github-high-star-optimizer` for project use. Then invoke:

```text
/github-high-star-optimizer Audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

See the complete [installation and verification guide](docs/INSTALLATION.md) for Codex, Claude Code, Windows, macOS/Linux, project-scoped setup, and other Agent Skills-compatible hosts.

Prepare a complete publishing package without touching the target repository:

```text
Use $github-high-star-optimizer in Prepare mode.
Create an evidence-backed README plan, GitHub metadata, release notes,
README Hero, Social Preview, and a 14-day relaunch package in a separate directory.
Do not invent product UI, features, users, metrics, or Star counts.
```

Prepare maintained localized introductions:

```text
Use $github-high-star-optimizer to prepare an English primary README and a
Simplified Chinese README. Keep commands, version numbers, claims, and
limitations consistent across both languages. Do not modify project code.
```

Evaluate whether a repository name is searchable and trustworthy:

```text
Use $github-high-star-optimizer in Audit mode to evaluate this repository name.
Sample current GitHub search queries, compare keep/rename candidates, and include
rename consequences. Do not rename the live repository.
```

Prepare a mostly automated external distribution campaign:

```text
Use $github-high-star-optimizer in Distribution Prepare mode.
Create platform-native posts and a dry-run manifest for DEV, Hashnode, Mastodon,
LinkedIn, and my authorized Discord, Slack, or Telegram destinations. Create an
assisted queue for rule-sensitive forums. Do not publish until I approve the
exact campaign ID and enabled destinations; never automate engagement.
```

The bundled standard-library publisher validates the package without network mutation by default:

```bash
python github-high-star-optimizer/scripts/distribution_publisher.py \
  /path/to/campaign/DISTRIBUTION_MANIFEST.json
```

After explicit campaign approval, live API/Webhook delivery requires both execution flags:

```bash
python github-high-star-optimizer/scripts/distribution_publisher.py \
  /path/to/campaign/DISTRIBUTION_MANIFEST.json \
  --execute --confirm exact-campaign-id
```

See [external distribution automation](github-high-star-optimizer/references/distribution-automation.md) for supported platforms, credential setup, safety gates, assisted forums, and result handling.

## Cross-agent compatibility

The canonical package follows the [Agent Skills specification](https://agentskills.io/specification). Codex and Claude Code use the same `SKILL.md`, references, and assets; only discovery paths and explicit invocation syntax differ. `agents/openai.yaml` supplies optional OpenAI UI metadata and is not required by the core workflow.

Compatibility with an Agent Skills format does not imply that every host provides GitHub access, image generation, browser control, or publishing permissions. The Skill falls back to a local audit or launch package when live capabilities are unavailable.

The deterministic distribution publisher requires Python 3.10+ and only uses the standard library. A host without shell access can still generate the manifest and platform copy, but cannot run the bundled publisher directly.

## Evidence and visual rules

Every material claim must come from repository files, releases, demos, issues, user-provided facts, or a clearly labeled inference. Generated visuals may provide brand framing or explanation, but they must not fabricate a product interface, command output, benchmark, integration, customer, feature, or popularity metric.

The bundled visual set follows that rule: it depicts the documented four-mode workflow and the verified no-code-change boundary, not a fictional product screen.

## Multilingual publishing

The Skill can produce a canonical README plus maintained localized versions for the project’s real audiences. Language links remain symmetric; commands, paths, identifiers, version numbers, shipped claims, and limitations remain equivalent. A translation is not allowed to strengthen a claim that the canonical language cannot support.

See [`references/multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md) for the localization workflow.

The current locale set and human-review status are recorded in [`docs/LOCALIZATION.md`](docs/LOCALIZATION.md).

## Repository structure

- [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md) — operating modes, boundaries, workflow, and handoff rules.
- [`github-high-star-optimizer/scripts`](github-high-star-optimizer/scripts) — dependency-free campaign dry-run, approved API/Webhook delivery, idempotency, and result capture.
- [`github-high-star-optimizer/references`](github-high-star-optimizer/references) — publishing rubric, naming/search, cross-agent compatibility, distribution automation, visuals, multilingual publishing, releases, evidence, and policy research.
- [`github-high-star-optimizer/assets`](github-high-star-optimizer/assets) — reusable audit, naming, distribution manifest, README, release, launch-kit, Social Preview, and image-generation templates.
- [`github-high-star-optimizer/tests`](github-high-star-optimizer/tests) — local behavior tests using only simulated HTTP endpoints.
- [`docs/INSTALLATION.md`](docs/INSTALLATION.md) — Codex, Claude Code, and portable Agent Skills installation and verification.
- [`docs/assets`](docs/assets) — final README, Social Preview, and release artwork.

## Non-goals

This Skill does not modify target-project code, dependencies, builds, tests, CI, runtime configuration, APIs, storage, telemetry, permissions, or security controls. Delivery automation is limited to explicitly approved content and destinations; paid Stars, star-for-star rings, automated engagement, reward-gated Stars, fake users, fake testimonials, and guaranteed-ranking claims remain prohibited.

## License

[MIT](LICENSE)

---

If this project is useful, you can Star it to find it again and help relevant users discover it.
