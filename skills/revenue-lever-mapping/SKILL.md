---
name: revenue-lever-mapping
description: Map which revenue or value lever an opportunity or feature intends to move, with a primary lever, a metric, a proxy, and the risks — so value claims are explicit instead of assumed.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: business
  knowledge_aware: true
---

# Overview

Use this skill to answer one question precisely: **which lever does this move, and how
would we know?** It forces a single primary revenue/value lever, names the metric that
would prove it, a usable proxy for early signal, and the risks to the claim. It carries
**no** proprietary framework; the value lens is resolved via the `strategic_framework`
knowledge slot when available, generic otherwise.

It is one of the capabilities orchestrated by `feature-value-governance`. Use it
standalone when the value claim itself is contested.

# When to Use

- An opportunity or feature is proposed and the value claim is vague ("users will love it").
- Two bets compete and you need to compare the lever each one actually pulls.
- A roadmap item lists no measurable mechanism of value.

# When NOT to Use

- The lever is already named, measured, and uncontested.
- There is no problem framing yet (nothing whose value can be mapped).
- The decision is pure execution planning (use `feature-planning`).

# Core Moves

1. **Frame and resolve knowledge.** State the opportunity in one line. Read the resolved
   `strategic_framework` capsule if present; otherwise run generic and mark it.
2. **Name the primary lever.** Exactly one: acquisition, activation, retention, expansion,
   efficiency, margin, or strategic_defense.
3. **Name secondary levers.** Zero or more, clearly subordinate to the primary.
4. **Attach a metric.** The metric that would prove the lever moved, with a direction.
5. **Pick a proxy.** A faster, cheaper early signal when the true metric is slow.
6. **State risks and uncertainty.** What would make this lever the wrong story; what is
   not yet known.

# Optional Modules

- **Driver decomposition** — Break the lever into its driver model (which funnel step,
  which cost line) when the value claim is contested.
- **Lever conflict check** — When a feature claims multiple co-equal levers, force a
  primary and explain the trade-off.
- **Proxy validity note** — When the proxy could mislead, state the conditions under
  which it diverges from the true metric.

# Activation Triggers

- Always declare and attempt to resolve `strategic_framework`; run generic loudly if unsatisfied.
- Use driver decomposition when stakeholders disagree on whether value exists.
- Use the lever conflict check when more than one lever is claimed as primary.

# Inputs (minimum)

- Problem, target ICP, value proposition, business context.

# Outputs (minimum)

- Primary lever, secondary levers, metric(s), proxy, risks — mappable to the
  `revenue_lever`, `primary_metric`, and `evidence_level` fields of the
  [Feature Value Governance Contract](../../../aletheia/schemas/feature-value-governance-contract.schema.json).

# Expected Output

```yaml
revenue_lever_map:
  opportunity: <one line>
  mode: generic | knowledge_aware
  strategic_framework_ref: <pack_id@version | generic>
  primary_lever: acquisition | activation | retention | expansion | efficiency | margin | strategic_defense
  primary_rationale: <short>
  secondary_levers: [ ... ]
  metric:
    name: <metric>
    direction: <up | down>
  proxy:
    name: <early signal>
    validity: <when it can mislead>
  risks: [ ... ]
  uncertainty: <what is not yet known>
```

# Verification

- Exactly one primary lever.
- The metric has a direction and is tied to the lever, not to activity.
- Uncertainty is stated, not hidden.

# Handoff Signals

- The lever maps a tree of bets → hand to `opportunity-tree-alignment`.
- Permanent cost is now the deciding factor → hand to `feature-complexity-audit`.
- A worth-doing verdict is needed → hand back to `feature-value-governance`.

# Pairs Well With

- `feature-value-governance`
- `opportunity-tree-alignment`
- `business-design`

# Anti-patterns

- Claiming every lever at once.
- Measuring activity ("clicks") as if it were value.
- Treating a proxy as proof.
