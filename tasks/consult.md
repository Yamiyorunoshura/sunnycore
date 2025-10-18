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

## [Steps]
**You should work along to the following steps:**
1. Determine project type and gather context. This identifies whether the project is Greenfield or Brownfield with relevant context collected.
2. Analyze scope and architectural impact. This assesses the complexity, scale, and potential impact on existing systems.
3. Apply decision criteria and recommend workflow. This evaluates requirements against criteria to provide a clear workflow recommendation.
4. Provide actionable next-step command. This gives the user the specific command to execute next.

## [Instructions]

### 1. Project Type Determination
**How to determine project type:**
- **Check for existing architecture**: Look for any documents in `{ARCH}/` directory
- **Greenfield indicators**: No architecture documents, starting from scratch, completely new system
- **Brownfield indicators**: Existing architecture documents, extending/modifying existing system

**For Greenfield projects:**
- Focus on understanding the complete scope since everything will be built new
- Assess if the requirements justify a full architecture design process

**For Brownfield projects:**
- **Read ALL existing architecture documents** to understand current system
- **Identify integration points**: How will new functionality connect to existing components
- **Assess impact scope**: Will changes affect existing component boundaries, contracts, or patterns
- **Look for extension opportunities**: Can requirements be satisfied by extending existing components

### 2. Scope Analysis and Decision Criteria
**How to analyze scope and complexity:**
- **Count expected tasks**: Break down requirements into feature-level tasks to estimate scope
- **Assess architectural impact**: Will this require new components, change existing boundaries, or modify contracts
- **Evaluate technology needs**: Does this require new technology, frameworks, or external integrations
- **Identify cross-cutting concerns**: Does this involve security, performance, observability, or other system-wide aspects

**Decision Matrix - Use Full Workflow (*create-requirements) when ANY of these apply:**
- **New system components**: Requires creating new services, modules, or major subsystems
- **Architectural changes**: Modifying component boundaries, introducing new patterns, or changing system structure
- **Technology additions**: New frameworks, databases, external services, or infrastructure changes  
- **Cross-cutting impact**: Security policies, performance requirements, monitoring, or system-wide changes
- **Large scope**: Estimated 5+ feature-level tasks or complex interconnected requirements
- **System transformation**: Major changes like monolith-to-microservices, platform migrations, or architectural overhauls

**Use PRD Workflow (*create-prd) when ALL of these apply:**
- **Within existing boundaries**: Features can be implemented within current component structure
- **Technology compatible**: Current tech stack can satisfy all requirements
- **Limited scope**: Estimated 1-5 feature-level tasks with clear boundaries
- **Enhancement focused**: Feature additions, UI improvements, or bug fixes without architectural impact
- **No cross-cutting changes**: Doesn't require system-wide modifications or new patterns

### 3. Making and Presenting the Recommendation
**How to structure your analysis and recommendation:**

1. **State Project Type with Evidence**
   - Clearly state Greenfield or Brownfield
   - Provide specific evidence (e.g., "Architecture documents found in `{ARCH}/`" or "No existing architecture documents")
   - For Brownfield: Summarize key existing components that will be affected

2. **Present Scope Analysis**
   - **Task estimate**: "Estimated X feature-level tasks based on requirement breakdown"
   - **Architectural impact**: Describe what components/boundaries will be affected
   - **Technology assessment**: State whether current tech stack is sufficient
   - **Cross-cutting concerns**: Identify any system-wide implications

3. **Provide Clear Workflow Recommendation**
   - State recommended workflow (Full or PRD)
   - **Justify with criteria**: Explain which specific decision criteria led to this recommendation
   - **Risk assessment**: Mention any risks of choosing the wrong workflow
   
4. **Give Actionable Next Command**
   - Provide exact command: `/sunnycore_pm *create-requirements` or `/sunnycore_pm *create-prd`
   - Explain what the user should expect in the next step

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
