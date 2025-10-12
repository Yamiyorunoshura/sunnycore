# Context Package: conclude

## Task Information
- **Task Name**: conclude
- **Role**: Product Owner (sunnycore_po)
- **Description**: Project conclusion and completion report

## Required Context Files

### 1. Command
```
{root}/sunnycore/commands/sunnycore_po.md
```

### 2. Task
```
{root}/sunnycore/tasks/conclude.md
```

### 3. Template
```
{root}/sunnycore/templates/completion-report-tmpl.yaml
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
2. sunnycore_po.md (command-level guidance)
3. conclude.md (task-level guidance)
4. completion-report-tmpl.yaml (template structure)

## Usage
This package should be loaded when `docs/progress.md` indicates that `conclude` task is in progress.

