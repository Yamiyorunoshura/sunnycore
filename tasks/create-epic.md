**GOAL**: Create feature-level task list breaking down requirements into executable tasks.

## [Context]
**You must read the following context:**
- `{REQ}/*.md` - Requirements documents
- `{ARCH}/*.md` - Architecture documents
- `{TMPL}/epic-tmpl.yaml` - Epic output format template

## [Products]
- `{EPIC}` - Feature-level task list with full requirement-architecture traceability

## [Constraints]
- **MUST** create feature-level tasks, **MUST NOT** go below feature granularity
- **MUST** focus on deliverables, **MUST NOT** include operational actions unless requested
- **MUST** use kebab-case, **MUST NOT** use spaces in file names
- **MUST** achieve 100% requirement coverage (every REQ-XXX and NFR-XXX mapped to tasks)
- **MUST** map tasks to architecture components from Components section

## [Steps]
**You should work along to the following steps:**
1. **Parse source documents.** Extract all REQ-XXX, NFR-XXX from requirements; extract Components, Technical Stack, and Requirements Traceability Matrix from architecture.
2. **Identify features from architecture components.** Each Component section represents a deliverable feature. Match components to requirements using the Traceability Matrix.
3. **Create feature-level task breakdown.** Generate one task per major component or logical feature grouping. Ensure task granularity is 1-3 days of work.
4. **Verify coverage and dependencies.** Check 100% requirement coverage, identify task dependencies from component dependencies in architecture.
5. **Complete draft, obtain approval, save to "{EPIC}".** Apply epic-tmpl.yaml format and save approved document.

## [Instructions]

### 0. How to Parse Source Documents

**A. Requirements Document Analysis (`{REQ}/*.md`)**

Extract the following from requirements documents:

1. **Functional Requirements (REQ-XXX):**
   - Located in "Functional Requirements" section
   - Format: `## REQ-{id}: {Title}`
   - Each has Description, Acceptance Criteria, Priority, Dependencies
   - **Action:** List all REQ-XXX IDs and their titles

2. **Non-Functional Requirements (NFR-XXX):**
   - Located in "Non-Functional Requirements" section
   - Format: `## NFR-{id}: {Title}`
   - Categories: Performance, Security, Reliability, Usability, Maintainability, Scalability
   - **Action:** List all NFR-XXX IDs and determine which require dedicated implementation tasks vs. which are addressed through architectural patterns

**B. Architecture Document Analysis (`{ARCH}/*.md`)**

Extract the following from architecture documents:

1. **Components Section (Primary Source for Tasks):**
   - Format: `## {Component Name}` under "Components" section
   - Each component has: Responsibility, Technology, Key Interfaces/APIs, Dependencies, Data Storage
   - **Action:** Each component typically becomes one feature-level task
   - **Marked status:** For brownfield, components are marked as New/Modified/Existing

2. **Requirements Traceability Matrix:**
   - Table format: `| Requirement ID | Requirement Title | Architecture Elements | Implementation Notes |`
   - **Action:** Use this to map REQ/NFR → Components → Tasks
   - Verify all requirements appear in this matrix

3. **Technical Stack:**
   - Definitive technology selections
   - **Action:** Reference in task descriptions to specify implementation technologies

4. **Component Dependencies:**
   - Found in each component's "Dependencies" subsection
   - **Action:** Use to determine task execution order and dependencies

**C. Feature Identification Strategy**

Follow this decision tree to identify feature-level tasks:

```
For each Component in architecture:
├─ Is it marked "New" or "Modified"? (brownfield)
│  ├─ YES → Create a task for this component
│  └─ NO (Existing) → Skip unless requirements reference it
│
├─ Does it map to ≥1 functional requirement?
│  ├─ YES → Create task: "{verb}-{component-noun}"
│  └─ NO → Check if it's infrastructure/cross-cutting
│     ├─ Infrastructure → Evaluate if separate task needed
│     └─ Cross-cutting → Address via NFR tasks
│
└─ Size check: Can this be completed in 1-3 days?
   ├─ YES → Keep as single task
   ├─ NO (Too large) → Split by sub-components or logical phases
   └─ TOO SMALL → Merge with related component
```

