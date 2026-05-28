---
name: feature-value-governance
description: Judge whether a proposed feature is worth doing — business intent, revenue or operational lever, user evidence, opportunity-tree fit, complexity cost, and overreach risk — using governed knowledge packs when available and general criteria when not.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: product
  knowledge_aware: true
---

# Overview

Use this skill to decide whether a proposed feature deserves investment before it enters a roadmap or a build. It surfaces the business intent the feature serves, the revenue or operational lever it pulls, the user evidence behind it, its alignment to the opportunity tree, its complexity cost, and its risk of overreaching into compliance, accessibility, or privacy.

The skill is **knowledge-aware**: it declares the knowledge it needs as slot *types* (see `skill-knowledge-dependency.yaml`) and lets AletheIA's [Knowledge Governance Layer](../../../aletheia/docs/concepts/knowledge-governance-layer.md) resolve which packs fill them. It carries **no** proprietary framework, policy, or persona content of its own. It runs in two modes:

- **Generic mode** — no authorized pack is available. The skill applies its general criteria and marks the output `mode: generic` with no fabricated pack citations.
- **Knowledge-aware mode** — the resolver returns at least one satisfying pack. The skill reasons from the **capsule first**, respects active restrictions, and cites every consumed pack as `pack_id@version`.

# When to Use

- A feature is proposed and someone must decide whether it is worth doing.
- Prioritizing or sequencing a backlog where value and cost are contested.
- A roadmap decision needs an explicit business intent and lever, not just a request.
- A feature might overreach into compliance, accessibility, or privacy and the risk needs naming before commitment.

# When NOT to Use

- The decision to build is already made and only execution planning remains (use `feature-planning`).
- The change is tiny and local with obvious value.
- The task is operating the Knowledge Governance Layer itself — registering a source (`knowledge-source-evaluation`), resolving a source conflict (`knowledge-conflict-resolution`), or risk-checking a sensitive source before use (`restricted-context-check`).
- No problem framing exists yet; there is nothing whose value can be judged.

# Core Moves

1. **Frame the feature and resolve knowledge.** State the proposed feature in one line. Identify which knowledge slots the task needs (`strategic_framework` always; `accessibility_guidelines` and `operating_model` by task shape). Read the resolved context pack: satisfied slots, gaps, conflicts, active restrictions. If a required slot is unsatisfied, apply `fallback_behavior` and say so loudly.
2. **Surface business intent.** Name the business or product intent the feature serves. In knowledge-aware mode, anchor it to the resolved `strategic_framework`; in generic mode, derive it from stated goals and mark the inference.
3. **Name the lever.** Identify the revenue or operational lever the feature pulls (acquisition, conversion, retention, expansion, cost-to-serve, risk reduction). One feature, one primary lever.
4. **Weigh user evidence.** Cite the user evidence supporting the feature from the `personas` slot when present; otherwise state the assumption explicitly with an assumption marker.
5. **Check opportunity-tree alignment.** Place the feature against the opportunity / outcome it claims to serve. Flag features that serve no live opportunity.
6. **Estimate complexity cost.** Give a coarse complexity read (low / medium / high) and the main drivers. Complexity is a cost against value, not a veto on its own.
7. **Assess overreach risk.** Judge whether the feature reaches into compliance, accessibility, or privacy. When `required_when` triggers match (interface change, content decision, customer-facing experience), the `accessibility_guidelines` slot becomes required; an unmet required slot stops the analysis per fallback.
8. **Render the verdict and audit trail.** Produce the **Expected Output** block: a worth-doing verdict with rationale, every consumed pack cited as `pack_id@version`, unsatisfied slots with the fallback applied, and any conflicts resolved via the [source precedence policy](../../../aletheia/docs/contracts/source-precedence-policy.md).

# Optional Modules

