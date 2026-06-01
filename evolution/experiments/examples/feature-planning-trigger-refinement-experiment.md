---
id: exp-feature-planning-trigger-refinement-001
skill_id: feature-planning
purpose: Test whether a sidecar template field that records the deferred-expansion trigger improves bounded planning legibility, without touching Core Moves.
source_observations:
  - obs-2026-04-13-feature-planning-expansion-trigger-gap
validation_cases:
  - vc-feature-planning-scope-boundary-001
candidate_change:
  target_surface: templates/
  change_type: template-refinement
  summary: Add an optional "expansion trigger / why-not-now" field to the feature-planning sidecar template so deferral is recorded explicitly.
protected_surface_touched: false
baseline_result:
  summary: The skill holds the smallest-slice line, but the deferral reason is implicit and not consistently captured in the output.
  passed_cases: []
  failed_cases:
    - vc-feature-planning-scope-boundary-001
candidate_result:
  summary: With the optional template field, the plan output records a deferred-expansion rationale naming a concrete trigger; smallest-slice discipline is unchanged.
  passed_cases:
    - vc-feature-planning-scope-boundary-001
  failed_cases: []
regression_check:
  regression_found: false
  notes: Smallest-slice behavior and existing slices/risks/proof structure are unaffected; the field is additive and optional.
recommendation:
  outcome: proposal-created
  rationale: One real observation plus a synthetic scope-boundary case both point to a small, additive sidecar refinement. Strong enough to promote to a proposal, not strong enough to write canon directly — this maps to the existing deferred proposal prop-2026-04-13-feature-planning-expansion-trigger-template.
human_review_required: true
---

# Skill Evolution Experiment

## Purpose
The Crisis Monitor two-round pilot (`obs-2026-04-13-feature-planning-expansion-trigger-gap`)
repeatedly reinforced that expansion should happen only when a real trigger appears. The
discipline is sound; what is missing is making the *why-not-now* legible in the output.
This experiment tests an additive template field, not a change to `Core Moves`.

## Candidate change
Add an optional "expansion trigger / why-not-now" field to the `feature-planning` sidecar
template (`templates/`). No protected surface is touched.

## Baseline vs. candidate
Against `vc-feature-planning-scope-boundary-001`:

- **Baseline:** the plan holds the smallest slice but leaves the deferral reason implicit;
  the case's acceptance criterion (a reviewer-pointable rationale naming a trigger) is not
  reliably met → case fails.
- **Candidate:** the optional field captures a deferred-expansion rationale with a concrete
  trigger; smallest-slice discipline and the slices/risks/proof structure are unchanged →
  case passes.

## Regression check
No regression. The field is additive and optional; no previously-passing behavior changes.

## Recommendation
`proposal-created`. Evidence is consistent (one real observation + one synthetic case) but
deliberately modest. This promotes to the Evolution Layer as a proposal — it aligns with
the already-deferred `prop-2026-04-13-feature-planning-expansion-trigger-template` — and
still requires human review and a PR before any canonical change.
