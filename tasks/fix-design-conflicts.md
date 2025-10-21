**GOAL**: Systematically resolve design conflicts identified in validation report while maintaining cross-document consistency and traceability.

## [Context]
**You must read the following context:**
- `{root}/docs/design-validation.md`

## [Products]  
- Modified design documents with resolved conflicts
- Cleaned validation report after successful resolution

## [Constraints]
- **MUST** fix in severity order (Critical→High→Medium→Low), **MUST NOT** fix out of order
- **MUST** obtain user confirmation for strategies, **MUST NOT** apply without confirmation  
- **MUST** maintain cross-document consistency, **MUST NOT** introduce new conflicts
- **MUST** complete all fixes before cleanup, **MUST NOT** delete reports prematurely

## [Steps]
Refer to the consolidated workflow in the Instructions section below.

## [Instructions]
1. **Step 1: Analyze and Prioritize Conflicts**
- **GOAL:** Establish a complete severity-ranked view of every conflict referenced in the validation report.
- **STEPS:**
  - Collect each conflict from `{root}/docs/design-validation.md` with source references and symptom descriptions.
  - Tag every conflict with severity (Critical→High→Medium→Low) and categorize by type (fabrication, reference, coverage, inconsistency).
  - Record cross-document dependencies and prerequisites between conflicts.
  - Build a structured conflict log capturing severity, type, impacts, and dependencies.
- **QUESTIONS:**
  - Have I captured every conflict and its exact source location?
  - Which conflicts block others because of shared dependencies or sequencing?
  - Is each severity assignment justified by delivery or compliance impact?
- **CHECKLIST:**
  - [ ] Conflict log includes severity, type, impacted documents, and dependencies.
  - [ ] Severity ordering reflects validation report priorities.
  - [ ] Cross-document relationships are documented.

2. **Step 2: Develop Comprehensive Fix Strategy**
- **GOAL:** Design an approved resolution strategy that minimizes new conflicts.
- **STEPS:**
  - Outline resolution options for every conflict with required document updates.
  - Assess cross-document impact and note safeguards that prevent cascading issues.
  - Sequence proposed fixes to respect dependencies while maximizing combined impact.
  - Prepare a recommended strategy summary emphasizing severity order and risk mitigations.
- **QUESTIONS:**
  - Does each strategy address the root cause rather than only the symptom?
  - Which options resolve multiple conflicts without violating constraints?
  - What confirmations or data are required from the user before execution?
- **CHECKLIST:**
  - [ ] Strategy covers all conflicts with severity-aligned plans.
  - [ ] Cross-document impacts and mitigations are documented.
  - [ ] User approval prerequisites are identified.

3. **Step 3: Execute Fixes Sequentially**
- **GOAL:** Implement approved fixes in strict severity order while maintaining consistency.
- **STEPS:**
  - Secure explicit user approval for the full fix strategy before modifying documents.
  - Apply fixes beginning with Critical issues, then High, Medium, and Low severities.
  - After each fix, validate cross-document consistency, references, and traceability.
  - Log progress, unexpected impacts, and any newly discovered conflicts.
- **QUESTIONS:**
  - Do I have recorded approval for the current fix sequence?
  - Have affected documents been revalidated immediately after each change?
  - Are any newly surfaced issues impacting the planned severity order?
- **CHECKLIST:**
  - [ ] User-approved plan documented prior to changes.
  - [ ] Fixes applied in strict severity order.
  - [ ] Verification notes captured for every implemented fix.

4. **Step 4: Verify Resolution Completeness**
- **GOAL:** Confirm all conflicts are resolved and overall design integrity is restored.
- **STEPS:**
  - Re-run comprehensive cross-document validation to confirm references and traceability.
  - Check that naming conventions, specifications, and dependencies remain consistent.
  - Document validation outcomes, proving no new conflicts exist.
  - Assemble verification evidence for user review and sign-off.
- **QUESTIONS:**
  - Does validation confirm zero unresolved conflicts or regressions?
  - Is 100% traceability coverage maintained after the fixes?
  - Have I recorded verifiable evidence for each validation activity?
- **CHECKLIST:**
  - [ ] Cross-document validation completed with zero outstanding conflicts.
  - [ ] Traceability and naming standards confirmed.
  - [ ] Verification evidence prepared for user review.

5. **Step 5: Complete Cleanup and Guidance**
- **GOAL:** Finalize documentation, capture learnings, and finish cleanup with user approval.
- **STEPS:**
  - Present consolidated change summary and verification results for user approval.
  - After approval, clean or archive the validation report to prevent confusion.
  - Recommend re-running automated validation to confirm a clean baseline.
  - Document lessons learned and provide guidance for the next workflow steps.
- **QUESTIONS:**
  - Has the user explicitly approved closure and cleanup actions?
  - What follow-up activities keep the system conflict-free?
  - Are next-step recommendations aligned with the project workflow?
- **CHECKLIST:**
  - [ ] User approved final resolution and cleanup.
  - [ ] Validation report cleaned or archived post-approval.
  - [ ] Next-step guidance recorded and communicated.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] All conflicts resolved in correct severity order with user approval obtained
- [ ] Cross-document consistency verified and no new conflicts introduced  
- [ ] User confirms all changes acceptable and validation report cleaned up