---
title: "ADR 002 — Adaptive Skills: domain agnosticism"
description: "Reference documentation for ADR 002 — Adaptive Skills: domain agnosticism in Adaptive Skills."
---

| Field | Value |
|---|---|
| Status | Accepted |
| Date | 2026-05-21 |
| Author | Neviton Santana |
| Deciders | Neviton Santana |
| Related | ADR-001 (Adaptive Skills as capability library), ADR-003 (Relationship with AletheIA) |
| Supersedes | — |

## 1. Context

Adaptive Skills was developed and validated through Q1–Q2 2026 with **Crisis Monitor** as the primary consumer project. Most existing evolution observations (`evolution/observations/`) reference Crisis-Monitor-specific situations; the [Crisis Management domain pack](https://github.com/nevitonsantana/adaptive-skills/blob/main/domain-packs/crisis-management) is the most mature domain pack; and the original README treated the case study as central evidence.

PR [#31](https://github.com/nevitonsantana/adaptive-skills/pull/31) (2026-05-18) already moved Crisis Monitor from "active backlog" to "team-owned field evidence." This ADR formalizes that shift and extends it: the entire library is domain-agnostic, not just the README.

The 2026-05-21 cross-repo plan (Epic 2) implements the cleanup of canonical content that still embeds Crisis Monitor framing.

## 2. Decision

**Adaptive Skills is domain-agnostic. Crisis Monitor is the first validation case, not the canonical case.** Other consumer projects and domains are expected and prioritized.

### 2.1 Membership criterion (canonical vs. example)

A skill, doc, or artifact belongs in **canonical layer** (`skills/`, `docs/`, `projections/`, `evolution/templates/`) only if it remains useful and well-defined after substituting Crisis Monitor for any other domain (software product, design system, data pipeline, regulatory program, operations runbook, etc.).

A skill, doc, or artifact belongs in **example layer** (`domain-packs/crisis-management/`, case studies, labeled examples) when it depends on Crisis-Monitor-specific stakeholders, vocabulary, incidents, or workflows.

### 2.2 Domain-pack semantics

Domain packs (e.g., `domain-packs/crisis-management/`) are explicitly **example layer**. A domain pack is a curated combination of skills + scenario evidence + glossary for one domain. It is not canon. The library can have many domain packs; none are canonical.

After Epic 2 of the cross-repo plan, `domain-packs/crisis-management/` will carry a README header that states this explicitly: "example domain pack — not the canonical domain pack."

### 2.3 Reading test (operational)

For any canonical skill or doc, the test is: *if a new adopter from a different domain reads this, do they see general capability and a labeled example, or do they see Crisis Monitor and have to translate?* The latter is a defect, tracked by Epic 2.

### 2.4 What this is not

- **Not** a requirement to produce a fictional second domain pack for balance. Declared agnosticism + transparency about first validation is sufficient until soft-launch produces real cases.
- **Not** a removal of Crisis-Monitor content. The case study and the domain pack are preserved as labeled evidence.
- **Not** a claim that *any* domain is equally well-supported today — only that nothing in the *library* prevents another domain.

## 3. Consequences

**Positive.** Adopters from non-crisis domains (a design squad, a data team, a compliance group) can read the canonical layer and recognize their work without translation. The Crisis-Monitor evidence gains a clearer role: labeled field evidence, not implicit canon. Skill catalog (Epic 7) can be organized by capability, not by domain.

**Negative.** Some skills currently named or framed against Crisis-Monitor scenarios will need renaming or reframing in Epic 2. Until that work lands, the gap between declared agnosticism and observable agnosticism is visible. Evolution observations from Q2 2026 are heavily Crisis-Monitor-flavored — Epic 2 + the reformulated Evolution Cycle #4 (2026-05-21 → 2026-06-30) will reclassify them.

**Accepted tradeoff.** A short window of declared-but-not-yet-observable agnosticism beats keeping Crisis Monitor entangled in canonical content. The window closes with Epic 2.

## 4. Alternatives considered

- **A. Declare Adaptive Skills crisis-domain-specific; build a separate general library later.** Rejected — the skill model was already general by intent; only the examples were specific. Forking duplicates maintenance for no gain.
- **B. Treat Crisis Monitor as the canonical reference; other domains as ports.** Rejected — institutionalizes the residue this ADR removes; contradicts the cross-repo plan's H5.
- **C. Produce a synthetic second domain pack to balance Crisis Management.** Rejected — premature, expensive, and creates a fictional artifact whose existence reduces credibility.
- **D. Leave agnosticism implicit.** Rejected — re-litigation cost argument from ADR-001.

## 5. Relationship

ADR-001 fixed *what* Adaptive Skills is (capability library). This ADR fixes *what it applies to* (any domain). ADR-003 fixes the relationship with AletheIA. Epic 2 of the cross-repo plan implements section 2.1 by auditing and reclassifying Crisis Monitor references. The reformulated Evolution Cycle #4 (period 2026-05-21 → 2026-06-30, see [`ROADMAP_EVOLUTIVO.md`](https://github.com/nevitonsantana/adaptive-skills/blob/main/ROADMAP_EVOLUTIVO.md)) reclassifies existing observations against this criterion.

The mirror ADR in the AletheIA repo (ADR-006) carries the same principle for the overlay layer.

## 6. Review

Reopen when:

- A second consumer project adopts Adaptive Skills and surfaces a structural assumption that *is* genuinely Crisis-Monitor-specific → narrow the agnosticism scope or extract the assumption into a domain pack.
- Soft-launch feedback shows adopters consistently fail to map a canonical skill to their domain without translation → the canonical layer needs further despoluição beyond Epic 2.
- A domain emerges where Adaptive Skills *should* take an opinionated stance (e.g., a heavily regulated domain with mandatory skill profiles) → consider a domain pack rather than reopening the core agnosticism claim.

If a review confirms the decision unchanged, record the confirmation date here and continue.
