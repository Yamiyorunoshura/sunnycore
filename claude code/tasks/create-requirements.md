[Input]
  1. {root}/sunnycore/templates/requirement-tmpl.yaml --Requirement template
  2. User-provided initial ideas and requirement descriptions

[Output]
  1. {root}/docs/requirements/*.md --Complete requirement specifications (including functional requirements, non-functional requirements, and acceptance criteria)

[Constraints]
  1. Each requirement must be verifiable and measurable; vague or subjective wording is not allowed
  2. Section and field names must align exactly with the requirement template
  3. Examples must not contain sensitive or personal data
  4. This workflow transforms initial ideas into complete, testable requirements through structured interaction
  5. Use standardized requirement templates to ensure consistency and verifiability

[Tools]
  1. **todo_write**
    - [Step 1: Create task list; Steps 2-4: Track task progress]
  2. **sequentialthinking (MCP)**
    - [Step 1: Structured decomposition and reflective reasoning; Step 2: Systematically decompose complex functional requirements; Step 3: Cross-domain systematic non-functional requirement analysis; Step 4: Structured Given-When-Then and verification logic]
  3. **playwright_browser (MCP)**
    - [Step 2: Conduct web research when needed to obtain requirement examples]
  4. **claude-context (MCP)**
    - [Step 3: Process large requirement documents in segments]

[Tool-Guidelines]
  1. **todo_write**
    - Create a todo list in the initial phase, including all major tasks
    - Update the status of each completed step to completed
  2. **sequentialthinking (MCP)**
    - Simple task reasoning: 1-3 totalThoughts
    - Medium task reasoning: 3-5 totalThoughts
    - Complex task reasoning: 5-8 totalThoughts
    - If still uncertain after completing the original reasoning steps: nextThoughtNeeded = true
    - Must complete all configured reasoning steps
  3. **playwright_browser (MCP)**
    - Usage scenario: When referencing industry standards or example requirements
    - Avoid including sensitive or proprietary information
  4. **claude-context (MCP)**
    - Usage scenario: When requirement document input exceeds 5000 tokens or contains large amounts of complex content requiring segmented processing
    - Avoid using when content is already in memory and within token limits

[Steps]
  1. Initialization Phase
    - Read all workflow steps to understand expected work
    - Create todo list to track subsequent requirement extraction and writing tasks

  2. Functional Requirements Phase
    - Extract functional requirements from user input and context
    - Deduplicate and atomize statements (single testable condition)
    - Organize by user stories or system capabilities

  3. Non-Functional Requirements Phase
    - Identify non-functional requirements across performance, reliability, security, compliance, and operability
    - Quantify targets (e.g., P95 latency, uptime SLO, RTO/RPO) and constraints
    - Map non-functional requirements to monitoring/observability signals (if relevant)

  4. Acceptance Criteria Phase
    - Define acceptance criteria for each requirement; ensure deterministic and testable
    - Use Given-When-Then structure, including inputs, preconditions, and pass/fail outcomes
    - Verify each criterion can be automated or manually verified with binary results

  5. Finalization Phase
    - Cross-check functional requirements, non-functional requirements, and acceptance criteria; request user confirmation
    - Populate requirement template and write output to {root}/docs/requirements.md
    - Execute uv run {root}/sunnycore/scripts/shard-requirements.py; if it fails, log the error to {root}/logs/errors.log (including timestamp, error type, failure reason, impact scope) and notify the user
    - Check all DoD items one by one to ensure they are met
    - Confirm all todo items are completed

[DoD]
  - [ ] Functional requirements have been extracted, deduplicated, and atomized
  - [ ] Non-functional requirements have been identified and quantified (including performance, security, reliability, etc.)
  - [ ] Each requirement has corresponding acceptance criteria (using Given-When-Then structure)
  - [ ] Content is in English and uses numbered lists
  - [ ] Each requirement is measurable and verifiable
  - [ ] shard-requirements.py has been executed or errors have been logged to {root}/logs/errors.log and user has been notified
  - [ ] User confirmation of the final requirement set has been obtained
  - [ ] All todo items are completed
