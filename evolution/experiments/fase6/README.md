# Fase 6 — Controlled expansion

Extends the Skill Evolution Validation Layer to the next skills in the recommended order:
`triad-check`, `business-design`, and `feature-value-governance` (the product-decision skill,
taken last and most cautiously). Each target first gets a real observation in
`evolution/observations/`, then a synthetic validation case, then an experiment.

## Batch

| Experiment | Skill | Source observation | Outcome |
| ---------- | ----- | ------------------ | ------- |
| `exp-triad-check-permanent-cost-001` | `triad-check` | `obs-2026-06-01-triad-check-permanent-cost-routing` | `reinforced` |
| `exp-business-design-module-precedence-001` | `business-design` | `obs-2026-06-01-business-design-assumption-leverage-trigger` | `proposal-created` |
| `exp-feature-value-governance-generic-mode-001` | `feature-value-governance` | `obs-2026-06-01-feature-value-governance-knowledge-fallback` | `defer` |

## What this batch demonstrates

- **triad-check → reinforced:** the permanent-cost routing to `feature-value-governance` already
  works; an explicit-trigger candidate added nothing.
- **business-design → proposal-created:** a small, additive Activation Triggers precedence
  clarification (map assumptions before scanning leverage on weak evidence) closes a real gap
  with no regression. This is the first Fase-batch outcome that recommends promotion — the
  proposal itself is **not** created here; promotion to `evolution/proposals/` remains a human
  step.
- **feature-value-governance → defer:** the knowledge-aware generic-mode fallback already works;
  evidence is thin and the skill is product-sensitive, so any module is deferred.

## Governance notes

- `feature-value-governance` is **knowledge-aware**; its case is `case_type: knowledge_aware`,
  synthetic and capsule-only, and the experiment requires human review.
- `business-design`'s **value-layer lens** uses a pluggable proprietary framework — it is
  deliberately **out of scope** for these cases. No pack content appears anywhere in the batch.
- No canonical skill was changed. Only `business-design` recommends a proposal, pending human
  promotion and review.

## Re-run

```bash
python3 scripts/validate_evolution.py                 # observations pass the existing pipeline
python3 scripts/validate_evolution_experiments.py     # cases + experiments structurally valid
```
