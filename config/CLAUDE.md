# CLAUDE.md

## [Priority-And-Execution-Rules]
1. Strictly follow the priority order CLAUDE.md > commands > tasks and execute only steps explicitly authorized.
2. When instructions are ambiguous, pause to request clarification and read every required file before proceeding.
3. Complete todos sequentially without skipping or reordering steps unless dependencies demand it.

### Example 1
[INPUT]
A user provides both `commands` and `tasks` directives, but the `commands` steps conflict with CLAUDE.md.

[DECISION]
Review CLAUDE.md first, then execute the `commands` instructions, postponing `tasks` until alignment is confirmed.

[OUTCOME]
The assistant follows the top-priority source, preventing actions that contradict core governance.

### Example 2
[INPUT]
The user demands skipping directly to step 4 even though steps 1-3 are unfinished.

[DECISION]
Continue executing todos in order, only advancing to step 4 after the earlier steps are complete or dependencies require otherwise.

[OUTCOME]
The workflow remains consistent, avoiding missing prerequisites.

## [Template-And-Output-Format]
1. Produce pure Markdown that mirrors the template hierarchy, mapping section→H1 and nested sections→H2.
2. Honor directives in tags such as [Description], [Path-Variables], [Input], [Output], [Role], [Skills], [Scope-of-Work], [Constraints], [DoD], [Steps], [Tools], [Blocking-Conditions], [Custom-Commands], and [Validation-Steps].
3. When updating existing outputs, read the current file first, preserve its structure, enhance the content, and avoid creating duplicates.

### Example 1
[INPUT]
An existing report already contains H1 and H2 headings alongside multiple tagged sections.

[DECISION]
Preserve the established hierarchy and tags while augmenting the content inside the appropriate sections.

[OUTCOME]
The updated document respects the template structure and remains easy to navigate.

### Example 2
[INPUT]
A new [Validation-Steps] section must be added to a document that currently lacks it.

[DECISION]
Introduce a new H2 titled `## [Validation-Steps]`, populate it with the requested instructions, and avoid duplicating other sections.

[OUTCOME]
The template stays uniform, and the new validation guidance is clearly incorporated.

## [Process-Validation-And-Completion]
1. After each step, self-verify artifacts, tests, and notes to confirm the stated outcome is met.
2. Before declaring completion, check every Definition of Done item and ensure nothing is left unresolved.
3. Do not pause mid-process unless a Blocking-Condition is triggered, and follow documented error-handling rules at all times.

### Example 1
[INPUT]
Implementation work is finished, but no verification has been performed yet.

[DECISION]
Review the artifacts, confirm tests, and ensure notes reflect the actual results before proceeding.

[OUTCOME]
The assistant validates the deliverables, reducing the risk of overlooked issues.

### Example 2
[INPUT]
An unexpected error message appears mid-task, and its severity is unclear.

[DECISION]
Consult the documented Blocking-Conditions to determine whether to pause and escalate or continue.

[OUTCOME]
Error handling stays aligned with policy, preventing premature termination or reckless continuation.

## [Summary-Instructions]
1. KEEP items (core rules, template structure, Available Tools table, Quick Reference, summary instructions) must remain intact.
2. MAY IGNORE items can be omitted only when irrelevant to the current task; retain them whenever the step demands.
3. IGNORE items may be dropped freely, provided structural integrity and necessary context stay intact.

### Example 1
[INPUT]
A summary rewrite is required while KEEP items contain critical rules.

[DECISION]
Retain the KEEP section verbatim and only adjust content in sections that permit modification.

[OUTCOME]
Key guidance remains accessible, and the summary stays compliant.

### Example 2
[INPUT]
An IGNORE section references obsolete examples unrelated to the assignment.

[DECISION]
Remove the IGNORE section entirely, ensuring the rest of the structure is untouched.

[OUTCOME]
The document becomes leaner without sacrificing necessary context.

## [MCP-Tools-Selection-Strategy]
1. Start with sequential-thinking for complex or multi-step decisions to plan and validate hypotheses.
2. Use claude-context for repository code lookup and context7 for external dependency documentation.
3. Reserve playwright for UX research while respecting site policies and security constraints.

### Example 1
[INPUT]
The task requires mapping a multi-stage strategy and reviewing internal code snippets.

[DECISION]
Launch sequential-thinking to reason through the plan, then use claude-context to retrieve the relevant code fragments.

[OUTCOME]
Tool usage aligns with the strategy guidance, enabling informed execution.

### Example 2
[INPUT]
Field research on a live user interface is needed to gather insights.

[DECISION]
Deploy playwright only after confirming the investigation qualifies as UX research and adheres to security policies.

[OUTCOME]
The assistant chooses the appropriate tool while respecting operational constraints.
