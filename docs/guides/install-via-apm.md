# Install Adaptive Skills via APM

This guide covers installing the Adaptive Skills capability library through the [APM package manager](https://microsoft.github.io/apm/). Adaptive Skills ships as a flat APM **Skill Collection** — `skills/<name>/SKILL.md` — conformant with the [`agentskills.io`](https://agentskills.io/specification) specification. Each skill installs as an independent unit; you can install the whole library or pick individual skills.

## Prerequisites

- APM CLI installed. See [APM installation](https://microsoft.github.io/apm/getting-started/install/).
- A consumer project (any directory; APM operates on the current working directory).
- A target harness that consumes `<project>/skills/` — Claude Code is the reference target (`target: claude` in `apm.yml`). Other agentskills.io-conformant harnesses should work without changes, since Adaptive Skills emits the spec-conformant Skill Collection layout.

## Install the full library

```bash
apm install nevitonsantana/adaptive-skills
```

This resolves the package from GitHub, writes a lockfile, and promotes each `skills/<name>/` directory into your project's target skill location (for Claude, `.claude/skills/<name>/`).

After install, list what landed:

```bash
ls .claude/skills/
# api-design  architecture-review  business-design  checkpoint-review
# code-style  communication  debugging  design-system-intelligence
# domain-language-alignment  feature-complexity-audit  feature-planning
# feature-value-governance  handoff-summary  heuristic-audit
# intent-clarification  knowledge-conflict-resolution
# knowledge-source-evaluation  lean-implementation  observability-review
# opportunity-tree-alignment  premortem  qa-review  refactoring
# restricted-context-check  revenue-lever-mapping  sunset-decision
# task-chunking  testing  triad-check  ux-provocation  ux-strategy
# ux-writing  workflow
```

33 skills, one per directory, each with a `SKILL.md` entrypoint.

## Install a single skill

APM's Skill Collection layout supports per-skill selection. Use the `--skill` flag:

```bash
apm install nevitonsantana/adaptive-skills --skill debugging
```

You can repeat the flag to pick multiple skills:

```bash
apm install nevitonsantana/adaptive-skills --skill debugging --skill premortem --skill triad-check
```

The selection is persisted in your project's `apm.yml` and lockfile, so subsequent `apm install` runs (in CI or on teammates' machines) reproduce the same skill subset.

## What ships and what does not

| In the APM payload | Not in the APM payload |
|---|---|
| `skills/**` (all 33 skills) | `domain-packs/` (see below) |
| `apm.yml` | `evolution/` (meta-process, not capability) |
| `docs/skill-categories.md` | `projections/`, `capabilities/`, `templates/`, `examples/` |
| `docs/guides/install-via-apm.md` | `docs/concepts/`, `docs/_meta/`, internal docs |
| `docs/adr/ADR-004` + `ADR-005` | Engine/evolution scripts (`scripts/validate_evolution.py`, etc.) |
| `LICENSE`, `README.md` | |

The payload is the capability surface a consumer executes, not the governance and evolution machinery the library uses to maintain itself.

## Domain packs (`crisis-management`)

`domain-packs/crisis-management/` is the first validation case for the domain-pack pattern. It is **deliberately excluded** from the main APM package for v0.1.0 — domain packs are case studies, not canonical capability surface (see [ADR-002 — Domain agnosticism](../adr/ADR-002-domain-agnosticism/) and [Épico 2 of the cross-repo plan](../adr/ADR-005-apm-packaging-strategy/)).

If you want the crisis-management skills today, consume them via `git clone`:

```bash
git clone https://github.com/nevitonsantana/adaptive-skills.git
cp -R adaptive-skills/domain-packs/crisis-management/skills/* <your-project>/.claude/skills/
```

A future release may promote `crisis-management` to a separate APM package (`apm install nevitonsantana/adaptive-skills-crisis-pack`) if soft-launch demand justifies it.

## Verify the install

After `apm install`, you can validate the installed skills against the agentskills.io spec using the same reference validator the library's CI uses:

```bash
pip install 'skills-ref==0.1.0'
skills-ref validate .claude/skills/
```

All 33 skills should report conformant.

## Two-step caveat (vs. AletheIA)

If you have used [AletheIA's APM install](https://github.com/nevitonsantana/AletheIA/blob/main/docs/guides/install-via-apm.md), you know it requires a second step (`apm run scaffold-overlay`) because AletheIA is a project scaffold, not a capability primitive. **Adaptive Skills does not need that second step.** Skills are exactly the kind of primitive APM is built to deliver — `apm install` materializes them directly. There is no `apm run install-skills` equivalent and none is needed.

## Troubleshooting

- **`apm: command not found`** — APM CLI is not on your PATH. See [APM installation](https://microsoft.github.io/apm/getting-started/install/).
- **No `.claude/skills/` after install** — your harness target may not be `claude`. Inspect your project's `apm.yml` for the `target:` value and consult the [APM target reference](https://microsoft.github.io/apm/reference/targets/).
- **`skills-ref validate` fails on a skill** — open an issue at [adaptive-skills/issues](https://github.com/nevitonsantana/adaptive-skills/issues) with the skill name and the validator output. Library CI runs `skills-ref validate` against every PR, so this should never happen on `main`; if it does, it is a release regression.

## Related documents

- [ADR-004 — agentskills.io conformance strategy](../adr/ADR-004-agentskills-io-conformance/)
- [ADR-005 — APM packaging strategy](../adr/ADR-005-apm-packaging-strategy/)
- [`docs/skill-categories.md`](../skill-categories/) — category taxonomy and per-category backlog
- [`docs/how-to-use-a-skill.md`](../how-to-use-a-skill/) — invocation patterns once skills are installed
