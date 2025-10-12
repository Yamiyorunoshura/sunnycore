# Context Package: init

## Task Information
- **Task Name**: init
- **Role**: Developer (sunnycore_dev)
- **Description**: Initialize project setup

## Required Context Files

### 1. Command
```
{root}/sunnycore/commands/sunnycore_dev.md
```

### 2. Task
```
{root}/sunnycore/tasks/init.md
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
2. sunnycore_dev.md (command-level guidance)
3. init.md (task-level guidance)

## Usage
This package should be loaded when `docs/progress.md` indicates that `init` task is in progress.

