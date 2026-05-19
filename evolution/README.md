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

## Directory guide

- `registry.json` — evolution policy for every published skill
- `templates/` — canonical formats for observations, proposals, and reviews
- `observations/` — concrete usage signals and attributions
- `proposals/` — approved, rejected, and deferred improvement proposals
- `reviews/` — review summaries for bounded pilot rounds

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
