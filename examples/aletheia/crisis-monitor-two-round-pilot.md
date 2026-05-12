# Crisis Monitor — Two-Round Pilot

This example shows a real small-lane pilot where **AletheIA** handled the macro layer and **Adaptive Skills** handled the micro layer.

## Lane

- routing
- approval
- follow-up explainability

## Round 1

### Skills

- `workflow`
- `feature-planning`
- `testing`

### Outcome

The base bundle was enough to validate the first real consumer use of the library in the lane.

## Round 2

### Skills

- `workflow`
- `feature-planning`
- `testing`
- `ux-writing` (triggered)

### Trigger

A mixed-language audit label created unnecessary friction:

- `Justificativa humana do approval`

It was changed to:

- `Justificativa humana da aprovação`

### Outcome

This proved that optional skills can enter because of a real trigger instead of becoming part of the default bundle too early.

## Why this example matters

It demonstrates three things at once:

1. a bounded lane is enough for a useful first pilot
2. AletheIA and Adaptive Skills can stay clearly separated
3. optional skill activation should be evidence-driven

For the fuller write-up, see `docs/crisis-monitor-case-study.md`.
