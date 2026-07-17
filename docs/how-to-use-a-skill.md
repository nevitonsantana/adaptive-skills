---
title: How to Use a Skill
description: Choose the smallest fitting skill, apply its core moves, use optional depth selectively, and verify the result.
---

Use a skill when it gives a task a clearer method, output, or verification standard. Do not use a skill merely because it exists.

## The basic loop

1. Identify the dominant need of the task.
2. Choose the smallest skill that addresses that need.
3. Check its “When to Use” and “When NOT to Use” sections.
4. Apply its Core Moves.
5. Activate only modules with a matching trigger.
6. Produce the Expected Output.
7. Check Verification before closing or handing off.

## Start from the task

Ask what the work needs now:

| Need | Example skill |
|---|---|
| Clarify the intended outcome | `intent-clarification` |
| Plan a feature | `feature-planning` |
| Diagnose an unknown failure | `debugging` |
| Implement without scope expansion | `lean-implementation` |
| Test a meaningful change | `testing` |
| Review usability | `heuristic-audit` |
| Examine architecture trade-offs | `architecture-review` |
| Preserve work for another session | `handoff-summary` |

If no skill clearly fits, proceed without one. A forced skill adds ceremony and can make the result worse.

## Check the fit

Before invoking a skill, read:

- **When to Use** — signals that the skill addresses the current need;
- **When NOT to Use** — conditions where another method or no skill is better.

Also confirm that project policy allows the intended action. A skill does not grant permissions or override a review gate.

## State the expected result

Tell the agent what the skill should help produce.

Good:

> Use `feature-planning` to propose the smallest testable slice for this request. Keep unresolved product decisions visible and return scope, risks, acceptance evidence, and the next safe step.

Weak:

> Run every planning skill.

The first instruction names the capability, purpose, and output. The second encourages unnecessary process.

## Apply Core Moves

Core Moves are the essential discipline of a skill. They should shape the work, not be copied mechanically into the response.

A good application:

- adapts the moves to the real task;
- makes assumptions visible;
- produces a concrete artifact;
- stays proportional to risk and complexity.

## Use optional modules selectively

Optional Modules add depth when their Activation Triggers match the task. Examples include security impact, multiple stakeholders, missing evidence, irreversible change, or unclear success criteria.

Do not treat every module as a required phase.

## Verify before closure

Use the skill's Verification section to ask:

- Does the output answer the actual task?
- Are assumptions and unavailable evidence visible?
- Are boundaries and risks clear?
- Is the result reviewable?
- Is the next action explicit?

For consequential work, the project's tests, reviewers, approvals, and source evidence remain authoritative.

## Use more than one skill only when necessary

Skills can form a short sequence when the task genuinely changes mode. For example:

```text
intent-clarification → feature-planning → premortem
```

This sequence first confirms the desired outcome, then plans a bounded slice, then stress-tests a consequential plan. Stop when the current need is satisfied.

## Match explanation depth to the reader

The same skill can communicate at different depths:

| Mode | Communication style |
|---|---|
| Plain | Explain impact first and define technical terms. |
| Guided | Explain the term, why it matters, and where it appears. |
| Professional | Use technical terms with short context. |
| Expert | Focus on project-specific decisions and ambiguity. |

Explanation depth does not change risk, permissions, evidence, or approval requirements.

## Common mistakes

- Selecting from the catalog before understanding the task.
- Running several skills to appear thorough.
- Copying the entire skill into the output.
- Skipping Core Moves because the answer appears obvious.
- Treating optional modules as mandatory.
- Accepting polished language instead of verification.
- Letting a skill replace human or project authority.

## Next steps

- Try the guided [first skill exercise](getting-started/first-skill/).
- Use the [skill catalog](getting-started/skill-catalog/) to choose by trigger.
- Read the [skill model](skill-model/) for the deeper Core + Modules + Triggers design.
