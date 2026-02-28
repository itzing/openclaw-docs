# openclaw-docs

This repository aggregates OpenClaw documentation into a single master file for **NotebookLM** ingestion.

## What this repository does

- Documentation source: local OpenClaw `docs` directory
  - `/var/lib/openclaw/.npm-global/lib/node_modules/openclaw/docs`
- Builder script: `scripts/build-master-docs.py`
- Output file: `MASTER_DOCS.md`
- Excluded directories: `zh-cn` and `ja-jp`

During build, each markdown file from `docs` (including subfolders) is appended to `MASTER_DOCS.md` as a separate section with:
- a heading: `## <filename.md>`
- a source line: `_Source: <relative/path.md>_`

## OpenClaw version tracking

- The currently processed OpenClaw version is stored in `OPENCLAW_VERSION.txt`.
- This is used to detect when docs need to be rebuilt after OpenClaw updates.

## Weekly auto-refresh

Script: `scripts/weekly-refresh.sh`

Flow:
1. Read current `openclaw --version`.
2. Compare it with `OPENCLAW_VERSION.txt`.
3. If the current version is newer:
   - rebuild `MASTER_DOCS.md`,
   - update `OPENCLAW_VERSION.txt`,
   - commit changes,
   - push to `origin/main`.

Cron schedule (Monday, 12:00 UTC):

```cron
0 12 * * 1 /var/lib/openclaw/.openclaw/workspace/projects/openclaw-docs/scripts/weekly-refresh.sh >> /var/lib/openclaw/.openclaw/workspace/projects/openclaw-docs/weekly-refresh.log 2>&1
```

## Why this exists

The goal is to keep one up-to-date master documentation file that is easy to upload into **NotebookLM** for search, Q&A, and context-aware doc workflows.
