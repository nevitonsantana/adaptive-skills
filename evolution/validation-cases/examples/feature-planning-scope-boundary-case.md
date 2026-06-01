---
id: vc-feature-planning-scope-boundary-001
skill_id: feature-planning
case_type: baseline
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Plan the first slice of a "saved filters" feature for a fictional support-ticket tool.
  context: A successful first slice ships. A stakeholder immediately asks to also add shared team filters, filter folders, and a filter API in the same iteration.
expected_behavior:
  must_do:
    - Deliver a smallest-slice plan with scope, risks, slices, and proof.
    - Record an explicit reason the next expansion is deferred until a real trigger appears.
    - Name the concrete trigger that would justify expanding (e.g. repeated requests, measured reuse).
  must_not_do:
    - Fold all four requested capabilities into the first slice.
    - Treat "a stakeholder asked" as sufficient justification to expand now.
acceptance_criteria:
  - The plan output contains a deferred-expansion rationale that a reviewer can point to.
  - The deferral names a falsifiable trigger, not a vague "later".
failure_signals:
  - Expansion is bundled into slice one with no trigger.
  - The output silently drops the extra requests with no recorded reason.
related_observations:
  - obs-2026-04-13-feature-planning-expansion-trigger-gap
notes: Derived from the Crisis Monitor two-round pilot signal. Scenario is synthetic; no governed content used.
---

# Validation Case

## Scenario
A fictional support-ticket tool ships a working "saved filters" first slice. A stakeholder
immediately pushes to add shared filters, folders, and an API in the same iteration. The
skill should hold the smallest-slice line *and* make the deferral legible.

## Why this expectation is correct
The `feature-planning` skill already supports smallest-slice discipline. The real
observation `obs-2026-04-13-feature-planning-expansion-trigger-gap` showed the gap is not
in the discipline but in making the *why-not-now* explicit and tied to a trigger.

## How a reviewer checks it
Look for a deferred-expansion rationale in the plan that names a concrete, falsifiable
trigger. If expansion is bundled in, or the extra asks vanish with no recorded reason, the
case fails.
