#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/../.. && pwd)"
cd "$ROOT_DIR"

# Load .env if present
if [[ -f .env ]]; then
  # shellcheck disable=SC1091
  source .env
fi

: "${PROMPTFOO_PROVIDER:=}"

CONFIG="general/tests/create-architecture/promptfoo.yaml"
ARTIFACT_DIR="artifacts/create-architecture"
mkdir -p "$ARTIFACT_DIR"

timestamp() { date +%Y%m%d-%H%M%S; }

RUN_LABEL="$(timestamp)"
OUT_JSON="$ARTIFACT_DIR/results-$RUN_LABEL.json"
OUT_TXT="$ARTIFACT_DIR/results-$RUN_LABEL.txt"

echo "Running create-architecture tests via promptfoo..."

CMD=(npx promptfoo eval -c "$CONFIG")
if [[ -n "$PROMPTFOO_PROVIDER" ]]; then
  CMD+=(--provider "$PROMPTFOO_PROVIDER")
fi

# Capture stdout to artifacts; also try to save JSON if supported
{"${CMD[@]}"} | tee "$OUT_TXT"

echo "Saved raw output to: $OUT_TXT"
echo "If JSON output is needed, re-run with:"
echo "  ${CMD[*]} --format json > $OUT_JSON"

