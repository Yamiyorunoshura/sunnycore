**GOAL**: Analyze requirements and recommend the most suitable development workflow (full development workflow or PRD workflow).

## [Input]
  1. User requirement description
  2. (Conditional) "{ARCH}/*.md" --Existing architecture documents (if exist)
  3. "{TMPL}/plan-tmpl.yaml" --Unified planning template; tailor sections to capture requirement scope, workflow decision factors, and risk assessment

## [Output]
  1. Simple workflow recommendation (which command to use)
  

## [Constraints]
  1. Do not misidentify project type (Greenfield/Brownfield)
  2. Do not skip existing architecture analysis for Brownfield projects
  3. Do not provide verbose analysis unless explicitly requested
  4. Do not recommend workflows that violate Decision-Criteria

## [Steps]
  1. Initialization & Context Gathering
    - Determine project type (Greenfield/Brownfield)
    - Gather complete context for both project types
    - Create plan.md at "{root}/docs/plan.md" using the plan template to log project type evidence, information sources, and decision checkpoints
    - Outcome: Project type determined, context collected, and plan.md initialized

  2. Requirement Scope & Impact Analysis
    - Analyze requirement scope and architectural impact
    - Assess requirement complexity and workflow depth needed
    - Outcome: Requirement complexity assessed and impact identified

  3. Workflow Recommendation & Decision
    - Provide clear workflow recommendation based on analysis
    - Include decision criteria and rationale
    - Outcome: Clear workflow recommendation with complete rationale

  4. Finalization & Guidance
    - Provide concise, actionable recommendation
    - Specify next step command
    - Handle user requests for additional details
    - Outcome: User receives clear next-step action guidance

## [Progress-Tracking-Guidelines]
  **Content for plan.md:**
  - Project type determination (Greenfield/Brownfield)
  - User requirement summary (concise description)
  - Existing architecture analysis (if Brownfield - components, patterns, tech stack)
  - Scope assessment:
    * Estimated task count
    * New components/modules needed (yes/no)
    * Architecture pattern changes (yes/no)
    * Technology stack changes (yes/no)
  - Impact analysis (architectural impact level: none/low/medium/high)
  - Decision criteria evaluation results
  - Workflow recommendation with rationale (PRD or Full workflow)
  - Recommended command to execute next

## [Decision-Criteria]
  **Recommend Full Workflow (*create-requirements) when:**
  - Introduces new system components or modules
  - Changes core architecture patterns (e.g., monolith to microservices)
  - Requires new technology stack or frameworks
  - Adds new external integrations or third-party services
  - Modifies component boundaries or responsibilities
  - Significant cross-cutting concerns (security, observability architecture)
  - Large scope (estimated 5+ tasks)

  **Recommend PRD Workflow (*create-prd) when:**
  - Modifications within existing component boundaries
  - Feature enhancements using existing architecture
  - Bug fixes or technical improvements
  - UI/UX changes without backend architecture changes
  - Small to medium scope (estimated 1-5 tasks)
  - Does not introduce new modules or architectural patterns

## [Workflow-Analysis-Guidelines]
  1. **Scope Assessment**
    - Analyze if requirement introduces new components/modules or changes architecture patterns
    - Estimate task count and complexity (1-5 tasks = PRD; 5+ tasks = Full workflow)
  
  2. **Architecture Impact**
    - For Brownfield: check if existing contracts/boundaries are affected
    - Identify if new technology stack, integrations, or cross-cutting concerns are needed
  
  3. **Decision Criteria** (use Decision-Criteria section above for specifics)
    - Full workflow: architectural changes, new modules, 5+ tasks
    - PRD workflow: within existing boundaries, 1-5 tasks, no new patterns

## [DoD]
  - [ ] Project type correctly determined with requirement scope and impact analyzed
  - [ ] Clear workflow recommendation provided with specific command (*create-requirements or *create-prd)
  - [ ] User understands workflow recommendation and rationale

## [Example]

### Good Example 1
[INPUT]
User asks: "Add product search functionality with filters to existing e-commerce dashboard"
Existing architecture found in docs/architecture/ showing Product Service with API Gateway.

