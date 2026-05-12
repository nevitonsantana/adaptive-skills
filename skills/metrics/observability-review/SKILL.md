---
name: observability-review
description: Design or review metrics, events, alerts, and diagnostics so they support real decisions and expose real failure.
version: 0.1.0
owner: adaptive-skills
---

# Overview

Use this skill when the question is what to measure, how to interpret it, and how to avoid vanity or blind instrumentation.

# When to Use

- instrumentation planning
- health metrics
- alerts
- operational dashboards
- diagnostics

# When NOT to Use

- when there is no actual decision or operational risk behind the metric

# Core Moves

1. Name the decision the signal should support.
2. Choose the signal type and unit of analysis.
3. Define the minimum reading needed.
4. State owner, threshold, and action.

# Optional Modules

- **Coverage gaps** — Check whether silence could hide failure.
- **Incentive review** — Test whether the metric would drive harmful behavior.
- **Segmentation pass** — Break the signal by source, queue, user type, or time window when averages would hide degradation.

# Activation Triggers

- Use coverage gaps when the absence of data could be misread as stability.
- Use incentive review when the metric may influence team behavior.
- Use segmentation when aggregation can hide partial failure.

# Expected Output

- decision-linked metric or alert
- clear owner and cadence
- misread risk note

# Verification

- The signal has an action attached to it.
- The unit of analysis is explicit.
- The reading distinguishes health from value when needed.

# Handoff Signals

- Instrumentation depends on engineering changes by another owner.
- A policy or product decision is required before the metric can be finalized.

# Pairs Well With

- `feature-planning`
- `qa-review`
- `business-design`

# Anti-patterns

- Measuring what is easy instead of what is useful.
- Treating activity as value.
- Hiding partial degradation behind averages.
