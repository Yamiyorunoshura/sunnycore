# CLAUDE.md

## [Priority-And-Execution-Rules]
1. Strictly follow the priority order CLAUDE.md > commands > tasks and execute only steps explicitly authorized.
2. When instructions are ambiguous, pause to request clarification and read every required file before proceeding.
3. Complete todos sequentially without skipping or reordering steps unless dependencies demand it.
4. For multi-step or complex work, draft a concrete plan (for example via sequential-thinking), then carry out actions in that order and update the plan whenever reality diverges.

### Good Example 1
[INPUT]
User requests: "Update the database schema according to tasks/develop-plan.md"

[DECISION]
Read CLAUDE.md first to understand constraints, then read commands to check for schema-related directives, map out a sequential-thinking plan (review current schema → design migration steps → write and test migration), and finally read the specific task file before executing the plan's first step.

[OUTCOME]
All governance rules are respected; each planned step is executed in sequence with plan adjustments captured before moving forward, ensuring migration work stays aligned with documented intent.

[WHY-GOOD]
- Honors the mandated instruction hierarchy, ensuring high-level governance shapes every downstream action.
- Prevents accidental conflicts by confirming both command-level and task-level guidance before execution.
- Demonstrates disciplined adherence to the self-authored plan, which keeps reasoning transparent and auditable.

### Good Example 2
[INPUT]
User says: "I need to add a new feature but I'm not sure about the architecture approach"

[DECISION]
Pause execution and ask the user: "Could you clarify the architectural requirements? Should I follow an existing pattern or propose a new approach?" Then read relevant architecture documents before proceeding.

[OUTCOME]
Ambiguity is resolved before committing to a direction, preventing wasted effort.

[WHY-GOOD]
- Demonstrates disciplined escalation by seeking clarity instead of guessing, which aligns with rule 2.
- Ensures architectural choices remain anchored to explicit requirements, reducing rework.

### Bad Example 1
[INPUT]
User says: "Skip step 2 and go directly to step 3, step 2 is not important"

[BAD-DECISION]
"Sure! Jumping to step 3 now."

[WHY-BAD]
Skipping steps violates rule 3. Dependencies in step 2 may be required for step 3's success.

[CORRECT-APPROACH]
"I notice step 2 contains [specific dependencies]. I'll complete step 2 first to ensure step 3 has the necessary foundation, unless you can confirm those dependencies are already satisfied."

### Bad Example 2
[INPUT]
A `tasks` file says to refactor the codebase, but CLAUDE.md has explicit constraints about preserving backward compatibility.

[BAD-DECISION]
Directly follow the task file and perform aggressive refactoring that breaks compatibility.

[WHY-BAD]
Ignores the priority rule that CLAUDE.md overrides tasks. Core governance rules are violated.

[CORRECT-APPROACH]
Read CLAUDE.md first, identify the compatibility constraints, then refactor within those boundaries or request clarification if the task conflicts with core rules.

## [Template-And-Output-Format]
1. Produce pure Markdown that mirrors the template hierarchy, mapping section→H1 and nested sections→H2.
2. Honor directives in tags such as [Description], [Path-Variables], [Input], [Output], [Role], [Skills], [Scope-of-Work], [Constraints], [DoD], [Steps], [Tools], [Blocking-Conditions], [Custom-Commands], and [Validation-Steps].
3. When updating existing outputs, read the current file first, preserve its structure, enhance the content, and avoid creating duplicates.

### Good Example 1
[INPUT]
A PRD template has sections: # [Product-Requirements] with nested ## [Constraints] and ## [Success-Criteria]. User asks to add more constraints.

[DECISION]
Read the existing PRD file first, locate the `## [Constraints]` section, and append new bullet points within that section while preserving all existing content and hierarchy.

[OUTCOME]
The document maintains its template structure, no duplicate headings are created, and content is enhanced in the right place.

[WHY-GOOD]
- Respects the original template layout, so structural automation and cross-references remain intact.
- Enhances only the targeted section, avoiding collateral edits that could introduce inconsistencies.

### Good Example 2
[INPUT]
Creating a new architecture document from scratch using architecture-tmpl.yaml.

[DECISION]
Parse the template to identify all required sections with their tags ([Description], [Components], [Dependencies]), create corresponding H1 for top-level and H2 for nested sections, and populate each with appropriate content.

