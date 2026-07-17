# Skill Model

## Why this model exists

Rigid step-by-step skills break when one skill supports multiple task shapes.
Unstructured skills break because they depend on improvisation.

Adaptive Skills uses a middle path:

- **Core Moves** for invariants
- **Optional Modules** for context-specific depth
- **Activation Triggers** for lightweight adaptiveness

## Core Moves

`Core Moves` are the few actions that should almost always happen.

Rules:
- 3 to 5 moves
- durable over time
- easy to scan quickly
- not a full procedure tree

## Optional Modules

Modules are contextual blocks.

Examples:
- risk review
- stakeholder alignment
- coverage gap analysis
- accessibility lens

Modules do not turn on by default.

## Activation Triggers

Triggers are natural-language cues such as:
- if the change is high-risk
- if the work crosses multiple functions
- if an existing interface already exists
- if another system consumes the contract
- if the plan has meaningful cost of failure and can still change

They are not a mini policy engine.

Triggers help select both the skill and its depth.

For example, a reversible plan may not need `premortem`; a consequential plan with hidden assumptions, missing rollback, or human decision gates probably does.

## Sidecars

A skill folder may include:
- `templates/`
- `checklists/`
- `examples/`
- `references/`
- `changelog.md`

Only add them when they reduce cognitive load or improve reuse.

## What not to do

- do not make the core a giant checklist
- do not create modules for one-off edge cases
- do not create empty sidecar folders
- do not turn a skill into a mini framework
- do not select skills just because they are available

## Selection discipline

A skill should be selected because it improves the task, not because the catalog needs to be exercised.

Use this order:

1. Identify the dominant need in the task.
2. Choose the smallest skill that fits that need.
3. Use `When NOT to Use` to reject weak fits.
4. Activate optional modules only when the trigger is present.
5. Verify the output using the skill's verification section.

See `docs/how-to-use-a-skill.md` for a practical usage guide.

Catalog growth is governed by the [Lean Skill Doctrine](skill-design-principles/lean-skill-doctrine/) and [Skill Catalog Governance](skill-catalog-governance/). A new skill, module, merge, split or deprecation should pass the [Skill Quality Gate](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/skill-quality-gate.md) before canon changes.


## Governed evolution

Skills are living assets, but not every observation should change the library.

The evolution layer is designed to:
- capture real usage evidence
- distinguish local residue from reusable skill friction
- protect the most conceptually sensitive surfaces
- allow small proposals before structural edits

Valid outcomes include `reinforced`, `no-change`, and proposal-oriented results such as `new-module-candidate`.

## Protected surfaces

In v1.1, the most sensitive surfaces stay protected from proposal-driven writeback:

- `name` and `description`
- `When to Use` / `When NOT to Use`
- `Core Moves`
- skill category and domain boundaries
- merge or split decisions for skills

That keeps the library coherent while still allowing safer refinements in triggers, modules, verification, and sidecars.
