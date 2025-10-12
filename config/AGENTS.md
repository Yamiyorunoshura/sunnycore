# AGENTS.md

## [Priority-And-Execution-Rules]
1. Strictly follow the priority order CLAUDE.md > commands > tasks and execute only steps explicitly authorized.
2. When instructions are ambiguous, pause to request clarification and read every required file before proceeding.
3. Complete todos sequentially without skipping or reordering steps unless dependencies demand it.

### Example 1
[INPUT]
A task note suggests ignoring a `commands` directive because it seems redundant.

[DECISION]
Consult CLAUDE.md first, then carry out the `commands` steps before evaluating whether the `tasks` reminder still applies.

[OUTCOME]
Execution stays aligned with the mandated hierarchy.

### Example 2
[INPUT]
The user asks to jump directly to the final checklist item without context.

[DECISION]
Process each todo in order unless a dependency makes reordering necessary, requesting clarification if needed.

[OUTCOME]
The assistant avoids skipping essential groundwork.

## [Template-And-Output-Format]
1. Produce pure Markdown that mirrors the template hierarchy, mapping section→H1 and nested sections→H2.
2. Honor directives in tags such as [Description], [Path-Variables], [Input], [Output], [Role], [Skills], [Scope-of-Work], [Constraints], [DoD], [Steps], [Tools], [Blocking-Conditions], [Custom-Commands], and [Validation-Steps].
3. When updating existing outputs, read the current file first, preserve its structure, enhance the content, and avoid creating duplicates.

### Example 1
[INPUT]
A brief instructs updating the [Tools] section while the document already follows the required hierarchy.

[DECISION]
Edit within the existing `## [Tools]` heading, keeping the rest of the Markdown layout untouched.

[OUTCOME]
The output remains consistent with the template and avoids structural drift.

### Example 2
[INPUT]
Multiple [Constraints] entries need clarifications without duplication.

[DECISION]
Expand the content inside each existing [Constraints] bullet instead of adding new headings.

[OUTCOME]
Readers find the enriched constraints exactly where they expect them.

## [Process-Validation-And-Completion]
1. After each step, self-verify artifacts, tests, and notes to confirm the stated outcome is met.
2. Before declaring completion, check every Definition of Done item and ensure nothing is left unresolved.
3. Do not pause mid-process unless a Blocking-Condition is triggered, and follow documented error-handling rules at all times.

### Example 1
[INPUT]
Code modifications were made but no linting or tests were rerun.

[DECISION]
Run the relevant validation steps and ensure notes describe the evidence before reporting completion.

[OUTCOME]
Deliverables meet the Definition of Done and documentation matches reality.

### Example 2
[INPUT]
A warning message appears, yet its impact is uncertain.

[DECISION]
Compare the scenario with documented Blocking-Conditions to decide whether to halt or continue.

[OUTCOME]
The assistant responds proportionally, minimizing unnecessary delays.

## [Summary-Instructions]
1. KEEP items (core rules, template structure, Available Tools table, Quick Reference, summary instructions) must remain intact.
2. MAY IGNORE items can be omitted only when irrelevant to the current task; retain them whenever the step demands.
3. IGNORE items may be dropped freely, provided structural integrity and necessary context stay intact.

### Example 1
[INPUT]
During a summary revision, KEEP items list non-negotiable behaviors.

[DECISION]
Leave the KEEP section untouched while refining other descriptive paragraphs.

[OUTCOME]
Critical guardrails remain visible to future readers.

### Example 2
[INPUT]
The MAY IGNORE section mentions optional onboarding steps that do not apply now.

[DECISION]
Explicitly note that they are not needed for this task but keep them for potential future use.

[OUTCOME]
The document stays informative without confusing the current execution.

## [MCP-Tools-Selection-Strategy]
1. Start with sequential-thinking for complex or multi-step decisions to plan and validate hypotheses.
2. Use context7 for external dependency documentation.
3. Reserve playwright for UX research while respecting site policies and security constraints.

### Example 1
[INPUT]
The task involves deep API research beyond the repository.

[DECISION]
Map the approach with sequential-thinking, then gather documentation through context7.

[OUTCOME]
Research is structured and relies on authoritative sources.

### Example 2
[INPUT]
An exploratory UI walk-through is required to confirm user flows.

[DECISION]
Employ playwright only after verifying the activity qualifies as UX research and complies with restrictions.

[OUTCOME]
Tool usage matches the prescribed selection policy.

### Example 3
[INPUT]
The implementation requires external api calls

[DECISION]
Use context7 to retrieve the external api documentation.

[OUTCOME]
The assistant retrieves the external api documentation, enabling informed implementation.
