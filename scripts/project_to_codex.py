#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def registry_path() -> Path:
    return repo_root() / "projections" / "registry.json"


def load_registry() -> list[dict]:
    data = json.loads(registry_path().read_text())
    skills = data.get("skills", [])
    if not isinstance(skills, list):
        raise SystemExit("registry.json must contain a list in 'skills'")
    return skills


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text().splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta


def titleize(identifier: str) -> str:
    return " ".join(part.capitalize() for part in identifier.replace("_", "-").split("-"))


def fallback_prompt(target_name: str, description: str) -> str:
    base = description.rstrip(".") if description else "run the skill responsibly"
    return f"Use ${target_name} when the task matches {base[:1].lower() + base[1:]}."


def yaml_quote(value: str) -> str:
    return json.dumps(value)


def build_openai_yaml(skill: dict, description: str) -> str:
    projection = skill["codex_projection"]
    target_name = projection["target_name"]
    default_prompt = projection.get("default_prompt") or fallback_prompt(target_name, description)
    display_name = titleize(target_name)
    return "\n".join(
        [
            "interface:",
            f"  display_name: {yaml_quote(display_name)}",
            f"  short_description: {yaml_quote(description)}",
            f"  default_prompt: {yaml_quote(default_prompt)}",
            "policy:",
            "  allow_implicit_invocation: true",
            "",
        ]
    )


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def select_skills(skills: list[dict], skill_id: str | None, all_flag: bool) -> list[dict]:
    eligible = [s for s in skills if s.get("codex_projection", {}).get("enabled")]
    if skill_id:
        matches = [s for s in eligible if s.get("id") == skill_id]
        if not matches:
            raise SystemExit(f"skill '{skill_id}' not found or not enabled for Codex projection")
        return matches
    if all_flag:
        return eligible
    raise SystemExit("use --skill <id> or --all")


def compare_file(target: Path, expected: str) -> tuple[str, str]:
    if not target.exists():
        return ("missing", "target missing")
    actual = target.read_text()
    if actual == expected:
        return ("match", f"ok ({content_hash(actual)})")
    return ("drift", f"drift repo={content_hash(expected)} local={content_hash(actual)}")


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def bundle_files(source: Path) -> list[tuple[str, Path]]:
    """Every file in the skill directory except the top-level SKILL.md, as
    (relative posix path, absolute path). Ensures referenced sibling files —
    skill-knowledge-dependency.yaml, workflow.md, templates/, modules/ — are
    projected alongside SKILL.md rather than dropped."""
    source_dir = source.parent
    files: list[tuple[str, Path]] = []
    for path in sorted(source_dir.rglob("*")):
        if path.is_dir():
            continue
        rel = path.relative_to(source_dir).as_posix()
        if rel == "SKILL.md":
            continue
        files.append((rel, path))
    return files


def project_skill(skill: dict, codex_root: Path, dry_run: bool, check: bool) -> None:
    source = repo_root() / skill["source_path"]
    meta = parse_frontmatter(source)
    description = meta.get("description", "")
    projection = skill["codex_projection"]
    target_dir = codex_root / projection["target_name"]
    target_skill = target_dir / "SKILL.md"
    target_yaml = target_dir / "agents" / "openai.yaml"
    expected_skill = source.read_text()
    expected_yaml = build_openai_yaml(skill, description)

    # SKILL.md and the generated openai.yaml, then the rest of the skill bundle so
    # the projected skill is complete (declared knowledge dependencies, workflow,
    # templates) rather than a lone SKILL.md.
    targets: list[tuple[str, Path, str]] = [
        ("SKILL", target_skill, expected_skill),
        ("openai.yaml", target_yaml, expected_yaml),
    ]
    for rel, abspath in bundle_files(source):
        targets.append((rel, target_dir / rel, abspath.read_text()))

    if check:
        for label, target, expected in targets:
            status, detail = compare_file(target, expected)
            print(f"[{status}] {label}: {target}: {detail}")
        return

    for label, target, expected in targets:
        if dry_run:
            print(f"[dry-run] {label}: would write {target}")
            continue
        ensure_parent(target)
        target.write_text(expected)
        print(f"[written] {label}: wrote {target}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Project canon skills into a Codex skills directory")
    parser.add_argument("--skill", help="single skill id to project/check")
    parser.add_argument("--all", action="store_true", help="project/check every eligible skill")
    parser.add_argument("--dry-run", action="store_true", help="show actions without writing")
    parser.add_argument("--check", action="store_true", help="compare canon vs target without writing")
    parser.add_argument("--codex-root", help="override Codex skills root for smoke tests")
    args = parser.parse_args()

    all_flag = args.all or (args.check and not args.skill)
    skills = select_skills(load_registry(), args.skill, all_flag)
    codex_root = Path(args.codex_root) if args.codex_root else Path.home() / ".codex" / "skills"

    for skill in skills:
        print(f"== {skill['id']} ==")
        project_skill(skill, codex_root, args.dry_run, args.check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
