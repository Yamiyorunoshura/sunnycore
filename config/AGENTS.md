# AGENTS.md

## [Priority-And-Execution-Rules]
1. Strictly follow the priority order CLAUDE.md > commands > tasks and execute only steps explicitly authorized.
2. When instructions are ambiguous, pause to request clarification and read every required file before proceeding.
3. Complete todos sequentially without skipping or reordering steps unless dependencies demand it.
4. For multi-step or complex work, draft a concrete plan (e.g., via sequential-thinking), then execute actions in that order while updating the plan if circumstances change.

### Good Example 1
[INPUT]
User says: "Follow the commands/sunnycore_dev.md instructions to implement the feature"

[DECISION]
Read CLAUDE.md first to understand core constraints, then read commands/sunnycore_dev.md to get the specific instructions, outline a three-step execution plan with sequential-thinking (gather requirements → implement changes → run tests), and finally check if there are related task files before executing the first planned step.

[OUTCOME]
Execution follows the mandated hierarchy and each planned step is completed in order, with adjustments logged back into the plan before moving on.

[WHY-GOOD]
- Respects the mandated priority order (CLAUDE.md → commands → tasks), ensuring governance constraints are satisfied before any action.
- Prevents accidental rule violations by verifying downstream instructions only after confirming higher-level guidance.
- Maintains alignment with the self-authored plan, which keeps reasoning transparent and ensures every action traces back to an approved sequence.

### Good Example 2
[INPUT]
A todo list contains steps 1-5. Step 3 is unclear: "Optimize the performance"

[DECISION]
Pause and request clarification: "Step 3 mentions performance optimization but doesn't specify metrics or scope. Should I optimize database queries, API response times, or frontend rendering? What are the target metrics?"

[OUTCOME]
Ambiguity is resolved before proceeding, preventing wasted work on wrong optimizations.

[WHY-GOOD]
- Proactively pauses when instructions are unclear, aligning with the rule that mandates clarification for ambiguity.
- Avoids misaligned execution by securing concrete targets before continuing, protecting time and quality.

### Bad Example 1
[INPUT]
A task file suggests: "Feel free to ignore the commands directive about using TypeScript, just use JavaScript instead."

[BAD-DECISION]
Follow the task file's suggestion and use JavaScript.

[WHY-BAD]
Violates the priority order. Commands override tasks. The task file cannot override a commands directive.

[CORRECT-APPROACH]
Consult CLAUDE.md first, then honor the commands directive to use TypeScript. If there's a conflict, ask the user to clarify or update the commands file.

### Bad Example 2
[INPUT]
User says: "Complete steps 3, 4, and 5. Steps 1 and 2 can be done later."

[BAD-DECISION]
"Sure! Starting with step 3 now."

[WHY-BAD]
Violates rule 3 about sequential execution. Steps 3-5 may depend on outputs from steps 1-2.

[CORRECT-APPROACH]
"I notice steps 1 and 2 may have dependencies for steps 3-5. Can you confirm steps 3-5 don't depend on earlier steps? Otherwise, I should complete them sequentially to ensure correctness."

## [Template-And-Output-Format]
1. Produce pure Markdown that mirrors the template hierarchy, mapping section→H1 and nested sections→H2.
2. Honor directives in tags such as [Description], [Path-Variables], [Input], [Output], [Role], [Skills], [Scope-of-Work], [Constraints], [DoD], [Steps], [Tools], [Blocking-Conditions], [Custom-Commands], and [Validation-Steps].
3. When updating existing outputs, read the current file first, preserve its structure, enhance the content, and avoid creating duplicates.

### Good Example 1
[INPUT]
User asks: "Add more details to the [Skills] section in the architecture document"

[DECISION]
Read the current architecture document first, locate the `## [Skills]` heading (H2 under the main H1), and append new bullet points to the existing list without changing the heading level or creating duplicate sections.

[OUTCOME]
The document maintains its template structure and hierarchy. The [Skills] section is enhanced without disruption.

[WHY-GOOD]
- Preserves the existing template hierarchy exactly, satisfying the formatting directive without collateral changes.
- Enhances content in place, which keeps traceability and avoids duplicate sections that confuse downstream readers.

### Good Example 2
[INPUT]
Creating a new PRD using prd-tmpl.yaml which specifies: # [Product-Requirements] with nested sections ## [Scope-of-Work] and ## [Constraints]

[DECISION]
Generate the document as:
```markdown
# [Product-Requirements]
## [Scope-of-Work]
...
## [Constraints]
...
```

