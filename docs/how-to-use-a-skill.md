# How to Use a Skill

Adaptive Skills works best when a skill is treated as a small execution aid, not as a role, a full process, or a replacement for judgment.

Use this guide when adopting a skill in another project or when deciding which skill should guide a specific task.

## 1. Start from the task, not from the catalog

Do not ask: "Which skills are available?"

Ask:

- What is the task trying to accomplish?
- What could fail if we execute poorly?
- Is the main need planning, implementation, review, handoff, debugging, communication, or risk reduction?
- Is this generic work, or is it domain-specific?

Then choose the smallest skill that matches the dominant need.

Examples:

- unclear execution slice -> `feature-planning`
- bug with unknown cause -> `debugging`
- uncertain validation quality -> `testing`
- cross-functional decision -> `triad-check`
- consequential plan with hidden assumptions -> `premortem`

## 2. Check whether the skill should be used

Before using a skill, read:

- `When to Use`
- `When NOT to Use`

This prevents two common mistakes:

- using a heavy skill on a simple task;
- using a generic skill where a project-local rule or domain pack should govern the work.

If the fit is weak, do not force the skill. Pick a smaller one or proceed without a skill.

## 3. Run the core moves

`Core Moves` are the invariant part of the skill.

They should usually happen unless there is a clear reason to skip one. Do not expand them into a rigid ceremony. Their purpose is to keep the work grounded, not to slow it down.

Good use:

- follow the core moves to structure thinking;
- keep outputs short and reviewable;
- make assumptions visible.

Bad use:

- copy the whole skill into the response;
- treat every bullet as a mandatory phase;
- run multiple skills when one would be enough.

## 4. Activate only the needed modules

Optional modules are not default steps.

Use them only when the task has a matching trigger, such as:

- high risk;
- multiple stakeholders;
- security, privacy, data, or reputation impact;
- unclear success criteria;
- missing rollback path;
- weak evidence;
- cross-functional dependency.

For example, `premortem` can stay lightweight for a reversible plan, but should move toward High-Assurance depth when the plan affects data, security, reputation, or AI autonomy.

## 5. Produce a concrete output

A skill should leave behind something reviewable:

- a plan;
- a checklist;
- a diagnosis;
- a revised brief;
- a risk gate;
- a handoff note;
- a recommendation with assumptions and limits.

If the output is only a generic discussion, the skill probably was not used well.

## 6. Verify closure

Use the skill's `Verification` section before treating the work as done.

Ask:

- Did the output answer the actual task?
- Are assumptions visible?
- Are the limits clear?
- Is there a next action?
- Did we avoid pulling project-local rules into the generic canon?

## Example: using `premortem`

Use `premortem` before executing a plan that still can change and has a meaningful cost of failure.

Good trigger:

> "We are about to roll out a quality gate process for AI-assisted code. It affects engineering, security, UX, accessibility, agent behavior, and human approval."

Why `premortem` fits:

- there is a concrete plan;
- the cost of a bad gate is meaningful;
- assumptions are likely hidden;
- the plan can still be adjusted;
- failure modes should become gates before execution.

Expected output:

- likely failure modes;
- most probable failure;
- most dangerous failure;
- hidden assumption;
- warning signals;
- hard gates, soft gates, review triggers, and human decision gates;
- revised plan;
- pre-execution checklist.

Bad trigger:

> "Can you rewrite this sentence?"

That should use a writing or review skill, not `premortem`.

## Healthy adoption rule

Start small.

A useful adoption is not one where every task uses a skill. It is one where the right skill improves clarity, proof, handoff, or decision quality at the right moment.
