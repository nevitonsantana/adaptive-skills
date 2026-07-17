---
title: "First Consumer Pilot Guide"
description: "Reference documentation for First Consumer Pilot Guide in Adaptive Skills."
---

## Goal

Run the first real adoption round of Adaptive Skills in another project without turning the pilot into a full migration.

The purpose of the pilot is to answer:
- can a small skill bundle improve execution quality?
- can the consumer team keep local overlays separate from the canon?
- do the projection and setup docs hold up under real use?

## Pilot scope

Keep the first pilot intentionally small.

Recommended shape:
- 1 project
- 1 team or lane
- 1 to 3 recurring task types
- 3 to 5 skills maximum
- 1 to 2 weeks of usage

Do **not** start with a whole-org rollout.

## Recommended starter bundle

Minimum bundle:
- `workflow`
- `feature-planning`
- `testing`

Optional add-ons by need:
- `debugging`
- `api-design`
- `premortem`
- `ux-writing`
- `heuristic-audit`
- `triad-check`

Use `premortem` only when the pilot lane includes a consequential plan that can still be changed. It is especially useful when the team needs to surface fragile assumptions, define gates, or decide whether to reduce scope before execution.

## Choose the lane

A good first pilot lane has these properties:
- work recurs often enough to compare before/after
- tasks are meaningful but not high-blast-radius
- the team can tolerate small process experiments
- at least one person can notice whether proof, handoff, or clarity improved

Examples:
- feature slicing for small backend or product changes
- UX copy clarity review in a dashboard or app flow
- API contract review for integration work
- debugging and regression review for a recurring class of bugs

## What to keep local

The consumer project should keep these local:
- ownership rules
- security or compliance controls
- release gates
- branch or review conventions
- project-specific vocabulary and domain truth

The pilot is successful when those local constraints stay local.

## Suggested pilot loop

### 1. Frame the lane

Write down:
- project name
- pilot lane
- skills in scope
- local overlays in scope
- pilot duration
- what would make the pilot worth continuing
- what would make the pilot too heavy to keep

### 2. Install only the chosen skills

For Codex-first pilots:
```bash
python3 scripts/project_to_codex.py --skill workflow
python3 scripts/project_to_codex.py --skill feature-planning
python3 scripts/project_to_codex.py --skill testing
```

For Claude-oriented pilots:
- start with `link-only` or `manual`
- adapt only a small subset

### 3. Use the skills in real work

Do not run artificial demos only.
Use the skills in real tickets, reviews, planning steps, or debugging loops.

For each use, record the reason the skill was selected. This helps distinguish good fit from novelty.

### 4. Capture evidence weekly

Track:
- which skills were used
- why each skill was selected
- where modules activated
- what improved
- what felt heavy or unnecessary
- where local overlays leaked into the generic layer

### 5. Decide what changes

At the end of the pilot, decide whether:
- the skill should stay as-is
- a module should be added or simplified
- an example is missing
- setup docs need clarification
- the consumer project should keep a local wrapper

## Success criteria

The first pilot is successful if:
- the team keeps using at least part of the bundle after the initial trial
- proof or planning quality visibly improves in at least one recurring task
- people can explain why a skill was selected
- the team does not feel forced into full-library adoption
- the canon stays clean while local project rules stay local

## Failure signals

- the pilot installs too many skills at once
- people cannot tell which skill to use
- every task feels slower with no quality gain
- skills are selected because they are available, not because the task needs them
- local project constraints keep getting copied into the canon
- the team tries to solve organizational problems with skills alone

## Output artifact

Use `templates/pilot/consumer-pilot-report.md` to capture the result of the first pilot.
