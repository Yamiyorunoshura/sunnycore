**GOAL**: Fix design conflicts and inconsistencies identified in design validation report, then clean up the validation report file.

## [Input]
  1. "{root}/docs/design-validation.md" --Validation report with identified issues
  

## [Output]
  1. Modified design documents based on conflict resolution:
    - "{PRD}" (if PRD workflow was used)
    - "{REQ}/*.md" (if full workflow was used)
    - "{ARCH}/*.md" (if full workflow was used)
    - "{EPIC}" (if full workflow was used)
    - "{PLAN}/*.md" (if full workflow was used)
  2. Deleted: "{root}/docs/design-validation.md" (after successful fixes)
  
  
## [Constraints]
  1. Do not fix issues out of severity order (Critical → High → Medium → Low)
  2. Do not apply fixes without user confirmation of strategy
  3. Do not introduce new conflicts or inconsistencies during fixes
  4. Do not delete validation report before all fixes are complete

## [Steps]
  1. Issue Analysis & Prioritization
    - Understand all issues from validation report
    - Extract, group, and prioritize issues properly
    - Conceive the best solution for the task that needs to be completed
    - Outcome: Issues categorized and prioritized, plan outline documented

  2. Fix Planning & User Confirmation
    - Develop comprehensive fix plans for all issues
    - Obtain user confirmation for each fix strategy
    - Handle user feedback and revisions
    - Outcome: Approved fix plans for all issues

  3. Fix Execution & Consistency
    - Resolve all approved fixes in priority order
    - Maintain cross-document consistency
    - Verify fix completeness for each issue
    - Outcome: All fixes implemented with consistency maintained

  4. Validation & Review
    - Review and validate all changes
    - Verify no new conflicts or issues introduced
    - Obtain user confirmation for all fixes
    - Outcome: All fixes validated and confirmed

  5. Cleanup & Summary
    - Delete validation report after successful fixes
    - Guide user to re-run validation for confirmation
    - Provide comprehensive summary of changes
    - Outcome: Cleanup completed with change summary provided

## [Fix-Strategies]

### For Fabricated Content:
  - Remove fabricated references
  - Replace with actual existing entities
  - Add missing entities if they should exist

### For Broken References:
  - Update references to correct entity IDs
  - Create missing entities if needed
  - Remove orphaned references

### For Conflicts:
  - Identify authoritative source (usually requirements)
  - Update conflicting documents to match
  - Resolve contradictions by choosing one approach

### For Inconsistent Naming:
  - Establish canonical naming convention
  - Update all occurrences across all documents
  - Create glossary if needed

### For Coverage Gaps:
  - Add missing mappings (req → arch → task → plan)
  - Create missing entities if needed
  - Remove orphaned entities if they are not needed

### For Terminology Inconsistencies:
  - Standardize terms across all documents
  - Use find-and-replace for consistent updates
  - Document terminology decisions

## [Error-Handling]
  1. Validation report missing: Cannot proceed, ask user to run validate-design first
  2. Validation report shows no issues: Nothing to fix, inform user and exit gracefully
  3. User rejects all fix proposals: Document user's concerns and stop execution
  4. Fix introduces new conflicts: Revert changes and propose alternative approach
  5. Critical files cannot be modified: Report error and list problematic files

## [Conflict-Resolution-Guidelines]
  1. **Prioritize by Severity**
    - Fix in order: Critical → High → Medium → Low
    - Focus on issues that block development or cause cascading problems
    - Obtain user confirmation for each fix strategy before execution
  
  2. **Maintain Consistency**
    - When fixing references, update all related documents simultaneously
    - Establish canonical source of truth (usually requirements for functional specs)
    - Use consistent terminology and naming conventions across fixes
  
  3. **Preserve Traceability**
    - Ensure 100% bidirectional mapping after fixes: requirements ↔ architecture ↔ tasks ↔ plans
    - Verify no new orphaned entities or broken references introduced
    - Document rationale for each resolution decision
  
  4. **Validation After Fixes**
    - Recommend re-running validate-design after all fixes complete
    - Verify cross-document consistency maintained
    - Ensure no new conflicts introduced during fix process

## [DoD]
  - [ ] All approved fixes successfully applied with cross-document consistency verified
  - [ ] No new issues introduced and all changes confirmed by user
  - [ ] Validation report "{root}/docs/design-validation.md" deleted

## [Example]

### Good Example 1
[INPUT]
Validation report shows 3 critical issues: REQ-005 reference doesn't exist, EmailService component fabricated, Task-4 references non-existent REQ-006. All are broken reference issues.

