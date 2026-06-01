---
name: opportunity-tree-alignment
description: Connect an opportunity tree to revenue levers and the value proposition, producing an aligned outcome -> opportunity -> lever -> feature-hypothesis path and flagging orphan bets.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: product
  knowledge_aware: true
---

# Overview

Use this skill to reorganize an opportunity tree by **economic value and evidence**, not
by enthusiasm. It draws the explicit path `outcome → opportunity → lever → feature
hypothesis` and flags features that serve no live opportunity (orphans) and opportunities
that pull no lever. It carries no proprietary framework; the value lens comes from the
`strategic_framework` slot when available.

# When to Use

- A backlog has competing bets and unclear links to outcomes.
- An opportunity tree exists but does not connect to revenue/value levers.
- You need to decide sequencing across opportunities by value and evidence.

# When NOT to Use

- There is a single, obvious bet with a clear outcome.
- No outcomes or opportunities have been framed yet.
- The lever for one feature is the only question (use `revenue-lever-mapping`).

# Core Moves

1. **Frame and resolve knowledge.** State the outcome(s) under discussion. Resolve
   `strategic_framework` / `operating_model` if present; else generic and mark it.
2. **List the opportunities** claimed under each outcome.
3. **Attach a lever to each opportunity** (delegating to `revenue-lever-mapping` when the
   claim is contested).
4. **Place candidate features** under the opportunity they serve.
5. **Flag orphans** — features with no opportunity, opportunities with no lever, outcomes
   with no opportunity.
6. **Reorder by value × evidence** and state the sequencing rationale.

# Optional Modules

- **Evidence weighting** — Rank opportunities by strength of evidence, separating strong
  signal from wishful framing.
- **Lever balance** — Check whether the tree over-indexes on one lever (e.g. all
  acquisition, no retention).
- **Pruning pass** — Recommend opportunities or features to drop, with the reason recorded.

# Activation Triggers

- Always declare and attempt to resolve `strategic_framework`; treat `operating_model` as
  relevant when the question is sequencing/prioritization.
- Use evidence weighting when bets compete for the same capacity.
- Use the lever balance check when the tree looks one-dimensional.

# Inputs (minimum)

- Outcome(s), opportunities, candidate features.

# Outputs (minimum)

- A tree reorganized by economic value and evidence, with orphans flagged. Feeds the
  `opportunity_tree_node` and `revenue_lever` fields of the
  [Feature Value Governance Contract](../../../aletheia/schemas/feature-value-governance-contract.schema.json).

# Expected Output

```yaml
opportunity_alignment:
  mode: generic | knowledge_aware
  strategic_framework_ref: <pack_id@version | generic>
  tree:
    - outcome: <outcome>
      opportunities:
        - opportunity: <opportunity>
          lever: <primary lever>
          evidence: strong | moderate | weak | assumption
          features:
            - hypothesis: <feature hypothesis>
              serves_opportunity: <bool>
  orphans:
    features_without_opportunity: [ ... ]
    opportunities_without_lever: [ ... ]
  sequencing_rationale: <why this order>
```

# Verification

- Every candidate feature is either placed under an opportunity or flagged as an orphan.
- Every opportunity has a lever or is flagged.
- Sequencing is justified by value and evidence, not by who asked.

# Handoff Signals

- A single bet's lever is contested → `revenue-lever-mapping`.
- A placed feature now needs a cost read → `feature-complexity-audit`.
- A worth-doing verdict is needed → `feature-value-governance`.

# Pairs Well With

- `revenue-lever-mapping`
- `feature-value-governance`
- `business-design`

# Anti-patterns

- Keeping orphan features because someone is attached to them.
- Trees that branch endlessly with no lever at the leaves.
- Sequencing by political weight instead of value × evidence.
