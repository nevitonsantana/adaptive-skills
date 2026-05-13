# Adaptive Skills

A public, English-first library of micro-skills for agentic work.

**AletheIA is the macro layer.** It frames work, gates risk, supports handoffs, and preserves continuity.
**Adaptive Skills is the micro layer.** It helps an agent or team execute a specific capability with discipline, lightweight structure, and reusable heuristics.

## Core thesis

The library is built around **Core + Modules + Triggers**:

- **Core Moves** — the few moves that should almost always happen
- **Optional Modules** — add-ons that activate only when the context needs them
- **Activation Triggers** — simple signals that help choose the right modules without building a rigid mini-engine

This keeps skills structured without turning them into bureaucracy.

## Governed evolution layer

The library now also includes a repository-level evolution layer.
It treats skills as governed living assets:

- observations capture real usage signals
- proposals turn repeated evidence into reviewable change requests
- `reinforced` and `no-change` are valid outcomes
- the canon never self-rewrites in v1.1

See `docs/evolution-layer.md` and `evolution/README.md`.

A separate **Efficiency Layer** is now tracked as a future path for context, checkpoint, handoff, and chunking discipline. It is intentionally separate from the Evolution Layer so the current v1.1 baseline does not get reopened prematurely. See `docs/efficiency-layer.md`, `docs/efficiency-layer-roadmap.md`, and `docs/efficiency-layer-candidate-skills.md`.

## What is in v0

### Generic library

- `skills/engineering`
- `skills/design`
- `skills/business`
- `skills/quality`
- `skills/metrics`
- `skills/cross-functional`
- `skills/efficiency`

Skeleton-only domains in v0:

- `skills/product`
- `skills/governance`

### Domain packs

- `domain-packs/crisis-management`

Domain packs are intentionally specific. They are useful, versioned, and reusable, but they are **not** treated as generic skills.

## Repository layout

```txt
/docs           -> model, taxonomy, telemetry, AletheIA integration
/skills         -> generic skills by domain
/domain-packs   -> explicit domain-specific packs
/projections    -> projection registry for agent installs
/evolution      -> governed learning artifacts, observations, proposals, reviews
/scripts        -> validation and projection tooling
/templates      -> starter templates for new skills
```

## Use with or without AletheIA

The library is useful on its own.

Use it without AletheIA when you want:
- reusable execution discipline
- consistent outputs
- better specialist handoffs

Use it with AletheIA when you also want:
- macro framing
- review gates
- continuity between rounds
- structured learning and operational memory

See `docs/aletheia-integration.md` for the integration model and `docs/agent-role-integration.md` for the role-to-skill consumption layer.

A real field case is documented in `docs/crisis-monitor-case-study.md`.

## Current domains

- **Engineering** — implementation, contracts, testing, debugging, structural review
- **Design** — UX strategy, critique, provocation, UX writing
- **Business** — strategic framing and synthesis
- **Quality** — cross-layer quality review
- **Metrics** — observable, decision-linked signals
- **Cross-functional** — triad-style checks for multi-function decisions
- **Efficiency** — chunking, checkpoints, handoff discipline, and bounded execution patterns

## Projection model

The repository keeps the canon in the repo and treats agent installs as derived artifacts.

- `projections/registry.json` defines projection metadata
- Codex projection is first-class today
- Claude projection remains selective and availability-based in v0

## Quick start

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_evolution.py
python3 scripts/report_projection_status.py
python3 scripts/project_to_codex.py --all --dry-run
```

## 📊 Project Management

- **[Project Kanban](./PROJECT_KANBAN.md)**: Quadro Kanban com tarefas, prioridades e status dos pilotos
- **[Roadmap Evolutivo](./ROADMAP_EVOLUTIVO.md)**: Planejamento estratégico Q2-Q3 2026 com fases, OKRs e métricas
- **[Evolution Backlog](./EVOLUTION_BACKLOG.md)**: Backlog de evolution cycles (observations, proposals, reviews)

### Status Atual (Abril 2026)

| Dimensão | Status | Próxima Entrega |
|----------|--------|-----------------|
| Skills Validadas | 23/35 | Efficiency Layer v1.1 - 2026-04-25 |
| Pilotos Ativos | 5 | Resultados - 2026-04-20 |
| Evolution Cycle | #3 (Observations) | Cycle #4 - 2026-05-01 |
| Domínios | 8/10 | Product + Governance - Maio 2026 |

**📋 Veja o [Project Kanban](./PROJECT_KANBAN.md) para detalhes das tarefas atuais e prioridades.**

## Adopt in another project

Start with:
- `docs/consumer-adoption.md`
- `docs/codex-consumer-setup.md`
- `docs/claude-consumer-setup.md`
- `docs/first-consumer-pilot.md`
- `docs/aletheia-first-test.md`
- `examples/README.md`
- `docs/aletheia-integration.md`
- `docs/agent-role-integration.md`
- `docs/efficiency-layer-first-pilot.md`
- `docs/efficiency-layer-crisis-monitor-reference.md`
- `docs/efficiency-layer-trio-patterns.md`
- `docs/efficiency-layer-next-signals.md`

Recommended first bundle for a new consumer:
- `workflow`
- `feature-planning`
- `testing`

## License

Apache-2.0
