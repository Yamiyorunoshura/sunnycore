[Constraints]
1. Only execute commands explicitly defined in [Custom-Commands]; no unlisted operations are allowed.
2. When executing commands, fully follow the steps and checkpoints in the corresponding task files, without skipping or simplifying processes.
3. When user commands are unclear or do not match the defined formats, request clarification rather than making assumptions.
4. Read all files explicitly defined in the task [Input].
5. Follow the tool usage methods defined in [Tools] to assist task execution.
6. Comply with all constraints defined in [Constraints].
  6.1 If there are conflicts between [Constraints], handle them according to the following priority:
    - Highest priority: CLAUDE.md[Constraints]
    - Second highest priority: commands[Constraints]
    - Third highest priority: tasks[Constraints]
7. Complete all to-do items in the todo list.
8. Verify the completion of all [DoD].
9. Read and complete tasks based on the relevant guidelines stated in [xxx-Guidelines].

10. Wrap-Up Gatekeeper — do not wrap up before completion
  10.1 No “completion” claims with incomplete ToDos: as long as the todo list contains any non-completed status (including pending, in_progress, blocked), it is forbidden to output closure phrases such as “completed,” “wrap up,” or “write summary,” and forbidden to enter the “generate development notes/journal” flow.
  10.2 Only three legal end states:
    - completed: all ToDos are completed and all [DoD] have been verified.
    - blocked: there are external dependencies or permission/resource issues. Each item must be marked blocked with a specific blocking reason and an unblocking condition.
    - external-interrupt: interruption caused by platform/tool limits (such as time/quota/timeout). Do not claim completion; you must execute the “state persistence and resume plan” workflow (see 10.6).
  10.3 Validate before declaring completion: any operation that sets a ToDo to completed must first run its corresponding validation steps (tests, build, type checking, static scans, runnable artifacts, etc.) and include an “evidence summary” in the output (key commands and summarized results). No validation, no completed.
  10.4 Final check before wrap-up (fail-stop): before outputting any “summary, development notes, journal,” re-read the current ToDo status. If any item is not completed, immediately return to the next pending item and continue, instead of generating a summary.
  10.5 Strict adherence to task files and tool rules:
    - Use [Tool-Guidelines] todo-write to create and update the list. Freeform text is not allowed to masquerade as status changes.
    - Follow the task file’s steps and checkpoints exactly; do not skip or merge steps.
    - Read all files listed in task [Input] before taking action.
  10.6 On interruption: “state persistence and resume plan”
    - Mark all unfinished items as blocked and attach “current progress, remaining work, unblocking conditions, suggested next-step commands.”
    - Generate `docs/RESUME_PLAN.md` containing: remaining ToDos, corresponding validation commands, potential risks, and recommended execution order.
    - At the end of the output, provide immediately runnable resume instructions (for example, the relevant slash command or explicit next-step command).
  10.7 Consistency check (anti-grandstanding): it is forbidden to output statements inconsistent with actual status, such as “most tests are done” or “due to time I’ll summarize now.” If platform/tool limits are detected, describe the limits and switch to the 10.6 workflow.
  10.8 Priority extension:
    - Wrap-Up Gatekeeper belongs to CLAUDE.md[Constraints]. If it conflicts with other layers, per 6.1 this section still prevails.

[Wrap-Up-Gatekeeper_Guidelines]
1. ToDo state model
   - Allowed states: pending | in_progress | completed | blocked
   - Every state change must record “evidence or output summary,” for example the validation commands, key output fragments, and checkpoints.
2. Task loop (each iteration)
   - Read the current task file and ToDo status
   - Pick the next non-completed item and set it to in_progress
   - Execute steps and checkpoints from the task file; break into finer ToDos if needed
   - Validate (per DoD); if it passes mark completed; otherwise revert or mark blocked with reasons
   - Only when all ToDos are completed may you produce “summary and development notes”
3. Validation and evidence
   - Common validations (examples): `npm run test`, `npm run build`, type checks, lint, security/license scans, end-to-end checks
   - Include a concise output summary (for example, tests passed count, build result, key checkpoints)
4. Interruptions and quota guard
   - If a platform or tool’s time/quota/timeout risk is detected, immediately follow 10.6
   - It is forbidden to output “completed” or “let’s summarize first” while items are incomplete
5. Documentation and outputs
   - Only after “all ToDos completed and all DoD passed” may you write “development notes/journal/change summary”
   - Must include: the list of completed items, the evidence summary, residual risks (if any), and next-step suggestions (if the task group continues)

[Tool-Guidelines]
This section describes tool usage scenarios.

1. **todo_write — Task Tracking Tool**
  Purpose:
  - Create to-do lists to track task execution progress
  - Track completion status of multi-stage workflows

2. **sequentialthinking (MCP) — Structured Reasoning Tool**
  Purpose:
  - Conduct structured reasoning and verification
  - Analyze complex problems and design decisions
  - Assess task complexity and dependencies
  
  Reasoning step recommendations:
  - Simple tasks: 1–3 totalThoughts
  - Medium tasks: 3–5 totalThoughts
  - Complex tasks: 5–8 totalThoughts

3. **claude-context (MCP) — Codebase Semantic Search and Indexing Tool**
  Purpose:
  - Build a codebase index to support semantic search
  - Find relevant code snippets and implementation details
  - Process large files or file collections in segments
  
  Notes:
  - Always use search_code directly for codebase search
  - Only use index_codebase when the codebase has not yet been indexed
  - Check indexing status first before attempting to index

4. **context7 (MCP) — External Reference Tool**
  Purpose:
  - Obtain external package and architecture pattern references
  - Find domain-specific best practices
  - Retrieve the latest API documentation

5. **playwright_browser (MCP) — Web Browsing Tool**
  Purpose:
  - Conduct web research to obtain requirement examples
  - Reference industry standards or example requirements
  
  Notes:
  - Avoid including sensitive or proprietary information

[Template-Usage-Guidelines]
1. After filling in information according to the template, convert YAML format to Markdown format as follows:
    - 1st key -> Level 1 heading
    - 2nd key -> Level 2 heading
    - 3rd key -> Level 3 heading
    and so on.

[Summary-Instructions]
When performing auto-compact (automatic conversation compression), follow these rules:

1. Content that MUST be preserved:
  - [Constraints] All constraint conditions
  - [Tools] Tool definitions
  - [Output] Output format requirements
  - [DoD] Definition of Done
  - All [xxx-Guidelines] related guidelines
  - [Summary-Instructions] Summary instructions
  - [Path-Variables] Path variables

2. Content that MAY be compressed:
  - Task status information (progress, results, etc.)
  - May be summarized while retaining key information

3. Content that MAY be discarded:
  - Test results of completed tasks
  - Output content of completed tasks (for example, already written documents, code, etc.)