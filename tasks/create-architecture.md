**GOAL**: Create comprehensive technical architecture documentation for Greenfield projects.

## [Input]
  1. "{REQ}/*.md" --Authoritative project requirements
  2. "{SCRIPTS}/shard-architecture.py" --Architecture sharding script
  3. "{TMPL}/architecture-tmpl.yaml" --Standardized architecture template
  

## [Output]
  1. Architecture document collection under "{ARCH}/" directory (*.md format)
  2. "{root}/docs/architecture.md" (Markdown format)(temporary architecture file. Will be sharded after running "shard-architecture.py")
  

## [Constraints]
  1. Do not make assumptions when requirements are incomplete or conflicting (must record issues and confirm)
  2. Do not produce architecture that lacks 100% requirement coverage
  3. Do not deviate from template structure or introduce non-existent paths
  4. Do not skip executing shard-architecture.py

## [Steps]
  1. Requirement Analysis & Mapping
    - Understand all requirements and their implications
    - Create complete requirement-to-architecture mapping matrix (100% coverage)
    - Record a short planning outline in the conversation (no standalone plan.md)
    - Outcome: Complete understanding, requirement mapping matrix created, and plan outline documented

  2. Architecture Design
    - Design comprehensive architecture with all components and boundaries
    - Map every requirement to specific architecture elements
    - Address all cross-cutting concerns
    - Outcome: Complete architecture design with full requirement coverage

  3. Documentation, Approval & Sharding
    - Create compliant architecture draft following template structure
    - Obtain user approval and integrate feedback
    - Run "shard-architecture.py" script to generate "{ARCH}/*.md" files
    - Outcome: Approved architecture document successfully sharded

  4. Final Verification
    - Verify architecture satisfies all requirements through mapping
    - Ensure consistency and justification of architecture decisions
    - Outcome: Architecture verified and validated

## [Error-Handling]
  1. "shard-architecture.py" execution failure: Check if "architecture.md" format complies with template specifications, fix and re-execute
  2. Unresolvable requirement conflicts: Record conflicts and confirm with requirement authors, do not make assumptions
  3. Architecture design infeasibility: Record technical limitations and propose alternative solutions

## [Architecture-Design-Guidelines]
  1. **Template Compliance & Complete Mapping**
    - Follow template structure strictly (overview, components, data flows, ADRs)
    - Establish 100% bidirectional mapping: requirements ↔ architecture elements
    - Verify all functional and non-functional requirements have corresponding architecture design
  
  2. **Decision Records (ADR)**
    - Document key decisions with context, rationale, alternatives, and trade-offs
    - Explain why this approach was chosen over others
    - Include expected impact and potential technical debt
  
  3. **Cross-Cutting Concerns**
    - Address security, observability, performance, reliability systematically
    - Define consistency mechanisms (authentication, logging, error handling) across components
    - Transform non-functional requirements into concrete architecture constraints
  
  4. **External API Documentation**
    - Document every external API integration in detail within the api-documentation section
    - For each external API, include:
      * API name and provider (e.g., "Stripe Payment API v1")
      * Complete API endpoint URLs and base paths
      * Authentication method and credential management approach
      * Request/response format specifications (JSON schema, data types, required fields)
      * API call methods (REST verbs, GraphQL queries, RPC methods)
      * Rate limits, quotas, and retry strategies
      * Error handling patterns and expected error codes
      * Purpose and functionality description
      * Integration points within the system architecture
      * Fallback strategies for API unavailability
    - Include versioning strategy for external API dependencies
    - Document any API contract assumptions or SLA requirements
  
  5. **Traceability & Justification**
    - Annotate source references for all architecture statements
    - Ensure every decision is justified by requirements or business drivers
    - Use clear terminology consistently throughout documentation

## [DoD]
  - [ ] Complete requirement-to-architecture mapping matrix with 100% coverage (all functional and non-functional requirements mapped)
  - [ ] Architecture document approved by user and exists at "{root}/docs/architecture.md" following template structure
  - [ ] Architecture successfully sharded with verified output files in "{ARCH}/"
  

## [Example]

### Good Example 1
[INPUT]
Requirements specify REQ-001 (WebSocket messaging), REQ-002 (message persistence), NFR-001 (latency < 100ms). Architecture template requires components, data flows, ADRs, and external APIs sections.

