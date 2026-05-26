---
name: premortem
description: Assume a future failure has already happened and work backwards to identify probable causes, fragile assumptions, warning signals, and preventive adjustments before execution begins.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: planning
---

# Overview

Use this skill when a plan, product, decision, launch, strategy, or commitment carries a meaningful cost of failure and there is still time to adjust.

Unlike a checklist, premortem forces a reframe: the initiative has already failed. The question is not "what might go wrong?" but "why did this fail?" That shift reduces automatic optimism and surfaces causal, specific failure modes rather than vague risks.

The skill outputs failure modes, fragile assumptions, observable warning signals, recommended gates, and a revised plan — all before execution begins.

Depth is proportional to risk. See `workflows/depth-profiles.md` for Lite, Standard, and High-Assurance profiles.

# When to Use

- A concrete plan or decision exists.
- The cost of being wrong is meaningful.
- The direction can still be changed.
- There is relevant uncertainty about adoption, execution, dependencies, or value.
- Impact is on product, users, business, security, data, reputation, or governance.

Typical fits:
- product or feature launch
- strategy or positioning change
- AI/agent experiment with operational impact
- architectural decision that is hard to reverse
- process change affecting a team or customer
- multi-stakeholder plan where success is defined differently by different parties
- proposal with reputational risk

# When NOT to Use

- The task is a factual question, text edit, or simple feedback request.
- The plan is too vague to analyze — help shape the plan first.
- The decision is already made and irreversible — consider a retrospective instead.
- A simple checklist resolves the uncertainty faster.
- There is no concrete plan yet, only an idea.

# Core Moves

1. Confirm minimum context: what is the initiative, who is affected, what does success look like, what is the cost of failure, and is a course change still possible.
2. Select depth profile: Lite, Standard, or High-Assurance.
3. Frame the future failure explicitly: "X months have passed. This initiative failed. Explain why."
4. Generate specific, causal failure modes — not generic risks.
5. Identify the most probable failure, the most dangerous failure, and the failure hardest to detect.
6. Surface the key hidden assumption the plan is treating as true without sufficient evidence.
7. Define observable warning signals for the top failure modes.
8. Map findings to gates: hard gate, soft gate, review trigger, or human decision gate.
9. Revise the plan with concrete adjustments.
10. Produce a pre-execution checklist.

# Optional Modules

- **Matrix module** — rate each failure mode by severity, probability, and detectability. Use in High-Assurance when multiple stakeholders need a shared risk view.
- **Assumption stress-test** — for each hidden assumption, ask: what would it take for this to be wrong? Useful when the plan rests on a small number of load-bearing beliefs.
- **Signal log** — define which signals to monitor after execution starts, not only before. Keeps the premortem useful as a living document.
- **Rollback gate** — explicitly check whether a rollback path exists before execution. If it does not, this absence becomes a hard gate by default.

# Activation Triggers

- Use the matrix module when the plan has more than 6 failure modes or when risk severity varies widely across modes.
- Use assumption stress-test when the plan depends on a belief that cannot be verified before execution.
- Use signal log when the initiative will run for more than 4 weeks and early detection matters.
- Use rollback gate for any initiative involving AI autonomy, data mutation, or irreversible external action.

# Expected Output

Minimum output for every execution:

- failure modes (specific and causal)
- most probable failure
- most dangerous failure
- hidden assumption
- warning signals
- recommended gates (hard / soft / review trigger / human decision)
- revised plan
- pre-execution checklist

Full output for High-Assurance adds: failure-mode matrix, most difficult-to-detect failure, critical hidden assumptions, measurable warning signals, and a list of pending human decisions.

See `templates/premortem-report.md` for the output template.

# Verification

- Each failure mode is specific to this plan — not a generic risk that would apply to any project.
- Each failure mode has a causal explanation, not just a label.
- The hidden assumption is the one the plan most depends on without evidence.
- Warning signals are observable before or shortly after execution starts.
- Gates are connected to specific failure modes, not added as general caution.
- The revised plan is more actionable than the original plan.
- The pre-execution checklist can be acted on immediately.

# Handoff Signals

- A hard gate is identified — escalate to the responsible decision-maker before proceeding.
- The plan requires a human decision gate — structure the trade-offs and hand off to the appropriate person.
- High-Assurance profile was selected but context is insufficient — pause and gather missing information.
- The initiative has already started and course correction is no longer possible — switch to a postmortem or retrospective posture instead.

# Pairs Well With

- `checkpoint-review` — use premortem before starting; checkpoint-review during execution.
- `architecture-review` — premortem surfaces risk; architecture-review validates the technical path.
- `qa-review` — premortem identifies what to test; qa-review verifies execution.
- `feature-planning` — premortem stress-tests the feature brief before work begins.

# Anti-patterns

- Generating generic failure modes ("lack of communication", "low adoption") instead of causal, plan-specific ones.
- Running High-Assurance depth on every request — reserve it for decisions with high cost of error.
- Treating premortem output as a final risk register rather than input to a revised plan.
- Activating premortem for a simple feedback request or a decision that is already irreversible.
- Softening real risks to avoid delivering uncomfortable output.
