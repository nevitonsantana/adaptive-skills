---
id: vc-testing-acceptance-evidence-001
skill_id: testing
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Decide the minimum reliable proof for a one-line copy change to a marketing banner.
  context: A fictional team tends to either skip proof entirely for "trivial" changes or demand a full regression suite regardless of risk.
expected_behavior:
  must_do:
    - Scale the proof to risk, reversibility, and impact.
    - Recommend a proportionate, minimal check (e.g. visual confirmation) for a low-risk, easily reversible change.
    - State why a heavier test layer is not warranted here.
  must_not_do:
    - Recommend a full regression suite for a trivial reversible copy change.
    - Recommend zero proof at all.
acceptance_criteria:
  - The recommendation is proportionate and names the risk/reversibility/impact rationale.
  - It picks a single, minimal proof rather than escalating to a suite.
failure_signals:
  - Over-testing (suite for a reversible one-liner).
  - Under-testing (ship with no proof).
related_observations: []
notes: Synthetic case; no source observation. Demonstrates a baseline expectation for proportional proof selection.
---

# Validation Case

## Scenario
A fictional team swings between skipping proof and demanding a full suite. A one-line
banner copy change (low risk, trivially reversible) should pull a proportionate, minimal
check from the skill — not the extremes.

## Why this expectation is correct
The `testing` skill exists to choose the *minimum reliable* proof based on risk,
reversibility, and impact. Both over- and under-testing violate its core purpose.

## How a reviewer checks it
The recommendation should name a single minimal proof and justify it via
risk/reversibility/impact. A regression suite or "no proof needed" both fail the case.