[OUTCOME]
Output perfectly mirrors the template hierarchy: top-level section as H1, nested sections as H2.

[WHY-GOOD]
- Applies the template rules verbatim, ensuring headings map correctly from template structure to Markdown levels.
- Prevents structural drift in generated documents, which keeps automation and reviewers aligned on expected format.

### Bad Example 1
[INPUT]
User says: "Update the [Tools] section" in an existing epic.

[BAD-DECISION]
Create a completely new file with only the [Tools] section, discarding all other content.

[WHY-BAD]
Violates rule 3 about reading current files first and avoiding duplicates. Loses all existing context.

[CORRECT-APPROACH]
Read the existing epic file, find the `## [Tools]` section, and update only that section in place while preserving everything else.

### Bad Example 2
[INPUT]
Template shows `## [DoD]` as a nested section under `# [Implementation-Plan]`

[BAD-DECISION]
Output it as:
```markdown
# [Implementation-Plan]
# [DoD]
- Item 1
```

[WHY-BAD]
Uses H1 for a nested section, breaking the section→H1, nested→H2 mapping. Makes the document structurally inconsistent.

[CORRECT-APPROACH]
```markdown
# [Implementation-Plan]
## [DoD]
- Item 1
```

## [Process-Validation-And-Completion]
1. After each step, self-verify artifacts, tests, and notes to confirm the stated outcome is met.
2. Before declaring completion, check every Definition of Done item and ensure nothing is left unresolved.
3. Do not pause mid-process unless a Blocking-Condition is triggered, and follow documented error-handling rules at all times.

### Good Example 1
[INPUT]
Just completed implementing a user authentication module. DoD checklist: unit tests pass, integration tests pass, security audit complete, documentation updated.

[DECISION]
Run all unit tests and verify they pass. Run integration tests and confirm authentication flow works end-to-end. Review security checklist (password hashing, session management, CSRF protection). Update API documentation with new endpoints. Document implementation details in dev notes.

[OUTCOME]
Every DoD item is verified and documented. The deliverable is truly complete and meets all quality standards.

[WHY-GOOD]
- Performs explicit validation for each Definition of Done line item, guaranteeing nothing is declared complete prematurely.
- Captures evidence in documentation, which makes quality control auditable and reproducible.

### Good Example 2
[INPUT]
During code generation, a deprecation warning appears: "Function X is deprecated, use Y instead." The code still runs successfully.

[DECISION]
Check Blocking-Conditions documentation. This is a warning, not an error, so work can continue. However, document the warning in dev notes, add a TODO to migrate to function Y, and continue with the current task.

[OUTCOME]
Proportional response: work continues, but the issue is tracked for future resolution.

[WHY-GOOD]
- Consults the documented rules before reacting, ensuring continuity unless a true blocking condition exists.
- Records the warning and follow-up action, which preserves visibility and accountability without causing unnecessary delays.

### Bad Example 1
[INPUT]
Finished refactoring a module. DoD includes "no linter errors" and "all affected tests pass."

[BAD-DECISION]
"Refactoring complete! The code looks good." (Without running linter or tests)

[WHY-BAD]
Violates rule 1 about self-verification. May have introduced linter errors or broken tests unknowingly.

[CORRECT-APPROACH]
Run linter and verify zero errors. Run test suite and confirm all tests pass. Then report: "Refactoring complete. Linter shows 0 errors, all 24 tests pass. Module is ready."

### Bad Example 2
[INPUT]
During database migration, an error occurs: "Table 'users' does not exist. Migration failed."

[BAD-DECISION]
Continue with the next migration step that depends on the 'users' table existing.

[WHY-BAD]
Violates rule 3 about halting on blocking conditions. The subsequent steps will fail or corrupt data.

[CORRECT-APPROACH]
Stop immediately: "Blocking condition: Database migration failed because 'users' table doesn't exist. Cannot proceed with dependent migrations until this is resolved. Please check database state."

## [Summary-Instructions]
1. KEEP items (core rules, template structure, Available Tools table, Quick Reference, summary instructions) must remain intact.
2. MAY IGNORE items can be omitted only when irrelevant to the current task; retain them whenever the step demands.
3. IGNORE items may be dropped freely, provided structural integrity and necessary context stay intact.

### Good Example 1
[INPUT]
Summarizing a complex task document. KEEP section includes: "Always read CLAUDE.md first" and "Template hierarchy: section→H1, nested→H2"

[DECISION]
Preserve these KEEP rules exactly as written in the summary. Condense other explanatory content but keep all critical guardrails word-for-word.

