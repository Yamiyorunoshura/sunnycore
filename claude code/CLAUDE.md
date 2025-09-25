# Claude Agent Configuration

## Core Principles

### Task Execution Framework
- Complete all tasks by following the unordered list items under each working stage
- Maintain systematic approach to task completion with proper validation at each stage

### Environment Awareness & Adaptation
**Core Principle**: Agents must detect and adapt to the current execution environment before performing any operations

#### Environment Detection Requirements
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

## Task & Todo Management

### Tool Usage Restrictions
**Core Principle**: Agents must not use any mcp or todo-list tools unless explicitly specified by XML tags in the prompt

#### Conditional Tool Activation
- Tools may only be used when the corresponding XML tags are present in the task prompt
- Always verify tool permissions before attempting to use specialized tools

### Dynamic Todo List Management
**Core Principle**: Commands generate initial todo lists; tasks execute and dynamically update them based on actual development situations

#### Todo List Lifecycle
1. **Initial Creation**: Commands create structured todo lists using `todo_write` tool based on command type
2. **Dynamic Updates**: Tasks update todo status and add/modify items as development progresses
3. **Stage-Based Organization**: Todo items organized by workflow stages for better tracking
4. **Adaptive Management**: Adjust todo lists based on actual project complexities and discoveries

#### Todo List Update Strategies
- **Progress Tracking**: Mark items as "completed" immediately after finishing each task
- **Discovery-Based Addition**: Add new todo items when discovering additional requirements during execution
- **Complexity Adaptation**: Break down complex todo items into smaller, atomic tasks when needed
- **Context-Aware Updates**: Modify todo descriptions based on actual findings and decisions
- **Stage Synchronization**: Ensure todo items align with current workflow stage execution

#### Universal Todo Management Examples
```javascript
// Initial Command Creation (Stage-based structure)
[
  {"id": "stage-1-setup", "content": "Stage 1: 讀取並分析需求文檔", "status": "in_progress"},
  {"id": "stage-2-design", "content": "Stage 2: 設計系統架構", "status": "pending"},
  {"id": "stage-3-implement", "content": "Stage 3: 實作核心功能", "status": "pending"}
]

// Dynamic Updates During Task Execution
// When complexity is discovered:
[
  {"id": "stage-1-setup", "content": "Stage 1: 讀取並分析需求文檔", "status": "completed"},
  {"id": "stage-1-validation", "content": "Stage 1.1: 驗證需求完整性", "status": "in_progress"}, // Added
  {"id": "stage-2-design", "content": "Stage 2: 設計系統架構", "status": "pending"},
  {"id": "stage-2-database-design", "content": "Stage 2.1: 設計資料庫結構", "status": "pending"}, // Added
  {"id": "stage-3-implement", "content": "Stage 3: 實作核心功能", "status": "pending"}
]

// When tasks are completed or modified:
[
  {"id": "stage-1-setup", "content": "Stage 1: 讀取並分析需求文檔", "status": "completed"},
  {"id": "stage-1-validation", "content": "Stage 1.1: 驗證需求完整性", "status": "completed"},
  {"id": "stage-2-design", "content": "Stage 2: 設計系統架構", "status": "completed"},
  {"id": "stage-2-database-design", "content": "Stage 2.1: 設計資料庫結構", "status": "in_progress"},
  {"id": "stage-3-implement", "content": "Stage 3: 實作核心功能", "status": "pending"}
]
```

#### Situational Adaptations
- **Simple Projects**: Maintain original todo structure with minimal additions
- **Complex Projects**: Add detailed sub-tasks and cross-cutting concerns
- **Discovery-Driven**: Add new stages or modify existing ones based on findings
- **Error Recovery**: Add remediation tasks when issues are discovered
- **Integration Challenges**: Add specific integration and testing tasks as needed

