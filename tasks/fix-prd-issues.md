**GOAL**: Fix issues identified during PRD acceptance phase.

## [Context]
**You must read the following context:**
- `{CUTOVER}` (required) - Contains issues to fix
- `{PRD}` (required) - Provides requirements and architecture context  
- `{TMPL}/dev-notes-tmpl.yaml` (required) - Output documentation structure

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
1. **Analyze Issues**: Extract and prioritize all issues from cutover report by severity
2. **Root Cause Analysis**: Map each issue to PRD requirements and identify underlying causes
3. **Plan Fixes**: Create fix strategies aligned with PRD architecture and assess risks
4. **RED Phase**: Write failing tests that reproduce each issue based on PRD acceptance criteria
5. **GREEN Phase**: Implement minimal fixes to make tests pass while following PRD architecture
6. **REFACTOR Phase**: Improve code quality and re-run acceptance tests to ensure PRD alignment
7. **Document Results**: Create comprehensive dev notes using the brownfield-fix-details template section

## [Instructions]

### Obtaining Information from Source Documents

**From Cutover Report**:
- Extract complete issue descriptions and severity levels
- Identify which requirements or features are affected
- Understand expected vs actual behavior from user perspective
- Note any configuration or setup problems mentioned

**From PRD Document**:
- Locate specific requirements (REQ-IDs) related to each issue
- Review architecture components and technology choices
- Understand acceptance criteria in Given-When-Then format
- Identify non-functional requirements that may be violated

**Prioritization Approach**: Address Critical → High → Medium → Low severity issues

### Root Cause Analysis Methodology

For each issue, trace the problem through three dimensions:
1. **Business Impact**: Which PRD requirement is violated and how?
2. **Technical Root Cause**: What is the underlying implementation gap?
3. **Architecture Alignment**: How should the fix integrate with PRD architecture?

Connect symptoms to root causes by examining:
- Missing configurations or environment setup
- Incomplete implementations or placeholder code
- Incorrect architecture pattern application
- Missing error handling or validation

### TDD Implementation Approach

**RED Phase Focus**: 
- Create tests that prove the issue exists using PRD acceptance criteria
- Ensure tests fail for the expected reason before proceeding
- Reference PRD Given-When-Then scenarios for test structure

**GREEN Phase Focus**:
- Implement minimal code to make tests pass
- Follow PRD architecture patterns and technology choices
- Avoid over-engineering - focus on making tests green

**REFACTOR Phase Focus**:
- Apply clean code principles while keeping tests green
- Add proper error handling and logging per PRD requirements
- Ensure final implementation matches PRD architecture quality standards

### Quality Validation Approach

After implementing fixes:
- Verify all affected PRD requirements now pass their acceptance criteria
- Run full test suite to ensure no regressions
- Confirm implementation follows PRD technology stack and patterns
- Test from end-user perspective matching original cutover scenarios

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] All issues resolved through full TDD cycle with all tests passing
- [ ] Acceptance tests re-executed with all issues resolved  
- [ ] Complete dev notes at "{root}/docs/cutover-fixes-dev-notes.md"

## [Examples]

### Good Approach
**Scenario**: Cutover shows critical push notification failure. PRD REQ-002 specifies notification delivery requirements.

**Approach**: Extract issue details and severity. Map to PRD REQ-002 requirements. Root cause: missing FCM configuration. Plan fix strategy following PRD architecture. RED: write failing test based on PRD acceptance criteria. GREEN: implement minimal FCM service. REFACTOR: add error handling per PRD standards. Re-run acceptance tests. Document comprehensive fix in dev notes.

**Why Good**: Follows TDD methodology, anchors fixes in PRD context, validates through acceptance testing.

### Poor Approach  
**Scenario**: Same notification failure.

**Poor Approach**: Implement notification service directly without tests. Add configuration and test manually. Mark as fixed without systematic validation or comprehensive documentation.

**Why Poor**: Skips TDD cycle, lacks systematic testing, provides no regression protection, insufficient documentation.
