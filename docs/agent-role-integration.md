# Agent Role Integration

## Goal

Explain how **AletheIA agent roles** consume **Adaptive Skills** without collapsing the macro and micro layers into one system.

The stable boundary is:

- **AletheIA** = macro layer
- **Adaptive Skills** = micro layer

This document describes a consumption model, not a new skill type and not a second agent framework inside this repository.

---

## Core rule

**Agent roles consume skills.**

That means:

- a **role** is a portable semantic responsibility defined by AletheIA
- a **skill** is a reusable micro-execution asset from this repository
- a **runtime adapter** or **consumer projection** is the local mechanism that makes either one usable in Codex, Claude Code, or another runtime

Keep these distinctions explicit:

- role != skill
- skill != agent
- runtime adapter != role definition

---

## Why this matters

Without this separation, teams tend to create one of two problems:

1. **role inflation**
   - every runtime invents its own role names for the same job
2. **skill inflation**
   - a generic skill gets treated as if it were a role, workflow engine, or project operating system

The healthy model is simpler:

- AletheIA defines the portable semantic boundary
- Adaptive Skills provides the reusable execution support
- the consumer project decides how those are projected into a specific runtime

---

## Recommended role -> skill matrix

This mapping is **recommended**, not mandatory.
It is a practical default for consumers that want the same mental stack across runtimes.
It does **not** replace trigger-based activation inside the skills themselves.

| AletheIA role | Recommended skills | Why this pairing is healthy |
|---|---|---|
| `orchestrator` | `workflow`, `feature-planning`, `communication` | frames the slice, chooses the next move, and keeps continuation legible |
| `explorer` | `architecture-review`, `workflow`, `debugging` | reduces discoverable unknowns before implementation or escalation |
| `implementer` | `api-design`, `refactoring`, `testing`, `debugging` | executes bounded changes while preserving contract and proof discipline |
| `reviewer` | `architecture-review`, `code-style`, `communication`, `testing` | challenges semantic drift, weak proof, and unclear design tradeoffs |
| `validator` | `testing`, `debugging`, `workflow` | confirms whether closure evidence is explicit enough to finish the slice |

---

## How to read this matrix

Read the matrix as:

- **role first** when the main question is semantic responsibility
- **skill first** when the main question is execution method

Examples:

- “Who should own this next boundary?” -> start from the **role**
- “How should this role execute the work?” -> choose the **skill**
- “How does this show up in Codex or Claude?” -> look at the **runtime adapter** or projection layer

The matrix is there to reduce ambiguity, not to force a full five-role ceremony onto every task.

---

## Relationship to projections and runtime adapters

This repository already supports projection and consumer-specific availability models.
That layer remains local and runtime-specific.

Examples:

- Codex projection may expose many skills as first-class consumable assets
- Claude projection may keep a skill as `link-only`, `manual`, or `available-not-default`
- a consumer may project the same skill differently in two runtimes without changing the role mapping

That is healthy.

The role mapping stays stable even when:

- projection mode changes
- target path changes
- a consumer keeps one skill available but not default in a specific runtime

This slice does **not** change projection behavior.
It only explains how to read the macro/micro relationship more clearly.

---

## Relationship to trigger-based skill activation

The role mapping does not replace the current skill model.

Skills still rely on:

- core moves
- optional modules
- activation triggers

That means the consumer should still prefer:

- activating only the skills that the current boundary really needs
- keeping optional modules optional
- avoiding large default bundles just because the role exists

The role tells you **what kind of boundary this is**.
The skill tells you **how to execute that boundary with discipline**.

---

## Relationship to the Efficiency Layer

This integration should **not** be used to reopen the Efficiency Layer as a hidden agent framework.

Problems such as:

- macro framing
- escalation posture
- continuity policy
- gate/review ownership

still belong to AletheIA or to consumer-local operating overlays.

The Efficiency Layer remains a bounded Adaptive Skills track focused on lighter execution support such as chunking, handoff summary, and checkpoint review.

---

## Cross-runtime continuity

A consumer may keep the same role across runtimes while changing only the local projection or runtime adapter.

Example:

- `implementer` in Codex may rely on `testing` + `debugging`
- the same `implementer` can continue in Claude Code with the same two skills
- the local runtime mechanics may differ, but the semantic role and micro-skill support stay coherent

This is the main reason to keep the macro/micro split explicit.

---

## Practical reading order

If you want to adopt this model in a real consumer project, read in this order:

1. `docs/aletheia-integration.md`
2. `docs/agent-role-integration.md`
3. `docs/consumer-adoption.md`
4. `examples/aletheia/role-to-skill-consumption.md`
5. runtime-specific consumer setup docs such as `docs/codex-consumer-setup.md` or `docs/claude-consumer-setup.md`

---

## Suggested next reading

- `docs/skill-model.md`
- `docs/consumer-adoption.md`
- `docs/efficiency-layer-next-signals.md`
- `examples/aletheia/feature-slice-worked-example.md`
