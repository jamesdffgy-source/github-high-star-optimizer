# High-star repository visual style library

Read this reference when selecting a visual direction, generating a README hero or Social Preview, treating screenshots, or deciding whether a repository needs imagery at all.

## Evidence boundary

Visual polish can improve comprehension and memorability, but the examples below do not prove that a visual style caused a repository's Stars. The sample is purposive rather than statistically representative. It combines established frameworks, product repositories, CLI tools, AI projects, and creative tools that had roughly 48k–248k Stars in a GitHub API snapshot on 2026-08-26.

Use the patterns to choose a truthful presentation for the target project. Do not copy another project's brand, layout, mascot, screenshot, or illustration.

## What the sample actually uses

| Visual archetype | Observed examples | What the image does | Best fit | Main risk |
|---|---|---|---|---|
| Proof-first full screenshot | Hoppscotch, Open WebUI, VS Code, RustDesk | Shows the real interface and immediately identifies the product category | GUI, web, desktop, developer tools | Raw screenshots can be unreadable or expose private data |
| Brand strip plus product proof | n8n, Excalidraw | Establishes identity first, then follows with a real screenshot/demo | Products with a recognizable visual language | Decorative banner pushes proof below the fold |
| Product-as-poster composite | Twenty, Appwrite, LobeHub | Crops and layers real UI inside a designed launch composition | Polished product launches and Social Preview | Perspective/blur can hide what the product really looks like |
| Minimal identity | Dify, Open WebUI banner, Ollama, Tailwind CSS | Uses a logo, name, one accent color, or short promise with large negative space | Strong brand or simple technical category | Unknown projects may look empty and unproven |
| Signature illustrated world | Excalidraw, n8n | Uses a product-native illustration language, not generic AI art | Creative tools or brands with an existing illustration system | Style imitation and visual clutter |
| Terminal proof and task demos | lazygit, fzf | Shows a real terminal state or a short action-to-result recording | CLI and TUI projects | Tiny type, unreadable speed, secrets, non-copyable commands |
| Minimal/no hero | React and other established libraries | Relies on category recognition, docs, install path, and ecosystem proof | Mature standards/frameworks with strong name recognition | Poor choice for a new unknown repository |

### Sample-specific observations

- **Dify:** oversized wordmark and outcome line in black/electric blue on a neutral field; typographic and extremely sparse rather than screenshot-led.
- **n8n:** dark indigo ecosystem illustration with colored connected blocks, followed by a bright, clean real workflow screenshot.
- **LobeHub:** large outcome headline, warm orange/yellow field, real UI cards, connectors, agent labels, and a branded mascot; a dense product-story composite.
- **Twenty:** light/dark responsive cover variants; cropped real product panels layered with pixel-like electric-blue illustration and generous black/white negative space.
- **Open WebUI:** an ultra-thin monochrome identity banner followed by a full-width dark product screenshot.
- **Excalidraw:** pastel hand-drawn brand strip followed by a framed product screenshot whose content demonstrates the same hand-drawn visual identity.
- **Hoppscotch:** light/dark full-width product screenshot; almost no decorative marketing layer.
- **Appwrite:** dark cinematic perspective crop of a real dashboard with one magenta accent; the UI itself becomes the poster.
- **Cal.com:** centered dark product state with abundant empty space, focusing attention on one scheduling interaction.
- **lazygit/fzf:** real terminal/TUI evidence, short task-specific demos, and readable state changes rather than abstract developer imagery.
- **React/Ollama:** little or no hero imagery. Their scale shows that high Stars do not require a large promotional illustration.

## Shared patterns worth reusing

These patterns recur across very different samples:

1. **One job per image.** Identity, product proof, explanation, and release announcement are separate jobs.
2. **The product remains recognizable.** Even cinematic composites retain real controls, output, or workflow structure.
3. **A restricted palette.** Monochrome plus one strong accent is more common than many competing colors.
4. **Large focal shapes and negative space.** The image survives README scaling and link-preview thumbnails.
5. **Minimal image text.** Usually project name plus a short outcome; installation and feature detail remain selectable Markdown.
6. **Brand consistency over fashionable style.** Excalidraw looks hand-drawn because the product is hand-drawn; n8n uses connected nodes because workflows are its core metaphor.
7. **Light/dark consideration.** Some repositories use `<picture>` sources for separate light and dark assets instead of forcing one compromised image.
8. **Proof follows brand.** A decorative cover is often paired with a real screenshot or demo nearby.

