---
title: "`agentskills.io` conformance audit"
description: "Reference documentation for `agentskills.io` conformance audit in Adaptive Skills."
---

> **Purpose.** Gap analysis between the Adaptive Skills repo and the open [Agent Skills specification](https://agentskills.io/specification), produced under Epic 3 of the 2026-05-21 cross-repo plan. Decision strategy (Case A / B / C) is recorded separately in [ADR-004](https://nevitonsantana.github.io/adaptive-skills/adr/ADR-004-agentskills-io-conformance/).
>
> **Date.** Created 2026-05-21.
>
> **Audit scope.** All 21 `SKILL.md` files under `skills/`. Domain-pack skills (`domain-packs/crisis-management/skills/`) are out of scope here; they will be audited separately if/when promotion to canonical `skills/` is considered.
>
> **Anti-criterion respected.** This audit does not execute remediation. It identifies divergences, recommends an approach per divergence, and proposes an overall strategy. Implementation belongs to a separate epic.

## 1. Spec snapshot (as of 2026-05-21)

Source: [agentskills.io/specification](https://agentskills.io/specification).

### 1.1 Directory structure (skill scope)

A skill is a directory containing, at minimum, a `SKILL.md` file:

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional
├── references/       # Optional
├── assets/           # Optional
└── ...               # Any additional files
```

The spec defines the **skill folder**. It does not legislate how a library organizes many skills — repo-level organization (e.g., grouping by domain) is outside the spec's scope.

### 1.2 `SKILL.md` frontmatter — fields

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | 1-64 chars; lowercase alphanumeric + hyphens; no leading/trailing/consecutive hyphens; **must match parent directory name** |
| `description` | Yes | 1-1024 chars; non-empty; describes what + when |
| `license` | No | Free-form |
| `compatibility` | No | Max 500 chars; environment requirements |
| `metadata` | No | Arbitrary string→string map for additional properties not in spec |
| `allowed-tools` | No | Space-separated tool list (experimental) |

### 1.3 Body content

The Markdown body after the frontmatter is **unrestricted**. The spec recommends step-by-step instructions, examples of inputs/outputs, common edge cases. Recommended size: `SKILL.md` under 500 lines; detailed reference material split into `references/`.

### 1.4 Progressive disclosure

Spec assumes 3-stage loading:
1. Discovery: name + description (~100 tokens) loaded for all skills at startup.
2. Activation: full `SKILL.md` body loaded when relevant (<5000 tokens recommended).
3. Resources: `scripts/`, `references/`, `assets/` loaded on demand.

### 1.5 Validation

Spec ships a reference validator at [`skills-ref`](https://github.com/agentskills/agentskills/tree/main/skills-ref):

```bash
skills-ref validate ./my-skill
```

## 2. Current state of Adaptive Skills

### 2.1 Inventory (21 skills, all under `skills/<domain>/<skill-name>/`)

| Domain | Skill |
|---|---|
| business | business-design |
| cross-functional | triad-check |
| design | heuristic-audit, ux-provocation, ux-strategy, ux-writing |
| efficiency | checkpoint-review, handoff-summary, task-chunking |
| engineering | api-design, architecture-review, code-style, communication, debugging, feature-planning, refactoring, testing, workflow |
| metrics | observability-review |
| planning | premortem |
| quality | qa-review |

> Note: `PROJECT_KANBAN.md` and `ROADMAP_EVOLUTIVO.md` cite "23 skills". Actual count is 21. The discrepancy is a stale baseline (one of the items resolved in Onda 0 was the kanban reconciliation); not in scope for this audit.

### 2.2 Frontmatter shape (uniform across all 21 skills)

```yaml
name: <skill-name>
description: <single-sentence what+when>
version: 0.1.0
owner: adaptive-skills
```

### 2.3 Body shape (uniform across all 21 skills)

Eleven sections, in this order:

1. `# Overview`
2. `# When to Use`
3. `# When NOT to Use`
4. `# Core Moves`
5. `# Optional Modules`
6. `# Activation Triggers`
7. `# Expected Output`
8. `# Verification`
9. `# Handoff Signals`
10. `# Pairs Well With`
11. `# Anti-patterns`

The first three are the "protected surfaces" of the Evolution Layer (`docs/skill-model.md`); the rest are proposal-safe.

### 2.4 Sizes

| Metric | Spec limit | Largest in repo |
|---|---|---|
| `SKILL.md` total lines | <500 recommended | 117 (`premortem`) |
| `description` length | ≤1024 chars | 182 chars (`premortem`) |
| `name` length | ≤64 chars | 22 chars (`architecture-review`) |

### 2.5 Subdirectories

None of the 21 skills use the spec's three *named* optional subdirectories (`scripts/`, `references/`, `assets/`). However, **8 of 21 skills have subdirectories under other names** (the spec explicitly allows "any additional files or directories"):

| Skill | Subdirectories present |
|---|---|
| `business/business-design` | `templates/` |
| `design/ux-writing` | `checklists/` |
| `efficiency/checkpoint-review` | `examples/`, `templates/` |
| `efficiency/handoff-summary` | `examples/`, `templates/` |
| `efficiency/task-chunking` | `examples/`, `templates/` |
| `engineering/feature-planning` | `templates/` |
| `planning/premortem` | `examples/`, `templates/`, `workflows/` |

The remaining 13 skills contain only `SKILL.md` at the skill folder root.

These extra subdirectories are spec-compliant (the catch-all "any additional files or directories" applies). Three optional considerations are flagged here for follow-up — none are blockers for Case A:

- **Naming alignment.** The spec gives `scripts/`, `references/`, `assets/` semantic meaning under progressive disclosure. The current names (`templates/`, `examples/`, `workflows/`, `checklists/`) are not wrong, but they are also not the spec's named conventions. Future-proofing could either rename or leave a `references/` symlink pointing at the canonical name.
- **Progressive disclosure footprint.** Spec's optional dirs load on demand; arbitrary subdirs may or may not be picked up by harnesses depending on how each implements discovery. No harness reports of this today, but worth confirming in Epic 5 smoke tests.
- **Library convention vs. spec.** The 4 ad-hoc subdir names should be documented somewhere (likely `docs/skill-model.md`) as part of the library's structural convention.

## 3. Diff: spec vs. current

### 3.1 What is conformant (no action)

| Aspect | Status |
|---|---|
| `SKILL.md` present at skill folder root | ✅ all 21 |
| `name` field present, valid characters | ✅ all 21 |
| `name` matches parent directory | ✅ all 21 (verified by name-vs-dirname comparison) |
| `description` field present, non-empty | ✅ all 21 |
| `description` within 1-1024 chars | ✅ all 21 (longest is 182) |
| `SKILL.md` body under 500 lines | ✅ all 21 (largest is 117) |
| Body format is unrestricted (no spec violations possible by content) | ✅ all 21 |
| Optional subdirs absent (allowed) | ✅ |
| No invalid frontmatter syntax | ✅ all 21 |

### 3.2 What diverges

| # | Divergence | Severity | Impact | Recommendation |
|---|---|---|---|---|
| **D1** | Top-level `version` field in frontmatter — not defined by spec | Low | Some strict clients may warn on unknown top-level fields. Spec's `metadata` field exists specifically for "additional properties not defined by the Agent Skills spec". | Move `version: "0.1.0"` (as quoted string) into `metadata`. |
| **D2** | Top-level `owner` field in frontmatter — not defined by spec | Low | Same as D1. | Move `owner: adaptive-skills` into `metadata`. |

That is the entire delta. No other divergences were found.

### 3.3 What this audit is NOT flagging

Several aspects of Adaptive Skills go *beyond* the spec, which is not a divergence:

- **11-section body structure.** Spec body is unrestricted. The Adaptive Skills body convention is internal library discipline; it does not violate any spec rule. *Note: the internal validator `scripts/validate_skills.py` enforces the 11 sections as required — see §3.4 below.*
- **Domain grouping in `skills/<domain>/<skill-name>/`.** Spec defines the skill folder boundary, not the library boundary. Repo-level organization is unconstrained.
- **Evolution Layer (`evolution/`), projections (`projections/`), templates (`templates/`), scripts (`scripts/`).** Library-level concerns. Out of skill scope.
- **`docs/skill-model.md` defining "protected surfaces" and governance rules.** Library governance discipline. Outside spec scope.

These items are repo-level *enrichment* on top of an otherwise spec-conformant skill format.

### 3.4 Internal validator (`scripts/validate_skills.py`) — interaction with remediation

The repo ships its own validator that runs in CI (Quality Gate, PR [#21](https://github.com/nevitonsantana/adaptive-skills/pull/21)). At the time of this audit (commit on branch `docs/agentskills-io-audit`), it enforces:

```python
REQUIRED_FRONTMATTER = {'name', 'description', 'version', 'owner'}
REQUIRED_SECTIONS = [11 sections]
FORBIDDEN_GENERIC_PATTERNS = ['Crisis Monitor', 'AGENTS.md', ...]
```

This has two implications for Case A remediation:

1. **Lockstep update required.** Moving `version`/`owner` into `metadata` will cause `validate_skills.py` to **fail** in CI because it still expects them at the top level. The remediation PR (Epic 5) MUST update `REQUIRED_FRONTMATTER` to `{'name', 'description'}` and either drop the version/owner enforcement or move it into a `metadata`-aware check. Otherwise CI breaks the same commit that fixes external conformance.
2. **Internal validator and reference validator diverge today.** Internally, 21/21 pass (because version/owner present). Externally (`skills-ref validate`), 21/21 fail. After Case A remediation, both should pass — but only if both validators are updated in the same PR.

### 3.4 Validator-confirmed results (`skills-ref validate`)

The reference validator from [agentskills/agentskills](https://github.com/agentskills/agentskills) was installed (`uv sync` against the pinned `skills-ref==0.1.0`) and run against all 21 skills on 2026-05-21.

**Results: 21 of 21 fail; all for the same reason.**

```
Validation failed for skills/<domain>/<skill-name>:
  - Unexpected fields in frontmatter: owner, version.
    Only ['allowed-tools', 'compatibility', 'description', 'license',
         'metadata', 'name'] are allowed.
```

This is significant in two ways:

1. **The validator is strict, not lenient, about unknown top-level fields.** D1+D2 are not "may warn"; they are deterministic failures per the reference validator. Strengthens the case for remediation.
2. **The validator surfaces no other issues.** `name` / `description` / dir-name match / body shape are all silent — i.e., conformant. Strengthens the case that the delta is exactly D1+D2 and nothing else.

### 3.5 What was *not* tested

- **Conformance of `domain-packs/crisis-management/skills/`.** Out of audit scope (per §3 opening). Will be audited if/when promotion to canonical `skills/` is considered.
- **Compatibility / allowed-tools experimental field behavior.** No skill uses these; nothing to test.

## 4. Strategy options

Per the cross-repo plan §5, three options are considered:

| Case | Description | Fit with this audit |
|---|---|---|
| **A — High conformance** | Small frontmatter adjustments resolve all divergences. APM packaging proceeds with no extra translation layer. | **Best fit.** Only D1+D2 to address (move two fields into `metadata`). |
| **B — Partial conformance** | Keep internal format + add projection layer that exports spec-conformant skills. Adaptive Skills keeps personality; APM consumers get conformant version. | **Overkill** for the observed delta. Projection layer adds maintenance for almost no gain. |
| **C — Large divergence** | Either rewrite to conform (high cost, high gain) or treat as proprietary format with custom adapter (no APM standard). | **Not applicable.** No structural divergence exists. |

## 5. Recommendation

**Case A — High conformance with cosmetic remediation.**

### Rationale

- Of six fields in the spec, two are required and both are conformant with zero issues. The other four are optional and either correctly absent or only marginally divergent.
- The two divergences (D1 + D2) are *cosmetic*, not structural: the spec actually provides `metadata` precisely for the use case `version`/`owner` represent.
- Remediation is mechanical: edit the same two lines in 21 files. No spec-defined behavior changes. No content rewrite. No conceptual debt.
- Adaptive Skills' internal body structure, governance, and evolution discipline are *outside the spec* and therefore unaffected. Conformance does not require giving up the library's personality.
- Case B's projection layer would translate something that is already conformant. Adds machinery and a synchronization burden for no observable gain.

### Proposed remediation (NOT executed in this PR)

For each of 21 `SKILL.md` files:

**Before:**
```yaml
---
name: task-chunking
description: ...
version: 0.1.0
owner: adaptive-skills
---
```

**After:**
```yaml
---
name: task-chunking
description: ...
metadata:
  version: "0.1.0"
  owner: adaptive-skills
---
```

Plus optional follow-ups (not strictly required for conformance):

- Run `skills-ref validate ./skills/<domain>/<name>` against each skill as part of the existing CI Quality Gate (PR [#21](https://github.com/nevitonsantana/adaptive-skills/pull/21)).
- Consider adding `compatibility` field on skills with specific environment assumptions (none observed today, but future skills may need it).
- Consider whether the 11-section internal structure should be documented at `docs/skill-model.md` as "library convention beyond spec" so adopters reading skills know which sections are spec-mandated (none) vs. library convention.

Remediation belongs in a future epic (not Epic 3 per anti-criterion). Could plausibly be folded into Epic 5 (APM packaging) since both touch every skill's frontmatter.

## 6. Risks and follow-ups

| Risk / open item | Mitigation |
|---|---|
| Spec changes after this audit | Re-audit on next minor release of `agentskills.io` spec; the spec is open and tracked on GitHub. |
| `skills-ref validate` reveals issues this audit missed | Run the validator as part of Epic 5 CI; treat any new finding as blocking. |
| Unknown top-level fields *do* break strict clients in practice | Case A remediation removes this risk entirely. |
| Domain pack `crisis-management/skills/` not audited here | Separate audit when that pack is reviewed for promotion or external publication. |

## 7. Revision

Reopen this audit when:
- The `agentskills.io` spec adds or changes required fields.
- A consumer harness rejects an Adaptive Skills installation citing conformance.
- The library adds a fundamentally new skill type (e.g., needs `scripts/` or `allowed-tools`).
- Case A remediation is implemented — at that point, this document moves from "current gap analysis" to "historical record of pre-remediation state".
