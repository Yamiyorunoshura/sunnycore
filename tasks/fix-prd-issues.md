**GOAL**: Fix issues identified during PRD acceptance phase.

## [Context]
**You must read the following context:**
- `{CUTOVER}` (required)
- `{PRD}` (required)
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
2. Reference PRD for context, conduct root cause analysis, document strategies in dev notes/progress. This identifies root causes with fix strategies documented.
3. Create comprehensive fix plan with risk assessment based on PRD. This creates detailed fix plan with risk assessment documented.
4. RED: Create failing tests reproducing issues, verify RED, record progress. This reproduces all issues with failing tests, status recorded.
5. GREEN: Implement minimal fixes to pass tests, verify all pass (exit code 0), record progress. This passes all tests with fixes, status recorded.
6. REFACTOR: Improve quality while maintaining green, re-run acceptance tests, record progress. This produces high-quality fixes with acceptance tests passing, status recorded.
7. Create complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md". This completes comprehensive fix documentation.

## [Instructions]

### 1. Issue Analysis with PRD Context
Extract ALL issues from cutover report and analyze with PRD context:

**For Each Issue**:
- Extract issue description and severity from cutover report
- Reference PRD to understand affected requirements
- Identify which PRD section (requirements, architecture, tasks) is impacted
- Understand expected vs actual behavior

**Severity Prioritization**: Critical → High → Medium → Low

### 2. PRD-Driven Root Cause Analysis
Conduct root cause analysis anchored in PRD specifications:

**Analysis Process**:
1. **Requirement Mapping**: Which PRD requirement does this issue violate?
2. **Architecture Review**: Which architecture component from PRD is involved?
3. **Root Cause Identification**: What is the underlying technical cause?
4. **Fix Strategy**: How to resolve while staying aligned with PRD?

**Root Cause Table**:
| Issue | Severity | PRD Requirement | Root Cause | Fix Strategy |
|-------|----------|----------------|------------|--------------|
| Push notifications fail | Critical | REQ-002 (notification delivery) | Missing FCM_SERVER_KEY config | Add FCM config + implement NotificationService per PRD architecture |

Document in dev notes or progress file for tracking.

### 3. Fix Planning Based on PRD Architecture
Create fix plans that align with PRD architecture:

**Fix Plan Components**:
- **Issue**: Clear description
- **PRD Context**: Relevant requirements and architecture sections
- **Root Cause**: Technical cause
- **Proposed Solution**: Fix approach aligned with PRD architecture
- **Files to Modify**: Code files to change
- **Risk Assessment**: Potential side effects
- **Testing Strategy**: How to verify fix

Record all fix plans in dev notes/progress before implementation.

### 4. TDD Fix Implementation
For EACH issue, follow TDD cycle with PRD as reference:

#### RED Phase
Create failing tests based on PRD acceptance criteria:
- Reference PRD Given-When-Then criteria for test scenarios
- Write tests that reproduce the issue
- Verify tests FAIL for the right reason
- Record progress in dev notes/progress

Example: For "Push notification failure" (REQ-002):
```javascript
// From PRD: "Given event occurs, When notification sent, Then delivered within 2s"
test('notification delivered within 2s', async () => {
  const result = await sendNotification({ event: 'order_placed' });
  expect(result.delivered).toBe(true);
  expect(result.deliveryTime).toBeLessThan(2000);
});
```

#### GREEN Phase
Implement minimal fix following PRD architecture:
- Refer to PRD architecture section for correct implementation approach
- Fix the issue with minimal code
- Verify tests PASS (exit code 0)
- Record progress in dev notes/progress

#### REFACTOR Phase
Improve quality while maintaining alignment with PRD:
- Apply patterns specified in PRD architecture
- Add error handling per PRD requirements
- Implement observability if specified in PRD
- Re-run tests to ensure green
- Record progress in dev notes/progress

### 5. PRD Alignment Verification
After each fix, verify alignment with PRD:
- Does implementation match PRD architecture?
- Are all PRD acceptance criteria met?
- Does solution follow PRD technology choices?
- Are PRD non-functional requirements satisfied?

### 6. Acceptance Re-Testing
Re-run acceptance tests matching PRD requirements:
- Test each affected PRD requirement
- Verify from end-user perspective per PRD scenarios
- Document results with evidence

**Success Criteria**:
- All PRD requirements pass acceptance tests
- No regressions in previously passing requirements
- Implementation aligns with PRD architecture

### 7. Comprehensive Documentation
Create `{root}/docs/cutover-fixes-dev-notes.md`:

**Must Include**:
- **Issues Summary**: All issues with PRD requirement mappings
- **Root Cause Analysis**: For each issue with PRD context
- **Fix Implementation**: Changes made following PRD architecture
- **TDD Progression**: RED → GREEN → REFACTOR for each fix
- **PRD Alignment**: How fixes align with PRD specifications
- **Acceptance Re-Test**: Results mapped to PRD requirements
- **Risk Mitigation**: How risks were addressed per PRD constraints

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] All issues resolved through full TDD cycle with all tests passing
- [ ] Acceptance tests re-executed with all issues resolved
- [ ] Complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md"

## [Example]

### Good #1
**Input**: Cutover shows critical: push notifications fail with "Invalid FCM token". PRD specifies REQ-002 for push notification delivery. Missing Firebase config  
**Decision**: Analyze issue (push notification failure). Prioritize: critical. Reference PRD for REQ-002 context. Root cause: FCM_SERVER_KEY missing from env config. Fix strategy: add FCM config and implement notification logic. Document in plan.md. RED: write test_send_notification expecting successful delivery (fails with config error). GREEN: add FCM_SERVER_KEY to .env, implement NotificationService.send() (test passes). REFACTOR: add error handling, retry logic, logging (tests stay green). Re-run acceptance for REQ-002 (push notifications deliver successfully). Document comprehensive fix.  
**Why Good**: This connects fix to PRD requirement, documents missing config, and validates through TDD and acceptance testing.

### Good #2
**Input**: Cutover lists 3 issues: critical auth failure, high-severity data validation missing, medium-severity UI inconsistency. PRD has relevant requirements  
**Decision**: Extract all 3 issues. Prioritize: critical (auth) first, then high (validation), then medium (UI). Reference PRD for each requirement context. Root cause analysis for each in plan.md. Fix strategy: Issue 1 - fix token validation; Issue 2 - add input validation middleware; Issue 3 - update UI components. Execute sequentially following TDD for each. RED: failing tests for all 3. GREEN: implement fixes until pass. REFACTOR: improve quality. Re-run acceptance for all 3 requirements. Document all fixes comprehensively in single dev notes.  
**Why Good**: This handles multiple issues with prioritized TDD cycles anchored in PRD requirements.

### Bad #1
**Input**: Cutover shows critical notification failure. PRD has relevant requirement  
**Bad Decision**: Quickly implement notification service without tests first. Add FCM config. Test manually (works on first try). Mark fixed without documentation. Skip re-running formal acceptance. Create minimal dev notes: "Fixed notifications. Added FCM."  
**Why Bad**: This violates TDD constraint (no RED phase proves issue existed), provides no test coverage for future regression, uses manual testing not systematic acceptance, and creates minimal dev notes violating documentation requirements.  
**Correct**: Execute full TDD: RED (write failing test proving notification failure)→GREEN (implement FCM integration until test passes)→REFACTOR (add error handling while keeping tests green). Re-run formal acceptance matching PRD requirements. Document complete root cause analysis, fix implementation, and risk assessment per dev-notes-tmpl.yaml.
