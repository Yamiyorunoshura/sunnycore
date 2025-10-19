# AGENTS.md

## [Priority-And-Execution-Rules]
1. **Priority hierarchy**: Strictly follow AGENTS.md > commands > tasks order. Execute only explicitly authorized steps.
2. **Ambiguity handling**: Pause to request clarification when instructions are ambiguous. Read all required files before proceeding.
3. **Sequential execution**: Complete todos in order. Do not skip or reorder steps unless dependencies require it.
4. **Task decomposition**: Break down multi-step or complex work into smaller steps before execution.
5. **Progress tracking**: Establish valid progress tracking mechanism before you start working on the tasks to prevent losing track in long conversations.

## [Template-And-Products-Format]
1. **Markdown hierarchy**: Produce pure Markdown mirroring template structure: every section title named in the template must be a single-`#` H1 (e.g., Evidence, Verification), while nested items such as Immediate Actions or Future Improvements drop to `##` H2+ so downstream sharding remains accurate.
2. **Tag directives**: Honor all template tags such as [Description], [Path-Variables], [CONTEXT], etc.
3. **Update existing files**: When updating, read current file first, preserve structure, enhance content, avoid duplicates.

## [Process-Validation-And-Completion]
1. **Step verification**: After each step, self-verify artifacts, tests, and notes to confirm stated EXPECTED-OUTCOME is met.
2. **Quality-Gate completion check**: Before declaring completion, check every Definition of Done item. Ensure nothing is unresolved.
3. **Blocking conditions**: Do not pause mid-process unless a Blocking-Condition is triggered. Follow documented error-handling rules.

## [Summary-Instructions]
1. **KEEP items**: Core rules, template structure, Available Tools table, Quick Reference, summary instructions must remain intact.
2. **MAY IGNORE items**: Can be omitted only when irrelevant to current task. Retain whenever the step demands.
3. **IGNORE items**: May be dropped freely, provided structural integrity and necessary context stay intact.

## [MCP-Tools-Selection-Strategy]
1. **Planning first**: Use sequential-thinking to draft, record, and maintain execution plan before acting on complex or multi-step decisions.
2. **Documentation lookup**: Use context7 for external dependency documentation.
3. **UX research tool**: Reserve playwright for UX research only. Respect site policies and security constraints.

---

## [Examples]

### Good Example 1: Following Priority and Template Rules

**[CONTEXT]**
Need to execute develop-plan command with task ID 1, decisions: follow priority hierarchy and template rules while maintaining proper execution order and verification.

**[DECISION]**
1. decisions: Read AGENTS.md first to understand core constraints (Rule 1)
2. decisions: Check commands for any auth-related directives (Rule 1)
3. decisions: Use sequential-thinking to plan: analyze requirements → design architecture → implement → test → verify Quality-Gate (Rule 11)
4. decisions: Create a todo list with steps of the tasks written
5. decisions: Read tasks/develop-plan.md completely (Rule 2)
6. decisions: Start working according to the steps in the task
7. decisions: Generate dev-notes based on the template: `# [Implementation-Plan]` with `## [Quality-Gate]` as H2 (Rules 4-5)
8. decisions: Execute steps sequentially without skipping (Rule 3)
9. decisions: Verify each step: run tests, check linter (Rule 7)
10. decisions: Complete Quality-Gate checklist before declaring done (Rule 8)

**[EXPECTED-OUTCOME]**  
Feature delivered with all governance rules respected, proper template structure maintained, all quality gates passed.

**[WHY-GOOD]**  
- Respects instruction hierarchy (AGENTS.md → commands → tasks)  
- Uses sequential-thinking for complex multi-step work  
- Established valid progress management mechanism (the todo list) to avoid missing tasks
- Maintains correct H1/H2 template hierarchy  
- Executes steps in order without skipping  
- Verifies at each step and checks complete Quality-Gate  

---

### Good Example 2: Summarizing and Updating Documents

**[CONTEXT]**
Need to summarize a long architecture document and update specific section while handling different content priority levels, decisions: properly categorize and process content according to KEEP/MAY IGNORE/IGNORE rules.

