#!/usr/bin/env bash
set -euo pipefail

# Install workflow/enforcement/templates into ~/.claude

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

CLAUDE_HOME="${HOME}/.claude"
CORE_SRC_ENF="${REPO_ROOT}/core/enforcement"
CORE_SRC_WF="${REPO_ROOT}/core/workflow"
CORE_SRC_TMPL="${REPO_ROOT}/core/templates"

mkdir -p "${CLAUDE_HOME}/core" "${CLAUDE_HOME}/workflow" "${CLAUDE_HOME}/templates"

echo "[info] Installing assets to ${CLAUDE_HOME}"

if [[ -d "${CORE_SRC_ENF}" ]]; then
  echo "[copy] enforcement -> ${CLAUDE_HOME}/core/"
  cp -R "${CORE_SRC_ENF}/." "${CLAUDE_HOME}/core/"
else
  echo "[warn] Missing directory: ${CORE_SRC_ENF}"
fi

if [[ -d "${CORE_SRC_WF}" ]]; then
  echo "[copy] workflow -> ${CLAUDE_HOME}/workflow/"
  cp -R "${CORE_SRC_WF}/." "${CLAUDE_HOME}/workflow/"
else
  echo "[warn] Missing directory: ${CORE_SRC_WF}"
fi

if [[ -d "${CORE_SRC_TMPL}" ]]; then
  echo "[copy] templates -> ${CLAUDE_HOME}/templates/"
  cp -R "${CORE_SRC_TMPL}/." "${CLAUDE_HOME}/templates/"
else
  echo "[warn] Missing directory: ${CORE_SRC_TMPL}"
fi

echo "[done] Assets installed."


