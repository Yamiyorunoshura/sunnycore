**GOAL**: Create detailed functional and non-functional requirements documentation.

## [Input]
  1. "{TMPL}/requirement-tmpl.yaml" --Requirement template
  2. User-provided initial ideas and requirement descriptions

## [Output]
  1. "{root}/docs/requirements.md" (Markdown format)(temporary requiremenmt file. Will be sharded after running "shard-requirements.py")
  2. "{REQ}/*.md" --Complete requirement specifications (including functional requirements, non-functional requirements, and acceptance criteria)

## [Constraints]
  1. Do not create vague or unmeasurable requirements
  2. Do not deviate from template structure and field names
  3. Do not include sensitive or personal data in examples
  4. Do not skip executing shard-requirements.py

## [Steps]
  1. Initialization & Scope Definition
    - Understand expected workflow and requirements gathering scope
    - Establish progress tracking mechanism
    - Outcome: Requirements gathering scope clearly defined

  2. Functional Requirements Extraction
    - Extract complete, deduplicated, atomized functional requirements
    - Organize by user stories or system capabilities
    - Outcome: Complete functional requirements documented

  3. Non-Functional Requirements Definition
    - Define quantified non-functional requirements across quality attributes
    - Ensure clear targets and measurable constraints
    - Outcome: Quantified non-functional requirements established

  4. Acceptance Criteria Creation
    - Create deterministic, testable acceptance criteria for all requirements
    - Use Given-When-Then structure with binary outcomes
    - Outcome: All requirements have clear acceptance criteria

  5. Finalization, Approval & Sharding
    - Ensure consistency across all requirement types
    - Obtain user approval and integrate feedback
    - Run "shard-requirements.py" to generate "{REQ}/*.md" files
    - Outcome: Approved requirements successfully sharded

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
  - [ ] Complete functional and non-functional requirements with quantified metrics and Given-When-Then acceptance criteria
  - [ ] Requirements successfully sharded to "{REQ}/*.md" files using shard-requirements.py
  - [ ] Final requirement set approved by user

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
