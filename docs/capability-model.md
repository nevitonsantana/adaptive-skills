---
title: "Capability Model"
description: "Reference documentation for Capability Model in Adaptive Skills."
---

Adaptive Skills is evolving from a flat library of skills into a lightweight capability layer.

The goal is not to create more skills by default. The goal is to make existing skills easier to compose, route, execute, observe, and evolve without turning this repository into an agent runtime.

## Definitions

- **Skill** — the human-readable method asset in `skills/` or `domain-packs/`. It describes when to use the method, core moves, optional modules, triggers, verification, handoff signals, and anti-patterns.
- **Capability** — a routable operational unit around a skill or module. It adds intent, dependencies, modes, risk posture, expected evidence, and escalation hints.
- **Micro-capability** — a small reusable move such as ambiguity check, scope boundary, proof recap, dependency thinning, or rollback gate.
- **Macro-capability** — a larger composition such as feature planning, debugging, checkpoint review, or premortem.
- **Workflow** — an ordered composition of capabilities for a task shape.
- **Runtime** — the consumer-local execution loop that selects, activates, checkpoints, resumes, and records capability use.
- **Harness** — the agent, tools, sandbox, permissions, memory, and observability around execution.
- **Governance layer** — the macro decision layer that decides depth, gates, escalation, human approval, and closure.

## Layer boundary

Adaptive Skills owns reusable capability definitions. AletheIA owns macro governance.

```txt
AletheIA
  framing, planning depth, readiness gates, human decisions, continuity

Adaptive Skills
  skills, micro-capabilities, routing hints, evidence shapes, evolution signals

Agent runtime / harness
  tool calls, sandbox approvals, local state, execution logs, projection behavior
```

## What changes

A skill can now be described operationally without changing the skill file itself:

```txt
feature-planning
 ├── ambiguity-check
 ├── scope-boundary
 ├── smallest-viable-slice
 ├── risk-mapping
 └── traceability-check
```

This lets a consumer ask:

- Which capability fits this task?
- Which modules should activate?
- Which depth is enough?
- What evidence should exist before closure?
- Is this a skill problem, routing problem, governance problem, or local execution problem?

## What does not change

- Skills remain canonical in `skills/` and `domain-packs/`.
- The capability layer does not auto-edit skills.
- The Evolution Layer remains the governed path for changing the library.
- Routing is advisory in this phase.
- This repository remains vendor agnostic and model agnostic.

## Anti-patterns

- Creating a new skill when a module or routing rule is enough.
- Treating capability metadata as an execution engine.
- Hiding governance decisions in routing rules.
- Applying high-risk ceremony to low-risk work.
- Making Adaptive Skills depend on AletheIA to be useful.
