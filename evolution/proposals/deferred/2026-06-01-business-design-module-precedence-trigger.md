---
proposal_id: prop-2026-06-01-business-design-module-precedence-trigger
skill_id: business-design
source_observations: obs-2026-06-01-business-design-assumption-leverage-trigger
target_surface: Activation Triggers
change_type: trigger-adjustment
automation_level: manual-assisted
status: deferred
rationale: an experiment showed a small additive precedence note (map assumptions before scanning leverage when evidence is weak) closes a real triggers gap with no regression, but a single Fase 6 observation plus one synthetic case is not yet enough for canon writeback
global_consistency_risk: low
---

# Proposal

## Proposed change
Add a precedence note to the `business-design` Activation Triggers: when evidence is weak, map
assumptions (assumption-map) before scanning leverage (leverage-scan). No change to Core Moves,
Verification, or the value-layer lens.

## Why now
The Fase 6 experiment `exp-business-design-module-precedence-001` (over observation
`obs-2026-06-01-business-design-assumption-leverage-trigger` and case
`vc-business-design-module-precedence-001`) showed the baseline reached for leverage first on
weak evidence, and the additive trigger fixed it with no regression.

## Why the target surface is appropriate
The gap is in module-selection legibility, not in skill identity or Core Moves. Activation
Triggers is the narrowest safe surface and is an allowed proposal target for this skill.

## Why this is not just local residue
The weak-evidence + monetization combination is common in strategy work, so the precedence
likely generalizes — but the evidence is still one observation plus one synthetic case.

## Decision notes
Deferred per the Skill Evolution Validation Layer: an experiment produces evidence, not a
decision. Promote to `approved` only after human review and, ideally, a second real signal.
Deliberately excludes the value-layer lens (pluggable proprietary framework); no pack content
is involved.
