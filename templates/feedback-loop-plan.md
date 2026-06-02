# Feedback Loop Plan

A short plan for building a fast, deterministic, agent-runnable pass/fail signal before changing code. Pairs with the `debugging` skill's **Feedback loop construction** module.

## Failure

_What is wrong, observed where, and how it shows up._

## Smallest reproducible signal

_The minimal input/state that triggers the failure._

## Loop type

- [ ] failing test
- [ ] CLI fixture
- [ ] HTTP script
- [ ] browser script
- [ ] trace replay
- [ ] throwaway harness
- [ ] property/fuzz loop
- [ ] other: ___

## How to run

_Exact command(s) or steps to execute the loop. Keep tool choices as examples; any deterministic runner is acceptable._

## Expected fail state

_What the loop shows before the fix (the red)._

## Expected pass state

_What the loop must show after the fix (the green)._

## Validation gaps

_What this loop does not cover; risks left unproven._

## Recurrence guard

_The automated or procedural guard that keeps this failure from returning, or the rationale for skipping one._
