# Template — Complexity Scorecard

Output template for `feature-complexity-audit`. Coarse and honest — no false-precision
decimals. Four dimensions, plus reversibility and a reduction recommendation.

| Dimension | Level (low/med/high) | Drivers |
| --- | --- | --- |
| **Cognitive** | | Surface users/team must hold. |
| **Technical** | | Dependencies, data model, integration, migration. |
| **Operational** | | Support, on-call, runbook, monitoring carry. |
| **Governance** | | Security, privacy, compliance, accessibility. |

| Field | Value |
| --- | --- |
| **Reversibility** | reversible / partially_reversible / one_way_door (+ mechanisms). |
| **Rolled-up level** | low / medium / high. |
| **Dominant driver** | The single biggest cost. |
| **Reduction recommendation** | Smallest scope that keeps the value, or the exception required. |
| **Uncertainty** | What is hard to estimate. |

> A `high` rolled-up level under a Build decision requires an explicit `exception_approval`
> (scope reduction or named approval) on the Feature Value Governance Contract.
