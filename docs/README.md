# Adaptive Skills Docs

Use this page as the documentation map for Adaptive Skills.

The recommended path is:

1. understand the model;
2. choose the right skill;
3. set up only the skills you need;
4. run a small pilot;
5. capture evidence before changing the canon.

## Start here

- `../README.md` — project overview and value proposition
- `skill-model.md` — Core + Modules + Triggers model
- `how-to-use-a-skill.md` — practical guide for choosing and using a skill
- `domain-taxonomy.md` — generic skills vs. domain packs
- `capability-model.md` — skills, capabilities, workflows, runtime, harness, and governance boundaries
- `capability-graph.md` — experimental graph overlay for composition and routing

## Adopt in another project

Follow this sequence:

1. `consumer-adoption.md` — adoption principles and recommended order
2. `how-to-use-a-skill.md` — selection and usage loop
3. `codex-consumer-setup.md` — Codex projection after skill selection
4. `claude-consumer-setup.md` — Claude reference-first setup
5. `first-consumer-pilot.md` — bounded first pilot
6. `pilot-evaluation-checklist.md` — evaluate whether to expand, adjust, or stop
7. `../templates/pilot/consumer-pilot-report.md` — capture pilot evidence

## Work with AletheIA

- `aletheia-integration.md` — macro/micro integration model
- `agent-role-integration.md` — role-to-skill consumption without collapsing roles and skills
- `specification-facilitation.md` — compose `workflow + feature-planning + premortem` for clarify/spec/plan/tasks/readiness support
- `aletheia-first-test.md` — first test structure
- [AletheIA + Adaptive Skills integrated evolution backlog](https://github.com/nevitonsantana/AletheIA/blob/main/docs/roadmaps/evolution-backlog-aletheia-adaptive-skills.md) — canonical P0–P11 dependency graph, source registry, and requirement traceability
- [AletheIA + Adaptive Skills ecosystem territory map](https://github.com/nevitonsantana/AletheIA/blob/main/docs/concepts/ecosystem-territory-map.md) — non-normative north-star view; current contracts and records remain authoritative
- [`../examples/context-surfaces/provider-loading.yaml`](../examples/context-surfaces/provider-loading.yaml) — capability-scoped provider-loading example for AletheIA's Context Surface Registry
- [`skill-observation-return-pattern.md`](skill-observation-return-pattern.md) — portable, recoverable skill return without Work Slice authority
- [`../examples/execution-records/feature-planning-observation-return.yaml`](../examples/execution-records/feature-planning-observation-return.yaml) — worked source-backed return

## Capability layer

The Capability Graph is an experimental metadata overlay. It makes routing, composition, execution modes, and evidence expectations explicit without moving existing skills or introducing a runtime engine.

- `capability-model.md` — terms and boundaries for skills, capabilities, workflows, runtime, harness, and governance
- `capability-graph.md` — graph structure and advisory routing model
- `operational-runtime.md` — runtime contract, checkpointing, resumability, and approval boundaries
- `execution-modes.md` — basic, extended, high-risk, multi-agent, and debugging depth profiles
- `../capabilities/catalog.yaml` — pilot capability metadata
- `../capabilities/routes.yaml` — advisory route examples
- `../capabilities/profiles.yaml` — execution depth profiles
- `../capabilities/dependencies.yaml` — capability graph relationships

## Evolve the library

- `evolution-layer.md` — governed evolution model
- `../evolution/README.md` — observations, proposals, and reviews
- `telemetry.md` — signal model for usage and improvement

## Efficiency track

The Efficiency Layer is a separate track for context, checkpoint, handoff, and chunking discipline.

- `efficiency-layer.md`
- `efficiency-layer-roadmap.md`
- `efficiency-layer-first-pilot.md`
- `efficiency-layer-pilot-checklist.md`
- `efficiency-layer-trio-patterns.md`
- `efficiency-layer-next-signals.md`

## Knowledge governance (skill side)

How skills consume governed knowledge bases (frameworks, policies, personas) without carrying their content.

- [`skill-knowledge-boundaries.md`](skill-knowledge-boundaries.md) — skill carries procedure; knowledge pack carries content
- [`declaring-knowledge-dependencies.md`](declaring-knowledge-dependencies.md) — slot-based declaration of required, optional, and conditional knowledge
- [`using-proprietary-frameworks-safely.md`](using-proprietary-frameworks-safely.md) — capsule + manifest + dependency declaration
- [`../templates/skill-knowledge-dependency.yaml`](../templates/skill-knowledge-dependency.yaml) — template for the dependency file
- [`../templates/framework-capsule-template.md`](../templates/framework-capsule-template.md) — template for authoring a capsule
- [`../templates/knowledge-aware-skill-template.md`](../templates/knowledge-aware-skill-template.md) — skill template supporting generic and knowledge-aware modes
- [`../skills/knowledge-source-evaluation/`](../skills/knowledge-source-evaluation) — evaluate a candidate before registration
- [`../skills/knowledge-conflict-resolution/`](../skills/knowledge-conflict-resolution) — apply source precedence when sources disagree
- [`../skills/restricted-context-check/`](../skills/restricted-context-check) — leakage / injection / poisoning / permission / contamination checks

The AletheIA-side contracts these depend on:

- knowledge-governance-layer (AletheIA `docs/concepts/`)
- knowledge-pack-manifest (AletheIA `docs/contracts/`)
- skill-knowledge-dependency-contract (AletheIA `docs/contracts/`)
- source-precedence-policy (AletheIA `docs/contracts/`)
- restricted-knowledge-usage-policy (AletheIA `docs/contracts/`)
- knowledge-audit-log-spec (AletheIA `docs/contracts/`)

## Field evidence

Adaptive Skills is domain-agnostic (see [`adr/ADR-002-domain-agnosticism.md`](adr/ADR-002-domain-agnosticism.md)). The first validation case is Crisis Monitor — labeled evidence, not canonical reference:

- [`crisis-monitor-case-study.md`](crisis-monitor-case-study.md) — first-validation field case
- [`efficiency-layer-crisis-monitor-reference.md`](efficiency-layer-crisis-monitor-reference.md) — first-validation field reference for the Efficiency Layer

Field evidence is not active product backlog inside this repository.
