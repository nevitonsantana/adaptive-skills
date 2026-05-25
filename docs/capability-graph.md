# Capability Graph

The Capability Graph describes how skills and modules relate during execution.

It is a hybrid model:

- a tree for human browsing;
- a graph for operational composition.

## Human discovery tree

```txt
Adaptive Skills
 ├── Engineering
 ├── Design
 ├── Business
 ├── Quality
 ├── Metrics
 ├── Cross-functional
 ├── Efficiency
 └── Planning
```

## Operational graph

```txt
workflow ──▶ feature-planning ──▶ testing
    │              │
    │              ├──▶ premortem
    │              └──▶ checkpoint-review
    └──▶ task-chunking ──▶ handoff-summary
```

The graph is not a mandatory chain. It is a map of likely composition paths.

## Routing principles

Routing should be explicit, small, and reviewable.

Use routing to answer:

1. What is the dominant need?
2. What is the smallest fitting capability?
3. Which modules are justified by the context?
4. What evidence should exist before closure?
5. Does the work need AletheIA-level governance?

## Example triggers

```txt
if ambiguity is medium_or_high
→ activate feature-planning with ambiguity-check

if context is getting heavy
→ activate checkpoint-review

if failure cost is meaningful and direction can still change
→ activate premortem

if next step crosses ownership boundary
→ activate handoff-summary or escalate to AletheIA
```

## Capability graph files

The first implementation uses a metadata overlay:

- `capabilities/catalog.yaml` — pilot capabilities and expected evidence.
- `capabilities/routes.yaml` — advisory route selection hints.
- `capabilities/profiles.yaml` — execution depth profiles.
- `capabilities/dependencies.yaml` — graph relationships and escalation boundaries.

These files do not replace `projections/registry.json` or `evolution/registry.json`.

## Stable versus experimental

Stable now:

- existing skill files;
- Core + Modules + Triggers;
- projection registry;
- Evolution Layer.

Experimental now:

- capability metadata;
- routing rules;
- execution profiles;
- execution records.

Not built now:

- runtime engine;
- graph database;
- autonomous self-rewrite;
- hidden policy engine.
