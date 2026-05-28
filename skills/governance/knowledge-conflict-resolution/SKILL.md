---
name: knowledge-conflict-resolution
description: Detect conflict between knowledge sources used in the same task and resolve it via source precedence, with escalation when precedence is not enough.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: governance
  knowledge_aware: true
---

# Overview

Use this skill when two or more sources selected by the [knowledge resolver](../../../../aletheia/docs/concepts/knowledge-resolver.md) disagree on a decision-relevant point. It applies the [source-precedence-policy](../../../../aletheia/docs/contracts/source-precedence-policy.md), records the resolution in the audit log, and escalates when precedence cannot settle the conflict.

# When to Use

- A task's resolved context pack contains sources that disagree.
- A skill output would change depending on which source is treated as authoritative.
- Two mandatory sources (e.g. privacy vs. accessibility) appear to conflict.

# When NOT to Use

- Selecting sources in the first place (handled by the resolver).
- Evaluating whether a single source can be registered (use `knowledge-source-evaluation`).
- Checking exposure risk of restricted excerpts (use `restricted-context-check`).

# Core Moves

1. State the conflict precisely: which sources, which decision point, which positions.
2. Locate each source in the precedence tiers.
3. Apply precedence; record the prevailing source and the suppressed sources.
4. Re-derive the affected decision under the prevailing source.
5. If precedence does not settle it (same tier, no tie-break, mandatory-vs-mandatory, deliverable-breaking), escalate to human review.

# Optional Modules

- **Tier tie-break** — apply, in order: authority level → scope specificity → recency → supersedes.
- **Mandatory clash protocol** — generate a structured review request when two mandatory sources collide.
- **Suppressed-source carry-forward** — preserve the lower source as context in the output, not as authority.

# Activation Triggers

- Resolver flags `conflicts_detected` in the context pack.
- A reviewer questions which source governed a decision.
- A `mandatory` source is present alongside an `interpretive` or `evidential` source on the same point.

# Expected Output

```yaml
conflict_resolution:
  conflict_id: <uuid>
  task_id: <task-id>
  between:
    - <pack_id@version>
    - <pack_id@version>
  topic: <decision point in one line>
  positions:
    - source: <pack_id@version>
      position: <one line>
    - source: <pack_id@version>
      position: <one line>
  resolved_by: source_precedence_policy | escalation
  prevailing_source: <pack_id@version | null>
  suppressed_sources: [<pack_id@version>, ...]
  human_review_required: <bool>
  human_review_reason: <if true>
  effect_on_deliverable: <short>
```

# Verification

- Conflict is described precisely enough that a reviewer can replay the reasoning.
- Precedence chosen matches the tier mapping in `source-precedence-policy`.
- Suppressed sources are preserved as context, not erased.
- Escalation fired whenever precedence did not settle the conflict.

# Handoff Signals

- Pass the structured conflict record to the next agent.
- If escalated, do not produce a final deliverable until review returns.

# Pairs Well With

- `knowledge-source-evaluation`
- `restricted-context-check`
- `feature-value-governance` (and any knowledge-aware skill)

# Anti-patterns

- "Splitting the difference" between a mandatory and an interpretive source.
- Dropping the lower-precedence source silently instead of preserving it as context.
- Treating recency as a primary tie-break (it is a tertiary one).
- Resolving in the skill output without writing an audit entry.
