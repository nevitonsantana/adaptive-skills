# Execution Plan — Engineering Skills Hardening Pack

Orchestrated, phase-by-phase plan. Each phase is self-contained and executable in a fresh chat. **Copy from the cited sources; do not invent structure.**

Repo root: `/Users/nevitonsantana/orchids-projects/adaptative-skills`
Source package: `~/Downloads/_Uteis/AI/AletheIA-Adaptative-Skills/Pacote_Engineering_Skills_Hardening_Pack/` (PRD `01_...md`, SDD `02_...md`, Prompt `03_...txt`, Guardrails `04_...md`).

---

## Phase 0 — Documentation Discovery (FACTS, already verified)

These are confirmed from the live repo, not assumed.

### Confirmed repo structure
- Target skills **all exist**: `skills/debugging/SKILL.md`, `skills/testing/SKILL.md`, `skills/architecture-review/SKILL.md`, `skills/feature-planning/SKILL.md`.
- `skills/domain-language-alignment/` **does NOT exist** (greenfield if created).
- `skills/feature-value-governance/` **exists** — this is the "Feature Value Governance Pack" the prompt says NOT to touch / conflict with. Keep `feature-planning` untouched this round.
- Templates live in `templates/` (flat files, e.g. `templates/complexity-scorecard.md`). Canonical skill template: `templates/skill/SKILL.template.md`.
- Examples live in `examples/engineering/` (e.g. `examples/engineering/new-feature-slice.md`). **The repo does NOT use `skills/<name>/examples/` subfolders** — ignore the SDD's suggested per-skill examples path; use `examples/engineering/`.
- Docs live in `docs/`; subdir `docs/reference-maps/` does NOT yet exist (create it). `docs/adr/` exists.
- Validators: `scripts/validate_skills.py`, `scripts/validate_evolution.py`, `scripts/report_projection_status.py`, `scripts/project_to_codex.py`.
- Projection registry: `projections/registry.json` (32 skills registered; `version: 1`).

### Allowed APIs / contracts (from `scripts/validate_skills.py`)
Every `skills/*/SKILL.md` MUST have:
- **Top-level frontmatter**: `name`, `description`.
- **Nested `metadata:`** (two-space indent): `version`, `owner`, `category`.
- **Exactly these 11 `#` sections** (all required, extra headings allowed):
  `Overview`, `When to Use`, `When NOT to Use`, `Core Moves`, `Optional Modules`, `Activation Triggers`, `Expected Output`, `Verification`, `Handoff Signals`, `Pairs Well With`, `Anti-patterns`.
- Frontmatter shape to COPY (from `skills/debugging/SKILL.md:1-8`):
  ```yaml
  ---
  name: debugging
  description: ...
  metadata:
    version: "0.1.0"
    owner: adaptive-skills
    category: engineering
  ---
  ```

### Anti-patterns the validator ENFORCES (forbidden substrings in any `skills/*/SKILL.md`)
`Crisis Monitor`, `AGENTS.md`, `CLAUDE.md`, `docs/PROJECT_STATE.md`, `/Users/`.
→ Never put absolute paths, `CLAUDE.md`, or case-study terms inside a SKILL.md. (Examples under `examples/` are NOT scanned, but keep them clean anyway.)

### Projection registry contract (`projections/registry.json`)
Each entry: `id`, `source_path`, `category`, `status`, `portability_tags[]`, `codex_projection{enabled,target_name,generate_openai_yaml,default_prompt}`, `claude_projection{enabled,mode,target_path}`. COPY the `debugging` entry (`projections/registry.json:68-88`) as the shape for any new skill. `validate_skills.py` fails if a registered `source_path` does not exist.

### Validation commands (confirmed to exist)
```bash
python3 scripts/validate_skills.py
python3 scripts/validate_evolution.py
python3 scripts/report_projection_status.py
python3 scripts/project_to_codex.py --all --dry-run
```

### Guardrails (from `04_Guardrails...md`)
Improve existing > create new. No copying mattpocock/skills text. No `skills.sh`, no Claude Code dependency, no new runtime/benchmark. Do NOT touch AletheIA, Knowledge Governance Layer, Feature Value Governance Pack. Do NOT weaken existing Verification/guardrails. Tool examples must always offer a generic fallback.

---

## Phase 1 — Reference Map + Pack Doc (docs only, lowest risk)

**What to implement (copy-based):**
1. Create `docs/reference-maps/` directory.
2. Create `docs/reference-maps/mattpocock-engineering-skills-map.md` — copy the table + section skeleton from SDD `02_...md:181-204` ("Reference map"). Sections: *Role of this reference*, *Candidate imports as concepts* (the decision table: adapt/defer/reject), *Justification*, *Adaptive Skills target*, *Risks*. Write ORIGINAL prose; cite mattpocock/skills as inspiration only, never authority.
3. Create `docs/engineering-skills-hardening-pack.md` — sections from PRD `01_...md:108-117` / Prompt `03_...txt:108-117`: *Objective, Problem, Principles, Scope, Non-scope, Skills impacted, Roadmap, Acceptance criteria, Validation*. Pull content from PRD §3, §5, §6, §13, §14.

