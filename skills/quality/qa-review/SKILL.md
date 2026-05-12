---
name: qa-review
description: Audit the consistency of a change across behavior, validation, handoffs, and operational risk.
version: 0.1.0
owner: adaptive-skills
---

# Overview

Use this skill after a meaningful change or before sign-off when you need a systems view of quality rather than a file-by-file check.

# When to Use

- pre-release review
- cross-functional change review
- regression suspicion

# When NOT to Use

- as a replacement for direct implementation or test execution

# Core Moves

1. Check the intended path end to end.
2. Look for mismatches between layers or owners.
3. Classify operational risk and severity.
4. State whether the issue blocks progress.

# Optional Modules

- **Handoff audit** — Review whether boundary-crossing work left unresolved ownership behind.
- **Regression lens** — Focus on what likely broke around the changed path.
- **Evidence gap** — Name what is still unproven before closure.

# Activation Triggers

- Use handoff audit when more than one specialty touched the work.
- Use regression lens when shared dependencies changed.
- Use evidence gap when confidence is coming from intuition instead of proof.

# Expected Output

- quality findings
- severity
- block/no-block recommendation

# Verification

- The review checks system behavior, not only code artifacts.
- Severity is tied to user or operational impact.
- The recommendation is explicit.

# Handoff Signals

- A specific team or specialty must close a gap before release.
- The issue is not primarily QA but product, design, or architecture.

# Pairs Well With

- `testing`
- `communication`
- `triad-check`

# Anti-patterns

- Reporting issues with no severity or consequence.
- Using QA review as a substitute for proof.
- Calling something “fine” because no one looked closely enough.
