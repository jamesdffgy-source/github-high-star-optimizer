# Cross-agent compatibility guide

Read this reference when installing, packaging, or documenting the Skill for Codex, Claude Code, or another host that implements the Agent Skills standard.

Sources were reviewed on 2026-08-27. Host behavior and install locations can change; verify current official documentation before publishing exact setup commands.

## Portable core

Keep one canonical skill directory:

```text
github-high-star-optimizer/
├── SKILL.md
├── agents/
├── assets/
├── references/
└── scripts/
```

The portable contract is the [Agent Skills specification](https://agentskills.io/specification): a directory containing `SKILL.md` with `name` and `description`, plus optional scripts, references, and assets. Use relative links from `SKILL.md` and keep host-specific metadata optional.

Do not copy the same Skill into multiple platform folders inside the source repository. Duplicate copies drift. Distribute one canonical package and document where each host loads it.

## Compatibility matrix

| Host | Status | Personal location | Project location | Explicit invocation |
|---|---|---|---|---|
| Codex | Core structure and distribution publisher locally validated | `$HOME/.agents/skills/<skill-name>` | `$REPO_ROOT/.agents/skills/<skill-name>` | Type `$skill-name`; `/skills` lists skills in CLI/IDE |
| Claude Code | Official structure documented; runtime test pending | `~/.claude/skills/<skill-name>` | `.claude/skills/<skill-name>` | `/skill-name` |
| Other Agent Skills hosts | Format-compatible by design | Host-specific | Host-specific | Host-specific |

OpenAI’s [Build skills documentation](https://developers.openai.com/codex/skills/) states that Codex reads repository and user skills from `.agents/skills`, detects changes automatically, and can install skills from other repositories through `$skill-installer`. Anthropic’s [Claude Code skills documentation](https://code.claude.com/docs/en/skills) states that Claude Code follows the Agent Skills open standard and reads personal and project skills from `.claude/skills`.

“Format-compatible” does not prove that every host exposes the same tools, permissions, invocation syntax, or live publishing capability. State only the compatibility that has been verified. Do not label Claude Code runtime behavior as tested until it has been executed in an actual Claude Code session.

## Portability invariants

- Keep the core frontmatter within the Agent Skills specification. Do not add host-only invocation fields unless the user explicitly requests a host-specific variant.
- Treat `agents/openai.yaml` as optional OpenAI UI metadata. Other hosts may ignore it; the core Skill must not depend on it.
- Do not depend on Claude Code-only dynamic injection, arguments, subagent frontmatter, or tool allowlists in the portable core.
- Refer to supporting files with relative paths and keep the important references directly linked from `SKILL.md`.
- Describe required capabilities, not a fixed tool name. For example, require “current GitHub search access” rather than assuming one browser or CLI.
- Preserve the same authorization boundary on every host. Host portability never grants permission to rename, push, release, post, or change live settings.
- When a host lacks image generation, GitHub access, browser control, or shell access, produce a brief or copy-ready payload instead of pretending the mutation occurred.
- The optional distribution publisher requires Python 3.10+ and shell access. Hosts without that runtime can still prepare the portable manifest, content files, and assisted queue instructions; do not label API delivery as tested there.

## Installation documentation requirements

A public Quickstart should provide:

1. one installer-assisted path when the host supports it;
2. one manual personal-scope path;
3. optional project-scope paths for Codex and Claude Code;
4. the exact invocation syntax for each named host;
5. a discovery check and restart fallback;
6. a warning not to overwrite an existing same-name skill without review.

Use the repository’s `docs/INSTALLATION.md` as the public pattern. Keep commands aligned with current official host documentation.

## Verification

After any portability change:

- run the available Agent Skills or host-specific validator against the canonical directory;
- verify every relative reference resolves after copying only the Skill directory;
- confirm optional host metadata is not required by the core workflow;
- test discovery and explicit invocation in each host before labeling it “tested”;
- record untested hosts as format-compatible or documented, not verified.
