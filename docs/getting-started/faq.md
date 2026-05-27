# Adaptive Skills — FAQ

Answers to common questions from teams adopting Adaptive Skills for the first time.

---

## General

**What exactly is Adaptive Skills?**  
A portable library of micro-skills for AI-assisted work. Each skill is a small, structured execution aid that defines when to use it, what to do, and what a good output looks like. See [`overview.md`](overview.md) for the full description.

**How is Adaptive Skills different from just writing good prompts?**  
Skills are reusable, versioned, and governed. A prompt lives in a thread and disappears when the session ends. A skill lives in the library, can be installed in any project, evolves through a governed loop (observation → proposal → review), and is validated against a spec before every release. Skills also have explicit "when NOT to use" sections — something prompts rarely have.

**Does Adaptive Skills replace AletheIA?**  
No. AletheIA and Adaptive Skills operate at different layers. AletheIA governs how a project decides, validates, hands off, and learns. Adaptive Skills provides the specialist capabilities that execute within that governance. Use them together: AletheIA for the macro loop, Adaptive Skills for execution discipline. See [`docs/aletheia-integration.md`](../aletheia-integration.md).

**Can I use Adaptive Skills without AletheIA?**  
Yes. Install via APM and invoke skills in any Claude Code or Codex session. You get reusable execution discipline without the full governance layer.

