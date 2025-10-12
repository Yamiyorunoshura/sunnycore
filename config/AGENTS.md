# AGENTS.md

## [Priority-And-Execution-Rules]
1. Strictly follow the priority order CLAUDE.md > commands > tasks and execute only steps explicitly authorized.
2. When instructions are ambiguous, pause to request clarification and read every required file before proceeding.
3. Complete todos sequentially without skipping or reordering steps unless dependencies demand it.

## [Template-And-Output-Format]
1. Produce pure Markdown that mirrors the template hierarchy, mapping section→H1 and nested sections→H2.
2. Honor directives in tags such as [Description], [Path-Variables], [Input], [Output], [Role], [Skills], [Scope-of-Work], [Constraints], [DoD], [Steps], [Tools], [Blocking-Conditions], [Custom-Commands], and [Validation-Steps].
3. When updating existing outputs, read the current file first, preserve its structure, enhance the content, and avoid creating duplicates.

## [Process-Validation-And-Completion]
1. After each step, self-verify artifacts, tests, and notes to confirm the stated outcome is met.
2. Before declaring completion, check every Definition of Done item and ensure nothing is left unresolved.
3. Do not pause mid-process unless a Blocking-Condition is triggered, and follow documented error-handling rules at all times.

## [Summary-Instructions]
1. KEEP items (core rules, template structure, Available Tools table, Quick Reference, summary instructions) must remain intact.
2. MAY IGNORE items can be omitted only when irrelevant to the current task; retain them whenever the step demands.
3. IGNORE items may be dropped freely, provided structural integrity and necessary context stay intact.

## [MCP-Tools-Selection-Strategy]
1. Start with sequential-thinking for complex or multi-step decisions to plan and validate hypotheses.
2. Use context7 for external dependency documentation.
3. Reserve playwright for UX research while respecting site policies and security constraints.
