---
title: "Matt Pocock Engineering Skills — Reference Map"
description: "Reference documentation for Matt Pocock Engineering Skills — Reference Map in Adaptive Skills."
---

## Role of this reference

The external repository [`mattpocock/skills`](https://github.com/mattpocock/skills) is used here as **inspiration and evidence** of engineering execution patterns for agents. It is **not** a source of truth for Adaptive Skills and carries no authority over this library.

We adopt *concepts*, never content. No skill body, prompt text, or script is copied from the external repository. Where an external idea is useful, we re-express it in original prose, adapted to the Adaptive Skills model (Core Moves + Optional Modules + Activation Triggers + Expected Output + Verification + Handoff Signals + Anti-patterns) and to our governance constraints (vendor-agnostic, model-agnostic, docs-first, Evolution Layer compatible).

This map records what we read, what we decided per concept, and why.

## Concepts evaluated

The four most relevant external concepts for engineering hardening:

- **diagnose** — a disciplined feedback loop for bugs and regressions before changing code.
- **tdd** — red/green/refactor, tests by behavior, vertical slices.
- **improve-codebase-architecture** — module depth, interface size, locality, deletion test.
- **grill-with-docs** — alignment of domain language, living context, and decision records (ADRs).

## Decision per concept

| External concept | Adaptive Skills target | Decision | Justification |
|---|---|---|---|
| diagnose — feedback loop | `debugging` → `Feedback loop construction` module | **adapt** | `debugging` already reproduces and isolates; it lacked an explicit, agent-runnable pass/fail loop before code changes. Adapting strengthens an existing skill rather than adding a new one. |
| tdd — behavior-first tests | `testing` → `Behavior-first test design` module | **adapt** | `testing` calibrates proof by risk but did not explicitly steer toward public-interface, refactor-surviving tests. |
| tdd — vertical slice | `testing` → `Vertical test slice` module | **adapt** | Encourages one-behavior cycles over horizontal mass test-writing; fits `testing` without a new skill. |
| improve architecture — module depth | `architecture-review` → `Module depth review` module | **adapt** | Adds concrete leverage/locality/deletion-test criteria to an existing review skill. |
| grill-with-docs — shared language / context / ADRs | new skill `domain-language-alignment` | **adapt (new skill)** | No existing skill aligns vocabulary across product, domain, docs, ADRs, and code. The capability is independent and reusable, so a small new skill is justified (see decision record below). |
| to-prd | — | **defer** | Overlaps with the Feature Value Governance Pack and `feature-planning`. Avoid conflict this round. |
| to-issues / vertical-slice-to-issues | `feature-planning` (candidate only) | **defer** | Recorded as a candidate; not implemented to avoid conflict with the Feature Value Governance Pack. |
| triage | — | **defer** | Out of scope for engineering hardening this round. |
| setup scripts (`skills.sh`) | — | **reject** | Would create a tool/runtime dependency. Adaptive Skills stays vendor- and runtime-agnostic. |

## Decision record — `domain-language-alignment`

**Decision: CREATE.** A repo scan confirmed no equivalent skill exists (`skills/` has no language/vocabulary/context-alignment skill). The behavior — reconciling canonical, ambiguous, and conflicting terms across product intent, domain concepts, documentation, ADRs, and code — is independent and reusable, satisfying the "create new skill only when the capability is clearly independent" guardrail. The skill is implemented in Phase 5 of the hardening plan.

## Risks

- **Importing too much style** — Mitigation: keep only principles compatible with Adaptive Skills; re-express in original prose.
- **Inflating the library** — Mitigation: three of four concepts harden *existing* skills; only one new skill is created.
- **Conflict with Feature Value Governance Pack** — Mitigation: `feature-planning` is left untouched; `to-prd`/`to-issues` deferred.
- **Excessive tool prescription** — Mitigation: specific tools (pytest, curl, headless browser, etc.) appear only as examples with a generic fallback, never as dependencies.
- **Copying external material** — Mitigation: concepts only; this map is the single point that cites the external repo, and it cites it as inspiration.