#### Best Practices
- **Atomic Tasks**: Each todo item should be specific and achievable
- **Clear Descriptions**: Use descriptive content that indicates expected outcome
- **Stage Alignment**: Ensure todo items map to specific workflow stages
- **Status Consistency**: Update status immediately after task completion
- **Merge Strategy**: Always use `merge: true` when updating existing todo lists

### Execution Workflow
1. **Environment Awareness**: Detect and analyze current execution environment
2. **Context Validation**: Read and verify all input files
3. **Task Categorization**: Assign to appropriate agents based on domain expertise
4. **Environment-Adapted Execution**: Execute tasks using environment-appropriate tools and commands
5. **Collaborative Execution**: Parallel task execution with specialized agents
6. **Structured Output**: Generate standardized documentation using templates

## File Organization & Standards

### Project Structure
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
- **File names**: kebab-case, no spaces (avoid introducing new spaced naming)
- **Task IDs**: Correspond to file names, use hyphen separation
- **Agent IDs**: Short identifiers (dev, pm, po, qa)
- **Template IDs**: Descriptive names ending with `-tmpl`

### Code Standards & Formatting
- **Template-Driven**: Use standardized templates (`templates/` directory) to ensure document format consistency
- **Code Standards**:
  - Markdown: ATX headings (`#`), sentence-case titles, concise sections
  - YAML: 2-space indentation, kebab-case keys (e.g. `dev-subagent-list`)
  - Shell: POSIX-compatible bash, prefer functions + `set -e` for robustness
  - File/folder naming: kebab-case, no spaces

### Documentation Standards
- **Primary Language**: Traditional Chinese documentation and communication
- **Technical Terms**: Chinese-English correspondence for accuracy
- **Communication**: Professional standards with structured XML output

### Template Usage Guidelines

#### YAML to Markdown Conversion Rules
**Core Principle**: All template-based outputs must follow standardized YAML-to-Markdown conversion patterns for consistency across project documentation.

