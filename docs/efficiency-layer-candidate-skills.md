---
title: "Efficiency Layer — First Candidate Skills"
description: "Reference documentation for Efficiency Layer — First Candidate Skills in Adaptive Skills."
---

## Why these three come first

The first Efficiency Layer candidates should solve repeated operational problems without collapsing into orchestration policy.

That is why the first set is:

- `task-chunking`
- `handoff-summary`
- `checkpoint-review`

They improve how work is carried out, but they do not require the repository to make stronger assumptions about model runtime, memory systems, or hidden orchestration.

---

## `task-chunking`

**Status:** published in `skills/task-chunking/` as the first Efficiency Layer skill.


### Purpose
Break oversized work into smaller, reviewable, and more testable slices.

### Helps when
- a task keeps entering as one large block
- the first useful slice is still unclear
- dependencies are making the task feel bigger than necessary

### Expected output
- smallest useful slice
- next slice boundary
- dependency notes
- stop condition for the current slice

### Boundary
- If the problem is feature definition, `feature-planning` is still primary.
- `task-chunking` is transversal: it helps keep execution bounded after or alongside planning.

---

## `handoff-summary`

**Status:** published in `skills/handoff-summary/` as the second Efficiency Layer skill.


### Purpose
Close one round of work with enough context for the next round without dragging the whole session forward.

### Helps when
- work must continue later
- another person or agent will resume it
- the context is getting heavy and a clean restart is healthier

### Expected output
- current state
- what was already proved
- what remains open
- next recommended step
- known risks or missing evidence

### Boundary
- If the handoff is about macro gate, review, or cross-boundary continuity, AletheIA remains the macro layer.
- `handoff-summary` is the micro execution aid for ending a round cleanly.

---

## `checkpoint-review`

**Status:** published in `skills/checkpoint-review/` as the third Efficiency Layer skill.


### Purpose
Insert a short, useful pause between rounds so teams do not keep pushing work forward blindly.

### Helps when
- the session is growing long
- the task shape changed mid-way
- the team needs to decide whether to continue, stop, or hand off

### Expected output
- what changed in this round
- what is now known
- whether the next step belongs in the same round
- whether a handoff or stop is healthier

### Boundary
- If the task needs formal gate or escalation, AletheIA remains responsible for macro posture.
- `checkpoint-review` is the lighter operating pattern for local round discipline.

---

## Why the others are deferred

### `context-compression`
Useful, but closer to memory/summary systems and therefore riskier to define too early.

### `prompt-framing`
Useful, but can overlap with general task framing, consumer onboarding, and AletheIA macro framing.

### `model-routing`
Useful, but too close to orchestration and model strategy; it should wait until the simpler efficiency skills are better proven.