**D. Handling Non-Functional Requirements**

NFRs require different treatment:

| NFR Category | Task Creation Rule | Example |
|--------------|-------------------|---------|
| Performance | Task only if requires specific implementation (caching layer, optimization module) | "implement-cache" |
| Security | Task if dedicated component exists (Auth Service, Encryption Module) | "implement-auth" |
| Reliability | Usually addressed through architectural patterns; task if monitoring/health-check system needed | "setup-monitoring" |
| Scalability | Usually addressed through deployment architecture; no separate task unless specific feature (auto-scaler) | "config-autoscale" |

**Rule:** Create NFR task only if it requires concrete deliverable beyond architectural decision.

### 1. Task Granularity and Size Validation

Create **feature-level** tasks that represent major deliverables, not atomic implementation steps.

**Granularity Rules:**

| Level | Scope | Duration | When to Use | Example |
|-------|-------|----------|-------------|---------|
| **Feature (CORRECT)** | 1 architecture component or logical feature group | 1-3 days | Always for Epic | "implement-auth" (Auth Service component) |
| **Sub-feature (TOO SMALL)** | Part of a component | <1 day | Belongs in implementation plan | "write-login-endpoint" |
| **Atomic (TOO SMALL)** | Single action | Hours | Never in Epic | "write-unit-tests", "run-npm-install" |
| **Multi-feature (TOO LARGE)** | Multiple components | >3 days | Split into separate tasks | "build-entire-backend" |

**Size Validation Checklist:**

For each task, verify:
- [ ] Maps to ≥1 architecture component from Components section
- [ ] Maps to ≥1 functional requirement (REQ-XXX)
- [ ] Represents a deployable/demonstrable feature increment
- [ ] Estimated as 1-3 days of focused development work
- [ ] Name ≤14 characters in kebab-case

**Correct Granularity** (Feature-level):
- ✓ "implement-auth" → Maps to "Auth Service" component, covers REQ-001, REQ-002
- ✓ "build-catalog" → Maps to "Product Catalog Service" component, covers REQ-005
- ✓ "payment-gateway" → Maps to "Payment Integration" component, covers REQ-010

**Incorrect Granularity** (Too atomic - implementation details):
- ✗ "write-login-test" → Part of "implement-auth" task
- ✗ "create-migration" → Part of database setup in component task
- ✗ "run-npm-install" → Operational action, not a feature
- ✗ "commit-to-git" → Development process, not a deliverable

**Incorrect Granularity** (Too large - multiple components):
- ✗ "build-backend" → Spans multiple services, split into per-component tasks
- ✗ "complete-system" → Entire system, should be broken into all component tasks

Atomic breakdown happens later in the `*create-plan` phase. Epic defines **what** to build; plan defines **how** to build it.

### 2. Requirement-Task Mapping and Coverage Verification

**Source:** Use the **Requirements Traceability Matrix** from architecture document as your starting point.

**Process:**

1. **Extract from Traceability Matrix:**
   - Architecture document contains: `| Requirement ID | Requirement Title | Architecture Elements | Implementation Notes |`
   - This shows REQ/NFR → Component mappings

2. **Create Task Mapping:**
   - For each row in Traceability Matrix:
     - Identify the Architecture Element (component name)
     - Create or assign to existing task for that component
     - Record the mapping

3. **Build Coverage Table:**

| Requirement ID | Requirement Title | Task ID | Task Name | Architecture Component |
|----------------|-------------------|---------|-----------|------------------------|
| REQ-001 | User Login | 1 | implement-auth | Auth Service |
| REQ-002 | JWT Token Validation | 1 | implement-auth | Auth Service |
| REQ-003 | Product Listing | 2 | build-catalog | Product Service |
| NFR-001 | P95 Latency <200ms | 3 | implement-cache | Cache Layer |

