**GOAL**: Fix issues identified during acceptance phase.

## [Context]
**You must read the following context:**
- `{CUTOVER}` (required)
- `{REQ}/*.md` (required)
- `{ARCH}/*.md` (required)
- `{TMPL}/dev-notes-tmpl.yaml` (required)

## [Products]
- `{root}/docs/cutover-fixes-dev-notes.md`
- Fixed code
- Updated documentation if needed

## [Constraints]
- **MUST** address all cutover issues, **MUST NOT** leave any unaddressed
- **MUST** follow TDD cycle for fixes (RED→GREEN→REFACTOR), **MUST NOT** skip
- **MUST** re-run acceptance tests after fixes, **MUST NOT** skip
- **MUST** not introduce new issues or break existing functionality, **MUST NOT** cause regressions

## [Steps]
**You should work along to the following steps:**
1. Understand all issues, prioritize by severity. This prioritizes issues.
2. Reference req and arch, conduct root cause analysis, document in plan.md. This identifies root causes with fix strategies in plan.md.
3. Create comprehensive fix plan with risk assessment in plan.md. This creates detailed fix plan with risk assessment in plan.md.
4. RED: Create failing tests reproducing issues, verify RED, update plan.md. This reproduces all issues with failing tests, status in plan.md.
5. GREEN: Implement minimal fixes to pass tests, verify all pass (exit code 0), update plan.md. This passes all tests with fixes, status in plan.md.
6. REFACTOR: Improve quality while maintaining green, re-run acceptance tests, update plan.md. This produces high-quality fixes with acceptance tests passing, status in plan.md.
7. Create complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md". This completes comprehensive fix documentation.

## [Instructions]

### 1. Issue Extraction and Prioritization
Extract ALL issues from the cutover report and prioritize by severity:

**Severity Levels**:
- **Critical**: Blocks release, prevents core functionality
- **High**: Major impact, no workaround available
- **Medium**: Significant impact, workaround exists
- **Low**: Minor issue, minimal impact

**Prioritization Rule**: Fix issues in severity order (Critical → High → Medium → Low)

### 2. Root Cause Analysis
For EACH issue, conduct thorough root cause analysis:

Reference requirements and architecture for context:
- Which requirement is affected? (from `{REQ}/*.md`)
- Which architecture component is involved? (from `{ARCH}/*.md`)
- What was the expected behavior vs actual behavior?

**Root Cause Analysis Table**:
| Issue | Severity | Affected Requirement | Root Cause | Fix Strategy |
|-------|----------|---------------------|------------|--------------|
| CSV export timeout | Critical | REQ-003 (10K rows) | Loading entire dataset into memory | Implement streaming export |
| Push notifications fail | Critical | REQ-002 | Missing FCM_SERVER_KEY env var | Add config + implement notification logic |

Document this analysis in a `plan.md` file for tracking.

### 3. Fix Planning with Risk Assessment
For each issue, create a detailed fix plan:

**Fix Plan Components**:
- **Issue Description**: Clear description of the problem
- **Root Cause**: Underlying technical cause
- **Proposed Solution**: How the fix will work
- **Files to Modify**: List of files that will be changed
- **Risk Assessment**: Potential side effects or risks
- **Testing Strategy**: How to verify the fix works

Update `plan.md` with complete fix plans before implementing.

### 4. TDD Fix Implementation
For EACH issue, follow the complete TDD cycle:

#### RED Phase
Create failing tests that reproduce the issue:
- Write tests that demonstrate the bug/missing functionality
- Verify tests FAIL for the expected reason
- Update `plan.md` with RED phase status

Example: For "CSV export timeout with 10K rows":
```javascript
test('export 10K rows within 30s timeout', async () => {
  const result = await exportCSV({ rowCount: 10000 });
  expect(result).toCompleteWithin(30000); // Should fail initially
});
```

#### GREEN Phase
Implement minimal fixes to make tests pass:
- Fix the specific issue with minimal code changes
- Verify tests PASS (exit code 0)
- Do NOT introduce unrelated changes
- Update `plan.md` with GREEN phase status