Avoid turning these observations into fixed requirements. Established projects can succeed with almost no imagery; weaker projects do not become credible through expensive-looking art.

## Select by project type

| Project type | Primary proof | Recommended supporting style | Do not generate |
|---|---|---|---|
| GUI/web/desktop | Real interface showing one successful user outcome | Clean screenshot, proof-first crop, or restrained product-as-poster composition | Invented screens, fake accounts, fictional integrations |
| CLI/TUI | Real terminal capture showing input → result | High-contrast terminal frame; short recording with one task | Commands, output, timings, or platform support not observed |
| Library/SDK | Real code/result pair or rendered output | Minimal identity, concise mechanism illustration | A fictional dashboard that implies a GUI product |
| Infrastructure/devops | Verified architecture plus deploy/observability evidence | Dark technical diagram or real console crop | Fake topology, uptime, throughput, security status |
| AI/model/research | Representative real input/output plus constraints | Controlled comparison grid or method diagram | Cherry-picked or synthetic output presented as ordinary performance |
| Creative/game/media | Real output montage with version/context | Signature visual world derived from the project's own work | Style imitation of living artists or unlicensed characters/assets |
| Resource list/template | Real generated artifact or searchable collection view | Minimal catalog/grid composition | Fake item count, contributors, popularity, or coverage |

## Truth classes

Classify every asset before creating it:

### Proof

Screenshots, terminal recordings, benchmark charts, input/output examples, dashboards, and user results. Proof must come from repository or user-provided evidence. Generative tools may crop, frame, place on a background, or remove irrelevant surroundings only when the content itself stays unchanged and the treatment cannot alter its meaning.

### Brand

Abstract backgrounds, textures, mascots, cover illustrations, decorative systems, and launch-card layouts. Brand assets may be generated, but they must not resemble evidence of functionality. Preserve an existing logo exactly when supplied; logo redesign is a separate, explicitly authorized brand decision.

### Explanation

Architecture, process, comparison, lifecycle, or concept diagrams. Use deterministic diagram/vector tools when labels, nodes, arrows, topology, or values must be exact. A raster generator is appropriate only for non-literal conceptual illustration.

## Image-generation workflow

1. Inspect the README, existing logo/brand assets, screenshots, demo, and current Social Preview read-only.
2. Build an asset inventory with owner/permission, freshness, sensitive-data status, and truth class.
3. Select one visual archetype based on project type, existing brand, proof strength, and intended placement. Explain why it fits.
4. Complete [../assets/IMAGE_GENERATION_BRIEF.template.md](../assets/IMAGE_GENERATION_BRIEF.template.md).
5. For a local screenshot or brand reference, inspect it before editing and label each input image's role.
6. Prefer a real screenshot with minimal treatment. Use generation when it adds useful identity, framing, or a truthful conceptual layer.
7. Generate non-destructively with a versioned filename. Keep drafts in the launch kit during Prepare mode.
8. Inspect the full-size result and a 320×160 thumbnail. Check text character-by-character.
9. Reject any variant that changes product content, suggests an unshipped feature, distorts a logo, or depends on illegible text.
10. Report final prompt, reference roles, generated portions, saved path, and whether the asset is only a draft.

If a bitmap generator is unavailable, deliver the exact brief and prompt. Do not substitute an unrequested SVG or claim an asset was generated.

## Prompt recipes

Use only the recipe matching the target asset. Preserve the project's evidence and brand rather than copying an example repository.

### Proof-first Social Preview

```text
Use case: ads-marketing
Asset type: GitHub repository Social Preview, 2:1 landscape
Primary request: create a restrained launch composition around the real product screenshot from Image 1
Input images: Image 1: immutable real product proof; Image 2: existing project logo to preserve exactly
Scene/backdrop: solid or subtle brand field with one accent and ample negative space
Subject: one readable crop of the real product outcome; project identity secondary
Style/medium: editorial developer-tool launch card, crisp, flat, high contrast
Composition/framing: one focal point; thumbnail-safe; keep critical content away from edges
Text (verbatim): "{{PROJECT_NAME}}" and "{{6_TO_12_WORD_OUTCOME}}"
Constraints: do not alter any UI, output, numbers, logos, or product state; no fake browser chrome; no badges; no Star count; no watermark
Avoid: generic futuristic code, neon overload, tiny feature lists, fake metrics, GitHub/Octocat imitation
```

