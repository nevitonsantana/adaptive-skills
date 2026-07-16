# Adaptive Skills SYSTEM_STATE

> Compact first-load index. This file is not a universal source of truth. Canonical skill files, capability declarations, evolution records, accepted decisions and validation evidence remain authoritative.

## Project identity

- **Project:** Adaptive Skills
- **Version:** `0.1.2` public baseline; unreleased evolution exists on `main`
- **Maturity:** operational portable library with experimental metadata overlays
- **Purpose:** reusable micro-skills and capability methods for disciplined AI-assisted work

## Current architecture summary

- `skills/` is the canonical portable method library.
- `capabilities/` is a metadata-first advisory overlay; it does not replace skills or execute routing.
- `evolution/` records observations, proposals and reviews without self-rewriting the canon.
- `projections/` derives runtime-specific installations from the repository canon.
- AletheIA may govern macro selection, gates and closure; Adaptive Skills does not acquire that authority.

Authoritative entrypoints:

- [`README.md`](README.md)
- [`docs/capability-model.md`](docs/capability-model.md)
- [`docs/evolution-layer.md`](docs/evolution-layer.md)
- [`docs/aletheia-integration.md`](docs/aletheia-integration.md)

## Delivered baseline

- Portable Core + Modules + Triggers skill model.
- Generic skills and explicit domain packs.
- Codex-first projection registry and validation scripts.
- Governed Evolution Layer with human-reviewed outcomes.
- Experimental capability graph and execution-pattern compatibility declarations.
- Recoverable skill observation return pattern.
- Consultative `intent-clarification` capability for AletheIA S8, with advise-only harness requirements.
- Lean Implementation Skill — delivered through Adaptive Skills PR #79 as a bounded engineering skill.
- Design System Intelligence Skill — delivered through Adaptive Skills PR #81 as a bounded Pulso pilot method.

## Active and planned evolution

- **Active:** AS-DOC-1 public documentation map curation.
- **Delivered:** official documentation readiness review recorded in `docs/official-docs-readiness.md`.
- **Planned through AletheIA backlog:** human expertise and evidence-based learning, coding-safety support and agent-role pilot.
- **Deferred:** automatic routing, self-editing skills, comparative rankings, broad telemetry and docs auto-publishing until repeated evidence exists.

Backlog authority: [AletheIA integrated evolution backlog](https://github.com/nevitonsantana/AletheIA/blob/main/docs/roadmaps/evolution-backlog-aletheia-adaptive-skills.md).

## Deprecated or merged plans

- Detailed evolution packs remain reference sources; the AletheIA backlog is the cross-repository executive map.
- Capability graph metadata supplements skills; it does not replace the canonical skill catalog.
- Adaptive Skills remains usable without AletheIA and must not import AletheIA macro-governance into skill methods.

## Documentation health

- README and docs index: current for the present architecture boundary; AS-DOC-1 is aligning the public reader path.
- CHANGELOG: current through the unreleased hardening baseline; S15 adds a documentation-only state entry.
- Projection and evolution validation: covered by repository scripts.
- First-use and language-depth coherence: delivered through the accepted S17 cross-repository pilot.

## Cognitive debt and open risks

- **Current level:** medium — capability, evolution, projection and catalog governance concepts require guided explanation for new users.
- SYSTEM_STATE can become stale; source files and accepted evidence always win.
- No usage percentage, success rate or skill ranking is admissible without comparable reviewed records.
- Provider naming retains historical `adaptative-skills` paths in some local integrations; GitHub redirects preserve compatibility.

## Next safe steps

1. Keep `lean-implementation` bounded: it does not replace debugging, testing, refactoring, architecture review or governance.
2. Keep skill use source-backed through execution/observation return records.
3. Coordinate the next ordered slice from the AletheIA backlog before adding new skills.
4. Do not create an automatic routing engine, global provider selector or skill self-edit loop.

## Last reviewed

- **Date:** 2026-07-16
- **Evidence baseline:** Adaptive Skills `c516815` after official docs readiness closure merge; AletheIA `f3d0a69` after S82 publication-evidence closure
- **Review trigger:** AS-DOC-1 public documentation map curation
