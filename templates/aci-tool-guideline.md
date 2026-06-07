# ACI Tool Guideline — fill-in template

Document a single tool against the Agent-Computer Interface (ACI) design bar before listing it in
an Agent Harness Contract's `allowed_tools`. ACI is about tool **design** (is this a good tool to
expose?); the AletheIA tool permission matrix is about **permission** (what authority does it need?).
See AletheIA `docs/concepts/agent-computer-interface.md`.

```yaml
aci_tool_guideline:
  tool_name:
  purpose:
  action_type: read | write | execute | transform | external_call
  risk_level: low | medium | high | critical
  input_schema:
    required_fields:
      -
    optional_fields:
      -
  output_schema:
    success_shape:
    error_shape:
  error_behavior:
    actionable_message_required: true
    retry_allowed: true
  idempotency:
    idempotent: true | false
    notes:
  gates:
    requires_confirmation:
    requires_human_review:
  examples:
    good:
    bad:
```

## Design bar (checklist)

- explicit name that reveals consequence;
- short, unambiguous description;
- restricted input schema;
- predictable output schema;
- actionable error messages;
- usage examples (good and bad);
- explicit states;
- idempotent where possible;
- scope limits;
- confirmation for irreversible actions.

## Anti-patterns

- a tool too generic; free-text output where a schema would do; an error with no recommended action;
  a name that hides consequence; a tool that mixes read and write; an irreversible action without a
  gate; a tool that returns too much context.
