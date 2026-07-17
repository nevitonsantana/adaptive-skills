---
title: "Evolution Layer"
description: "Reference documentation for Evolution Layer in Adaptive Skills."
---

## Why this layer exists

Adaptive Skills already treats skills as reusable, structured, and portable.
The next step is to let the library improve through real usage without turning it into an unrestricted self-rewriting system.

The evolution layer exists to make that improvement:

- visible
- reviewable
- domain-aligned
- safe enough to govern by pull request

## Core thesis

Skills should improve through use, but the improvement loop must stay governed.

This repository therefore uses an explicit loop:

1. **Observe** — capture what happened in a real task or pilot.
2. **Read** — review the current skill, modules, sidecars, and fit.
3. **Execute** — assess how the skill was actually used.
4. **Reflect** — separate local friction from reusable library friction.
5. **Attribute** — decide whether the issue belongs to the skill, the trigger, the module, the surrounding operating system, or nowhere.
6. **Propose** — write an auditable proposal when change is justified.
7. **Govern** — decide whether the proposal is accepted, rejected, deferred, or downgraded to no-change.
8. **Write** — update the library only after review.

## Implemented now — Evolution Layer v1.1

The current v1.1 baseline is already implemented through:

- `docs/evolution-layer.md`
- `evolution/registry.json`
- `evolution/observations/`
- `evolution/proposals/`
- `evolution/reviews/`
- `scripts/validate_evolution.py`

Decisions already taken in v1.1:

- repository-level governance instead of per-skill logs
- no auto-writeback into `SKILL.md`
- no mandatory `telemetry.md` or `improvement-log.md` inside every skill
- success-aware outcomes such as `reinforced` and `no-change`
- a small, domain-aligned pilot using a limited initial skill set

## Editorial decision

**The Evolution Layer v1.1 is considered structurally correct and will not be reworked into a per-skill logging model right now.**

This avoids reopening decisions that were intentionally chosen for v1.1:

- centralised evidence
- lighter governance
- less bureaucracy per skill
- canonical writeback only through pull request

## What this is not

This is not a self-rewrite runtime.
In v1.1:

- skills do **not** edit themselves automatically
- the canon in `skills/` and `domain-packs/` is still changed by normal pull requests
- observations and proposals are repository-level artifacts, not hidden memory

The inspiration from systems such as Memento-Skills is the governed learning loop, not automatic mutation of the public library.

## Success-aware outcomes

Not every observation should change the library.
Valid outcomes include:

- `reinforced` — the skill worked and the case strengthens confidence in the current design
- `no-change` — the issue was local, macro-layer, or not a library problem
- `proposal-created` — a concrete improvement proposal is justified
- `new-module-candidate` — repeated context suggests a module may be missing
- `new-skill-candidate` — repeated evidence suggests the current skill boundary is too small
- `rejected` — a proposed change should not enter the library

## Implemented structure versus deferred structure

### Adopted in v1.1

```txt
evolution/
  registry.json
  observations/
  proposals/
  reviews/
  templates/
```

This is the current, supported structure.
It is enough for governed learning without making every skill heavier.

### Deferred for Evolution Layer v1.2+

```txt
skill-name/
  telemetry.md
  improvement-log.md
```

This structure is **not adopted in v1.1**.
It remains a future candidate only if real pilot scale shows that the repository-level structure is no longer sufficient.

The same is true for a future split such as:

```txt
telemetry/
  skill-usage/
  skill-failures/
  skill-opportunities/

improvements/
  proposals/
  approved/
  rejected/

experiments/
  automated-refinement/
```

That may become useful later, but it should not be treated as missing work in the current baseline.

## Protected versus proposal-safe surfaces

The v1.1 layer protects the most conceptually sensitive surfaces:

- skill identity and thesis
- `When to Use` / `When NOT to Use`
- `Core Moves`
- category and domain boundaries
- merge or split decisions for skills

The layer is more open to proposals for:

- `Activation Triggers`
- `Optional Modules`
- `Verification`
- `Anti-patterns`
- `templates/`, `checklists/`, `examples/`, `references/`, and `changelog.md`

## Initial pilot

The first evolution pilot is intentionally small and domain-aligned.
It focuses on:

- `workflow`
- `feature-planning`
- `testing`
- `debugging`
- `ux-writing`

It also uses the first validation case (Crisis Monitor + AletheIA — see [`crisis-monitor-case-study.md`](https://nevitonsantana.github.io/adaptive-skills/crisis-monitor-case-study/) for the labeled field record) as seed evidence, especially where the library needs to distinguish:

- a good local fix
- a reinforced skill
- a true proposal-worthy library gap

Per [ADR-002](https://nevitonsantana.github.io/adaptive-skills/adr/ADR-002-domain-agnosticism/), this case is the first instance, not the canonical reference. New observations from other consumer projects are expected and prioritized — the reformulated Evolution Cycle #4 (2026-05-21 → 2026-06-30) reclassifies existing observations against the agnosticism criterion.

## Evolution Layer vs Efficiency Layer

These are related but different tracks.

- **Evolution Layer** improves the library itself.
- **Efficiency Layer** improves how work is carried out with the library.

Examples:

- if `feature-planning` has a weak trigger or sidecar gap, that belongs to the Evolution Layer
- if tasks keep arriving too large across many sessions, that belongs to the Efficiency Layer
- if handoffs are poor because a skill boundary is weak, that belongs to the Evolution Layer
- if handoffs are poor because teams lack a good end-of-round practice, that belongs to the Efficiency Layer

## New track — Efficiency Layer v0

Efficiency Layer is a separate, future track.
It is **not** part of the Evolution Layer v1.1 baseline.

Its purpose is to improve operational efficiency around:

- context growth
- task chunking
- prompt quality
- checkpoints
- handoff summaries
- model-class calibration

See `docs/efficiency-layer.md` for the roadmap.

## Relation to AletheIA

AletheIA may eventually help coordinate this layer by surfacing repeated breakdowns, handoff friction, and continuity signals.
But Adaptive Skills must remain useful without AletheIA.
The evolution layer therefore stays repository-native and review-native in v1.1.

## Recommended next step

Do not restructure the Evolution Layer further right now.
The next sensible move is:

- merge the current Evolution Layer work
- keep using the bounded pilot
- observe whether the repository-level artifacts remain sufficient
- plan Efficiency Layer v0 separately, beginning with:
  - `task-chunking`
  - `handoff-summary`
  - `checkpoint-review`