4. **Verify 100% Coverage:**
   - [ ] Every REQ-XXX from requirements document appears in mapping
   - [ ] Every NFR-XXX either mapped to task OR addressed architecturally (document in notes)
   - [ ] Every task references at least one requirement
   - [ ] No orphan tasks (task without requirement justification)

**Mapping Rules:**

- **One-to-One:** Simple requirement → Single component → Single task (e.g., REQ-003 → Product Service → build-catalog)
- **Many-to-One:** Multiple requirements → Same component → Single task (e.g., REQ-001, REQ-002 → Auth Service → implement-auth)
- **One-to-Many:** Complex requirement → Multiple components → Multiple tasks (e.g., REQ-010 "Checkout" → Payment Service, Order Service, Notification Service → 3 tasks)
- **NFR Mapping:** NFR-XXX → Only if concrete component exists (e.g., NFR-001 Performance → Cache Layer → implement-cache)

### 3. Task Naming Conventions
Follow these naming rules:
- **Format**: `{verb}-{noun}` in kebab-case
- **Length**: ≤14 characters (excluding task ID)
- **Examples**: "implement-auth", "build-api", "create-reports"

### 4. Operational Actions Exclusion
Do NOT include operational or process tasks unless explicitly requested:
- ✗ Testing (covered in TDD workflow)
- ✗ Linting (part of development standards)
- ✗ Deployment (separate operational concern)
- ✗ Documentation (embedded in dev-notes)
- ✗ Code review (part of review workflow)

Focus only on **deliverable features** that provide user or business value.

### 5. Task Dependencies

**Source:** Extract from architecture document's **Components** section → **Dependencies** subsection for each component.

**Process:**

1. **Identify Component Dependencies:**
   - In each Component's "Dependencies" subsection, find:
     - Other components this depends on
     - External services required
     - Shared resources
   
2. **Map Component Dependencies → Task Dependencies:**
   
   Example from architecture:
   ```
   ## Profile Service
   **Dependencies:**
   - Auth Service (requires authentication)
   - User Database (shared resource)
   ```
   
   Translates to:
   ```
   - [ ] Task-2: build-profile
     - **Dependencies:** Task-1 (Auth Service must exist first)
   ```

3. **Dependency Rules:**
   - **Component dependency → Task dependency:** If Component B depends on Component A, then Task-B depends on Task-A
   - **Shared infrastructure:** Tasks using shared resources (databases, message queues) may need infrastructure task first
   - **External APIs:** If component integrates external API, check if API integration task needed first
   - **Data dependencies:** Tasks that consume data from other components must execute after data producers

4. **Document Dependencies:**
   - Use format: `**Dependencies:** Task-1, Task-3` in each task specification
   - Create dependency graph in "Task Dependencies" section of epic
   - Identify critical path (longest dependency chain)
   - Identify parallel execution opportunities (tasks with no dependencies)

**Example Dependency Analysis:**

| Task | Component | Depends On (from arch) | Task Dependency |
|------|-----------|-------------------------|-----------------|
| Task-1: implement-auth | Auth Service | User Database | None (or infrastructure setup) |
| Task-2: build-profile | Profile Service | Auth Service, User Database | Task-1 |
| Task-3: build-catalog | Product Service | Product Database | None |
| Task-4: checkout-flow | Order Service | Auth Service, Product Service, Payment Gateway | Task-1, Task-3 |

**Verification:**
- [ ] All inter-component dependencies from architecture are reflected in task dependencies
- [ ] No circular dependencies exist
- [ ] Tasks are ordered respecting dependency constraints

### 6. Definition of Done (DoD)

For each task, create **specific, verifiable** Quality-Gates based on:

