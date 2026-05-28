# Workflow — feature-value-governance

Ordered steps for judging whether a proposed feature is worth doing. Mirrors the Core Moves in `SKILL.md`.

## Step 1 — Frame and resolve knowledge

- State the proposed feature in one line.
- Identify the task shape: is it an `interface_change`, `content_decision`, `customer_facing_experience`, `roadmap_decision`, or `prioritization_decision`? The shape decides which conditional slots become required.
- Read the resolved context pack: which slots are satisfied (and by which `pack_id@version`), which are unsatisfied, which restrictions are active, which conflicts were flagged.
- If a **required** slot is unsatisfied, apply `fallback_behavior` (`stop_and_request_source`) and say so loudly. Do not proceed as if the source were present.
- If no pack is available at all, continue in **generic mode** and mark the output `mode: generic`.

## Step 2 — Surface business intent

- Name the business or product intent the feature serves.
- Knowledge-aware mode: anchor it to the resolved `strategic_framework` capsule and cite the pack.
- Generic mode: derive it from stated goals and mark it as an inference.

## Step 3 — Name the lever

- Identify the single primary revenue or operational lever: acquisition, conversion, retention, expansion, cost-to-serve, or risk reduction.
- Give a one-line rationale. One feature, one primary lever.

## Step 4 — Weigh user evidence

- If `personas` resolved, pull the relevant capsule/excerpt (respect retrieval mode) and summarize the evidence.
- If not, state the user assumption explicitly and set `is_assumption: true`.

## Step 5 — Check opportunity-tree alignment

- Place the feature against the opportunity / outcome it claims to serve.
- Flag a feature that serves no live opportunity as misaligned.

## Step 6 — Estimate complexity cost

- Give a coarse read: low / medium / high, with the main drivers.
- Treat complexity as a cost weighed against value, not an automatic veto.

## Step 7 — Assess overreach risk

- Judge reach into compliance, accessibility, and privacy.
- If a `required_when` trigger matched, the relevant slot (e.g. `accessibility_guidelines`) is **required**; an unmet required slot stops the analysis per fallback.
- Assess each triggered dimension against the resolved normative pack, or against general norms with a clear generic marker.

## Step 8 — Render verdict and audit trail

- Emit the `feature_value_analysis` block (see `SKILL.md` "Expected Output" and `template.value-analysis.md`).
- Cite every consumed pack as `pack_id@version`.
- List unsatisfied slots and the fallback applied.
- Record any conflicts and how the [source precedence policy](../../../aletheia/docs/contracts/source-precedence-policy.md) resolved them.
- Route `likely` overreach risk and unresolved mandatory conflicts to human review before commitment.
