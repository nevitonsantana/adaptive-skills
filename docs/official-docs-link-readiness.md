---
title: "Official docs link readiness"
description: "Reference documentation for Official docs link readiness in Adaptive Skills."
---

## Status

AS-DOC-2 route and link readiness classification for the current Markdown-first documentation set.

This review does not introduce a documentation site, generated routing, GitHub Pages, Blume, or automatic publishing.

## Scope

Checked Markdown links across the repository and classified them into:

- local repository links that should resolve in GitHub-rendered Markdown;
- external source links that intentionally point to authoritative upstream records;
- future publication-route concerns that should be revisited only if a generated documentation shell is chosen.

## Findings

Initial scan covered 246 Markdown files. It found:

- 394 local Markdown links;
- 9 missing local links, all in legacy planning/reference files;
- 73 external links;
- 14 GitHub `blob` Markdown links that may open source Markdown rather than a rendered docs site.

The missing local links were repaired when an obvious current repository target existed:

| Previous target | Replacement | Reason |
|---|---|---|
| `./evolution/EVOLUTION_LAYER_V1.1.md` | `./evolution/README.md` | Current evolution entrypoint exists. |
| `./projections/SKILLS_REGISTRY.md` | `./projections/registry.json` | Projection registry is now JSON and canonical. |
| `./domain-packs/crisis-management/CASE_STUDY.md` | `./domain-packs/crisis-management/README.md` | Domain pack README is the current entrypoint. |
| local `../Downloads/.../aletheia-adaptive-skills-plano-cross-repo.md` | AletheIA backlog URL | Local machine path should not be a public docs dependency. |

Post-repair scan shows no missing local Markdown links.

## Source links versus public docs routes

GitHub `blob` Markdown links are kept as source links for now. They point to authoritative upstream records in AletheIA or Adaptive Skills and are acceptable while Adaptive Skills remains Markdown-first.

If AS-DOC-3 chooses a generated documentation shell, these source links should be revisited route by route. The decision should distinguish:

- links that should stay as source-code evidence;
- links that should become public docs routes;
- links that should be duplicated into local reference pages only when source ownership allows it.

## Current decision

Proceed with GitHub-rendered Markdown readiness only. Do not add a generated documentation shell or automatic publication workflow in this slice.
