# Adaptive Skills Docs

Use this page as the documentation map for Adaptive Skills.

The recommended public reader path is:

1. **Overview** — [`../README.md`](https://github.com/nevitonsantana/adaptive-skills/blob/main/README.md) and [`getting-started/overview.md`](getting-started/overview.md).
2. **Install / consume** — [`getting-started/installation-guide.md`](getting-started/installation-guide.md), [`guides/install-via-apm.md`](guides/install-via-apm.md), [`codex-consumer-setup.md`](codex-consumer-setup.md), and [`claude-consumer-setup.md`](claude-consumer-setup.md).
3. **Choose a skill** — [`getting-started/skill-catalog.md`](getting-started/skill-catalog.md), [`how-to-use-a-skill.md`](how-to-use-a-skill.md), and [`skill-categories.md`](skill-categories.md).
4. **Understand the model** — [`skill-model.md`](skill-model.md), [`domain-taxonomy.md`](domain-taxonomy.md), and [`skill-catalog-governance.md`](skill-catalog-governance.md).
5. **Use with AletheIA** — [`aletheia-integration.md`](aletheia-integration.md), [`agent-role-integration.md`](agent-role-integration.md), and [`specification-facilitation.md`](specification-facilitation.md).
6. **Advanced overlays** — [`capability-model.md`](capability-model.md), [`capability-graph.md`](capability-graph.md), [`operational-runtime.md`](operational-runtime.md), and [`evolution-layer.md`](evolution-layer.md).
7. **Evidence and decisions** — [`adr/README.md`](adr/README.md), [`_meta/`](https://github.com/nevitonsantana/adaptive-skills/blob/main/docs/_meta/), [`../examples/README.md`](https://github.com/nevitonsantana/adaptive-skills/blob/main/examples/README.md), and [`../evolution/README.md`](https://github.com/nevitonsantana/adaptive-skills/blob/main/evolution/README.md).

## Start here

- `../README.md` — project overview and value proposition
- [`official-docs-readiness.md`](official-docs-readiness.md) — publication-readiness map for turning the Markdown corpus into official docs
- [`official-docs-link-readiness.md`](official-docs-link-readiness.md) — route and link readiness classification for official docs
- [`official-docs-blume-shell.md`](official-docs-blume-shell.md) — decision record for the manual Blume documentation shell
- [`../SYSTEM_STATE.md`](https://github.com/nevitonsantana/adaptive-skills/blob/main/SYSTEM_STATE.md) — compact current-state index; source records and canonical files remain authoritative
- `skill-model.md` — Core + Modules + Triggers model
- `skill-design-principles/lean-skill-doctrine.md` — S20 doctrine for necessary, distinct, proportional, verifiable and governable skills
- `skill-catalog-governance.md` — catalog lifecycle, intake, merge/split/deprecation and quality-gate flow
- `how-to-use-a-skill.md` — practical guide for choosing and using a skill
- `domain-taxonomy.md` — generic skills vs. domain packs
- `capability-model.md` — skills, capabilities, workflows, runtime, harness, and governance boundaries
- `capability-graph.md` — experimental graph overlay for composition and routing
- `capability-routing-boundary.md` — S10 boundary note aligning capability fit with AletheIA routing governance

## Official documentation path

The current repository documentation is Markdown-first. The path above is the curated public-doc map for GitHub-rendered documentation. [`official-docs-readiness.md`](official-docs-readiness.md) records the remaining gated slices before adding a generated documentation site or publication workflow.

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
- [`../examples/context-surfaces/provider-loading.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/examples/context-surfaces/provider-loading.yaml) — capability-scoped provider-loading example for AletheIA's Context Surface Registry
- [`skill-observation-return-pattern.md`](skill-observation-return-pattern.md) — portable, recoverable skill return without Work Slice authority
- [`../examples/execution-records/feature-planning-observation-return.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/examples/execution-records/feature-planning-observation-return.yaml) — worked source-backed return

## Capability layer

The Capability Graph is an experimental metadata overlay. It makes routing, composition, execution modes, and evidence expectations explicit without moving existing skills or introducing a runtime engine.

- `capability-model.md` — terms and boundaries for skills, capabilities, workflows, runtime, harness, and governance
- `capability-routing-boundary.md` — what Adaptive Skills may declare versus what remains with AletheIA/harness governance
- `design-system-intelligence-pulso-pilot.md` — S24 Pulso pilot boundary for source-backed design-system review without scanners or promotion authority
- `capability-graph.md` — graph structure and advisory routing model
- `operational-runtime.md` — runtime contract, checkpointing, resumability, and approval boundaries
- `execution-modes.md` — basic, extended, high-risk, multi-agent, and debugging depth profiles
- `../capabilities/catalog.yaml` — pilot capability metadata
- `../capabilities/routes.yaml` — advisory route examples
- `../capabilities/profiles.yaml` — execution depth profiles
- `../capabilities/dependencies.yaml` — capability graph relationships

## Evolve the library

- `skill-catalog-governance.md` — quality gate and catalog lifecycle before canon changes
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
- [`../templates/skill-knowledge-dependency.yaml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/skill-knowledge-dependency.yaml) — template for the dependency file
- [`../templates/framework-capsule-template.md`](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/framework-capsule-template.md) — template for authoring a capsule
- [`../templates/knowledge-aware-skill-template.md`](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/knowledge-aware-skill-template.md) — skill template supporting generic and knowledge-aware modes
- [`../skills/knowledge-source-evaluation/`](https://github.com/nevitonsantana/adaptive-skills/blob/main/skills/knowledge-source-evaluation) — evaluate a candidate before registration
- [`../skills/knowledge-conflict-resolution/`](https://github.com/nevitonsantana/adaptive-skills/blob/main/skills/knowledge-conflict-resolution) — apply source precedence when sources disagree
- [`../skills/restricted-context-check/`](https://github.com/nevitonsantana/adaptive-skills/blob/main/skills/restricted-context-check) — leakage / injection / poisoning / permission / contamination checks

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
