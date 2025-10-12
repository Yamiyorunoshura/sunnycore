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
  3. "{root}/docs/plan.md" (temporary document, will be deleted after the task is completed) --For progress tracking

## [Constraints]
  1. Do not propose design without reviewing existing requirements and architecture
  2. Do not break existing contracts (any changes must include explicit Impact Analysis)
  3. Do not deviate from template structure
  4. Do not skip executing shard-architecture.py

## [Steps]
  1. Existing Architecture Evaluation
    - Understand current architecture, extension points, and constraints
    - Identify affected domains and dependencies
    - Establish progress tracking mechanism
    - Outcome: Complete understanding of existing architecture and extension points

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

### Example 1: Add OAuth2 to Existing REST API
[Input]
- Requirements: REQ-001 (OAuth2 authentication)
- Existing architecture: REST API with basic auth, User Service, PostgreSQL
- Template: architecture-tmpl.yaml

[Decision]
- New component: OAuth2 Server (integrate with existing User Service)
- Preserve existing API contracts (add Authorization header only)
- Impact Analysis: All API endpoints need authentication middleware update

[Expected Outcome]
- docs/architecture.md with OAuth2 Server component and integration points
- Impact Analysis section documenting changes to existing API Gateway
- Reference: docs/architecture/components.md#user-service for integration context

### Example 2: Add Analytics Module to CMS
[Input]
- Requirements: REQ-001 (page view tracking), REQ-002 (user behavior analytics)
- Existing: Content Management System with PostgreSQL, Redis cache
- Knowledge base: best-practices-caching.md

[Decision]
- New components: Analytics Collector (async), Analytics DB (ClickHouse)
- Extension point: Event bus (existing) for analytics events
- No breaking changes: Analytics operates independently via event subscription

[Expected Outcome]
- docs/architecture.md showing Analytics module integrated via event bus
- Compatibility verification: existing components unchanged
- Updated architecture documents showing clear module boundaries

### Example 3: Migrate Monolith Order Service to Microservice
[Input]
- Requirements: REQ-001 (extract order processing to separate service)
- Existing: Monolithic e-commerce app, shared PostgreSQL database
- Constraints: Zero downtime migration required

[Decision]
- New component: Order Microservice with dedicated database
- Migration strategy: Strangler Fig pattern with API Gateway routing
- Impact Analysis: Database schema split, API contract evolution

[Expected Outcome]
- docs/architecture.md with migration phases and dual-write strategy
- Impact Analysis documenting breaking changes and migration path
- ADRs explaining Strangler Fig pattern choice and trade-offs
