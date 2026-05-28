# Changelog

## Unreleased

- add `feature-value-governance` as the first knowledge-aware consumer skill (`product` domain): judges whether a proposed feature is worth doing — business intent, revenue/operational lever, user evidence, opportunity-tree fit, complexity cost, and overreach risk — declaring knowledge slot types (not source ids) and running loudly in generic mode when no governed pack is available; consumes the AletheIA Knowledge Governance Layer (ADR-008) per the skill-side boundary (ADR-006)
- introduce the knowledge-aware skills boundary (docs-only): boundary doc, dependency-declaration guide, capsule + skill templates, and three governance skills (`knowledge-source-evaluation`, `knowledge-conflict-resolution`, `restricted-context-check`) implementing the skill-side surface of the AletheIA Knowledge Governance Layer (ADR-006)

## 0.1.2

- rename repository from `adaptative-skills` to `adaptive-skills` (modern English standard; GitHub redirect preserves old URLs)

## 0.1.1

- add a next-signals guide for when Efficiency Layer expansion should reopen
- add a short trio-patterns guide for combining the first Efficiency Layer skills
- add a Crisis Monitor-based reference case for the first Efficiency Layer trio
- add an Efficiency Layer pilot kit for validating the first trio in real work
- publish `checkpoint-review` as the third Efficiency Layer skill
- publish `handoff-summary` as the second Efficiency Layer skill
- publish `task-chunking` as the first Efficiency Layer skill
- document the first Efficiency Layer roadmap and the initial candidate skills
- clarify Evolution Layer v1.1 as the current baseline and separate Efficiency Layer as a future track
- add a governed evolution layer with repo-level registry, observations, proposals, and reviews
- add validation for evolution metadata and protected proposal surfaces
- document success-aware outcomes such as `reinforced` and `no-change`

## 0.1.0

- initial public scaffold for Adaptive Skills
- English-first skill model built on Core + Modules + Triggers
- generic skill domains plus crisis-management domain pack
- Codex-first projection registry and tooling
- validation, taxonomy, telemetry, and AletheIA integration docs
