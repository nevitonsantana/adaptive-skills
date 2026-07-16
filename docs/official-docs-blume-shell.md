# Official docs Blume shell

## Status

AS-DOC-3 decision and implementation record for using Blume as the Adaptive Skills official documentation shell.

This slice introduces a local/manual Blume build. It does not publish GitHub Pages, add automatic deployment, or change skill behavior, projections, routing, runtime, or governance.

## Decision

Use Blume for Adaptive Skills official documentation, matching the direction already proven in AletheIA.

The initial shell reads from `docs/` only. Repository assets outside `docs/` remain source links unless they are intentionally promoted into the public documentation corpus later.

## Why Blume

Blume is a good fit because it turns the existing Markdown corpus into a navigable documentation site while preserving the repository-first writing workflow.

It also provides useful generated artifacts for AI-assisted usage:

- static pages;
- search index;
- sitemap and robots files;
- `llms.txt` and `llms-full.txt`;
- `agent-readability.json`.

## Local commands

```bash
pnpm install
pnpm run docs:validate
pnpm run docs:build
```

## Validation evidence

Validated locally on 2026-07-16:

- `pnpm run docs:validate` — passed with no broken Blume links;
- `pnpm run docs:build` — built 67 pages;
- `python3 scripts/validate_system_state.py` — passed;
- `python3 scripts/validate_skills.py` — passed;
- `python3 scripts/validate_capabilities.py` — passed;
- `python3 scripts/validate_harness_requirements.py` — passed;
- `python3 scripts/validate_knowledge_deps.py` — passed;
- `python3 scripts/validate_evolution.py` — passed.

## Boundaries

This shell is manual-first. Publication remains gated.

The next safe slice is AS-DOC-4: add or run a manual GitHub Pages publication workflow and capture smoke-test evidence for representative routes.
