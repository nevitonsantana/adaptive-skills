---
title: "Skill Knowledge Boundaries"
description: "Reference documentation for Skill Knowledge Boundaries in Adaptive Skills."
---

## Goal

State the boundary between **skill** and **knowledge** so that skills remain reusable, portable, and safe to ship.

A skill is a **procedure**: how to think, what to ask, what to produce.
A knowledge pack is **content**: a framework, a policy, a persona, a guideline.

The two must not be merged.

---

## What a skill must carry

- the situation it applies to
- the questions it asks
- the moves it executes
- the criteria it uses
- the format of its output
- the verification it runs
- the handoff it leaves behind

All of these can be written without referencing any proprietary content.

---

## What a skill must not carry

- the body of a proprietary framework
- the text of an internal policy
- excerpts from confidential or regulated sources
- client, customer, or partner names
- examples drawn from real, identifiable engagements
- detailed scoring tables that encode an organization's specific carve-outs

If a skill needs that content, it declares a **knowledge dependency** (see [declaring-knowledge-dependencies.md](declaring-knowledge-dependencies/)) and lets AletheIA's [Knowledge Governance Layer](https://github.com/nevitonsantana/AletheIA/blob/main/docs/concepts/knowledge-governance-layer.md) resolve it.

---

## Two modes every knowledge-aware skill supports

1. **Generic mode.** The skill runs with general criteria when no authorized source is available. The output is marked as generic.
2. **Knowledge-aware mode.** The skill runs with sources resolved by the registry. The output cites pack ids and versions and applies any active restrictions.

A skill that cannot run in generic mode must say so loudly in its `fallback_behavior`. Silent dependence on a specific source is an anti-pattern.

---

## Why the boundary matters

- **Portability.** A skill that embeds one company's framework cannot move to another.
- **Safety.** A skill that ships with internal content leaks that content into every agent that loads it.
- **Auditability.** Embedded content cannot be versioned independently of the skill.
- **Governance.** A skill cannot be the place where source precedence and sensitivity are decided.

---

## Quick checklist when authoring a skill

- [ ] Does the skill contain any verbatim text from a non-public source? If yes, remove it.
- [ ] Does the skill name a specific framework as required? If yes, replace with a knowledge dependency on a *type*.
- [ ] Are there examples that include real identifiers? If yes, generalize them.
- [ ] Does the skill state how it behaves when its knowledge dependencies are not met? If no, add `fallback_behavior`.
- [ ] Does the skill require human review for any specific outcomes? If yes, declare them.

---

## See also

- [declaring-knowledge-dependencies.md](declaring-knowledge-dependencies/)
- [using-proprietary-frameworks-safely.md](using-proprietary-frameworks-safely/)
- [knowledge-aware-skill-template](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/knowledge-aware-skill-template.md)