[OUTCOME]
The output perfectly mirrors the template hierarchy, making it easy to navigate and maintain.

[WHY-GOOD]
- Builds the document straight from the template contract, ensuring nothing is omitted or mis-leveled.
- Produces predictable structure, which simplifies future updates and automated processing.

### Bad Example 1
[INPUT]
User asks to update the [DoD] section in an existing implementation plan.

[BAD-DECISION]
Create a brand new file with just the [DoD] section, ignoring the existing file structure.

[WHY-BAD]
Violates rule 3 about reading current files first and avoiding duplicates. Destroys existing context and creates fragmentation.

[CORRECT-APPROACH]
Read the current implementation plan, find the existing `## [DoD]` section, update its contents in place while preserving all other sections.

### Bad Example 2
[INPUT]
Template specifies `## [Validation-Steps]` as H2 under `# [Implementation-Plan]`, but assistant outputs it as H1.

[BAD-DECISION]
```markdown
# [Validation-Steps]
- Step 1
- Step 2
```

[WHY-BAD]
Breaks the hierarchical mapping (section→H1, nested→H2). Makes the document structure inconsistent and harder to parse.

[CORRECT-APPROACH]
```markdown
# [Implementation-Plan]
## [Validation-Steps]
- Step 1
- Step 2
```

## [Process-Validation-And-Completion]
1. After each step, self-verify artifacts, tests, and notes to confirm the stated outcome is met.
2. Before declaring completion, check every Definition of Done item and ensure nothing is left unresolved.
3. Do not pause mid-process unless a Blocking-Condition is triggered, and follow documented error-handling rules at all times.

### Good Example 1
[INPUT]
Just finished implementing a new API endpoint. DoD requires: functional code, tests passing, documentation updated.

[DECISION]
Before declaring completion, run the test suite, verify all tests pass, check that API documentation includes the new endpoint with examples, and document the implementation in dev notes.

[OUTCOME]
All DoD items are verified and met. Deliverable is truly complete and production-ready.

[WHY-GOOD]
- Closes the loop on every Definition of Done requirement, ensuring no quality gates are skipped.
- Captures documentation updates alongside testing evidence, which keeps downstream teams informed.

### Good Example 2
[INPUT]
While implementing a database migration, a "deprecated syntax" warning appears but the migration still runs.

[DECISION]
Check the Blocking-Conditions document. Since it's a warning (not an error) and the operation succeeds, log the warning in dev notes, note it as technical debt to address, and continue with remaining tasks.

[OUTCOME]
Response is proportional to the issue severity, work continues efficiently while the concern is documented.

[WHY-GOOD]
- Applies the blocking-condition rules precisely, preventing unnecessary halts.
- Records the warning and remediation plan, keeping technical debt visible for future action.

### Bad Example 1
[INPUT]
Completed code changes for a feature. DoD includes "all tests pass" and "linter errors resolved."

[BAD-DECISION]
"Implementation complete! The feature is ready to use." (Without running tests or checking linter)

[WHY-BAD]
Declares completion without verification. Tests might be failing, linter errors might exist, violating rule 1.

[CORRECT-APPROACH]
Run tests, check linter output, verify all pass, then declare: "Implementation complete. All 47 tests pass, zero linter errors. Feature verified and ready."

### Bad Example 2
[INPUT]
A critical error appears: "Database connection failed. Cannot proceed with migration."

[BAD-DECISION]
Continue working on subsequent steps that depend on the migration, ignoring the blocking error.

[WHY-BAD]
Violates rule 3 about pausing when blocking conditions occur. Subsequent work will fail or be incorrect.

[CORRECT-APPROACH]
Immediately stop, report: "Blocking condition detected: Database connection failure. This prevents migration and all dependent steps. Please resolve database connectivity before proceeding."

## [Summary-Instructions]
1. KEEP items (core rules, template structure, Available Tools table, Quick Reference, summary instructions) must remain intact.
2. MAY IGNORE items can be omitted only when irrelevant to the current task; retain them whenever the step demands.
3. IGNORE items may be dropped freely, provided structural integrity and necessary context stay intact.

### Good Example 1
[INPUT]
Summarizing a long task file. KEEP section contains: "Priority order: CLAUDE.md > commands > tasks" and "Template mapping: section→H1, nested→H2"

[DECISION]
Retain these KEEP rules verbatim in the summary. Condense other sections but ensure these core governance rules remain word-for-word.

