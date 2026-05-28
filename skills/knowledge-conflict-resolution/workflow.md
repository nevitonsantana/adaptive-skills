# Workflow — knowledge-conflict-resolution

## Step 1 — Name the conflict

Write a single line: *which sources, on which decision point, with which positions*. If you cannot state it in one line, the conflict is not yet clear enough to resolve.

## Step 2 — Locate tiers

Use the tier mapping in [source-precedence-policy](../../../aletheia/docs/contracts/source-precedence-policy.md). Tag each source with its tier.

## Step 3 — Tie-break inside a tier

In order:

1. higher `authority_level`
2. narrower, more specific `scope`
3. more recent `version` (only when both still inside `expiry`)
4. explicit `supersedes` / `prerequisite_sources` relationships

## Step 4 — Apply precedence

The higher-tier source's position prevails **in the dimension of conflict**. The lower source is preserved as context.

## Step 5 — Decide escalation

Escalate to human review if any of the following is true:

- two sources at the same tier remain tied after tie-breaks
- two `mandatory` sources conflict
- the suppressed source's removal makes the deliverable infeasible
- the topic is in a `human_review_required_for` condition of any involved source

## Step 6 — Record

Emit the structured `conflict_resolution` block (see SKILL.md "Expected Output") and write an audit entry per [knowledge-audit-log-spec](../../../aletheia/docs/contracts/knowledge-audit-log-spec.md).

## Step 7 — Re-derive the decision

Reproduce the affected decision under the prevailing source. Mention the suppressed source as context, not as authority.
