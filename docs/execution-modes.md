# Execution Modes

Execution modes define how deep a capability should run.

The rule is: use the shallowest mode that still makes the next step safe, reviewable, and restartable.

## Workflow modes

```txt
workflow/basic
 └── obvious task, low risk, small proof

workflow/extended
 ├── material ambiguity
 ├── dependencies
 └── multiple validation steps

workflow/high-risk
 ├── irreversible or costly failure
 ├── human decision gate
 ├── traceability
 └── premortem or readiness review

workflow/multi-agent
 ├── multiple specialists
 ├── coordination protocol
 ├── checkpoint and handoff discipline
 └── AletheIA-level governance
```

## Debugging modes

```txt
debugging/quick-fix
 └── obvious local failure, low blast radius

debugging/root-cause
 ├── reproducible failure
 ├── boundary check
 └── recurrence guard

debugging/production-incident
 ├── high urgency
 ├── observability-first
 ├── rollback or escalation
 └── human approval boundaries
```

## Governance tradeoffs

| Mode | Benefit | Cost |
|---|---|---|
| Basic | Fast and light | May miss hidden ambiguity |
| Extended | Better clarity and proof | More context and tokens |
| High-risk | Safer consequential decisions | More governance overhead |
| Multi-agent | Better specialization | Coordination complexity |

## Token and resource implications

- Basic mode should avoid extra artifacts unless they change the decision.
- Extended mode may produce a compact plan or trace.
- High-risk mode justifies deeper context, risk mapping, and gates.
- Multi-agent mode must pay for coordination only when role split improves quality.

## Anti-overengineering check

Before deepening the mode, ask:

- What risk does the deeper mode reduce?
- What decision becomes more reviewable?
- What evidence would be missing without it?
- Would a smaller checkpoint be enough?

If the answer is unclear, stay shallow.
