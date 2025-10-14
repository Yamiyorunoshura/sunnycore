# CLAUDE.md

## [Priority-And-Execution-Rules]
1. **Priority hierarchy**: Strictly follow CLAUDE.md > commands > tasks order. Execute only explicitly authorized steps.
2. **Ambiguity handling**: Pause to request clarification when instructions are ambiguous. Read all required files before proceeding.
3. **Sequential execution**: Complete todos in order. Do not skip or reorder steps unless dependencies require it.
4. **Task decomposition**: Break down multi-step or complex work into smaller steps before execution.
5. **Progress tracking**: Establish valid progress tracking mechanism before you start working on the tasks to prevent losing tack in long conversations.

## [Template-And-Output-Format]
1. **Markdown hierarchy**: Produce pure Markdown mirroring template structure: section→H1, nested sections→H2.
2. **Tag directives**: Honor all template tags such as [Description], [Path-Variables], [Input], [Output], [Role], [Skills], [Scope-of-Work], [Constraints], [DoD], [Steps], [Tools], [Blocking-Conditions], [Custom-Commands], [Validation-Steps].
3. **Update existing files**: When updating, read current file first, preserve structure, enhance content, avoid duplicates.

## [Process-Validation-And-Completion]
1. **Step verification**: After each step, self-verify artifacts, tests, and notes to confirm stated outcome is met.
2. **DoD completion check**: Before declaring completion, check every Definition of Done item. Ensure nothing is unresolved.
3. **Blocking conditions**: Do not pause mid-process unless a Blocking-Condition is triggered. Follow documented error-handling rules.

## [Summary-Instructions]
1. **KEEP items**: Core rules, template structure, Available Tools table, Quick Reference, summary instructions must remain intact.
2. **MAY IGNORE items**: Can be omitted only when irrelevant to current task. Retain whenever the step demands.
3. **IGNORE items**: May be dropped freely, provided structural integrity and necessary context stay intact.

## [MCP-Tools-Selection-Strategy]
1. **Planning first**: Use sequential-thinking to draft, record, and maintain execution plan before acting on complex or multi-step decisions.
2. **Documentation lookup**: Use claude-context for repository code queries, context7 for external dependency documentation.
3. **UX research tool**: Reserve playwright for UX research only. Respect site policies and security constraints.

---

## [Comprehensive-Examples]

### Good Example 1: Following Priority and Template Rules

**[INPUT]**  
User: "Implement a user authentication module based on tasks/develop-plan.md"

**[DECISION]**  
1. Read CLAUDE.md first to understand core constraints (Rule 1)
2. Check commands for any auth-related directives (Rule 1)
3. Use sequential-thinking to plan: analyze requirements → design architecture → implement → test → verify DoD (Rule 11)
4. Read tasks/develop-plan.md completely (Rule 2)
5. Create implementation-plan.md using correct hierarchy: `# [Implementation-Plan]` with `## [DoD]` as H2 (Rules 4-5)
6. Execute steps sequentially without skipping (Rule 3)
7. Verify each step: run tests, check linter (Rule 7)
8. Complete DoD checklist before declaring done (Rule 8)

**[OUTCOME]**  
Feature delivered with all governance rules respected, proper template structure maintained, all quality gates passed.

**[WHY-GOOD]**  
- Respects instruction hierarchy (CLAUDE.md → commands → tasks)  
- Uses sequential-thinking for complex multi-step work  
- Maintains correct H1/H2 template hierarchy  
- Executes steps in order without skipping  
- Verifies at each step and checks complete DoD  

---

### Good Example 2: Summarizing and Updating Documents

**[INPUT]**  
User: "Summarize docs/architecture.md (long file), update the [Components] section, remove outdated examples marked as IGNORE"

**[DECISION]**  
1. Identify KEEP, MAY IGNORE, and IGNORE items (Rule 10)
2. Preserve all KEEP items completely, including full Available Tools table even if lengthy (Rule 10)
3. Omit MAY IGNORE items (historical context) and document: "Project history (MAY IGNORE) excluded as not relevant to current task" (Rule 10)
4. Remove IGNORE items (outdated examples) but verify no necessary context is lost (Rule 10)
5. Use claude-context to search existing component implementations (Rules 11-12)
6. Read docs/architecture.md completely before updating (Rule 6)
7. Locate `## [Components]` section and update in place without changing heading levels (Rules 4-6)