**Documentation references:** SDD `02_...md:6` (decision table values), Guardrails `04_...md:42-52` (preferred decisions: diagnose→debugging adapt, tdd→testing adapt, module depth→architecture-review adapt, shared language→evaluate new skill, to-prd/to-issues/triage→defer, setup scripts→reject).

**Verification checklist:**
- `ls docs/reference-maps/mattpocock-engineering-skills-map.md docs/engineering-skills-hardening-pack.md` succeeds.
- `grep -ri "skills.sh\|install" docs/reference-maps/` returns nothing implying installation.
- No verbatim long quotes from the external repo (manual read).
- `python3 scripts/validate_skills.py` still passes (no skill touched yet).

**Anti-pattern guards:** Do not copy external skill bodies. Do not present the reference as a source of truth. Do not add new skills here.

---

## Phase 2 — Harden `debugging` (add Feedback loop construction module)

**What to implement (copy-based):** Edit `skills/debugging/SKILL.md` in place — APPEND, do not rewrite existing bullets.
1. Under existing `# Optional Modules`, add the bullet from SDD `02_...md:80-82`:
   `- **Feedback loop construction** — Build or identify a fast, deterministic, agent-runnable pass/fail signal before changing code. Prefer the smallest loop that reproduces the failure: focused failing test, CLI fixture, HTTP script, browser script, trace replay, throwaway harness, or property/fuzz loop.`
2. Under existing `# Activation Triggers`, add SDD `02_...md:86-88` trigger line.
3. Under existing `# Verification`, add the 3 checks from SDD `02_...md:92-96` WITHOUT removing the existing three.
4. Create `examples/engineering/feedback-loop-construction-example.md` — synthetic, non-proprietary; mirror style of `examples/engineering/new-feature-slice.md`.
5. Create `templates/feedback-loop-plan.md` — copy the exact 8 headings from SDD `02_...md:208-235` (Failure, Smallest reproducible signal, Loop type [list], How to run, Expected fail state, Expected pass state, Validation gaps, Recurrence guard).

**Documentation references:** SDD §5.1, §7; PRD §8.1 debugging; existing `skills/debugging/SKILL.md`.

**Verification checklist:**
- `grep -n "Feedback loop construction" skills/debugging/SKILL.md` → 1 hit.
- `grep -c '^# ' skills/debugging/SKILL.md` → still `11`.
- `grep -E "/Users/|CLAUDE.md|AGENTS.md|Crisis Monitor" skills/debugging/SKILL.md` → empty.
- `python3 scripts/validate_skills.py` passes.

**Anti-pattern guards:** No new `#` headings inside the skill. Keep original Verification bullets. Tool names (curl, pytest…) are examples with a generic fallback, never required.

---

## Phase 3 — Harden `testing` (Behavior-first + Vertical slice modules)

**What to implement (copy-based):** Edit `skills/testing/SKILL.md` (append only).
1. `# Optional Modules`: add `Behavior-first test design` (SDD `02_...md:104-106`) and `Vertical test slice` (SDD `02_...md:110-112`).
2. `# Activation Triggers`: add when-to-use lines (PRD §8.1 testing: vague-term, intermittent, refactor-coupling cases).
3. `# Verification`: append the 3 behavior-survives-refactor checks (SDD `02_...md:116-120`) without deleting existing ones.
4. Create `examples/engineering/behavior-first-test-example.md` (synthetic).
5. Create `templates/behavior-first-test-plan.md` — exact 7 headings from SDD `02_...md:239-255`.

**Documentation references:** SDD §5.2, §8; PRD §8.1 testing.

**Verification checklist:**
- `grep -n "Behavior-first test design\|Vertical test slice" skills/testing/SKILL.md` → 2 hits.
- `grep -c '^# ' skills/testing/SKILL.md` → still `11`.
- `python3 scripts/validate_skills.py` passes.

**Anti-pattern guards:** Don't prescribe a specific test framework. Don't couple modules to implementation-detail testing. Keep existing verification.

---

## Phase 4 — Harden `architecture-review` (Module depth review module)

**What to implement (copy-based):** Edit `skills/architecture-review/SKILL.md` (append only).
1. `# Optional Modules`: add `Module depth review` bullet (SDD `02_...md:128-130`).
2. Add the 5 checks (interface size vs hidden behavior, deletion test, locality, adapter reality, test surface) from SDD `02_...md:134-140` under `# Activation Triggers` or `# Verification`.
3. Create `examples/engineering/module-depth-review-example.md` (synthetic).
4. Create `templates/module-depth-review.md` — exact headings from SDD `02_...md:259-285` (Module/boundary, Interface, Implementation complexity hidden, Leverage, Locality, Deletion test, Adapter reality, Test surface, Recommendation [proceed/reduce/merge/split/escalate]).

**Documentation references:** SDD §5.3, §9; PRD §8.1 architecture-review (criteria list :100-108).

**Verification checklist:**
- `grep -n "Module depth review" skills/architecture-review/SKILL.md` → 1 hit.
- `grep -c '^# ' skills/architecture-review/SKILL.md` → still `11`.
- `python3 scripts/validate_skills.py` passes.

