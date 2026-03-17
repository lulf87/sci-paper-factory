#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-02_public_data/raw/KiTS23}"
OUT_DIR="${2:-02_public_data/provenance}"

mkdir -p "$OUT_DIR"

find "$ROOT" -type f \
  ! -path "*/.git/*" \
  -print0 \
  | sort -z \
  | xargs -0 shasum -a 256 > "$OUT_DIR/KiTS23.sha256"

if command -v git >/dev/null 2>&1; then
  git -C "$ROOT" rev-parse HEAD > "$OUT_DIR/KiTS23.git_commit.txt" || true
  git -C "$ROOT" status --short > "$OUT_DIR/KiTS23.git_status.txt" || true
fi

echo "Wrote: $OUT_DIR/KiTS23.sha256"
echo "Wrote: $OUT_DIR/KiTS23.git_commit.txt (if git repo present)"
echo "Wrote: $OUT_DIR/KiTS23.git_status.txt (if git repo present)"
