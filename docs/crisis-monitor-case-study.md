# Crisis Monitor Case Study

## Why this case matters

The first real consumer test of Adaptive Skills happened in **Crisis Monitor**, using **AletheIA** as the macro layer and a small set of skills as the micro layer.

This matters because it was not a synthetic demo.
It was a bounded, real product lane with existing signals, approvals, follow-up explainability, and auditability.

## Context

The test stayed inside one small lane:

- routing
- approval
- follow-up explainability

The goal was not to launch a new framework rollout.
The goal was to verify whether the macro/micro split would stay legible in real work.

## Macro versus micro in the field

### AletheIA handled the macro layer

- framing the immediate task
- setting minimum proof expectations
- reading whether review or handoff was needed
- preserving continuity between rounds

### Adaptive Skills handled the micro layer

- shrinking the slice to the smallest useful change
- making the execution shape more explicit
- keeping verification proportional
- activating optional skills only when a real trigger appeared

### Crisis Monitor kept its local rules

- domain semantics
- rollout constraints
- ownership boundaries
- approval and audit contracts

This separation was one of the most important outcomes of the pilot.

## Round 1

### Bundle used

- `workflow`
- `feature-planning`
- `testing`

### What it proved

- the base bundle was sufficient in a real lane
- the micro layer added discipline without creating a second governance framework
- the same lane already used by AletheIA was the right place to start

### Evidence shape

The proof stayed intentionally small:

- smoke validation
- authenticated functional flow
- consistency between proposal card, audit trail, and follow-up explainability

## Round 2

### Additional skill activated

- `ux-writing`

### Why it activated

A real textual clarity problem appeared in the audit surface:

- `Justificativa humana do approval`

That label mixed Portuguese and English in a place that needed fast operational reading.
The round changed it to:

- `Justificativa humana da aprovação`

### What it proved

- optional skills work better when activated by real triggers, not by default enthusiasm
- `ux-writing` was useful as a precise micro adjustment, not as a broad copy rewrite
- the same existing smoke remained enough as proportional proof

## What the pilot proved overall

After two small rounds, the case study supports these conclusions:

1. **Macro/micro separation is usable in real work**
2. **The base bundle is enough for an initial consumer pilot**
3. **Optional skills should enter by trigger, not by default**
4. **A small, auditable lane is a better first proving ground than a broad rollout**

## What the pilot did not prove

The case does **not** prove that:

- every lane in the product should adopt the library immediately
- every optional skill is ready to enter
- the library should become a product-wide dependency
- the same result will automatically generalize to more cross-functional or integration-heavy work

## Expansion rule learned from the case

The most important operational rule from the Crisis Monitor pilot is:

> expand only when a **real trigger** appears.

That means future rounds should be opened only if one of these is true:

- there is a new real textual or operational ambiguity
- another optional skill has a clear, verifiable trigger
- the current bundle hits a real limit that cannot be handled inside the same boundary

## Recommended use of this case

Use this case when you need to explain:

- how Adaptive Skills works with AletheIA without depending on it
- what a small first consumer pilot should look like
- why skill activation by trigger is healthier than a large default bundle
- how to keep product-local rules out of the generic library
