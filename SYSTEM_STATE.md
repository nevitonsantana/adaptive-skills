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

## Active and planned evolution

- **Active:** no repository-local implementation slice open; S15 is delivered.
- **Planned through AletheIA backlog:** intent-to-evidence support, capability routing reconciliation, Design System pilot and agent-role pilot.
- **Deferred:** automatic routing, self-editing skills, comparative rankings and broad telemetry until repeated evidence exists.

Backlog authority: [AletheIA integrated evolution backlog](https://github.com/nevitonsantana/AletheIA/blob/main/docs/roadmaps/evolution-backlog-aletheia-adaptive-skills.md).

## Deprecated or merged plans

- Detailed evolution packs remain reference sources; the AletheIA backlog is the cross-repository executive map.
- Capability graph metadata supplements skills; it does not replace the canonical skill catalog.
- Adaptive Skills remains usable without AletheIA and must not import AletheIA macro-governance into skill methods.

## Documentation health

- README and docs index: current for the present architecture boundary.
- CHANGELOG: current through the unreleased hardening baseline; S15 adds a documentation-only state entry.
- Projection and evolution validation: covered by repository scripts.
- First-use and language-depth coherence: not assessed by S15; planned for later P11 work.

## Cognitive debt and open risks

- **Current level:** medium — capability, evolution and projection concepts require guided explanation for new users.
- SYSTEM_STATE can become stale; source files and accepted evidence always win.
- No usage percentage, success rate or skill ranking is admissible without comparable reviewed records.
- Provider naming retains historical `adaptative-skills` paths in some local integrations; GitHub redirects preserve compatibility.

## Next safe steps

1. Support AletheIA S8 with portable intent-clarification methods only when requested.
2. Keep skill use source-backed through execution/observation return records.
3. Implement only dependency-valid backlog slices; do not create an automatic routing engine.
4. Reassess documentation health during the later explainable-language and first-use pilot.

## Last reviewed

- **Date:** 2026-06-23
- **Evidence baseline:** Adaptive Skills `baf4a4a`; AletheIA `ec9e9af`; integrated backlog through S15
- **Review trigger:** accepted skill-model, capability, evolution, projection, maturity or roadmap change
