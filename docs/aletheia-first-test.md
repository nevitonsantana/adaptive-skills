# First AletheIA Test

## Goal

Run a small, explicit test of how Adaptive Skills behaves when AletheIA is used as the macro layer.

This is **not** a benchmark and not a runtime integration.
It is a practical operating test for the macro/micro split:

- **AletheIA** -> framing, proof expectations, review gates, handoff, continuity
- **Adaptive Skills** -> micro execution pattern for the task itself

## Recommended first test shape

Use one small feature-like task with visible proof.

Recommended bundle:
- `workflow`
- `feature-planning`
- `testing`

Optional if the task crosses functions:
- `triad-check`

## What to test

You want to learn whether the split is understandable in real use.

Questions to answer:
- can AletheIA frame the task without absorbing the skill?
- can the skill guide execution without becoming a mini-framework?
- does proof stay clearer when AletheIA owns the gate and the skill owns the execution pattern?
- does handoff stay explicit if a cross-functional step appears?

## Suggested flow

### 1. AletheIA frames the task

Capture:
- goal
- dominant lane
- immediate boundary
- minimum proof
- whether handoff risk exists

### 2. Adaptive Skills drives the micro moves

Use:
- `workflow` to set local execution clarity
- `feature-planning` to define the smallest useful slice
- `testing` to define proportionate proof

### 3. AletheIA evaluates closure

Check:
- was the right skill bundle chosen?
- was the proof explicit enough?
- did a handoff become necessary?
- did any repeated failure suggest a library improvement?

## Expected output of the test

At the end of the test, you should be able to write:
- what AletheIA did
- what the skills did
- what stayed local to the consumer project
- what felt clear
- what felt redundant
- what should change next

## Success criteria

The test is successful if:
- the macro/micro split remains legible
- the task gets better framing and better proof with low overhead
- the skill bundle stays small
- no one confuses project-local rules with the generic library

## Failure signals

- AletheIA starts duplicating the skill internals
- the skill starts duplicating macro governance
- the team cannot tell who owns proof versus execution guidance
- the test needs too much setup for a small task

## Recommended artifact

Use `examples/aletheia/first-test-report.md` as the output skeleton.

## Worked example

If you want to see the test as a concrete scenario, read `examples/aletheia/feature-slice-worked-example.md` and `examples/aletheia/first-test-report-sample.md`.
