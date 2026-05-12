# Efficiency Layer

## Why this is a separate track

The Evolution Layer helps the library learn without drift.
The Efficiency Layer tackles a different problem: how work using the library can become lighter, clearer, and less wasteful over time.

It exists to improve the relationship between:

- task framing
- context size
- execution cost
- checkpoint discipline
- handoff quality
- model-class choice

This is related to the library, but it is **not** the same thing as evolving a skill contract.

## Problem areas

The Efficiency Layer is aimed at recurring operational problems such as:

- context that grows without control
- weak initial prompts or task framing
- oversized tasks with no smallest useful slice
- missing checkpoints between rounds
- poor handoff summaries
- overuse of the most expensive or most powerful model class when simpler work would suffice

## Relation to AletheIA

This track has a strong conceptual connection to AletheIA because AletheIA already helps with:

- framing
- gates
- handoffs
- continuity
- proof
- review

But the Efficiency Layer still belongs in Adaptive Skills as a transversal capability layer, not as an AletheIA dependency.

## Efficiency Layer v0 — framing and operating patterns

The first phase should stay documentation-first and pattern-first.
It should define:

- the main efficiency problems to watch
- the difference between a skill problem and an operating-pattern problem
- how checkpoints, chunking, and handoffs reduce waste without over-process

## Efficiency Layer v0.1 — first candidate skills

The first candidate skills should be:

- `task-chunking`
- `handoff-summary`
- `checkpoint-review`

These are the best first candidates because they are easier to validate through real work and have the lowest overlap risk with the existing Evolution Layer.

## Deferred for later

These candidates should stay deferred until the earlier trio is proven:

- `context-compression`
- `prompt-framing`
- `model-routing`

They are more likely to overlap with agent behavior, orchestration, or AletheIA-level concerns, so they should not be the first implementation step.

## What this track should not do

The Efficiency Layer should not:

- replace the existing skills
- reopen the Evolution Layer baseline
- become a hidden AletheIA dependency
- turn token efficiency into the only success measure

The point is operational sustainability, not narrow token optimization.

## Recommended next step

Plan Efficiency Layer v0 as a separate implementation track after the current Evolution Layer work is merged and used a bit more in practice.
