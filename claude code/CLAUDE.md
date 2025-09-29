# Claude Agent Configuration

## 🔴 Critical Priority: Rule Hierarchy and Priority System
**Critical Principle**: When conflicting instructions or constraints are encountered, agents must apply the following strict priority order:

### Priority Level 1: CLAUDE.md Rules (Highest Authority)
- **Source**: All rules, principles, and configurations defined in `{root}/sunnycore/CLAUDE.md`
- **Scope**: System-wide policies, environment detection, task management, file organization standards
- **Authority**: Overrides all other constraints when conflicts arise
- **Examples**: Environment detection requirements, todo list management principles, naming conventions

### Priority Level 2: Command-Level Constraints (Medium Authority)  
- **Source**: `<constraints>` sections in `{root}/sunnycore/commands/*.md`
- **Scope**: Command-specific execution rules and behavioral requirements
- **Authority**: Applies within command execution context, subordinate to CLAUDE.md rules
- **Examples**: Workflow process requirements, milestone checkpoint rules, output generation standards

### Priority Level 3: Task-Level Constraints (Contextual Authority)
- **Source**: `<constraints>` sections in `{root}/sunnycore/tasks/*.md`  
- **Scope**: Task-specific implementation rules and technical requirements
- **Authority**: Applies within individual task execution, subordinate to both CLAUDE.md and command constraints
- **Examples**: TDD cycle requirements, file path specifications, template formatting rules

### Conflict Resolution Framework
```
IF (CLAUDE.md rule conflicts with Command constraint):
  → Apply CLAUDE.md rule, note deviation in execution log

IF (Command constraint conflicts with Task constraint):  
  → Apply Command constraint, document override decision

IF (Multiple constraints at same level conflict):
  → Apply most restrictive/safest option, escalate to user if ambiguous
```

### Priority Application Examples
1. **Environment Detection**: CLAUDE.md environment awareness rules override any task-specific environment assumptions
2. **Todo Management**: CLAUDE.md todo principles override command or task-level todo formatting preferences  
3. **File Naming**: CLAUDE.md kebab-case standard overrides task-specific naming suggestions
4. **Template Usage**: Command-level template requirements override task-specific template preferences

## 🔴 Critical Priority: XML Tag Framework Understanding

### Core Purpose
**Essential Knowledge**: All agents must understand the XML-based structured prompt framework used throughout this system. Each XML tag has specific meaning and requirements that must be followed precisely.

### Input/Output Tags (基礎組件)

#### `<input>` - Task Input Container
**Purpose**: Contains all required inputs for task execution
**Required Sub-tags**:
- `<context>` - Background information that must be specific and referenceable
- `<templates>` - List of templates to be used
- `<tasks>` - Task workflow steps (for commands only)
- `<rules>` - Rules and constraints

**Example**:
```xml
<input>
  <context>
  1. Current project architecture uses microservices
  2. Database: PostgreSQL 14.x
  3. Framework: Django 4.2
  </context>
  <templates>
  1. architecture-analysis-tmpl
  2. requirements-mapping-tmpl
  </templates>
</input>
```

#### `<output>` - Output Format Definition
**Purpose**: Defines machine-readable output structure
**Requirements**: Must be specific, verifiable, and structured
**Avoid**: Vague requirements like "provide a good summary"

**Example**:
```xml
<output>
1. JSON format: {"title": string, "summary": string, "priority": number}
2. Each section must be ≤ 200 words
3. Include exactly 3 actionable recommendations
</output>
```

### Quality Control Tags (進階組件)

#### `<constraints>` - Hard Constraints
**Purpose**: Non-negotiable limitations that must be enforced
**Requirements**: 3-5 verifiable rules using priority levels
**Priority Levels**: `MUST` > `SHOULD` > `MAY`

**Example**:
```xml
<constraints importance="Critical">
- MUST: Response length 100-300 words
- MUST: Include exactly 3 bullet points
- SHOULD: Use active voice (>80% of sentences)
- MAY: Include relevant code examples
</constraints>
```

#### `<questions>` - Self-Check Questions
**Purpose**: Critical questions for validation during task execution
**Requirements**: 2-3 high-value questions focusing on completeness, assumptions, and success criteria

**Example**:
```xml
<questions>
- Have I addressed all input requirements completely?
- What key assumptions am I making about the context?
- How will the success of this output be measured?
</questions>
```

#### `<checks>` - Quality Validation Checklist
**Purpose**: Observable, verifiable checkpoints for final validation
**Requirements**: 2-5 checkbox items that can be objectively verified
**Format**: Use `[ ]` checkbox format

**Example**:
```xml
<checks>
- [ ] Output contains exactly 3 sections
- [ ] All technical terms are defined
- [ ] Response length is within 200-400 words
- [ ] Includes at least one practical example
</checks>
```

### Special Function Tags

#### `<example>` - Practical Examples
**Purpose**: Provide concrete illustrations when needed
**Principle**: Minimal viable examples that clarify requirements
**Usage**: Include only when essential for understanding

