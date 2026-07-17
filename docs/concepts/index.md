---
title: Concepts
description: Explore the models and boundaries behind skills, composition, capabilities, harnesses, and governed knowledge.
---

Start here when you want to understand why Adaptive Skills is structured the way it is. These concepts explain the system; they do not add a second runtime or change how a skill executes.

## Skills

Skills are portable micro-execution assets. Each skill carries a focused method, activation triggers, optional modules, verification expectations, failure signals, and handoff guidance.

Start with:

- [Skill model](https://nevitonsantana.github.io/adaptive-skills/skill-model/) — anatomy and selection discipline.
- [Skill categories](https://nevitonsantana.github.io/adaptive-skills/skill-categories/) — current organizational taxonomy.
- [Domain taxonomy](https://nevitonsantana.github.io/adaptive-skills/domain-taxonomy/) — generic skills versus domain packs.
- [Lean skill doctrine](https://nevitonsantana.github.io/adaptive-skills/skill-design-principles/lean-skill-doctrine/) — why skills stay small and composable.

## Composition

Composition describes how multiple skills participate in one task without becoming a hidden workflow engine.

Start with:

- [Execution patterns](https://nevitonsantana.github.io/adaptive-skills/execution-patterns-for-skills/) — supported participation patterns.
- [Looping models](https://nevitonsantana.github.io/adaptive-skills/looping-models-for-skills/) — bounded iteration and stop conditions.
- [Workflow recipes](https://nevitonsantana.github.io/adaptive-skills/guides/workflow-recipes/) — practitioner-oriented examples.
- [Skills in orchestrated workflows](https://nevitonsantana.github.io/adaptive-skills/skills-in-orchestrated-workflows/) — AletheIA stage participation.

## Capabilities

Capability metadata helps consumers discover and route to skills. It is an advisory overlay; the canonical executable assets remain under `skills/`.

Start with:

- [Capability model](https://nevitonsantana.github.io/adaptive-skills/capability-model/) — definitions and layer boundary.
- [Capability graph](https://nevitonsantana.github.io/adaptive-skills/capability-graph/) — relationships among capabilities.
- [Capability routing boundary](https://nevitonsantana.github.io/adaptive-skills/capability-routing-boundary/) — what routing may and may not decide.
- [Execution modes](https://nevitonsantana.github.io/adaptive-skills/execution-modes/) — declared ways capabilities participate.

## Harnesses

Harnesses make skills available in a runtime. They own local loading, permissions, tool access, and execution mechanics; skills retain their portable method and declared requirements.

Start with:

- [Skill and harness boundaries](https://nevitonsantana.github.io/adaptive-skills/skill-harness-boundaries/).
- [Using skills inside harnesses](https://nevitonsantana.github.io/adaptive-skills/using-skills-inside-harnesses/).
- [Harness requirements](https://nevitonsantana.github.io/adaptive-skills/harness-requirements-for-skills/).
- [Operational runtime](https://nevitonsantana.github.io/adaptive-skills/operational-runtime/).

## Knowledge

Knowledge-aware skills can use governed source material without embedding proprietary content or silently treating untrusted text as instruction.

Start with:

- [Skill knowledge boundaries](https://nevitonsantana.github.io/adaptive-skills/skill-knowledge-boundaries/).
- [Declaring knowledge dependencies](https://nevitonsantana.github.io/adaptive-skills/declaring-knowledge-dependencies/).
- [Using proprietary frameworks safely](https://nevitonsantana.github.io/adaptive-skills/using-proprietary-frameworks-safely/).

## How the families connect

1. A **skill** defines a portable execution method.
2. **Composition** defines how that method can participate with other bounded methods.
3. **Capability metadata** improves discovery without replacing the skill.
4. A **harness** supplies local runtime mechanics and authority boundaries.
5. Governed **knowledge** supplies source-backed context when the skill declares it.

## Next steps

- Use the [ecosystem map](https://nevitonsantana.github.io/adaptive-skills/concepts/ecosystem-map/) for a compact system view.
- Read [Adaptive Skills and AletheIA](https://nevitonsantana.github.io/adaptive-skills/aletheia-integration/) for the macro/micro boundary.
- Return to [Choose the right skill](https://nevitonsantana.github.io/adaptive-skills/guides/skill-selection/) when your goal is practical selection rather than architecture.
