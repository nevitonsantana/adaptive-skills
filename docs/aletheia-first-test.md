---
title: Run the first AletheIA test
description: Validate the macro-governance and micro-execution split with one small, evidence-producing task.
---

This exercise tests whether AletheIA and Adaptive Skills remain understandable when used together. It is an operating test, not a benchmark or runtime integration.

## Before you begin

Choose one small feature-like task that:

- has a clear human owner;
- can be completed in one bounded Work Slice;
- produces visible proof;
- does not require sensitive or restricted context for the first trial.

Use this initial skill set:

- `workflow`;
- `feature-planning`;
- `testing`.

Add `triad-check` only when the task genuinely crosses product, design, and engineering.

## Step 1 — Let AletheIA frame the task

Record:

- the goal;
- the immediate boundary;
- explicit non-goals;
- minimum closure evidence;
- review or handoff gates;
- known uncertainty.

Do not select a large skill bundle during framing.

## Step 2 — Use skills for micro execution

Run one skill at a time:

1. `workflow` makes the local execution boundary and next step explicit.
2. `feature-planning` defines the smallest useful delivery slice.
3. `testing` defines proof proportionate to risk.

Inspect each output before invoking the next skill. A skill may expose a reason to stop, review, or change the plan.

## Step 3 — Return evidence

Capture:

- which skill and modules were used;
- the usable, partial, failed, or unavailable result;
- authoritative evidence references;
- known risks and missing values;
- the advisory handoff signal.

Use the [skill observation return pattern](skill-observation-return-pattern/) when a structured return helps. Do not infer unavailable values.

## Step 4 — Let AletheIA evaluate closure

The governing layer checks:

- whether the selected skills matched the Work Slice;
- whether evidence satisfies the declared gate;
- whether a human review or handoff is required;
- whether a repeated failure should become an observation;
- whether the slice should continue, change, escalate, or close.

The skill output informs this decision but does not make it.

## Record what you learned

At the end, write:

- what AletheIA governed;
- what each skill contributed;
- what remained consumer-local;
- what felt clear or redundant;
- what evidence was available or missing;
- the next safe improvement, if any.

Use the repository's first-test report template in your local copy: `examples/aletheia/first-test-report.md`.

## Success criteria

The trial succeeds when:

- the macro/micro split remains legible;
- framing and proof improve with low overhead;
- the skill set stays small;
- evidence remains source-backed;
- project-local rules are not mistaken for generic library behavior.

## Failure signals

Stop and review when:

- AletheIA duplicates skill internals;
- a skill starts deciding macro gates or closure;
- proof ownership becomes unclear;
- the setup is disproportionate to the task;
- the workflow requires invented evidence or unavailable measurements.

## Next steps

- Compare the result with [Adaptive Skills and AletheIA](aletheia-integration/).
- Read [Observation and evidence return](skill-observation-return-pattern/) before formalizing the record.
- Use [Workflow recipes](guides/workflow-recipes/) for later tasks, while preserving AletheIA as the governing frame.
