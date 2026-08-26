# Publishing-only audit rubric

Use this rubric for an existing repository. Score only what a visitor, user, contributor, or publisher can observe from the public presentation and release surface. Do not inspect or grade source-code quality.

## Scoring method

- Award full points only when the item is visible, accurate, and usable.
- Award half points when present but unclear, buried, outdated, or partly broken.
- Award zero when missing, misleading, unverifiable, or blocked by placeholders.
- Record evidence next to every score.
- A high score means “release/presentation ready,” not “guaranteed to gain Stars.”

## A. Positioning and proof — 25 points

| Item | Points | Full-credit evidence |
|---|---:|---|
| Specific audience | 5 | A visitor can name the intended user, not merely “developers/everyone” |
| Concrete problem/outcome | 5 | Copy describes a recognizable situation and result |
| Defensible differentiator | 5 | Difference from the default alternative is factual and specific |
| Visible proof | 5 | Real screenshot, output, demo, reproducible result, or named case with permission |
| Honest scope and maturity | 5 | Alpha/beta/production status, limitations, prerequisites, and non-goals are clear |

Red flags: superlatives without evidence, trend-chasing keywords, positioning made entirely from implementation details, claimed users/logos without proof.

## B. README conversion surface — 25 points

| Item | Points | Full-credit evidence |
|---|---:|---|
| Above-the-fold clarity | 5 | Name, one-line value, visual result, and primary action appear early |
| Quickstart visibility | 5 | Verified existing install/use path is easy to find and copy |
| Information architecture | 5 | User journey precedes deep implementation; headings and links scan well |
| Use cases and expected output | 4 | At least one realistic example shows what success looks like |
| Support/navigation | 3 | Docs, issues/discussions/support, security, and license destinations are findable |
| Localization/accessibility | 3 | Relevant language variants, symmetric navigation, image alt text, readable visuals |

Red flags: giant logo before value, badge wall, background story before usage, broken language switch, unverified install command, roadmap presented as shipped.

## C. Visual demonstration — 15 points

| Item | Points | Full-credit evidence |
|---|---:|---|
| Hero/proof visual | 5 | Actual product/result is legible and representative; generated decoration is clearly secondary to proof |
| Demo story | 4 | GIF/video/screenshot sequence shows input → action → result without misleading cuts |
| Social Preview | 3 | A current, readable 1280×640 brief or image is available |
| Asset discipline | 3 | Reasonable file size, alt/fallback, dark/mobile checks, no unauthorized logos, fabricated UI, output, or metrics |

For CLI/library projects, terminal output, diagrams, benchmarks, and minimal code/result pairs can replace UI screenshots.

## D. Trust and repository metadata — 15 points

| Item | Points | Full-credit evidence |
|---|---:|---|
| About description/homepage | 3 | Accurate, concise, and aligned with README |
| Topics | 2 | 8–15 relevant, non-spammy discovery terms, or a justified smaller set |
| License identity | 3 | Existing license is detectable and described accurately; no automatic license choice |
| Maintenance/support state | 3 | Maintainer/support route and realistic response expectations are visible |
| Community/security surface | 2 | Applicable files exist without fake contacts or unenforceable promises |
| Badges/status claims | 2 | High-signal, current, accessible, and not used as substitute for proof |

## E. Release readiness — 10 points

| Item | Points | Full-credit evidence |
|---|---:|---|
| Real release reason | 3 | Version/relaunch has a material user-facing improvement or clear project milestone |
| Release notes | 3 | Outcome, changes, limitations, upgrade steps, contributors, and links are separated |
| Consistency | 2 | Version/date/status agree across README, release, docs, and announcement drafts |
| Response readiness | 2 | Maintainer coverage, FAQ, rollback/incident communication plan exist where relevant |

## F. Distribution and measurement readiness — 10 points

| Item | Points | Full-credit evidence |
|---|---:|---|
| Audience-channel fit | 3 | One primary community is selected because its audience matches |
| Channel-native content | 2 | Drafts provide value in the platform’s format instead of copy-paste advertising |
| Ethical compliance | 2 | No vote/Star solicitation scheme, brigading, spam, fake identities, or incentives |
| Measurement baseline | 2 | Current Star/visitor/referrer/adoption baseline and next checkpoint are defined |
| Follow-through | 1 | 14-day response/content/release follow-up owner is clear |

## Score interpretation

| Score | Interpretation | Action |
|---:|---|---|
| 85–100 | Release-ready presentation | Launch a focused channel test; monitor adoption and feedback |
| 70–84 | Strong but leaky | Fix the top two P1 conversion gaps before a wide relaunch |
| 50–69 | Packaging obscures value | Rework positioning, proof, README, and release reason |
| 0–49 | Not ready for amplification | Stop promotion; resolve P0/P1 publishing blockers first |

## Required audit output

Use a table with: area, score, evidence, visitor consequence, priority, recommended publishing change, verification method. End with:

1. three strengths to preserve;
2. three highest-impact gaps;
3. allowed non-code files/settings involved;
4. missing facts requiring the user;
5. a clear statement that the score does not evaluate source code or guarantee Stars.
