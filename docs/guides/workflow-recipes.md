---
title: Workflow recipes
description: Combine a small number of Adaptive Skills for common delivery, debugging, design, and governance tasks.
---

Recipes are starting patterns, not automatic pipelines. Run one skill at a time, inspect its output, and decide whether the next skill is still necessary.

## Deliver a new feature

1. `intent-clarification` — confirm outcome, constraints, success, and unresolved ambiguity.
2. `feature-value-governance` — check whether the feature deserves investment when value is uncertain.
3. `feature-planning` — define the smallest useful slice and its proof.
4. `lean-implementation` — implement only the approved slice.
5. `testing` — choose and run risk-appropriate proof.
6. `handoff-summary` — return verified state and the next safe step.

**Stop early when:** intent or value remains unresolved. Do not convert ambiguity into implementation scope.

## Debug a production issue

1. `workflow` — state the incident boundary and closure proof.
2. `debugging` — reproduce, isolate, fix, and guard recurrence.
3. `testing` — validate the failure mode and nearby risk.
4. `communication` — explain impact, resolution, and remaining uncertainty.
5. `handoff-summary` — preserve verified incident context.

**Stop early when:** the issue cannot be reproduced. Record the evidence gap instead of guessing at a fix.

## Review a product experience

1. `ux-strategy` — clarify the experience goal and plausible directions.
2. `heuristic-audit` — identify usability failures in the current interface.
3. `ux-writing` — improve labels, guidance, errors, and decision language.
4. `triad-check` — reconcile product, design, and engineering consequences.

**Optional:** add `ux-provocation` before commitment when the team has converged too quickly on one direction.

## Make an architecture decision

1. `domain-language-alignment` — establish shared terms.
2. `architecture-review` — compare boundaries, coupling, complexity, and maintenance cost.
3. `premortem` — identify failure conditions and warning signals.
4. `triad-check` — review cross-functional consequences when the decision affects the product experience.
5. `communication` — record the decision and trade-offs.

## Govern a feature portfolio decision

1. `revenue-lever-mapping` — make the intended value mechanism explicit.
2. `opportunity-tree-alignment` — connect the bet to an outcome and opportunity.
3. `feature-complexity-audit` — estimate permanent carry cost.
4. `feature-value-governance` — make the auditable investment judgment.
5. `sunset-decision` — use only for an existing feature under keep-or-remove review.

## Use governed knowledge safely

1. `knowledge-source-evaluation` — assess whether the source is suitable and at what maturity.
2. `restricted-context-check` — review leakage, injection, permission, and contamination risks.
3. `knowledge-conflict-resolution` — resolve decision-relevant disagreement between accepted sources.

**Boundary:** these skills do not grant access, override permissions, or turn untrusted content into authoritative instructions.

## Close a long work session

1. `checkpoint-review` — decide whether to continue, stop, or hand off.
2. `qa-review` — check consistency and operational risk if meaningful work changed.
3. `handoff-summary` — package verified state without dragging the full session forward.

## Next steps

- Use [Choose the right skill](./skill-selection/) to adapt a recipe to the current bottleneck.
- Read [How to use a skill](../how-to-use-a-skill/) before invoking the first skill.
- In AletheIA, keep the Work Slice as the governing frame and use skills only inside that boundary.