[DECISION]
Create requirement-to-architecture mapping matrix targeting 100% coverage. Design components: WebSocket Gateway (handles REQ-001), Message Broker with Redis (REQ-001), Message Store with MongoDB (REQ-002). Map all requirements: REQ-001→WebSocket Gateway+Message Broker, REQ-002→Message Store, NFR-001→architecture constraint for all components. Create ADR-001 documenting choice of WebSocket over HTTP polling with rationale (real-time performance, lower latency). Address cross-cutting concerns (authentication with JWT, monitoring with Prometheus). Generate docs/architecture.md following template. Obtain user approval. Execute shard-architecture.py to create docs/architecture/overview.md, components.md, traceability_matrix.md.

[OUTCOME]
Complete architecture document at docs/architecture.md with 100% requirement coverage verified. Sharded files successfully created in docs/architecture/. Traceability matrix shows REQ-001 and REQ-002 mapped to specific components. ADRs explain all key decisions with trade-offs.

[WHY-GOOD]
- Drives the design from explicit requirement mapping, ensuring nothing is left uncovered before documentation.
- Completes mandatory workflows—ADRs, approval, sharding—so downstream teams receive structured, validated artifacts.

### Good Example 2
[INPUT]
Requirements include REQ-001 (payment processing via Stripe API), REQ-002 (fraud detection), NFR-001 (ACID compliance). Template includes api-documentation section for external APIs.

[DECISION]
Design architecture with Payment Gateway, Fraud Analyzer (ML service), Transaction DB (PostgreSQL). Create ADR-001 for synchronous processing to ensure ACID guarantees with trade-off analysis. Document Stripe API in api-documentation section with complete details: endpoint URLs (https://api.stripe.com/v1/charges), authentication (Bearer token), request/response schemas (JSON with amount, currency, source fields), rate limits (100 req/sec), retry strategies (exponential backoff), error handling (4xx/5xx codes). Map requirements: REQ-001→Payment Gateway+Stripe integration, REQ-002→Fraud Analyzer, NFR-001→synchronous processing pattern. Verify 100% coverage. Obtain approval and shard.

[OUTCOME]
docs/architecture.md with comprehensive external API documentation for Stripe including authentication, schemas, rate limits, and error handling. All requirements mapped with justification. Sharded successfully with detailed api-documentation.md file containing complete Stripe integration specifications.

[WHY-GOOD]
- Documents external integrations to the depth demanded by the template, avoiding ambiguous API usage later.
- Confirms coverage and compliance steps, resulting in an architecture package that developers can implement directly.

### Bad Example 1
[INPUT]
Requirements show REQ-001, REQ-002, REQ-003. Some requirements are vague or conflicting.

[BAD-DECISION]
Make assumptions about unclear requirements without confirming with user. Design architecture ignoring conflicts. Skip creating requirement-to-architecture mapping matrix. Generate architecture document missing some requirement mappings. Run sharding script without verification.

[WHY-BAD]
Violates Constraint 1 (do not make assumptions when requirements incomplete/conflicting). Violates Constraint 2 (do not produce architecture lacking 100% coverage). Skips Step 1 (record issues and confirm). Missing mapping matrix means no verification of coverage. Architecture built on assumptions will fail review.

[CORRECT-APPROACH]
During Step 1, identify vague requirements and conflicts. Record specific issues: "REQ-002 conflicts with NFR-001: requirement specifies eventual consistency but NFR requires ACID compliance". Pause and request clarification from user. Do not proceed until conflicts resolved. After clarification, create complete mapping matrix ensuring 100% coverage before designing components.

### Bad Example 2
[INPUT]
Architecture template includes external API documentation requirements. System integrates with Twilio SMS API.

[BAD-DECISION]
Mention "Uses Twilio for SMS" without providing API details. Skip documenting authentication method, endpoint URLs, request/response formats, rate limits, and error handling. Generate architecture without api-documentation section. Skip sharding script execution claiming "documentation is complete enough".

[WHY-BAD]
Violates Constraint 3 (do not deviate from template structure). Violates Architecture-Design-Guidelines point 4 (external API documentation requirement). Violates Constraint 4 (do not skip executing shard-architecture.py). Insufficient API documentation will cause implementation failures when developers need integration details.

[CORRECT-APPROACH]
Follow Architecture-Design-Guidelines section 4 completely. In api-documentation section document Twilio SMS API: name "Twilio SMS API v2010-04-01", endpoints "https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages.json", authentication (HTTP Basic Auth with Account SID and Auth Token), request format (POST with To, From, Body fields), response schema (JSON with sid, status, error_code), rate limits (varies by account), retry strategy (idempotent with message SID), error handling (handle 400/429/500 codes), purpose (send SMS notifications), integration points (Notification Service), fallback (queue messages for retry). Execute shard-architecture.py to verify template compliance.
