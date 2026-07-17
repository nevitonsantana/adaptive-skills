---
title: "Skill Evolution Experiments"
description: "Reference documentation for Skill Evolution Experiments in Adaptive Skills."
---

A **skill evolution experiment** compares a skill as it is today (**baseline**) against a
proposed change (**candidate**) using one or more
[validation cases](validation-case-guidelines/), checks for regression, and records a
recommendation. It produces evidence — never a decision.

Read [optimization-boundaries.md](optimization-boundaries/) first.

## The authorized flow

```txt
Execution Evidence
  → Observation              (evolution/observations/)
  → Validation Case          (evolution/validation-cases/)
  → Skill Evolution Experiment (evolution/experiments/)
  → Regression Check
  → Proposal                 (evolution/proposals/)
  → Human Review             (evolution/reviews/)
  → Pull Request
  → Canonical Skill Update
```

Everything up to and including the experiment is **evidence**. Everything after the
proposal is **human authority**. The two never collapse into one step.

## How to run an experiment (by hand)

1. **Start from a signal.** Usually a real observation in `evolution/observations/`.
   Note its id under `source_observations`.
2. **Write or reuse validation cases** that capture the expectation precisely. List them
   under `validation_cases`. At least one is required.
3. **Describe the candidate change.** Fill `candidate_change` with the `target_surface`,
   `change_type`, and a short `summary`. The target surface must be an allowed proposal
   target — never a protected surface (see below).
4. **Record the baseline result.** Run the cases against the skill *as it is*. Write
   which cases passed and which failed, honestly.
5. **Record the candidate result.** Reason through the same cases *with the change
   applied*. Write passed/failed again.
6. **Check for regression.** A candidate that fixes the target case but breaks a case
   that previously passed is a regression. Set `regression_check.regression_found` and
   write a regression note (template provided).
7. **Recommend an outcome** — see below. Set `human_review_required` (`true` for any
   protected surface, knowledge-aware skill, or anything non-trivial).

## Outcomes

`recommendation.outcome` is one of:

| outcome            | meaning                                                              |
| ------------------ | ------------------------------------------------------------------- |
| `reinforced`       | the skill already behaves correctly; evidence strengthens it        |
| `no-change`        | the candidate is not worth it; keep the skill as is                 |
| `proposal-created` | strong evidence; promote to `evolution/proposals/`                  |
| `defer`            | promising but insufficient evidence; revisit after more signals     |
| `rejected`         | the candidate degrades behavior                                     |

There is no `approved` or `merged` outcome. The strongest thing an experiment can do is
create a proposal. `reinforced` and `no-change` are legitimate, valuable results.

## Protected vs. proposal-target surfaces

Reuse the canonical taxonomy from `evolution/registry.json`:

- **Protected surfaces** (never a candidate target): `name`, `description`, `When to Use`,
  `When NOT to Use`, `Core Moves`, `skill-domain`, `skill-category`, `skill-merge-split`,
  `skill-thesis`. If an experiment claims to touch one of these,
  `protected_surface_touched: true` and `human_review_required: true` are mandatory.
- **Proposal targets** (allowed candidate surfaces): `Activation Triggers`,
  `Optional Modules`, `Verification`, `Anti-patterns`, `templates/`, `checklists/`,
  `examples/`, `references/`, `changelog.md`.

`change_type` reuses the registry's change types, e.g. `trigger-adjustment`,
`verification-tightening`, `example-addition`.

## Pilot order

Per the design, start experiments on non-sensitive, generic skills:

1. `feature-planning`
2. `testing`
3. `workflow`
4. `triad-check`
5. `feature-value-governance` (last — it governs product decisions; do not pilot here first)

## Validation

Run `python3 scripts/validate_evolution_experiments.py` before opening a PR. It checks
structure only: no runtime, no model calls, no writes. See the script header for the full
rule list.
