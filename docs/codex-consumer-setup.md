---
title: "Codex Consumer Setup"
description: "Reference documentation for Codex Consumer Setup in Adaptive Skills."
---

## Goal

Use Adaptive Skills from another project with a small, predictable Codex-first setup.

This guide assumes:
- the consumer project has its own local operating rules
- Adaptive Skills remains the reusable skill canon
- Codex skills are installed under `~/.codex/skills`

Projection is the delivery step, not the adoption strategy. Choose the smallest useful skill set before installing anything.

## Recommended setup order

### 1. Clone or reference the repository

You can keep the repository as a standalone checkout and project from it:

```bash
git clone https://github.com/nevitonsantana/adaptive-skills.git
cd adaptive-skills
```

### 2. Choose the skills before projecting

Read:

- `docs/how-to-use-a-skill.md`
- `docs/consumer-adoption.md`

Then write down:

- the consumer task or lane
- the skills in scope
- why each skill is needed
- which local rules must stay in the consumer project

For a first consumer project, start with:

- `workflow`
- `feature-planning`
- `testing`

Add `premortem` only when the plan has meaningful cost of failure and can still be changed before execution.

### 3. Validate before projecting

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_evolution.py
python3 scripts/report_projection_status.py
```

This confirms:
- skill contracts are structurally valid
- evolution metadata is coherent
- registry entries resolve correctly
- Claude modes remain explicit

### 4. Preview selected Codex projection

Preview the selected skills first:

```bash
python3 scripts/project_to_codex.py --skill workflow --dry-run
python3 scripts/project_to_codex.py --skill feature-planning --dry-run
python3 scripts/project_to_codex.py --skill testing --dry-run
```

Use `--all --dry-run` for repo maintenance or full projection review, not as the default first-adoption path:

```bash
python3 scripts/project_to_codex.py --all --dry-run
```

Use preview output to verify what would be installed into `~/.codex/skills`.

### 5. Install the selected skills

For the starter bundle:

```bash
python3 scripts/project_to_codex.py --skill workflow
python3 scripts/project_to_codex.py --skill feature-planning
python3 scripts/project_to_codex.py --skill testing
```

Install more only when the project truly needs them.

### 6. Confirm local availability

After projection, check the target directory:

```bash
ls ~/.codex/skills
```

Then use the skills in real work before adding more.

### 7. Keep project-local overlays local

Your consumer project may still need files such as:
- `AGENTS.md`
- `CLAUDE.md`
- project-specific decision logs
- release or security rules

Those files should describe the local operating model.
They should not duplicate the skill canon.

## Suggested first bundle by project need

### General product or feature work
- `workflow`
- `feature-planning`
- `testing`

### Contract and backend work
- `workflow`
- `api-design`
- `testing`
- `debugging`

### UX clarity and copy work
- `ux-writing`
- `heuristic-audit`

### Cross-functional decision pressure test
- `triad-check`
- `communication`

### Consequential planning or launch risk
- `workflow`
- `feature-planning`
- `premortem`
- `testing`

## Drift checks

To compare the repo canon against the local Codex installation:

```bash
python3 scripts/project_to_codex.py --check
```

Use this when:
- the repo changed
- a skill was edited locally by mistake
- you want to confirm what is missing versus what has drifted

Do not use drift checks as a reason to install every skill. Missing can be healthy if the consumer project intentionally selected a smaller bundle.

## Suggested operating model in a consumer repo

A practical split is:
- Adaptive Skills -> reusable skill canon
- consumer repo -> local ownership, security, review, and release rules
- AletheIA (optional) -> macro framing, proof expectations, handoff, continuity

## What not to do

- do not install every skill on day one
- do not use `--all` as the default adoption path
- do not move project-local policies into generic skills
- do not treat projection as the source of truth
- do not assume Claude should mirror Codex installation in v0
