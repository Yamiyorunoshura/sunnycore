**GOAL**: Fix issues identified during acceptance phase by systematically addressing root causes through TDD and comprehensive testing.

## [Context]
**Read these context documents to understand issues and system design:**
- `{CUTOVER}` - Contains all issues found during acceptance testing with severity levels
- `{REQ}/*.md`(Only the related documents) - Shows what functionality was intended and acceptance criteria
- `{ARCH}/*.md`(Only the related documents) - Reveals system design, components, and technical decisions
- `{TMPL}/dev-notes-tmpl.yaml` - Provides structure for documentation output

## [Products]
- `{root}/docs/cutover-fixes-dev-notes.md` (comprehensive fix documentation)
- Fixed code addressing all issues
- Updated documentation if architectural changes made

## [Constraints]
- **MUST** address all cutover issues systematically, **MUST NOT** leave any unresolved
- **MUST** follow complete TDD cycle (RED→GREEN→REFACTOR) for each fix
- **MUST** re-run full acceptance tests to verify resolution
- **MUST** maintain existing functionality without introducing regressions

## [Steps]
1. **Extract and prioritize issues** - Analyze cutover report to identify all issues by severity (Critical→High→Medium→Low)
2. **Conduct root cause analysis** - Cross-reference requirements and architecture to understand why issues occurred
3. **Plan systematic fixes** - Create comprehensive fix strategy with risk assessment for each issue
4. **Execute TDD cycle** - For each issue: write failing test (RED) → implement minimal fix (GREEN) → improve quality (REFACTOR)
5. **Verify comprehensive resolution** - Re-run all acceptance tests and verify no new issues introduced
6. **Document fix implementation** - Create detailed development notes following template structure

## [Instructions]

### Issue Analysis and Planning
**Start by understanding the full scope:** Read the cutover report to extract all issues. Use severity levels (Critical→High→Medium→Low) to prioritize which issues block production vs. which can be addressed in follow-up releases.

**Conduct systematic root cause analysis:** For each issue, trace backwards from the symptom to understand WHY it occurred. Cross-reference the requirements documents to see what was intended, then examine the architecture documents to understand how the system should work. Look for gaps between intention (requirements), design (architecture), and reality (cutover issues).

**Create a comprehensive fix strategy:** Before writing any code, plan your approach for each issue. Consider which components need changes, what risks each fix introduces, and how fixes might interact with each other. Document your analysis in a working `plan.md` file to track progress.

### TDD Implementation Approach
**Follow disciplined TDD for each fix:** The RED→GREEN→REFACTOR cycle ensures you understand the problem (RED), solve it minimally (GREEN), then improve the solution (REFACTOR) while maintaining working code.

**RED Phase - Prove the problem exists:** Write tests that demonstrate each issue. If a feature is missing, write tests that expect the feature to work. If a bug exists, write tests that expose the bug. Verify these tests fail for the right reasons before proceeding.

**GREEN Phase - Solve minimally:** Implement the simplest possible fix to make your tests pass. Focus on correctness first, elegance later. Verify all tests pass (including existing ones) before moving on.

**REFACTOR Phase - Improve quality:** Once tests are green, improve your implementation. Add proper error handling, logging, validation, and documentation. Ensure code quality meets standards while keeping all tests passing.

### Quality Assurance and Verification
**Prevent regressions systematically:** After each fix, run the full test suite to ensure existing functionality remains intact. If any existing tests fail, investigate immediately - your fix may have unintended consequences.

**Validate end-to-end resolution:** Once all fixes are implemented, re-run the same acceptance tests that revealed the original issues. Test from the user's perspective to ensure problems are truly resolved, not just masked.

**Maintain comprehensive documentation:** Use the dev-notes template to document your analysis, decisions, and implementation. Focus on the reasoning behind your fixes and any trade-offs made. This knowledge is critical for future maintenance and similar issues.

## [Quality-Gates]
**All gates must pass before completion:**
- [ ] All cutover issues systematically resolved through complete TDD cycle
- [ ] Full test suite passing (no regressions introduced)
- [ ] Acceptance tests re-executed with all original issues confirmed resolved
- [ ] Comprehensive development notes created following template structure

## [Examples]

### Effective Approach
**Scenario**: Cutover shows critical CSV export timeout for 10K rows, requirements specify this capacity, architecture shows in-memory processing.

**Analysis**: Cross-reference REQ-003 (10K row support) with architecture (in-memory loading) to identify root cause - memory limitations causing timeout.

**Implementation**: Follow TDD - write failing test for 10K rows within acceptable time limits, implement streaming solution to pass test, refactor for error handling and monitoring. Re-run acceptance tests to confirm resolution.

**Documentation**: Record root cause analysis linking requirements gap to architectural limitation, document streaming implementation decision and performance improvements achieved.

### Common Pitfalls to Avoid
**Incomplete Analysis**: Jumping to solutions without understanding requirements context or architectural constraints leads to Band-Aid fixes rather than systematic resolution.

**Skipping TDD Discipline**: Implementing fixes without first writing failing tests provides no regression protection and doesn't prove the issue is actually resolved.

**Inadequate Verification**: Not re-running acceptance tests means you may have fixed symptoms rather than root causes, leaving users with unresolved problems.
