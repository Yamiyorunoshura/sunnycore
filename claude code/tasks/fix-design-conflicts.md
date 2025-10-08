**GOAL**: Fix design conflicts and inconsistencies identified in design validation report, then clean up the validation report file.

## [Input]
  1. "{root}/docs/design-validation.md" --Validation report with identified issues

## [Output]
  1. Modified design documents based on conflict resolution:
    - "{PRD}" (if PRD workflow was used)
    - "{REQ}/*.md" (if full workflow was used)
    - "{ARCH}/*.md" (if full workflow was used)
    - "{EPIC}" (if full workflow was used)
    - "{PLAN}/*.md" (if full workflow was used)
  2. Deleted: "{root}/docs/design-validation.md" (after successful fixes)

## [Constraints]
  1. Must read and parse design-validation.md to extract all issues
  2. Must prioritize fixes by severity (Critical → High → Medium → Low)
  3. Must interact with user to confirm fix strategy for each issue
  4. Must preserve document structure and formatting
  5. Must maintain consistency across all modified documents
  6. Must delete design-validation.md only after all fixes are complete
  7. Must recommend re-running validate-design to confirm fixes

## [Tools]
  1. **todo_write**
    - [Step 1: Create todo list with all issues to fix; Steps 2-4: Track fix progress]
  2. **sequentialthinking (MCP)**
    - [Step 1: Analyze issues and determine fix strategies; Step 2-3: Reason about conflict resolution and consistency maintenance]
  3. **claude-context (MCP)**
    - [Step 2: Search codebase when verifying fixes impact existing code]

## [Steps]
  1. Analysis Phase
    - Read all workflow steps to understand expected work
    - Verify "{root}/docs/design-validation.md" exists
    - Parse validation report and extract all issues with:
      - Issue ID/number
      - Severity level
      - Issue type (fabricated content, broken reference, conflict, inconsistency, coverage gap)
      - Affected documents and locations
      - Description and impact
    - Group issues by severity and type
    - Create todo list with all issues to be fixed, ordered by severity

  2. Fix Planning Phase
    - For each issue (starting with Critical, then High, Medium, Low):
      - 2.1. Analyze Issue Context
        - Identify root cause of the issue
        - Determine which documents need to be modified
        - Assess impact of potential fixes on other documents
      
      - 2.2. Present Fix Options to User
        - Explain the issue clearly with context
        - Propose 2-3 fix strategies (if multiple approaches exist)
        - Highlight recommended approach and rationale
        - Show affected files and approximate changes needed
      
      - 2.3. Get User Confirmation
        - Wait for user to select fix strategy or provide custom approach
        - Clarify any ambiguities before proceeding
        - if user approves then proceed to 2.4, else revise proposal

      - 2.4. Record Fix Plan
        - Document selected fix strategy
        - List all files to be modified
        - Note any dependencies on other fixes

  3. Fix Execution Phase
    - For each approved fix (in priority order):
      - 3.1. Apply Document Changes
        - Read affected documents
        - Apply fixes according to selected strategy
        - Ensure consistency with related documents
        - Preserve formatting and structure
      
      - 3.2. Cross-Document Consistency Check
        - if fix involves terminology change, update all occurrences across all documents
        - if fix involves adding/removing entities, update all references
        - if fix involves architecture change, propagate to tasks and plans
      
      - 3.3. Verify Fix Completeness
        - Confirm the specific issue is resolved
        - Check for any new issues introduced by the fix
        - Update todo list to mark issue as fixed

  4. Validation Phase
    - Review all changes made
    - Perform quick consistency check across modified documents
    - Verify no new conflicts or issues were introduced
    - Present summary of all fixes to user
    - Request user confirmation that all issues are addressed

  5. Cleanup Phase
    - Delete "{root}/docs/design-validation.md"
    - Recommend user to re-run validation to confirm fixes:
      - if PRD workflow: `/sunnycore_po *validate-design prd`
      - if full workflow: `/sunnycore_po *validate-design full`
    - Provide summary of changes made and files modified

## [Fix-Strategies]

### For Fabricated Content:
  - Remove fabricated references
  - Replace with actual existing entities
  - Add missing entities if they should exist

### For Broken References:
  - Update references to correct entity IDs
  - Create missing entities if needed
  - Remove orphaned references

### For Conflicts:
  - Identify authoritative source (usually requirements)
  - Update conflicting documents to match
  - Resolve contradictions by choosing one approach

### For Inconsistent Naming:
  - Establish canonical naming convention
  - Update all occurrences across all documents
  - Create glossary if needed

### For Coverage Gaps:
  - Add missing mappings (req → arch → task → plan)
  - Create missing entities if needed
  - Remove orphaned entities if they are not needed

### For Terminology Inconsistencies:
  - Standardize terms across all documents
  - Use find-and-replace for consistent updates
  - Document terminology decisions

## [Error-Handling]
  1. Validation report missing: Cannot proceed, ask user to run validate-design first
  2. Validation report shows no issues: Nothing to fix, inform user and exit gracefully
  3. User rejects all fix proposals: Document user's concerns and stop execution
  4. Fix introduces new conflicts: Revert changes and propose alternative approach
  5. Critical files cannot be modified: Report error and list problematic files

## [DoD]
  - [ ] Design validation report has been read and parsed
  - [ ] All issues have been extracted and categorized
  - [ ] Fix strategies have been proposed for all issues
  - [ ] User has approved fix strategies
  - [ ] All approved fixes have been applied
  - [ ] Cross-document consistency has been verified
  - [ ] No new issues have been introduced
  - [ ] User confirmation obtained for all changes
  - [ ] "{root}/docs/design-validation.md" has been deleted
  - [ ] User has been advised to re-run validate-design for confirmation

