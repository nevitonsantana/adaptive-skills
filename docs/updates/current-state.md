---
title: Current state
description: See the currently published Adaptive Skills inventory, supporting metadata, and maturity boundaries.
---

This page describes the repository state represented by current documentation and validation gates. Canonical files and automated validators take precedence if this summary drifts.

## Published capability surface

- **33 generic skills** under `skills/*/SKILL.md`.
- **3 domain-pack skills** in the crisis-management validation pack.
- Generic skills remain the reusable public capability library.
- Domain-pack skills remain validation cases rather than part of the generic inventory.

See the [complete skills catalog](https://nevitonsantana.github.io/adaptive-skills/getting-started/skill-catalog/) for task triggers and expected outcomes.

## Supporting metadata

The repository validates capability metadata, per-skill harness requirements where declared, governed knowledge dependencies, evolution records, and projection consistency.

These layers support discovery, compatibility, and governance. They do not replace canonical skill instructions or create an autonomous runtime.

## Consumption and AletheIA

Adaptive Skills can be consumed independently through a compatible harness. AletheIA integration remains optional:

- AletheIA owns macro Work Slice governance.
- Adaptive Skills owns reusable micro-execution methods.
- Consumer harnesses own local loading and runtime mechanics.

## Documentation state

The public Blume site provides progressive paths for beginners, practitioners, advanced readers, and maintainers. Manual GitHub Pages publication remains the current release process.

## Maturity boundaries

Current documentation does not claim autonomous orchestration, automatic routing authority, universal effectiveness from pilots, automatic promotion from observation, or an AletheIA dependency.

## How to verify

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_capabilities.py
python3 scripts/validate_harness_requirements.py
python3 scripts/validate_knowledge_deps.py
python3 scripts/validate_evolution.py
pnpm run docs:validate
```

## Next steps

- Browse [Cases and evidence](https://nevitonsantana.github.io/adaptive-skills/cases/) for bounded maturity records.
- Read [Changelog](https://nevitonsantana.github.io/adaptive-skills/updates/changelog/) for consumer-facing changes.
- Read [Updates and evolution](https://nevitonsantana.github.io/adaptive-skills/updates/) before interpreting roadmap material.
