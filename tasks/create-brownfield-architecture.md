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
- **MUST** lead the user through question-driven checkpoints before committing to design updates, **MUST NOT** advance without explicit user acknowledgement

## [Instructions]
[Instructions]
1. **Step 1: Current-State Discovery Dialogue**
- **GOAL:** Build a validated view of existing system boundaries, contracts, and extension points with user confirmation before proposing changes.
- **STEPS:**
  - Summarize the existing architecture context to the user, highlighting known components, contracts, and extension points; ask targeted questions about undocumented behaviors or recent changes.
  - Capture the user's responses, risks, and constraints in structured notes aligned with the architecture template sections.
  - Agree with the user on outstanding gaps, research tasks, or additional artifacts needed prior to design.
- **QUESTIONS (for the user and self-check):**
  - Which areas of the current architecture need clarification from the user?  
  - Where does the user see stable extension points versus risky modifications?  
  - What constraints or tech debt does the user expect to influence the solution?
- **CHECKLIST:**
  - [ ] User confirmations logged for reviewed architecture artifacts and identified extension points.
  - [ ] Risks, constraints, and open questions captured with user acknowledgement.
  - [ ] Follow-up actions agreed before moving forward.

2. **Step 2: Co-Design Extension Strategy**
- **GOAL:** Define and iteratively refine an extension approach that preserves compatibility while meeting requirements, with user feedback at each decision.
- **STEPS:**
  - Present candidate integration patterns and component updates to the user, explaining trade-offs and asking for preferences or constraints.
  - For each change area, ask clarifying questions about operational impacts, dependencies, and compliance requirements before documenting decisions.
  - Collaboratively outline migration and rollback paths, capturing the user's approval or concerns for each critical scenario.
- **QUESTIONS (for the user and self-check):**
  - Which strategy does the user prefer for integrating new capabilities without breaking existing consumers?  
  - What additional safeguards does the user require for capacity, security, or compatibility?  
  - Are migration and rollback expectations acceptable to the user?
- **CHECKLIST:**
  - [ ] Extension design choices validated with the user and linked to requirements.
  - [ ] Impact analysis updated with user-supplied insights on interfaces, dependencies, and operations.
  - [ ] Migration and rollback plans documented with user-approved owners.

3. **Step 3: Document & Validate with User**
- **GOAL:** Produce template-compliant architecture documentation with full traceability, reviewed section-by-section with the user.
- **STEPS:**
  - Populate every required section of `{TMPL}/architecture-tmpl.yaml` in `{root}/docs/architecture.md`, referencing agreed requirements, decisions, and impacts.
  - After drafting each major section, summarize the content for the user, solicit feedback, and adjust before moving on.
  - Record user approvals, outstanding clarifications, and exception handling within the document or issue log.
- **QUESTIONS (for the user and self-check):**
  - Does the user accept how requirements and decisions are documented in each section?  
  - What additional evidence or references does the user need for risk, compatibility, or migration topics?  
  - Are any approvals pending before documentation can be finalized?
- **CHECKLIST:**
  - [ ] Template sections completed and validated with the user.
  - [ ] Requirement traceability, decision rationale, and impact analysis updated per user feedback.
  - [ ] User approvals or follow-up tasks recorded for each outstanding issue.

4. **Step 4: Verify Integration & Distribute Collaboratively**
- **GOAL:** Confirm compatibility between new and existing components with the user, then deliver finalized documentation.
- **STEPS:**
  - Review integration validation evidence with the user, confirming that updated and existing contracts, workflows, and data flows remain stable.
  - Walk through migration and rollback procedures, capturing any additional operational guidance requested by the user.
  - Execute `{SCRIPTS}/shard-architecture.py` after user sign-off, distribute `{ARCH}/*.md`, and inspect the outputs together for accuracy.
  - Update follow-up logs with agreed owners, due dates, and escalation paths.
- **QUESTIONS (for the user and self-check):**
  - What evidence satisfies the user that integrations remain compatible?  
  - Did the user confirm migration and rollback readiness?  
  - Do the sharded files match the user's expectations?
- **CHECKLIST:**
  - [ ] Integration validation reviewed with the user and accepted.
  - [ ] Migration and rollback procedures confirmed with responsible teams and user approval.
  - [ ] `{ARCH}/*.md` regenerated after user confirmation and verified collaboratively.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Existing architecture thoroughly understood and extension points identified  
- [ ] New components designed with impact analysis for any changes to existing system
- [ ] Architecture documentation created using template and properly sharded
- [ ] Integration compatibility verified between new and existing components