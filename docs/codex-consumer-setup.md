# Codex Consumer Setup

## Goal

Use Adaptive Skills from another project with a small, predictable Codex-first setup.

This guide assumes:
- the consumer project has its own local operating rules
- Adaptive Skills remains the reusable skill canon
- Codex skills are installed under `~/.codex/skills`

## Recommended setup order

### 1. Clone or reference the repository

You can keep the repository as a standalone checkout and project from it:

```bash
git clone https://github.com/nevitonsantana/adaptive-skills.git
cd adaptive-skills
```

### 2. Validate before projecting

```bash
python3 scripts/validate_skills.py
python3 scripts/report_projection_status.py
```

This confirms:
- skill contracts are structurally valid
- registry entries resolve correctly
- Claude modes remain explicit

### 3. Preview Codex projection

```bash
python3 scripts/project_to_codex.py --all --dry-run
```

Use this to verify what would be installed into `~/.codex/skills`.

### 4. Install the selected skills

For a first consumer project, start with:

```bash
python3 scripts/project_to_codex.py --skill workflow
python3 scripts/project_to_codex.py --skill feature-planning
python3 scripts/project_to_codex.py --skill testing
```

Install more only when the project truly needs them.

### 5. Keep project-local overlays local

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

## Drift checks

To compare the repo canon against the local Codex installation:

```bash
python3 scripts/project_to_codex.py --check
```

Use this when:
- the repo changed
- a skill was edited locally by mistake
- you want to confirm what is missing versus what has drifted

## Suggested operating model in a consumer repo

A practical split is:
- Adaptive Skills -> reusable skill canon
- consumer repo -> local ownership, security, review, and release rules
- AletheIA (optional) -> macro framing, proof expectations, handoff, continuity

## What not to do

- do not install every skill on day one
- do not move project-local policies into generic skills
- do not treat projection as the source of truth
- do not assume Claude should mirror Codex installation in v0
