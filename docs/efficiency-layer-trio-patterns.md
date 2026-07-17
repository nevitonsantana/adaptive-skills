---
title: "Efficiency Layer Trio Patterns"
description: "Reference documentation for Efficiency Layer Trio Patterns in Adaptive Skills."
---

## Purpose

Describe how the first Efficiency Layer trio should be used together without turning it into a mandatory process overlay.

The trio is:

- `task-chunking`
- `checkpoint-review`
- `handoff-summary`

This guide exists to make the combined pattern easier to reuse after the first pilot artifacts and the first-validation-case field reference (Crisis Monitor — see [`efficiency-layer-crisis-monitor-reference.md`](https://nevitonsantana.github.io/adaptive-skills/efficiency-layer-crisis-monitor-reference/)) landed.

## Core idea

The trio is not three separate ceremonies.
It is one lightweight operating loop for bounded work:

1. keep the slice small
2. pause before accidental expansion
3. close the round in a resumable way

## The simplest sequence

### 1. Start with `task-chunking`

Use it when the round arrives too large or too fuzzy.

Its job is to answer:

- what is the smallest useful slice now?
- what belongs later?
- what is the stop condition for this round?

### 2. Use `checkpoint-review` before continuing blindly

Use it when the round is no longer obviously the same small slice.

Its job is to answer:

- did the task change shape?
- should the round continue?
- should it stop or hand off instead?

### 3. End with `handoff-summary` when the round should resume later

Use it when continuity matters but dragging the whole session forward would be wasteful.

Its job is to leave:

- current state
- proof already obtained
- open edge or next step
- the safest resume point

## Common patterns

### Pattern A — bounded single-round delivery

Use:

- `task-chunking`
- maybe `checkpoint-review`

Skip `handoff-summary` when the round ends cleanly and nothing meaningful needs to be resumed.

### Pattern B — pause and resume in the same lane

Use:

- `task-chunking`
- `checkpoint-review`
- `handoff-summary`

This is the default trio pattern for work that will continue later.

### Pattern C — prevent slice creep

Use:

- `task-chunking` early
- `checkpoint-review` whenever adjacent follow-up tries to enter the same round

`handoff-summary` only matters if the deferred next slice really needs a resumable note.

## What the trio should not become

The trio should not become:

- a required ritual for every task
- a replacement for `feature-planning`
- a replacement for `workflow`
- a hidden AletheIA clone
- a long written template for trivial work

## Boundary with other skills

### vs `feature-planning`

- `feature-planning` defines the feature slice and acceptance logic
- `task-chunking` keeps active execution from growing past a healthy round

### vs `workflow`

- `workflow` stabilizes objective, proof, and execution posture
- the efficiency trio reduces avoidable waste inside the round

### vs AletheIA

- AletheIA remains the macro layer for framing, gates, escalation, and continuity posture
- the efficiency trio is the micro operating discipline inside the round

## Failure signals

Revisit the trio usage if:

- chunk notes are almost as large as the work itself
- checkpoint reviews happen constantly without changing decisions
- handoff summaries repeat full session history
- the team cannot tell whether a problem belongs to planning, macro framing, or efficiency

## Healthy outcomes

The trio is working well when:

- work enters smaller
- sessions stop earlier and more intentionally
- resumptions are lighter
- fewer adjacent ideas leak into the same round

## Recommended follow-up

Use this guide together with:

- `docs/efficiency-layer-first-pilot.md`
- `docs/efficiency-layer-crisis-monitor-reference.md`
- `docs/efficiency-layer-pilot-checklist.md`
- `examples/efficiency/crisis-monitor-efficiency-reference.md`
