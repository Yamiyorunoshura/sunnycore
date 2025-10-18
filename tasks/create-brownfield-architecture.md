**GOAL**: Create architecture change documentation for Brownfield projects.

## [Context]
**You must read the following context:**
- `{REQ}` - Requirements to understand what needs to be built
- `{ARCH}/*.md`(Only the related documents) - Existing architecture to understand current system
- `{SCRIPTS}/shard-architecture.py` - Tool for distributing architecture content
- `{TMPL}/architecture-tmpl.yaml` - Template structure for architecture documentation
- `{KNOWLEDGE}/*.md` - Domain knowledge and patterns

## [Products]
- `{root}/docs/architecture.md` (temporary consolidation)
- `{ARCH}/*.md`(Only the related documents) (updated distributed architecture files)

## [Constraints]
- **MUST** understand existing architecture before designing changes
- **MUST** preserve backward compatibility or provide migration paths
- **MUST** use architecture template structure for consistency

## [Instructions]
[Instructions]
1. **Step 1: Understand Current Architecture**
- **GOAL:** Build a validated view of existing system boundaries, contracts, and extension points before proposing changes.
- **STEPS:**
  - Gather the relevant requirements, knowledge base notes, and architecture files that scope the brownfield change.
  - Read the selected architecture documents to map components, contracts, dependencies, and active integration patterns.
  - Capture constraints, technical debt, and candidate extension points in working notes aligned with the architecture template sections.
  - Confirm outstanding knowledge gaps or risks with stakeholders or existing documentation before moving on.
- **QUESTIONS:**
  - Which architecture files map directly to the targeted requirements and domains?
  - Where do stable extension points exist versus areas that would require risky modifications?
  - What constraints (tech debt, version locks, compliance rules) could block or alter the extension plan?
- **CHECKLIST:**
  - [ ] All relevant architecture artifacts reviewed and annotated.
  - [ ] Extension points and dependencies cataloged with rationale.
  - [ ] Risks, constraints, and open questions logged for follow-up.

2. **Step 2: Design Extension Strategy**
- **GOAL:** Define an extension approach that preserves compatibility while meeting the new requirements.
- **STEPS:**
  - Select integration patterns that favor extension points and avoid breaking existing contracts.
  - Draft proposed component updates using the architecture template sections (system architecture, components, data flows).
  - Evaluate impacts on current interfaces, dependencies, and operational characteristics, documenting mitigation options.
  - Outline migration and rollback paths to cover any unavoidable changes to existing components.
- **QUESTIONS:**
  - Which integration pattern delivers the requirement with minimal disruption to current consumers?
  - Do new or modified components rely on existing services that need capacity, security, or version adjustments?
  - How will we maintain backward compatibility or notify consumers about required migrations?
- **CHECKLIST:**
  - [ ] Extension design leverages documented extension points or provides a justified alternative.
  - [ ] Impact analysis completed for interfaces, dependencies, and operations.
  - [ ] Migration and rollback strategy drafted with owners identified.

3. **Step 3: Document and Validate**
- **GOAL:** Produce template-compliant architecture documentation with full traceability and stakeholder validation.
- **STEPS:**
  - Populate every required section of `architecture-tmpl.yaml` with the updated system overview, component details, and data flows.
  - Link requirements, decisions, and impacts to the appropriate sections to maintain traceability.
  - Share the draft with stakeholders for review, focusing on compatibility, risk, and migration coverage; incorporate agreed feedback.
  - Record approvals or explicit exceptions before proceeding to distribution.
- **QUESTIONS:**
  - Are all mandatory template sections (introduction, components, data flows, external APIs) updated with the latest design?
  - Does each requirement map to architecture elements, decisions, or components in the document?
  - Which stakeholders must sign off, and what open issues remain before approval?
- **CHECKLIST:**
  - [ ] Architecture document fully populated and consistent with the template.
  - [ ] Requirement traceability and decision rationale documented.
  - [ ] Stakeholder feedback addressed and approvals recorded.

4. **Step 4: Verify Integration and Distribute**
- **GOAL:** Confirm compatibility between new and existing components and deliver finalized documentation.
- **STEPS:**
  - Validate that updated and existing contracts, workflows, and data flows operate together via targeted tests or reviews.
  - Execute migration and rollback checks, ensuring procedures are documented for operations teams.
  - Run `{SCRIPTS}/shard-architecture.py` to distribute the consolidated document into `{ARCH}/*.md` and inspect outputs for accuracy.
  - Capture remaining follow-up items, regressions, or operational handoffs.
- **QUESTIONS:**
  - What evidence confirms that core contracts and integrations remain stable after the extension?
  - How will operations respond if migration steps fail or need to be rolled back?
  - Did the sharding process update all distributed architecture files without conflicts?
- **CHECKLIST:**
  - [ ] Integration validation completed and findings documented.
  - [ ] Migration and rollback procedures confirmed with responsible teams.
  - [ ] Sharded architecture files regenerated and verified.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Existing architecture thoroughly understood and extension points identified  
- [ ] New components designed with impact analysis for any changes to existing system
- [ ] Architecture documentation created using template and properly sharded
- [ ] Integration compatibility verified between new and existing components

## [Example]

### Good #1: Authentication Enhancement
**Input**: Existing REST API with basic auth. REQ-001: Add OAuth2 authentication  
**Approach**: 
1. **Discovery**: Read existing User Service and API Gateway architecture, map current auth flow
2. **Design**: Design OAuth2 Server as new component, integrate via existing auth middleware extension points
3. **Documentation**: Create comprehensive architecture using template, show requirement traceability  
4. **Verification**: Confirm existing basic auth continues working, validate OAuth2 integration
**Why Good**: Follows systematic discovery, uses extension points, preserves existing functionality, complete documentation.

### Good #2: Analytics Addition  
**Input**: Existing CMS with PostgreSQL+Redis. Requirements for analytics and behavior tracking
**Approach**:
1. **Discovery**: Map existing CMS architecture, identify event bus as natural extension point
2. **Design**: Add Analytics Collector and ClickHouse as isolated components subscribing to events
3. **Documentation**: Document new components with ADRs, maintain requirement traceability
4. **Verification**: Confirm CMS performance unaffected, validate analytics data flow
**Why Good**: Leverages existing patterns, minimal system impact, complete architectural documentation.

### Bad #1: Assumption-Based Design
**Input**: Need to add new feature to existing system  
**Bad Approach**: Skip architecture review, assume integration points, design without understanding existing contracts, ignore impact analysis.  
**Why Bad**: Violates discovery phase, risks breaking existing functionality, creates integration problems.  
**Correct Approach**: Systematically read existing architecture, understand extension points, design for compatibility, document all impacts.
