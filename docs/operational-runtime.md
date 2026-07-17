---
title: "Operational Runtime Model"
description: "Reference documentation for Operational Runtime Model in Adaptive Skills."
---

Adaptive Skills should define runtime contracts before it builds runtime machinery.

This document describes how a consumer runtime may use the capability layer. It is not an implementation of a runtime engine.

## Lifecycle

```txt
1. Intake
2. Context classification
3. Capability routing
4. Depth selection
5. Execution
6. Checkpoint or gate
7. Validation
8. Handoff or closure
9. Execution record
10. Evolution signal
```

## Runtime context

A runtime context should be small enough to hand off and explicit enough to review.

```json
{
  "task_id": "optional-local-id",
  "goal": "Turn vague feature request into a small executable slice",
  "risk_level": "medium",
  "ambiguity_level": "high",
  "selected_capabilities": ["workflow", "feature-planning"],
  "activated_modules": ["ambiguity-check", "scope-boundary"],
  "mode": "workflow/extended",
  "human_approval_required": false,
  "evidence_expected": ["clarifications", "smallest-slice", "acceptance-evidence"]
}
```

## Checkpointing

A checkpoint should happen when continuing by momentum is riskier than pausing.

Typical triggers:

- context is too large;
- task shape changed;
- proof is unclear;
- next step crosses ownership;
- human approval may be needed;
- execution mode needs to deepen or shrink.

Use `checkpoint-review` for local pauses. Use AletheIA when the pause is a macro gate or governance decision.

## Resumability

A resumable execution should leave:

- current goal;
- selected capabilities and modules;
- what was proved;
- what remains unresolved;
- next recommended step;
- risks, blockers, or human decisions.

Use `handoff-summary` when the next round needs a clean restart.

## Observability

The first layer of observability is an execution record, not telemetry automation.

The record should help decide:

- did the selected capability fit?
- was the selected depth proportional?
- did evidence support closure?
- did a routing hint fail?
- should the Evolution Layer receive an observation?

## Approval boundaries

Risky or state-changing actions belong to the runtime and governance layer, not the capability metadata.

Adaptive Skills may say:

```txt
human decision gate required
```

But the actual approval mechanism belongs to AletheIA or the consumer runtime.
