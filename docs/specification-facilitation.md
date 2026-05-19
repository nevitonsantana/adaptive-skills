# Specification Facilitation

Use this guide when a feature request needs light specification discipline before implementation, but does not need a new framework, CLI, or mandatory ritual.

The recommended composition is:

```txt
workflow -> feature-planning -> premortem
```

- `workflow` frames the immediate work boundary and minimum proof.
- `feature-planning` clarifies the feature, selects the smallest useful slice, and connects requirements to tasks and evidence.
- `premortem` is optional. Use it only when the plan has meaningful cost of failure and can still be changed.

This is a Spec Kit-inspired facilitation pattern, not a copy of Spec Kit. Adaptive Skills should not create `.specify/`, slash commands, project constitutions, CLI automation, or a mandatory specification lifecycle.

## Boundary with AletheIA

AletheIA governs the slice.
Adaptive Skills facilitates the method.

That means:

- AletheIA owns Work Slice framing, planning depth, readiness gates, continuity, governance, and handoff.
- Adaptive Skills owns micro-execution support: clarification, scope discipline, traceability, anti-overengineering review, and output quality.

The composition remains useful without AletheIA. A consumer can use the same skill sequence for any feature plan that needs clarification before execution.

## When to use

Use this facilitation when:

- a feature request is real enough to plan, but still has material ambiguity;
- assumptions could change scope, proof, architecture, or readiness;
- the team needs a short spec before tasks;
- the first slice must stay small and reviewable;
- tasks need traceability back to requirements and decisions.

## When not to use

Do not use this facilitation when:

- the task is a tiny edit with obvious scope;
- the issue is still only an idea and needs product framing first;
- the plan is already clear and only needs implementation;
- a simple checklist would resolve the uncertainty faster;
- using the flow would add ceremony without changing decisions.

## Flow

### 1. Clarify

Use `workflow` and the `Specification clarification` module in `feature-planning`.

Capture only questions that change execution:

- scope
- acceptance evidence
- technical direction
- readiness
- risk posture

Mark unresolved items explicitly:

```md
- `[NEEDS CLARIFICATION]`: Which user state should receive the new fallback message?
```

Do not fill gaps by inventing requirements.

### 2. Spec

Write the smallest useful feature brief.

Keep the layers separate:

- **what** should change;
- **why** it matters;
- **how** is already decided;
- **how** is intentionally not decided yet.

The spec should be enough to plan the first slice, not enough to describe every future phase.

### 3. Plan

Use `feature-planning` to choose the smallest useful slice and break it into verifiable increments.

Add traceability only where it helps review:

| Requirement | Decision | Task | Acceptance Evidence |
|---|---|---|---|
| User sees the fallback state before acting. | Reuse existing data state and do not change publish semantics. | Render fallback copy in the summary card. | Smoke confirms fallback appears and publish behavior is unchanged. |

### 4. Tasks

Tasks should come from the trace, not from speculative architecture.

Each task should have:

- a requirement or decision behind it;
- a visible acceptance condition;
- no hidden future-phase work.

### 5. Readiness support

Before execution, run the anti-overengineering check:

- Is any task solving a future problem rather than the first slice?
- Is any technical decision unsupported by the current requirement?
- Is any ambiguity blocking proof or readiness?
- Would `premortem` materially improve the plan because failure cost is meaningful?

If the answer to the last question is yes, run `premortem` before implementation. Otherwise, keep the proof proportional and proceed with the smaller plan.

## Output shape

A compact output is enough:

```md
## Clarifications
- `[NEEDS CLARIFICATION]`:

## What / Why
- What:
- Why:

## How Boundary
- Already decided:
- Not decided yet:

## Smallest Useful Slice

## Requirement → Decision → Task → Evidence

## Overengineering Check

## Acceptance Evidence
```

## Failure modes

- Treating specification facilitation as a required ceremony for every task.
- Expanding Adaptive Skills into macro governance.
- Hiding unresolved ambiguity inside confident planning language.
- Creating tasks that cannot be traced back to a requirement or decision.
- Running a full premortem when a small clarification pass is enough.
