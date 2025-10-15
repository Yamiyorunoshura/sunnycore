**GOAL**: Create detailed functional and non-functional requirements documentation.

## [Context]
**You must read the following context:**
- `{TMPL}/requirement-tmpl.yaml` (defines document structure and formatting)
- User-provided ideas and descriptions

## [Products]
- `{root}/docs/requirements.md` (temporary, will be sharded)
- `{REQ}/*.md`

## [Constraints]
- **MUST** create measurable requirements, **MUST NOT** create vague ones
- **MUST** follow `requirement-tmpl.yaml` structure, **MUST NOT** deviate
- **MUST** exclude sensitive data in examples, **MUST NOT** include
- **MUST** execute shard-requirements.py after approval, **MUST NOT** skip

## [Steps]
**You should work along to the following steps:**
1. Define requirements gathering scope. This establishes boundaries and context clearly.
2. Extract atomic, deduplicated functional requirements from user input. This creates complete functional requirements.
3. Infer and quantify non-functional requirements with measurable metrics. This establishes verifiable quality attributes.
4. Execute quality checks for completeness and consistency. This ensures all requirements meet engineering standards.
5. Obtain user approval, then run shard-requirements.py. This produces approved requirements sharded successfully.

## [Instructions]

### 1. Define Requirements Gathering Scope
Establish clear boundaries before extracting requirements:
- **Problem domain**: What problem are we solving?
- **Target users**: Who will use this system? (personas, roles)
- **Use cases**: What are the primary user journeys?
- **System boundaries**: What's in-scope vs. out-of-scope?
- **Integration context**: Existing systems, platforms, or constraints

Document these in the **Project Overview** section per `requirement-tmpl.yaml`.

### 2. Extract Functional Requirements from User Input

**Core extraction principles:**

**A. Decompose vague statements into atomic capabilities**
- ❌ User says: "Users search products"
- ✓ Extract multiple atomic requirements:
  - REQ-001: Category filtering (UI control + backend query)
  - REQ-002: Price range filtering (slider + real-time query)
  - REQ-003: Rating filtering (star selection + count display)

**B. Ask clarifying questions to uncover hidden requirements**
- If user says "notification system" → Ask: Which channels? (email, SMS, push?) Real-time or batch? User preferences?
- If user says "dashboard" → Ask: Which metrics? Update frequency? User roles with different views?

**C. Ensure each requirement is SMART**
- **S**pecific: Exactly what capability/feature?
- **M**easurable: How do we verify it works?
- **A**chievable: Technically feasible with available resources?
- **R**elevant: Aligns with project goals?
- **T**estable: Can write clear pass/fail acceptance criteria?

**D. Deduplicate and trace dependencies**
- Avoid overlapping requirements (e.g., "login" and "user authentication" are likely the same)
- Identify dependencies: REQ-005 may depend on REQ-002 being completed first

Follow the **Functional Requirements** format in `requirement-tmpl.yaml` (REQ-001, REQ-002, etc.).

### 3. Infer and Quantify Non-Functional Requirements

**Core quantification principles:**

**A. Transform qualitative adjectives into measurable metrics**
- "fast" → P95 latency < 200ms, P99 < 500ms
- "scalable" → Support 10K concurrent users, 100K requests/min
- "reliable" → 99.9% uptime, max 43min downtime/month
- "secure" → OAuth 2.0 + JWT, AES-256 encryption, OWASP Top 10 compliance
- "user-friendly" → ≤3 clicks to complete task, 95% task completion rate

**B. Infer implicit NFRs from context**
- If user mentions "mobile app" → Infer: app size < 50MB, cold start < 2s
- If user mentions "financial transactions" → Infer: PCI-DSS compliance, audit logging
- If user mentions "global users" → Infer: multi-region deployment, CDN latency < 100ms

**C. Use industry-standard categories**
- **Performance**: Response time, throughput, resource usage
- **Scalability**: Concurrent users, data volume, transaction rate
- **Reliability**: Uptime, MTBF, MTTR, fault tolerance
- **Security**: Authentication, authorization, encryption, compliance
- **Usability**: Task completion time, error rate, accessibility (WCAG 2.1)
- **Maintainability**: Code coverage, deployment frequency, documentation

Follow the **Non-Functional Requirements** format in `requirement-tmpl.yaml` (NFR-001, NFR-002, etc.).

### 4. Quality Checks Before Finalization

Run these checks before seeking user approval:

**Completeness checks:**
- [ ] All user-mentioned features have corresponding functional requirements
- [ ] All quality expectations have corresponding NFRs with metrics
- [ ] Every requirement has Given-When-Then acceptance criteria
- [ ] Constraints section covers technical, business, and regulatory limits

