# Skill Evolution Experiments

A skill evolution experiment compares a skill as it is today (**baseline**) against a
proposed change (**candidate**) using one or more
[validation cases](../validation-cases/README.md), checks for regression, and records a
recommendation.

> **Optimization is evidence, not authority.** The strongest outcome an experiment can
> produce is `proposal-created`. It never edits a skill, and never decides on its own.

## Directory guide

- `templates/skill-evolution-experiment-template.md` — canonical experiment format
- `templates/regression-note-template.md` — for recording a regression
- `examples/` — safe, non-sensitive worked experiments
- `pilot/` — the Fase 5 batch: real experiments over existing observations (outcomes: no-change, defer, reinforced)

## Authorized flow

```txt
Observation → Validation Case → Experiment → Regression Check
  → Proposal → Human Review → Pull Request → Canonical Skill Update
```

Everything up to the experiment is evidence; everything after the proposal is human
authority. See
[skill-evolution-experiments.md](../../docs/evolution/skill-evolution-experiments.md) and
[optimization-boundaries.md](../../docs/evolution/optimization-boundaries.md).

## Validation

```bash
python3 scripts/validate_evolution_experiments.py
```

Structural checks only — no runtime, no model calls, no writes to `skills/`.
