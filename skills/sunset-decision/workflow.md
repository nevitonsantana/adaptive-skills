# Workflow — sunset-decision

Ordered steps for judging an existing feature. Mirrors the Core Moves in `SKILL.md`.

## Step 1 — Frame and resolve knowledge
- Name the feature. Pull usage, cost, support load, strategic alignment, and dependency signals. Resolve `strategic_framework` if present; else generic and mark it.

## Step 2 — Read traction vs. cost
- Decide whether value-per-cost is positive, flat, or negative. Use all three of usage, cost, and support — never one alone.

## Step 3 — Map dependencies
- List what breaks if the feature changes, internal and customer-facing. Run the strategic-account check to find high-value dependents.

## Step 4 — Choose a disposition
- keep, limit, refactor, deprecate, or remove.

## Step 5 — Attach a plan
- deprecate/remove → migration/removal plan (announce → path → grace → decommission) with a churn guardrail.
- limit/refactor → the reduced scope.
- keep → the next review trigger.

## Step 6 — State evidence and uncertainty
- Cite the data behind the disposition; name what is not yet known (e.g. unsized migration friction for strategic accounts).

## Step 7 — Emit and record
- Emit the `sunset_decision_record`; record as a `sunset` (or `park`) decision on the Feature Value Governance Contract for audit.
