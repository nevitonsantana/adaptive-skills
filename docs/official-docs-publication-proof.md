# Official docs publication proof

## Status

AS-DOC-4 manual publication proof plan for the Adaptive Skills Blume documentation site.

This slice adds a manual GitHub Pages publication workflow. It does not publish on every merge and does not introduce automatic deployment.

## Publication workflow

Manual workflow:

- `.github/workflows/docs-pages.yml`
- trigger: `workflow_dispatch`
- build source: `apps/docs`
- published artifact: `apps/docs/dist`

## Validation before publication

The workflow validates before upload:

```bash
pnpm install --frozen-lockfile
pnpm run docs:validate
pnpm run docs:build
```

## Smoke-test routes

After a manual run succeeds, smoke-test these representative routes:

| Route | Why it matters |
|---|---|
| `/adaptive-skills/` | public site root |
| `/adaptive-skills/README/` | generated docs index route |
| `/adaptive-skills/getting-started/overview/` | first-reader overview |
| `/adaptive-skills/getting-started/installation-guide/` | install path |
| `/adaptive-skills/official-docs-blume-shell/` | AS-DOC-3 decision record |
| `/adaptive-skills/official-docs-link-readiness/` | AS-DOC-2 link readiness record |
| `/adaptive-skills/adr/README/` | ADR grouping route |
| `/adaptive-skills/llms.txt` | agent-readable summary artifact |
| `/adaptive-skills/sitemap.xml` | discovery artifact |

## Boundaries

Publication remains manual-first. Automatic publishing on merge requires a separate explicit governance decision.

## Pending evidence

After this workflow is merged, run it manually and record:

- workflow run URL;
- deployment URL;
- HTTP status for representative routes;
- any route, title, or rendering issue found during smoke test.
