# Example — Specification Facilitation Composition

## Scenario

A consumer project wants to add a readiness summary before an operator starts a multi-step action.

The request is clear enough to plan, but not clear enough to implement safely because the fallback behavior, proof, and task boundary are still ambiguous.

## Skill combination

- `workflow`
- `feature-planning`
- `premortem` only if the failure cost is meaningful and the plan can still change

## Macro layer: AletheIA

AletheIA governs:

- Work Slice framing
- planning depth
- readiness gates
- continuity
- handoff

Example slice frame:

- goal: add a readiness summary before the operator starts the action
- immediate boundary: summary content, visible state, and proof
- out of scope: redesigning the whole workflow, new automation, or changing approval rules
- readiness gate: first slice can proceed only after blocking ambiguity is resolved or marked for human decision

## Micro layer: Adaptive Skills

Adaptive Skills facilitates the method:

- `workflow` states the immediate boundary and minimum proof
- `feature-planning` clarifies what/why, keeps how bounded, and turns the first slice into tasks
- `premortem` stress-tests the plan only if a bad readiness decision would be costly

## Flow

### 1. Clarify

```md
## Clarifications
- `[NEEDS CLARIFICATION]`: Should the readiness summary block the action when one source is unavailable, or only warn the operator?
- `[NEEDS CLARIFICATION]`: Which existing data state is authoritative for readiness?
```

Only these questions are kept because each one changes scope, proof, or readiness.

Questions about visual polish, future automation, or dashboard redesign are deferred because they do not affect the smallest useful slice.

### 2. Spec

```md
## What / Why
- What: show a short readiness summary before the operator starts the action.
- Why: reduce accidental starts when required context is missing or stale.

## How Boundary
- Already decided: use existing readiness data; do not introduce a new data source.
- Not decided yet: whether unavailable data blocks the action or only creates a warning.
- Implementation assumptions: current action semantics remain unchanged in the first slice.
```

### 3. Plan

Smallest useful slice:

- render the readiness summary using existing data;
- show an explicit unavailable-data state;
- keep the underlying action unchanged until the blocking/warning decision is clarified.

### 4. Tasks

| Requirement | Decision | Task | Acceptance Evidence |
|---|---|---|---|
| Operator can see readiness before acting. | Add a summary before the action, not inside a later confirmation. | Render the readiness summary in the existing flow. | Smoke confirms the summary appears before the action. |
| Missing data is visible. | Do not invent readiness from partial data. | Add an unavailable-data state. | Regression check covers missing readiness data. |
| First slice does not change behavior silently. | Keep action semantics unchanged until clarification is resolved. | Avoid block/warn logic in the first slice. | Existing action smoke still passes. |

### 5. Readiness support

Anti-overengineering check:

- No new readiness engine.
- No new automation.
- No redesign of the operator workflow.
- No blocking behavior until the unresolved readiness question is answered.

Premortem decision:

- Do not run `premortem` for the first slice if the summary is informational and reversible.
- Run `premortem` before adding blocking behavior, because a false block or false pass has meaningful operational cost and the plan can still change.

## Why this composition is enough

No new skill is needed because:

- `workflow` already frames the work;
- `feature-planning` owns clarification, slicing, traceability, and proof;
- `premortem` already covers consequential failure analysis;
- AletheIA owns the macro gate and handoff decisions.

The composition improves specification quality without turning Adaptive Skills into a macro framework.
