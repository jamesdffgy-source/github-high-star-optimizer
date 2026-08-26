# Repository naming and search discoverability guide

Read this reference when the user asks whether a repository name is clear, searchable, collision-resistant, trustworthy, or worth changing.

Sources were reviewed on 2026-08-27. GitHub search behavior and current competitors can change; repeat live sampling before a rename or launch.

## Name for intent, not prestige

A repository name should help the intended user predict the project’s job. Prefer a real task, category, artifact, or outcome over prestige claims.

Treat words such as `best`, `ultimate`, `viral`, `high-star`, `trending`, and `growth-hack` as risk terms. They are not automatically forbidden, but they may:

- describe an aspirational result instead of the actual function;
- attract an irrelevant or low-trust audience;
- sound like guaranteed ranking or engagement manipulation;
- displace higher-intent task words such as `repository`, `readme`, `launch`, `release`, `docs`, or `publishing`.

Do not confuse searchability with keyword density. One clear name plus an aligned description and relevant Topics is stronger than a long list of popular terms.

## What GitHub search can see

Before analysis, verify the current [GitHub repository search documentation](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories).

At the review date, ordinary repository search covers repository name, description, and Topics. README text is searchable when `in:readme` is used. GitHub does not publish a dependable formula for best-match ranking, so never promise a position.

## Evidence sheet

Record:

- canonical product category;
- primary audience and the words they use for the task;
- publishing-only scope and important non-goals;
- existing package, CLI, domain, social, documentation, and Skill invocation names;
- current external links and release references that a rename would affect;
- live GitHub search samples and the review date.

## Query set

Use a small, representative set rather than hundreds of synthetic keywords:

1. **Exact identity:** current and candidate names with `in:name`.
2. **Category:** for example, `github repository optimizer`.
3. **Task:** for example, `github readme optimizer` or `open source launch skill`.
4. **Host/ecosystem:** for example, `codex github skill` or `claude code github skill` when supported.
5. **Risk interpretation:** queries combining the name with `buy stars`, `fake stars`, or `star bot` only to check misleading adjacency—never to optimize for those terms.

Record result counts and whether the project appears in the first 30 or 100 results. Treat the sample as a dated observation, not a stable ranking guarantee.

## Candidate scorecard — 100 points

| Criterion | Points | Full-credit test |
|---|---:|---|
| User-intent fit | 25 | Contains or strongly evokes the category/task the target user searches for |
| Natural wording | 15 | Easy to say, spell, remember, and translate; no awkward prestige phrase |
| Truthful scope | 20 | Does not imply code optimization, guaranteed Stars, SEO rank, or unsupported functionality |
| Search-field coverage | 15 | Complements the About description and Topics without repeating every keyword |
| Distinctiveness | 10 | Low exact-name collision and no confusing established project overlap |
| Cross-host portability | 5 | Works as a repository, Skill folder, and invocation name across intended hosts |
| Rename cost | 10 | Package names, URLs, actions, docs, assets, and external references can be migrated safely |

Do not choose the highest numerical score blindly. Reject a candidate that creates a material scope or trust problem even if it contains more keywords.

## Candidate families

Provide at least one option from each relevant family:

- **Descriptive:** category + task, such as `github-repo-launch-optimizer`.
- **Scope-led:** emphasizes publishing boundaries, such as `github-repo-publishing-kit`.
- **Brand + descriptor:** a distinctive brand paired with a searchable subtitle in the README and About field.
- **Keep current:** retain identity while improving description, Topics, README language, and aliases.

Candidate examples are structural patterns, not automatic recommendations. Check live collisions and the project’s actual scope.

## Rename decision

Recommend renaming only when at least one material issue exists:

- users consistently misunderstand the project’s job;
- the name emphasizes an irrelevant or risky term;
- a collision causes confusion;
- the wording is hard to spell or search;
- the project has materially repositioned and the current name is no longer truthful.

Prefer metadata changes when the name is already clear and the discoverability gap can be covered by the description and Topics.

## Migration map

Before a live rename, list and verify:

- GitHub repository name and local `origin` URL;
- Skill folder, frontmatter `name`, explicit invocation syntax, and host-specific installation examples;
- root and localized READMEs, badges, release links, image labels, templates, and generated assets;
- package registries, GitHub Actions references, Pages URLs, documentation domains, social posts, and external directories;
- releases/tags and compatibility notes.

GitHub’s [repository rename documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository) currently says web traffic and normal clone/fetch/push traffic redirect, while GitHub Actions references do not. Recheck this before mutation. Never rename automatically; show the final migration payload and obtain explicit authorization.

## Required output

Return:

1. a clear keep/rename recommendation with confidence;
2. current-name strengths and risks;
3. dated live-query evidence;
4. three to five candidates with score, meaning, collision result, and downside;
5. the recommended About description and Topics whether or not the name changes;
6. rename consequences and a rollback/redirect check;
7. a statement that search sampling does not guarantee Stars or ranking.
