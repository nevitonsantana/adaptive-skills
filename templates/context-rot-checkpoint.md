# Context-Rot Checkpoint — fill-in template

Capture a checkpoint at each milestone of a long session, before a structural change, or when
context has grown too far. It keeps a session reviewable and restartable. See AletheIA
`docs/concepts/context-rot-controls.md` for the rot signals and minimal controls.

```yaml
context_checkpoint:
  task_id:
  timestamp:
  current_goal:
  decisions_made:
    - decision:
      rationale:
      evidence:
  active_constraints:
    -
  context_used:
    - source:
      version:
      restriction:
  open_questions:
    -
  next_action:
  stop_conditions:
    -
  should_continue_same_thread: true | false
```

## When to fill this

- at each milestone;
- before a structural change (summarize the decision first);
- when context grows too far (re-anchor to the harness contract);
- when the task exceeds its original scope (hand off);
- when history hurts more than it helps (`should_continue_same_thread: false` → start a new session).