#### `<tools>` - Required Tools List
**Purpose**: Specify tools needed for task completion
**Usage**: Only include when specific tools are required for the task

#### `<instructions>` - Complex Guidance Content
**Purpose**: Container for detailed instructions, rules, or reference materials
**Sub-tags Support**: Can include structured XML sub-tags like:
- `<review-standards>` / `<evaluation-criteria>` - Assessment standards
- `<quality-matrix>` / `<scoring-system>` - Quality/scoring systems
- `<decision-rules>` / `<approval-criteria>` - Decision-making rules
- `<reference-guide>` / `<best-practices>` - Reference materials

### Professional Role Tags

#### `<role name="Role Name">` - Professional Role Definition
**Purpose**: Define agent's professional identity and decision-making style
**Required Elements**:
- **名字** (Name): Professional title or domain
- **角色** (Role): Core responsibilities and decision scope  
- **人格特質** (Personality Traits): Only traits that affect decision-making style

**Example**:
```xml
<role name="Technical Architect">
名字：Senior Software Architect
角色：System design and technical decision-making with focus on scalability
人格特質：
- Detail-oriented with emphasis on long-term maintainability
- Evidence-based decision making
- Direct communication style with constructive feedback
</role>
```

### Workflow Management Tags

#### `<workflow importance="Priority Level">` - Process Structure
**Purpose**: Define 3-5 key stages of work execution
**Requirements**: Each stage must have clear deliverables and checkpoints
**Stage Format**: ID must follow pattern `{number}: {stage_name}`

**Example**:
```xml
<workflow importance="Important">
  <stage id="1: analysis">
  - Gather requirements from context
  - Identify key constraints and assumptions
  - Document current state analysis
  </stage>
  
  <stage id="2: design">
  - Create initial architecture structure
  - Define component interactions
  - Validate against constraints
  </stage>
</workflow>
```

#### `<stage id="Stage ID">` - Individual Workflow Stage
**Purpose**: Define specific work phase with concrete outputs
**ID Format**: `{number}: {descriptive_name}`
**Requirements**: Must include specific actions and expected outcomes

### Template-Specific Tags

#### `<start sequence>` - Command Initialization (Commands Only)
**Purpose**: Define initialization steps for command-type prompts
**Usage**: Only appears in commands template type

#### `<custom_commands>` - Interactive Commands (Commands Only)
**Purpose**: Define available sub-commands for interactive workflows
**Format**: Use `*{command_name}` followed by description

**Example**:
```xml
<custom_commands>
- *analyze
  - Perform detailed architectural analysis
- *recommend  
  - Generate actionable recommendations
- *validate
  - Validate current implementation against best practices
</custom_commands>
```

#### `<subagent-list>` - Agent Delegation (Tasks Only)
**Purpose**: List specialized agents that may be invoked during task execution
**Usage**: Only appears in tasks template type

### Tag Interpretation Guidelines

#### Importance Levels
- **Critical**: Must be handled immediately, system-breaking impact
- **Important**: Significant impact on overall quality and outcome
- **Normal**: Standard priority, execute according to plan
- **Optional**: Additional value when resources permit

#### Tag Processing Rules
1. **Mandatory Tags**: `<input>`, `<output>`, `<constraints>` must always be present
2. **Conditional Tags**: Some tags are template-specific (commands vs tasks vs agents)
3. **Nested Structure**: Respect parent-child relationships in XML hierarchy
4. **Attribute Processing**: Pay attention to tag attributes like `importance="Level"`

#### Common Anti-Patterns to Avoid
- **Ignoring constraints**: All `<constraints>` must be enforced strictly
- **Vague outputs**: `<output>` must specify concrete, measurable formats
- **Incomplete workflows**: Each `<stage>` must produce verifiable deliverables
- **Role confusion**: Stick to the defined `<role>` characteristics consistently

## 🔴 Critical Priority: Environment Awareness & Adaptation
**Core Principle**: Agents must detect and adapt to the current execution environment before performing any operations

### Environment Detection Requirements
- **Virtual Environment Check**: Always detect if working within virtual environments (venv, conda, poetry, etc.)
- **Package Manager Detection**: Identify available package managers (pip, uv, poetry, npm, etc.)
- **Dependency Files**: Check for `requirements.txt`, `pyproject.toml`, `package.json`, etc.
- **Runtime Environment**: Detect Python version, Node.js version, or other runtime specifics

### Adaptive Execution Strategy
- **Test Execution**: Use appropriate test runners and virtual environments:
  - Python: `python -m pytest` instead of direct `pytest`
  - Node.js: `npm test` or `yarn test` within project context
  - Virtual environments: Activate before running commands
- **Installation Commands**: Use project-appropriate package managers:
  - Prefer `uv` if `uv.lock` exists
  - Use `poetry` if `pyproject.toml` with poetry configuration exists
  - Fall back to `pip` for standard Python projects
- **Script Execution**: Consider execution context and dependencies

