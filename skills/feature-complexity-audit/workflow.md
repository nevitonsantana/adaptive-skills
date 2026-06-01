# Workflow — feature-complexity-audit

Ordered steps for estimating permanent cost. Mirrors the Core Moves in `SKILL.md`.

## Step 1 — Frame
- State the feature and the exact scope being costed. Identify the task shape (interface_change, content_decision, customer_facing_experience) — it decides whether `accessibility_guidelines` becomes required for the governance dimension.

## Step 2 — Score four dimensions
- Cognitive, technical, operational, governance — each low/medium/high with named drivers. Do not collapse into a single technical estimate.

## Step 3 — Name reversibility
- reversible / partially_reversible / one_way_door, with mechanisms (flag, cohort, rollback, sunset, migration plan). If `one_way_door`, run the one-way-door check and require a technical gate.

## Step 4 — Roll up
- Combine into a coarse level (low/medium/high) and name the dominant driver. Keep it honest and coarse — no false-precision decimals.

## Step 5 — Recommend reduction
- The smallest scope that keeps the value, or — if high cost is accepted — the explicit `exception_approval` the contract will require.

## Step 6 — Emit and route
- Emit the `complexity_scorecard`; map to the contract's `complexity_cost` and `reversibility`.
- A `high` rolled-up level under a `build_now` verdict routes to human review and requires `decision.exception_approval`.
