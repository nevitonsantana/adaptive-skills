---
name: sunset-decision
description: Decide whether an existing feature should be kept, limited, refactored, deprecated, or removed — based on usage, cost, support load, strategic alignment, and dependencies — and produce an auditable sunset decision record.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: governance
  knowledge_aware: true
---

# Overview

Use this skill to judge an **existing** feature against its ongoing cost. Most governance
looks forward at new bets; this one looks back at what is already carried. It weighs
usage, permanent cost, support load, strategic alignment, and dependencies, and returns
one of five dispositions with a migration/removal plan when warranted. Killing a feature
that no longer earns its keep is a healthy outcome, not a failure.

# When to Use

- A feature has low traction but ongoing maintenance, support, or security cost.
- A periodic portfolio review of carried features.
- A feature blocks a platform upgrade or widens the attack surface.
- Cost-cutting pressure needs a principled, auditable way to choose what to drop.

# When NOT to Use

- The feature is new and has not had a fair chance to show traction.
- The decision is about a *new* feature (use `feature-value-governance`).
- There is no usage, cost, or support data at all to reason from.

# Core Moves

1. **Frame and resolve knowledge.** Name the feature and pull the signals: usage, cost,
   support load, strategic alignment, dependencies. Resolve `strategic_framework` if present.
2. **Read traction vs. cost.** Is value-per-cost still positive, flat, or negative?
3. **Map dependencies.** Who/what breaks if it changes — internal and customer-facing.
4. **Choose a disposition:** keep, limit, refactor, deprecate, or remove.
5. **Attach a plan.** For deprecate/remove: a migration/removal plan with a churn
   guardrail. For limit/refactor: the reduced scope. For keep: the next review trigger.
6. **State evidence and uncertainty.** Cite the data; name what is not known (e.g.
   strategic accounts whose migration friction is unsized).

# Optional Modules

- **Migration plan** — Phased deprecation: announce → provide path → grace period →
  decommission, with a churn guardrail.
- **Strategic-account check** — Identify high-value accounts that depend on the feature
  and size their migration friction before removal.
- **Cost-recovery estimate** — Quantify the maintenance/security/upgrade cost recovered by
  removal.

# Activation Triggers

- Always pull usage AND cost AND support signals; a disposition with only one is unsafe.
- Use the strategic-account check before any `remove` or `deprecate` disposition.
- Use the migration plan whenever the disposition is deprecate or remove.

# Inputs (minimum)

- Usage, cost, support load, strategic alignment, dependencies.

# Outputs (minimum)

- One disposition (keep / limit / refactor / deprecate / remove) with a plan and an
  auditable rationale — recorded as a `sunset` (or `park`) decision on the
  [Feature Value Governance Contract](../../../aletheia/schemas/feature-value-governance-contract.schema.json).

# Expected Output

```yaml
sunset_decision_record:
  feature: <one line>
  mode: generic | knowledge_aware
  signals:
    usage: <summary + numbers>
    permanent_cost: <summary>
    support_load: <summary>
    strategic_alignment: <summary>
    dependencies: [ ... ]
  value_per_cost: positive | flat | negative
  disposition: keep | limit | refactor | deprecate | remove
  plan: <migration/removal plan, reduced scope, or next review trigger>
  churn_guardrail: <what must not happen>
  evidence: [ ... ]
  uncertainty: <what is not yet known>
```

# Verification

- The disposition rests on usage AND cost AND support, not a single signal.
- Deprecate/remove always carries a migration plan and a churn guardrail.
- Strategic-account dependencies are checked before removal.
- Evidence and uncertainty are both stated.

# Handoff Signals

- A removal needs a structural plan → `architecture-review`.
- The feature should be reshaped rather than removed → `feature-planning`.
- The portfolio question is really "what new bet replaces this" → `feature-value-governance`.

# Pairs Well With

- `feature-value-governance`
- `feature-complexity-audit`
- `observability-review`

# Anti-patterns

- Keeping a feature because removing it feels like admitting failure.
- Removing a feature without a migration path for the accounts that use it.
- Deciding on usage alone while ignoring the cost it offsets (or vice versa).
