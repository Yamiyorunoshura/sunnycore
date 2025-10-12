# Context Package: document-project

## Task Information
- **Task Name**: document-project
- **Role**: Architect (sunnycore_architect)
- **Description**: Document project architecture and design

## Required Context Files

### 1. Command
```
{root}/sunnycore/commands/sunnycore_architect.md
```

### 2. Task
```
{root}/sunnycore/tasks/document-project.md
```

### 3. Template
```
None (No specific template for this task)
```

### 4. Core Guidance
```
{root}/sunnycore/CLAUDE.md
```

## Context Loading Instructions

When this task is in progress, the agent should:

1. **Read the command file** to understand the role and scope of work
2. **Read the task file** to understand the specific steps and DoD
3. **Read CLAUDE.md** for general guidance and execution rules

## Priority Order
1. CLAUDE.md (highest priority - general guidance)
2. sunnycore_architect.md (command-level guidance)
3. document-project.md (task-level guidance)

## Usage
This package should be loaded when `docs/progress.md` indicates that `document-project` task is in progress.

