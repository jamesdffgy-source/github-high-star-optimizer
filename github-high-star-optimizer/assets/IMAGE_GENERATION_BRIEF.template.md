# {{PROJECT_NAME}} image-generation brief

Status: Draft publishing asset; not linked, uploaded, or published.

## Asset decision

- Placement: {{README_HERO_SOCIAL_PREVIEW_RELEASE_CARD_OR_OTHER}}
- Truth class: {{PROOF_BRAND_OR_EXPLANATION}}
- Visual archetype: {{PROOF_FIRST_BRAND_PLUS_PROOF_PRODUCT_POSTER_MINIMAL_TERMINAL_OR_OTHER}}
- Why this fits the project: {{EVIDENCE_BASED_REASON}}
- Why an image is needed: {{COMMUNICATION_JOB}}
- If no image is better, stop reason: {{NOT_APPLICABLE_OR_REASON}}

## Verified content

| Element | Source/path | Role | Permission/owner | Sensitive-data result | May generation alter it? |
|---|---|---|---|---|---|
| {{SCREENSHOT_OR_OUTPUT}} | {{SOURCE}} | Immutable proof | {{OWNER}} | {{RESULT}} | No |
| {{LOGO}} | {{SOURCE}} | Brand reference | {{OWNER}} | N/A | No, unless concept exploration was explicitly requested |
| {{OTHER}} | {{SOURCE}} | {{ROLE}} | {{OWNER}} | {{RESULT}} | {{YES_NO_AND_LIMIT}} |

Unsupported elements to omit: {{LIST}}

## Output specification

- Canvas/aspect ratio: {{SIZE}}
- Format and maximum size: {{FORMAT_LIMIT}}
- Light/dark behavior: {{SOLID_TRANSPARENT_OR_SEPARATE_VARIANTS}}
- Safe area: {{MARGIN}}
- Thumbnail target: must remain clear at 320×160
- Filename: {{PROJECT_NAME}}-{{ASSET_TYPE}}-v{{N}}.png
- Prepare-mode output directory: {{SEPARATE_LAUNCH_KIT_PATH}}

## Generation prompt

```text
Use case: {{IMAGEGEN_TAXONOMY_SLUG}}
Asset type: {{PLACEMENT_AND_SIZE}}
Primary request: {{MAIN_REQUEST}}
Input images: {{IMAGE_1_ROLE_IMAGE_2_ROLE}}
Scene/backdrop: {{BACKGROUND}}
Subject: {{ONE_FOCAL_SUBJECT}}
Style/medium: {{STYLE}}
Composition/framing: {{COMPOSITION}}
Lighting/mood: {{LIGHTING_OR_NOT_APPLICABLE}}
Color palette: {{EXISTING_BRAND_PALETTE}}
Materials/textures: {{ONLY_IF_USEFUL}}
Text (verbatim): "{{EXACT_TEXT_OR_NONE}}"
Constraints: preserve real screenshots, output, logo geometry, and verified product state; {{OTHER_INVARIANTS}}
Avoid: invented UI, commands, metrics, integrations, customers, endorsements, Star count, badge wall, tiny feature list, watermark, trademark imitation
```

## Generated-content disclosure

- Real portions: {{LIST}}
- Generated portions: {{LIST}}
- Editing/compositing performed: {{LIST}}
- Claims depicted: {{LIST_AND_EVIDENCE}}

## QA

- [ ] Real screenshot/output pixels and meaning were not altered.
- [ ] No unshipped feature, fake interface, command, metric, customer, integration, or endorsement appears.
- [ ] Existing logo geometry and spelling are exact.
- [ ] Required text was checked character-by-character at 100% zoom.
- [ ] One focal point remains clear at 320×160.
- [ ] Product evidence remains readable; decoration does not overpower it.
- [ ] Contrast/transparency works on light and dark surfaces, or variants exist.
- [ ] Alt text and non-image explanation are drafted.
- [ ] No secret, personal data, private hostname, or proprietary content appears.
- [ ] File type, dimensions, size, filename, and repository path are valid.
- [ ] Asset remains in the launch kit unless Apply/Publish was explicitly authorized.

## Handoff

- Final prompt: {{PROMPT_OR_PATH}}
- Selected file: {{PATH_OR_NOT_GENERATED}}
- Rejected variants and reasons: {{LIST}}
- Remaining user approval: {{APPROVAL}}

