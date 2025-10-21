**GOAL**: Execute project acceptance validation from business and user perspectives.

## [Context]
**You must read the following context:**
- `{REQ}/*.md`(Only the related documents) (required)
- `{ARCH}/*.md`(Only the related documents) (required)
- `{TMPL}/cutover-report-tmpl.yaml` (required)

## [Products]
- `{CUTOVER}`

## [Constraints]
- **MUST** verify architecture alignment, **MUST NOT** accept architectural deviations (auto-reject)
- **MUST** scan production code for mocks/stubs/hardcoded values, **MUST NOT** accept any found (auto-reject; tests using mocks OK)
- **MUST** test from end-user perspective, **MUST NOT** perform technical testing
- **MUST** halt if required inputs missing, **MUST NOT** proceed without complete input set

## [Instructions]
1. **Step 1: Confirm Required Inputs**
- **GOAL:** Ensure every prerequisite document and template needed for cutover validation is present and complete.
- **STEPS:**
  - Map the scope to the relevant `{REQ}` and `{ARCH}` files plus `{TMPL}/cutover-report-tmpl.yaml`.
  - Review each input for completeness, current version, and absence of blocking TODO/FIXME notes.
  - Record missing or outdated inputs and halt until they are resolved.
- **QUESTIONS:**
  - Which requirement and architecture documents apply to this cutover?
  - Are there pending updates or approvals that change the baseline inputs?
  - Does the cutover template reflect the latest project context?
- **CHECKLIST:**
  - [ ] Required `{REQ}` documents verified and scoped.
  - [ ] Required `{ARCH}` documents verified and scoped.
  - [ ] `{TMPL}/cutover-report-tmpl.yaml` confirmed accessible and current.

2. **Step 2: Validate Architecture Alignment (AUTO-REJECT)**
- **GOAL:** Confirm the implementation matches architectural intent before proceeding to execution or testing.
- **STEPS:**
  - Trace implemented components against architecture diagrams, patterns, and interface contracts.
  - Follow critical data flows end-to-end to confirm sequencing and technology usage match specifications.
  - Log alignment results and immediately mark an automatic rejection if any deviation appears.
- **QUESTIONS:**
  - Do component responsibilities and boundaries mirror the architecture?
  - Are mandated patterns or technologies bypassed or substituted?
  - Does the runtime data flow reflect the documented diagrams?
- **CHECKLIST:**
  - [ ] Component responsibilities match architectural documentation.
  - [ ] Data flow, interfaces, and tech stack verified against `{ARCH}`.
  - [ ] No architecture deviations detected; otherwise process halted.

3. **Step 3: Scan Production Code Readiness (AUTO-REJECT)**
- **GOAL:** Ensure production code paths are free from mocks, stubs, or hardcoded values prior to execution.
- **STEPS:**
  - Search production directories for mock objects, stubbed responses, and hardcoded credentials or configuration.
  - Inspect TODO/FIXME annotations and confirm none affect production execution paths.
  - Document findings and stop the cutover if any incomplete implementation exists.
- **QUESTIONS:**
  - Are any production modules still referencing test doubles or placeholder logic?
  - Do configuration values originate from secure, environment-driven sources?
  - Have all TODO/FIXME notes been resolved or justified outside production paths?
- **CHECKLIST:**
  - [ ] No mocks or stubs present in production execution paths.
  - [ ] No hardcoded secrets or configuration detected.
  - [ ] Outstanding TODO/FIXME items audited and cleared for production.

4. **Step 4: Prepare and Document Environment**
- **GOAL:** Establish a reproducible environment configuration aligned with project requirements.
- **STEPS:**
  - Compile required environment variables, external services, and infrastructure dependencies from documentation.
  - Configure the environment following recorded setup steps, noting command sequences and prerequisites.
  - Capture issues, resolutions, and any deviations needed to achieve a working setup.
- **QUESTIONS:**
  - What configuration items are mandatory for this environment tier?
  - Were there undocumented dependencies or credentials required during setup?
  - How will future users recreate the environment without gaps?
- **CHECKLIST:**
  - [ ] Environment variables, services, and infrastructure requirements documented.
  - [ ] Setup steps executed and validated for reproducibility.
  - [ ] Configuration issues captured with resolutions or blockers.

5. **Step 5: Execute System and Verify Basic Functionality**
- **GOAL:** Confirm the application launches successfully and core workflows operate at a smoke-test level.
- **STEPS:**
  - Start the system using documented commands or scripts and verify startup diagnostics.
  - Perform primary health checks or smoke scenarios to ensure key services respond.
  - Capture evidence (logs, screenshots, timestamps) showing the system operates as expected.
- **QUESTIONS:**
  - Did the system start without critical errors or degraded components?
  - Which baseline workflows prove the system is operational?
  - What evidence best demonstrates successful execution?
- **CHECKLIST:**
  - [ ] Startup completed with no blocking errors.
  - [ ] Core smoke scenarios executed successfully.
  - [ ] Execution evidence collected and stored for the report.

6. **Step 6: Validate Critical Requirements from User Perspective**
- **GOAL:** Demonstrate that critical business workflows deliver expected outcomes for end users.
- **STEPS:**
  - Map each critical requirement to user-focused test scenarios derived from `{REQ}`.
  - Execute Given-When-Then style tests covering business flows, capturing outcomes and artifacts.
  - Record pass/fail status with rationale, linking issues to affected requirements.
- **QUESTIONS:**
  - Which user journeys are critical for business acceptance?
  - Do observed outcomes satisfy the acceptance criteria defined in `{REQ}`?
  - What deviations or usability concerns surfaced during execution?
- **CHECKLIST:**
  - [ ] All critical business workflows tested end-to-end.
  - [ ] Evidence captured for each requirement outcome.
  - [ ] Failures mapped to requirement IDs with user-impact notes.

7. **Step 7: Compile Cutover Report and Decision**
- **GOAL:** Produce the `{CUTOVER}` report summarizing findings and documenting the acceptance decision.
- **STEPS:**
  - Populate `{TMPL}/cutover-report-tmpl.yaml` sections with validated data, evidence, and configuration notes.
  - Summarize requirement results, issues, and risk posture, referencing success/partial/fail criteria.
  - State the acceptance decision (Success / Partial Success / Failed) and any conditions or next actions.
- **QUESTIONS:**
  - Does the collected evidence justify the proposed cutover status?
  - Are blockers or risks clearly documented with ownership and timelines?
  - What immediate follow-up steps are required post-report?
- **CHECKLIST:**
  - [ ] Report sections completed with accurate data and references.
  - [ ] Acceptance decision recorded with supporting rationale.
  - [ ] Next steps and conditions captured for stakeholders.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] **CRITICAL**: Implementation verified to align with architecture specifications
- [ ] **CRITICAL**: Production code verified free of mocks/stubs/hardcoded values  
- [ ] All critical requirements tested from end-user perspective with documented results
- [ ] Environment setup documented and verified functional
- [ ] Complete cutover report generated with clear acceptance decision
