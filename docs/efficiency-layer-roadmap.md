---
title: "Efficiency Layer Roadmap"
description: "Reference documentation for Efficiency Layer Roadmap in Adaptive Skills."
---

## Goal

Turn the Efficiency Layer into a clear, bounded roadmap for improving how work is carried out with Adaptive Skills.

This roadmap is not about changing the current Evolution Layer baseline.
It is about reducing waste in:

- task framing
- context growth
- oversized work slices
- weak checkpoints
- poor handoffs
- overpowered default model use

## Current position

The Efficiency Layer currently exists as a documented thesis, not as a published skill set.

That is intentional.
The first step should remain docs-first so the repository can separate:

- a library problem
- a workflow problem
- an orchestration problem
- an AletheIA concern

## v0 — framing and operating patterns

The v0 phase should document the operating patterns that make work lighter without over-process.

It should establish:

- what efficiency problems are in scope
- what signals show a task is too large or too vague
- what a healthy checkpoint looks like
- what should remain in AletheIA or project-local overlays instead of entering this library

Expected output of v0:

- a bounded problem map
- first candidate skill briefs
- explicit boundaries versus Evolution Layer and AletheIA

## v0.1 — first candidate skills

The first candidate skills are:

- `task-chunking`
- `handoff-summary`
- `checkpoint-review`

They are first because they:

- are easy to validate through real usage
- address repeated operational waste
- have clearer boundaries than more agent-like concerns
- can work with or without AletheIA

## Deferred for later

These candidates should remain deferred until the first three are validated:

- `context-compression`
- `prompt-framing`
- `model-routing`

They have higher overlap risk with:

- model behavior
- orchestration policy
- AletheIA-style macro guidance

## Boundary rules

Efficiency Layer should not:

- reopen the Evolution Layer v1.1 baseline
- become a hidden AletheIA dependency
- optimize only for token count
- replace normal feature, design, or quality skills

Efficiency Layer should:

- reduce avoidable rework
- make checkpoints cheaper and clearer
- improve handoff discipline
- help teams keep work slices bounded

## Recommended next implementation step

After this roadmap pass, the next sensible move is a separate documentation pass that defines:

- one brief per candidate skill
- expected outputs
- where each skill stops and AletheIA begins
- one lightweight example of combined usage


## First pilot artifacts

The pilot artifacts for this first use pass are:

- `docs/efficiency-layer-first-pilot.md`
- `docs/efficiency-layer-pilot-checklist.md`
- `templates/pilot/efficiency-pilot-report.md`
- `docs/efficiency-layer-crisis-monitor-reference.md`
- `examples/efficiency/crisis-monitor-efficiency-reference.md`
- `docs/efficiency-layer-trio-patterns.md`
- `docs/efficiency-layer-next-signals.md`