**Conversion Standards****:
- **YAML first-level keys** → **Markdown level 1 headings (#)**
- **YAML second-level keys** → **Markdown level 2 headings (##)**
- **YAML third-level keys** → **Markdown level 3 headings (###)**
- **YAML values (strings or numbers)** → **Markdown body text**

#### Template Application Guidelines
- **Consistent Structure**: All generated documents must adhere to template section ordering and hierarchy
- **Standardized Formatting**: Use ATX headings (`#`) and maintain proper indentation
- **Template Adherence**: Follow template field names and structure exactly as specified
- **Output Validation**: Ensure generated Markdown maintains readability and proper nesting

## Specialized Tools & Integrations

### Context7 Integration
**Use Cases**:
- create-architecture
- create-brownfield-architecture

**Purpose**: Fetch external package or API references by resolving IDs and retrieving focused excerpts.

**Invocation Flow**:
```json
{"name":"functions.context7__resolve-library-id","arguments":{"libraryName":"<package name>"}}
{"name":"functions.context7__get-library-docs","arguments":{"context7CompatibleLibraryID":"<resolved ID>","tokens":2000,"topic":"<optional topic>"}}
```
**Guidelines**: Use only when local files are insufficient, and cite key sources and conclusions in the final reply.

### Sequential Thinking Tool
**Use Cases**:
- brownfield-tasks
- create-architecture
- create-brownfield-architecture
- create-requirements
- create-tasks
- develop-tasks
- plan-tasks
- review

**Purpose**: Decompose complex tasks, record reasoning chains, and validate hypotheses.

**Invocation Flow**:
```json
{"name":"functions.sequential-thinking__sequentialthinking","arguments":{"thought":"<current reasoning>","thoughtNumber":1,"totalThoughts":3,"nextThoughtNeeded":true}}
```
**Guidelines**: When strategies change, adjust fields such as `isRevision` or `needsMoreThoughts` to keep the narrative coherent.

### Playwright Browser Automation
**Use Cases**:
- create-requirements

**Purpose**: Perform web interactions, gather online information, or simulate user flows.

**Invocation Flow**:
```json
{"name":"functions.playwright__browser_navigate","arguments":{"url":"https://example.com"}}
{"name":"functions.playwright__browser_click","arguments":{"element":"Submit button","ref":"<element ref>"}}
```
**Guidelines**: After execution, summarize the actions and retrieved data, explaining how they relate to the task.

### Claude Context Management
**Use Cases**:
- brownfield-tasks
- create-brownfield-architecture
- create-requirements
- develop-tasks
- plan-tasks
- review

**Purpose**: Load large documents or dialogue snippets in segments to preserve focus.

**Invocation Flow**:
```json
{"name":"functions.claude-context","arguments":{"source":"<source description>","focus":"<requested topic>"}}
```
**Guidelines**: Track which segments have been fetched across multiple requests to avoid duplication and minimize context load.

## Advanced Reading Strategies

### Partial Reading Strategy
**Core Principle**: Intelligently determine when to use partial reading to optimize context consumption and focus on relevant content sections.

### When to Use Partial Reading
- **Large Files (>500 lines)**: Always consider partial reading first
- **Specific Content Search**: When looking for particular sections, functions, or configurations  
- **Context Optimization**: When full file reading would exceed reasonable token limits
- **Iterative Analysis**: When building understanding incrementally through multiple focused reads

### Partial Reading Decision Framework
1. **File Size Assessment**: 
   - Small files (<100 lines): Read entire file
   - Medium files (100-500 lines): Consider context relevance
   - Large files (>500 lines): Default to partial reading unless specifically requested otherwise

2. **Content Type Analysis**:
   - Code files: Focus on specific functions, classes, or modules
   - Configuration files: Target specific sections or settings
   - Documentation: Read relevant sections based on current task
   - Log files: Read recent entries or specific time ranges

3. **Task Context Consideration**:
   - Debugging: Read around error locations (±20 lines)
   - Feature development: Focus on relevant modules/functions
   - Architecture review: Read headers, imports, and key structures
   - Configuration changes: Target specific config sections

### Partial Reading Techniques
```markdown
## Strategic Reading Patterns

### 1. Header-First Reading (Documentation/Code)
- Read first 50 lines to understand structure
- Read table of contents or import sections
- Then target specific sections based on findings

### 2. Function-Focused Reading (Code Files)
- Use grep to find function/class definitions first
- Read specific functions with context (±10 lines)
- Read import statements and dependencies

### 3. Configuration-Targeted Reading
- Read specific configuration sections
- Focus on changed or relevant settings
- Include related comments and examples

### 4. Error-Context Reading (Debugging)
- Read around specific line numbers (±20 lines)
- Include function definitions and variable declarations
- Read relevant imports and dependencies
```

### Partial Reading Implementation
```json
// Example: Reading specific function in large code file
{"name":"read_file","arguments":{"target_file":"large_file.py","offset":245,"limit":30}}

// Example: Reading configuration section  
{"name":"read_file","arguments":{"target_file":"config.yaml","offset":100,"limit":50}}

// Example: Reading file header for structure understanding
{"name":"read_file","arguments":{"target_file":"documentation.md","offset":1,"limit":100}}
```

### Adaptive Reading Strategy
- **First Pass**: Read file structure (headers, imports, TOC) - typically first 50-100 lines
- **Second Pass**: Based on first pass findings, read relevant sections using targeted offset/limit
- **Third Pass**: If needed, read additional context around identified areas of interest
- **Integration**: Combine insights from multiple partial reads to form complete understanding

### Context Preservation Techniques
- **Reference Tracking**: Note line numbers and section headers when making partial reads
- **Cross-Reference**: Link findings across different partial reads of the same file
- **Progressive Building**: Use each partial read to inform the next reading strategy
- **Summary Integration**: Maintain running summary of insights from multiple partial reads
