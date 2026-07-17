# Changelog

## Unreleased

- reorganize skill discovery into a concise 33-skill catalog, a task-based selection guide, and reusable workflow recipes

- rewrite the beginner documentation journey with audience-based homepage paths, a concise overview, installation guidance, quickstart, first-skill exercise, usage guide, and current FAQ

- organize the Blume sidebar into progressive reader journeys and classify the complete documentation corpus by audience and publication role

- reconcile the public documentation with the 33-skill canon and add a validation gate for catalog and category coverage

- keep Blume rich-pattern guidance as an internal authoring reference instead of a public docs route

- fix duplicate rendered titles on Blume MDX documentation pages

- add a first Blume rich-content pattern guide and component-based documentation homepage

- add a Blume docs homepage so the published Pages root resolves

- allow the manual docs Pages workflow to initialize GitHub Pages when needed

- add manual GitHub Pages publication workflow and smoke-test plan for Adaptive Skills docs

- close AS-DOC-3 Blume docs shell state after PR #92 merge

- add a manual Blume documentation shell for Adaptive Skills official docs

- close AS-DOC-2 link readiness state after PR #90 merge

- classify official docs link readiness and repair legacy local documentation links

- close AS-DOC-1 public documentation map state after PR #88 merge

- align the root README and docs index on the official public documentation path

- close official docs readiness review state after PR #86 merge

- add official docs readiness review and link it from the docs index

- rename the maintainer-facing `.github/README.md` to `.github/PROJECT_OPERATIONS.md` so GitHub renders the root Adaptive Skills README on the repository homepage

- clarify that GitHub Project documentation is maintainer-facing operational support, not required setup for Adaptive Skills consumers

- repair stale documentation links in the ecosystem map and knowledge-source-evaluation workflow so local Markdown references resolve correctly

- add `intent-clarification` as the consultative Adaptive Skills counterpart for AletheIA S8 Intent-to-Evidence: human-owned outcome and expectations, explicit evidence holes and guessing risk, portable record template, worked example, advise-only harness declaration, and projection/evolution registration; the skill cannot approve, execute, or govern a Work Slice

- add a compact `SYSTEM_STATE.md` first-load index, context-surface entry and validator for S15 continuity governance; canonical skills, capabilities, evolution records and evidence remain authoritative

- sync indexes and root `README.md` after the Engineering Skills Hardening Pack: list the four hardening templates in `templates/README.md` and the four engineering examples in `examples/README.md`, add `domain-language-alignment` to the engineering roster in `docs/skill-categories.md`, and correct stale README facts (product/governance no longer skeleton-only, domains 10/10, validated-skills count, catalog pointer)
- add the **Engineering Skills Hardening Pack** (`debugging`, `testing`, `architecture-review` hardened with operational modules; new transversal skill `domain-language-alignment`): append-only modules preserving protected surfaces and existing verifications — `debugging` gains Feedback loop construction; `testing` gains Behavior-first test design and Vertical test slice; `architecture-review` gains Module depth review. Ships four worksheet templates, four synthetic examples, a pack doc, and a `mattpocock/skills` reference map (external inspiration only, no content copied). Registers `domain-language-alignment` in the projection and evolution registries (`manual-assisted`, pilot `hold`); `feature-planning` left unchanged (deferred candidate)
- add `templates/README.md` indexing the template inventory and documenting when to use each model; flags that `knowledge-aware-skill-template.md` is a content guide (its illustrative headings fail `validate_skills.py` if copied verbatim) and that the real `SKILL.md` must keep the 11 required sections
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
