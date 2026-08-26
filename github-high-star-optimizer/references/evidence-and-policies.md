# Evidence, policies, and research notes

Use this reference when supporting recommendations, verifying platform constraints, or policing growth tactics. Sources were reviewed on 2026-08-26. Platform rules and product behavior can change; verify current official pages before publishing or making external changes.

## Evidence hierarchy

1. Current official GitHub/platform documentation and policy.
2. Peer-reviewed or clearly described empirical research.
3. First-party maintainer case studies with disclosed project and timeframe.
4. Community anecdotes used only to propose experiments.

Never turn a correlation or a single launch story into a guaranteed tactic.

## Stable GitHub facts to use carefully

- README should explain what the project does, why it is useful, how to start, where to get help, and who maintains it: [GitHub About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).
- Topics help people discover and contribute to projects; GitHub currently permits no more than 20 per repository: [Classifying a repository with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).
- Social Preview currently recommends at least 640×320 and 1280×640 for best display, under 1 MB: [Customizing Social Preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).
- Community Profile recognizes repository health files such as README, License, CONTRIBUTING, Code of Conduct, Issue/PR templates: [About community profiles](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories).
- Releases package software, notes, and assets and can use generated release notes: [About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases).
- Traffic shows a rolling past-14-day view for people with push access: [Viewing traffic](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository).
- Stars help users save/find repositories and express appreciation; repository rankings and Explore may depend on Stars, but Stars are only an approximate interest signal: [Saving repositories with stars](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars), [Starring API](https://docs.github.com/en/rest/activity/starring).

Do not claim knowledge of the GitHub Trending algorithm. GitHub exposes Trending as a discovery surface but does not publish a dependable formula in the cited documentation.

## Research findings: correlation, not prescription

- A survey of 791 developers reported that roughly three out of four considered Star count before using/contributing, while the paper also warns against choosing solely by Stars and notes social promotion: [What’s in a GitHub Star?](https://arxiv.org/abs/1811.07643).
- A study of 1,950 READMEs across ten languages found popular repositories more often used organized lists, images, external links, contribution guidance, and references: [README content and popularity](https://arxiv.org/abs/2206.10772).
- A study of 1,149 academic AI repositories found images, links to GitHub repositories, and presence of a License among the most differentiating features; it explicitly does not claim causality: [Popular academic AI repositories](https://arxiv.org/abs/2010.02472).

Permitted inference: these findings support testing clear structure, real visuals, useful links, contribution guidance, reproducibility, and license clarity.

Forbidden inference: adding a GIF, list, or License will automatically cause a specific Star increase.

## Maintainer case studies: hypothesis generators

- Plane reports early user validation, concise self-hosting instructions, release-note repurposing, focused Reddit participation, and a later Hacker News spike; it also treats Stars as an early attention signal rather than the final metric: [Plane 20K case study](https://plane.so/blog/how-we-got-to-20k-github-stars).
- PostHog describes open source as a differentiation and trust mechanism and reports its early Hacker News launch drove deployments and visibility: [PostHog open-source benefits](https://newsletter.posthog.com/p/the-hidden-benefits-of-being-an-open).
- A Usertour maintainer reports that honest technical build notes, Reddit/Hacker News, release demos, and continued sharing were more useful than going silent after launch: [Usertour 1K case study](https://dev.to/eason_4d12db696ed0477/how-i-promoted-my-open-source-project-and-got-1k-github-stars-17i9).
- Chinese community anecdotes report meaningful spikes after V2EX, technical articles, social video/reposts, and newsletter inclusion; outcomes vary and must not be used as promised conversion rates: [V2EX 300-Star recap](https://v2ex.com/t/1059843), [channel-effect recap](https://www.v2ex.com/t/1145435).

## Authenticity and anti-manipulation

GitHub’s current Acceptable Use Policies prohibit fake accounts, automated inauthentic interactions, automated starring/following and rank abuse, secondary markets for inauthentic activity, and engagement incentivized by airdrops, tokens, credits, gifts, or giveaways: [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies).

Recent empirical fake-Star research finds large coordinated campaigns, many associated with short-lived malicious repositories, and suggests any promotion effect is short-lived and becomes a long-term burden: [Six Million Suspected Fake Stars](https://kapravelos.com/publications/fakestars-icse26.pdf).

Reject:

- paid Stars or “guaranteed Trending” services;
- star-for-star rings and mass account creation;
- automated starring/following/commenting;
- reward-gated Stars, votes, reviews, or referrals;
- mass unsolicited DMs or Issues;
- brigading Product Hunt, Hacker News, Reddit, or other platforms.

## Current external platform sources

- Hacker News requires a Show HN to be something the maker built that users can try, discourages barriers, forbids solicited votes/comments, and currently disallows generated or AI-edited comment text: [Show HN](https://news.ycombinator.com/showhn.html), [HN Guidelines](https://news.ycombinator.com/newsguidelines.html).
- Reddit prohibits repeated or unsolicited mass engagement and asks promoters to participate authentically and follow individual community rules: [Reddit Spam](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam).
- Product Hunt’s current guide says makers can share the launch link but cannot ask people directly to upvote; paying hunters/promoters for artificial traffic can lead to removal or bans: [Product Hunt Launch Guide](https://www.producthunt.com/launch), [Before Launch](https://www.producthunt.com/launch/before-launch).

When drafting for any platform, check its current rules and the specific community’s local rules. Provide a draft; do not impersonate the user or publish without authorization.

## Claim ledger format

Maintain this table for material claims:

| Proposed claim | Evidence | Evidence type | Confidence | Allowed wording | Missing verification |
|---|---|---|---|---|---|
| `<claim>` | `<file/link/user fact>` | official / repository / user / inference | high/medium/low | `<copy-safe wording>` | `<needed fact>` |

Remove low-confidence promotional claims from headline and release copy. Put honest limitations near the related claim, not only in a distant disclaimer.

