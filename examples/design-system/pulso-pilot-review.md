# Pulso Pilot Review — Synthetic Example

## Context

- Skill: `design-system-intelligence`
- Mode: Pulso pilot
- Artifact: Mission Control static prototype
- Design-system source refs: Pulso `DESIGN.md`, Pulso token file, AletheIA Pulso bridge note

## Review output

```yaml
review_id: DSIR-20260701-001
skill_id: design-system-intelligence
mode: design-system/pulso-pilot
artifact_refs:
  - aletheia://examples/visual-operations/prototype/mission-control-static.html
design_system_ref:
  id: pulso
  source_refs:
    - pulso://DESIGN.md
    - pulso://src/app/globals.css
conformance_observations:
  - area: typography
    finding: aligned
    confidence: medium
    source_refs:
      - aletheia://examples/visual-operations/prototype/pulso-token-comparison.md
  - area: state_color
    finding: candidate_issue
    confidence: low
    source_refs:
      - aletheia://examples/visual-operations/prototype/mission-control-static.html
candidate_findings:
  - kind: candidate_issue
    summary: Add source-backed accessibility contrast evidence before treating semantic state colors as reusable primitives.
    severity: medium
    recommended_next_step: human_review_required
pattern_generalization_gate:
  comparable_artifacts_count: 1
  recurrence_evidence: unavailable
  design_system_owner_review: pending
  outcome: needs_more_evidence
```

## Boundary note

This review can inform AletheIA, but it cannot approve UI changes, promote Pulso primitives, or create a scanner.
