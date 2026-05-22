# Efficiency Layer First Pilot Guide

## Goal

Run the first real pilot of the Efficiency Layer without turning it into a broad productivity program.

The purpose is to answer:

- do the first three efficiency skills reduce avoidable operational waste?
- do they make bounded work easier to continue, pause, or stop?
- do their boundaries stay clear relative to AletheIA and the other skills?

## Recommended pilot shape

Keep the pilot intentionally small:

- 1 project or lane
- 1 to 3 recurring task shapes
- the initial efficiency trio only:
  - `task-chunking`
  - `handoff-summary`
  - `checkpoint-review`
- 1 to 2 weeks of real use

Do **not** start with a broad process rollout.

## Good pilot lanes

Choose a lane where:

- work tends to arrive oversized
- context grows noticeably across rounds
- handoffs or restarts are common
- the team can compare before and after with real work

Good examples:

- a feature lane with repeated slice creep
- a workstream with many pauses and resumptions
- a debugging or delivery loop that keeps expanding past one clean round

## What to keep local

The pilot should not pull in:

- local release gates
- local review ownership maps
- org-specific scheduling or staffing rules
- company-specific model policy

Those remain local overlays or AletheIA-level macro posture.

## Reference case

A first-validation reference case (Crisis Monitor) is available in [`docs/efficiency-layer-crisis-monitor-reference.md`](efficiency-layer-crisis-monitor-reference.md). Use it when you want one concrete field example of the trio mapped onto a real product lane without treating that product repo as the implementation target. Per [ADR-002](adr/ADR-002-domain-agnosticism.md), this is the first concrete instance, not the canonical pattern.

## Suggested pilot loop

### 1. Pick one recurring lane

Write down:
- project
- lane
- the recurring pain pattern
- which of the three efficiency skills are in scope

### 2. Use only the trio

Prefer the smallest fit:
- `task-chunking` when the task arrives too large
- `checkpoint-review` when a round needs a stop-or-continue decision
- `handoff-summary` when the round should close and resume later

### 3. Capture one short note per meaningful use

Track:
- which skill was used
- why it was triggered
- whether it made the next step clearer
- whether it felt lighter or heavier than the previous way of working

### 4. Review after a small number of rounds

At the end of the pilot, decide:
- which skill was genuinely useful
- which boundary was still confusing
- whether another efficiency skill is justified
- whether the trio is already enough for the lane

## Success criteria

The first Efficiency Layer pilot is successful if:

- at least one recurring lane feels easier to keep bounded
- stop-or-continue decisions become more explicit
- handoffs become smaller and more resumable
- the trio stays clearly separate from AletheIA macro work

## Failure signals

- the pilot becomes a generic productivity initiative
- the trio is used everywhere instead of where pain is real
- the team cannot tell when a problem belongs to feature planning versus chunking
- checkpoint or handoff notes become long ceremony instead of useful compression

## Output artifact

Use `templates/pilot/efficiency-pilot-report.md` to capture the result.