### Minimal technical cover

```text
Use case: ads-marketing
Asset type: README hero or repository Social Preview
Primary request: a minimal identity cover for {{PROJECT_NAME}} based on its existing visual system
Input images: Image 1: existing logo or brand reference, preserve exactly
Scene/backdrop: clean solid field or very subtle geometric texture derived from the project's own core metaphor
Subject: logo/project name and one concise outcome line
Style/medium: restrained technical editorial design; monochrome plus one existing brand accent
Composition/framing: large typography, generous negative space, one focal point, readable as a thumbnail
Text (verbatim): "{{PROJECT_NAME}}" and "{{OUTCOME_LINE}}"
Constraints: no product UI; no invented symbol; no extra slogan; no badges; no URL; no fake metrics; no watermark
```

### CLI/TUI proof card

```text
Use case: ads-marketing
Asset type: README hero or release card for a CLI/TUI project
Primary request: frame the real terminal capture from Image 1 as the central proof of one completed task
Input images: Image 1: immutable real terminal capture; Image 2: optional existing logo
Scene/backdrop: simple dark or light field matching the existing terminal theme
Subject: readable terminal state with input and resulting output visible
Style/medium: precise developer-tool editorial layout, not sci-fi
Composition/framing: terminal occupies most of the canvas; minimal caption area; no perspective distortion
Constraints: preserve every command and output character; no invented commands; no speed claims; no secrets; no glow that hurts readability; no watermark
```

### Product-as-poster composite

```text
Use case: ads-marketing
Asset type: README launch hero
Primary request: compose two or three real product crops into a cohesive product story
Input images: Image 1: primary immutable outcome screen; Image 2: secondary immutable workflow screen; Image 3: existing logo
Scene/backdrop: project brand field with restrained depth and one existing accent color
Subject: real product panels arranged from action to outcome
Style/medium: polished product editorial composite with crisp UI and subtle depth
Composition/framing: primary screen largest; secondary screen supports it; clear reading order; generous negative space
Constraints: do not redraw or regenerate UI; no perspective that makes text unreadable; no invented screen; preserve logo; no fake metric or endorsement; no watermark
```

## Visual QA gate

An asset is ready only when all applicable checks pass:

- **Truth:** all UI, output, metrics, logos, and claims are sourced; generated portions are recorded.
- **Fit:** the visual archetype matches the project type and existing identity, not merely a popular trend.
- **Focal clarity:** one message and one obvious visual focus survive at 320×160.
- **Text:** exact, short, readable, and also available outside the image when it carries essential meaning.
- **Proof legibility:** real product/terminal content remains readable enough to support the claim.
- **Accessibility:** useful alt text and a static/text fallback exist; meaning is not image-only.
- **Theme:** transparent edges and contrast work on light/dark surfaces, or separate variants exist.
- **Technical:** correct size/format, reasonable weight, stable relative path, descriptive kebab-case filename.
- **Rights/privacy:** no unauthorized logo, face, customer data, secret, private hostname, or proprietary content.
- **Scope:** the asset is a publishing artifact; no code, workflow, dependency, build, or runtime file changed.

## Research sources

Official repository pages/READMEs inspected on 2026-08-26:

- [Dify](https://github.com/langgenius/dify)
- [n8n](https://github.com/n8n-io/n8n)
- [LobeHub](https://github.com/lobehub/lobehub)
- [Twenty](https://github.com/twentyhq/twenty)
- [Open WebUI](https://github.com/open-webui/open-webui)
- [Excalidraw](https://github.com/excalidraw/excalidraw)
- [Hoppscotch](https://github.com/hoppscotch/hoppscotch)
- [Appwrite](https://github.com/appwrite/appwrite)
- [RustDesk](https://github.com/rustdesk/rustdesk)
- [Cal.com](https://github.com/calcom/cal.com)
- [React](https://github.com/facebook/react)
- [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss)
- [Ollama](https://github.com/ollama/ollama)
- [lazygit](https://github.com/jesseduffield/lazygit)
- [fzf](https://github.com/junegunn/fzf)

Current platform constraints and markup patterns:

- [GitHub Social Preview documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- [GitHub responsive light/dark image example](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github#adding-an-image-to-suit-your-visitors)
- [GitHub image and relative-link syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images)

Re-verify platform size/type limits before publishing. Repository visuals and Star counts change over time.
