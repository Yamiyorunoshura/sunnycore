**GOAL**: Execute project acceptance validating deliverables from business and user perspectives.

## [Context]
**You must read the following context:**
- `{PRD}` (required)
- `{TMPL}/cutover-report-tmpl.yaml` (required)

## [Products]
- `{CUTOVER}`

## [Constraints]
- **MUST** test from end-user perspective, **MUST NOT** perform technical testing
- **MUST** halt if required inputs missing, **MUST NOT** proceed
- **MUST** test all critical requirements, **MUST NOT** skip any
- **MUST** follow template structure, **MUST NOT** deviate
- **CRITICAL**: **MUST** reject ANY production code with mock/stub/hardcoded values regardless of functional tests (auto-Fail; tests using mocks OK), **MUST NOT** accept

## [Instructions]
1. **Step 1: Validate Inputs**
- **GOAL:** Confirm prerequisite documents are present and usable before any testing work begins.
- **STEPS:**
  - Open `{PRD}` and confirm it includes project scope, requirement identifiers (REQ-/NFR-), and success criteria.
  - Review `{TMPL}/cutover-report-tmpl.yaml` to understand each required report section and expected outputs.
  - Stop immediately and record the blocker if either document is missing, outdated, or incomplete.
- **QUESTIONS:**
  - Do I have the latest versions of the PRD and cutover template?
  - Are any mandatory sections or requirement IDs absent?
  - What approvals or inputs are missing before I can proceed?
- **CHECKLIST:**
  - [ ] `{PRD}` accessibility and completeness confirmed
  - [ ] Template structure reviewed and understood
  - [ ] Blockers logged if documents are deficient

2. **Step 2: Scan Production Code Integrity**
- **GOAL:** Ensure production code is free of mocks, stubs, TODOs, or hardcoded values that violate acceptance criteria.
- **STEPS:**
  - Identify production code directories and prioritize business logic, integrations, and configuration files.
  - Search for keywords (e.g., "mock", "stub", "TODO", placeholder credentials) and inspect flagged areas manually.
  - If any production mocks/stubs/hardcoded values exist, document evidence and mark the engagement as failed before proceeding.
- **QUESTIONS:**
  - Have I covered all production modules, including background jobs and configuration files?
  - Are any test doubles or placeholders leaking into production paths?
  - What evidence do I need to justify an automatic fail decision?
- **CHECKLIST:**
  - [ ] Code scan completed across all production paths
  - [ ] Findings recorded with locations and impact
  - [ ] Automatic fail applied if disallowed artifacts exist

3. **Step 3: Extract Business Acceptance Scope**
- **GOAL:** Define the business-critical workflows and criteria that acceptance testing must cover.
- **STEPS:**
  - From `{PRD}`, list critical user journeys, functional requirements (REQ-xxx), and non-functional requirements (NFR-xxx) tied to business value.
  - Capture success criteria and acceptance conditions for each critical requirement.
  - Map each requirement to the relevant section of `{CUTOVER}` output to ensure coverage during reporting.
- **QUESTIONS:**
  - Which requirements are critical versus high/medium priority?
  - What business outcomes define success for each requirement?
  - Are there dependencies or assumptions called out in the PRD that affect testing?
- **CHECKLIST:**
  - [ ] Critical requirements and user journeys enumerated
  - [ ] Success criteria documented for each critical item
  - [ ] Requirement-to-report section mapping prepared

4. **Step 4: Prepare Environment**
- **GOAL:** Establish a working environment that mirrors target deployment and surface setup gaps.
- **STEPS:**
  - Identify required configuration items (e.g., API keys, feature flags) using the template’s Configuration Requirements section.
  - Follow documented setup steps, noting durations, dependencies, and any deviations.
  - Log issues, missing instructions, or blockers encountered during setup for later reporting.
- **QUESTIONS:**
  - Do I have all necessary credentials and configuration values?
  - Which dependencies (tools, services) must be installed or verified?
  - What setup pain points could impact production readiness?
- **CHECKLIST:**
  - [ ] Configuration item list compiled with statuses
  - [ ] Environment setup executed or blocked itemized
  - [ ] Setup issues captured with impact notes

5. **Step 5: Execute Project**
- **GOAL:** Run the project in the prepared environment to validate startup readiness.
- **STEPS:**
  - Launch the application using documented commands or scripts, capturing runtime timestamps.
  - Observe startup behavior, logging URLs, ports, credentials, and any console output or errors.
  - Document unresolved errors or performance anomalies for inclusion in project execution section.
- **QUESTIONS:**
  - Did the project start successfully without manual fixes?
  - What errors or warnings appeared during execution?
  - Are access points (URL, port, credentials) clear for testers?
- **CHECKLIST:**
  - [ ] Startup command executed with outcome recorded
  - [ ] Access information documented for the report
  - [ ] Execution errors or anomalies captured

6. **Step 6: Run End-User Acceptance Tests**
- **GOAL:** Validate critical requirements from an end-user perspective and gather evidence.
- **STEPS:**
  - For each critical REQ/NFR, design user-facing test scenarios aligned with documented success criteria.
  - Execute workflows in the running environment, focusing on business outcomes instead of internal implementations.
  - Capture evidence (screens, logs, responses) and mark Pass/Fail/Not Tested with business impact notes.
  - Record any issues discovered, including reproduction steps and severity.
- **QUESTIONS:**
  - Have I covered every critical requirement outlined in Step 3?
  - What user-facing symptoms indicate failure or unmet expectations?
  - Is additional context needed to explain partial successes or failures?
- **CHECKLIST:**
  - [ ] All critical requirements tested or documented as not testable
  - [ ] Evidence collected and organized per requirement
  - [ ] Issues logged with severity and business impact

7. **Step 7: Compile Assessment & Reporting**
- **GOAL:** Populate the cutover report with findings and determine final status.
- **STEPS:**
  - Fill each section of `{CUTOVER}` using data gathered (configuration, setup, execution, acceptance tests, issues).
  - Apply decision criteria (Success / Partial Success / Failed) based on requirement outcomes and code integrity.
  - Highlight business impact, recommended actions, and deployment readiness blockers.
- **QUESTIONS:**
  - Does the report clearly justify the selected status with evidence?
  - Are all mandatory template sections completed without omissions?
  - What immediate actions are required before production?
- **CHECKLIST:**
  - [ ] Cutover report sections populated per template guidance
  - [ ] Final status selected with supporting rationale
  - [ ] Recommendations and blockers documented

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] **CRITICAL**: Production code scanned, NO mock/stub/hardcoded values (tests using mocks OK)
- [ ] All critical business requirements tested from end-user perspective with results recorded
- [ ] Complete cutover report generated following template structure
- [ ] All issues documented with severity and business impact