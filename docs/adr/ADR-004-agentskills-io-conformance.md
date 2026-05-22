# ADR 004 — Adaptive Skills: `agentskills.io` conformance strategy

| Field | Value |
|---|---|
| Status | Accepted |
| Date | 2026-05-21 |
| Author | Neviton Santana |
| Deciders | Neviton Santana |
| Related | ADR-001 (Adaptive Skills as capability library), [`_meta/agentskills-io-conformance-audit.md`](../_meta/agentskills-io-conformance-audit.md) |
| Supersedes | — |

## 1. Context

ADR-001 declared a *posture* toward [`agentskills.io`](https://agentskills.io/specification): Adaptive Skills aims at conformance with the open standard for the capability-library layer. The *strategy* was deferred to this ADR pending a real gap analysis.

Epic 3 of the 2026-05-21 cross-repo plan produced that gap analysis (see [`_meta/agentskills-io-conformance-audit.md`](../_meta/agentskills-io-conformance-audit.md)). The audit was performed manually and confirmed by running the reference validator [`skills-ref==0.1.0`](https://github.com/agentskills/agentskills/tree/main/skills-ref) against all 21 skills.

Findings (full detail in the audit doc):

- **Required spec fields** (`name`, `description`): conformant on all 21 skills.
- **Folder structure**: conformant on all 21 (each skill folder contains `SKILL.md` at root; `name` field matches parent directory).
- **Body**: spec body is unrestricted; the 11-section internal convention is library enrichment, not divergence.
- **Sizes**: largest `SKILL.md` is 117 lines (spec recommends <500); longest `description` is 182 chars (spec limit 1024).
- **Divergences observed**: two — `version` and `owner` are present as top-level frontmatter fields, which the spec does not define. The validator rejects them on this basis (21/21 fail with the same message).

The plan offered three strategy options (§5 Epic 3):

- **Case A — High conformance**: small adjustments resolve all divergences; APM packaging proceeds without translation.
- **Case B — Partial conformance**: keep internal format + add projection layer for spec-conformant export.
- **Case C — Large divergence**: rewrite to conform (high cost) or treat as proprietary (no APM standard; custom adapter).

## 2. Decision

**Adaptive Skills adopts Case A: high conformance with cosmetic remediation.**

### 2.1 What this means

- The library will move the `version` and `owner` top-level frontmatter fields into the spec-defined optional `metadata` field. No other change to skills is required.
- After remediation, the reference validator (`skills-ref validate`) will pass against all 21 skills.
- The library's internal 11-section body convention, governance discipline (`docs/skill-model.md`), evolution layer, projection scripts, and domain packs are **unaffected** — they live outside the skill folder boundary and outside spec scope.
- No projection / translation layer is built. Skills consumed via APM and skills consumed by harnesses directly read the same files.

### 2.2 Remediation pattern (normative)

For each `SKILL.md`:

**Before:**
```yaml
---
name: <skill-name>
description: <...>
version: 0.1.0
owner: adaptive-skills
---
```

**After:**
```yaml
---
name: <skill-name>
description: <...>
metadata:
  version: "0.1.0"
  owner: adaptive-skills
---
```

The `version` value MUST be quoted as a string, per the spec's `metadata` field type (string→string map).

### 2.3 When remediation lands

Remediation is **not** executed in this ADR's PR (anti-criterion of Epic 3). It will be folded into **Epic 5** of the cross-repo plan (APM packaging of Adaptive Skills), since both touch every skill's frontmatter and Epic 5 has a natural validation gate (`apm install` smoke test). Alternative: a small standalone PR before Epic 5; either is acceptable.

Concretely, Epic 5 must produce (all in the same PR — see §3 below on the lockstep requirement):
- 21/21 `SKILL.md` files updated per §2.2 pattern.
- `scripts/validate_skills.py` updated to reflect the new frontmatter shape: drop `version`/`owner` from `REQUIRED_FRONTMATTER`; if version/owner are still wanted as soft requirements, check them inside `metadata` instead.
- `skills-ref validate` invoked in CI (new Quality Gate step) and passing on all 21 skills.
- `apm install nevitonsantana/adaptive-skills` succeeds on a clean smoke project.
- No body content changes; no protected-surface touch (governance preserved).

### 2.4 Validation as ongoing discipline

`skills-ref validate` should run in the CI Quality Gate (already established by PR [#21](https://github.com/nevitonsantana/adaptive-skills/pull/21)) once remediation lands. Concretely: a new CI step that validates every `SKILL.md` against the pinned validator version. This makes future regressions deterministic, not "may warn".

## 3. Consequences

**Positive.** Adaptive Skills moves from "high-conformance-with-caveat" to "validator-clean" with mechanical edits. APM packaging (Epic 5) unblocked: skills install on any spec-compliant harness without a translation step. The library's identity — governance, evolution, body convention — is fully preserved.

**Negative — lockstep update required.** The repo's internal validator [`scripts/validate_skills.py`](../../scripts/validate_skills.py) currently enforces `REQUIRED_FRONTMATTER = {'name', 'description', 'version', 'owner'}` and runs in the Quality Gate CI (PR [#21](https://github.com/nevitonsantana/adaptive-skills/pull/21)). Moving `version`/`owner` into `metadata` without updating this validator in the same PR would break CI. The remediation PR (Epic 5 or a standalone) therefore MUST:

1. Edit all 21 `SKILL.md` files per §2.2.
2. Edit `scripts/validate_skills.py` to drop `version`/`owner` from `REQUIRED_FRONTMATTER` (or move them to a `metadata`-aware check).
3. Add `skills-ref validate` to the Quality Gate workflow so external and internal validators agree from that point forward.

External consumers depending on the old top-level shape (if any exist outside this repo) will need a one-line change to read from `metadata`. None are known today.

**Accepted tradeoff.** Strict conformance with the open standard outweighs preserving idiosyncratic frontmatter shape. Case A delivers the maximum compatibility surface for the minimum delta — provided the lockstep update is respected.

## 4. Alternatives considered

- **Case B (partial + projection).** Rejected — would add a projection layer to translate something already conformant after a 1-line frontmatter edit. Adds maintenance for no observable gain. Considered only if the library deliberately wanted to keep `version`/`owner` at top level for an external reason; no such reason exists.
- **Case C — rewrite for full conformance.** Rejected because *no* rewrite is needed; the audit shows the library is structurally compliant.
- **Case C — proprietary format with custom adapter.** Rejected — abandons APM standard for negative reasons. The audit shows there is no structural reason to be proprietary; choosing it would be self-imposed isolation.
- **Do nothing.** Rejected — validator deterministically fails, which would block APM packaging.

## 5. Relationship

ADR-001 declared the *posture*; this ADR settles the *strategy*. ADR-002 (domain agnosticism) and ADR-003 (relationship with AletheIA) are orthogonal. The audit doc [`_meta/agentskills-io-conformance-audit.md`](../_meta/agentskills-io-conformance-audit.md) is the empirical basis; this ADR is the decision.

**Downstream:** Epic 5 of the cross-repo plan (APM packaging) implements section 2.2 + 2.4 as part of its scope.

## 6. Review

Reopen when:

- The `agentskills.io` spec adds, removes, or modifies required fields → re-audit, then either reaffirm Case A or reopen the choice.
- The reference validator changes its strictness model (e.g., starts accepting unknown top-level fields, or starts rejecting something currently passing) → re-audit.
- A spec-divergent feature becomes valuable enough to justify Case B (e.g., a domain-specific extension that doesn't fit in `metadata`) → reopen.
- A harness in the ecosystem rejects Adaptive Skills installation citing a conformance issue not in this audit → re-audit and address.

If a review confirms the decision unchanged, record the confirmation date here and continue.