**[OUTCOME]**  
Summary is focused and lean while preserving all governance rules. Architecture doc maintains template structure with enhanced content in correct section.

**[WHY-GOOD]**  
- Strictly preserves KEEP items regardless of length  
- Carefully handles MAY IGNORE (only excludes irrelevant content)  
- Intelligently processes IGNORE (checks for necessary context)  
- Selects appropriate lightweight tool (claude-context)  
- Reads existing file before updating, preserves structure  

---

### Bad Example 1: Violating Priority and Execution Rules

**[INPUT]**  
User: "Implement payment integration based on tasks/develop-plan.md"

**[BAD-DECISION]**  
1. [VIOLATION] Skip reading CLAUDE.md (violates Rule 1)
2. [VIOLATION] Skip checking commands for security/tech-stack directives (violates Rule 1)
3. [VIOLATION] No sequential-thinking planning for complex task (violates Rule 11)
4. [VIOLATION] Jump directly to Step 3, skip Steps 1-2 (violates Rule 3)
5. [VIOLATION] Create payment-module.md with wrong hierarchy (violates Rules 4-5):
   ```markdown
   # [Implementation-Plan]
   # [DoD]          ← Wrong: should be H2
   - Item 1
   ```
6. [VIOLATION] Declare "Implementation complete!" without running tests or checking DoD (violates Rules 7-8)

**[OUTCOME]**  
May violate security constraints in CLAUDE.md. Tech-stack requirements in commands ignored. Steps skipped causing missing dependencies. Template structure broken. Tests failing, deliverable incomplete.

**[WHY-BAD]**  
- Ignores priority hierarchy, violates governance  
- No planning for complex task  
- Breaks template heading levels  
- Skips steps, breaks dependencies  
- Declares completion without verification  

**[CORRECT-APPROACH]**  
1. Read CLAUDE.md first (identify security constraints)
2. Check commands (confirm required tech stack)
3. Use sequential-thinking to plan 6-step execution
4. Read tasks/develop-plan.md completely
5. Execute all steps in order
6. Use correct hierarchy: `## [DoD]` as H2
7. Verify tests and linter at each step
8. Complete DoD check before declaring done

---

### Bad Example 2: Wrong Tool Selection and Format Violations

**[INPUT]**  
1. User: "What React version does this project use?"
2. User: "Summarize docs/workflow.md. KEEP section has 15-item Available Tools table but seems long"
3. User: "Update epic.md [Tools] section"

**[BAD-DECISION]**  
1. [VIOLATION] Launch sequential-thinking to reason about React versions, hypothesize framework choices... (violates Rules 11, 15)
   - **Correct**: Just read package.json directly

2. [VIOLATION] "Tools table is too long, I'll keep only the 5 most important" (violates Rule 10)
   - **Correct**: KEEP means mandatory preservation regardless of length

3. [VIOLATION] Create brand new file with only [Tools] section, discard all existing content (violates Rule 6)
   - **Correct**: Read existing epic.md, locate `## [Tools]`, update only that section

4. [VIOLATION] User: "Analyze competitor website backend validation"
   - AI: Launch playwright, try to access backend endpoints, inspect API calls... (violates Rule 13)
   - **Correct**: "I can only analyze public UI. Backend inspection violates security policies. Proceed with public pages only?"

**[OUTCOME]**  
Simple queries waste time on unnecessary reasoning. Mandatory governance rules deleted. Existing file content lost. Security policies violated.

**[WHY-BAD]**  
- Inappropriate tool selection (over-using sequential-thinking, misusing playwright)  
- Violates KEEP directive (deletes mandatory items)  
- Destroys document structure (creates new file instead of updating)  
- Violates security constraints (attempts unauthorized access)  

**[CORRECT-APPROACH]**  
1. Simple query: `read_file package.json` → Report "React 18.2.0"
2. KEEP items: Preserve complete 15-item tools table (KEEP = non-negotiable)
3. Update file: `read_file epic.md` → Locate `## [Tools]` → Update only that section
4. UX research: "I can help analyze public page UX. Should I focus on public landing pages? I'll respect robots.txt and terms of service."
