---
title: "Skill / Harness Boundaries"
description: "Reference documentation for Skill / Harness Boundaries in Adaptive Skills."
---

## Goal

State the boundary between a **skill** and a **harness** so that skills stay portable and harnesses
stay reviewable.

A skill is a **procedure**: how to think, what to ask, what to produce.
A harness is an **execution environment**: which tools, what autonomy, which gates, which sensors,
what logs, what rollback.

The two must not be merged. A skill should run unchanged inside a light harness or a strict one; a
harness should govern any skill without rewriting it.

This sits alongside [skill-knowledge-boundaries.md](https://nevitonsantana.github.io/adaptive-skills/skill-knowledge-boundaries/) (skill vs.
content) — together they keep a skill free of both embedded content and embedded environment.

---

## What a skill carries

- the situation it applies to;
- the questions it asks;
- the moves it executes;
- the criteria it uses;
- the format of its output;
- its handoff signals.

## What a harness carries

- the autonomy level the agent may operate at;
- the tools it may use, and at what permission;
- the actions it must never take;
- the gates that guard side effects;
- the sensors expected before judgment;
- the logs and trace required;
- the rollback strategy and human-review requirement.

The harness is declared in an **Agent Harness Contract** (AletheIA: `docs/contracts/agent-harness-contract.md`),
with a fill-in template at [`../templates/agent-harness-contract.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/agent-harness-contract.yaml).

---

## Two orthogonal axes

Execution depth and autonomy are different questions. Do not collapse them.

| Axis | Question | Where it lives |
|---|---|---|
| **Execution mode** | *how deep* should the work run? | [execution-modes.md](https://nevitonsantana.github.io/adaptive-skills/execution-modes/) (basic / extended / high-risk / multi-agent) |
| **Autonomy level** | *how much authority* does the agent hold? | Agent Harness Contract (observe / advise / act_with_approval / autonomous_within_bounds) |

A `debugging/root-cause` run (deep) can still be `act_with_approval` (gated authority). A
`workflow/basic` run (shallow) can still be `autonomous_within_bounds` if its blast radius is
trivial. Pick each axis on its own evidence.

---

## See also

- [skill-knowledge-boundaries.md](https://nevitonsantana.github.io/adaptive-skills/skill-knowledge-boundaries/)
- [execution-modes.md](https://nevitonsantana.github.io/adaptive-skills/execution-modes/)
- [using-skills-inside-harnesses.md](https://nevitonsantana.github.io/adaptive-skills/using-skills-inside-harnesses/)
- [harness-aware-engineering-skills.md](https://nevitonsantana.github.io/adaptive-skills/harness-aware-engineering-skills/)
