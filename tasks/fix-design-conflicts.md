**GOAL**: Fix design conflicts identified in validation report, then clean up the validation report file.

## [Input]
- `{root}/docs/design-validation.md`

## [Output]
- Modified design documents:
  - `{PRD}` (if PRD workflow)
  - `{REQ}/*.md` (if full workflow)
  - `{ARCH}/*.md` (if full workflow)
  - `{EPIC}` (if full workflow)
  - `{PLAN}/*.md` (if full workflow)
- Deleted: `{root}/docs/design-validation.md` (after successful fixes)

## [Constraints]
- **MUST** fix in severity order (Critical→High→Medium→Low), **MUST NOT** fix out of order
- **MUST** obtain user confirmation for strategies, **MUST NOT** apply without confirmation
- **MUST** not introduce new conflicts, **MUST NOT** create inconsistencies
- **MUST** not delete validation report before all fixes complete, **MUST NOT** delete prematurely

## [Steps]
1. Understand all issues, extract and prioritize → Issues categorized and prioritized
2. Develop fix plans, obtain user confirmation → Approved fix plans for all issues
3. Resolve all fixes in priority order, maintain consistency → All fixes implemented with consistency
4. Review and validate changes, verify no new conflicts → All fixes validated and confirmed
5. Delete validation report, guide user to re-run validation → Cleanup completed with change summary

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] All approved fixes applied with cross-document consistency verified
- [ ] No new issues introduced, all changes confirmed by user
- [ ] Validation report "{root}/docs/design-validation.md" deleted

## [Example]

### Good #1
**Input**: Validation shows 3 critical: REQ-005 doesn't exist, EmailService fabricated, Task-4 references non-existent REQ-006  
**Decision**: Read validation→Extract all issues→Categorize: 3 critical (broken references)→Create plan.md→Develop fix plans: Issue 1 - remove REQ-005 or map to REQ-003; Issue 2 - add EmailService to arch or remove refs; Issue 3 - update Task-4 to existing REQ→Present to user→User approves→Execute: update PRD (REQ-005→REQ-003), add EmailService to arch, update Task-4 to REQ-004→Verify cross-document consistency (all refs valid)→User confirms→Delete validation report→Recommend re-run validation  
**Why Good**: Resolves systematically with user approval, confirms consistency, cleans up validation report

### Good #2
**Input**: Validation shows coverage gaps: REQ-001 no arch mapping, COMP-003 not mapped to task, Task-2 no plan (medium severity)  
**Decision**: Analyze validation (3 medium coverage gaps)→Categorize by type→Create plan.md with gap analysis→Develop strategies: Gap 1 - add AuthService to arch and map to REQ-001; Gap 2 - add Task-5 for Cache Layer; Gap 3 - create 2-plan.md→User approves→Execute: create AuthService in components.md with REQ-001 mapping, add Task-5 to epic.md with COMP-003 mapping, create plans/2-plan.md→Verify 100% coverage: all req have arch, all components have tasks, all tasks have plans→User confirms→Delete validation report  
**Why Good**: Addresses coverage gaps holistically, restores full traceability, documents completion

### Bad #1
**Input**: Validation has 5 issues including critical fabricated content, broken refs, conflicts (mix severity)  
**Bad Decision**: Fix all simultaneously without prioritization→Skip user confirmation because fixes seem obvious→Apply fixes across multiple docs without tracking→Delete validation report immediately after changes→Don't verify new conflicts  
**Why Bad**: Violates fix in severity order (should be Critical→High→Medium→Low), violates obtain user confirmation, untracked changes risk new inconsistencies, violates not delete before fixes complete  
**Correct**: Prioritize: Critical first, then High, Medium, Low→Document fix strategy in plan.md→Present to user, obtain approval before execution→Apply sequentially maintaining cross-doc consistency→After ALL fixes complete, verify no new conflicts→Obtain final user confirmation→Only then delete validation report
