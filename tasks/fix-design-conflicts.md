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

## [Instructions]

### 1. Issue Analysis and Categorization
Extract and categorize ALL issues from the validation report:

**Issue Categories**:
- **Fabricated Content**: References to non-existent entities (e.g., REQ-005 doesn't exist)
- **Broken References**: Invalid cross-references between documents
- **Coverage Gaps**: Requirements without architecture, components without tasks
- **Inconsistencies**: Contradictions or naming mismatches across documents
- **Conflicts**: Direct contradictions in specifications

**Severity Categorization**:
- **Critical**: Fabricated content, broken references blocking work
- **High**: Coverage gaps preventing complete traceability
- **Medium**: Inconsistencies affecting clarity
- **Low**: Minor naming variations

Document all issues with categories and severity in a tracking table.

### 2. Fix Strategy Development
For each issue, develop a specific fix strategy:

**Strategy Components**:
- **Issue**: Clear description of the problem
- **Affected Documents**: Which documents need modification
- **Proposed Fix**: Detailed solution
- **Cross-Document Impact**: How fix affects other documents
- **Risk**: Potential for introducing new issues

**Example Fix Strategies**:
| Issue | Severity | Strategy | Impact |
|-------|----------|----------|--------|
| REQ-005 doesn't exist but referenced in arch | Critical | Remove REQ-005 ref OR map to existing REQ-003 | Architecture doc + Epic |
| EmailService in arch but not in epic tasks | Critical | Add Task-5 for EmailService OR remove from arch | Architecture + Epic |
| Task-4 references non-existent REQ-006 | Critical | Update Task-4 to reference REQ-004 | Epic |

Create a `plan.md` file documenting ALL fix strategies before proceeding.

### 3. User Confirmation
Present fix strategies to user and obtain approval:
- Show complete fix plan with all strategies
- Highlight cross-document impacts
- Request explicit confirmation before proceeding

**DO NOT** apply any fixes without user approval.

### 4. Sequential Fix Implementation
Apply fixes in severity order with careful tracking:

**For Each Fix** (Critical → High → Medium → Low):
1. Apply the approved fix to affected document(s)
2. Update `plan.md` with fix status
3. Verify cross-document consistency immediately
4. Document any unexpected impacts

**Critical: Maintain Consistency**
After each fix, verify:
- All references are valid (no broken links)
- No new conflicts introduced
- Cross-document mappings preserved
- Naming conventions consistent

### 5. Cross-Document Verification
After ALL fixes are applied, perform comprehensive verification:

**Verification Checklist**:
- [ ] All requirements referenced in architecture exist in `{REQ}/*.md`
- [ ] All architecture components referenced in epic exist in `{ARCH}/*.md`
- [ ] All tasks reference valid requirements
- [ ] All plans exist for epic tasks
- [ ] No fabricated entities remain
- [ ] No broken cross-references
- [ ] Consistent naming across documents
- [ ] 100% coverage maintained

Document verification results.

### 6. User Confirmation of Changes
Present complete change summary to user:
- List all documents modified
- Summary of changes made
- Verification results
- Any remaining issues (if any)

Obtain user confirmation that all changes are acceptable.

### 7. Cleanup and Recommendation
Only after user confirms changes are acceptable:

1. **Delete Validation Report**:
   ```bash
   rm {root}/docs/design-validation.md
   ```

2. **Provide Recommendation**:
   "Design conflicts resolved. Recommend re-running validation with /sunnycore_po *validate-design to confirm no new issues."

**DO NOT** delete validation report until all fixes are confirmed by user.

## [Steps]
1. Understand all issues, extract and prioritize. This categorizes and prioritizes issues.
2. Develop fix plans, obtain user confirmation. This creates approved fix plans for all issues.
3. Resolve all fixes in priority order, maintain consistency. This implements all fixes with consistency.
4. Review and validate changes, verify no new conflicts. This validates all fixes and confirms them.
5. Delete validation report, guide user to re-run validation. This completes cleanup with change summary.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] All approved fixes applied with cross-document consistency verified
- [ ] No new issues introduced, all changes confirmed by user
- [ ] Validation report "{root}/docs/design-validation.md" deleted

## [Example]

### Good #1
**Input**: Validation shows 3 critical: REQ-005 doesn't exist, EmailService fabricated, Task-4 references non-existent REQ-006  
**Decision**: Read validation. Extract all issues. Categorize: 3 critical (broken references). Create plan.md. Develop fix plans: Issue 1 - remove REQ-005 or map to REQ-003; Issue 2 - add EmailService to arch or remove refs; Issue 3 - update Task-4 to existing REQ. Present to user. User approves. Execute: update PRD (REQ-005→REQ-003), add EmailService to arch, update Task-4 to REQ-004. Verify cross-document consistency (all refs valid). User confirms. Delete validation report. Recommend re-run validation.  
**Why Good**: This resolves systematically with user approval, confirms consistency, and cleans up validation report.

### Good #2
**Input**: Validation shows coverage gaps: REQ-001 no arch mapping, COMP-003 not mapped to task, Task-2 no plan (medium severity)  
**Decision**: Analyze validation (3 medium coverage gaps). Categorize by type. Create plan.md with gap analysis. Develop strategies: Gap 1 - add AuthService to arch and map to REQ-001; Gap 2 - add Task-5 for Cache Layer; Gap 3 - create 2-plan.md. User approves. Execute: create AuthService in components.md with REQ-001 mapping, add Task-5 to epic.md with COMP-003 mapping, create plans/2-plan.md. Verify 100% coverage: all req have arch, all components have tasks, all tasks have plans. User confirms. Delete validation report.  
**Why Good**: This addresses coverage gaps holistically, restores full traceability, and documents completion.

### Bad #1
**Input**: Validation has 5 issues including critical fabricated content, broken refs, conflicts (mix severity)  
**Bad Decision**: Fix all simultaneously without prioritization. Skip user confirmation because fixes seem obvious. Apply fixes across multiple docs without tracking. Delete validation report immediately after changes. Don't verify new conflicts.  
**Why Bad**: This violates fix in severity order (should be Critical→High→Medium→Low), violates obtain user confirmation, creates untracked changes risking new inconsistencies, and violates not delete before fixes complete.  
**Correct**: Prioritize: Critical first, then High, Medium, Low. Document fix strategy in plan.md. Present to user, obtain approval before execution. Apply sequentially maintaining cross-doc consistency. After ALL fixes complete, verify no new conflicts. Obtain final user confirmation. Only then delete validation report.
