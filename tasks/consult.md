**GOAL**: Analyze requirements and recommend the most suitable development workflow (full development workflow or PRD workflow).

## [Input]
  1. User requirement description
  2. (Conditional) "{ARCH}/*.md" --Existing architecture documents (if exist)

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
    - Create plan.md at "{root}/docs/plan.md" for progress tracking
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

### Example 1: Add Search Feature to Existing App
[Input]
- User requirement: "Add product search functionality with filters"
- Project type: Brownfield (docs/architecture/ exists with API Gateway, Product Service)

[Decision]
- Scope: Small (within existing Product Service boundaries, no new modules)
- Impact: No architecture changes (uses existing API, adds new endpoint)
- Estimated tasks: 2-3 (search endpoint, filter logic, UI integration)
- Recommendation: PRD workflow (small scope, existing architecture sufficient)

[Expected Outcome]
- Recommendation: "Use `/sunnycore_pm *create-prd` - This is a small feature addition within existing architecture (2-3 tasks estimated)"
- Rationale: No new components needed, fits within current Product Service

### Example 2: Migrate to Microservices Architecture
[Input]
- User requirement: "Break monolith into microservices for better scalability"
- Project type: Brownfield (docs/architecture/ shows monolithic architecture)

[Decision]
- Scope: Large (fundamental architecture change, multiple new services)
- Impact: Major (changes system boundaries, adds service mesh, new deployment model)
- Estimated tasks: 10+ (service extraction, API gateway, data migration, etc.)
- Recommendation: Full workflow (requires comprehensive architecture redesign)

[Expected Outcome]
- Recommendation: "Use `/sunnycore_pm *create-requirements` - This requires architecture redesign (microservices pattern, 10+ tasks estimated)"
- Rationale: Introduces new architectural patterns and multiple new components

