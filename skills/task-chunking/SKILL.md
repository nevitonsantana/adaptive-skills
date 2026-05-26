---
name: task-chunking
description: Break oversized work into smaller, reviewable slices with explicit stop conditions and next-slice boundaries.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: efficiency
---

# Overview

Use this skill when the task is too large, too fuzzy, or too entangled to execute safely as one block.

# When to Use

- the work enters as one oversized request
- the first useful slice is still unclear
- dependencies are making the task feel bigger than it should be
- the team needs a clear stop condition before execution expands

# When NOT to Use

- the task is already a small, obvious slice
- the real problem is feature definition rather than execution shape
- the work needs macro gate or policy review instead of chunking

# Core Moves

1. Name the smallest useful slice that can stand on its own.
2. Separate what belongs in this slice from what must wait.
3. Identify the minimum dependencies needed for the current slice.
4. Declare the stop condition for this round.
5. Name the next slice only if it is already justified.

# Optional Modules

- **Dependency thinning** — reduce or defer cross-system coupling when the slice is too entangled.
- **Checkpoint insertion** — add a short pause point when the work is likely to sprawl mid-round.
- **Handoff-ready slicing** — make the current slice legible enough for another round or another operator to continue later.

# Activation Triggers

- Use dependency thinning when the task keeps expanding because of other systems or teams.
- Use checkpoint insertion when the round is likely to grow past one clean execution pass.
- Use handoff-ready slicing when another round, session, or agent may need to resume the work.

# Expected Output

- smallest useful slice
- explicit in-slice versus later boundary
- dependency notes for the current slice
- stop condition for the round
- optional next-slice marker

# Verification

- The current slice can be explained without listing the entire larger initiative.
- The stop condition is explicit enough to prevent silent scope growth.
- Dependencies kept for the current slice are truly necessary.
- The next slice is not being smuggled into the current one.

# Handoff Signals

- The current slice is blocked by another ownership boundary.
- The next slice would require a different skill or operating context.
- Macro review or gate posture is needed before continuing.

# Pairs Well With

- `workflow`
- `feature-planning`
- `checkpoint-review`

# Anti-patterns

- Renaming a large task as a “slice” without reducing it.
- Keeping hidden future work inside the current chunk.
- Treating chunking as a substitute for product or architecture decisions.
