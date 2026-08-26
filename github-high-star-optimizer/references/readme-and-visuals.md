# README and visual conversion guide

Read this reference when creating or revising README content, badges, screenshots, GIFs, diagrams, Social Preview, or localized landing copy.

## README job

The README is the repository landing page. Its first screen must answer:

1. What is this?
2. Who is it for?
3. What concrete result does it create?
4. What does that result look like?
5. What should I do next?

Use repository/user evidence. Do not invent product benefits from the name or technology stack.

## Recommended conversion order

1. Project identity and evidence-safe one-line value.
2. Language switch when the audience needs it.
3. At most 3–5 high-signal badges.
4. Real visual result or terminal/demo output.
5. One primary CTA: Try Demo, Quickstart, Install, or View Docs.
6. Three outcome-oriented reasons to use it.
7. Verified Quickstart copied from the current project material.
8. Realistic use case with expected output.
9. Fair comparison or “when to use / when not to use.”
10. Features, current limitations, maturity, prerequisites.
11. Documentation, examples, architecture only as needed.
12. Roadmap/status, contribution, support, security, license, acknowledgements.
13. Optional non-incentivized Star CTA after value has been demonstrated.

Do not force this exact structure when ecosystem conventions or the existing project provide a better user journey.

## Positioning options

Draft three alternatives:

- **Outcome-led:** `[Project] helps [specific user] achieve [measurable/observable result] in [situation].`
- **Category + differentiator:** `[Category] for [audience] — [specific mechanism/constraint that differentiates it].`
- **Alternative framing:** `[Specific alternative] for people who need [reason to switch], without [important cost/friction].`

Recommend one using evidence strength, audience clarity, and search discoverability—not stylistic preference alone.

## Quickstart safety

- Copy the current command exactly from a verified repository source.
- Never “simplify” a command in a way that changes behavior or security.
- Keep prerequisites, supported versions, credentials, ports, data effects, and expected output visible.
- If the documented path cannot be verified, label it “existing documented command; not executed in this task” rather than claiming success.
- Do not add a new install mechanism; that would exceed publishing-only scope.

## Badges

Prefer high-signal badges: current release, build status already produced by the repository, package/download identity, documentation, and existing license. Avoid:

- decorative technology walls;
- broken or stale badges;
- badges implying audits, coverage, security, compatibility, or downloads without a real source;
- dynamic third-party badges that leak visitor data without consideration;
- placing so many badges that the value statement and demo move below the fold.

## Visual asset plan

For style selection, generated-image boundaries, observed high-star repository patterns, and prompt construction, read [visual-style-library.md](visual-style-library.md). A visually impressive image cannot replace real product proof.

Select a proof format that matches the project:

| Project | Strong proof asset |
|---|---|
| GUI/Web/Desktop | Screenshot or 20–40 second input → action → result demo |
| CLI | Terminal recording with readable font and no secrets |
| Library/SDK | Minimal code beside actual output, plus optional mechanism diagram |
| Infrastructure | Architecture diagram plus verified deploy/observability result |
| AI/Research | Representative input/output, method diagram, requirements and limitations |
| Resource list/template | Search/filter/classification view or concrete generated result |

Demo storyboard:

1. State the starting problem in one short frame.
2. Show the minimum user action without jump cuts that hide complexity.
3. Hold the result long enough to read.
4. Show one differentiator or constraint.
5. End with project name and primary action, not a demand for Stars.

Protect secrets, personal data, customer names, hostnames, API keys, and proprietary content. Obtain permission for logos/testimonials.

Separate visual assets by truth function:

- **Proof:** actual product screenshot, terminal recording, output pair, benchmark, or measured chart. It must come from verifiable project evidence.
- **Brand:** logo, color field, abstract illustration, mascot, texture, or decorative composition. It may be generated, but must not look like proof of functionality.
- **Explanation:** architecture, lifecycle, comparison, or concept diagram. Prefer deterministic diagrams when nodes, arrows, labels, or topology must be exact.

For a new or lesser-known project, lead with proof. Brand-only covers are strongest when the project identity is already recognizable or when a proof visual follows immediately.

## Social Preview brief

Current GitHub guidance recommends 1280×640 for best display, at least 640×320, PNG/JPG/GIF, under 1 MB. Verify the official documentation before publishing if it may have changed.

The brief must state:

- canvas and safe area;
- project name;
- 6–12 word outcome statement;
- one actual product/result visual or a simple brand mark;
- background and contrast for light/dark sharing surfaces;
- mobile thumbnail test;
- no tiny badges, URLs, fake metrics, or dense feature lists.

## Localization

- Use the language of the target audience, not English by reflex.
- For global developer reach, an English primary README plus maintained localized versions is often practical, but do not require it for local-only projects.
- Keep language links symmetric and near the top.
- Add a visible “content may lag” notice when translations are not maintained at the same cadence.
- Preserve commands, paths, API identifiers, and version numbers exactly across translations.

## Accessibility and rendering QA

- Meaningful alt text describes the information, not “image.”
- Do not encode essential instructions only inside images.
- Provide a static image or text fallback for GIF/video.
- Check narrow mobile width, dark mode, image transparency, reduced-motion concerns, and file size.
- Use relative repository links when appropriate and verify case sensitivity.
- Keep headings hierarchical and link labels descriptive.

## Truthful comparison

If a comparison is helpful, include date/version, measurement context, sources, and explicit situations where the alternative is a better fit. Compare decision criteria, not brand prestige. Never use an alternative’s logo without permission or imply endorsement.

## Compliant Star CTA

Use only after showing value. Example:

> If this project is useful, you can Star it to find it again and help other relevant users discover it.

Do not gate access, create urgency, offer rewards, or repeatedly place the CTA throughout the README.
