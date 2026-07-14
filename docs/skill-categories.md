# Skill categories

Adaptive Skills tags every published skill with a `metadata.category` value in the `SKILL.md` frontmatter. Categories are *attributes*, not directory structure — the on-disk layout is flat (`skills/<name>/SKILL.md`) to conform with the [`agentskills.io`](https://agentskills.io/specification) Skill Collection layout consumed by APM. See [ADR-005](adr/ADR-005-apm-packaging-strategy.md) for the rationale behind the flatten.

This document is the canonical narrative for each category and tracks its backlog. The machine-readable mapping is in [`projections/registry.json`](../projections/registry.json) under each skill's `category` field.

Category growth is governed by [Skill Catalog Governance](skill-catalog-governance.md): backlog entries are candidates, not authorization to create skills. New categories or category moves should pass the [Skill Quality Gate](../templates/skill-quality-gate.md) when they change skill boundaries.

## business

Business-domain skills for strategic framing, value logic, and operating-model thinking.

- **Published:** `business-design`
- **Backlog:** `stakeholder-mapping`, `value-proposition`, `operating-model`

## cross-functional

Skills for decisions that cross product, design, engineering, or business boundaries.

- **Published:** `triad-check`
- **Backlog:** `alignment-brief`, `escalation-review`

## design

Design-domain skills for experience framing, UX critique, content clarity, and bounded design-system review. These are generic design skills, not UI implementation kits.

- **Published:** `ux-strategy`, `ux-provocation`, `heuristic-audit`, `ux-writing`, `design-system-intelligence`
- **Backlog:** `ux-research-synthesis`, `ux-ui-review`

## efficiency

Skills that compound execution speed without sacrificing clarity — task chunking, handoff hygiene, mid-flight checkpoints.

- **Published:** `task-chunking`, `handoff-summary`, `checkpoint-review`
- **Backlog:** see [`docs/efficiency-layer-candidate-skills.md`](efficiency-layer-candidate-skills.md)

## engineering

Reusable execution skills for engineering work. These skills should work across products without inheriting local operating rules.

- **Published:** `workflow`, `feature-planning`, `testing`, `debugging`, `api-design`, `refactoring`, `lean-implementation`, `architecture-review`, `code-style`, `communication`, `domain-language-alignment`
- **Backlog:** v0 already covers the core set; new entries flow through the Evolution Layer.

## governance

Governance-domain placeholder. No published generic skills yet.

- **Published:** —
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

Product-domain placeholder. No published generic skills yet.

- **Published:** —
- **Backlog:** `product-discovery`, `roadmap-thinking`, `prioritization`, `hypothesis-design`

## quality

Quality-domain skills for readiness, consistency, and reliability review.

- **Published:** `qa-review`
- **Backlog:** `release-readiness`, `risk-assessment`
