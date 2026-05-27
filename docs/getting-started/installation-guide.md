# Adaptive Skills — Installation Guide

> **One step.** Unlike AletheIA, Adaptive Skills does not require a second scaffold command. `apm install` materializes skills directly into your project. There is no `apm run install-skills` equivalent and none is needed.

This guide walks you through installing Adaptive Skills in a consumer project. Estimated time: 10–15 minutes.

---

## Prerequisites

Before you start, confirm:

1. **APM is installed.** Run `apm --version`. If not found, install it first:
   - Instructions: [microsoft.github.io/apm/installation](https://microsoft.github.io/apm/installation)
   - APM requires Node.js ≥ 18. Run `node --version` to confirm.

2. **You have a project directory.** Adaptive Skills installs into a consumer project. You can use an existing one or create a new directory:
   ```bash
   mkdir my-project && cd my-project
   git init
   ```

3. **You are in the project root.** Run `pwd` (macOS/Linux) or `cd` (Windows) and confirm you are at the top level.

4. **GitHub access.** The package resolves from `github.com/nevitonsantana/adaptive-skills`. The repository is public. For corporate proxies, configure APM credentials first: `apm config set github.token <your-pat>`.

---

## Option A — Install the full library (recommended for most teams)

```bash
apm install nevitonsantana/adaptive-skills
```

What happens:

- APM resolves the package from GitHub and writes `apm.lock.yaml`.
- All 21 skills are materialized into `.claude/skills/` (for Claude Code) or the equivalent target for your harness.

**Commit the lockfile** so teammates and CI get the same skill versions:

```bash
git add apm.lock.yaml
git commit -m "chore: add adaptive-skills apm.lock.yaml"
```

### Verify the install

```bash
ls .claude/skills/
```

You should see a folder per skill:

```
api-design  architecture-review  business-design  checkpoint-review
code-style  communication        debugging        feature-planning
handoff-summary  heuristic-audit  observability-review  premortem
qa-review   refactoring  task-chunking  testing  triad-check
ux-provocation  ux-strategy  ux-writing  workflow
```

Each folder contains a single `SKILL.md`. If any folders are missing, see [Troubleshooting](#troubleshooting).

---

## Option B — Install individual skills

For teams that want to start with a focused set:

```bash
apm install nevitonsantana/adaptive-skills --skill workflow --skill feature-planning --skill testing
```

The recommended starter bundle for a new consumer project:

| Skill | Why start here |
|---|---|
| `workflow` | Frames any non-trivial task with scope and proof before execution |
| `feature-planning` | Turns vague intent into a scoped, testable slice |
| `testing` | Calibrates the right level of validation — prevents both under- and over-testing |

Add skills as you encounter the need:

| When you need | Add |
|---|---|
| To stress-test a plan before execution | `premortem` |
| To diagnose a bug systematically | `debugging` |
| To pause mid-task and decide whether to continue | `checkpoint-review` |
| To pass work cleanly to the next session or person | `handoff-summary` |
| To bring product, design, and engineering perspectives together | `triad-check` |

The selection is persisted in your project's `apm.yml` and lockfile. Teammates reproduce the same set with `apm install` from the lockfile.

---

## What ships and what does not

| Included in the APM package | Not included |
|---|---|
| All 21 skills (`skills/**`) | `domain-packs/` (case studies — see below) |
| `docs/skill-categories.md` | `evolution/` (meta-process, not capability) |
| `docs/guides/install-via-apm.md` | `projections/`, `capabilities/`, `templates/` |
| `LICENSE`, `README.md` | Validation scripts (`scripts/validate_skills.py`, etc.) |

**Domain packs:** `domain-packs/crisis-management/` is excluded from the standard package — it is a case study, not the generic capability surface (see [ADR-002](../adr/ADR-002-domain-agnosticism.md)). To use it manually:

```bash
git clone https://github.com/nevitonsantana/adaptive-skills.git
cp -R adaptive-skills/domain-packs/crisis-management/skills/* .claude/skills/
```

---

## Using skills in a session

Once installed, skills are available in Claude Code automatically. To invoke a skill:

```
Use the workflow skill to frame this task before we start.
```

or simply:

```
run workflow
```

For harnesses other than Claude Code, see [`docs/codex-consumer-setup.md`](../codex-consumer-setup.md) for Codex projection or [`docs/how-to-use-a-skill.md`](../how-to-use-a-skill.md) for the general invocation pattern.

---

## Validate the install (optional)

The library ships with a reference validator. To confirm all installed skills are spec-conformant:

```bash
pip install 'skills-ref==0.1.0'   # PyPI package; ships the `agentskills` CLI
agentskills validate .claude/skills/
```

All skills should report conformant. This is the same check the library's CI runs on every PR (`skills-ref` is the PyPI distribution name; `agentskills` is the CLI entrypoint it installs).

---

## Updating

When a new version is published:

```bash
apm update nevitonsantana/adaptive-skills
```

Review the CHANGELOG before updating to understand what changed. Skills are versioned individually — a CHANGELOG entry will tell you which skills changed and whether any core moves were updated.

---

## Troubleshooting

**`apm: command not found`**  
APM is not installed or not on `$PATH`. Install from [microsoft.github.io/apm/installation](https://microsoft.github.io/apm/installation) and restart your shell.

**Install completes but `.claude/skills/` is empty**  
Your harness target may not be `claude`. Check your project's `apm.yml` for the `target:` value. If there is no `apm.yml`, APM defaults to the target in the package — which is `claude`. If you are using a different harness (Codex, Cursor, etc.), consult [APM target reference](https://microsoft.github.io/apm/reference/targets/).

**`apm install` fails with a network error**  
For corporate proxies or GitHub auth requirements: `apm config set github.token <your-pat>`. Run `apm install --verbose` for detailed output.

**A skill folder exists but the SKILL.md is empty**  
This should not happen on `main` — it indicates a release regression. Open an issue at [adaptive-skills/issues](https://github.com/nevitonsantana/adaptive-skills/issues) with the skill name.

**Claude Code does not seem to load the skills**  
Confirm `.claude/skills/` exists at the project root. In Claude Code, skills in `.claude/skills/` are available automatically when you start a session from that directory. If you started the session from a subdirectory, skills may not load — always start from the project root.

**`agentskills validate` fails on a skill**  
The installed skill is not spec-conformant. This is a library regression — open an issue. Do not manually edit the installed `SKILL.md` to fix the validation; it will be overwritten on the next `apm update`.

---

## What to do next

1. Pick your first skill: [`skill-catalog.md`](skill-catalog.md) — start with `workflow` if unsure
2. Learn how to invoke skills effectively: [`docs/how-to-use-a-skill.md`](../how-to-use-a-skill.md)
3. See composite flows (multiple skills for one task): [`skill-catalog.md#composite-flows`](skill-catalog.md#composite-flows)
4. Technical reference for this install: [`docs/guides/install-via-apm.md`](../guides/install-via-apm.md)
5. Using Adaptive Skills with AletheIA: [`docs/aletheia-integration.md`](../aletheia-integration.md)
