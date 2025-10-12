**GOAL**: Create detailed functional and non-functional requirements documentation.

## [Input]
  1. "{TMPL}/requirement-tmpl.yaml" --Requirement template
  2. User-provided initial ideas and requirement descriptions

## [Output]
  1. "{root}/docs/requirements.md" (Markdown format)(temporary requiremenmt file. Will be sharded after running "shard-requirements.py")
  2. "{REQ}/*.md" --Complete requirement specifications (including functional requirements, non-functional requirements, and acceptance criteria)
  3. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not create vague or unmeasurable requirements
  2. Do not deviate from template structure and field names
  3. Do not include sensitive or personal data in examples
  4. Do not skip executing shard-requirements.py

## [Steps]
  1. Initialization & Scope Definition
    - Understand expected workflow and requirements gathering scope
    - Create plan.md at "{root}/docs/plan.md" for progress tracking
    - Outcome: Requirements gathering scope clearly defined and plan.md initialized

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

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - User requirement description summary (initial ideas and input)
  - Requirements extraction progress:
    * Functional requirements extracted (count, organized by categories)
    * Each functional requirement with ID and description
    * Deduplication status (duplicates identified and resolved)
  - Non-functional requirements progress:
    * Quality attributes defined (performance, security, reliability, etc.)
    * Each NFR with quantified metrics and targets
    * Measurability verified (specific metrics, not vague)
  - Acceptance criteria progress:
    * Requirements with acceptance criteria (count)
    * Given-When-Then format compliance
    * Testability verification (binary pass/fail outcomes)
  - Consistency check status (cross-requirement dependencies identified)
  - User approval status (draft/approved/revisions needed)
  - Sharding status (script execution, output files verified)

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

### Good Example 1
[INPUT]
User idea: "I want customers to search products by category, price range, and ratings with fast response"

[DECISION]
Step 1: Define scope - product search system. Step 2: Extract functional requirements - REQ-001 (category filter UI and logic), REQ-002 (price range slider and query), REQ-003 (rating filter 1-5 stars). Deduplicate and atomize. Step 3: Define NFRs - NFR-001 (search response time P95 <500ms), NFR-002 (support 100 concurrent users). Quantify with specific metrics. Step 4: Create acceptance criteria - Given user on product page, When applies category "Electronics" and price "$100-$500", Then system returns filtered results in <500ms. Binary pass/fail outcomes. Step 5: Generate docs/requirements.md. Obtain approval. Execute shard-requirements.py to create docs/requirements/functional.md and non-functional.md.

[OUTCOME]
Complete sharded requirements: docs/requirements/functional.md with REQ-001, REQ-002, REQ-003. docs/requirements/non-functional.md with NFR-001 (< 500ms), NFR-002 (100 users). All with Given-When-Then acceptance criteria. Verifiable and measurable. Sharding successful.

### Good Example 2
[INPUT]
User idea: "Send real-time notifications to users on iOS and Android when events occur with high reliability"

[DECISION]
Step 1: Define scope - push notification system. Step 2: Functional requirements - REQ-001 (event subscription management), REQ-002 (cross-platform delivery iOS/Android), REQ-003 (notification templates). Organized by capabilities. Step 3: NFRs - NFR-001 (delivery latency <2s), NFR-002 (99.9% delivery success rate), NFR-003 (handle 10K notifications/min). All quantified. Step 4: Acceptance criteria with specific metrics - Given event occurs, When notification sent, Then delivered to device within 2s. Step 5: Generate requirements.md. Approval obtained. Shard successfully.

[OUTCOME]
docs/requirements/functional.md with event-based notification requirements. docs/requirements/non-functional.md with quantified targets (< 2s latency, 99.9% success, 10K/min throughput). Verifiable acceptance criteria. Complete sharding to docs/requirements/*.md.

### Bad Example 1
[INPUT]
User describes multiple ideas with vague terms.

[BAD-DECISION]
Create vague requirements: "REQ-001: System should be user-friendly", "NFR-001: System should be fast". No quantification. No Given-When-Then format. Mix functional and non-functional together. Skip deduplication. No sharding script execution. Save as single file without following template.

[WHY-BAD]
Violates Constraint 1 (vague, unmeasurable requirements). Violates Requirements-Analysis-Guidelines point 1 (not verifiable, no clear success criteria). Violates Constraint 2 (deviate from template). Violates Constraint 4 (skip shard-requirements.py). "User-friendly" and "fast" are not testable. Unusable for implementation.

[CORRECT-APPROACH]
Follow Requirements-Analysis-Guidelines point 1: make requirements verifiable and measurable. Transform "user-friendly" to specific REQ: "REQ-001: Users can complete checkout in ≤3 clicks". Transform "fast" to quantified NFR: "NFR-001: API response time P95 <200ms". Use Given-When-Then: "Given user initiates checkout, When clicks checkout button, Then completes payment in ≤3 clicks". Separate functional from non-functional. Execute shard-requirements.py to generate proper structure.

### Bad Example 2
[INPUT]
Healthcare patient record access requirements with regulatory needs.

[BAD-DECISION]
Create functional requirements only, skip non-functional entirely. No security or compliance requirements. No data retention policies. Fabricate requirement IDs not from user input. Skip acceptance criteria step. No quantification of any quality attributes. Claim sharding complete without running script.

[WHY-BAD]
Violates Requirements-Analysis-Guidelines point 2 (no structured classification of functional vs non-functional). Missing critical NFRs for healthcare (HIPAA compliance, data retention). Violates Constraint 1 (fabricate IDs). Violates DoD (no acceptance criteria). Violates Constraint 4 (not execute sharding). Will fail regulatory audit.

[CORRECT-APPROACH]
Extract functional requirements: REQ-001 (role-based access), REQ-002 (audit logging), REQ-003 (search patient records). Extract NON-FUNCTIONAL requirements: NFR-001 (HIPAA compliance with specific controls), NFR-002 (audit log retention 7 years per regulation), NFR-003 (encrypt PHI at rest AES-256). Use Requirements-Analysis-Guidelines point 3 to quantify: retention period (7 years), encryption standard (AES-256). Create acceptance criteria aligned with regulations. Execute shard-requirements.py for proper output structure.
