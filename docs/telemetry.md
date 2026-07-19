---
title: "Recommended Telemetry"
description: "Reference documentation for Recommended Telemetry in Adaptive Skills."
---

This repository still does not implement runtime telemetry.
What it now provides is a **governed telemetry shape** so real usage can feed the evolution layer without drifting into anecdote.

![Telemetry Evidence Funnel](https://nevitonsantana.github.io/adaptive-skills/assets/adaptive-skills/08_telemetry_evidence_funnel.png)

> **Conceptual / future-state illustration.** This image describes a possible evidence flow; it does not represent an implemented telemetry store, automatic collector, dashboard, or outcome metric.

## Recommended fields

- `skill_id`
- `domain`
- `context`
- `modules_activated`
- `trigger_matches`
- `result`
- `handoff_required`
- `failure_type`
- `improvement_note`
- `evidence_refs`
- `attribution_guess`
- `result_mode`

## How telemetry should be read

Telemetry is useful only when it helps answer one of these questions:

- did the current skill work as intended?
- was the issue local to the project or lane?
- is a trigger, module, or sidecar weak?
- is there enough evidence to create a proposal?
- is `reinforced` or `no-change` actually the correct outcome?

## Relation to the evolution layer

In v1.1, telemetry should normally feed repository-level artifacts such as:

- `evolution/observations/`
- `evolution/proposals/`
- `evolution/reviews/`

It should not become vanity instrumentation or a hidden self-editing loop.


## Deferred per-skill telemetry

Per-skill files such as `telemetry.md` or `improvement-log.md` are not part of the current baseline.
They remain future candidates only if the repository-level evolution artifacts become too coarse for real usage volume.
