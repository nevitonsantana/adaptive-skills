---
name: handoff-summary
description: Close a round of work with enough verified context for the next round without dragging the full session forward.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: efficiency
---

# Overview

Use this skill when work needs to continue later, cross to another person or agent, or restart cleanly without carrying the whole original context.

# When to Use

- a task will continue in another round
- another person or agent may resume the work
- the session is becoming too heavy to keep carrying forward
- a clean restart is healthier than continuing with full context

# When NOT to Use

- the work is already complete and does not need continuation
- the next step is immediate and stays inside the same small round
- the real need is macro review or gate escalation rather than summary

# Core Moves

1. State the current task state in one short paragraph.
2. Record what has already been proved.
3. Name what remains open or unresolved.
4. Give the next recommended step.
5. Call out any missing evidence, risks, or blockers that the next round must see.

# Optional Modules

- **Boundary note** — explain which ownership, domain, or operating boundary the next round will cross.
- **Proof bundle** — list the exact artifacts or checks that already support the current state.
- **Restart guidance** — tell the next round what to read first and what can be ignored.

# Activation Triggers

- Use the boundary note when the next round crosses skill, team, or system ownership.
- Use the proof bundle when the next operator should not have to rediscover validation work.
- Use restart guidance when the original session is too large to re-read efficiently.

# Expected Output

- concise current state
- proof already obtained
- open items
- next step
- visible blockers or risks

# Verification

- Another operator could resume without reconstructing the whole round.
- Proven versus unproven work is visibly separated.
- The next step is concrete enough to act on.
- The summary is smaller than the original session but still safe to continue from.

# Handoff Signals

- The next step needs macro gate, escalation, or formal review posture.
- The work is crossing into a new operating context that needs more than a local summary.
- The summary reveals that the work should stop rather than continue.

# Pairs Well With

- `workflow`
- `task-chunking`
- `checkpoint-review`

# Anti-patterns

- Writing a long replay of the whole session instead of a resumable summary.
- Hiding uncertainty inside polished prose.
- Calling something done when only one round of evidence exists.
