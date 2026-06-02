---
id: vc-workflow-bounded-lane-001
skill_id: workflow
case_type: baseline
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Frame a small, reversible change to a fictional internal dashboard before any code is written.
  context: A two-round effort that should stay inside a narrow, auditable lane. The team has clear macro framing and local ownership; the risk is scope leaking outward mid-task.
expected_behavior:
  must_do:
    - Produce explicit scope, proof, and next step before execution.
    - Keep the work inside one reversible lane.
    - Make the proof for "this stayed in lane" legible to a reviewer.
  must_not_do:
    - Expand the lane without an explicit reason.
    - Defer naming the proof until after execution.
acceptance_criteria:
  - The framing names scope, proof, and next step up front.
  - A reviewer can confirm the lane stayed bounded from the output alone.
failure_signals:
  - Scope widens silently across the two rounds.
  - Proof is implicit or only stated retroactively.
related_observations:
  - obs-2026-04-13-workflow-crisis-monitor-bounded-lane
notes: Synthetic scenario modeled on the Crisis Monitor bounded-lane signal. No governed content used.
---

# Validation Case

## Scenario
A fictional internal dashboard gets a small, reversible change handled across two rounds. The
expectation is that `workflow` keeps the work bounded and explicit without any added move.

## Why this expectation is correct
The source observation (`obs-2026-04-13-workflow-crisis-monitor-bounded-lane`) concluded the
lane was healthy because macro framing and local ownership were already clear — the skill
itself did not need adjustment. This case captures that baseline expectation so a future
candidate can be tested against it rather than assumed.

## How a reviewer checks it
Confirm scope/proof/next-step are stated up front and the lane stays bounded across both
rounds. Silent scope growth or retroactive proof fails the case.
