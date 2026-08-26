# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img
    src="docs/assets/github-high-star-optimizer-readme-hero.png"
    alt="GitHub High-Star Optimizer workflow: Audit, Prepare, Apply, and Publish, with zero code changes."
  />
</p>

> A Codex Skill for turning an existing GitHub project into a clearer, credible, launch-ready repository—without changing product code.

[![Release](https://img.shields.io/github/v/release/jamesdffgy-source/github-high-star-optimizer)](https://github.com/jamesdffgy-source/github-high-star-optimizer/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

GitHub High-Star Optimizer improves the publishing surface of a real, existing project: positioning, README structure, evidence-safe visuals, repository metadata, release notes, localized introductions, and ethical launch materials. It does not promise Stars or manipulate engagement.

## What it optimizes

- **Clarity:** audience, problem, outcome, differentiator, and one obvious next action.
- **Trust:** claims linked to repository evidence, explicit limitations, and real screenshots or output.
- **Presentation:** README Hero, Social Preview, release artwork, badges, and information hierarchy.
- **Distribution:** GitHub metadata, release notes, localized launch copy, and a measured relaunch sequence.
- **Safety:** no source-code, dependency, build, test, CI, runtime, or product-behavior changes.

## Four operating modes

| Mode | What happens | Repository mutation |
|---|---|---|
| **Audit** | Scores the existing publishing surface and prioritizes gaps. | None |
| **Prepare** | Creates a separate launch kit with proposed copy and assets. | None |
| **Apply** | Applies an explicitly approved allowlist of non-code publishing files. | Approved files only |
| **Publish** | Updates GitHub metadata, releases, or external launch surfaces after authorization. | Explicitly authorized actions only |

## Quick start

1. Clone this repository.
2. Copy the inner [`github-high-star-optimizer`](github-high-star-optimizer) directory into the skills directory configured for your Codex environment.
3. Invoke the Skill with a real repository or local workspace in scope.

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

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

## Evidence and visual rules

Every material claim must come from repository files, releases, demos, issues, user-provided facts, or a clearly labeled inference. Generated visuals may provide brand framing or explanation, but they must not fabricate a product interface, command output, benchmark, integration, customer, feature, or popularity metric.

The bundled visual set follows that rule: it depicts the documented four-mode workflow and the verified no-code-change boundary, not a fictional product screen.

## Multilingual publishing

The Skill can produce a canonical README plus maintained localized versions for the project’s real audiences. Language links remain symmetric; commands, paths, identifiers, version numbers, shipped claims, and limitations remain equivalent. A translation is not allowed to strengthen a claim that the canonical language cannot support.

See [`references/multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md) for the localization workflow.

The current locale set and human-review status are recorded in [`docs/LOCALIZATION.md`](docs/LOCALIZATION.md).

## Repository structure

- [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md) — operating modes, boundaries, workflow, and handoff rules.
- [`github-high-star-optimizer/references`](github-high-star-optimizer/references) — publishing rubric, README and visual guidance, multilingual publishing, releases, evidence, and policy research.
- [`github-high-star-optimizer/assets`](github-high-star-optimizer/assets) — reusable audit, README, release, launch-kit, Social Preview, and image-generation templates.
- [`docs/assets`](docs/assets) — final README, Social Preview, and release artwork.

## Non-goals

This Skill does not modify application code, dependencies, builds, tests, CI, runtime configuration, APIs, storage, telemetry, permissions, or security controls. It also rejects paid Stars, star-for-star rings, automated engagement, reward-gated Stars, fake users, fake testimonials, and guaranteed-ranking claims.

## License

[MIT](LICENSE)

---

If this project is useful, you can Star it to find it again and help relevant users discover it.