#### REFACTOR Phase
Improve fix quality while maintaining green tests:
- Add error handling and validation
- Improve code structure if needed
- Add logging and observability
- Re-run tests to ensure they stay green
- Update `plan.md` with REFACTOR phase status

### 5. Regression Prevention
After implementing each fix, verify no regressions:
- Run ALL existing tests (not just new tests)
- Verify previously passing functionality still works
- Check that the fix doesn't introduce new issues

**Regression Check**: If ANY existing test fails, HALT and investigate before proceeding.

### 6. Acceptance Re-Testing
After ALL fixes are implemented, re-run acceptance tests:
- Test from end-user perspective (same as original cutover)
- Verify ALL issues are resolved
- Document results with evidence (screenshots, logs)

**Acceptance Criteria**:
- All critical issues: Fixed ✓
- All high issues: Fixed ✓
- All medium issues: Fixed ✓
- All low issues: Fixed ✓
- No new issues introduced ✓
- All existing functionality preserved ✓

### 7. Comprehensive Documentation
Create `{root}/docs/cutover-fixes-dev-notes.md` with complete fix documentation:

**Must Include**:
- **Issues Summary**: List of all issues with severity
- **Root Cause Analysis**: For each issue
- **Fix Implementation**: What was changed and why
- **TDD Progression**: RED → GREEN → REFACTOR for each fix
- **Test Results**: Before and after metrics
- **Acceptance Re-Test**: Results of re-running acceptance tests
- **Risk Mitigation**: How risks were addressed
- **Known Limitations**: Any remaining issues or technical debt

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] All issues resolved through full TDD cycle with all tests passing
- [ ] Acceptance tests re-executed with all issues resolved
- [ ] Complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md"

## [Example]

### Good #1
**Input**: Cutover shows high-severity: CSV export times out for >1000 rows. Requirements specify 10K rows. Architecture shows in-memory processing  
**Decision**: Analyze issue (export timeout). Prioritize: high severity. Reference REQ-003 (10K rows) and arch (in-memory). Root cause: loading entire dataset into memory causes timeout. Fix strategy: streaming export. RED: write test for 10K row export with 30s timeout (fails). GREEN: implement streaming CSV writer (passes at 12s). REFACTOR: add progress indicator, optimize query (tests stay green). Re-run acceptance (10K rows successfully). Document fix completely.  
**Why Good**: This anchors in requirement and architecture analysis, executes full TDD and acceptance retest, and produces evidence.

### Good #2
**Input**: Cutover identifies critical: push notifications fail with missing FCM key. Two separate issues  
**Decision**: Extract all issues (2 issues: FCM config missing, payload validation missing). Prioritize both critical. Root cause: Issue 1 - FCM_SERVER_KEY not in env; Issue 2 - payload validation missing. Create strategies in plan.md. RED: tests reproducing both (both fail). GREEN: add FCM_SERVER_KEY to env, implement validation (tests pass). REFACTOR: error handling and logging (tests stay green). Re-run acceptance for both (notifications deliver, invalid payloads rejected). Document all comprehensively.  
**Why Good**: This handles multiple critical issues systematically and updates config and documentation alongside code.

### Bad #1
**Input**: Cutover shows critical: export timeout for large datasets. Requirements specify 10K support  
**Bad Decision**: Skip TDD. Directly implement streaming without tests first. Test manually with 5K rows (works). Mark fixed. Skip re-running acceptance tests. Generate quick dev notes without root cause.  
**Why Bad**: This violates TDD constraint (no RED phase proves issue exists), provides no test coverage for future regressions, uses manual testing only 5K not verifying 10K requirement, and skips acceptance re-run.  
**Correct**: Execute full TDD: RED (write test for 10K rows, fails proving issue exists)→GREEN (implement streaming until passes)→REFACTOR (improve while keeping green). Re-run acceptance with actual 10K dataset. Document complete root cause analysis and metrics.