[DECISION]
Determine project type: Brownfield (architecture exists). Analyze scope: Feature addition within existing Product Service boundaries, no new modules needed. Estimated tasks: 2-3 (search endpoint, filter logic, UI integration). No architecture pattern changes. No new technology stack. Fits within existing component boundaries. Decision Criteria evaluation: Recommend PRD workflow (small scope, existing architecture sufficient, estimated 1-5 tasks).

[OUTCOME]
Clear recommendation: "Use /sunnycore_pm *create-prd - This is a small feature addition within existing architecture (2-3 tasks estimated, no architectural changes required). The search functionality can be implemented using existing Product Service and API Gateway."

[WHY-GOOD]
- Evaluates scope against documented architecture and decision criteria before choosing a workflow, avoiding knee-jerk escalation.
- Communicates the rationale explicitly, so the user understands why the PRD path fits.

### Good Example 2
[INPUT]
User requests: "Migrate current monolithic application to microservices for better scalability"
Existing architecture shows monolithic design with single database.

[DECISION]
Determine project type: Brownfield (existing monolithic architecture documented). Analyze scope: Fundamental architecture change, multiple new services needed (Order Service, Inventory Service, User Service, etc.). New patterns required (service mesh, API gateway, distributed data). New technology stack components (message queue, service discovery). Estimated tasks: 10+ (service extraction, data migration, API gateway setup, etc.). Major cross-cutting concerns (distributed tracing, circuit breakers). Decision Criteria evaluation: Recommend Full workflow (requires comprehensive architecture redesign).

[OUTCOME]
Clear recommendation: "Use /sunnycore_pm *create-requirements - This requires complete architecture redesign (introducing microservices pattern, estimated 10+ tasks, new service boundaries, distributed data management). A comprehensive requirements and architecture phase is necessary."

[WHY-GOOD]
- Recognizes the transformational nature of the request and maps it to the full workflow based on concrete scope indicators.
- Provides a justification that links architectural shifts, task volume, and new tech stack elements to the recommendation.

### Bad Example 1
[INPUT]
User wants to "add a caching layer to improve API performance"

[BAD-DECISION]
Immediately recommend full workflow without analyzing scope or existing architecture. Create plan.md but skip existing architecture review. Assume this requires new modules and architectural changes without verification.

[WHY-BAD]
Violates Constraint 1 (do not misidentify project type). Skips Constraint 2 (do not skip existing architecture analysis for Brownfield). Ignores Step 1 (determine project type and gather context). Violates Decision-Criteria by not properly assessing task count and architectural impact. Caching is typically a modification within existing boundaries, not requiring full workflow.

[CORRECT-APPROACH]
First determine if docs/architecture/ exists (Brownfield check). Read existing architecture to understand current setup. Analyze scope: adding Redis cache middleware is typically 2-3 tasks within existing API boundaries, no new modules. Check Decision-Criteria: modifications within existing boundaries, 1-5 tasks estimated, no new architecture patterns. Recommend PRD workflow with clear rationale explaining it's an enhancement to existing infrastructure.

### Bad Example 2
[INPUT]
User describes a complex multi-service platform with new payment gateway, notification system, and analytics pipeline. No existing architecture.

[BAD-DECISION]
Quickly recommend PRD workflow because "it's faster". Skip analysis of complexity and architectural impact. Ignore the fact that multiple new modules are being introduced. Provide recommendation without rationale or estimated task count.

[WHY-BAD]
Violates Constraint 4 (do not recommend workflows that violate Decision-Criteria). Skips Steps 1-2 (context gathering and scope analysis). Ignores Decision-Criteria indicators for full workflow: introduces multiple new components, requires new integrations, large scope (likely 5+ tasks). Violates Constraint 3 (do not provide verbose analysis unless requested) by not providing ANY rationale.

[CORRECT-APPROACH]
Analyze scope systematically: payment gateway = new module, notification system = new module, analytics pipeline = new module. Multiple new components and external integrations identified. Estimated tasks: likely 8-12 (payment integration, notification service, analytics ingestion, storage, reporting). Check Decision-Criteria: introduces new system components, adds multiple new third-party integrations, large scope estimated. Recommend full workflow with specific rationale: "/sunnycore_pm *create-requirements - Multiple new modules (payment, notifications, analytics) require comprehensive architecture design. Estimated 8-12 tasks with significant integration complexity."
