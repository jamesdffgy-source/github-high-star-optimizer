---
name: github-high-star-optimizer
description: Audit and optimize an existing GitHub repository's public presentation and release package for organic star growth—positioning, README, evidence-safe generated visuals, repository metadata, release notes, community documents, and launch copy—without changing source code, dependencies, builds, tests, CI, or runtime behavior. Use when a user asks to make a repository star-ready, improve its GitHub presentation, generate repository launch images, or prepare/relaunch an existing project.
---

# GitHub High-Star Optimizer

Turn a real, existing project into a clear, credible, visually compelling, release-ready GitHub repository. Optimize how the project is understood, trusted, tried, and shared; do not manufacture popularity or modify how the software works.

## Hard scope boundary

Never modify:

- application, library, model, or infrastructure source code;
- tests, dependencies, manifests, lockfiles, build scripts, CI workflows, runtime configuration, or generated code;
- product behavior, APIs, storage, telemetry, permissions, or security controls.

Do not describe code changes as recommendations unless the user separately asks for a code/product review. If a publishing claim would require a code change, mark it as blocked and omit the claim.

The allowed publishing surface, subject to the user's authorization, is:

- repository name suggestion, About description, homepage, Topics, and Social Preview brief;
- `README*`, documentation landing copy, screenshots/GIF storyboards, demo copy, badges, link organization, and non-code launch image assets;
- localized README introductions, language navigation, and multilingual release/launch copy that preserve the canonical claims;
- release title/notes, changelog prose, migration announcement, and launch calendar;
- `CONTRIBUTING`, `SUPPORT`, `SECURITY`, `CODE_OF_CONDUCT`, Issue/PR templates, governance/roadmap copy, only when requested and treated as real policy commitments;
- channel-native announcement drafts and ethical outreach plans.

Do not select or replace a software license, invent a security contact, add a funding destination, or make a governance promise without explicit user input. Draft these items with clearly marked placeholders.

## Integrity rules

- Never buy, automate, exchange, or reward Stars, votes, follows, reviews, or comments.
- Never propose giveaways, credits, tokens, access, or downloads conditioned on a Star.
- Never fabricate users, company logos, testimonials, benchmarks, download counts, security status, compatibility, roadmap completion, or maintenance activity.
- Treat all unsupported claims as unverified. Either cite repository evidence, ask the user for proof, or remove/qualify the claim.
- Star count is an attention signal, not proof of adoption or quality. Pair it with honest usage and community metrics.
- Do not promise a Star count, GitHub Trending placement, Product Hunt rank, or launch outcome.
- Do not post, send messages, change live repository settings, publish a release, or edit the target repository unless the user authorized that mutation. Preparing local drafts is not authorization to publish them.

## Select the operating mode

Infer the narrowest mode that satisfies the request:

1. **Audit** — read-only. Score the current publishing surface, identify evidence-backed gaps, and propose priorities. Use this for “review,” “analyze,” or “how can this repo get more Stars?”
2. **Prepare** — create a separate local launch kit containing proposed copy and assets; leave the target repository untouched. Use when the user wants drafts, options, or a plan.
3. **Apply** — edit only the explicitly approved non-code publishing files in the target repository. Before editing, list the allowed files; after editing, verify the diff contains no out-of-scope files.
4. **Publish** — mutate GitHub metadata, create/publish a release, or post externally only when the user explicitly requests that action and the required tool/account is available. Show the final payload and obtain any approval required by the environment immediately before the mutation.

When the request is ambiguous, default to **Prepare**, not Apply or Publish.

## Workflow

### 1. Inspect the existing project read-only

Identify the repository root or GitHub URL. Inspect only what is needed to understand the public product:

- existing README/localizations, docs entry pages, screenshots, logo, demo, releases, changelog, community files, license identity, and repository metadata;
- package/manifests only to verify the project name, supported environment, current install command, and links—never edit them;
- public Issues/Discussions and release history when they help reveal audience language, recurring confusion, or real proof.

Record unknowns instead of guessing. Preserve working copy, repository conventions, localization choices, existing user changes, and unrelated dirty files.

### 2. Build the evidence sheet

Extract five facts before writing promotional copy:

- primary audience;
- painful situation or desired outcome;
- demonstrated result;
- defensible differentiator;
- proof and limitations.

For every proposed headline or claim, retain a traceable source: repository file, release, demo, Issue, user-provided fact, or clearly labeled inference. Do not infer adoption from Stars.

### 3. Score and prioritize

For any audit or full optimization, read [references/audit-rubric.md](references/audit-rubric.md) completely and apply its 100-point publishing-only rubric. Code quality must not affect the score.

Use priorities:

- **P0 — release blocker:** misleading claim, broken primary link, missing/ambiguous license display, non-working documented install path, absent project identity, inaccessible core demo, policy placeholder presented as real.
- **P1 — conversion blocker:** unclear audience/value, no visible result, Quickstart buried, weak proof, missing metadata/social preview, release notes without user value.
- **P2 — compounding improvement:** localization, comparison page, contributor stories, content repurposing, additional channel, measurement refinement.

Do not start broad distribution while P0 items remain.

### 4. Create the publishing package

Read only the references relevant to the requested outputs:

