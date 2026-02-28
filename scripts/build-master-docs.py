#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = Path('/var/lib/openclaw/.npm-global/lib/node_modules/openclaw/docs')
OUT_FILE = ROOT / 'MASTER_DOCS.md'

EXCLUDED_DIRS = {'zh-cn', 'ja-jp'}


def is_excluded(path: Path) -> bool:
    return any(part.lower() in EXCLUDED_DIRS for part in path.parts)


def collect_md_files(base: Path):
    files = []
    for p in base.rglob('*.md'):
        if not p.is_file():
            continue
        rel = p.relative_to(base)
        if is_excluded(rel):
            continue
        files.append(p)
    return sorted(files)


md_files = collect_md_files(DOCS_DIR)

with OUT_FILE.open('w', encoding='utf-8') as f:
    f.write('# OpenClaw Docs Master\n\n')
    f.write(f'Собрано из `{DOCS_DIR}`.\n\n')
    f.write('Исключены директории: `zh-cn`, `ja-jp`.\n\n')
    f.write(f'Всего файлов: **{len(md_files)}**.\n\n')

    for p in md_files:
        rel = p.relative_to(DOCS_DIR)
        f.write('---\n\n')
        f.write(f'## {p.name}\n\n')
        f.write(f'_Source: `{rel}`_\n\n')
        content = p.read_text(encoding='utf-8', errors='replace')
        f.write(content)
        if not content.endswith('\n'):
            f.write('\n')
        f.write('\n')

print(f'Wrote {OUT_FILE} with {len(md_files)} files')