**Sources:**
1. **Acceptance Criteria** from corresponding requirements (REQ-XXX)
2. **Component specifications** from architecture (Key Interfaces/APIs)
3. **Non-functional targets** from NFR-XXX
4. **Technology-specific standards** from Technical Stack section

**How to Create Quality-Gates:**

1. Extract acceptance criteria from mapped requirements (REQ-XXX)
2. Extract API/interface specifications from component's "Key Interfaces/APIs"
3. Extract performance/quality targets from relevant NFR-XXX
4. Combine into specific, verifiable criteria

**Quality-Gate Template:**

```
- **Quality-Gate:**
  - {Functional criterion from REQ acceptance criteria}
  - {API/interface criterion from component spec}
  - {Performance criterion from NFR if applicable}
  - All unit and integration tests passing (coverage ≥80%)
  - Code meets quality standards (linting, formatting)
  - Development notes completed
```

**Standard Gates (Apply to All Tasks):**
- [ ] All acceptance criteria from mapped requirements verified
- [ ] All component interfaces/APIs from architecture implemented
- [ ] Unit tests passing (≥80% coverage)
- [ ] Integration tests passing
- [ ] Code quality standards met (linting, formatting)
- [ ] Development notes completed ({DEV_NOTES}/task-{id}.md)
- [ ] No critical linter errors
- [ ] Performance targets met (if NFR applicable)

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Epic at "{EPIC}" with feature-level, outcome-oriented tasks mapped to requirements
- [ ] 100% requirement coverage
- [ ] kebab-case file names

## [Example]

### Good #1: E-commerce System with Complete Document Structure

**Input Documents:**

**Requirements ({REQ}/requirements.md):**
```
## REQ-001: User Registration
**Description:** Users can create accounts with email/password
**Acceptance Criteria:**
- Given valid email/password, When user registers, Then account created and confirmation email sent

## REQ-002: User Login
**Description:** Users can authenticate with JWT tokens
**Acceptance Criteria:**
- Given valid credentials, When user logs in, Then JWT token returned

## REQ-003: Product Browsing
**Description:** Users can view product catalog with filtering
**Acceptance Criteria:**
- Given product catalog, When user applies filters, Then filtered products displayed

## NFR-001: Performance
**Category:** Performance
**Target Metric:** P95 latency < 200ms for all API endpoints
```

**Architecture ({ARCH}/architecture.md):**
```
## Components

### Auth Service
**Responsibility:** User authentication and authorization
**Technology:** Node.js, Express, JWT, bcrypt
**Key Interfaces/APIs:**
- POST /api/auth/register
- POST /api/auth/login
**Dependencies:** User Database

### Product Service
**Responsibility:** Product catalog management
**Technology:** Node.js, Express, Redis (caching)
**Key Interfaces/APIs:**
- GET /api/products
- GET /api/products/:id
**Dependencies:** Product Database, Cache Layer

### Cache Layer
**Responsibility:** Response caching for performance
**Technology:** Redis
**Dependencies:** None

## Requirements Traceability Matrix
| Requirement ID | Architecture Elements |
|----------------|-----------------------|
| REQ-001 | Auth Service |
| REQ-002 | Auth Service |
| REQ-003 | Product Service |
| NFR-001 | Cache Layer |
```

**Decision Process:**

1. **Parse documents:**
   - Requirements: REQ-001, REQ-002, REQ-003, NFR-001
   - Components: Auth Service, Product Service, Cache Layer
   - Traceability: REQ-001,002 → Auth Service; REQ-003 → Product Service; NFR-001 → Cache Layer

2. **Identify features:**
   - Component "Auth Service" handles REQ-001, REQ-002 → Task-1: "implement-auth"
   - Component "Product Service" handles REQ-003 → Task-2: "build-catalog"
   - Component "Cache Layer" handles NFR-001 → Task-3: "setup-cache"

3. **Verify granularity:**
   - Task-1: Auth Service complete (registration + login) = 2-3 days ✓
   - Task-2: Product Service with filtering = 2 days ✓
   - Task-3: Redis caching layer = 1 day ✓

