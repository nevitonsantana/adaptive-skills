---
id: exp-debugging-cause-isolation-001
skill_id: debugging
purpose: Test whether a cause-isolation checklist/module is warranted, using the seed observation plus one synthetic case.
source_observations:
  - obs-2026-04-13-debugging-cause-isolation-seed
validation_cases:
  - vc-debugging-cause-isolation-001
candidate_change:
  target_surface: Optional Modules
  change_type: module-candidate
  summary: Hypothesized "cause-isolation" optional module that forces symptom/cause separation before any fix is endorsed.
protected_surface_touched: false
baseline_result:
  summary: The skill is directionally right and passes the synthetic case, but the seed observation reports real-world usage still sometimes jumps from symptom to fix.
  passed_cases:
    - vc-debugging-cause-isolation-001
  failed_cases: []
candidate_result:
  summary: The candidate module would make symptom/cause separation explicit. On this one synthetic case it changes nothing (already passes); its value depends on the recurring real-world pattern, which is not yet captured in enough observations.
  passed_cases:
    - vc-debugging-cause-isolation-001
  failed_cases: []
regression_check:
  regression_found: false
  notes: No regression. Evidence is still one seed observation plus one synthetic case — below the bar for a module-level change.
recommendation:
  outcome: defer
  rationale: The seed observation explicitly asked for at least one more real observation before approving a module-level change. The synthetic case strengthens the hypothesis but is not a field signal. Defer until a second real observation appears.
human_review_required: true
---

# Skill Evolution Experiment

## Purpose
The seed observation (`obs-2026-04-13-debugging-cause-isolation-seed`) flagged a recurring
maintainer concern — debugging usage jumping from symptom to fix — and asked for more evidence
before any module change. This experiment tests the cause-isolation module hypothesis against
a synthetic case.

## Candidate change
A hypothesized "cause-isolation" optional module (`Optional Modules`) that forces explicit
symptom/cause separation before a fix is endorsed. No protected surface is touched.

## Baseline vs. candidate
Against `vc-debugging-cause-isolation-001`:

- **Baseline:** the skill isolates the cause and treats the proposed fix as a hypothesis →
  case passes.
- **Candidate:** the module would formalize that separation, but on this single synthetic case
  it changes nothing. Its real value rests on the recurring field pattern, not this case.

## Regression check
No regression. The evidence base is one seed observation + one synthetic case — below the bar
the observation itself set for a module-level change.

## Recommendation
`defer`. Promising but insufficient. Revisit when a second *real* observation of the
symptom-to-fix jump appears; then this experiment can be re-run toward `proposal-created`.
