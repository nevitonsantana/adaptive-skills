# Harness Trace Summary — fill-in template

A minimal, reviewable summary of what the agent did within its Agent Harness Contract: skills,
tools, context, gates, evidence, and the final decision.

> This template is a human-readable summary. The **machine-checkable per-action record** is the
> AletheIA AHGE record (`schemas/agent-harness-governance-record.schema.json`) — the contract's
> `observability.trace_required` is satisfied by that record. Use this summary to report; use the
> AHGE record to validate.

```yaml
harness_trace:
  task_id:
  agent_id:
  autonomy_level:
  skills_used:
    -
  tools_called:
    - name:
      action_type:
      result:
  context_used:
    - source:
      retrieval_mode:
      restrictions:
  gates_triggered:
    - gate:
      decision:
      rationale:
  evidence:
    - type:
      result:
  gaps:
    -
  final_decision:
  human_review_required:
```

## See also

- [agent-harness-contract.yaml](agent-harness-contract.yaml) — the declared envelope this trace reports against
- AletheIA `docs/contracts/agent-harness-governance-extension.md` — the per-action record this mirrors
