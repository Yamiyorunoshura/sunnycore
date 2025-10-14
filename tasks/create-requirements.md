**GOAL**: Create detailed functional and non-functional requirements documentation.

## [Input]
**You must read the following documents:**
- `{TMPL}/requirement-tmpl.yaml`
- User-provided ideas and descriptions

## [Output]
- `{root}/docs/requirements.md` (temporary, will be sharded)
- `{REQ}/*.md`

## [Constraints]
- **MUST** create measurable requirements, **MUST NOT** create vague ones
- **MUST** follow template structure, **MUST NOT** deviate
- **MUST** exclude sensitive data in examples, **MUST NOT** include
- **MUST** execute shard-requirements.py, **MUST NOT** skip

## [Steps]
**You should work along to the following steps:**
1. Define requirements gathering scope. This establishes scope clearly.
2. Extract complete, deduplicated functional requirements. This creates complete functional requirements documentation.
3. Define quantified non-functional requirements. This establishes quantified non-functional requirements.
4. Create testable acceptance criteria (Given-When-Then). This ensures all requirements have acceptance criteria.
5. Ensure consistency, obtain approval, run shard-requirements.py. This produces approved requirements sharded successfully.

## [Instructions]

### 1. Requirement Gathering Scope
Establish clear boundaries for requirement gathering:
- Identify the problem domain and user needs
- Define system boundaries and out-of-scope items
- Clarify target users and use cases

### 2. Functional Requirements
Extract and document functional requirements that are:
- **Complete**: Cover all user-facing capabilities
- **Atomic**: Each requirement represents one distinct capability
- **Deduplicated**: No overlapping or redundant requirements
- **Traceable**: Each has a unique identifier (REQ-001, REQ-002, etc.)

Transform vague user input into precise requirements:
- Input: "Users search products"
- Output:
  - REQ-001: Category filter with dropdown UI and backend query
  - REQ-002: Price range slider ($0-$10,000) with real-time filtering
  - REQ-003: Star rating filter (1-5 stars) with count display

### 3. Non-Functional Requirements (NFRs)
Quantify ALL non-functional requirements with measurable, verifiable metrics:

#### Performance Requirements
- ❌ "System should be fast"
- ✓ "API response time P95 < 200ms, P99 < 500ms under 100 concurrent users"

#### Scalability Requirements
- ❌ "Support many users"
- ✓ "Support 1000 concurrent users with 10K requests/minute peak load"

#### Reliability Requirements
- ❌ "High availability"
- ✓ "99.9% uptime SLA, max 43 minutes downtime/month"

#### Security Requirements
- ❌ "Secure authentication"
- ✓ "OAuth 2.0 + JWT with 15-minute token expiry, RFC 6238 TOTP for 2FA"

#### Usability Requirements
- ❌ "User-friendly"
- ✓ "Users complete checkout flow in ≤3 clicks, 95% task completion rate"

### 4. Acceptance Criteria (Given-When-Then)
For EVERY requirement, create testable acceptance criteria:

**Format**:
```
Given [initial context/state]
When [action/event occurs]
Then [expected outcome with measurable criteria]
```

**Examples**:
```
Functional (REQ-001):
Given: User is on product listing page with 500 products
When: User selects "Electronics" category and price range "$100-$500"
Then: System returns filtered results in < 500ms showing only matching products

Non-Functional (NFR-001):
Given: System has 1000 concurrent users
When: Load test runs for 10 minutes at peak traffic
Then: P95 response time remains < 200ms, P99 < 500ms, 0 errors
```

The acceptance criteria must be:
- **Binary**: Pass or fail, no ambiguity
- **Verifiable**: Can be tested objectively
- **Complete**: Cover happy path and edge cases

### 5. Requirement Organization
Organize requirements by capability or user journey:
- Group related requirements together
- Separate functional and non-functional requirements
- Maintain clear hierarchy (epic → features → requirements)

### 6. Quality Checks
Before finalizing:
- **Completeness**: All user needs covered
- **Consistency**: No contradictions between requirements
- **Measurability**: All metrics are quantified
- **Testability**: All have Given-When-Then acceptance criteria
- **Sensitivity**: No sensitive data in examples (use placeholders)

### 7. Sharding Workflow
After creating the unified `requirements.md`:
1. Obtain user approval for the complete requirement set
2. Execute `shard-requirements.py` to split into semantic files
3. Verify sharded files in `{REQ}/` directory (typically: functional.md, non-functional.md)
4. Confirm all cross-references are preserved

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Functional and non-functional requirements with quantified metrics and Given-When-Then criteria
- [ ] Requirements sharded to "{REQ}/*.md" using shard-requirements.py
- [ ] Final requirement set approved by user

## [Example]

### Good #1
**Input**: "Customers search products by category, price, ratings with fast response"  
**Decision**: Define scope: product search. Extract functional: REQ-001 (category filter UI+logic), REQ-002 (price range slider+query), REQ-003 (rating filter 1-5 stars). Deduplicate and atomize. Define NFRs: NFR-001 (P95 <500ms), NFR-002 (100 concurrent users). Quantify. Create acceptance: Given user on product page, When applies category "Electronics" and price "$100-$500", Then returns filtered results <500ms. Use binary pass/fail. Generate requirements.md. Obtain approval. Shard to functional.md and non-functional.md.  
**Why Good**: This turns vague request into atomic, measurable requirements with explicit acceptance tests.

### Good #2
**Input**: "Send real-time notifications to iOS/Android when events occur with high reliability"  
**Decision**: Define scope: push notification system. Extract functional: REQ-001 (event subscription), REQ-002 (cross-platform delivery iOS/Android), REQ-003 (notification templates). Organize by capabilities. Define NFRs: NFR-001 (<2s latency), NFR-002 (99.9% delivery success), NFR-003 (10K notifications/min). Quantify all. Create acceptance: Given event occurs, When notification sent, Then delivered within 2s. Obtain approval. Shard successfully.  
**Why Good**: This captures functional breadth and demanding NFRs while eliminating ambiguity.

### Bad #1
**Input**: Multiple vague ideas  
**Bad Decision**: Create vague: "REQ-001: user-friendly", "NFR-001: fast system". Omit quantification. Omit Given-When-Then. Mix functional and non-functional. Skip deduplication. Skip sharding. Save as single file without template.  
**Why Bad**: This creates vague unmeasurable requirements that are not verifiable with no clear success criteria. "user-friendly" and "fast" are not testable.  
**Correct**: Transform "user-friendly" to specific REQ: "Users complete checkout in ≤3 clicks". Transform "fast" to quantified NFR: "API P95 <200ms". Use Given-When-Then. Separate functional from non-functional. Execute shard-requirements.py.