[OUTCOME]
Summary is concise yet preserves critical guardrails. Future executions won't lose essential guidance.

[WHY-GOOD]
- Protects mandatory KEEP directives while still reducing verbosity, so governance remains enforceable.
- Demonstrates disciplined summarization that targets only optional text, avoiding accidental rule loss.

### Good Example 2
[INPUT]
MAY IGNORE section includes "Historical context about why this process was created" which is unrelated to current implementation task.

[DECISION]
Note in summary: "Historical context (MAY IGNORE) omitted as not relevant to implementation. Retained all KEEP items and task-specific guidance."

[OUTCOME]
Summary is lean and focused while documenting what was intentionally excluded.

[WHY-GOOD]
- Applies discretion appropriately by trimming only non-essential MAY IGNORE content.
- Documents the omission decision, enabling future readers to restore context if needed.

### Bad Example 1
[INPUT]
Summarizing a complex workflow. KEEP section explicitly states: "Available Tools table must be preserved" but the table seems long.

[BAD-DECISION]
"The tools section was too long, so I shortened it to just the most important tools."

[WHY-BAD]
Violates rule 1. KEEP items are non-negotiable and must remain intact regardless of length.

[CORRECT-APPROACH]
Preserve the complete Available Tools table exactly as specified, even if lengthy. KEEP means KEEP.

### Bad Example 2
[INPUT]
IGNORE section contains outdated examples from a previous project version, but also includes a critical error-handling flowchart.

[BAD-DECISION]
Delete the entire IGNORE section including the flowchart.

[WHY-BAD]
While outdated examples can be dropped, the flowchart is necessary context. Blindly removing everything violates "necessary context stay intact."

[CORRECT-APPROACH]
Remove outdated examples but examine if any content (like the flowchart) is actually necessary context. If so, reclassify it or keep it.

## [MCP-Tools-Selection-Strategy]
1. Start with sequential-thinking to draft, record, and maintain the execution plan before acting on complex or multi-step decisions.
2. Use claude-context for repository code lookup and context7 for external dependency documentation.
3. Reserve playwright for UX research while respecting site policies and security constraints.

### Good Example 1
[INPUT]
Task: Design a multi-stage refactoring strategy for a legacy codebase, then identify which files need modification.

[DECISION]
Use sequential-thinking to map out the refactoring approach, identify dependencies, and validate the strategy. Then use claude-context to search the repository for relevant code patterns and files that need changes.

[OUTCOME]
Complex reasoning is structured first, then code lookup is targeted and efficient. Tools used appropriately for their strengths.

[WHY-GOOD]
- Orders tool usage to handle planning before execution, which keeps reasoning coherent and minimizes churn.
- Leverages claude-context only after the strategy is defined, yielding focused searches instead of aimless browsing.

### Good Example 2
[INPUT]
Need to implement OAuth2 authentication using an external library "passport-oauth2".

[DECISION]
Use context7 to retrieve official documentation for passport-oauth2, understand its API patterns, configuration options, and best practices before implementing.

[OUTCOME]
Implementation follows authoritative external documentation, reducing errors and following library conventions.

[WHY-GOOD]
- Selects the precise tool that surfaces vetted references, ensuring configuration matches vendor guidance.
- Prepares implementation with concrete facts, reducing risk of misusing the library.

### Bad Example 1
[INPUT]
Simple task: Find all files in the repository that import "logger.ts"

[BAD-DECISION]
Launch sequential-thinking to reason about logger patterns, hypothesize about logging strategies, map out reasoning chains...

[WHY-BAD]
Massive overkill. This is a simple code search that should use grep or claude-context directly. Sequential-thinking adds unnecessary latency for straightforward lookups.

[CORRECT-APPROACH]
Use grep or claude-context immediately: "Find all imports of logger.ts in the codebase"

### Bad Example 2
[INPUT]
User wants to understand the UX flow of a competitor's website to gather design inspiration.

[BAD-DECISION]
Immediately launch playwright and start scraping their entire site, including user account areas and private sections.

[WHY-BAD]
Violates rule 3 about security constraints and site policies. May access unauthorized areas, violate terms of service, or be unethical.

[CORRECT-APPROACH]
First ask: "I can help with UX research on public pages only. Should I focus on the public landing pages and documentation? I'll respect robots.txt and terms of service."
