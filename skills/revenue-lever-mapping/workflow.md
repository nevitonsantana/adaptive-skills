# Workflow — revenue-lever-mapping

Ordered steps for mapping the lever an opportunity moves. Mirrors the Core Moves in `SKILL.md`.

## Step 1 — Frame and resolve knowledge
- State the opportunity in one line.
- Read the resolved `strategic_framework` capsule if present and cite it. If unsatisfied, run generic mode and mark `mode: generic`.

## Step 2 — Name the primary lever
- Choose exactly one: acquisition, activation, retention, expansion, efficiency, margin, strategic_defense.
- One-line rationale tied to a mechanism, not a feeling.

## Step 3 — Name secondary levers
- Zero or more, each clearly subordinate to the primary. If two feel co-equal, run the lever conflict check and force a primary.

## Step 4 — Attach a metric
- The metric that proves the lever moved, with an explicit direction (up/down) and, where possible, a baseline.

## Step 5 — Pick a proxy
- A faster early signal when the true metric is slow. Note the conditions under which the proxy diverges from the metric.

## Step 6 — State risks and uncertainty
- What would make this the wrong lever story; what is not yet known. Never present the map as settled truth.

## Step 7 — Emit and route
- Emit the `revenue_lever_map` block.
- Map fields onto the Feature Value Governance Contract (`revenue_lever`, `primary_metric`, `evidence_level`).
- Hand off to `opportunity-tree-alignment`, `feature-complexity-audit`, or back to `feature-value-governance` as needed.
