[Input]
  1. "{root}/docs/dev-notes/{task_id}-dev-notes.md" --Development notes (required)
  2. "{root}/docs/review-results/{task_id}-review.md" --Review report (required)
  3. "{root}/sunnycore/templates/completion-report-tmpl.yaml" --Completion report template (required)
  4. "{root}/docs/cutover.md" --Cutover report (required)
  5. "{root}/docs/cutover-fixes-dev-notes.md" --Cutover development notes (required)
  6. "{root}/docs/progress.md" --Progress record

[Output]
  1. Completion report: "{root}/docs/completion-report.md" (Markdown format)

[Constraints]
  1. Must ensure completion report complies with template requirements
  2. Completion report must include the following core content:
    (1) All key decisions and their rationale
    (2) Technology choices and alternative solution comparisons
    (3) Problems encountered, root cause analysis, and solutions
    (4) Future recommendations
    (5) DoD verification evidence (format as "file path:line number", e.g., "src/main.py:L42-L56")
  3. If required input files (dev-notes, review, template) are missing or incorrectly formatted, must generate a missing file list in the terminal and halt execution, waiting for user to provide supplementary files
  4. If any of the 5 core content items are completely missing from development notes or review report, should annotate "To be supplemented: missing XX item" in the corresponding chapter of the completion report and continue execution

[Tools]
  1. **todo_write**: Create and manage task list
    - [Step 1: Create todo list; Steps 2-7: Track task progress]
  2. **sequentialthinking (MCP)**: Perform structured reasoning and verification
    - [Step 2: Reasoning tasks for conceiving the report; Step 3: Verify if DoD is satisfied]
  3. **claude-context (MCP)**: Search codebase to locate implementation details
    - [Step 2: Find relevant code; Step 3: Precise keyword search]
    - Prerequisite: Codebase has been indexed through index_codebase
    - Failure handling: If not indexed or search fails, switch to grep tool for keyword search, or annotate "Unable to locate code evidence" and continue execution

[Steps]
  1. Input Validation Phase
    - Verify existence of all input files (dev-notes, review, template, requirements/*.md, tasks.md)
    - If required input files are missing (dev-notes, review, template), must generate a missing list in the terminal and halt execution; if optional files are missing (requirements, tasks.md), can mark and continue execution
    - Create todo list based on actual tasks

  2. Information Extraction Phase
    - Read development notes and review report
    - Extract the first 4 core content items from constraint 2 (key decisions and their rationale, technology choices and alternative solution comparisons, problems encountered and solutions, future recommendations)
    - If key information is missing, handle according to constraint 2

  3. Structure Mapping Phase
    - Read "completion-report-tmpl.yaml" to understand field structure
    - Map extracted information to template fields:
      * Key decisions and their rationale → development_summary.key_decisions
      * Technology choices and alternative solution comparisons → development_summary.technologies_used
      * Problems encountered and solutions → development_summary.challenges_encountered
      * Future recommendations → recommendations.future_improvements
      * DoD verification evidence → Verification results section at the end of the report
    - Use claude-context to search code to supplement implementation details (when the report mentions specific technical choices but does not annotate evidence in "file path:line number" format)

  4. Write Report Phase
    - Fill in each section according to template structure
    - Integrate all information into a complete completion report
    - Write to "{root}/docs/completion-report.md"

  5. Quality Check Phase
    - Verify report complies with template requirements (structure is complete)
    - Verify report content is complete (check item by item whether the 5 core content items required by constraint 2 are clearly presented in the report and annotate corresponding sections)
    - Check if all DoD verification evidence is included
    - If deficiencies are found, should return to Step 4 to fix the report (maximum 2 iterations, if still deficient then annotate "To be supplemented" and continue execution)

  6. DoD Verification Phase
    - Check all DoD items one by one to ensure they are met
    - Attach item-by-item DoD verification results at the end of the report
    - Confirm all todo items are completed

  7. File Archiving Phase
    - Verify existence of "requirements/", "epic.md" and "implementation-plan/"
    - Use terminal commands to move the above files to "{root}/docs/archive/{version_name}/" (if folder does not exist, create it first)
    - Suggested command: `mkdir -p "{root}/docs/archive/{version_name}" && mv -n {files} "{root}/docs/archive/{version_name}/"` (use -n parameter to avoid overwriting existing files)
    - If mv -n fails because files already exist, should record a warning and annotate "Files already exist in archive folder", DoD is considered complete
    - Execute verification command: `ls "{root}/docs/archive/{version_name}"` to confirm files exist in the target folder, if expected files are missing from the target folder, generate an error message and annotate DoD as incomplete, waiting for user to handle

[DoD]
  - [ ] Completion report has been generated and complies with template structure (including all necessary sections in the template)
  - [ ] Completion report content fully covers the 5 core content items listed in constraint 2
  - [ ] If "requirements/", "epic.md" and "implementation-plan/" exist, they have been safely moved to the archive folder; if they do not exist, this has been recorded in the report
  - [ ] All todo items are completed (including: input validation, information extraction, structure mapping, write report, quality check, DoD verification, file archiving)
