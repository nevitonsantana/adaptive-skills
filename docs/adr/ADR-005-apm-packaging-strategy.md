---
title: "ADR 005 — Adaptive Skills: APM packaging strategy"
description: "Reference documentation for ADR 005 — Adaptive Skills: APM packaging strategy in Adaptive Skills."
---

| Field | Value |
|---|---|
| Status | Accepted |
| Date | 2026-05-25 |
| Author | Neviton Santana |
| Deciders | Neviton Santana |
| Related | ADR-001 (Adaptive Skills as capability library), ADR-002 (Domain agnosticism), ADR-004 (`agentskills.io` conformance), AletheIA ADR-007 (AletheIA APM packaging strategy) |
| Supersedes | — |

## 1. Context

Épico 5 of the 2026-05-21 cross-repo plan requires packaging Adaptive Skills as an APM package installable via `apm install nevitonsantana/adaptive-skills`, with optional per-skill install via `--skill <name>` (plan §5 Frente 4). ADR-004 settled `agentskills.io` conformance strategy (Case A — high conformance with mechanical remediation: move `version`/`owner` into `metadata` block). AletheIA ADR-007 documented its own APM packaging path (`type: hybrid`, two-step `apm install` + `apm run scaffold-overlay`) and explicitly noted that Adaptive Skills "will face a different mismatch (its primitives map more cleanly to APM `skill` type) and likely use a different layout."

Investigating the current APM specification (`microsoft.github.io/apm/`, fetched 2026-05-25) confirmed four package layouts:

- **APM Package** (`.apm/` directory) — typed subdirectories; no `--skill` partial install.
- **Skill Bundle** (`SKILL.md` at root) — one skill per package.
- **Skill Collection** (`skills/<name>/SKILL.md`) — multiple skills; **supports `--skill <name>` per-skill install**; aligns with `agentskills.io` directory convention.
- **Plugin Collection** (`plugin.json`) — Claude-native plugin manifest.

The `apm.yml` `type:` enum is `instructions | skill | hybrid | prompts`. `version:` matches `^\d+\.\d+\.\d+`. `includes:` is the allow-list controlling package payload.

Three structural questions had to be answered before authoring `apm.yml`:

1. **Layout**: the repo organized skills nested as `skills/<category>/<skill-name>/SKILL.md`, two levels under `skills/`. APM Skill Collection promotes "each `skills/<name>/` directory" — direct children of `skills/`. The nested layout would be ambiguous to the layout detector (`cross-functional`, `design`, `engineering`, ... could be read as skill names with broken inner structure).
2. **Versioning**: the cross-repo plan sketched alignment with the library roadmap (`v1.1`, `v2.0`), but a fresh first APM release wants alpha signalling. AletheIA used `0.1.0-alpha`. APM's `version:` regex (`^\d+\.\d+\.\d+`) does not document prerelease-suffix tolerance.
3. **Domain packs (`crisis-management/`)**: Épico 2 explicitly demoted Crisis Monitor from canonical to "first validation case among many expected." Bundling `domain-packs/` into the main APM payload would silently re-canonicalize it.

## 2. Decision

**Adaptive Skills ships as a single APM Skill Collection** (`type: skill`, `target: claude`) with three accompanying structural decisions:

### 2.1 Flatten skills layout (decision A1)

`skills/<category>/<skill-name>/SKILL.md` is rewritten to `skills/<skill-name>/SKILL.md`. The category is preserved as a string attribute in the skill's frontmatter `metadata.category` field (already a string→string map by the agentskills.io spec). The on-disk taxonomy is replaced by a metadata-driven taxonomy.

