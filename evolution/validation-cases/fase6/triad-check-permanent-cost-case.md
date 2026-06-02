---
id: vc-triad-check-permanent-cost-001
skill_id: triad-check
case_type: baseline
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Decide whether a fictional product should switch to indefinite raw-event retention to enable future analytics.
  context: Product wants the option value; design sees little user-facing change; tech flags that indefinite retention is hard to reverse and adds permanent operational cost. The lenses disagree about whether the value justifies the forever-carry.
expected_behavior:
  must_do:
    - Consider product, design, and technical lenses explicitly.
    - Identify the dominant conflict as a value-vs-permanent-cost tension.
    - Route the tension to feature-value-governance instead of letting one function win.
    - End with an operational next move and clearer ownership.
  must_not_do:
    - Collapse the three lenses into a single opinion.
    - End with collective ambiguity and no next move.
acceptance_criteria:
  - The output names the permanent-cost tension and routes it to feature-value-governance.
  - The next step is operational, not merely descriptive.
failure_signals:
  - One function quietly wins without surfacing the value-governance question.
  - The check ends without clearer ownership.
related_observations:
  - obs-2026-06-01-triad-check-permanent-cost-routing
notes: Synthetic cross-boundary decision modeled on the Permanent-cost tension module. No governed content used.
---

# Validation Case

## Scenario
A fictional team weighs indefinite raw-event retention. Product wants option value, design is
neutral, tech flags irreversible permanent cost. The expectation is that `triad-check` surfaces
the value-vs-forever-carry tension and routes it, rather than letting one lens win.

## Why this expectation is correct
This is exactly what the Permanent-cost tension module and its activation trigger describe, and
it avoids the "collapsing three lenses into one opinion" anti-pattern.

## How a reviewer checks it
The output must name the permanent-cost tension, route to `feature-value-governance`, and end
with an operational next move and clearer ownership. A quiet single-function win or terminal
ambiguity fails the case.
