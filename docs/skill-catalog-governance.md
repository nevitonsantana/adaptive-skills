# Skill Catalog Governance

## Purpose

Define how Adaptive Skills reviews new skills, optional modules, merges, splits and deprecations
without turning the catalog into a runtime, policy engine or AletheIA replacement.

This document operationalizes the [Lean Skill Doctrine](skill-design-principles/lean-skill-doctrine.md).

## Scope

Applies to:

- new generic skills;
- optional modules in existing skills;
- sidecars such as templates, examples, checklists and references;
- merge, split and deprecation proposals;
- catalog category changes;
- S22 `lean-implementation` review before the skill is created.

## Non-goals

- No runtime policy engine.
- No automatic skill routing.
- No blocking mechanism inside `SKILL.md`.
- No rewrite of existing skills in S20.
- No `skill-catalog-review` skill in this phase.
- No provider-specific rules.
- No AletheIA governance embedded into Adaptive Skills methods.

## Lifecycle

```text
candidate -> draft -> published -> observed -> reinforced | revise | merge | deprecate
```

| State | Meaning | Required evidence |
|---|---|---|
| `candidate` | A possible skill/module/change exists as an issue, pack, observation or proposal | source ref and problem statement |
| `draft` | A bounded PR proposes the change | quality gate and validation plan |
| `published` | The change has passed repository validation and review | merge evidence |
| `observed` | Real or synthetic use has produced a source-backed observation | observation or validation case |
| `reinforced` | Evidence supports keeping the current design | review record |
| `revise` | Evidence supports a bounded adjustment | proposal and review |
| `merge` | Two surfaces overlap enough to combine | overlap evidence and migration note |
| `deprecate` | A surface should stop being recommended | deprecation rationale and alternative |

## New skill intake

A new skill proposal must include:

- source refs;
- dominant task shape;
- adjacent skills reviewed;
- reason an optional module is insufficient;
- expected output and verification;
- boundary statement showing it declares rather than enforces;
- completed [Skill Quality Gate](../templates/skill-quality-gate.md).

## Module proposal flow

Use an optional module when an existing skill owns the dominant task shape and the new behavior is
triggered only by context.

A module proposal must declare:

- activation trigger;
- added output/evidence;
- when to skip;
- why it does not deserve standalone skill status.

## Merge, split and deprecation

Merge when two skills repeatedly compete for the same dominant need and a single boundary would be
clearer.

Split when one skill has two recurring dominant needs that create different outputs, verification or
handoff signals.

Deprecate when a skill is no longer useful, overlaps a stronger surface, or carries unsafe/unclear
boundaries that cannot be repaired proportionally.

## Protected surfaces

These surfaces require explicit review before change:

- `name` and `description`;
- `When to Use` / `When NOT to Use`;
- `Core Moves`;
- category and domain boundaries;
- merge, split or deprecation decisions;
- harness requirements and governance boundary statements.

## Proposal-safe surfaces

These surfaces can evolve through smaller proposals when evidence supports the change:

- `Activation Triggers`;
- `Optional Modules`;
- `Verification`;
- `Anti-patterns`;
- templates, examples, checklists and references.

## Decision outcomes

Quality-gate decisions use this vocabulary:

```text
accept_as_new_skill
convert_to_optional_module
merge_into_existing_skill
split_existing_skill
deprecate
defer_until_recurrence_is_proven
reject
```

The decision must name evidence refs and why lighter options were not enough.

## Relationship to AletheIA

Adaptive Skills owns catalog doctrine and skill content. AletheIA owns macro-governance over how a
consumer task selects, observes, rejects, overrides or proposes skill use.

The matching AletheIA contract is expected to govern:

- skill selection decisions;
- skill proposal decisions;
- over-selection and skill-sprawl signals;
- narrow blocking posture for authority/safety violations;
- observation records with provenance.

Adaptive Skills remains useful without AletheIA. The catalog governance here is repository-native;
it does not require a runtime or external orchestrator.

## Required validation

For S20 docs-only changes:

- `python3 scripts/validate_system_state.py`
- `python3 scripts/validate_capabilities.py`
- `python3 scripts/validate_evolution.py`
- `python3 scripts/validate_skills.py`
- `git diff --check`

For future skill creation, also run projection status and any skill-specific validation required by
the changed files.

## Related docs

- [Lean Skill Doctrine](skill-design-principles/lean-skill-doctrine.md)
- [Skill Quality Gate](../templates/skill-quality-gate.md)
- [Skill Model](skill-model.md)
- [Skill Categories](skill-categories.md)
- [Harness Requirements for Skills](harness-requirements-for-skills.md)
- [Evolution Layer](evolution-layer.md)
