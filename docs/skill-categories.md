---
title: "Skill categories"
description: "Reference documentation for Skill categories in Adaptive Skills."
---

Adaptive Skills tags every published skill with a `metadata.category` value in the `SKILL.md` frontmatter. Categories are *attributes*, not directory structure — the on-disk layout is flat (`skills/<name>/SKILL.md`) to conform with the [`agentskills.io`](https://agentskills.io/specification) Skill Collection layout consumed by APM. See [ADR-005](https://nevitonsantana.github.io/adaptive-skills/adr/ADR-005-apm-packaging-strategy/) for the rationale behind the flatten.

This document is the canonical narrative for each category and tracks its backlog. The machine-readable mapping is in [`projections/registry.json`](https://github.com/nevitonsantana/adaptive-skills/blob/main/projections/registry.json) under each skill's `category` field.

Category growth is governed by [Skill Catalog Governance](https://nevitonsantana.github.io/adaptive-skills/skill-catalog-governance/): backlog entries are candidates, not authorization to create skills. New categories or category moves should pass the [Skill Quality Gate](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/skill-quality-gate.md) when they change skill boundaries.

## business

Business-domain skills for strategic framing, value logic, and operating-model thinking.

- **Published:** `business-design`, `revenue-lever-mapping`
- **Backlog:** `stakeholder-mapping`, `value-proposition`, `operating-model`

## cross-functional

Skills for decisions that cross product, design, engineering, or business boundaries.

- **Published:** `triad-check`
- **Backlog:** `alignment-brief`, `escalation-review`

## design

Design-domain skills for experience framing, UX critique, content clarity, and bounded design-system review. These are generic design skills, not UI implementation kits.

- **Published:** `ux-strategy`, `ux-provocation`, `heuristic-audit`, `ux-writing`, `design-system-intelligence`
- **Backlog:** `ux-research-synthesis`, `ux-ui-review`

## docs

Documentation skills for structuring, writing, publishing, and validating reader-facing technical content.

- **Published:** `documentation`
- **Backlog:** —

## efficiency

Skills that compound execution speed without sacrificing clarity — task chunking, handoff hygiene, mid-flight checkpoints.

- **Published:** `task-chunking`, `handoff-summary`, `checkpoint-review`
- **Backlog:** see [`docs/efficiency-layer-candidate-skills.md`](https://nevitonsantana.github.io/adaptive-skills/efficiency-layer-candidate-skills/)

## engineering

Reusable execution skills for engineering work. These skills should work across products without inheriting local operating rules.

- **Published:** `workflow`, `feature-planning`, `testing`, `debugging`, `api-design`, `refactoring`, `lean-implementation`, `architecture-review`, `code-style`, `communication`, `domain-language-alignment`
- **Backlog:** v0 already covers the core set; new entries flow through the Evolution Layer.

## governance

Skills for reviewing permanent cost, lifecycle decisions, and governed knowledge use without taking project-level decision authority.

- **Published:** `feature-complexity-audit`, `sunset-decision`, `knowledge-source-evaluation`, `knowledge-conflict-resolution`, `restricted-context-check`
- **Backlog:** `decision-log`, `handoff-governance`, `ai-safety-review`

## metrics

Metrics-domain skills for observable systems, decision-oriented telemetry, and operational signals.

- **Published:** `observability-review`
- **Backlog:** `metric-design`, `instrumentation-thinking`

## planning

Skills for structuring, stress-testing, and de-risking plans before execution begins.

- **Published:** `premortem`, `intent-clarification`
- **Backlog:** —

## product

Product-domain skills for deciding whether opportunities and feature investments are connected to user, business, and outcome evidence.

- **Published:** `feature-value-governance`, `opportunity-tree-alignment`
- **Backlog:** `product-discovery`, `roadmap-thinking`, `prioritization`, `hypothesis-design`

## quality

Quality-domain skills for readiness, consistency, and reliability review.

- **Published:** `qa-review`
- **Backlog:** `release-readiness`, `risk-assessment`