4. **Map dependencies:**
   - Auth Service dependencies: User Database (infrastructure)
   - Product Service dependencies: Product Database, Cache Layer → Task-2 depends on Task-3
   - Cache Layer dependencies: None

5. **Create Quality-Gates from acceptance criteria:**
   - Task-1 gates derived from REQ-001, REQ-002 acceptance criteria + Auth Service APIs
   - Task-2 gates derived from REQ-003 criteria + Product Service APIs + NFR-001 (uses cache)
   - Task-3 gates from NFR-001 metrics

6. **Result:**
```
- [ ] Task-1: implement-auth
  - **Requirements:** REQ-001, REQ-002
  - **Architecture:** Auth Service
  - **Dependencies:** None
  - **Quality-Gate:**
    - Registration endpoint creates account and sends email
    - Login endpoint returns valid JWT
    - Password hashing with bcrypt
    - All auth tests passing (≥80% coverage)

- [ ] Task-3: setup-cache
  - **Requirements:** NFR-001
  - **Architecture:** Cache Layer
  - **Dependencies:** None
  - **Quality-Gate:**
    - Redis cluster deployed and configured
    - Cache hit rate >70% after warmup
    - P95 latency <50ms for cached responses

- [ ] Task-2: build-catalog
  - **Requirements:** REQ-003
  - **Architecture:** Product Service
  - **Dependencies:** Task-3
  - **Quality-Gate:**
    - Product listing endpoint with filters
    - Responses cached via Redis
    - P95 latency <200ms (leveraging cache)
    - All product tests passing
```

**Why Good:**
- ✓ Derived tasks directly from architecture Components section
- ✓ Used Traceability Matrix for REQ→Component→Task mapping
- ✓ 100% coverage: All 3 REQs + 1 NFR mapped
- ✓ Feature-level granularity (1-3 days each)
- ✓ Dependencies from component Dependencies subsections
- ✓ Quality-Gates derived from acceptance criteria + component specs
- ✓ Names ≤14 chars, kebab-case

### Bad #1: Incorrect Granularity and Missing Traceability

**Input:** Same requirements and architecture as Good #1

**Bad Decision:**
```
- [ ] Task-1: write-register-endpoint
- [ ] Task-2: write-login-endpoint
- [ ] Task-3: write-unit-tests
- [ ] Task-4: setup-database
- [ ] Task-5: create-product-model
- [ ] Task-6: write-product-controller
- [ ] Task-7: deploy-redis
- [ ] Task-8: run-npm-install
```

**Why Bad:**
- ✗ Too atomic: Tasks are implementation steps, not features
- ✗ No traceability: Requirements not mapped to tasks
- ✗ Ignored architecture: Didn't use Components as task basis
- ✗ Included operational actions: "run-npm-install", "write-unit-tests"
- ✗ Wrong granularity: Tasks are <1 day each

**Correct Approach:**
- Use **Components** from architecture as task basis
- Map using **Traceability Matrix**: REQ-001,002 → Auth Service → Single "implement-auth" task
- Feature-level: Complete Auth Service (all endpoints) as one deliverable
- Exclude operational: Testing/deployment are part of task execution, not separate tasks

### Bad #2: Over-Aggregation

**Input:** Same requirements and architecture as Good #1

**Bad Decision:**
```
- [ ] Task-1: build-entire-backend-system
  - **Requirements:** REQ-001, REQ-002, REQ-003, NFR-001
  - **Architecture:** Auth Service, Product Service, Cache Layer
```

**Why Bad:**
- ✗ Too large: Spans all components, >3 days
- ✗ Not testable: Cannot verify completion incrementally
- ✗ Violates architecture structure: Should respect component boundaries

**Correct Approach:**
- One task per component: 3 components → 3 tasks
- Each task is independently deliverable and testable
- Respect component boundaries from architecture
