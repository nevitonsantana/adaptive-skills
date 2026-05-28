# Architecture Decision Records (ADRs)

This directory holds **durable architectural decisions** for Adaptive Skills. ADRs are written when a decision is hard to reverse, affects multiple parts of the library, or settles a recurring ambiguity that has cost time to re-litigate.

## What an ADR is — and is not

- **Is**: a record of *why* we decided something at a specific date, with the alternatives we rejected and the conditions that would reopen the decision.
- **Is not**: a tutorial, a roadmap, or a contract spec. Those live in `docs/concepts/`, `ROADMAP_EVOLUTIVO.md`, and the skill model docs.

If a document explains *how* to do something, it is a guide. If it specifies *what must be true*, it is a contract. ADRs answer *why this path and not another*.

## Convention

- **Format**: lightweight, repo-native. Mirrors the AletheIA repo convention for cross-repo consistency.
- **Filename**: `ADR-NNN-<kebab-case-title>.md`, with `NNN` zero-padded.
- **Numbering**: monotonic, never reused. If an ADR is superseded, the new ADR gets the next number and links back via the `Supersedes` field.
- **Status values**: `Proposed`, `Accepted`, `Superseded by ADR-XXX`, `Rejected`, `Deprecated`.
- **Length**: prefer ≤2 pages. If an ADR grows past that, the decision is probably mixing two concerns.

## Required structure

Every ADR starts with a metadata table:

```markdown
| Field | Value |
|---|---|
| Status | Accepted |
| Date | YYYY-MM-DD |
| Author | <name> |
| Deciders | <names> |
| Related | ADR-XXX — <title> |
| Supersedes | — or ADR-XXX |
```

Followed by numbered sections:

1. **Context** — what is the state of the world and what is the open question.
2. **Decision** — what we decided, in normative voice.
3. **Consequences** — positive, negative, and accepted tradeoffs.
4. **Alternatives considered** — what we rejected and why.
5. **Relationship** — to other ADRs, phases, or artifacts that depend on this decision.
6. **Review** — conditions that would reopen the ADR.

## Current ADRs

| ID | Title | Status |
|---|---|---|
| [ADR-001](ADR-001-adaptive-skills-as-capability-library.md) | Adaptive Skills as capability library | Accepted |
| [ADR-002](ADR-002-domain-agnosticism.md) | Domain agnosticism | Accepted |
| [ADR-003](ADR-003-relationship-with-aletheia.md) | Relationship with AletheIA | Accepted |
| [ADR-004](ADR-004-agentskills-io-conformance.md) | `agentskills.io` conformance strategy | Accepted |
| [ADR-005](ADR-005-apm-packaging-strategy.md) | APM packaging strategy | Accepted |
| [ADR-006](ADR-006-knowledge-aware-skills-boundary.md) | Knowledge-aware skills boundary | Accepted |
