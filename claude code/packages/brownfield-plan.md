# Context Package: brownfield-plan

## Task Information
- **Task Name**: brownfield-plan
- **Role**: Developer (sunnycore_dev)
- **Description**: Re-develop plan that failed review based on review feedback

## Required Context Files

### 1. Command
```
{root}/sunnycore/commands/sunnycore_dev.md
```

### 2. Task
```
{root}/sunnycore/tasks/brownfield-plan.md
```

### 3. Template
```
{root}/sunnycore/templates/dev-notes-tmpl.yaml
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
2. sunnycore_dev.md (command-level guidance)
3. brownfield-plan.md (task-level guidance)
4. dev-notes-tmpl.yaml (template structure)

## Usage
This package should be loaded when `docs/progress.md` indicates that `brownfield-plan` task is in progress.

