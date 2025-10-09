**GOAL**: Create architecture change documentation for Brownfield projects, extending existing architecture.

## [Input]
  1. "{REQ}" --Standardized requirement source
  2. "{ARCH}/*.md" --Existing architecture document collection
  3. "{SCRIPTS}/shard-architecture.py" --Architecture sharding script
  4. "{TMPL}/architecture-tmpl.yaml" --Architecture template
  5. "{KNOWLEDGE}/*.md" --Project knowledge

## [Output]
  1. "{root}/docs/architecture.md" (temporary architecture file. Will be sharded after running "shard-architecture.py")
  2. "{ARCH}/*.md" --Updated architecture document collection (*.md format)

## [Constraints]
  1. Must thoroughly review "{REQ}" and "{ARCH}/*.md" before proposing design (evidence: reference reviewed content in architecture draft using `Reference: {file path}#{section heading}` format)
  2. Must preserve existing contracts; any proposed changes must include explicit "Impact Analysis" subsection
  3. Must fully comply with "{TMPL}/architecture-tmpl.yaml" structure and section order
  4. Must draft to "{root}/docs/architecture.md", then execute: uv run "{SCRIPTS}/shard-architecture.py" to perform sharding
  5. Should use clear, concise English with 2-space indentation throughout
  6. Architecture design required external API call must use context7 (MCP) to search for library documentation and API references

## [Tools]
  1. **todo_write**
    - [Step 1: Track tasks; Steps 2-4: Track task status]
  2. **sequential-thinking (MCP)**
    - [Step 1: Evaluate extension points and constraints of existing architecture]
    - [Step 2: Design new module boundaries and integration patterns]
    - When to use: When need to evaluate multiple integration approaches or analyze impact scope
    - [Step 3: Structured drafting of architecture change document]
  3. **claude-context (MCP)**
    - [Step 1: Search existing architecture implementations, public contracts, and integration points]
    - Query examples: "What are the existing system boundaries?" "How is data flow implemented?" "What are the shared services?"
  4. **context7 (MCP)**
    - [Step 2: Query official API documentation and integration guidance for new integration technologies]
  5. **playwright (MCP)**
    - [Step 1-2: Research architecture migration patterns and integration cases]
    - When to use: When need to study how similar systems evolved their architecture or integrated new components

## [Steps]
  1. Evaluate Existing Architecture Phase
    - Understand current architecture, extension points, and constraints
    - Identify affected domains and dependencies
    - Establish progress tracking mechanism for design tasks

  2. Design New Module Phase
    - Achieve complete new module design with clear boundaries and interfaces
    - Ensure proper integration with existing components
    - Ensure comprehensive impact analysis for all proposed changes

  3. Documentation and Approval Phase
    - Achieve compliant architecture draft following template structure
    - Ensure user approval is obtained with proper feedback integration
    - Achieve successful architecture sharding by running the "shard-architecture.py" script with verified output under "{ARCH}/"

  4. Finalization Phase
    - Ensure all impact analyses are complete and accurate
    - Ensure compatibility between new and existing modules is verified

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
  
  4. **Decision Records for Changes**
    - Document why changes are needed with context and rationale
    - Explain integration approach and trade-offs
    - Annotate source references (source_refs) for all architecture statements

## [DoD]
  - [ ] "{REQ}" and "{ARCH}/*.md" have been thoroughly reviewed
  - [ ] Extension points, constraints, and affected domains have been identified
  - [ ] New module has documented boundaries, interfaces, and data flows
  - [ ] All proposed changes include explicit "Impact Analysis" subsections
  - [ ] Compatibility with existing contracts has been clarified (no breaking changes)
  - [ ] User approval has been obtained for architecture draft
  - [ ] "{root}/docs/architecture.md" exists and follows the template
  - [ ] "shard-architecture.py" has been executed and shard file generation has been verified

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

Work directory structure example:

```
{project_root}/
├── {config_dir}/                # {config_description}
│   ├── {settings_dir}/         # {settings_description}
│   └── {constants_dir}/        # {constants_description}
├── {src_dir}/                  # {src_description}
│   ├── {core_dir}/            # {core_description}
│   ├── {api_dir}/             # {api_description}
│   ├── {models_dir}/          # {models_description}
│   └── {utils_dir}/           # {utils_description}
├── {tests_dir}/               # {tests_description}
│   ├── {unit_dir}/           # {unit_description}
│   └── {integration_dir}/    # {integration_description}
├── {docs_dir}/               # {docs_description}
│   ├── {requirements_dir}/   # {requirements_description}
│   ├── {architecture_dir}/   # {architecture_description}
│   └── {guides_dir}/         # {guides_description}
└── {readme_file}             # {readme_description}
```