**[DECISION]**
1. decisions: Identify KEEP, MAY IGNORE, and IGNORE items (Rule 10)
2. decisions: Preserve all KEEP items completely, including full Available Tools table even if lengthy (Rule 10)
3. decisions: Omit MAY IGNORE items (historical context) and document: "Project history (MAY IGNORE) excluded as not relevant to current task" (Rule 10)
4. decisions: Remove IGNORE items (outdated examples) but verify no necessary context is lost (Rule 10)
5. decisions: Search codebase to find existing component implementations: "Where are components implemented?" (Rules 11-12)
6. decisions: Read docs/architecture.md completely before updating (Rule 6)
7. decisions: Locate `## [Components]` section and update in place without changing heading levels (Rules 4-6)

**[EXPECTED-OUTCOME]**  
Summary is focused and lean while preserving all governance rules. Architecture doc maintains template structure with enhanced content in correct section.

**[WHY-GOOD]**  
- Strictly preserves KEEP items regardless of length  
- Carefully handles MAY IGNORE (only excludes irrelevant content)  
- Intelligently processes IGNORE (checks for necessary context)  
- Searched codebase for semantic code discovery  
- Reads existing file before updating, preserves structure  

---

### Bad Example 1: Violating Priority and Execution Rules

**[CONTEXT]**
Need to implement payment integration based on a specific task file, decisions: skip governance rules and directly proceed with implementation without proper planning or verification.

**[BAD-DECISION]**
1. decisions: [VIOLATION] Skip reading AGENTS.md (violates Rule 1)
2. decisions: [VIOLATION] Skip checking commands for security/tech-stack directives (violates Rule 1)
3. decisions: [VIOLATION] No sequential-thinking planning for complex task (violates Rule 11)
4. decisions: [VIOLATION] Jump directly to Step 3, skip Steps 1-2 (violates Rule 3)
5. decisions: [VIOLATION] Create payment-module.md with wrong hierarchy (violates Rules 4-5):
    ```markdown
    # [Implementation-Plan]
    # [Quality-Gate]          ← Wrong: should be H2
    - Item 1
    ```
6. decisions: [VIOLATION] Declare "Implementation complete!" without running tests or checking Quality-Gate (violates Rules 7-8)

**[EXPECTED-OUTCOME]**  
May violate security constraints in AGENTS.md. Tech-stack requirements in commands ignored. Steps skipped causing missing dependencies. Template structure broken. Tests failing, deliverable incomplete.

**[WHY-BAD]**  
- Ignores priority hierarchy, violates governance  
- No planning for complex task  
- Breaks template heading levels  
- Skips steps, breaks dependencies  
- Declares completion without verification  

**[CORRECT-APPROACH]**  
1. Read AGENTS.md first (identify security constraints)
2. Check commands (confirm required tech stack)
3. Use sequential-thinking to plan 6-step execution
4. Read tasks/develop-plan.md completely
5. Execute all steps in order
6. Use correct hierarchy: `## [Quality-Gate]` as H2
7. Verify tests and linter at each step
8. Complete Quality-Gate check before declaring done

---

### Bad Example 2: Wrong Tool Selection and Format Violations

**[CONTEXT]**
Need to handle multiple user requests about framework version, document summarization with content priorities, and file updates, decisions: use inappropriate tools and violate governance rules.

**[BAD-DECISION]**
1. decisions: [VIOLATION] Launch sequential-thinking to reason about React versions, hypothesize framework choices... (violates Rules 11, 15)
   - **Correct**: Just read package.json directly

2. decisions: [VIOLATION] "Tools table is too long, I'll keep only the 5 most important" (violates Rule 10)
   - **Correct**: KEEP means mandatory preservation regardless of length

3. decisions: [VIOLATION] Create brand new file with only [Tools] section, discard all existing content (violates Rule 6)
   - **Correct**: Read existing epic.md, locate `## [Tools]`, update only that section

4. decisions: [VIOLATION] User: "Analyze competitor website backend validation"
   - AI: Launch playwright, try to access backend endpoints, inspect API calls... (violates Rule 13)
   - **Correct**: "I can only analyze public UI. Backend inspection violates security policies. Proceed with public pages only?"

**[EXPECTED-OUTCOME]**  
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
