# Context Package: create-plan

## Task Information
- **Task Name**: create-plan
- **Role**: Product Manager (sunnycore_pm)
- **Description**: Create detailed TDD implementation plans for all tasks in epic

## Required Context Files

### 1. Command
```
{root}/sunnycore/commands/sunnycore_pm.md
```

### 2. Task
```
{root}/sunnycore/tasks/create-plan.md
```

### 3. Template
```
{root}/sunnycore/templates/implementation-plan-tmpl.yaml
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
2. sunnycore_pm.md (command-level guidance)
3. create-plan.md (task-level guidance)
4. implementation-plan-tmpl.yaml (template structure)

## Usage
This package should be loaded when `docs/progress.md` indicates that `create-plan` task is in progress.

