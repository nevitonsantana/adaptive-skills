---
id:
skill_id:
case_type:        # baseline | regression | edge_case | knowledge_aware
sensitivity:      # public | synthetic | internal | confidential | restricted | regulated
source_policy:    # synthetic_only | authorized_pack | public_source
capsule_only:     # true | false   (must be true for confidential/restricted/regulated)
input:
  task:
  context:
expected_behavior:
  must_do:
    -
  must_not_do:
    -
acceptance_criteria:
  -
failure_signals:
  -
related_observations:
  -
notes:
---

# Validation Case

## Scenario
<!-- A short, reproducible description. Synthetic-first: invent realistic but fictional
     detail rather than pasting governed content. -->

## Why this expectation is correct
<!-- Tie the must_do / must_not_do back to the skill's purpose or a real observation. -->

## How a reviewer checks it
<!-- Restate acceptance_criteria and failure_signals in plain language. -->
