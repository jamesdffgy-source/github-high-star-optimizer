# Installation and Quickstart

GitHub High-Star Optimizer is one canonical [Agent Skills](https://agentskills.io/specification) package. Codex and Claude Code use the same `github-high-star-optimizer` directory; only their discovery locations and invocation syntax differ.

## Codex — installer-assisted

Ask Codex:

```text
Use $skill-installer to install the skill from
https://github.com/jamesdffgy-source/github-high-star-optimizer/tree/main/github-high-star-optimizer
```

Codex detects installed skills automatically. If it does not appear, restart Codex. In Codex CLI or the IDE extension, use `/skills` to inspect available skills or type `$github-high-star-optimizer` to invoke it.

## Codex — manual personal installation

From the parent directory where you want to clone the repository:

### macOS / Linux

```bash
git clone https://github.com/jamesdffgy-source/github-high-star-optimizer.git
cd github-high-star-optimizer
mkdir -p "$HOME/.agents/skills"
cp -R ./github-high-star-optimizer "$HOME/.agents/skills/"
```

### Windows PowerShell

```powershell
git clone https://github.com/jamesdffgy-source/github-high-star-optimizer.git
Set-Location .\github-high-star-optimizer
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse .\github-high-star-optimizer "$HOME\.agents\skills\"
```

For a repository-scoped Codex installation, copy the Skill directory to `<repository>/.agents/skills/github-high-star-optimizer` instead.

Invoke it:

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

## Claude Code

Clone the repository, then copy the same inner Skill directory to one of the official Claude Code locations:

- personal: `~/.claude/skills/github-high-star-optimizer/`
- project: `<repository>/.claude/skills/github-high-star-optimizer/`

### macOS / Linux personal installation

```bash
git clone https://github.com/jamesdffgy-source/github-high-star-optimizer.git
cd github-high-star-optimizer
mkdir -p "$HOME/.claude/skills"
cp -R ./github-high-star-optimizer "$HOME/.claude/skills/"
```

### Windows PowerShell personal installation

```powershell
git clone https://github.com/jamesdffgy-source/github-high-star-optimizer.git
Set-Location .\github-high-star-optimizer
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\github-high-star-optimizer "$HOME\.claude\skills\"
```

Invoke it in Claude Code:

```text
/github-high-star-optimizer Audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

Claude Code watches existing skill directories for changes. If the top-level skills directory did not exist when the session started, restart Claude Code once.

## Other Agent Skills-compatible hosts

Copy the canonical `github-high-star-optimizer` directory into the host’s documented Skill location. Invocation syntax, available tools, permissions, and live GitHub publishing capabilities vary by host; check that host’s current official documentation.

Do not interpret format compatibility as proof that every host can generate images, browse the web, access GitHub, or publish externally. When those capabilities are unavailable, the Skill should produce a local audit or launch package instead.

## Verification prompt

After installation, ask for a read-only audit:

```text
Audit this repository's public GitHub presentation. Do not modify files or live settings.
First state the operating mode and the evidence sources you will inspect.
```

A correct activation should identify **Audit** mode and retain the no-code-change and no-unapproved-publishing boundaries.

## Existing installation warning

If a same-name Skill directory already exists, compare it before copying. Do not silently overwrite local customizations.

## Official references

- [OpenAI: Build skills](https://developers.openai.com/codex/skills/)
- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [Agent Skills specification](https://agentskills.io/specification)
