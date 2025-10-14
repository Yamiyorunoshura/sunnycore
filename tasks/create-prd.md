**GOAL**: Create Product Requirements Document integrating requirements, architecture, and tasks.

## [Input]
- User requirement description
- `{TMPL}/prd-tmpl.yaml`
- `{ARCH}/*.md` (if Brownfield)
- `{KNOWLEDGE}/*.md` (if exist)

## [Output]
- `{PRD}`

## [Constraints]
- **MUST** correctly identify project type (Greenfield/Brownfield), **MUST NOT** misidentify
- **MUST** create measurable requirements, **MUST NOT** create vague ones
- **MUST** exclude operational actions unless requested, **MUST NOT** include unnecessarily
- **MUST** provide impact analysis for Brownfield contract changes, **MUST NOT** break existing contracts

## [Steps]
1. Determine project type, gather context → Project type determined with context gathered
2. Define verifiable functional and quantified non-functional requirements → Complete requirements with acceptance criteria
3. Design architecture (Greenfield: new; Brownfield: extending with impact analysis) → Complete architecture documentation
4. Integrate requirements, architecture, tasks into unified PRD → Integrated PRD with full traceability
5. Complete PRD, save to "{PRD}", obtain confirmation → Approved PRD created

## [DoD]
- [ ] Functional and non-functional requirements with quantified metrics and Given-When-Then criteria
- [ ] Architecture complete with 100% requirement mapping and impact analysis (if Brownfield)
- [ ] PRD at "{PRD}" approved by user

## [Example]

### Good #1
**Input**: "Export dashboard data to CSV/PDF". Existing arch: Dashboard Service (React), Analytics API (Node.js), PostgreSQL  
**Decision**: Brownfield confirmed (arch exists)→Read existing arch→Define: REQ-001 (CSV export), REQ-002 (PDF with charts), NFR-001 (export <5s for 10K rows), Given-When-Then criteria→Design: add Export Service using Analytics API, no breaking changes→Impact Analysis: new endpoints only→Map: REQ-001→Export Service→Task-1, REQ-002→Task-2, 100% coverage→Generate PRD→Approval  
**Why Good**: Handles Brownfield carefully, reviews existing assets, documents impacts, preserves compatibility

### Good #2
**Input**: "Add 2FA for login". No existing architecture  
**Decision**: Greenfield→Define: REQ-001 (TOTP generation), REQ-002 (code verification), NFR-001 (RFC 6238 compliance)→Quantified all NFRs→Design: Auth Service (FastAPI), Redis (TOTP storage), PostgreSQL→Components, data flows, ADRs→Task-1 (TOTP setup), Task-2 (verification), Task-3 (backup codes)→Complete req→arch→task mapping→Generate PRD→Approval  
**Why Good**: Identifies Greenfield, designs end-to-end, embeds quantifiable requirements and task mapping

### Bad #1
**Input**: User describes requirement  
**Bad Decision**: Skip project type determination→Create vague requirements: "fast system"→Mix functional and non-functional→No Given-When-Then→Fabricate component names→No traceability→Skip approval→Save incomplete PRD  
**Why Bad**: Violates project type identification, vague unmeasurable requirements, no traceability, unusable PRD  
**Correct**: Determine project type (check docs/architecture/)→Create SMART requirements (specific, measurable)→Given-When-Then for acceptance→Quantify NFRs (P95 <200ms, not "fast")→Design with 100% mapping→Obtain approval
