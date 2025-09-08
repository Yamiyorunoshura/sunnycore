# Repository Guidelines

## Project Structure & Module Organization
- Root docs and scripts drive workflows; no compiled build.
- Key folders:
  - `claude code/` – agents, commands, config (`config.yaml`), scripts.
  - `codex/` – Codex-specific agents and tasks; see `codex/AGENTS.md`.
  - `warp code/` – Warp presets (agents, tasks).
  - `general/` – shared `config.yaml`, `scripts/`, `templates/`, `tasks/`.
  - Top-level: `README.md`, `install.command`, vocabulary and guides.

## Build, Test, and Development Commands
- `./install.command` – interactive setup (language, MCP/tool config, copies templates). Run from repo root.
- `bash general/scripts/shard-architecture.sh` – split `docs/architecture.md` into `docs/architecture/` files.
- `bash general/scripts/shard-requirements.sh` – split `docs/requirements.md` into structured parts.
- Syntax checks:
  - `bash -n path/to/script.sh` – shell syntax check.
  - Optional: run `tree docs/architecture` to verify generated files.

## Coding Style & Naming Conventions
- Markdown: use ATX headings (`#`), sentence-case titles, concise sections.
- YAML: 2-space indentation, kebab-case keys (e.g., `dev-subagent-list`).
- Shell: POSIX-compatible bash; prefer functions + `set -e` for robustness.
- File/folder names: kebab-case, no spaces (avoid introducing new spaced names).
- Keep configs minimal; co-locate examples near templates.

## Testing Guidelines
- Scripts: add a dry-run or clear log output; validate with `bash -n` and sample inputs.
- Docs/templates: ensure links and paths resolve; preview Markdown locally.
- Changes affecting `install.command`: test end-to-end in a fresh directory.

## Commit & Pull Request Guidelines
- Commits: clear, descriptive, imperative mood; Chinese or English acceptable. Group related changes.
  - Examples: `更新需求模板：統一非功能性需求格式` or `Add Codex install flow and templates`.
- PRs: include summary, scope (files/dirs touched), before/after examples or screenshots for docs, and any linked issues.
- For script changes: include sample command, expected output snippet, and rollback notes if applicable.

## Agent-Specific Instructions
- Add or modify agents under `claude code/agents/`, `codex/agents/`, or `warp code/agents/` as appropriate.
- Update `config.yaml` in the corresponding area to register new agents or task lists.
- For Codex-specific behavior, document usage in `codex/AGENTS.md` and reference from `README.md` if user-facing.