- For README, screenshots, badges, Social Preview, or bilingual structure, read [references/readme-and-visuals.md](references/readme-and-visuals.md).
- For visual direction, image generation, screenshot treatment, or style selection, read [references/visual-style-library.md](references/visual-style-library.md) completely. Use [assets/IMAGE_GENERATION_BRIEF.template.md](assets/IMAGE_GENERATION_BRIEF.template.md) for each generated asset.
- For repository metadata, community surface, release notes, relaunch sequencing, or channel copy, read [references/release-and-distribution.md](references/release-and-distribution.md).
- For localized README introductions, language navigation, multilingual release notes, or broad language coverage, read [references/multilingual-publishing.md](references/multilingual-publishing.md) completely.
- For platform rules, research claims, fake-Star boundaries, and source quality, read [references/evidence-and-policies.md](references/evidence-and-policies.md).

Use the matching files in `assets/` as output scaffolds; replace every placeholder or leave it visibly marked for user completion. Do not copy an asset into the target repository if the user requested only an audit or preview.

A full Prepare result normally contains:

- current-state audit and prioritized gap list;
- three evidence-safe positioning options with one recommended option;
- repository About description, homepage recommendation, and 8–15 relevant Topic suggestions;
- README rewrite or section-level patch plan;
- screenshot/GIF storyboard, visual direction, image-generation brief, and 1280×640 Social Preview brief or generated draft;
- release title and release notes draft;
- a canonical-language manifest and localized introductions when multilingual publishing is requested;
- channel-native launch drafts for only the audiences that match the project;
- 14-day relaunch calendar and measurement baseline;
- claim/evidence ledger and a list of decisions requiring the user.

Avoid producing every artifact when a smaller request only needs one or two.

### 4a. Generate visuals without inventing the product

When actual raster image generation is requested and an image-generation tool is available:

- classify the asset as **proof**, **brand**, or **explanation** before generating;
- use real repository or user-provided screenshots/output as the source of truth for proof assets;
- inspect every local reference image before editing or compositing it;
- generate decorative backgrounds, framing, lighting, texture, illustration, or launch-card composition around real proof, but never hallucinate a product UI, command output, benchmark, integration, customer, or shipped feature;
- prefer deterministic SVG/diagram tools for exact architecture, labels, or technical flows; do not use a raster generator when exact structure matters;
- preserve existing logos and brand systems unless the user explicitly requests concept exploration; never silently replace a logo;
- generate into the separate launch kit in Prepare mode, use versioned filenames, and do not link or copy the asset into the target repository until Apply is authorized;
- if the tool cannot reliably render required text, generate a text-free base and use a deterministic layout tool when available; otherwise visually verify every character and reject incorrect variants;
- if no image-generation tool is available, deliver the complete prompt and asset brief instead of pretending an image was produced.

Do not generate a generic decorative hero merely because the README feels empty. A new project without real visual proof usually needs a clear screenshot, terminal capture, output sample, or diagram plan before it needs illustration.

### 4b. Build multilingual introductions without claim drift

When multilingual publishing is requested:

- choose one canonical README or introduction and record it in the package;
- select languages from real audience evidence or the user’s explicit scope, not decorative language count;
- keep the same language navigation near the top of every localized README;
- preserve commands, paths, API identifiers, filenames, URLs, version numbers, shipped claims, limitations, and license identity across languages;
- keep one canonical detailed release body and add localized summaries unless full translations can be reviewed and maintained;
- never strengthen a claim in translation or present a roadmap item as shipped;
- disclose in the handoff when a translation has not been reviewed by a fluent human.

Treat localization as a maintained publishing surface. If parity cannot be maintained, label the localized file with its review date and link to the canonical source.

### 5. Apply with a non-code file allowlist

Before Apply mode, state the exact files that may change. During the edit:

- preserve verified install commands and technical semantics;
- keep relative links portable across branches;
- minimize badge and image weight;
- never erase user content merely to fit the template;
- maintain existing language variants or flag translation drift;
- keep legal, security, support, and governance language factual and enforceable.

After edits, inspect the diff. If any source, test, dependency, workflow, build, or runtime file changed, stop and revert only the changes created by this task without touching the user's pre-existing work.

### 6. Validate the publishing result

Verify, as applicable:

- project purpose is understandable above the fold;
- one primary action is obvious and the documented path is copied exactly from verified project material;
- images have alt text and remain legible on mobile/dark backgrounds;
- generated assets preserve real product evidence, contain no fabricated UI/output, and declare which portions are generated;
- required text is exact, logos are authorized, focal content survives a 320×160 thumbnail test, and cropped screenshots remain truthful;
- Social Preview follows current GitHub size/type limits;
- every material claim is supported or qualified;
- comparisons name the date/version and admit where alternatives fit better;
- all links resolve and language-switch links are symmetric;
- localized introductions preserve canonical claims, commands, limitations, versions, and license identity;
- release copy separates shipped features from roadmap items;
- community and security contact placeholders are not presented as live policy;
- channel drafts obey current platform/community rules;
- no out-of-scope file changed and no external action occurred without authorization.

## Handoff

Lead with the resulting publishing improvement, not the process. Report:

- files or drafts created/changed;
- the top three conversion improvements;
- unresolved facts/placeholders and why they matter;
- canonical language, published locales, and human-review status for multilingual output;
- actions the user must perform in GitHub Settings or external platforms;
- the next measurement checkpoint;
- an explicit confirmation that source code and runtime behavior were not changed.
