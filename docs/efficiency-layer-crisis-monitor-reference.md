# Efficiency Layer — Crisis Monitor Reference

## Purpose

Use the Crisis Monitor case as the first real reference for the Efficiency Layer trio **without** turning the product repo into a new implementation target.

This document exists because the Crisis Monitor lane already proved a healthy macro/micro split with:

- **AletheIA** as the macro layer
- **Adaptive Skills** as the micro layer
- a small, auditable product lane as the real field context

The next useful move is not a fourth efficiency skill.
It is to show how the first efficiency trio can be read against that same kind of lane.

## Why Crisis Monitor is a good reference case

The Crisis Monitor pilots already had the right shape:

- a bounded lane
- recurring rounds
- explicit proof expectations
- handoff sensitivity
- a real risk of context and slice creep if the work grows carelessly

That makes the lane a good reference for efficiency patterns, even if the actual product repo is not the place to edit right now.

## Reference lane

Use the same small lane previously validated in Crisis Monitor:

- routing
- approval
- follow-up explainability
- auditable closure between chat, audit trail, and summary

This lane is useful because it is small enough to stay reviewable, but rich enough to expose:

- oversized round risk
- pause-or-continue decisions
- resumable handoff needs

## How the trio maps to the lane

### `task-chunking`

Use it when the lane starts arriving as one broad change instead of one bounded round.

In this reference case, it should help separate:

- current-round change
- next-round change
- local follow-up that does not belong in the present slice

It does **not** replace `feature-planning`.
It helps keep an already chosen lane small enough to execute cleanly.

### `checkpoint-review`

Use it when the round reaches a natural pause and the team needs to decide:

- continue in the same round
- stop cleanly
- hand off to another round or owner

In the Crisis Monitor reference case, this matters when a lane stays technically open but the next step is no longer the same smallest useful slice.

### `handoff-summary`

Use it when the lane should resume later without dragging the full prior context forward.

In this reference case, the handoff should stay short and operational:

- what was done
- what was proved
- what remains open
- what should happen next

It should not try to duplicate AletheIA macro review or local product governance.

## Boundary with AletheIA

In the Crisis Monitor reference case:

- **AletheIA** still owns macro framing, proof expectation, review posture, and continuity logic
- **Efficiency Layer** owns lighter operating discipline inside the round

If the question is:

- what the round is really for
- whether the lane should escalate
- whether a cross-boundary handoff is needed

that is still AletheIA territory.

If the question is:

- whether the current slice is too big
- whether the round should stop now
- how to leave a resumable note

that is where the efficiency trio helps.

## Boundary with local product overlays

This reference case should not absorb product-local rules into the library.

Keep local to Crisis Monitor:

- thread ownership
- product semantics
- rollout policy
- approval policy
- domain-specific trust or audit rules

The point of the reference is to show the trio working **inside** a real lane, not to convert local operating policy into generic skill canon.

## What this reference should prove

A useful first reference pass should show that:

- the trio can fit a real product lane without inflating the process
- `task-chunking` keeps the lane smaller
- `checkpoint-review` makes stop-or-continue explicit
- `handoff-summary` makes the next round lighter to resume
- none of this collapses into hidden AletheIA replacement

## What this reference should not try to prove

This is **not** trying to prove that:

- every Crisis Monitor lane needs the trio
- the trio belongs in every project by default
- the product repo should be reworked around efficiency artifacts
- a fourth efficiency skill is already justified

## Recommended use

Treat this document as a field reference for the first Efficiency Layer pilot.

Use it together with:

- `docs/efficiency-layer-first-pilot.md`
- `docs/efficiency-layer-pilot-checklist.md`
- `templates/pilot/efficiency-pilot-report.md`
- `examples/efficiency/crisis-monitor-efficiency-reference.md`
