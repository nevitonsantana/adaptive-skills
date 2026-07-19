---
title: Adaptive Skills and AletheIA
description: Understand how AletheIA governs work while Adaptive Skills supplies reusable execution capabilities.
---

**AletheIA governs the work; Adaptive Skills provides reusable execution capabilities inside that work.**

They are complementary systems with different responsibilities. Neither needs to absorb the other.

![Macro Governance / Micro Execution](https://nevitonsantana.github.io/adaptive-skills/assets/adaptive-skills/03_macro_governance_micro_execution.png)

*Macro Governance / Micro Execution — AletheIA governs the work while Adaptive Skills provides reusable execution capabilities.*

## The relationship at a glance

| Layer | Owns | Does not own |
|---|---|---|
| **AletheIA — macro governance** | Framing, Work Slice gates, review, handoffs, continuity, and governed learning | The internal method of every reusable skill |
| **Adaptive Skills — micro execution** | Specialist heuristics, bounded workflows, output discipline, and failure signals | Work Slice approval, closure, routing authority, or project governance |
| **Consumer harness** | Local loading, projection, runtime access, and execution evidence | The portable semantic definition of roles or skills |

Adaptive Skills remains independently useful. This repository never assumes that AletheIA is installed, running, or required.

## How a Work Slice uses skills

1. **AletheIA frames the Work Slice.** It establishes the goal, boundary, evidence expectations, and gates.
2. **The consumer selects a small skill set.** Selection follows the immediate execution need, not a default bundle.
3. **Each skill performs a bounded micro task.** It returns a method output, risks, evidence references, and an advisory handoff signal.
4. **AletheIA evaluates the evidence.** The governing layer decides whether the Work Slice continues, changes, escalates, or closes.
5. **Recurring friction may become an observation.** Adaptive Skills still owns any governed change to its library.

## Roles and skills

A role is not a skill.

- An **AletheIA role** describes a portable semantic responsibility.
- An **Adaptive Skill** describes a reusable execution method.
- A **projection or runtime adapter** makes either one available in a specific consumer environment.

For example, an `implementer` role may consume `testing` and `debugging`. The role owns the responsibility boundary; the skills support how work is performed. See [Roles and skills](https://nevitonsantana.github.io/adaptive-skills/agent-role-integration/) for the recommended mapping.

## Orchestrated workflows

When a skill participates as a stage in an AletheIA orchestration, it must respect the declared input, output, gate, and evidence contract. It does not reach into other stages, silently broaden its authority, or replace the orchestration owner.

See [Skills in orchestrated workflows](https://nevitonsantana.github.io/adaptive-skills/skills-in-orchestrated-workflows/) for stage participation and escalation rules.

## Returning observations and evidence

A skill may return a compact, source-backed observation to an AletheIA-compatible harness. The return can describe:

- the skill and modules used;
- result and available evidence;
- risks and missing information;
- an advisory handoff signal;
- a governed recovery pointer when output is lossy.

The return is decision support, not replacement evidence. It cannot approve, block, close, restart, or mutate a Work Slice. See [Observation and evidence return](https://nevitonsantana.github.io/adaptive-skills/skill-observation-return-pattern/).

## First integration example

The smallest useful test uses one feature-like task with visible proof:

1. AletheIA frames the task.
2. `workflow`, `feature-planning`, and `testing` support micro execution.
3. AletheIA evaluates closure evidence.

Follow [Run the first AletheIA test](https://nevitonsantana.github.io/adaptive-skills/aletheia-first-test/) for the complete exercise.

## Boundaries and non-goals

This integration does not:

- make AletheIA mandatory for Adaptive Skills;
- turn Adaptive Skills into an agent framework;
- give a skill Work Slice authority;
- make role-to-skill mappings mandatory;
- change projection or runtime behavior;
- let observations replace authoritative source evidence;
- reopen the Efficiency Layer as hidden orchestration.

The Efficiency Layer remains a bounded Adaptive Skills track focused on lightweight execution support such as `task-chunking`, `handoff-summary`, and `checkpoint-review`.

## Next steps

- Read [Roles and skills](https://nevitonsantana.github.io/adaptive-skills/agent-role-integration/) to separate responsibility from method.
- Read [Skills in orchestrated workflows](https://nevitonsantana.github.io/adaptive-skills/skills-in-orchestrated-workflows/) for stage contracts.
- Read [Observation and evidence return](https://nevitonsantana.github.io/adaptive-skills/skill-observation-return-pattern/) for portable returns.
- Run [the first AletheIA test](https://nevitonsantana.github.io/adaptive-skills/aletheia-first-test/) in a small real task.
