**GOAL**: Create architecture change documentation for Brownfield projects, extending existing architecture.

## [Input]
  1. "{REQ}" --Standardized requirement source
  2. "{ARCH}/*.md" --Existing architecture document collection
  3. "{SCRIPTS}/shard-architecture.py" --Architecture sharding script
  4. "{TMPL}/architecture-tmpl.yaml" --Architecture template
  5. "{KNOWLEDGE}/*.md" --Project knowledge
  

## [Output]
  1. "{root}/docs/architecture.md" (Markdown format)(temporary architecture file. Will be sharded after running "shard-architecture.py")
  2. "{ARCH}/*.md" --Updated architecture document collection (*.md format)
  

## [Constraints]
  1. Do not propose design without reviewing existing requirements and architecture
  2. Do not break existing contracts (any changes must include explicit Impact Analysis)
  3. Do not deviate from template structure
  4. Do not skip executing shard-architecture.py

## [Steps]
  1. Existing Architecture Evaluation
    - Understand current architecture, extension points, and constraints
    - Identify affected domains and dependencies
    - Conceive the best solution for the task that needs to be completed
    - Outcome: Complete understanding of existing architecture, extension points identified, and plan outline documented

  2. New Module Design & Impact Analysis
    - Design new module with clear boundaries and interfaces
    - Plan integration with existing components
    - Conduct comprehensive impact analysis for all changes
    - Outcome: Complete new module design with impact analysis

  3. Documentation, Approval & Sharding
    - Create compliant architecture draft following template
    - Obtain user approval and integrate feedback
    - Run "shard-architecture.py" to update "{ARCH}/*.md" files
    - Outcome: Approved architecture changes successfully sharded

  4. Compatibility Verification
    - Verify all impact analyses are complete and accurate
    - Validate compatibility between new and existing modules
    - Outcome: New and existing modules verified as compatible

## [Brownfield-Architecture-Guidelines]
  1. **Preserve Existing Contracts**
    - Maintain all public API interfaces, data models, and event formats
    - Any breaking changes must include explicit "Impact Analysis" section
    - Document migration path and backward compatibility strategy
  
  2. **Extension Point Analysis**
    - Identify where new functionality integrates with existing system
    - Map dependencies on shared services and constraints
    - Verify compatibility with existing technical stack
  
  3. **Template Compliance & Mapping**
    - Follow template structure; include all sections from existing architecture
    - Establish mapping: new requirements → new/modified components → existing system
    - Use `Reference: {file path}#{section}` format for all reviewed content
  
  4. **External API Documentation**
    - Document every external API integration (new or modified) in detail within the api-documentation section
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
    - For existing external API integrations: verify continued compatibility or document required changes
  
  5. **Decision Records for Changes**
    - Document why changes are needed with context and rationale
    - Explain integration approach and trade-offs
    - Annotate source references (source_refs) for all architecture statements

## [DoD]
  - [ ] New module design complete with boundaries, interfaces, and explicit impact analysis for all changes
  - [ ] Compatibility with existing contracts verified (no breaking changes or migration path provided)
  - [ ] Architecture document approved and successfully sharded to "{ARCH}/"

## [Example]

### Good Example 1
[INPUT]
Existing REST API with basic auth documented in docs/architecture/. New requirement REQ-001 requires OAuth2 authentication.

[DECISION]
Read existing architecture documents to understand User Service and API Gateway. Design OAuth2 Server component integrating with existing User Service. Preserve existing API contracts (only add Authorization header support). Create Impact Analysis documenting API Gateway middleware changes. Map REQ-001→OAuth2 Server. Reference docs/architecture/components.md#user-service. Generate architecture.md following template. Obtain approval. Execute shard-architecture.py.

[OUTCOME]
Updated docs/architecture.md with OAuth2 Server integrated cleanly. Impact Analysis shows no breaking changes. All references valid. Sharded successfully with clear integration boundaries.

[WHY-GOOD]
- Extends the existing system without breaking contracts, aligning with Brownfield constraints and documenting the impacts explicitly.
- Completes approval and sharding, ensuring the updated architecture is distributed in the standard format.

### Good Example 2
[INPUT]
Existing CMS with PostgreSQL, Redis. Requirements REQ-001 (analytics tracking), REQ-002 (behavior analysis). Knowledge base has best-practices-caching.md.

[DECISION]
Identify Brownfield project. Design Analytics Collector (async) and Analytics DB (ClickHouse). Use existing event bus as extension point - analytics subscribes to events. No changes to CMS components (no breaking changes). Document decision for ClickHouse selection (ADR). Map requirements to new components. Reference existing architecture docs. Generate complete architecture.md. Shard after approval.

[OUTCOME]
docs/architecture.md showing Analytics module via event bus integration. Compatibility verified - zero CMS impact. References to event-bus.md and best-practices-caching.md included. Clear module boundaries in sharded documents.

[WHY-GOOD]
- Introduces new capabilities through approved extension points, preserving legacy stability while meeting new requirements.
- Captures traceability and references, making the integration auditable and ready for development teams.

### Bad Example 1
[INPUT]
Need to add feature to existing system with docs/architecture/.

[BAD-DECISION]
Design without reading existing docs. Assume integration points. Skip Impact Analysis. Use fabricated component names not in existing system. Run sharding without compatibility check.

[WHY-BAD]
Violates Constraint 1 (review existing architecture first). Violates Constraint 2 (no Impact Analysis for changes). Ignores Brownfield-Architecture-Guidelines about preserving contracts. Creates incompatible design.

[CORRECT-APPROACH]
Execute Step 1: read ALL docs/architecture/*.md files first. Understand current components, contracts, extension points. Identify affected domains. Design new module ensuring compatibility. Create Impact Analysis for ANY existing component changes. Use Reference format to cite reviewed content. Then generate and shard.

### Bad Example 2
[INPUT]
Adding payment service using Stripe API. Existing Order Service documented.

[BAD-DECISION]
Mention "Uses Stripe" without details. Skip api-documentation section. Ignore Order Service integration needs. Miss endpoint URLs, authentication, rate limits, error handling. No Impact Analysis for Order Service changes.

[WHY-BAD]
Violates Brownfield-Architecture-Guidelines point 4 (complete external API documentation). Violates Constraint 2 (missing Impact Analysis). Blocks implementation with insufficient integration details. Violates template requirements.

[CORRECT-APPROACH]
Follow Guidelines section 4 fully. Document Stripe API completely: name, endpoints (https://api.stripe.com/v1/charges), authentication (API key management), schemas, rate limits, retry strategies, error codes, integration with Order Service, fallbacks. Create Impact Analysis for Order Service changes. Reference existing Order Service docs. Verify compatibility, provide migration path if needed.
