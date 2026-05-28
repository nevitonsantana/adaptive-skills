# Workflow — knowledge-source-evaluation

A short, repeatable pass to decide whether a candidate source can enter the registry.

---

## Step 1 — Capture the candidate

Collect, from the proposer:

- proposed `id` (kebab-case, unique in project/org)
- name
- a link to the source (or a description if the source is not yet a file)
- the proposer's intended use
- the proposed owner

If any of these is missing, stop and request them. Do not infer ownership.

---

## Step 2 — Classify type

Pick exactly one type from the source taxonomy:

`compliance_policy | security_policy | privacy_policy | accessibility_guideline | operating_model | product_strategy | proprietary_framework | design_system | persona | research_finding | benchmark | stakeholder_input`

If two types seem to fit, pick the higher-authority one. If neither fits, refuse and ask the proposer to reframe.

---

## Step 3 — Assess sensitivity

Ask:

- Could publication of this content harm the organization, a client, or a user?
- Is the content subject to legal, regulatory, or contractual restriction?
- Does the content contain identifiers, secrets, or strategic detail?

Map to one of: `public | internal | confidential | restricted | regulated`.
When uncertain, escalate one level.

---

## Step 4 — Assess authority

Pick the lowest authority that honestly describes the source. Persona is `evidence_proxy`, not `normative`. A proprietary framework is `interpretive`, not `mandatory`, unless backed by a corporate policy that already exists at higher authority.

---

## Step 5 — Define scope

List the task families and decisions this source should inform. Narrow scope is better than broad scope. If the proposer asks for "everywhere", refuse and ask for specific use cases.

---

## Step 6 — Decide retrieval mode

Default to `capsule_first` for any large or sensitive source. Use `excerpt_only` for policies. Use `full_source_allowed` only for `public` sources.

If `capsule_first` is chosen and no capsule exists, the candidate is not yet eligible for `register_governed`. Use the [framework-capsule-template](../../../templates/framework-capsule-template.md) to author one.

---

## Step 7 — Decide exposure policy

For each of `citation_required`, `full_text_exposure`, `export_allowed`:

- start from the sensitivity defaults
- tighten further if the proposer's intended use suggests external delivery

---

## Step 8 — Pick maturity recommendation

| Recommendation | Conditions |
|---|---|
| `register_minimal` | required identity fields present; no capsule; not eligible for required slots |
| `register_operational` | required fields + capsule present; bound to specific skills/agents |
| `register_governed` | operational + usage policy + audit fields + external reviewer sign-off |
| `refuse` | missing owner, ambiguous type, sensitive content without restrictions, or proposer asks to bypass controls |

---

## Step 9 — Record evaluation

Emit the structured output (see SKILL.md "Expected Output"). Attach it to the source's registry entry so future evaluators see prior reasoning.
