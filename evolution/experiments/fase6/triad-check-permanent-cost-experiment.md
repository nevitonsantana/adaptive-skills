---
id: exp-triad-check-permanent-cost-001
skill_id: triad-check
purpose: Test whether the permanent-cost routing to feature-value-governance needs a clearer activation trigger, or whether the skill already handles it.
source_observations:
  - obs-2026-06-01-triad-check-permanent-cost-routing
validation_cases:
  - vc-triad-check-permanent-cost-001
candidate_change:
  target_surface: Activation Triggers
  change_type: trigger-adjustment
  summary: Hypothesized extra trigger making "route to feature-value-governance" explicit whenever the dominant conflict is value-vs-permanent-cost.
protected_surface_touched: false
baseline_result:
  summary: The skill already considers all three lenses, surfaces the permanent-cost tension, and routes to feature-value-governance; the case passes cleanly.
  passed_cases:
    - vc-triad-check-permanent-cost-001
  failed_cases: []
candidate_result:
  summary: The extra trigger restates what the Permanent-cost tension module already does. It passes the case but adds no behavior the baseline lacked.
  passed_cases:
    - vc-triad-check-permanent-cost-001
  failed_cases: []
regression_check:
  regression_found: false
  notes: No regression and no new capability; the existing module + trigger already cover the routing.
recommendation:
  outcome: reinforced
  rationale: The case strengthens confidence that triad-check correctly routes value-vs-permanent-cost tensions to feature-value-governance. No structural change is justified.
human_review_required: true
---

# Skill Evolution Experiment

## Purpose
The Fase 6 observation (`obs-2026-06-01-triad-check-permanent-cost-routing`) found the routing
behavior healthy. This experiment tests an explicit-trigger candidate against that conclusion.

## Candidate change
A hypothesized Activation Trigger making the routing to `feature-value-governance` explicit for
value-vs-permanent-cost conflicts. No protected surface is touched.

## Baseline vs. candidate
Against `vc-triad-check-permanent-cost-001`:

- **Baseline:** all three lenses considered, permanent-cost tension surfaced, routed to
  `feature-value-governance`, operational next move → case passes.
- **Candidate:** the extra trigger duplicates the existing Permanent-cost tension module; passes
  but adds nothing.

## Regression check
No regression, no new capability.

## Recommendation
`reinforced`. A valid, good result — keep the canon unchanged.
