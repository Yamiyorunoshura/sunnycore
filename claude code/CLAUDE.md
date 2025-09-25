# General rules

## Behaviour

### Task Execution
- You must complete the tasks by following the unordered list items under each working stage

### Environment Sensation & Awareness
**Core Principle**: Agents must detect and adapt to the current execution environment before performing any operations

#### Environment Detection
- **Virtual Environment Check**: Always detect if working within virtual environments (venv, conda, poetry, etc.)
- **Package Manager Detection**: Identify available package managers (pip, uv, poetry, npm, etc.)
- **Dependency Files**: Check for `requirements.txt`, `pyproject.toml`, `package.json`, etc.
- **Runtime Environment**: Detect Python version, Node.js version, or other runtime specifics

#### Adaptive Execution Strategy
- **Test Execution**: Use appropriate test runners and virtual environments:
  - Python: `python -m pytest` instead of direct `pytest`
  - Node.js: `npm test` or `yarn test` within project context
  - Virtual environments: Activate before running commands
- **Installation Commands**: Use project-appropriate package managers:
  - Prefer `uv` if `uv.lock` exists
  - Use `poetry` if `pyproject.toml` with poetry configuration exists
  - Fall back to `pip` for standard Python projects
- **Script Execution**: Consider execution context and dependencies

#### Environment-Aware Command Generation
```bash
# Good: Environment-aware
source venv/bin/activate && python -m pytest tests/
# or
uv run pytest tests/

# Bad: Direct execution without context
pytest tests/
```

#### Current Project Environment Guidelines
- **Primary Package Manager**: Use `uv` (detected via `uv.lock`)
- **Test Execution**: Use `uv run pytest` or `uv run python -m pytest`
- **Dependency Installation**: Use `uv add` or `uv sync`
- **Script Execution**: Prefer `uv run <command>` to ensure proper environment
- **Environment Activation**: Not required when using `uv run`

### Tool Usage Restrictions
**Core Principle**: Agents must not use any mcp or todo-list tools unless explicitly specified by XML tags in the prompt

#### Conditional Tool Activation
- Tools may only be used when the corresponding XML tags are present:

### Execution Mode
1. **Environment Awareness**: Detect and analyze current execution environment
2. **Context Validation**: Read and verify all input files
3. **Task Categorization**: Assign to appropriate agents based on domain expertise
4. **Environment-Adapted Execution**: Execute tasks using environment-appropriate tools and commands
5. **Collaborative Execution**: Parallel task execution with specialized agents
6. **Structured Output**: Generate standardized documentation using templates

### File Structure Specifications
```
{root}/
├── .claude/
|    ├── commands/        # Custom command definitions  
├── sunnycore/ 
    ├── tasks/           # Task execution workflows
    ├── templates/       # Standardized templates
    ├── scripts/         # Utility scripts
    └── CLAUDE.md        # Agent system configuration
```

### Naming Conventions
- File names: kebab-case, no spaces (avoid introducing new spaced naming)
- Task IDs: Correspond to file names, use hyphen separation
- Agent IDs: Short identifiers (dev, pm, po, qa)
- Template IDs: Descriptive names ending with `-tmpl`

## Output style

### Code-Style Oriented
- **Template-Driven**: Use standardized templates (`templates/` directory) to ensure document format consistency
- **Code Standards**:
  - Markdown: ATX headings (`#`), sentence-case titles, concise sections
  - YAML: 2-space indentation, kebab-case keys (e.g. `dev-subagent-list`)
  - Shell: POSIX-compatible bash, prefer functions + `set -e` for robustness
  - File/folder naming: kebab-case, no spaces

### Documentation Consistency
- Primary language: Traditional Chinese documentation and communication
- Technical terms: Chinese-English correspondence for accuracy
- Professional communication standards with structured XML output

# MCP tools introduction

## context7
- Situations:
    - create-architecture
    - create-brownfield-architecture
- Purpose: fetch external package or API references by resolving IDs and retrieving focused excerpts.
- Invocation flow:
```json
{"name":"functions.context7__resolve-library-id","arguments":{"libraryName":"<package name>"}}
{"name":"functions.context7__get-library-docs","arguments":{"context7CompatibleLibraryID":"<resolved ID>","tokens":2000,"topic":"<optional topic>"}}
```
- Use it only when local files are insufficient, and cite key sources and conclusions in the final reply.

## sequential-thinking
- Situations:
    - brownfield-tasks
    - create-architecture
    - create-brownfield-architecture
    - create-requirements
    - create-tasks
    - develop-tasks
    - plan-tasks
    - review
- Purpose: decompose complex tasks, record reasoning chains, and validate hypotheses.
- Invocation flow:
```json
{"name":"functions.sequential-thinking__sequentialthinking","arguments":{"thought":"<current reasoning>","thoughtNumber":1,"totalThoughts":3,"nextThoughtNeeded":true}}
```
- When strategies change, adjust fields such as `isRevision` or `needsMoreThoughts` to keep the narrative coherent.

## playwright
- Situations:
    - create-requirements
- Purpose: perform web interactions, gather online information, or simulate user flows.
- Invocation flow:
```json
{"name":"functions.playwright__browser_navigate","arguments":{"url":"https://example.com"}}
{"name":"functions.playwright__browser_click","arguments":{"element":"Submit button","ref":"<element ref>"}}
```
- After execution, summarise the actions and retrieved data, explaining how they relate to the task.

## claude-context
- Situations:
    - brownfield-tasks
    - create-brownfield-architecture
    - create-requirements
    - develop-tasks
    - plan-tasks
    - review
- Purpose: load large documents or dialogue snippets in segments to preserve focus.
- Invocation flow:
```json
{"name":"functions.claude-context","arguments":{"source":"<source description>","focus":"<requested topic>"}}
```
- Track which segments have been fetched across multiple requests to avoid duplication and minimise context load.
