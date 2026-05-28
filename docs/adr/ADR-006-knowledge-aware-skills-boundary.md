# ADR 006 — Knowledge-aware skills boundary

| Field | Value |
|---|---|
| Status | Accepted |
| Date | 2026-05-28 |
| Author | Neviton Santana |
| Deciders | Neviton Santana |
| Related | ADR-001 (Adaptive Skills as capability library), ADR-002 (Domain agnosticism), ADR-003 (Relationship with AletheIA), AletheIA ADR-008 (Knowledge Governance Layer) |
| Supersedes | — |

## 1. Context

Adaptive Skills is meant to be portable: a skill is a *procedure* that can be picked up by any consumer. As soon as a skill needs proprietary content — a strategic framework, an internal policy, a persona — there is pressure to inline that content into the skill. Doing so breaks portability, leaks proprietary material into every consumer that loads the skill, and prevents independent versioning.

AletheIA ADR-008 introduces a Knowledge Governance Layer that solves the framework-side problem: knowledge packs, manifests, source precedence, restricted-use policy, audit. The open question for Adaptive Skills is: *what does a skill author need to honor on the skill side, and what new skills must exist to support the layer?*

## 2. Decision

Establish the following non-negotiables for Adaptive Skills:

1. **Skill carries procedure; knowledge pack carries content.** No skill ships verbatim text from a proprietary framework, internal policy, or restricted source. No skill ships examples with real client / customer identifiers.
2. **Skills declare slot types, not source ids.** A skill's `skill-knowledge-dependency.yaml` lists slot names (e.g. `strategic_framework`) with `accepted_types`. It never names a specific pack.
3. **Every knowledge-aware skill supports two modes.** *Generic* runs with general criteria when no governed source is available; *knowledge-aware* runs with packs resolved by AletheIA. Generic-mode output must be marked as such.
4. **`fallback_behavior` is mandatory.** Each of `missing_required_source`, `missing_optional_source`, `restricted_source`, and `conflicting_sources` must declare an explicit choice. Silent fallback is never an option.
5. **Capsule-first by default.** When a slot is filled, the skill reasons from the capsule. Excerpts or full source are consulted only when the slot's retrieval mode and the task explicitly allow it.
6. **Three governance skills ship as part of the boundary.** `knowledge-source-evaluation`, `knowledge-conflict-resolution`, and `restricted-context-check` are the minimal skill-side toolkit that lets AletheIA's contracts be honored at execution time.

The boundary lands as docs + templates + the three governance skills, with no runtime implementation. Skills remain flat under `skills/<name>/` per the existing convention and the `agentskills.io` conformance loop.

## 3. Consequences

**Positive**
- Portability is preserved. A skill that depends only on slot types can be picked up by any consumer that registers compatible packs.
- A clear seam exists between Adaptive Skills (procedure) and AletheIA (governance) — neither encroaches on the other.
- New skills can be authored against the `knowledge-aware-skill-template` without re-deriving the boundary each time.
- The three governance skills give consumers a ready-made evaluation, conflict, and risk-check toolkit.

**Negative / accepted tradeoffs**
- Skill authors must produce a manifest (`skill-knowledge-dependency.yaml`) alongside `SKILL.md`. This is friction at authoring time, but eliminates a class of governance failure at runtime.
- Until a consumer publishes governed packs, knowledge-aware skills run only in generic mode. We accept this: the alternative is silent dependence on whatever happens to be in context.
- The `evolution/registry.json` requires an entry per published skill — three more entries to maintain — but the validator catches divergence immediately.

## 4. Alternatives considered

- **Inline proprietary content into skills.** Rejected. Destroys portability and violates ADR-002 (Domain agnosticism). Also surfaces in audit and licensing risk.
- **Make knowledge-awareness opt-in via a separate skill family.** Rejected. The boundary belongs to every skill that might consume governed content; making it optional invites drift.
- **Nest the governance skills under `skills/governance/`.** Rejected. The `agentskills.io` conformance loop iterates `skills/*/` expecting each to be a single skill folder with `SKILL.md`. Nesting breaks that contract; the convention is flat.
- **Treat AletheIA's resolver as a soft suggestion that skills may override.** Rejected. Soft overrides defeat the purpose of governance. Skills declare and consume; AletheIA decides.

## 5. Relationship

- Implements the skill-side surface of AletheIA ADR-008 (Knowledge Governance Layer).
- Reinforces ADR-002 (Domain agnosticism) by keeping company-specific frameworks out of the library.
- Reinforces ADR-003 (Relationship with AletheIA) — Adaptive Skills executes, AletheIA governs.
- Does not change the existing skill model (Core + Modules + Triggers); adds a metadata flag (`knowledge_aware: true`) and a sibling manifest.

## 6. Review

Reopen this ADR if:

- A runtime resolver lands and the skill-side contract needs to harden against an actual API.
- A consumer pushes back on the two-mode requirement (generic + knowledge-aware) as too heavy.
- The three governance skills prove insufficient and a fourth genuinely belongs in the canon (not in a domain pack).
- `agentskills.io` conformance changes to allow nested categories under `skills/`.
