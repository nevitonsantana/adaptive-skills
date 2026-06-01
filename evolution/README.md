# Evolution Layer

This folder contains the governed learning layer for Adaptive Skills.

It exists so the library can improve through real usage without turning into an unrestricted self-rewriting system.

## Reading order

1. `docs/evolution-layer.md`
2. `evolution/registry.json`
3. `evolution/templates/`
4. `evolution/observations/`
5. `evolution/proposals/`
6. `evolution/reviews/`
7. `evolution/validation-cases/` and `evolution/experiments/` (Skill Evolution Validation Layer)

## Directory guide

- `registry.json` — evolution policy for every published skill
- `templates/` — canonical formats for observations, proposals, and reviews
- `observations/` — concrete usage signals and attributions
- `proposals/` — approved, rejected, and deferred improvement proposals
- `reviews/` — review summaries for bounded pilot rounds
- `validation-cases/` — reproducible expectations used as evidence (Skill Evolution Validation Layer)
- `experiments/` — baseline-vs-candidate experiments that produce proposals, never decisions

## Skill Evolution Validation Layer

A docs-first layer that tests proposed skill evolutions with evidence *before* they become
proposals. **Optimization is evidence, not authority** — experiments never edit skills and
never decide on their own. See `docs/evolution/optimization-boundaries.md`,
`docs/evolution/validation-case-guidelines.md`, and
`docs/evolution/skill-evolution-experiments.md`. Validate structure with
`python3 scripts/validate_evolution_experiments.py`.

## Current v1.1 boundaries

- no skill self-rewrite
- no per-skill telemetry files
- no per-skill improvement logs
- no auto-writeback into `SKILL.md`
- no aggressive automation beyond validation and structured proposals

## Current pilot focus

The first pilot uses five skills:

- `workflow`
- `feature-planning`
- `testing`
- `debugging`
- `ux-writing`

The current seed evidence includes the Crisis Monitor case study, especially the use of `ux-writing` for a small but real explainability adjustment.
