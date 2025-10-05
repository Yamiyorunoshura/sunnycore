[General-Guidelines]
1. Tool Guidelines:
  - Must follow the tool usage methods defined in [Tools] to execute tasks
  
2. Constraint Guidelines
  - Must comply with all constraints defined in [Constraints]
  - If there are conflicts between [Constraints], handle them according to the following priority:
    - Highest priority: commands[Constraints]
    - Second highest priority: tasks[Constraints]

3. Task Guidelines
  - Must complete all to-do items
  - Must complete all [DoD]

[Template-Usage-Guidelines]
1. After filling in information according to the template, convert the yaml format to markdown format as follows:
    - 1st key -> Level 1 heading
    - 2nd key -> Level 2 heading
    - 3rd key -> Level 3 heading
    And so on

[Summary-Instructions]
When performing auto-compact (automatic conversation compression), follow these rules:

1. Content that MUST be preserved:
  - [Constraints] All constraint conditions
  - [Tools] Tool definitions
  - [Output] Output format requirements
  - [DoD] Definition of Done
  - All [xxx-Guidelines] related guidelines

2. Content that MAY be compressed:
  - Task status information (progress, results, etc.)
  - Can be summarized while retaining key information

3. Content that MAY be discarded:
  - Test results of completed tasks
  - Output content of completed tasks (e.g., already written documents, code, etc.)