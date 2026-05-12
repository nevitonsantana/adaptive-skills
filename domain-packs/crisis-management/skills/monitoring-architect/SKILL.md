---
name: monitoring-architect
description: Design monitoring coverage as an operational sensing system with useful sources, tiers, keywords, noise filters, and readiness.
version: 0.1.0
owner: adaptive-skills
---

# Overview

Use this skill when the work is about building or reviewing crisis monitoring coverage, not interpreting the crisis itself.

# When to Use

- monitoring design
- source and tier planning
- coverage review
- noise reduction and readiness

# When NOT to Use

- pure crisis analysis
- generic analytics with no monitoring architecture question

# Core Moves

1. Define the decision the monitoring must support.
2. Choose the minimum sensing layers.
3. Shape keywords, exclusions, tiers, and source mix.
4. Review readiness and false confidence risks.

# Optional Modules

- **Source expansion** — Assess whether more sources improve decisions or only add noise.
- **Coverage risk** — Describe which blind spots remain even after the proposed setup.
- **Operational cadence** — Note how the setup should be reviewed or tuned over time.

# Activation Triggers

- Use source expansion when the request is to “monitor everything.”
- Use coverage risk when stakeholders may over-trust the setup.
- Use operational cadence when the monitoring will stay active for a while.

# Expected Output

- monitoring design
- coverage logic
- readiness note
- blind-spot note

# Verification

- The setup supports a real decision.
- Noise and coverage were both considered.
- Blind spots are explicit instead of hidden.

# Handoff Signals

- The next move is crisis analysis or implementation work.
- A product or data contract change is required to support the architecture.

# Pairs Well With

- `crisis-analyst`
- `feature-planning`

# Anti-patterns

- Treating source count as coverage quality.
- Designing monitoring with no decision in mind.
- Ignoring the cost of false confidence.
