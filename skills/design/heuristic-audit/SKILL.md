---
name: heuristic-audit
description: Audit an existing interface for usability failures, operational impact, and minimum defensible fixes.
version: 0.1.0
owner: adaptive-skills
---

# Overview

Use this skill when the interface exists and you need a practical, prioritized read of what is breaking down.

# When to Use

- screen reviews
- existing flows with friction
- dashboard and workspace audits

# When NOT to Use

- choosing a new strategic direction before the interface exists

# Core Moves

1. Choose the review depth.
2. Identify a small set of meaningful findings.
3. Name the heuristic behind each issue.
4. Describe the operational impact.
5. Suggest the minimum defensible correction.

# Optional Modules

- **Severity pass** — Sort issues by operational harm rather than taste.
- **State coverage** — Check empty, loading, and failure states when the problem spans system feedback.
- **Accessibility lens** — Add focus, contrast, semantics, or assistive-tech checks when relevant.

# Activation Triggers

- Use severity pass when the list of issues is long.
- Use state coverage when dynamic states are central to the experience.
- Use accessibility lens when the interface is dense or high-risk.

# Expected Output

- prioritized findings
- heuristic mapping
- minimum fixes

# Verification

- Findings are concrete and observable.
- Each issue explains why it matters operationally.
- Recommendations do not balloon into a redesign without cause.

# Handoff Signals

- The next step is visual redesign or content work.
- A product or technical decision must change before UX can improve.

# Pairs Well With

- `ux-writing`
- `ux-strategy`

# Anti-patterns

- Using heuristics as a decorative checklist.
- Reporting style preferences as usability failures.
- Listing too many low-value findings.
