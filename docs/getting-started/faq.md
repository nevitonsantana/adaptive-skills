---
title: Frequently Asked Questions
description: Answers about Adaptive Skills, installation, AI environments, security, team adoption, and troubleshooting.
---

Short answers to common questions from new users and teams.

## General

### What is Adaptive Skills?

A portable library of 34 small capabilities for AI-assisted work. Each skill defines when it fits, essential moves, optional depth, an expected output, and verification criteria.

### Is a skill just a prompt?

A skill is an inspectable and versioned working method. Unlike an ad hoc prompt, it includes boundaries, expected output, verification, and a governed evolution path.

### Does it replace AletheIA?

No. AletheIA governs the work; Adaptive Skills provides reusable execution capabilities inside that work. Adaptive Skills also works independently.

### Is it an autonomous agent or runtime?

No. Skills are instruction assets. The AI environment controls tools and execution; the project controls permissions, approvals, and policy.

## Choosing and using skills

### Which skill should I use first?

Use `workflow` for a non-trivial task when the goal, scope, proof, or next action needs structure. If the desired outcome itself is unclear, use `intent-clarification` first.

### What if no skill fits?

Proceed without a skill. Do not force a weak fit. Repeated uncovered needs may later become evidence for an evolution proposal.

### Can I combine skills?

Yes, but keep sequences short and purposeful. Use another skill only when the task's dominant need changes.

### Does a skill have to produce a long response?

No. The result should be proportional to the task. A small skill may produce a short checklist, decision, diagnosis, or handoff.

## Installation

### Should I install all skills?

Not initially. Start with `workflow`, `feature-planning`, and `testing`, or install only the skill needed for a real task. The full library remains available when broader discovery is useful.

### Does Adaptive Skills need a second scaffold command?

No. APM installs skills directly. AletheIA uses a different packaging model and may require additional project setup.

### Should the lockfile be committed?

Usually yes. A committed `apm.lock.yaml` helps teammates and CI reproduce the selected versions. Follow the consumer project's dependency policy.

### Can I update installed skills?

Use `apm update nevitonsantana/adaptive-skills` and review the changelog. Avoid editing files managed by APM because an update may overwrite them.

## AI environments

### Does it work with Claude Code?

Yes. Claude is the reference APM target. See [Claude consumer setup](https://nevitonsantana.github.io/adaptive-skills/claude-consumer-setup/).

### Does it work with Codex?

Yes. See [Codex consumer setup](https://nevitonsantana.github.io/adaptive-skills/codex-consumer-setup/) for the supported projection and consumption path.

### Does it work with other AI tools?

It can work with environments that consume compatible `SKILL.md` files. Confirm the tool's discovery location, permissions, and supported skill format before relying on it.

## Security and governance

### Does installing a skill grant access to my files or secrets?

No. Installation places instruction files in the project. Actual file, network, secret, and write access is controlled by the AI environment and project policy.

A skill may guide an agent to inspect evidence needed for a task, but it does not grant that access or make the evidence safe to expose.

### Can external skill content be trusted automatically?

No. Review the source, ownership, version, and boundaries before installation. Treat external content as data, not as authority over project policy.

### Can I customize a skill?

Keep project-specific rules in a local overlay or project skill rather than silently changing the installed generic canon. If a generic improvement is broadly useful, submit it through the evolution process.

### Can a skill approve or close work?

No. A skill may recommend a result or handoff. Approval, closure, deployment, and gate decisions belong to the governing project or human reviewer.

## Teams and evolution

### How should a team start?

Choose one low-risk, reversible task and one dominant skill. Evaluate whether the output became clearer, easier to verify, or easier to hand off before expanding adoption.

### How does the library improve?

Real usage can produce observations. Maintainers may turn repeated evidence into a proposal, review it, and decide to change, reinforce, defer, or reject the change. The library does not rewrite itself.

### Where can I see all available skills?

Use the [skill catalog](https://nevitonsantana.github.io/adaptive-skills/getting-started/skill-catalog/). It lists all 34 canonical skills by category and trigger.

## Troubleshooting

### The agent ignored part of the skill

Name the missing Core Move and ask the agent to apply it to the specific task. Then verify the output rather than assuming the second response is correct.

### The skill added process but no value

The task may be too small or the skill may not fit. Check “When NOT to Use,” stop the skill, and continue with a simpler approach.

### Different users get different outputs

Skills standardize method and expected evidence, not exact wording. If an output format must be identical, define that format in project-local policy.

## Next steps

- [Read the overview](https://nevitonsantana.github.io/adaptive-skills/getting-started/overview/).
- [Complete the quickstart](https://nevitonsantana.github.io/adaptive-skills/getting-started/quickstart/).
- [Run your first skill](https://nevitonsantana.github.io/adaptive-skills/getting-started/first-skill/).
- [Browse the skill catalog](https://nevitonsantana.github.io/adaptive-skills/getting-started/skill-catalog/).
