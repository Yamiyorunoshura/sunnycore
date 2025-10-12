# Context Package: create-brownfield-architecture

## Task Information
- **Task Name**: create-brownfield-architecture
- **Role**: Architect (sunnycore_architect)
- **Description**: Create technical architecture documentation for Brownfield projects

## Required Context Files

### 1. Command
```
{root}/sunnycore/commands/sunnycore_architect.md
```

### 2. Task
```
{root}/sunnycore/tasks/create-brownfield-architecture.md
```

### 3. Template
```
{root}/sunnycore/templates/architecture-tmpl.yaml
```

### 4. Core Guidance
```
{root}/sunnycore/CLAUDE.md
```

## Context Loading Instructions

When this task is in progress, the agent should:

1. **Read the command file** to understand the role and scope of work
2. **Read the task file** to understand the specific steps and DoD
3. **Read the template file** to understand the output format requirements
4. **Read CLAUDE.md** for general guidance and execution rules

## Priority Order
1. CLAUDE.md (highest priority - general guidance)
2. sunnycore_architect.md (command-level guidance)
3. create-brownfield-architecture.md (task-level guidance)
4. architecture-tmpl.yaml (template structure)

## Usage
This package should be loaded when `docs/progress.md` indicates that `create-brownfield-architecture` task is in progress.

