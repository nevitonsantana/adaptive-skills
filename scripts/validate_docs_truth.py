#!/usr/bin/env python3
"""Validate public documentation claims against the canonical skill files."""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def skill_category(path: Path) -> str | None:
    text = path.read_text()
    match = re.search(r"^metadata:\s*$.*?^\s{2}category:\s*['\"]?([^\n'\"]+)", text, re.M | re.S)
    return match.group(1).strip() if match else None


def catalog_index_names(text: str) -> list[str]:
    index = text.split('## Skill details', 1)[0]
    return re.findall(r"^\| \[`([a-z0-9-]+)`\]\(#[a-z0-9-]+\) \|", index, re.M)


def catalog_detail_names(text: str) -> list[str]:
    details = text.split('## Skill details', 1)[1].split('## Composite flows', 1)[0]
    return re.findall(r'^### ([a-z0-9-]+)$', details, re.M)


def category_rosters(text: str) -> dict[str, set[str]]:
    rosters: dict[str, set[str]] = {}
    sections = re.split(r'^## ', text, flags=re.M)[1:]
    for section in sections:
        name, _, body = section.partition('\n')
        published = re.search(r'^- \*\*Published:\*\* (.+)$', body, re.M)
        if published:
            rosters[name.strip()] = set(re.findall(r'`([a-z0-9-]+)`', published.group(1)))
    return rosters


def main() -> int:
    root = repo_root()
    skills: dict[str, str] = {}
    errors: list[str] = []

    for path in sorted(root.glob('skills/*/SKILL.md')):
        category = skill_category(path)
        if not category:
            errors.append(f'{path.relative_to(root)}: missing metadata.category')
            continue
        skills[path.parent.name] = category

    catalog_path = root / 'docs/getting-started/skill-catalog.md'
    catalog_names = catalog_index_names(catalog_path.read_text())
    duplicates = sorted(name for name, count in Counter(catalog_names).items() if count > 1)
    if duplicates:
        errors.append(f'catalog index contains duplicate skills: {", ".join(duplicates)}')
    missing = sorted(set(skills) - set(catalog_names))
    unknown = sorted(set(catalog_names) - set(skills))
    if missing:
        errors.append(f'catalog index is missing skills: {", ".join(missing)}')
    if unknown:
        errors.append(f'catalog index contains unknown skills: {", ".join(unknown)}')

    detail_names = catalog_detail_names(catalog_path.read_text())
    detail_duplicates = sorted(name for name, count in Counter(detail_names).items() if count > 1)
    if detail_duplicates:
        errors.append(f'catalog details contain duplicate skills: {", ".join(detail_duplicates)}')
    detail_missing = sorted(set(skills) - set(detail_names))
    detail_unknown = sorted(set(detail_names) - set(skills))
    if detail_missing:
        errors.append(f'catalog details are missing skills: {", ".join(detail_missing)}')
    if detail_unknown:
        errors.append(f'catalog details contain unknown skills: {", ".join(detail_unknown)}')

    canonical_by_category: dict[str, set[str]] = defaultdict(set)
    for name, category in skills.items():
        canonical_by_category[category].add(name)

    category_path = root / 'docs/skill-categories.md'
    documented_by_category = category_rosters(category_path.read_text())
    for category in sorted(set(canonical_by_category) | set(documented_by_category)):
        canonical = canonical_by_category.get(category, set())
        documented = documented_by_category.get(category, set())
        if canonical != documented:
            missing_names = sorted(canonical - documented)
            unknown_names = sorted(documented - canonical)
            detail: list[str] = []
            if missing_names:
                detail.append(f'missing {", ".join(missing_names)}')
            if unknown_names:
                detail.append(f'unknown {", ".join(unknown_names)}')
            errors.append(f'category {category}: {"; ".join(detail)}')

    if errors:
        print('Documentation truth validation failed:')
        for error in errors:
            print(f'- {error}')
        return 1

    print(f'Validated public catalog and category coverage for {len(skills)} canonical skills.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
