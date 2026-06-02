---
name: domain-language-alignment
description: Align project language across product intent, domain concepts, documentation, ADRs, and code before implementation or architectural change.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: engineering
---

# Overview

Use this skill to reconcile vocabulary before agents touch code or plan. Misaligned language between product, domain, docs, and code is a hidden source of defects, rework, and ambiguous handoffs. This skill makes terms explicit and recommends where they should be recorded.

# When to Use

- before a relevant implementation or architectural change
- when the request uses vague, overloaded, or inconsistent terms
- when business language conflicts with names in the code
- when a decision should become an ADR or decision record
- when context docs exist (for example `CONTEXT.md`, `CONTEXT-MAP.md`, or an `adr/` directory)

# When NOT to Use

- for trivial local changes with no shared vocabulary at stake
- when the domain language is already settled and consistently used
- as a substitute for actually deciding the design

# Core Moves

1. Identify the project context and available domain docs.
2. Extract key terms used in the request, docs, code, and prior decisions.
3. Mark ambiguous, overloaded, missing, or conflicting terms.
4. Recommend canonical terms and where they should be recorded.
5. Flag decisions that deserve an ADR or decision record.
6. Produce a concise alignment record for handoff.

# Optional Modules

- **Glossary pass** — Collect terms into a single glossary when many concepts are in play.
- **Code-vs-domain diff** — Compare names in code against domain language to surface drift.
- **ADR trigger sweep** — Identify which naming or modeling decisions warrant a recorded decision.

# Activation Triggers

- Use the glossary pass when more than a handful of terms are contested.
- Use the code-vs-domain diff when code names and business names appear to diverge.
- Use the ADR trigger sweep when a term choice would constrain future design.

# Expected Output

- canonical terms
- ambiguous terms
- naming conflicts
- docs or ADR updates recommended
- implementation risk from language mismatch
- handoff summary

# Verification

- Each canonical term has a single agreed meaning and a recommended home.
- Ambiguous and conflicting terms are listed explicitly, not silently resolved.
- Decisions that constrain future design are flagged as ADR candidates.
- The handoff summary is usable by someone who was not in the discussion.

# Handoff Signals

- A product or domain owner must confirm a contested term's meaning.
- A naming decision needs an ADR before implementation proceeds.
- The mismatch reveals a modeling problem beyond vocabulary.

# Pairs Well With

- `feature-planning`
- `architecture-review`
- `api-design`

# Anti-patterns

- Picking a "winning" term without recording it or its rationale.
- Treating a naming conflict as cosmetic when it reflects a modeling disagreement.
- Producing a glossary nobody can find or will maintain.