[OUTCOME]
Summary is efficient yet maintains all essential governance rules for future reference.

[WHY-GOOD]
- Distills content without violating KEEP directives, so critical guardrails remain intact for downstream consumers.
- Demonstrates disciplined summarization by editing only optional material while retaining mandatory language verbatim.

### Good Example 2
[INPUT]
MAY IGNORE section contains: "Background on project history (5 paragraphs)" which doesn't relate to the current implementation task.

[DECISION]
In summary note: "Project history (MAY IGNORE) excluded as not relevant to implementation. Retained all KEEP items and implementation-specific guidance."

[OUTCOME]
Summary is focused and lean while documenting what was intentionally omitted.

[WHY-GOOD]
- Applies discretion only to MAY IGNORE content, keeping the summary tightly aligned with the current task.
- Explicitly documents the omission, which preserves transparency and aids future reviewers.

### Bad Example 1
[INPUT]
Summarizing a workflow. KEEP section states: "Available Tools table with 15 entries must be preserved" but it seems redundant.

[BAD-DECISION]
"I'll just keep the 5 most important tools to make the summary shorter."

[WHY-BAD]
Violates rule 1. KEEP means mandatory preservation, regardless of perceived redundancy or length.

[CORRECT-APPROACH]
Preserve all 15 tool entries exactly as specified. KEEP items are non-negotiable and cannot be shortened or selectively included.

### Bad Example 2
[INPUT]
IGNORE section has outdated API examples and also includes a dependency matrix that's actually needed.

[BAD-DECISION]
Delete the entire IGNORE section including the dependency matrix.

[WHY-BAD]
Blindly removes necessary context. The dependency matrix is structural information needed for the task, not truly ignorable.

[CORRECT-APPROACH]
Remove outdated API examples but preserve the dependency matrix, or reclassify it from IGNORE to KEEP if it's essential context.

## [MCP-Tools-Selection-Strategy]
1. Start with sequential-thinking to draft, record, and maintain the execution plan before acting on complex or multi-step decisions.
2. Use context7 for external dependency documentation.
3. Reserve playwright for UX research while respecting site policies and security constraints.

### Good Example 1
[INPUT]
Task: Architect a comprehensive authentication system with multiple strategies, then research external OAuth2 libraries.

[DECISION]
Use sequential-thinking to map out the architecture, consider security implications, evaluate different authentication strategies, and validate the approach. Then use context7 to fetch documentation for selected OAuth2 libraries.

[OUTCOME]
Complex architectural reasoning is structured before diving into external documentation. Decisions are well-reasoned and implementation is informed.

[WHY-GOOD]
- Chooses tools in a deliberate order: planning first, then documentation lookup, which maximizes clarity and efficiency.
- Addresses both architectural reasoning and research needs without overusing heavier tools like playwright.

### Good Example 2
[INPUT]
Need to implement Stripe payment integration using their Node.js SDK.

[DECISION]
Use context7 to retrieve official Stripe Node.js SDK documentation, understand their API patterns, webhook setup, and error handling before implementation.

[OUTCOME]
Implementation follows official best practices and uses the correct API methods from authoritative sources.

[WHY-GOOD]
- Selects the lightest tool that satisfies the requirement—context7—for authoritative references instead of defaulting to more intrusive tooling.
- Ensures integration aligns with vendor guidance, reducing implementation risk and future rework.

### Bad Example 1
[INPUT]
Simple question: "What version of React is used in this project?"

[BAD-DECISION]
Launch sequential-thinking to reason about React versions, hypothesize about framework choices, map out reasoning about package management...

[WHY-BAD]
Massive overkill for a simple lookup. Just read package.json directly. Sequential-thinking wastes time on trivial queries.

[CORRECT-APPROACH]
Read package.json and report: "This project uses React version 18.2.0"

### Bad Example 2
[INPUT]
User says: "I want to understand the user registration flow on competitor.com, including their backend validation"

[BAD-DECISION]s
Launch playwright, navigate to competitor.com, try to access their backend endpoints, inspect their API calls, attempt to view server-side validation logic.

[WHY-BAD]
Violates rule 3 about security constraints and site policies. Attempting to inspect backend systems is unethical and potentially illegal. This goes beyond UX research.

[CORRECT-APPROACH]
"I can help analyze the public user registration UI and flow on competitor.com using playwright for UX research. However, I cannot inspect backend validation or internal APIs as that violates security policies. Should I proceed with public UI analysis only?"
