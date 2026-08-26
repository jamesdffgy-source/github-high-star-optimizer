# Repository metadata, release, and distribution guide

Read this reference when optimizing GitHub About fields, Topics, Social Preview placement, community surface, Releases, a relaunch, channel copy, or measurement.

## Repository metadata package

Produce a copy-ready block:

```text
Suggested repository name: <only if renaming is justified>
About description: <specific category + audience/result + differentiator>
Homepage: <one primary live demo/docs/project URL>
Topics: <8–15 relevant lowercase terms, fewer if the niche is narrow>
Social Preview: <asset path or brief>
```

GitHub permits up to 20 Topics, but relevance is more important than filling the limit. Cover category, problem, ecosystem, language/framework, deployment, and defining properties. Do not add unrelated popular terms.

Renaming is high friction. Recommend it only for a concrete collision, misleading identity, unsearchable spelling, or material repositioning, and include redirect/package/docs consequences. Do not rename automatically.

## Community surface

These files can improve confidence but represent real commitments:

- `CONTRIBUTING`: accepted contribution types, setup links, review path, realistic response time.
- `SUPPORT`: where questions, bugs, private matters, and paid support belong.
- `SECURITY`: supported versions and a real private vulnerability-reporting contact.
- `CODE_OF_CONDUCT`: chosen standard, enforcement contact, and actual willingness to enforce.
- Issue/PR templates: request actionable information without making contribution burdens excessive.
- `GOVERNANCE`/`ROADMAP`: decision rights, scope, maturity, and direction without fake deadlines.

Never create a false security email, response SLA, legal promise, maintainer roster, funding link, or governance process. Use visible placeholders in Prepare mode.

## Release reason

An existing project deserves a relaunch only when there is a truthful user-facing reason, such as:

- a major version or stable milestone;
- dramatically clearer installation/documentation using an existing supported path;
- a new real demo or platform/package already shipped;
- a meaningful user-requested capability already released;
- verified performance/reliability result;
- rebranding/repositioning with a migration explanation;
- moving from an internal prototype to a documented public project.

A README rewrite alone can justify a presentation refresh, but not claims of a new product version.

## Release notes structure

1. One-sentence user outcome.
2. Why this release matters now.
3. Shipped highlights grouped by user value.
4. Breaking changes and exact upgrade/migration path from existing project docs.
5. Fixes and limitations.
6. Verified install/download links and checksums only if they already exist.
7. Contributors and evidence-backed user acknowledgements.
8. Support/security/reporting links.
9. Non-incentivized feedback/Star CTA.

Separate shipped work from roadmap. Never label an unmerged branch, planned feature, or unverified fix as released.

## Relaunch sequence

### Preparation window (7–21 days)

- Capture baseline: Stars, unique repository visitors/referrers where available, downloads/installs/adoption proxy, open support load.
- Test the public instructions with target users or verify they match current docs; do not change code.
- Resolve publishing P0 items.
- Prepare README, visuals, metadata, release notes, FAQ, claim ledger, and response coverage.
- Select one primary community and one secondary channel; do not blast every platform.

### Launch waves

1. Existing users/contributors and GitHub Release/Discussion.
2. One audience-matched community; answer questions and update confusing copy.
3. A technical article, comparison, migration, or reproducible result for durable search traffic.
4. A larger platform only after the project can be tried and maintainers can respond.
5. Localized release for a genuinely distinct language community.

Leave 2–7 days between waves when possible. Treat feedback as information; do not defend every criticism or promise every request.

### 14-day follow-through

- Day 0: publish the canonical release and primary channel post.
- Days 1–2: answer, acknowledge limitations, fix broken copy/links only within authorized scope.
- Days 3–4: publish one technical proof piece.
- Days 5–7: highlight a real use case or contributor; update FAQ.
- Days 8–10: second audience-matched channel, with native framing.
- Days 11–14: report what was learned, compare metrics, and choose the next publishing experiment.

## Channel decision rules

### Hacker News / Show HN

Use only for something the author made that people can actually try. Minimize signup/email barriers, explain how and why it was built, and have the maker participate. Do not ask friends for votes/comments. Hacker News currently prohibits generated or AI-edited comment text; provide facts and an outline, then require the human maker to write the submission/comment in their own words. Verify current official guidelines before launch.

### Reddit

Choose a subreddit where the project directly solves a known problem. Read its specific rules, disclose the author relationship, provide useful context, and avoid repeated cross-posts, unsolicited DMs, bots, or a profile consisting mostly of self-promotion. A Reddit draft should sound native to that community, not like a press release.

### Product Hunt

Use for a live, polished product suited to early adopters. Prepare tagline, gallery, maker comment, goals, and all-day response coverage. Current official guidance allows sharing the launch but forbids asking people directly to upvote; do not pay hunters or promoters for artificial traffic. Verify rules before launch.

### Technical writing platforms

Publish a standalone useful tutorial, architecture decision, benchmark method, migration, or failure analysis. The project link should be a natural implementation/source, not the article’s only value.

### V2EX and Chinese developer communities

Use plain, specific language; state that you are the author; show what works; include technical details and limitations; choose the correct node/topic; respond to critique. For 掘金/知乎/公众号/Bilibili, rewrite for the platform rather than copying the same announcement. Prepare Chinese troubleshooting and accessible media where the audience needs them.

### Newsletters, maintainers, and ecosystem partners

Pitch only when the project is directly relevant. Provide a one-line result, why it matters to their audience, a real demo, license/status, and source links. Personalize; never mass-message stargazers or scrape contact details for solicitation.

## Channel-native draft fields

Each draft should contain:

- audience and channel;
- hook grounded in a real user problem;
- author disclosure;
- result/demo;
- how it works at the appropriate depth;
- limitations and status;
- direct project link;
- invitation for feedback;
- no vote/Star reward or manipulation.

## Measurement

GitHub repository Traffic currently exposes a rolling 14-day window to users with push access, including visitors, clones, referrers, and popular content. Archive it at least weekly if available.

Track:

- exposure: post impressions and repository unique visitors/referrers;
- activation: demo/Quickstart/install success proxy;
- trust: net new Stars, watches, forks, return visits;
- adoption: downloads, dependents, active use, deployments, or project-specific proxy;
- community: substantive issues, first response time, contributors, repeat contributors;
- quality of attention: questions and use cases from the intended audience.

Approximate visitor-to-Star conversion only for the same window:

```text
net new Stars / unique repository visitors
```

Label it approximate: visitors and Stars are not perfectly aligned, unstars and repeats exist, and channel events confound sequential comparisons. Optimize adoption and qualified feedback, not this ratio alone.

