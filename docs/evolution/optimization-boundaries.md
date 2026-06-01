# Optimization Boundaries

> **Optimization is evidence, not authority. Governance outranks optimization.**

This document defines what the **Skill Evolution Validation Layer** may and may not do.
It is the guardrail for every validation case and experiment under `evolution/`.

The layer is conceptually inspired by the idea of treating natural-language skill
documents as improvable artifacts — but it deliberately stops at *evidence*. It does
not optimize, train, score, or rewrite anything.

## Where this layer sits

```txt
AletheIA                      contracts, gates, policies, evaluation depth, human decision
Knowledge Governance Layer    sources, authority, sensitivity, scope, restrictions, packs
Adaptive Skills               skills, modules, triggers, verification, handoff signals
Evolution Layer               observations, proposals, reviews, outcomes
Skill Evolution Validation    validation cases, experiments, regression, comparative evidence
  Layer  (this document)
```

The validation layer feeds the existing Evolution Layer. It never bypasses it. A useful
experiment results in a **proposal**, which still goes through human review and a pull
request before any canonical skill changes.

## What an experiment MAY do

- Record a **validation case**: a concrete, reproducible expectation for a skill.
- Run a **baseline vs. candidate** comparison *by hand or by reasoning*, and write down
  what each produced against the validation cases.
- Record a **regression note** when a candidate fixes the target case but degrades a
  case that already worked.
- Produce a **recommendation** whose strongest possible outcome is `proposal-created`.
- Point at real `observations/` and `validation-cases/` as its evidence base.

## What an experiment MUST NOT do

- ❌ Implement SkillOpt, an optimizer runtime, or a benchmark engine.
- ❌ Call an LLM or any model from this layer.
- ❌ Auto-edit, auto-merge, or auto-writeback into any `SKILL.md`.
- ❌ Write anything under `skills/`.
- ❌ Change `evolution/registry.json`, the Knowledge Governance Layer, the Feature Value
  Governance Pack, or AletheIA contracts without an explicit, separate proposal.
- ❌ Turn a score, ratio, or "win count" into a decision. There are no scores here.
- ❌ Approve its own change. No experiment outcome may be `approved` or `merged`.
- ❌ Copy proprietary, confidential, restricted, or regulated content into traces,
  prompts, examples, or any exportable artifact. See
  [validation-case-guidelines.md](validation-case-guidelines.md).

## The only authorized path to a canonical change

```txt
Observation
  → Validation Case
  → Skill Evolution Experiment
  → Regression Check
  → Proposal            (evolution/proposals/)
  → Human Review        (evolution/reviews/)
  → Pull Request
  → Canonical Skill Update
```

Every arrow after **Proposal** is a human decision. The validation layer stops at
evidence; it does not cross into authority.

## Good outcomes that are *not* "a change"

A `reinforced` or `no-change` result is a **success**, not a failure. Confirming that a
skill already behaves correctly under a new case is valuable evidence and prevents
needless churn. Few strong cases beat many weak ones.

## Enforcement

`scripts/validate_evolution_experiments.py` enforces the structural half of these
boundaries (sensitivity declared, synthetic-only for sensitive cases, protected
surfaces require human review, no `skills/` write targets, no `approved` outcome). The
judgment half — "is this evidence actually strong?" — stays with the human reviewer.
