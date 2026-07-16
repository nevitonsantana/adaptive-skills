# Crisis Monitor references — inventory and reclassification

> **Purpose.** Track every reference to the first validation case (Crisis Monitor) across the Adaptive Skills repo, classify each by layer (canonical / example / meta / by-design), and record the action taken in Epic 2 of the 2026-05-21 cross-repo plan.
>
> **Date.** Created 2026-05-21.
>
> **Scope.** Markdown / JSON / YAML content in the repo. Excludes `evolution/observations/` and `evolution/proposals/deferred/` (which the reformulated Evolution Cycle #4 will reclassify between 2026-05-21 and 2026-06-30).
>
> **Related ADR.** [ADR-002 — Domain agnosticism](../adr/ADR-002-domain-agnosticism.md).
>
> **Prior work.** PR [#31](https://github.com/nevitonsantana/adaptive-skills/pull/31) (2026-05-18) already shifted Crisis Monitor from "active backlog" to "team-owned field evidence" in the README. This PR continues and completes that work across the canonical doc layer.

## Method

```
grep -rln -iE "crisis[- _]?monitor" --include="*.md" --include="*.json" \
  --include="*.yaml" --include="*.yml" .
```

Each match was classified as:

- **A — narrative dependency** (canonical doc tells the story *through* Crisis Monitor): refactor required.
- **B — cosmetic / framing**: add labeled "first validation case" + ADR link.
- **C — by design / already in example layer**: log only; no action.

## Type A — refactored in this PR

| File | Action |
|---|---|
| `docs/evolution-layer.md` | "Crisis Monitor + AletheIA case as seed evidence" generalized: introduced as "first validation case" with link, plus paragraph on Evolution Cycle #4 reclassification work. |
| `docs/efficiency-layer-trio-patterns.md` | Intro sentence about "after the Crisis Monitor field reference landed" reframed as "first-validation-case field reference" with link. |
| `docs/efficiency-layer-first-pilot.md` | "Reference case" section reframed as "first-validation reference case" with ADR-002 link. |
| `docs/consumer-adoption.md` | "Real consumer reference" section reframed as "first concrete small-lane pilot" with ADR-002 link. |

## Type B — cosmetic / framing in this PR

| File | Action |
|---|---|
| `README.md` (root) | "Field evidence" section expanded with ADR-002 link + explicit "first validation case" framing + reference to `domain-packs/crisis-management/` as first example pack. |
| `docs/README.md` (docs map) | "Field evidence" section expanded with ADR-002 link + "first validation case" framing. |
| `domain-packs/crisis-management/README.md` | Top-of-file callout added: "Example domain pack — not the canonical domain pack." Per plan §5 Epic 2 explicit requirement. Sections "How to use this pack" added with when-useful/when-not guidance. |

## Type C — by design or already in example layer (no action; logged)

| File | Layer | Why no action |
|---|---|---|
| `docs/crisis-monitor-case-study.md` | case study | Filename declares it. Case study layer. |
| `docs/efficiency-layer-crisis-monitor-reference.md` | reference | Filename declares it. Reference layer. |
| `docs/efficiency-layer-roadmap.md` | roadmap | Just lists Crisis Monitor reference doc paths, no narrative dependency. |
| `docs/aletheia-integration.md` | reference | Only lists CM docs as related references; not narrative-dependent. |
| `docs/adr/ADR-001-adaptive-skills-as-capability-library.md` | adr | Mentions CM as first validation case — designed for this. |
| `docs/adr/ADR-002-domain-agnosticism.md` | adr | Topic *is* the reclassification. |
| `docs/adr/ADR-003-relationship-with-aletheia.md` | adr | Mentions CM as context. |
| `evolution/observations/*` (multiple) | evolution | Historical observations; reclassification is the reformulated Evolution Cycle #4 (2026-05-21 → 2026-06-30) per [`ROADMAP_EVOLUTIVO.md`](https://github.com/nevitonsantana/adaptive-skills/blob/main/ROADMAP_EVOLUTIVO.md). |
| `evolution/proposals/deferred/*` | evolution | Same. |
| `evolution/reviews/*` | evolution | Same. |
| `evolution/README.md` | evolution | Layer overview; references are by design. |
| `domain-packs/crisis-management/skills/*` | domain pack | Domain-specific skills; reclassified as "example pack" via the new pack README header. |
| `examples/aletheia/crisis-monitor-two-round-pilot.md` | examples | Examples layer. |
| `examples/efficiency/crisis-monitor-efficiency-reference.md` | examples | Examples layer. |
| `examples/README.md`, `examples/efficiency/README.md` | examples | Examples layer indexes. |
| `.github/PROJECT_OPERATIONS.md`, `.github/GITHUB_PROJECT_OPERATIONS.md` | project mgmt | GitHub Project tooling docs; not adopter-facing. |
| `PROJECT_KANBAN.md`, `ROADMAP_EVOLUTIVO.md`, `CHANGELOG.md` | meta | Already reconciled in Onda 0 (2026-05-21, commit `fb586e7`). |

## Validation against acceptance criteria

The plan (§5, Epic 2) requires:

| Criterion | Status |
|---|---|
| No canonical doc has narrative dependency on Crisis Monitor | ✅ 4 Type-A files refactored; 3 Type-B files reframed. |
| Crisis Monitor appears exclusively in case study / examples / domain pack (now labeled) layers | ⚠️ Crisis Monitor name still appears in canonical docs *as labeled first-validation reference with link to case study and ADR*. This is intentional per ADR-002 and the user's gate decision: preserve transparency about the first case, not erase it. |
| `domain-packs/crisis-management/` has README explicitly stating it is example, not canonical | ✅ New top-of-file callout added with "Example domain pack — not the canonical domain pack." |
| Each repo has a README that explains "first validation case was Crisis Monitor; others are expected" | ✅ `README.md` root "Field evidence" section now states this with ADR-002 link. |

## Anti-criteria respected

- ❌ No Crisis Monitor content was deleted — only reframed/linked.
- ❌ No fictional second case was created to balance.
- ❌ `skills/`, `projections/`, `scripts/`, `templates/` were not touched.
- ❌ Evolution observations/proposals/reviews were not edited inline — that work is the reformulated Evolution Cycle #4 (2026-05-21 → 2026-06-30).

## Out-of-scope follow-ups

- Companion repo (AletheIA) carries the parallel inventory at `docs/_meta/crisis-monitor-references.md`. Its execution lives in PR [`docs/despoluicao-crisis-monitor`](https://github.com/nevitonsantana/AletheIA/tree/docs/despoluicao-crisis-monitor).
- Reclassification of `evolution/observations/` and `evolution/proposals/deferred/` is explicitly deferred to Evolution Cycle #4 (reformulated 2026-05-21).
- Skills inside `domain-packs/crisis-management/skills/` could later be evaluated for promotion to canonical `skills/` if they pass the ADR-002 reading test against another domain. Out of scope for this PR.

## Revision

Reopen this inventory when:
- A new Crisis Monitor reference is added in a non-example layer (regression).
- A second consumer project produces canonical evidence that should be cited alongside Crisis Monitor in the canonical layer (positive evolution toward observable agnosticism).
- A second domain pack is added — at that point, re-evaluate whether `domain-packs/crisis-management/` still needs the "first example" framing or has moved to "one of several examples".
