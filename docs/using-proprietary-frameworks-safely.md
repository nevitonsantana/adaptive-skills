# Using Proprietary Frameworks Safely

## Goal

Explain how a skill can use a proprietary framework — strategic, design, or analytical — without copying it into the skill and without exposing it inappropriately at runtime.

The mechanism is: **capsule + manifest + dependency declaration**, governed by AletheIA's [Knowledge Governance Layer](https://github.com/nevitonsantana/AletheIA/blob/main/docs/concepts/knowledge-governance-layer.md).

---

## The three artifacts

1. **Knowledge pack manifest** — declares ownership, version, sensitivity, authority, scope, retrieval mode, and usage policy. Lives in the project / org, not in the skill. See [knowledge-pack-manifest](https://github.com/nevitonsantana/AletheIA/blob/main/docs/contracts/knowledge-pack-manifest.md).
2. **Framework capsule** — operational summary of the framework. The default surface a skill consumes. See [framework-capsules](https://github.com/nevitonsantana/AletheIA/blob/main/docs/concepts/framework-capsules.md).
3. **Skill knowledge dependency** — the skill says *"I need a strategic framework"*, not *"I need framework X"*. The resolver decides which pack satisfies the slot.

---

## Authoring path

1. Identify the framework you intend to use.
2. Confirm its owner. If you are not the owner, get authorization to capsule it.
3. Write a capsule that is **operational, not narrative**. Use the [framework-capsule-template](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/framework-capsule-template.md).
4. Write the manifest with sensitivity, authority, retrieval mode, and exposure rules.
5. In the skill, declare a knowledge dependency on the *type* (`proprietary_framework`, `product_strategy`, etc.), not on the pack id.
6. Choose a `preferred_retrieval_mode` of `capsule_first` unless there is a strong reason to consult the full source.
7. Ensure the skill operates in **generic mode** when no authorized pack is available.

---

## Capsule discipline

A capsule is small and operational. It does not include:

- the framework's full narrative
- proprietary diagrams that encode the framework's value
- examples drawn from real, identifiable engagements
- carve-outs that belong to one organization

If you find yourself paraphrasing the framework into the capsule, stop. The capsule is *how to use* the framework, not *what it is in detail*.

---

## Runtime posture

When a knowledge-aware skill runs:

- the resolver picks a pack that fills the slot
- the resolver returns the **capsule first** by default
- the skill reasons from the capsule
- the skill cites the pack `id@version` in its output
- the skill marks any restrictions active (no verbatim, no export, etc.)
- the skill writes audit entries per [knowledge-audit-log-spec](https://github.com/nevitonsantana/AletheIA/blob/main/docs/contracts/knowledge-audit-log-spec.md)

If the framework is `confidential` or higher, the skill must:

- not reproduce verbatim text
- not include the framework body in handoffs, logs, or traces
- escalate to human review if the deliverable is external

---

## What to do when there is no capsule

If a framework you want to use does not yet have a capsule:

1. Do **not** inline its content into the skill.
2. Do **not** paste it into a system prompt.
3. Either operate in **generic mode** with a clear marker, or pause and ask the framework owner to produce a capsule.

Skills must refuse to absorb un-encapsulated content as a shortcut.

---

## See also

- [skill-knowledge-boundaries.md](skill-knowledge-boundaries.md)
- [declaring-knowledge-dependencies.md](declaring-knowledge-dependencies.md)
- [framework-capsule-template](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/framework-capsule-template.md)
- [knowledge-aware-skill-template](https://github.com/nevitonsantana/adaptive-skills/blob/main/templates/knowledge-aware-skill-template.md)
