# Context Package: consult

## Task Information
- **Task Name**: consult
- **Role**: Assistant (sunnycore_assistant)
- **Description**: Provide consultation and guidance

## Required Context Files

### 1. Command
```
{root}/sunnycore/commands/sunnycore_assistant.md
```

### 2. Task
```
{root}/sunnycore/tasks/consult.md
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
2. sunnycore_assistant.md (command-level guidance)
3. consult.md (task-level guidance)

## Usage
This package should be loaded when `docs/progress.md` indicates that `consult` task is in progress.