**Anti-pattern guards:** Don't recommend abstraction for aesthetics. Keep existing dependency/maintenance checks.

---

## Phase 5 — Decision: create or defer `domain-language-alignment`

**What to implement:** First, DECIDE explicitly (record the decision in `docs/reference-maps/mattpocock-engineering-skills-map.md` and the pack doc). Confirmed: no equivalent skill exists → recommend **create**.

If creating (copy-based):
1. Create `skills/domain-language-alignment/SKILL.md` by copying `templates/skill/SKILL.template.md` and the frontmatter shape from `skills/debugging/SKILL.md:1-8`. Use frontmatter from SDD `02_...md:148-157` but convert to the validator's nested `metadata:` form (`version`/`owner`/`category`). MUST contain all 11 required sections.
   - `# Core Moves`: 6 moves from SDD `02_...md:161-168`.
   - `# Expected Output`: list from SDD `02_...md:172-179`.
   - Fill `When to Use` from PRD §8.2 (before relevant implementation; vague/inconsistent terms; business-vs-code naming conflict; decisions needing ADR; presence of `CONTEXT.md`/`docs/adr/`).
   - Fill `Pairs Well With` and `Anti-patterns` (template requires them).
2. Add a registry entry to `projections/registry.json` by COPYING the `debugging` block (`projections/registry.json:68-88`), changing `id`, `source_path`, `target_name`, `default_prompt`. Keep `version: 1` at top; valid JSON.
3. Create `templates/domain-language-alignment-record.md` — exact headings from SDD `02_...md:289-308`.
4. Create `examples/engineering/domain-language-alignment-example.md` (synthetic).

**Documentation references:** SDD §5.4, §10; PRD §8.2; `templates/skill/SKILL.template.md`; `projections/registry.json:68-88`.

**Verification checklist:**
- `grep -c '^# ' skills/domain-language-alignment/SKILL.md` → `11`.
- `grep -E "/Users/|CLAUDE.md|AGENTS.md" skills/domain-language-alignment/SKILL.md` → empty.
- `python3 -c "import json;json.load(open('projections/registry.json'))"` → no error.
- `python3 scripts/validate_skills.py` passes (incl. registry source-exists check).

**Anti-pattern guards:** Do NOT add `feature-planning` changes (`vertical-slice-to-issues`) — defer to avoid Feature Value Governance Pack conflict; record as candidate only. Do not invent frontmatter keys outside `name/description/metadata.{version,owner,category}`.

---

## Phase 6 — Final Verification

**What to run (all must pass / be reviewed):**
```bash
cd /Users/nevitonsantana/orchids-projects/adaptative-skills
python3 scripts/validate_skills.py
python3 scripts/validate_evolution.py
python3 scripts/report_projection_status.py
python3 scripts/project_to_codex.py --all --dry-run
```

**Cross-phase checklist (maps back to each phase):**
- 11 sections intact in all 4 edited skills + new skill:
  `for s in debugging testing architecture-review feature-planning domain-language-alignment; do echo "$s: $(grep -c '^# ' skills/$s/SKILL.md 2>/dev/null)"; done` (each `11`).
- Forbidden patterns absent: `grep -rE "/Users/|CLAUDE.md|AGENTS.md|Crisis Monitor|docs/PROJECT_STATE.md" skills/` → empty.
- New module bullets present (Phases 2–4 greps above all hit).
- Templates created: `ls templates/feedback-loop-plan.md templates/behavior-first-test-plan.md templates/module-depth-review.md templates/domain-language-alignment-record.md`.
- Docs created: `ls docs/engineering-skills-hardening-pack.md docs/reference-maps/mattpocock-engineering-skills-map.md`.
- Examples created under `examples/engineering/` (4 files).
- `git status` shows ONLY: 4 skills, 1 new skill dir, `projections/registry.json`, 4 templates, 2 docs, 4 examples. **No changes** under AletheIA / knowledge-governance / feature-value-governance / evolution surfaces.
- Registry JSON valid and new skill's `source_path` exists.

**Anti-pattern guards (final sweep):**
- No external-repo verbatim copy (manual read of reference map).
- No `skills.sh` / Claude Code dependency / new runtime introduced (`grep -ri "skills.sh" . --include=*.md`).
- `feature-planning/SKILL.md` unchanged: `git diff --stat skills/feature-planning/SKILL.md` → empty.

---

## Out of scope (explicit)
- Editing AletheIA, Knowledge Governance Layer, Feature Value Governance Pack, Evolution Layer protected surfaces.
- `feature-planning` modifications (`vertical-slice-to-issues`) — deferred, recorded as candidate.
- Installing or vendoring `mattpocock/skills`.
- Per-skill `examples/` subfolders (repo uses `examples/engineering/`).

## Delivery report template (final answer)
1. Decisions taken (incl. domain-language-alignment create/defer).
2. Files created. 3. Files changed. 4. Deliberately out of scope. 5. Remaining risks. 6. Validation commands run + results. 7. Recommended next steps.
