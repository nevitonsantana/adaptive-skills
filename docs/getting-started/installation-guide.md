---
title: Installation Guide
description: Install a focused starter set or the full Adaptive Skills library and verify the result safely.
---

This guide installs Adaptive Skills in a consumer project. If you only want to understand the library first, read the [overview](https://nevitonsantana.github.io/adaptive-skills/getting-started/overview/). If you want the shortest path to a first task, use the [quickstart](https://nevitonsantana.github.io/adaptive-skills/getting-started/quickstart/).

## Before you begin

You need:

- a project directory;
- Git;
- Node.js 18 or newer for APM;
- an AI environment that can consume `SKILL.md` files;
- permission to add configuration files to the project.

Adaptive Skills itself is Markdown. The installation tool places those files where the selected AI environment can discover them.

## Recommended: install a small starter set

Start with three skills:

```bash
apm install nevitonsantana/adaptive-skills \
  --skill workflow \
  --skill feature-planning \
  --skill testing
```

| Skill | Why it is useful first |
|---|---|
| `workflow` | Makes the goal, scope, proof, and next action explicit. |
| `feature-planning` | Turns feature intent into a small, testable delivery slice. |
| `testing` | Chooses proof that matches the change and its risk. |

Installing a focused set makes it easier to learn when each skill adds value. You can add more skills later.

## Alternative: install the full library

```bash
apm install nevitonsantana/adaptive-skills
```

This installs all **33 canonical generic skills**. Domain packs, repository governance records, capability metadata, and evolution artifacts are not part of the standard capability payload.

## What the installation changes

APM:

1. resolves the Adaptive Skills package;
2. records the selected version in `apm.lock.yaml`;
3. places each selected skill in the target directory for your AI environment;
4. allows teammates and CI to reproduce the same selection.

Commit the lockfile when it is appropriate for your project:

```bash
git add apm.lock.yaml
git commit -m "chore: install adaptive skills"
```

## Verify the result

For the Claude target, list the installed skills:

```bash
ls .claude/skills/
```

Each installed skill should have its own directory and a `SKILL.md` entrypoint.

You may also validate the installed collection:

```bash
pip install 'skills-ref==0.1.0'
agentskills validate .claude/skills/
```

## Environment-specific setup

- **Claude Code:** read [Claude consumer setup](https://nevitonsantana.github.io/adaptive-skills/claude-consumer-setup/).
- **Codex:** read [Codex consumer setup](https://nevitonsantana.github.io/adaptive-skills/codex-consumer-setup/). The repository also provides a Codex projection script for maintainers and source consumers.
- **Another compatible harness:** confirm where that harness expects `SKILL.md` files, then use the APM target or supported installation method for that location.

The detailed package contract and payload boundaries are documented in [Install via APM](https://nevitonsantana.github.io/adaptive-skills/guides/install-via-apm/).

## Update later

```bash
apm update nevitonsantana/adaptive-skills
```

Review the repository changelog before updating. Do not edit installed skill files directly if they are managed by APM; the next update may overwrite local changes.

## Troubleshooting

### `apm: command not found`

Install APM and restart the terminal. Confirm with:

```bash
apm --version
```

### The expected skill directory is empty

Confirm the selected APM target and the directory from which you started the AI environment. Harnesses normally discover project skills relative to the project root.

### Installation fails through a corporate network

Check proxy and GitHub access rules. Use the organization's approved credential mechanism; do not place personal access tokens in documentation, prompts, or committed files.

### The validator reports a failure

Record the skill name and validator output, then open an issue. Do not silently patch a managed installed file and treat the library as valid.

## Security boundary

Installing a skill makes instructions available to an AI environment. It does not itself grant file, network, secret, deployment, or write access. Those permissions belong to the harness and project policy.

Always review external skill sources before installation and keep consequential actions behind the project's normal approval controls.

## Next steps

1. [Run your first skill](https://nevitonsantana.github.io/adaptive-skills/getting-started/first-skill/).
2. [Learn the general usage loop](https://nevitonsantana.github.io/adaptive-skills/how-to-use-a-skill/).
3. [Browse the complete skill catalog](https://nevitonsantana.github.io/adaptive-skills/getting-started/skill-catalog/).
