# Looping Models for Skills

Two of the ten execution patterns are loops: `loop_until_done` (repeat until an objective stop
condition) and `scheduled_stateful_loop` (recurring runs with persistent state). This doc covers
what a skill must declare before it is allowed to run inside either. Loop permission itself is
governed in the AletheIA repo (`docs/contracts/objective-gate-policy.md`); this page is the
skill-side view.

## The layering heuristic

```txt
timer     → outside the skill (schedule/recurrence is the orchestration's concern)
condition → inside the loop (the objective stop condition that ends a run)
skill     → innermost (does one bounded unit of work per iteration)
```

A skill never owns the timer and never owns the stop condition. It does one verifiable unit of
work per iteration and reports evidence. If a skill needs to know "how many runs so far" or "what
was already done", that is **loop state**, owned by the orchestration (AletheIA
`docs/contracts/loop-state-contract.md`) — not skill-internal memory.

## Preconditions a loop-compatible skill inherits

A skill may declare compatibility with a loop pattern **only under conditions** that satisfy the
loop rule:

1. an **objective stop condition** exists (tests pass, queue empty, budget reached — not "until it
   looks good");
2. a **budget** (token, time, or iteration) bounds the run;
3. **persistent state** exists when the loop recurs;
4. an **objective gate** verifies any artifact the iteration changes;
5. **human review** precedes any irreversible action.

If any precondition is missing at run time, the skill's `escalation_triggers` must include
`objective_gate_missing` so the run routes back to AletheIA instead of looping anyway.

## loop_until_done vs scheduled_stateful_loop, from the skill side

| | `loop_until_done` | `scheduled_stateful_loop` |
|---|---|---|
| Volume | uncertain, finite | recurring, open-ended |
| State | within-run only | persistent loop state across runs |
| Skill must declare | objective gate + `max_iterations` | the above + state read/write expectations + audit per run |
| Typical skills | [debugging](../examples/execution-patterns/debugging-patterns.yaml) with a failing-test gate | triage-style classification with a queue-empty condition |

## Skills that must not loop

Judgment-heavy skills declare loop patterns as **incompatible**, with the rationale recorded —
e.g. [feature-value-governance](../examples/execution-patterns/feature-value-governance-patterns.yaml):
feature judgment has no objective stop condition, and a recurring automated roadmap action would
create governance risk. Incompatibility is a declaration, not a runtime block; enforcement stays
with the harness.

## Related

- [execution-patterns-for-skills.md](execution-patterns-for-skills.md) — the pattern axis
- [pattern-compatibility-guidelines.md](pattern-compatibility-guidelines.md) — filling the declaration
- [skills-in-orchestrated-workflows.md](skills-in-orchestrated-workflows.md) — stage participation
