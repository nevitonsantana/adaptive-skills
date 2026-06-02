---
id: exp-business-design-module-precedence-001
skill_id: business-design
purpose: Test whether a small Activation Triggers clarification on module precedence (assumptions before leverage when evidence is weak) improves the skill.
source_observations:
  - obs-2026-06-01-business-design-assumption-leverage-trigger
validation_cases:
  - vc-business-design-module-precedence-001
candidate_change:
  target_surface: Activation Triggers
  change_type: trigger-adjustment
  summary: Add a precedence note to the triggers — when evidence is weak, map assumptions before scanning leverage — without changing Core Moves or the value-layer lens.
protected_surface_touched: false
baseline_result:
  summary: The skill separates facts from hypotheses well, but with both assumption-map and leverage-scan seeming to apply, the output reached for leverage first on weak evidence; the precedence acceptance criterion is not reliably met.
  passed_cases: []
  failed_cases:
    - vc-business-design-module-precedence-001
candidate_result:
  summary: With the precedence trigger, assumptions are mapped before leverage is scanned when evidence is weak; facts vs. speculation stay separated and a decision is changed. The case passes.
  passed_cases:
    - vc-business-design-module-precedence-001
  failed_cases: []
regression_check:
  regression_found: false
  notes: Additive trigger clarification; Core Moves, Verification, and the value-layer lens are unchanged. No previously-passing behavior is affected.
recommendation:
  outcome: proposal-created
  rationale: One Fase 6 observation plus a synthetic edge case both show a small, additive triggers clarification closes a real precedence gap with no regression. Strong enough to promote to a proposal in evolution/proposals/ for human review — not strong enough to write canon directly. Promotion remains a human step.
human_review_required: true
---

# Skill Evolution Experiment

## Purpose
The Fase 6 observation (`obs-2026-06-01-business-design-assumption-leverage-trigger`) flagged
ambiguity about which optional module to apply first when both assumption-map and leverage-scan
seem to apply. This experiment tests a small precedence clarification.

## Candidate change
Add an Activation Triggers precedence note — when evidence is weak, map assumptions before
scanning leverage. No protected surface, no Core Moves change, and the value-layer lens
(pluggable proprietary framework) is untouched.

## Baseline vs. candidate
Against `vc-business-design-module-precedence-001`:

- **Baseline:** with weak evidence and a monetization angle, the output scanned leverage before
  examining assumptions → the precedence criterion fails.
- **Candidate:** assumptions are mapped first; facts vs. speculation stay separated and a
  decision is changed → case passes.

## Regression check
No regression — the change is additive and leaves Core Moves, Verification, and the value-layer
lens intact.

## Recommendation
`proposal-created`. Promote to `evolution/proposals/` for human review and a PR. This experiment
is evidence; the promotion and any canonical edit remain human decisions.
