# Engineering Skills Hardening Pack

## Objective

Harden the existing engineering skills of Adaptive Skills so they are more executable, testable, and useful in real code work — without inflating the library or weakening governance. The external repository `mattpocock/skills` is used as inspiration and evidence of useful patterns, not as a normative source (see [`reference-maps/mattpocock-engineering-skills-map.md`](reference-maps/mattpocock-engineering-skills-map.md)).

## Problem

The engineering skills already have good governance and conceptual structure, but some remain too abstract to guide agents on concrete code tasks:

- `debugging` reproduces and isolates, but lacked an explicit module for building fast, deterministic feedback loops before changing code.
- `testing` calibrates minimal proof by risk, but did not explicitly steer toward behavior, public interfaces, and vertical slices.
- `architecture-review` evaluates dependencies and maintenance, but lacked concrete module-depth, locality, leverage, and deletion-test criteria.
- No transversal skill aligned domain language, living documentation, and ADRs before agents touch code or plan.

## Principles

1. Improve existing skills before creating new ones.
2. External references are inspiration and evidence, not authority.
3. A specific tool is an example, never a contract — always provide a generic fallback.
4. A feedback loop comes before any relevant code change.
5. Tests should prove behavior, not implementation.
6. Good architecture reduces complexity perceived by the interface's caller.
7. Domain language is part of operational architecture.

## Scope

- Add operational modules to `debugging`, `testing`, and `architecture-review`, preserving every existing Core Move, Verification, and guardrail.
- Create the transversal skill `domain-language-alignment` (capability confirmed absent and independent).
- Add four operational templates and one synthetic example per engineering front.
- Document how the external reference was used (reference map) without copying its content.

## Non-scope

- Copying content from `mattpocock/skills` or installing `skills.sh`.
- Creating a Claude Code dependency, a new runtime, or a benchmark engine.
- Modifying AletheIA, the Knowledge Governance Layer, the Feature Value Governance Pack, or protected Evolution Layer surfaces.
- Modifying `feature-planning` (the `vertical-slice-to-issues` idea is recorded as a deferred candidate to avoid overlap with the Feature Value Governance Pack).
- Adding many new skills or weakening existing verifications.

## Skills impacted

| Skill | Change | Type |
|---|---|---|
| `debugging` | `Feedback loop construction` module | hardened |
| `testing` | `Behavior-first test design` + `Vertical test slice` modules | hardened |
| `architecture-review` | `Module depth review` module | hardened |
| `domain-language-alignment` | new transversal skill | created |
| `feature-planning` | none (candidate deferred) | unchanged |

## Roadmap

- **Phase 1** — Reference map + this pack doc (docs only).
- **Phase 2** — Harden `debugging` + `feedback-loop-plan` template + example.
- **Phase 3** — Harden `testing` + `behavior-first-test-plan` template + example.
- **Phase 4** — Harden `architecture-review` + `module-depth-review` template + example.
- **Phase 5** — Create `domain-language-alignment` + registry entry + record template + example.
- **Phase 6** — Final validation.

## Acceptance criteria

- The repo contains an external reference map with no improperly copied content.
- `debugging`, `testing`, and `architecture-review` are evaluated and, where adequate, hardened — with all existing sections and guardrails intact.
- An explicit decision exists about creating `domain-language-alignment` (decision: create).
- Simple operational templates exist for each front.
- Examples are safe, synthetic, and non-proprietary.
- Existing repo validations still pass.
- No AletheIA, Knowledge Governance Layer, or Feature Value Governance Pack surface was changed without explicit authorization.

## Validation

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_evolution.py
python3 scripts/report_projection_status.py
python3 scripts/project_to_codex.py --all --dry-run
```

All four engineering `SKILL.md` files must keep their 11 required sections, and no `skills/*/SKILL.md` may contain forbidden generic references (`/Users/`, `CLAUDE.md`, `AGENTS.md`, case-study terms).
