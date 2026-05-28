---
name: <your-skill-name>
description: <one-sentence purpose; what it does and when to use it>
version: 0.1.0
owner: adaptive-skills
metadata:
  knowledge_aware: true
  modes:
    - generic
    - knowledge_aware
---

# Overview

<2–4 sentences. What this skill produces, for whom, in what situation.>

# When to Use

- <trigger 1>
- <trigger 2>

# When NOT to Use

- <out-of-scope case 1>
- <out-of-scope case 2>

# Modes

This skill operates in two modes.

## Generic mode

Used when no authorized knowledge pack satisfies the skill's dependencies.

- Apply general criteria from this skill.
- Mark the output as **generic** (no pack citations).
- Do **not** fabricate references to specific frameworks, policies, or personas.

## Knowledge-aware mode

Used when the [knowledge resolver](../../aletheia/docs/concepts/knowledge-resolver.md) returns at least one satisfying pack.

- Reason from the **capsule first**.
- Respect active restrictions (no verbatim, no export, citation required, etc.).
- Cite each consumed pack as `pack_id@version` in the output.
- Surface unsatisfied slots and the fallback applied.

# Core Moves

1. Frame the task and identify required knowledge slots.
2. Read the resolved context pack: satisfied slots, gaps, conflicts, restrictions.
3. Reason from capsules; pull excerpts only when the slot's retrieval mode allows it.
4. Produce the deliverable in the **Expected Output** format below.
5. Write the audit trail (which slots used which pack, what restrictions applied).

# Knowledge Dependencies

Declared in `skill-knowledge-dependency.yaml`. Summary here for the reader:

- `<slot-1>` — required: <true|false|when ...> ; accepted types: <list>
- `<slot-2>` — required: <true|false|when ...> ; accepted types: <list>

Fallback behavior:

- missing required → stop_and_request_source
- missing optional → continue_with_assumption_marker
- restricted source → request_authorized_context_pack
- conflicting sources → apply_source_precedence_policy

# Expected Output

```yaml
result:
  summary: <short>
  decisions:
    - <decision 1>
    - <decision 2>
  knowledge_used:
    - slot: <slot-name>
      pack: <pack_id@version>
      retrieved_scope: capsule | excerpt | metadata | full
      restrictions: [<...>]
  unsatisfied_slots:
    - slot: <slot-name>
      fallback: <applied fallback>
  conflicts:
    - between: [<pack_id@version>, <pack_id@version>]
      prevailing: <pack_id@version>
      reason: source_precedence_policy
  mode: generic | knowledge_aware
```

# Verification

- All required slots either satisfied or stopped per fallback.
- No verbatim restricted text in the output.
- Pack citations present in knowledge-aware mode.
- Audit entries reconstructable from the output.

# Handoff Signals

- Surface unresolved conflicts to the next agent.
- Surface unsatisfied required slots and what authorization would unlock them.
- Carry forward the active restrictions; do not let them drop at the boundary.

# Pairs Well With

- `knowledge-source-evaluation`
- `knowledge-conflict-resolution`
- `restricted-context-check`

# Anti-patterns

- Hardcoding a specific pack id as a requirement.
- Producing knowledge-aware output without citations.
- Silent fallback from required → generic.
- Inlining capsule text into the skill itself.