The category narrative and per-category backlog (previously held in `skills/<category>/README.md`) are consolidated into [`docs/skill-categories.md`](https://nevitonsantana.github.io/adaptive-skills/skill-categories/), which is the canonical narrative source from this ADR forward. The machine-readable mapping continues to live in [`projections/registry.json`](https://github.com/nevitonsantana/adaptive-skills/blob/main/projections/registry.json) under each skill's `category` field.

### 2.2 Version `0.1.0` (decision C1)

`apm.yml` declares `version: 0.1.0` — the minimal three-part semver that APM's regex unambiguously accepts. The alpha signal is carried by the git tag (`v0.1.0-alpha-apm`) and the manifest `description`, not by the manifest version string. This matches AletheIA's effective release stance while staying inside the documented APM constraint.

### 2.3 Exclude `domain-packs/` from APM payload (decision D3)

`domain-packs/` is omitted from `includes:` and therefore does not ship with `apm install nevitonsantana/adaptive-skills`. Domain packs remain consumable via `git clone` for adopters who explicitly want them. This preserves the Épico 2 positioning of `crisis-management/` as a case study, not canonical surface. If soft-launch (Épico 8) reveals demand for domain-pack distribution, a separate APM package (`nevitonsantana/adaptive-skills-crisis-pack`) becomes the natural answer — a decision deferred to a future ADR.

### 2.4 What the manifest looks like

```yaml
name: adaptive-skills
version: 0.1.0
type: skill
target: claude
includes:
  - apm.yml
  - skills/**
  - docs/skill-categories.md
  - docs/guides/install-via-apm.md
  - docs/adr/ADR-004-agentskills-io-conformance.md
  - docs/adr/ADR-005-apm-packaging-strategy.md
  - LICENSE
  - README.md
```

Full file: [`apm.yml`](https://github.com/nevitonsantana/adaptive-skills/blob/main/apm.yml). Adopter-facing companion: [`docs/guides/install-via-apm.md`](https://nevitonsantana.github.io/adaptive-skills/guides/install-via-apm/).

## 3. Consequences

**Positive.**

- `apm install nevitonsantana/adaptive-skills` and `apm install nevitonsantana/adaptive-skills --skill <name>` both work natively because the layout is exactly what APM's Skill Collection expects. No projection layer, no two-step adoption flow (AletheIA needed one for scaffold-at-root delivery; Adaptive Skills does not, because skills are first-class APM primitives).
- ADR-004 Case A remediation lands in the same PR as the flatten, satisfying the lockstep requirement explicitly stated in ADR-004 §2.3 and §3. Library-internal validator (`scripts/validate_skills.py`) and spec-conformance validator (`skills-ref validate`) both pass against all 21 skills post-remediation, and `skills-ref validate` is added to the Quality Gate CI workflow per ADR-004 §2.4.
- Category taxonomy survives the flatten without quality loss: machine-readable mapping in `projections/registry.json`, human-readable narrative in `docs/skill-categories.md`, and per-skill self-description in `metadata.category`. Discovery tooling (e.g., a future Skill Finder) reads the same source of truth no matter the question.
- Domain packs are not silently promoted to canonical, honoring Épico 2's anti-criterion.

**Negative.**

- The category dimension loses visual presence on disk. Anyone scanning `skills/` no longer sees `engineering/`, `design/`, etc. as grouping containers. Mitigation: `docs/skill-categories.md` is linked from the README and the install guide; `projections/registry.json` exposes the same data structurally.
- Any external code, docs, or harness configuration referencing the old nested paths (`skills/<category>/<name>/SKILL.md`) breaks at the path level. The repo's own internal references were swept in the same PR; external breakage is unknown and bounded by the fact that v0.1.0 is the library's first APM release with no prior distribution.
- The `--skill <name>` mechanism is fully dependent on APM's documented Skill Collection behavior. If APM changes the partial-install semantics, the install guide is wrong until updated. Bounded risk: the spec is stable enough to depend on for v0.1.0.

**Accepted tradeoffs.**

- Flatten over dual-layout-with-projection: rejected projecting the library into a flat shape under `dist/skills/` because it would reintroduce the translation layer that ADR-004 Case A explicitly rejected. Choosing A1 means the repo and the APM payload are the same shape, end to end.
- `0.1.0` over `0.1.0-alpha`: rejected the suffix because the documented APM regex does not include prerelease tolerance. Carrying the alpha signal in the git tag is observable enough; encoding it in the manifest would risk install-time validation failure for cosmetic gain.
- Exclude over include for `domain-packs/`: rejected including them as a default because doing so contradicts Épico 2. Future demand can promote them via a separate package without affecting the main library's adopter surface.

## 4. Alternatives considered

- **A2 — keep nested layout** (`skills/<category>/<name>/SKILL.md` plus `type: skill`). Rejected: APM Skill Collection's `skills/<name>/` semantics are ambiguous on nested structure; the most likely behavior is that category directories are interpreted as broken skill folders. The risk of silent install failure for adopters outweighs the cosmetic benefit of keeping categories as folders.
- **A3 — `.apm/` package layout.** Rejected: it would shift all skills under `.apm/skills/` to use the APM Package type, **losing the `--skill <name>` partial install** which is an explicit Épico 5 requirement.
- **A4 — dual layout** (source nested, built flat). Rejected because it reintroduces a projection layer that ADR-004 Case A removed. Adds maintenance and CI complexity for no install-side benefit.
- **C2 — `version: 0.1.0-alpha`.** Rejected because the APM manifest schema documents `version:` as matching `^\d+\.\d+\.\d+`; prerelease suffix support is undocumented and risky for the first release.
- **C3 — `version: 1.0.0`.** Rejected because the library is materially in soft-launch territory and adopters should know they are picking up the first packaged release. Inflating the version misrepresents maturity.
- **D1 — separate `adaptive-skills-crisis-pack` APM package.** Not rejected, but **deferred**. Promotes domain-packs to peer distribution status without forcing it on adopters who only want generic skills. Will be reopened if soft-launch demand justifies a second package.
- **D2 — include `domain-packs/` in the main payload.** Rejected: re-canonicalizes Crisis Monitor against Épico 2.
- **D4 — subdirectory `skills/crisis-management/`.** Rejected: violates the `domain-packs/` boundary the Épico 2 work spent capital reinforcing.

## 5. Relationship

- **ADR-001** declared Adaptive Skills' posture as a capability library. This ADR specifies the *distribution* layer that makes that posture installable.
- **ADR-002** declared domain agnosticism. The D3 decision (exclude domain-packs from the main APM package) operationalizes that ADR at the distribution surface.
- **ADR-004** declared `agentskills.io` Case A as the conformance strategy and explicitly designated Épico 5 (this work) as the place where remediation lands. Section 2.1 above completes the remediation lockstep: 21 SKILL.md updated, `scripts/validate_skills.py` updated, `skills-ref validate` added to CI.
- **AletheIA ADR-007** addressed the sibling problem for AletheIA. The contrast is informative: AletheIA needed `type: hybrid` and a two-step adoption flow because it is a project scaffold; Adaptive Skills uses `type: skill` and one-step adoption because its primitives are exactly what APM Skill Collection delivers. The two ADRs together document that *AletheIA + Adaptive Skills* spans both ends of APM's compatibility spectrum.
- **`docs/guides/install-via-apm.md`** is the adopter-facing companion to this ADR.
- **2026-05-21 cross-repo plan §7** (success metrics). This ADR contributes to the "Adoptabilidade técnica" signal — time-to-install for a context-free adopter should be one `apm install` away after this ADR's PR merges.

## 6. Review

Reopen this decision when any of the following occurs:

- The `agentskills.io` spec adds, removes, or modifies required frontmatter fields, or changes Skill Collection layout semantics. Re-audit against the new spec; reaffirm or amend.
- The APM specification publishes new package types, lifecycle hooks, or partial-install mechanisms that change which layout is optimal. Most likely scenario: a `scaffold` or `template` type emerges and AletheIA migrates; that does not affect this ADR but may co-evolve in a future revision.
- Soft launch (Épico 8) reveals adopter demand for distributing `domain-packs/crisis-management/` via APM. Open a successor ADR for D1 (separate package).
- `--skill <name>` partial install ceases to work as documented. Re-investigate APM behavior; layout choice may need to change.
- An external consumer of the old nested path layout surfaces and reports breakage. Decide whether to publish a one-time migration shim or document the path change as a v0.1.0 expectation.

If review confirms the decision unchanged, record the confirmation date here and continue.
