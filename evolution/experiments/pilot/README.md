# Fase 5 — Pilot batch

The first real run of the Skill Evolution Validation Layer over **existing observations** in
`evolution/observations/`, as called for by the design's Fase 5 ("run manually on 2–3 real
observations"). Deliberately small: few strong cases, not a benchmark suite.

## What this batch demonstrates

The point of the pilot is **not** to produce changes. It is to show the flow works and that
the full outcome range is legible — including the outcomes that keep the canon unchanged.

| Experiment | Skill | Source observation | Outcome |
| ---------- | ----- | ------------------ | ------- |
| `exp-workflow-bounded-lane-001` | `workflow` | `obs-2026-04-13-workflow-crisis-monitor-bounded-lane` | `no-change` |
| `exp-debugging-cause-isolation-001` | `debugging` | `obs-2026-04-13-debugging-cause-isolation-seed` | `defer` |
| `exp-ux-writing-label-clarity-001` | `ux-writing` | `obs-2026-04-13-ux-writing-crisis-monitor-clarity` | `reinforced` |

Each experiment ran its candidate against a synthetic validation case (in
`../../validation-cases/pilot/`) and concluded honestly:

- **workflow → no-change:** the hypothesized sidecar added ceremony with no benefit; the skill
  already passed the case.
- **debugging → defer:** one seed observation + one synthetic case is below the bar the
  observation itself set; revisit when a second real signal appears.
- **ux-writing → reinforced:** the proposed checklist duplicated moves the skill already
  performs; the case strengthens the current skill.

## Outcome

**No canonical skill changed.** No proposal was promoted. That is the expected, healthy result
for this batch — it validates that the layer produces evidence and respects the boundary
between evidence and authority.

## How to re-run

```bash
python3 scripts/validate_evolution_experiments.py
```

See [optimization-boundaries.md](../../../docs/evolution/optimization-boundaries.md) and
[skill-evolution-experiments.md](../../../docs/evolution/skill-evolution-experiments.md).
