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
**You should work along to the following steps:**
1. **Analyze and prioritize conflicts** - Systematically categorize all issues by severity and impact
2. **Develop comprehensive fix strategy** - Create detailed resolution plans with cross-document impact analysis  
3. **Execute fixes sequentially** - Apply approved fixes in priority order while maintaining consistency
4. **Verify resolution completeness** - Validate all conflicts resolved and no new issues introduced
5. **Complete cleanup and guidance** - Finalize documentation and provide next-step recommendations

## [Instructions]

### 1. Analyze and Prioritize Conflicts
**Objective**: Create comprehensive understanding of all design conflicts and their relationships.

**Approach**:
- Extract all issues from the validation report, categorizing by type (fabricated content, broken references, coverage gaps, inconsistencies)
- Assign severity levels (Critical→High→Medium→Low) based on impact to development progress
- Identify cross-document dependencies where fixing one issue affects others
- Create issue tracking matrix showing relationships and fix order requirements

**Focus**: Understand the complete conflict landscape before developing solutions. Look for patterns and root causes that may indicate systemic issues requiring broader fixes.

### 2. Develop Comprehensive Fix Strategy  
**Objective**: Design systematic resolution approach with minimal risk of introducing new conflicts.

**Approach**:
- For each conflict, develop specific fix strategies considering multiple resolution options
- Analyze cross-document impact of each proposed fix to avoid cascade failures
- Prioritize fixes that resolve multiple issues simultaneously when possible
- Design fix sequence that respects document dependencies and maintains referential integrity
- Create detailed plan documenting all strategies and their rationale

**Focus**: Design fixes that address root causes, not just symptoms. Consider how each fix affects the entire document ecosystem.

### 3. Execute Fixes Sequentially
**Objective**: Apply approved fixes systematically while maintaining consistency throughout the process.

**Approach**:
- Obtain explicit user approval for the complete fix strategy before beginning implementation
- Execute fixes in strict severity order (Critical first, then High, Medium, Low)
- After each fix, immediately verify cross-document consistency and referential integrity
- Track progress and document any unexpected impacts or additional issues discovered
- Maintain running verification that no new conflicts are introduced

**Focus**: Methodical execution with continuous validation. Each fix should improve overall design health without degrading other aspects.

### 4. Verify Resolution Completeness
**Objective**: Confirm all conflicts resolved and overall design integrity restored.

**Approach**:
- Perform comprehensive cross-document validation to ensure all references are valid
- Verify 100% traceability coverage is maintained across all document relationships  
- Check that all naming conventions and specifications are consistent
- Validate that no new conflicts were inadvertently introduced during fix process
- Document complete verification results for user review

**Focus**: Thorough validation that goes beyond the original conflicts to ensure overall design health.

### 5. Complete Cleanup and Guidance  
**Objective**: Finalize resolution process and provide clear next steps.

**Approach**:
- Present complete change summary to user for final approval
- Only after user confirmation, remove the validation report to prevent confusion
- Recommend re-running validation to confirm clean state
- Provide summary of resolution process and any lessons learned
- Guide user on next appropriate steps in the development workflow

**Focus**: Proper closure with user agreement and clear path forward. Ensure no cleanup occurs without explicit user approval.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] All conflicts resolved in correct severity order with user approval obtained
- [ ] Cross-document consistency verified and no new conflicts introduced  
- [ ] User confirms all changes acceptable and validation report cleaned up

## [Example]

### Good: Systematic Conflict Resolution
**Input**: Validation shows critical fabricated references and coverage gaps across multiple documents  
**Decision**: Extract and categorize all issues by severity. Develop comprehensive fix strategy addressing cross-document impacts. Obtain user approval for complete plan. Execute fixes in Critical→High→Medium→Low order, verifying consistency after each change. Validate complete resolution and obtain final user confirmation before cleanup.  
**Why Good**: Follows systematic approach with proper prioritization, user approval, and thorough validation.

### Bad: Unstructured Fixes
**Input**: Multiple conflicts of varying severity requiring systematic resolution  
**Bad Decision**: Apply fixes randomly without severity ordering. Skip user approval process. Make changes across documents without tracking impacts. Clean up validation report before confirming resolution completeness.  
**Why Bad**: Violates severity-order requirement, bypasses user confirmation, risks introducing new conflicts, and premature cleanup prevents verification.  
**Correct**: Analyze all conflicts systematically, develop approved strategy, execute in proper order with continuous validation, confirm user approval before any cleanup.
