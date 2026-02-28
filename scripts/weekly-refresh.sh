#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/var/lib/openclaw/.openclaw/workspace/projects/openclaw-docs"
cd "$REPO_DIR"

current_version="$(openclaw --version)"
stored_version="$(cat OPENCLAW_VERSION.txt 2>/dev/null || echo 0.0.0)"

version_gt() {
  # returns 0 if $1 > $2
  [ "$(printf '%s\n%s\n' "$1" "$2" | sort -V | tail -n1)" = "$1" ] && [ "$1" != "$2" ]
}

if version_gt "$current_version" "$stored_version"; then
  python3 scripts/build-master-docs.py
  printf "%s\n" "$current_version" > OPENCLAW_VERSION.txt

  git config user.name "OpenClaw Assistant"
  git config user.email "assistant@openclaw.local"

  git add MASTER_DOCS.md OPENCLAW_VERSION.txt scripts/build-master-docs.py scripts/weekly-refresh.sh
  if ! git diff --cached --quiet; then
    git commit -m "docs: refresh master for OpenClaw ${current_version}"
    git push origin main
  fi
fi
