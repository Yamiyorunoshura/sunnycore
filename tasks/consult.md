**GOAL**: Recommend optimal development workflow (full or PRD) based on requirement analysis.

## [Context]
**You must read the following context:**
- User requirement description
- `{ARCH}/*.md`(Only the related documents) (if exist)

## [Products]
- Workflow recommendation with command

## [Constraints]
- **MUST** correctly identify project type (Greenfield/Brownfield), **MUST NOT** misidentify
- **MUST** analyze existing architecture for Brownfield, **MUST NOT** skip
- **MUST** follow decision criteria, **MUST NOT** recommend incorrect workflow

## [Instructions]
1. **Step 1: Determine Project Type and Context**
- **GOAL:** Classify the initiative as Greenfield or Brownfield and capture supporting context.
- **STEPS:**
  - Gather the user requirement description and list all relevant `{ARCH}/` documents.
  - Assess whether architecture artifacts exist to confirm Greenfield or Brownfield status.
  - If Brownfield, review every referenced architecture file to note affected components, integration points, and scope of change.
- **QUESTIONS:**
  - Do `{ARCH}/` documents confirm an existing architecture or a blank slate?
  - Which current components or contracts will the work interact with?
  - What evidence supports the Greenfield vs. Brownfield classification?
- **CHECKLIST:**
  - [ ] Project type recorded with explicit evidence from the available context.
  - [ ] Notes captured on existing components or assumptions for a new build.

2. **Step 2: Analyze Scope and Architectural Impact**
- **GOAL:** Evaluate complexity, scale, and system impact of the requirement.
- **STEPS:**
  - Break the requirement into feature-level tasks to estimate scope.
  - Examine how the change affects component boundaries, contracts, and cross-cutting concerns (security, performance, observability).
  - Assess technology needs, confirming compatibility with the current stack or identifying additions.
- **QUESTIONS:**
  - How many feature-level tasks are necessary to deliver the requirement?
  - Will any components, boundaries, or contracts need to change?
  - Are new technologies or integrations required to satisfy the scope?
- **CHECKLIST:**
  - [ ] Task estimate documented with key drivers.
  - [ ] Architectural and cross-cutting impacts summarized.
  - [ ] Technology compatibility or required additions assessed.

3. **Step 3: Apply Decision Criteria and Recommend Workflow**
- **GOAL:** Select the appropriate workflow using the decision matrix criteria.
- **STEPS:**
  - Compare findings against Full Workflow (`*create-requirements`) triggers such as new components, architectural changes, or technology additions.
  - Validate whether all PRD (`*create-prd`) conditions hold: within existing boundaries, limited scope, compatible technology, no cross-cutting changes.
  - Choose the workflow that best aligns with the evidence and capture the justification referencing specific criteria.
- **QUESTIONS:**
  - Which Full Workflow criteria are satisfied by the analysis?
  - Do all PRD conditions remain true without exception?
  - What risks emerge if the recommended workflow is incorrect?
- **CHECKLIST:**
  - [ ] Workflow recommendation recorded with explicit criteria-based justification.
  - [ ] Rationale ties directly to scope, impact, and technology findings.
  - [ ] Risks or caveats of the decision noted for the user.

4. **Step 4: Provide Actionable Next-Step Command**
- **GOAL:** Deliver a clear command that guides the user to the next action.
- **STEPS:**
  - Select `/sunnycore_pm *create-requirements` or `/sunnycore_pm *create-prd` to match the recommendation.
  - Explain what the chosen command initiates for the user.
  - Highlight any prerequisites or immediate follow-ups needed before or after running the command.
- **QUESTIONS:**
  - Does the command align with the recommended workflow and project context?
  - What should the user prepare or verify before executing the command?
  - Which immediate outcomes or follow-up tasks should the user anticipate?
- **CHECKLIST:**
  - [ ] Command provided and consistent with the workflow recommendation.
  - [ ] Next-step explanation clarifies expected outcomes.
  - [ ] Prerequisites or follow-up actions identified for the user.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Project type determined with evidence and existing architecture analyzed (if Brownfield)
- [ ] Scope analysis completed with task estimates and architectural impact assessment
- [ ] Workflow recommendation provided with clear rationale based on decision criteria
- [ ] Actionable next-step command given to user

## [Example]

### Good #1: Proper Brownfield Analysis
**Input**: "Add product search with filters to e-commerce dashboard"  
**Analysis Process**: 
1. **Project Type**: Brownfield confirmed - existing Product Service + API Gateway architecture
2. **Scope Analysis**: Within existing Product Service boundaries, enhancing search functionality, estimated 2-3 tasks (search UI, filter API, index optimization)
3. **Decision Criteria**: Technology compatible (existing stack sufficient), limited scope, within boundaries, no architectural changes
4. **Recommendation**: PRD workflow - `/sunnycore_pm *create-prd`  
**Why Good**: Systematic analysis following the decision matrix, clear evidence-based reasoning.

### Good #2: Complex System Transformation
**Input**: "Migrate monolith to microservices"  
**Analysis Process**:
1. **Project Type**: Brownfield - existing monolithic architecture  
2. **Scope Analysis**: System transformation, multiple new services, service mesh patterns, estimated 10+ tasks, affects all components
3. **Decision Criteria**: New system components, architectural changes, technology additions, large scope - meets multiple "Full Workflow" criteria
4. **Recommendation**: Full workflow - `/sunnycore_pm *create-requirements`  
**Why Good**: Recognizes transformational scope with multiple qualifying criteria for full workflow.

### Bad #1: Insufficient Analysis
**Input**: "Add caching layer for API performance"  
**Bad Approach**: Immediately recommend full workflow without analysis  
**Why Bad**: Skips project type determination, no scope analysis, no architecture review  
**Correct Approach**: 
1. Check for existing architecture documents
2. Analyze scope: Redis middleware integration, 2-3 tasks, within existing API boundaries  
3. Apply criteria: Technology addition (Redis) but within existing boundaries, limited scope
4. Recommend PRD workflow with clear rationale