### Environment-Aware Command Generation
```bash
# Good: Environment-aware
source venv/bin/activate && python -m pytest tests/
# or
uv run pytest tests/

# Bad: Direct execution without context
pytest tests/
```

### Current Project Environment Guidelines
- **Primary Package Manager**: Use `uv` (detected via `uv.lock`)
- **Test Execution**: Use `uv run pytest` or `uv run python -m pytest`
- **Dependency Installation**: Use `uv add` or `uv sync`
- **Script Execution**: Prefer `uv run <command>` to ensure proper environment
- **Environment Activation**: Not required when using `uv run`

## 🔴 Critical Priority: Task & Todo Management

### Tool Usage Restrictions
**Core Principle**: Agents must not use any mcp or todo-list tools unless explicitly specified by XML tags in the prompt

#### Conditional Tool Activation
- Tools may only be used when the corresponding XML tags are present in the task prompt
- Always verify tool permissions before attempting to use specialized tools

### Dynamic Todo List Management
**Core Principle**: Commands generate initial todo lists; tasks execute and dynamically update them based on actual development situations

#### Critical Prerequisites
**MUST READ TASK FILES FIRST**: Before creating any todo lists, commands MUST read the corresponding task file (e.g., {root}/sunnycore/tasks/*.md) to understand the actual workflow stages and requirements. Todo lists MUST be based on ACTUAL stages from task files, not template examples.

#### Todo List Lifecycle
1. **Initial Creation**: Commands create structured todo lists using `todo_write` tool based on ACTUAL stages from corresponding task files
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
**IMPORTANT**: Examples below use variables to represent actual content from task files. Commands MUST read corresponding task files first to populate these variables.

```javascript
// Initial Command Creation (Stage-based structure)
[
  {"id": "stage-1-{task_stage_1}", "content": "Stage 1: {stage_1_description_from_task_file}", "status": "in_progress"},
  {"id": "stage-2-{task_stage_2}", "content": "Stage 2: {stage_2_description_from_task_file}", "status": "pending"},
  {"id": "stage-N-{task_stage_n}", "content": "Stage N: {final_stage_description_from_task_file}", "status": "pending"}
]

// Dynamic Updates During Task Execution
// When complexity is discovered:
[
  {"id": "stage-1-{task_stage_1}", "content": "Stage 1: {stage_1_description_from_task_file}", "status": "completed"},
  {"id": "stage-1-{discovered_substage}", "content": "Stage 1.1: {discovered_requirement_description}", "status": "in_progress"}, // Added
  {"id": "stage-2-{task_stage_2}", "content": "Stage 2: {stage_2_description_from_task_file}", "status": "pending"},
  {"id": "stage-2-{discovered_subtask}", "content": "Stage 2.1: {additional_task_discovered}", "status": "pending"}, // Added
  {"id": "stage-N-{task_stage_n}", "content": "Stage N: {final_stage_description_from_task_file}", "status": "pending"}
]

// When tasks are completed or modified:
[
  {"id": "stage-1-{task_stage_1}", "content": "Stage 1: {stage_1_description_from_task_file}", "status": "completed"},
  {"id": "stage-1-{discovered_substage}", "content": "Stage 1.1: {discovered_requirement_description}", "status": "completed"},
  {"id": "stage-2-{task_stage_2}", "content": "Stage 2: {stage_2_description_from_task_file}", "status": "completed"},
  {"id": "stage-2-{discovered_subtask}", "content": "Stage 2.1: {additional_task_discovered}", "status": "in_progress"},
  {"id": "stage-N-{task_stage_n}", "content": "Stage N: {final_stage_description_from_task_file}", "status": "pending"}
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

## 🟡 Important Priority: Task Execution Framework
- Complete all tasks by following the unordered list items under each working stage
- Maintain systematic approach to task completion with proper validation at each stage

### Execution Workflow
1. **Environment Awareness**: Detect and analyze current execution environment
2. **Context Validation**: Read and verify all input files
3. **Task Categorization**: Assign to appropriate agents based on domain expertise
4. **Environment-Adapted Execution**: Execute tasks using environment-appropriate tools and commands
5. **Collaborative Execution**: Parallel task execution with specialized agents
6. **Structured Output**: Generate standardized documentation using templates

## 🟡 Important Priority: File Organization & Standards

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

**Conversion Standards**:
- **YAML first-level keys** → **Markdown level 1 headings (#)**
- **YAML second-level keys** → **Markdown level 2 headings (##)**
- **YAML third-level keys** → **Markdown level 3 headings (###)**
- **YAML values (strings or numbers)** → **Markdown body text**

#### Template Application Guidelines
- **Consistent Structure**: All generated documents must adhere to template section ordering and hierarchy
- **Standardized Formatting**: Use ATX headings (`#`) and maintain proper indentation
- **Template Adherence**: Follow template field names and structure exactly as specified
- **Output Validation**: Ensure generated Markdown maintains readability and proper nesting

## 🟢 Normal Priority: Specialized Tools & Integrations

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

### Claude-Context
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

## ⚪ Optional Priority: Advanced Reading Strategies

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