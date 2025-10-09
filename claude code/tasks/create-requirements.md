**GOAL**: Create detailed functional and non-functional requirements documentation.

## [Input]
  1. "{TMPL}/requirement-tmpl.yaml" --Requirement template
  2. User-provided initial ideas and requirement descriptions

## [Output]
  1. "{root}/docs/requirements.md" (temporary requiremenmt file. Will be sharded after running "shard-requirements.py")
  2. "{REQ}/*.md" --Complete requirement specifications (including functional requirements, non-functional requirements, and acceptance criteria)

## [Constraints]
  1. Each requirement must be verifiable and measurable; vague or subjective wording is not allowed
  2. Section and field names must align exactly with the requirement template
  3. Examples must not contain sensitive or personal data
  4. This workflow transforms initial ideas into complete, testable requirements through structured interaction
  5. Use standardized requirement templates to ensure consistency and verifiability

## [Tools]
  1. **todo_write**
    - [Step 1: Create task list; Steps 2-4: Track task progress]
  2. **sequential-thinking (MCP)**
    - [Step 1: Structured decomposition of user stories and system capabilities]
    - [Step 2: Systematically decompose complex functional requirements into atomic requirements]
    - [Step 3: Transform abstract quality attributes into quantifiable non-functional requirements]
    - [Step 4: Validate logical completeness of Given-When-Then acceptance criteria]
  3. **playwright (MCP)**
    - [Step 2: When need to research competitor features or collect UI flow examples]
    - Use scenarios: Crawl competitor website feature flows, error handling approaches, UX design references
  4. **claude-context (MCP)**
    - [Step 3: Search codebase for similar requirement implementations and related modules]
    - Query examples: "How is similar functionality implemented?" "What are the related modules?"

## [Steps]
  1. Initialization Phase
    - Understand the expected workflow and requirements gathering scope
    - Establish progress tracking mechanism for requirement extraction tasks

  2. Functional Requirements Phase
    - Achieve complete, deduplicated, and atomized functional requirements
    - Ensure requirements are organized by user stories or system capabilities

  3. Non-Functional Requirements Phase
    - Achieve quantified non-functional requirements across all quality attributes
    - Ensure requirements have clear targets and measurable constraints

  4. Acceptance Criteria Phase
    - Achieve deterministic and testable acceptance criteria for all requirements
    - Ensure all criteria use Given-When-Then structure with binary outcomes

  5. Finalization Phase
    - Ensure consistency across all requirement types
    - Ensure user approval is obtained with proper feedback integration
    - Achieve successful requirement sharding by running the "shard-requirements.py" script with verified output under "{REQ}/"

## [Requirements-Analysis-Guidelines]
  1. **Verifiability First**
    - Each requirement must be testable and measurable with clear success/failure criteria
    - Avoid vague wording; use concrete, quantifiable metrics
  
  2. **Structured Classification**
    - Separate functional (what system does) from non-functional (quality attributes: performance, security, reliability)
    - Use Given-When-Then format for all acceptance criteria
  
  3. **Quantify Quality Attributes**
    - Non-functional requirements need specific metrics (e.g., "P95 latency < 200ms" not "fast response")
    - Transform abstract qualities into monitorable signals
  
  4. **Traceability & Dependencies**
    - Map requirement relationships and priorities
    - Identify preconditions and impact scope for each requirement

## [DoD]
  - [ ] Complete set of functional requirements exists, with all requirements being atomic, unique, and measurable
  - [ ] All non-functional requirements are identified with specific quantified metrics (including performance, security, reliability, etc.)
  - [ ] All requirements have clear acceptance criteria in Given-When-Then format
  - [ ] Requirements are successfully sharded into "{REQ}/*.md" files, or errors are logged to "{root}/logs/errors.log" and user is notified
  - [ ] Final requirement set is approved by user

## [Example]

### Example 1: E-commerce Product Search
[Input]
User idea: "I want customers to search products by category, price range, and ratings"

[Decision]
- Extract 3 functional requirements: REQ-001 (category filter), REQ-002 (price range filter), REQ-003 (rating filter)
- Define non-functional requirement: NFR-001 (search response time < 500ms)
- Create Given-When-Then acceptance criteria for each

[Expected Outcome]
- docs/requirements/functional.md with REQ-001, REQ-002, REQ-003
- docs/requirements/non-functional.md with NFR-001 (performance target)
- Each requirement has measurable acceptance criteria

### Example 2: Mobile Push Notification System
[Input]
User idea: "Send real-time notifications to users on iOS and Android when events occur"

[Decision]
- Functional requirements: REQ-001 (event subscription), REQ-002 (cross-platform delivery), REQ-003 (notification templates)
- Non-functional: NFR-001 (delivery latency < 2s), NFR-002 (99.9% delivery success rate)
- Acceptance criteria with specific metrics

[Expected Outcome]
- docs/requirements/functional.md with event-based notification requirements
- docs/requirements/non-functional.md with quantified reliability and performance targets
- Verifiable acceptance criteria using Given-When-Then format

### Example 3: Healthcare Patient Record Access
[Input]
User idea: "Doctors need secure access to patient medical history with audit trails"

[Decision]
- Functional: REQ-001 (role-based access), REQ-002 (audit logging), REQ-003 (search patient records)
- Non-functional: NFR-001 (HIPAA compliance), NFR-002 (audit log retention 7 years)
- Security-focused acceptance criteria

[Expected Outcome]
- docs/requirements/functional.md with access control and audit requirements
- docs/requirements/non-functional.md with compliance and data retention policies
- Acceptance criteria aligned with healthcare regulations
