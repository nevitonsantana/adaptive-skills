---
title: Choose the right skill
description: Select an Adaptive Skill from the task you need to complete, not from a long inventory.
---

Start with the decision or outcome you need. A skill supports a bounded part of the work; it does not replace human intent or automatically own the whole task.

## Fast decision guide

| Your immediate need | Start with | Add when needed |
|---|---|---|
| The request is ambiguous | `intent-clarification` | `workflow`, then `feature-planning` |
| The task is large or likely to sprawl | `task-chunking` | `workflow`, `checkpoint-review` |
| You need to plan a feature | `feature-planning` | `premortem`, `triad-check` |
| You need to implement an approved slice | `lean-implementation` | `testing`, `qa-review` |
| Something is broken | `debugging` | `testing`, then `handoff-summary` |
| You need to improve structure safely | `refactoring` | `testing`, `architecture-review` |
| You are defining a contract | `api-design` | `architecture-review`, `testing` |
| You are reviewing an interface | `heuristic-audit` | `ux-writing`, `ux-strategy` |
| A UX direction needs challenge | `ux-provocation` | `ux-strategy`, `triad-check` |
| You are deciding whether to build a feature | `feature-value-governance` | `revenue-lever-mapping`, `feature-complexity-audit` |
| You are deciding whether to retire a feature | `sunset-decision` | `feature-complexity-audit`, `communication` |
| Sources disagree | `knowledge-conflict-resolution` | `restricted-context-check` |
| A source may be sensitive or untrusted | `restricted-context-check` | `knowledge-source-evaluation` |
| You need useful telemetry | `observability-review` | `qa-review` |
| Work is ending or changing hands | `handoff-summary` | `checkpoint-review` |

## Selection rules

1. **Choose the dominant need.** Start with the skill that addresses the current bottleneck.
2. **Prefer one skill first.** Add another only when the first skill produces a clear handoff need.
3. **Do not use skill count as a quality signal.** More skills can create more context and coordination cost.
4. **Keep authority explicit.** Skills advise and structure execution; people and governing systems retain decisions.
5. **Read the canonical skill before use.** The installed `SKILL.md` defines triggers, boundaries, Core Moves, and expected evidence.

## Common confusions

### `workflow` or `task-chunking`?

Use `workflow` to frame the whole bounded task. Use `task-chunking` when the work is too large and must be split into reviewable slices.

### `feature-planning` or `lean-implementation`?

Use `feature-planning` to decide the delivery slices. Use `lean-implementation` only after the slice and acceptance evidence are confirmed.

### `testing` or `qa-review`?

Use `testing` to choose reliable proof for changed behavior. Use `qa-review` for a broader consistency and operational-risk review.

### `ux-strategy`, `ux-provocation`, or `heuristic-audit`?

Use `ux-strategy` while choosing a direction, `ux-provocation` to challenge a dominant hypothesis, and `heuristic-audit` to evaluate an interface that already exists.

## Next steps

- Check the [complete skills catalog](https://nevitonsantana.github.io/adaptive-skills/getting-started/skill-catalog/).
- Follow [How to use a skill](https://nevitonsantana.github.io/adaptive-skills/how-to-use-a-skill/) for a safe invocation pattern.
- Use [Workflow recipes](https://nevitonsantana.github.io/adaptive-skills/guides/workflow-recipes/) for tested sequences.