[DECISION]
Read validation report and extract all issues. Categorize by severity (3 critical) and type (broken references). Create plan.md with issue list. Develop fix plans: Issue 1 - remove REQ-005 reference or map to existing REQ-003; Issue 2 - add EmailService to architecture or remove references; Issue 3 - update Task-4 to reference existing requirement. Present fix strategies to user for confirmation. User approves all fixes. Execute fixes in order: update PRD to map REQ-005→REQ-003, add EmailService component definition to architecture section, update Task-4 to reference REQ-004. Verify cross-document consistency (all references now valid). Obtain user confirmation. Delete validation report. Recommend re-running validation.

[OUTCOME]
Updated docs/PRD.md with all fixes applied: REQ-005 references now map to REQ-003, EmailService component added to architecture section with proper definition, Task-4 updated to reference REQ-004. All references verified valid. Cross-document consistency maintained. Validation report docs/design-validation.md deleted. User confirmed all fixes. Plan.md shows all issues resolved. Recommendation provided: Re-run validate-design to confirm zero issues.

[WHY-GOOD]
- Resolves every critical finding systematically with user approval, eliminating dangling references.
- Confirms consistency and cleans up the validation report, leaving the documentation set in a verified state.

### Good Example 2
[INPUT]
Validation report shows coverage gaps: REQ-001 has no architecture mapping, COMP-003 not mapped to any task, Task-2 has no implementation plan. Medium severity issues.

[DECISION]
Analyze validation report (3 medium-severity coverage gaps). Categorize issues by type (coverage gaps). Create plan.md with detailed gap analysis. Develop fix strategies: Gap 1 - add AuthService component to architecture and map to REQ-001; Gap 2 - add Task-5 to epic for Cache Layer; Gap 3 - create 2-plan.md for Task-2. Obtain user approval for fix strategies. Execute fixes: create AuthService in docs/architecture/components.md with REQ-001 mapping, add Task-5 to docs/epic.md with COMP-003 mapping, create docs/plans/2-plan.md following plan template. Verify 100% coverage: all requirements have architecture, all components have tasks, all tasks have plans. User confirms. Delete validation report.

[OUTCOME]
Updated docs/architecture/components.md with AuthService component mapped to REQ-001. Updated docs/epic.md with Task-5 for Cache Layer implementation mapped to COMP-003. Created docs/plans/2-plan.md with complete TDD structure for Task-2. 100% bidirectional coverage achieved across all documents. Cross-document consistency verified. Validation report deleted after user confirmation. Plan.md documents all gaps filled. Recommendation: Re-run validation for confirmation.

[WHY-GOOD]
- Addresses coverage gaps holistically—requirements, components, tasks, plans—restoring full traceability.
- Documents completion, deletes the stale report, and prompts re-validation, ensuring the fix cycle is closed properly.

### Bad Example 1
[INPUT]
Validation report shows 5 issues including critical fabricated content, broken references, and conflicts. Mix of severity levels.

[BAD-DECISION]
Fix all issues simultaneously without prioritization. Skip user confirmation because fixes seem obvious. Apply fixes across multiple documents without tracking consistency. Delete validation report immediately after making changes. Do not verify if new conflicts introduced.

[WHY-BAD]
Violates Constraint 1 (fix in severity order). Should prioritize Critical → High → Medium → Low. Violates Constraint 2 (apply fixes without user confirmation). User must approve strategies before execution. Untracked multi-document changes risk introducing new inconsistencies. Violates Constraint 4 (delete report before fixes complete). Cannot verify all issues resolved. No verification of new conflicts violates Step 4.

[CORRECT-APPROACH]
Prioritize issues by severity: Critical first, then High, Medium, Low. Document fix strategy for each issue in plan.md. Present strategies to user and obtain approval before execution. Apply fixes sequentially maintaining cross-document consistency. After ALL fixes complete, verify no new conflicts introduced. Obtain final user confirmation. Only then delete validation report per Constraint 4. Recommend re-running validation to confirm zero issues remain.

### Bad Example 2
[INPUT]
Validation report shows issue: REQ-003 conflicts with architecture component definition. Architecture says "synchronous API calls", requirements say "async for performance".

[BAD-DECISION]
Immediately decide that async is better and change requirements to match architecture. Do not consult user. Reasoning: "Async is modern best practice, so requirements must be wrong." Apply fix without documenting conflict or decision rationale.

[WHY-BAD]
Violates Constraint 2 (apply fixes without user confirmation). Conflicts require user input to determine authoritative source. Self-deciding which document is "correct" ignores business context. Requirements may intentionally specify async for valid business reasons. Not documenting rationale violates Conflict-Resolution-Guidelines. Unilateral decision may contradict business objectives.

[CORRECT-APPROACH]
Identify conflict between requirements (async) and architecture (sync). Document conflict clearly in plan.md with both positions. Present conflict to user: "Requirements specify async for performance, architecture specifies sync. Which is the authoritative source?" User clarifies requirements take precedence. Update architecture to match requirements (change sync→async). Document decision rationale in plan.md. Maintain both documents' consistency with agreed-upon approach. Obtain user confirmation before proceeding.