**Does it require a specific agent or harness?**  
No. Skills are conformant with the [`agentskills.io`](https://agentskills.io/specification) spec, which means they work in any harness that reads that format. Claude Code is the primary reference target today; Codex projection is also supported. Other conformant harnesses should work without changes.

**What does "micro-skill" mean?**  
Small scope and single concern. A skill handles one dominant need — debugging, planning, handoff, review — not everything at once. This keeps skills practical: you can pick the smallest one that fits the task instead of loading a large all-purpose prompt.

---

## Choosing the right skill

**How do I know which skill to use?**  
Start from the dominant need of the task, not from the catalog. Ask: what could fail if we execute poorly? Is the main need planning, implementation, review, handoff, debugging, or risk reduction? Then find the skill that addresses that need.

If unsure, start with `workflow` — it frames any non-trivial task with explicit scope and proof before execution starts.

Full trigger signals and decision guidance: [`skill-catalog.md`](skill-catalog.md) and [`docs/how-to-use-a-skill.md`](../how-to-use-a-skill.md).

**What if no skill fits exactly?**  
Proceed without a skill. Do not force a skill that does not fit — a weak fit produces a worse output than working without one. If you notice a repeatable pattern that no skill covers, that is a candidate for a new skill via the evolution layer.

**Can I use multiple skills for the same task?**  
Yes. Several tasks benefit from a sequence — for example, `workflow` → `feature-planning` → `premortem` for starting a new feature. See the [composite flows](skill-catalog.md#composite-flows) in the catalog for common combinations.

**What is the difference between `workflow` and `feature-planning`?**  
`workflow` frames any task — it adds scope, proof, and a next step before execution starts. Use it for anything non-trivial.  
`feature-planning` goes further: it turns intent into a structured delivery plan with a smallest slice, explicit risks, and success criteria. Use it specifically when the work is a feature or functional change that needs staged delivery.

**When should I use `premortem`?**  
When the cost of failure is high and there is still time to adjust. Classic signals: a plan that feels confident but has many implicit assumptions; a launch with a hard deadline; a decision that would be expensive or embarrassing to reverse. The skill forces a reframe — assume failure already happened, then work backwards.

---

## Installation

**Do I need two commands like AletheIA does?**  
No. `apm install nevitonsantana/adaptive-skills` is sufficient. Skills are exactly the kind of primitive APM is built to deliver — they materialize directly without a second scaffold step. See [`installation-guide.md`](installation-guide.md).

**Should I install all skills or just a few?**  
For most teams, start with the recommended starter bundle (`workflow`, `feature-planning`, `testing`) and add skills as you encounter the need. Installing all 24 is fine — unused skills do not cause overhead. Choose per-skill install if you want explicit control over what is available in sessions.

**Do I need to reinstall when a teammate joins?**  
No — they run `apm install` from the committed `apm.lock.yaml` and get the same skill set. This is why committing the lockfile matters.

**Can I install in CI?**  
Yes. `apm install` is idempotent and reads from `apm.lock.yaml`. If your CI pipeline runs agent steps that use skills, add `apm install` as a setup step before those steps.

---

## Security and credentials

**Do skills read my code, environment variables, or credentials?**  
No. Skills are SKILL.md files — structured markdown with instructions and criteria. They do not execute code, make network requests, or read files. The agent reads the skill and applies its structure to the task in the session.

**Is it safe to commit installed skills to a public repository?**  
Yes. Skills contain no project-specific information — they are generic execution patterns from a public library. The only project-specific artifact is your `apm.lock.yaml`, which contains the package name, version, and hash — no credentials.

**What if I want to customize a skill for my project?**  
Do not edit the installed `SKILL.md` files directly — they will be overwritten on the next `apm update`. Instead, create project-local operating procedures in `ops/ai/skills/` (if using AletheIA) or in a separate `project-skills/` folder. Project-local skills override or complement library skills for domain-specific work.

---

## Environment

**Does Adaptive Skills work on Windows?**  
Yes. Skills are markdown files — platform-agnostic. The installation uses APM (Node.js-based), which supports Windows. For skill invocation in Claude Code, behavior is identical across platforms.

**What Node.js version does APM require?**  
Node.js ≥ 18. Run `node --version` to check. Adaptive Skills itself has no Node.js dependency — this is an APM requirement.

**Does it work offline after install?**  
Yes. Once installed, skills are local files. They do not make network requests during invocation. Only `apm install` and `apm update` require network access.

**What about Codex?**  
Adaptive Skills has first-class Codex projection support. Instead of APM install, use the projection script: `python3 scripts/project_to_codex.py --all`. See [`docs/codex-consumer-setup.md`](../codex-consumer-setup.md) for the full setup.

---

## Common errors and failure cases

**The agent runs through a skill but the output is low quality.**  
Two common causes: (1) The skill did not fit the task — check "When NOT to use" and consider whether a different skill is a better fit. (2) The agent treated the skill as a template to fill mechanically rather than as a thinking structure. Skills should guide judgment, not replace it. Prompt the agent: "Apply the core moves of `<skill>` to this specific task" rather than "run `<skill>`."

**The agent uses the skill but skips core moves.**  
Core moves are the invariant part of the skill. If an agent skips them, surface it explicitly: "You skipped the reproduction step from the debugging skill. Please reproduce the bug before proposing a fix." Agents sometimes collapse steps when they feel confident — the skill's value is precisely in enforcing the discipline.

**Invoking a skill slows the agent down without adding value.**  
The skill may be the wrong fit for this task complexity. `workflow` on a single-step task, or `premortem` on a low-stakes decision, adds ceremony without value. Use the "When NOT to use" section as a guide.

**Two people are using the same skill set but getting inconsistent outputs.**  
Skills define structure, not exact outputs — variation is expected. If critical outputs must be consistent (e.g., handoff format, closeout structure), add a project-local policy that specifies the output format and reference it in your `ops/ai/policies/` folder.

**A skill that worked in one project does not seem to work in another.**  
Check whether the harness is loading the installed skills. In Claude Code, skills in `.claude/skills/` are loaded automatically when starting from the project root. If you started the session from a subdirectory, skills may not be available — always start from the project root.

---

## Teamwork

**How does the team agree on which skills to use?**  
Start with the recommended starter bundle (`workflow`, `feature-planning`, `testing`). As the team works, note which tasks generated friction or inconsistent outputs — those are candidates for adding a skill. Document the team's skill conventions in a `ops/ai/policies/skills-policy.md` file.

**Can different team members use different skills for the same task type?**  
Yes, but with a cost: output consistency decreases when different people use different approaches. If a task type is recurring and shared (e.g., all PRs go through `qa-review`), standardize it in the policy file so the team converges.

**How do we contribute a skill back to the library?**  
Through the evolution layer: file an evolution proposal in `evolution/proposals/`. See [`docs/evolution-layer.md`](../evolution-layer.md) and [`CONTRIBUTING.md`](../../CONTRIBUTING.md) for the process. Proposals go through review before any change reaches the canon.

**Should we use the same `apm.lock.yaml` across all projects?**  
No — lockfiles are per-project. Each project pins the version it depends on. This is intentional: different projects can use different versions of the library without conflicts.

---

## OS-specific notes

| Topic | macOS | Linux | Windows |
|---|---|---|---|
| APM installation | `npm install -g @microsoft/apm` or via Homebrew | `npm install -g @microsoft/apm` | `npm install -g @microsoft/apm` or winget |
| Skill location (Claude Code) | `.claude/skills/` | `.claude/skills/` | `.claude\skills\` |
| Codex projection | `python3 scripts/project_to_codex.py --all` | same | `python scripts/project_to_codex.py --all` |
| Line endings | LF | LF | Configure `git config core.autocrlf input` to avoid diff noise in SKILL.md files |
| Validator | `pip install agentskills && agentskills validate .claude/skills/` | same | same (use `pip` or `pip3`) |

For harness-specific setup, see [`docs/claude-consumer-setup.md`](../claude-consumer-setup.md) (Claude Code) or [`docs/codex-consumer-setup.md`](../codex-consumer-setup.md) (Codex).