- **Revenue lever detail** — Decompose the primary lever into a small driver model (e.g. which step of the funnel, which cost line) when the value claim is contested.
- **Opportunity-tree mapping** — Draw the feature → opportunity → outcome path explicitly when the backlog has competing bets.
- **Complexity audit** — Expand the complexity read into build, integration, and operational-carry costs when complexity is the deciding factor.
- **Overreach deep-check** — When an `accessibility_guidelines`, privacy, or compliance dimension is in play, run the dimension against the resolved normative pack (or, in generic mode, against general norms with a clear generic marker).
- **Persona evidence pull** — When `personas` resolves, pull the relevant capsule excerpt (respecting retrieval mode) instead of paraphrasing the whole source.
- **Conflict resolution hook** — When two packs disagree on a decision-relevant point, hand off to `knowledge-conflict-resolution` or apply the precedence policy inline and record it.

# Activation Triggers

- Always: declare and attempt to resolve `strategic_framework`; run generic mode loudly if unsatisfied and the fallback permits.
- Use the overreach deep-check and treat `accessibility_guidelines` as required when the task is an `interface_change`, `content_decision`, or `customer_facing_experience`.
- Treat `operating_model` as required when the task is a `roadmap_decision` or `prioritization_decision`.
- Pull persona evidence when the `personas` slot resolves; otherwise mark the user-evidence claim as an assumption.
- Run the complexity audit when complexity is the pivotal factor in the verdict.
- Invoke the conflict resolution hook when resolved packs disagree.

# Expected Output

```yaml
feature_value_analysis:
  feature: <one-line description>
  mode: generic | knowledge_aware
  business_intent: <intent served; cite framework pack in knowledge-aware mode>
  lever:
    primary: acquisition | conversion | retention | expansion | cost_to_serve | risk_reduction
    rationale: <short>
  user_evidence:
    summary: <what the evidence says, or the assumption made>
    is_assumption: <bool>
  opportunity_alignment:
    serves: <opportunity / outcome, or "none">
    aligned: <bool>
  complexity:
    cost: low | medium | high
    drivers: [<...>]
  overreach_risk:
    compliance: none | possible | likely
    accessibility: none | possible | likely
    privacy: none | possible | likely
    notes: <short>
  verdict:
    worth_doing: yes | no | conditional
    conditions: [<...>]            # when conditional
    rationale: <short>
  knowledge_used:
    - slot: <slot-name>
      pack: <pack_id@version>
      retrieved_scope: capsule | excerpt | metadata | full
      restrictions: [<...>]
  unsatisfied_slots:
    - slot: <slot-name>
      fallback: <applied fallback>
  conflicts:
    - between: [<pack_id@version>, <pack_id@version>]
      prevailing: <pack_id@version>
      reason: source_precedence_policy
```

# Verification

- Every required slot is either satisfied or stopped per `fallback_behavior`; no silent generic fallback on a required slot.
- The output declares `mode`; generic-mode output carries no fabricated pack citations.
- Each consumed pack is cited as `pack_id@version`; knowledge-aware output without citations is invalid.
- No verbatim text from a `confidential` or higher source appears in the output, logs, or handoff.
- The verdict names exactly one primary lever and ties it to a stated business intent.
- Overreach dimensions that triggered a `required_when` slot were actually assessed against the resolved (or generically marked) norm.
- Conflicts, if any, name the prevailing pack and the precedence reason.

# Handoff Signals

- A `worth_doing: yes` verdict hands off to `feature-planning` for delivery shaping.
- An unmet required slot hands back to the requester with the exact authorization that would unlock knowledge-aware mode.
- A `likely` overreach risk on compliance, accessibility, or privacy routes to human review before commitment.
- Unresolved conflicts between mandatory and lower-tier sources escalate to human review; do not invent a compromise.
- Carry active restrictions forward; do not let capsule-only or no-export drop at the boundary.

# Pairs Well With

- `feature-planning`
- `knowledge-source-evaluation`
- `knowledge-conflict-resolution`
- `restricted-context-check`

# Anti-patterns

- Naming a specific framework, policy, or persona as a hard requirement instead of declaring a slot type.
- Inlining capsule or framework text into this skill or its templates.
- Producing a confident verdict in generic mode as if a governed source were present.
- Citing a pack in knowledge-aware mode without `pack_id@version`.
- Treating complexity as an automatic veto, or treating high value as license to overreach into compliance/accessibility/privacy.
- Resolving a mandatory-vs-lower-tier source conflict by splitting the difference.