**Consistency checks:**
- [ ] No contradictory requirements (e.g., REQ-010 vs. REQ-025)
- [ ] NFR targets are aligned (e.g., P95 < 200ms but supports 10K concurrent users is realistic?)
- [ ] Dependencies are valid and acyclic

**Feasibility checks:**
- [ ] Each requirement is technically achievable with available technology
- [ ] NFR metrics are realistic given project constraints (time, budget, team size)
- [ ] No requirements violate stated constraints

**Sensitivity checks:**
- [ ] Examples use placeholder data (user@example.com, not real emails)
- [ ] No proprietary algorithms, trade secrets, or confidential data exposed

### 5. Approval and Sharding Workflow

**A. Obtain user approval:**
1. Present the complete `requirements.md` document
2. Walk through key requirements and acceptance criteria
3. Confirm scope alignment and feasibility
4. Address any user feedback or clarifications

**B. Execute sharding:**
1. Run `python scripts/shard-requirements.py` to split `requirements.md`
2. Verify sharded files appear in `{REQ}/` directory (typically: `functional.md`, `non-functional.md`, `constraints.md`)
3. Confirm cross-references and requirement IDs are preserved
4. Notify user of successful sharding

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Requirements extracted following SMART principles (Specific, Measurable, Achievable, Relevant, Testable)
- [ ] All NFRs quantified with measurable metrics (no vague adjectives like "fast" or "secure")
- [ ] Every requirement has Given-When-Then acceptance criteria per `requirement-tmpl.yaml`
- [ ] Quality checks passed (completeness, consistency, feasibility, sensitivity)
- [ ] Final requirement set approved by user
- [ ] Requirements sharded to "{REQ}/*.md" using shard-requirements.py

## [Example]

### Good #1: Decomposition and Quantification
**Input**: "Customers search products by category, price, ratings with fast response"

**Decision Process**:
1. **Scope**: Product search capability for e-commerce platform
2. **Extract functional** (decompose vague "search" into atomic capabilities):
   - REQ-001: Category filter with dropdown UI and backend query
   - REQ-002: Price range slider ($0-$10K) with real-time filtering
   - REQ-003: Star rating filter (1-5 stars) with result count
3. **Quantify NFRs** (transform "fast" into metrics):
   - NFR-001: API response time P95 < 500ms under 100 concurrent users
   - NFR-002: Search results render in < 300ms after filter change
4. **Quality check**: SMART criteria met, no contradictions, technically feasible
5. **Generate** `requirements.md` per `requirement-tmpl.yaml`, obtain approval, run shard script

**Why Good**: Transforms vague user input into atomic, measurable, testable requirements with clear acceptance criteria.

### Good #2: Inferring Implicit Requirements
**Input**: "Send real-time notifications to iOS/Android when events occur with high reliability"

**Decision Process**:
1. **Scope**: Cross-platform push notification system
2. **Extract functional**:
   - REQ-001: Event subscription management (users opt-in/out by event type)
   - REQ-002: iOS push via APNs with certificate handling
   - REQ-003: Android push via FCM with token management
   - REQ-004: Notification template engine (title, body, actions)
3. **Quantify NFRs** (infer from "real-time" and "high reliability"):
   - NFR-001: Latency < 2s from event trigger to device delivery (P95)
   - NFR-002: 99.9% delivery success rate
   - NFR-003: Support 10K notifications/min peak load
   - NFR-004: Retry mechanism with exponential backoff (3 attempts)
4. **Ask clarifications**: Notification priority levels? Silent notifications? Rich media support?
5. **Generate** and shard after approval

**Why Good**: Infers implicit NFRs from context, asks clarifying questions to uncover hidden requirements.

### Bad #1: Vague and Unmeasurable
**Input**: "Need a user-friendly system that's fast and secure"

**Bad Decision**: 
- REQ-001: "System must be user-friendly"
- NFR-001: "System must be fast"
- NFR-002: "System must be secure"
- Skip Given-When-Then, skip quantification, obtain approval, skip sharding

**Why Bad**: 
- "User-friendly", "fast", "secure" are not measurable or testable
- No decomposition into atomic capabilities
- No acceptance criteria
- Cannot verify these requirements in testing

**Correct Approach**:
1. **Ask clarifications**: What does "user-friendly" mean? (task completion time? error rate?) What does "fast" mean? (API latency? page load?) What security concerns? (authentication? data encryption?)
2. **Transform to measurable**:
   - REQ-001: "Users complete checkout in ≤3 clicks with 95% task completion rate"
   - NFR-001: "API P95 < 200ms, P99 < 500ms under 500 concurrent users"
   - NFR-002: "OAuth 2.0 authentication, AES-256 data encryption, OWASP Top 10 compliance"
3. **Create Given-When-Then** for each requirement
4. **Follow workflow**: Generate per template → quality check → approval → shard
