# AletheIA Integration

## Macro versus micro

AletheIA and Adaptive Skills are complementary, not interchangeable.

- **AletheIA** handles macro orchestration: framing, gates, review, handoffs, continuity, and learning.
- **Adaptive Skills** handle micro execution: specialist heuristics, reusable workflows, output discipline, and failure signals.

## Integration points

AletheIA may:
1. suggest the most relevant skill
2. suggest optional modules based on context
3. require minimum proof before closure
4. detect that a handoff is required
5. turn repeated breakdowns into observations or proposals
6. help carry learning across rounds when the same lane keeps exposing the same friction


## Agent-role consumption layer

AletheIA roles may consume Adaptive Skills without turning this repository into an agent framework.

Healthy reading model:

- **AletheIA role** -> semantic responsibility
- **Adaptive Skill** -> reusable micro-execution support
- **projection / runtime adapter** -> consumer-local delivery mechanism

That means a consumer may keep the same role across Codex and Claude Code while changing only how the skills are loaded or projected locally.

For the recommended role-to-skill matrix, see `docs/agent-role-integration.md`.

## Important boundary

Skills remain useful without AletheIA.

This repository should never assume that AletheIA is installed, running, or required.

## First practical test

If you want to try the macro/micro split in a real task, start with `docs/aletheia-first-test.md` and `examples/aletheia/first-test-report.md`.

## Real case reference

If you want to see the model after two real rounds in a product lane, read:

- `docs/crisis-monitor-case-study.md`
- `examples/aletheia/crisis-monitor-two-round-pilot.md`

## Evolution-layer boundary

The evolution layer can be informed by AletheIA, but it should never depend on AletheIA to exist.
AletheIA may surface recurring signals; the Adaptive Skills repository still owns the governed writeback through its own review process.

## Efficiency-layer boundary

A future Efficiency Layer may align closely with AletheIA because both care about handoffs, checkpoints, and bounded work. Even then, the Efficiency Layer should remain an Adaptive Skills track rather than becoming an AletheIA requirement.

## Current Efficiency Layer focus

The current Efficiency Layer roadmap is intentionally narrow.
Its first candidate skills are:

- `task-chunking`
- `handoff-summary`
- `checkpoint-review`

These are intentionally lighter than model-routing or prompt-framing and should be easier to validate with real work before deeper overlap with AletheIA is considered.
