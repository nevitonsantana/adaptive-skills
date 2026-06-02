---
id: vc-debugging-cause-isolation-001
skill_id: debugging
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Diagnose why a fictional batch job intermittently writes duplicate rows.
  context: The reporter proposes a fix (add a unique constraint) before the cause is isolated. The skill should resist jumping to the fix.
expected_behavior:
  must_do:
    - Isolate the cause before recommending a fix.
    - State the smallest reproduction or evidence needed to confirm the cause.
    - Separate "symptom" from "cause" explicitly.
  must_not_do:
    - Endorse the proposed fix before the cause is confirmed.
    - Skip straight from symptom to remediation.
acceptance_criteria:
  - The response isolates a candidate cause and names how to confirm it before fixing.
  - The proposed fix is treated as a hypothesis, not a conclusion.
failure_signals:
  - The output recommends the unique constraint without isolating the cause.
  - Symptom and cause are conflated.
related_observations:
  - obs-2026-04-13-debugging-cause-isolation-seed
notes: Synthetic scenario modeled on the recurring "jump to fix before isolating cause" maintainer signal. No governed content used.
---

# Validation Case

## Scenario
A fictional batch job intermittently writes duplicate rows and the reporter wants to add a
unique constraint immediately. The expectation is that `debugging` isolates the cause first.

## Why this expectation is correct
The seed observation (`obs-2026-04-13-debugging-cause-isolation-seed`) captures a recurring
maintainer concern: some debugging usage jumps from symptom to fix too quickly. This case
makes that expectation testable — and is the *second* signal the observation asked for before
considering any module-level change.

## How a reviewer checks it
The response must isolate a candidate cause and name how to confirm it before endorsing any
fix. Recommending the constraint up front, or conflating symptom and cause, fails the case.
