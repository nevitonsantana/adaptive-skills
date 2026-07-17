# Official docs readiness

## Status

Readiness review for turning the existing Markdown documentation into an official, publishable documentation surface.

This document does not introduce a static-site generator, publishing workflow, routing engine, or automatic documentation mutation.

## Current posture

Adaptive Skills already has enough source material for an official documentation surface:

- root README explains the product and repository boundary;
- `docs/README.md` provides a reader map;
- getting-started pages cover overview, installation, catalog, and FAQ;
- ADRs record architectural decisions;
- capability, evolution, harness, knowledge, and AletheIA integration docs are present;
- validation scripts cover skills, capabilities, harness requirements, knowledge dependencies, evolution records, and system state.

The main gap is not content volume. The gap is publication structure: the repository does not yet define a curated public-doc route map, generated-site tooling, or manual publication evidence equivalent to the current AletheIA Blume flow.

## Recommended public reader path

Use this order for a first official docs experience:

1. **Overview** — `README.md` and `docs/getting-started/overview.md`.
2. **Install / consume** — `docs/getting-started/installation-guide.md`, `docs/guides/install-via-apm.md`, `docs/codex-consumer-setup.md`, and `docs/claude-consumer-setup.md`.
3. **Choose a skill** — `docs/getting-started/skill-catalog.md`, `docs/how-to-use-a-skill.md`, and `docs/skill-categories.md`.
4. **Understand the model** — `docs/skill-model.md`, `docs/domain-taxonomy.md`, and `docs/skill-catalog-governance.md`.
5. **Use with AletheIA** — `docs/aletheia-integration.md`, `docs/agent-role-integration.md`, and `docs/specification-facilitation.md`.
6. **Advanced overlays** — `docs/capability-model.md`, `docs/capability-graph.md`, `docs/operational-runtime.md`, and `docs/evolution-layer.md`.
7. **Evidence and decisions** — `docs/adr/README.md`, `_meta` reports, examples, and evolution records.

## Candidate publication slices

| Slice | Goal | Acceptance | Non-goals |
|---|---|---|---|
| AS-DOC-1 | Curate the official docs map | `docs/README.md` and root README agree on the public reader path | Static site, publishing automation |
| AS-DOC-2 | Check route/link readiness | Delivered in [`official-docs-link-readiness.md`](official-docs-link-readiness/): local broken links repaired, source links classified | Bulk rewrite |
| AS-DOC-3 | Choose publication shell | Delivered in [`official-docs-blume-shell.md`](official-docs-blume-shell/): Blume selected and validated locally | Deploy before validation |
| AS-DOC-4 | Manual publication proof | Manual Pages workflow and smoke-test plan recorded in [`official-docs-publication-proof.md`](official-docs-publication-proof/) | Automatic publishing on merge |

## Boundaries

Official documentation should not collapse Adaptive Skills into AletheIA.

Adaptive Skills owns reusable micro-skills, capability metadata, projections, and governed evolution of the skill canon. AletheIA may consume and govern those capabilities at the macro Work Slice level, but Adaptive Skills documentation should remain usable for teams that do not use AletheIA.

## Validation checklist

Before publishing an official docs site, run at least:

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_capabilities.py
python3 scripts/validate_harness_requirements.py
python3 scripts/validate_knowledge_deps.py
python3 scripts/validate_evolution.py
python3 scripts/validate_system_state.py
```

If publication tooling is introduced later, add a separate build/audit command and keep manual publication evidence until automatic publishing has an explicit governance decision.

## Current decision

Proceed with documentation readiness first. Do not introduce Blume, GitHub Pages, or another static-site tool in this slice.
