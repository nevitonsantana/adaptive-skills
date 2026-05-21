# ADR 003 — Adaptive Skills: relationship with AletheIA

| Field | Value |
|---|---|
| Status | Accepted |
| Date | 2026-05-21 |
| Author | Neviton Santana |
| Deciders | Neviton Santana |
| Related | ADR-001 (Adaptive Skills as capability library), ADR-002 (Domain agnosticism) |
| Supersedes | — |

## 1. Context

Both Adaptive Skills and [AletheIA](https://github.com/nevitonsantana/AletheIA) were developed by the same author in roughly the same period, often against the same consumer project (Crisis Monitor). Existing docs already cross-reference the two — see [`docs/aletheia-integration.md`](../aletheia-integration.md), [`docs/aletheia-first-test.md`](../aletheia-first-test.md), and the "Integration with AletheIA" milestone in [`ROADMAP_EVOLUTIVO.md`](../../ROADMAP_EVOLUTIVO.md).

This cross-referencing is useful but creates a question: *can Adaptive Skills be used without AletheIA, and vice versa? Are they the same product split into two repos, or two products that happen to share a context?*

ADR-001 and ADR-002 settle Adaptive Skills' identity in isolation. This ADR settles the relationship.

## 2. Decision

**Adaptive Skills and AletheIA are two independent artifacts on distinct ecosystem layers. They can be used together, but neither requires the other.** Their relationship is *reference*, not *dependency*.

### 2.1 Layer separation (normative)

- **Adaptive Skills** occupies the *capability library* layer (ADR-001).
- **AletheIA** occupies the *operating overlay* layer (AletheIA's ADR-004 and ADR-005).

The two layers are orthogonal: an overlay can run with no capability library, and a capability library can be consumed by harnesses with no overlay. Combining them produces compounded value but is not architecturally required.

### 2.2 Allowed integration shapes

Three combinations are all valid:

1. **Adaptive Skills standalone.** Consumer projects install one or more skills via projection (today) or APM (after Epic 5). The harness uses skills directly. AletheIA is absent.
2. **AletheIA standalone.** Consumer projects install AletheIA as an operating overlay. AletheIA's contracts and gates do not require any specific skill library; they call out to whatever capability is available, including custom in-project skills.
3. **Together.** AletheIA references Adaptive Skills as the preferred capability library. Skills installed via APM at the consumer level are available both for direct harness use and for AletheIA's contracts to invoke.

### 2.3 What this is NOT

- **Not** a claim that Adaptive Skills is a sub-component of AletheIA, or vice versa.
- **Not** a requirement that integration uses a particular protocol — both can interoperate via files, projections, or future APM-installed packages.
- **Not** a deprecation of existing integration docs (`docs/aletheia-integration.md`, `docs/aletheia-first-test.md`). Those docs describe one integration shape (option 3 above) and remain useful.

### 2.4 When skills live in the consumer project vs. in Adaptive Skills

A consumer project that uses AletheIA will accumulate project-specific skills. Those skills live **inside the consumer project's overlay directory** (typically `ops/ai/skills/` or equivalent), not in the Adaptive Skills repo. They are local to the project.

Skills are promoted to Adaptive Skills (the shared library) when:

- The skill has been validated in ≥1 project.
- The skill is generalizable (passes the ADR-002 reading test against ≥1 other domain hypothetically).
- The skill follows the protected-surface and evolution discipline of Adaptive Skills (`docs/skill-model.md`).

This promotion path mirrors AletheIA's own ADR-002 (memory and skill promotion policy) for symmetry.

## 3. Consequences

**Positive.** Adopters can choose their entry point: a team that wants only portable skills can take Adaptive Skills alone; a team that wants only governance can take AletheIA alone; a team that wants both gets a compounded effect. Marketing/positioning becomes honest — neither repo overstates the other's necessity.

**Negative.** Two repos require two release cadences, two CI pipelines, two docs sets. Some duplicated material (notably the ecosystem map, by design) must be kept in sync. Cross-repo navigation cost is non-zero for new adopters.

**Accepted tradeoff.** Two coherent repos with clear boundaries beat one merged repo with internal layer confusion.

## 4. Alternatives considered

- **A. Merge the two repos into one.** Rejected — the layers are genuinely distinct (capability vs. governance), and a merged repo would force consumers who want only one layer to take both.
- **B. Make Adaptive Skills a hard dependency of AletheIA.** Rejected — eliminates the "AletheIA standalone" use case and contradicts AletheIA's ADR-004 (overlay does not embed capability).
- **C. Make AletheIA a hard dependency of Adaptive Skills.** Rejected — eliminates the "library standalone" use case; most harnesses consume skills directly without an overlay.
- **D. Position Adaptive Skills as "AletheIA's skill module."** Rejected — accurate marketing-wise in the *together* case but misleading for the other two cases; loses standalone framing.

## 5. Relationship

ADR-001 settled Adaptive Skills' identity. ADR-002 settled its domain agnosticism. This ADR settles its cross-repo relationship. The mirror in AletheIA is ADR-005 (positioning in the ecosystem), which explicitly lists Adaptive Skills as a non-competitor. [`docs/concepts/ecosystem-map.md`](../concepts/ecosystem-map.md) is the synchronized view of both repos.

Epics 4 and 5 of the 2026-05-21 cross-repo plan implement section 2.2 by making both repos installable as independent APM packages — this ADR is prerequisite to both.

## 6. Review

Reopen when:

- Adopters report that the "AletheIA standalone" or "Adaptive Skills standalone" path produces materially incomplete value → either the standalone story is unclear (fix the artifact) or the layers are entangled in practice (revisit ADR-001 / AletheIA's ADR-004).
- A pattern emerges where the same skill needs to live in both repos with different shapes → tighten the promotion criterion in section 2.4.
- The "together" combination becomes the only realistic use case in practice → consider whether the two-repo split still earns its cost.

If a review confirms the decision unchanged, record the confirmation date here and continue.
