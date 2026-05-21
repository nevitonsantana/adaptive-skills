# ADR 001 — Adaptive Skills as capability library

| Field | Value |
|---|---|
| Status | Accepted |
| Date | 2026-05-21 |
| Author | Neviton Santana |
| Deciders | Neviton Santana |
| Related | ADR-002 (Domain agnosticism), ADR-003 (Relationship with AletheIA) |
| Supersedes | — |

## 1. Context

Adaptive Skills was built incrementally through Q1–Q2 2026 with no explicit position statement about *what kind of artifact it is* in the agentic ecosystem. The repo contains: a skill model (`docs/skill-model.md`), 23+ skills across 8 domains, evolution discipline (observations/proposals/reviews), projection scripts to Codex/Claude, and a Crisis Monitor case study used as field evidence.

These artifacts can be read in several incompatible ways:

- As an operating overlay (it has governance, evolution, projection — overlay-like).
- As a runtime (it has projection scripts that "install" things — runtime-like).
- As a squad bundle (it has domain packs and pilot reports — bundle-like).
- As a capability library (it has portable skills cataloged by domain — library-like).

Without a fixed reading, every PR and every adopter conversation re-litigates the same question. The 2026-05-21 cross-repo plan (Epic 1) requires this to be settled before APM packaging and external adoption.

## 2. Decision

**Adaptive Skills is a capability library: a portable, governed collection of micro-skills consumable by harnesses or referenced by overlays.**

### 2.1 What this means (normative)

- A **skill** is a single unit of reusable capability: a name, a description, triggers, core moves, optional modules, when-to / when-not-to use.
- The library is **portable**: skills must run in any conformant harness; no skill assumes a specific runtime, harness, or consumer project.
- The library is **governed**: skills do not self-edit; changes go through the evolution loop (observation → proposal → review). Protected surfaces (name, core moves, when-not-to-use) are invariants.
- Skills are **consumed in two modes**: (a) directly by a harness via projection or APM install; (b) indirectly by an operating overlay (e.g., AletheIA) that references them.

### 2.2 What Adaptive Skills is NOT

- **Not an operating overlay.** It does not legislate how a consumer project decides, validates, hands off, or reports. That layer is AletheIA (or another overlay; see ADR-003).
- **Not a runtime.** Projection scripts copy artifacts into a harness; they do not persist sessions, manage memory, or run agents.
- **Not a squad-ready bundle.** Skills are individual capabilities. The library does not ship a pre-configured squad of agents the way BMAD or SDD do.
- **Not a Crisis-Monitor framework.** Crisis Monitor was the first validation case (see ADR-002 and PR [#31](https://github.com/nevitonsantana/adaptive-skills/pull/31)); the library is domain-agnostic.

### 2.3 Conformance posture

Adaptive Skills targets conformance with [`agentskills.io`](https://agentskills.io/) as the open standard for the capability-library layer. The exact strategy (full conformance, partial conformance with projection, or proprietary format with adapter) is the subject of Epic 3 of the cross-repo plan and will be recorded in a future ADR-004.

## 3. Consequences

**Positive.** Pitch becomes one sentence: "portable, governed micro-skill library, agentskills.io-conformant, usable standalone or alongside an overlay." Risk that adopters read the projection scripts as "a CLI to learn" is bounded. Boundary against runtime concerns is explicit, so feature pressure to absorb session/memory/cron is rejected on principle, not on taste.

**Negative.** The "library" framing is conceptually less immediate than "framework you install and run"; first-conversation education cost. Some adopters want a turnkey agent setup and will need to be pointed at BMAD/SDD plus Adaptive Skills, rather than expecting Adaptive Skills alone to suffice.

**Accepted tradeoff.** Smaller, sharper surface beats broader surface that drifts toward runtime or overlay concerns.

## 4. Alternatives considered

- **A. Position as an operating overlay.** Rejected — collapses Adaptive Skills into AletheIA's layer; duplicates the overlay niche; loses the standalone-library use case.
- **B. Position as a runtime / "skill runner."** Rejected — projection is install-time, not run-time; persistent state is out of scope; conflates layers.
- **C. Position as a squad bundle.** Rejected — bundles ship configured agents; Adaptive Skills ships capability primitives, not configured squads.
- **D. Leave positioning implicit.** Rejected — re-litigation cost across PRs and adopter conversations already exceeds the cost of this ADR.

## 5. Relationship

ADR-002 fixes the orthogonal axis (domain agnosticism). ADR-003 fixes the relationship with AletheIA so the two repos can be used independently or together. Epic 3 of the cross-repo plan (`agentskills.io` conformance audit) and Epic 5 (APM packaging) both consume this ADR as prerequisite. [`docs/concepts/ecosystem-map.md`](../concepts/ecosystem-map.md) is the public-facing context.

## 6. Review

Reopen when:

- The library starts persistently storing runtime state to function correctly → the layer boundary moved; either revisit this ADR or extract the runtime concern.
- Adopters consistently report that they expected an overlay or a squad bundle → either the positioning text is unclear (fix the artifact) or the niche shifted (revisit the ADR).
- A successor standard to `agentskills.io` consolidates with materially different assumptions about what a skill is → re-evaluate the library framing.

If a review confirms the decision unchanged, record the confirmation date here and continue.
