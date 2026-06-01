# Workflow — opportunity-tree-alignment

Ordered steps for aligning an opportunity tree to value. Mirrors the Core Moves in `SKILL.md`.

## Step 1 — Frame and resolve knowledge
- State the outcome(s) under discussion. Resolve `strategic_framework` / `operating_model` if present and cite; else run generic and mark `mode: generic`.

## Step 2 — List opportunities
- Under each outcome, list the opportunities currently claimed.

## Step 3 — Attach a lever per opportunity
- Name the primary lever for each. Delegate to `revenue-lever-mapping` when the value claim is contested.

## Step 4 — Place candidate features
- Put each candidate feature under the single opportunity it serves.

## Step 5 — Flag orphans
- Features with no opportunity, opportunities with no lever, outcomes with no opportunity — list them explicitly.

## Step 6 — Reorder by value × evidence
- Sequence opportunities by economic value weighted by evidence strength. Record the rationale; do not order by who asked.

## Step 7 — Emit and route
- Emit the `opportunity_alignment` block; map placed features to the contract's `opportunity_tree_node` and `revenue_lever`.
- Route contested levers to `revenue-lever-mapping`, cost reads to `feature-complexity-audit`, verdicts to `feature-value-governance`.
