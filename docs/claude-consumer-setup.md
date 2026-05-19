# Claude Consumer Setup

## Goal

Use Adaptive Skills in a Claude-oriented workflow without pretending that v0 supports symmetric auto-installation.

In v0, Claude projection is intentionally selective.
That means the repository helps you decide what to reuse, but it does not try to force every skill into a Claude-native installation shape.

Start with skill selection, not projection symmetry. A skill can be useful in Claude by reference before it needs a Claude-specific wrapper.

## Current Claude modes

The projection registry uses three modes:

- `link-only` — keep the canon in this repository and point local docs or workflows to it
- `manual` — adapt the skill deliberately for the Claude workflow in your consumer project
- `available-not-default` — the skill is still available for Claude use, but it is not part of the current default operating path

You can inspect the current state with:

```bash
python3 scripts/report_projection_status.py
python3 scripts/project_to_claude.py
```

## Recommended adoption order

### 1. Choose the skill from the task

Read:

- `docs/how-to-use-a-skill.md`
- `docs/consumer-adoption.md`

Then decide:

- what task or lane Claude is supporting
- which skill fits the dominant need
- whether the canonical skill is enough by reference
- whether the consumer project needs a local wrapper

### 2. Start from the canon, not from duplication

Read the selected skill in this repository first.
If the skill is enough as-is, use `link-only` behavior in your local project notes or workflow docs.

For example, `premortem` can often be used by linking to the canonical skill and asking Claude to follow its core moves. A wrapper is only needed if the team has a repeated Claude-specific planning ritual.

### 3. Adapt only the skills that really need Claude-specific handling

Good `manual` candidates are skills where:
- collaboration style matters
- the work is heavily conversational
- the consumer team already has a Claude-specific ritual or prompt style

Examples in v0:
- `ux-strategy`
- `ux-provocation`
- `heuristic-audit`
- `ux-writing`
- `business-design`
- `triad-check`

### 4. Treat non-default skills as available, not blocked

If a skill is marked `available-not-default`, it is still usable with Claude.
It simply means the repository is not treating it as part of the current default Claude path.

## Practical setup model

A good Claude-oriented consumer setup usually looks like this:

- Adaptive Skills repo -> canonical skill definition
- consumer project docs -> local notes about when Claude should use or adapt those skills
- consumer project Claude setup -> only the small subset that truly benefits from a Claude-specific wrapper

Recommended local note shape:

```md
## Adaptive Skills used in this project

- `workflow` -> use by reference for bounded work slices.
- `feature-planning` -> use by reference before implementation.
- `premortem` -> use by reference for consequential plans; do not run by default.
- `ux-writing` -> local Claude wrapper allowed for recurring conversational copy reviews.
```

## Suggested local pattern

A consumer project can keep a short local note such as:

- use `workflow` by link/reference only
- adapt `ux-writing` manually for Claude if the team already reviews copy conversationally
- keep `testing` as `available-not-default` until there is a real Claude-native reason to wrap it
- keep `premortem` as reference-first unless consequential planning becomes a recurring Claude workflow

## When to choose manual adaptation

Use manual adaptation when:
- the team needs a Claude-specific prompt style
- the local workflow changes the reading order or output ritual
- the skill needs a smaller wrapper for a recurring conversational loop

Do not choose manual adaptation when:
- you are only chasing symmetry with Codex
- the canonical skill already works by reference
- the local project has not actually used the skill yet
- the skill is only needed occasionally and can be linked from the canon

## What not to do

- do not mirror the entire library into Claude on day one
- do not create Claude wrappers before selecting the skills by task need
- do not rewrite the canon just to fit a local Claude wrapper
- do not treat `available-not-default` as missing support
- do not collapse local Claude rituals into the generic library

## Relationship to AletheIA

If you use AletheIA, keep the same split:
- Adaptive Skills -> micro execution guidance
- AletheIA -> macro framing, gates, continuity, handoff

Claude-specific wrapping stays local to the consumer project unless it becomes broadly reusable.
