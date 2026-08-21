#!/usr/bin/env bash
# push.sh — Daily DSA streak helper
# Usage: push "your commit message"

set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

# ── 1. Require a commit message ────────────────────────────────────────────
if [[ -z "$1" ]]; then
  echo "❌  Please provide a commit message."
  echo "    Usage: push \"day 42: binary search\""
  exit 1
fi

MSG="$*"

# ── 2. Check for anything to commit ────────────────────────────────────────
if git diff --quiet && git diff --cached --quiet && \
   [[ -z "$(git ls-files --others --exclude-standard)" ]]; then
  echo "⚠️  Nothing to commit — working tree is clean."
  exit 0
fi

# ── 3. Stage, commit, push ─────────────────────────────────────────────────
git add -A
git commit -m "$MSG"
git push origin "$(git branch --show-current)"

# ── 4. Streak summary ──────────────────────────────────────────────────────
echo ""
echo "✅  Pushed: \"$MSG\""
echo ""

# Count unique days with commits (local log)
STREAK=$(git log --format="%ad" --date=short | sort -u | \
  awk -v today="$(date +%F)" '
    BEGIN { streak=0; prev="" }
    {
      if (NR==1 && $0 != today) exit
      if (prev == "") { streak=1; prev=$0; next }
      # check consecutive days
      cmd = "date -d \"" prev " -1 day\" +%F"
      cmd | getline yesterday; close(cmd)
      if ($0 == yesterday) { streak++; prev=$0 }
      else exit
    }
    END { print streak }
  ')

echo "🔥  Current streak: ${STREAK:-1} day(s)"
