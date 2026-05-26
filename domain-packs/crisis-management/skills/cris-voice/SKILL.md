---
name: cris-voice
description: Review assistant tone, semantic safety, and fact-versus-inference boundaries for crisis-facing responses.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: crisis-management
---

# Overview

Use this skill when a crisis assistant response must be clear, careful, and trustworthy under high-interpretation conditions.

# When to Use

- assistant response review
- executive versus spokesperson mode tuning
- semantically sensitive crisis language

# When NOT to Use

- generic interface copy
- analysis work with no drafted response yet

# Core Moves

1. Confirm the response mode and audience.
2. Separate facts from inference and speculation when needed.
3. Adjust tone for consequence and sensitivity.
4. Remove language that sounds oracular or falsely certain.

# Optional Modules

- **Mode contrast** — Sharpen the difference between internal executive tone and external-facing tone.
- **Next action clarity** — Make the recommended next step explicit without overstating certainty.
- **Terminology simplification** — Reduce unnecessary jargon that could distort interpretation.

# Activation Triggers

- Use mode contrast when the same response could be read internally and externally.
- Use next action clarity when the response should support a decision.
- Use terminology simplification when expert language risks misread by the audience.

# Expected Output

- safer response framing
- clear mode alignment
- fact/inference hygiene

# Verification

- The response does not imply certainty it does not have.
- Mode and audience are explicit in the language.
- The response remains actionable without sounding absolute.

# Handoff Signals

- The next step is formal comms or stakeholder review.
- The response reveals a deeper analysis or monitoring gap.

# Pairs Well With

- `crisis-analyst`
- `ux-writing`
- `communication`

# Anti-patterns

- Using polish to hide uncertainty.
- Writing as if the assistant is an authority instead of an aid.
- Blending fact, interpretation, and action into one undifferentiated voice.
