# Walkthrough — Build Now (skill composition)

Shows how the skills compose to a Build verdict. Feature: *one-click CSV export for saved
reports* (the contract record is in AletheIA `examples/feature-governance/build-example.md`).

## 1 — feature-value-governance frames and resolves

- Feature stated in one line. Task shape: `interface_change` (adds an export button).
- Resolves `strategic_framework` → `example-4-layers@1.2.0` (generic example pack used
  here; a proprietary pack would substitute under the resolver).
- `accessibility_guidelines` becomes required (interface change).

## 2 — revenue-lever-mapping

```yaml
revenue_lever_map:
  opportunity: Remove weekly manual rework for ops analysts
  mode: knowledge_aware
  strategic_framework_ref: example-4-layers@1.2.0
  primary_lever: retention
  primary_rationale: Friction tied to renewal risk in a high-value ICP
  secondary_levers: [efficiency]
  metric: { name: weekly active exporters in ICP, direction: up }
  proxy: { name: export button click-through, validity: misleads if clicks don't become repeat use }
  risks: [export alone may not move renewal]
  uncertainty: unknown share of renewal risk attributable to this gap
```

## 3 — feature-complexity-audit

```yaml
complexity_scorecard:
  feature: one-click CSV export
  dimensions:
    cognitive: { level: low, drivers: one new button, familiar mental model }
    technical: { level: low, drivers: reuses existing report query layer }
    operational: { level: low, drivers: minimal support surface }
    governance: { level: low, drivers: no new PII; export of data user already sees }
  reversibility: { level: reversible, mechanisms: [flag, cohort, rollback] }
  rolled_up_level: low
  dominant_driver: none significant
  reduction_recommendation: ship as-is; scope already minimal
  uncertainty: support volume from power users hard to predict
```

## 4 — gates and verdict

- Problem ✓ · ICP ✓ · Lever ✓ (retention) · Evidence ✓ (strong) · Complexity ✓ (low) ·
  Reversibility ✓ · Metrics ✓.
- No exception needed (cost is low).
- Verdict: **Build Now**, born measurable, with 30/90 review. Recorded on the contract.

## What this illustrates

- The orchestrator called only the two skills the question needed (lever + complexity),
  not the whole chain.
- Uncertainty traveled with the verdict and was not laundered into the score.
- The strategic lens was cited as `pack_id@version`, never reproduced.
