# PO Conclude Task Execution Instructions

<task_metadata>
name: "PO Conclude Task Execution"
version: "2.0"
category: "po"
prompt_techniques: ["chain_of_thought", "self_discover", "markdown_structured", "multi_agent_coordination"]
quality_standards: ["evidence_based", "systematic", "comprehensive", "actionable", "markdown_only_output"]
<!-- task_metadata>

## Task Overview
When the user calls the `*conclude` command, coordinate multi-agent synchronous and sequential execution according to the unified concluding workflow to complete project closure, documentation outputs, and knowledge curation.

- **Multi-Agent Collaboration Targets**: Collaborate with `po_project-concluder`, `po_file-classifier`, `po_knowledge-curator`, and `po_architecture-documenter`.
- **Follow Workflow**: `{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.yaml`.
- **Enforcement**: Comply with `{project_root}/sunnycore/po/enforcement/po_project-concluder-enforcement.md`.
- **Output Standard**: All external documents must be Markdown-only (no XML tags in final deliverables).

## Execution Steps (SELF-DISCOVER Framework)

### Step 1: Requirements Understanding and Context Establishment (SELECT)
1. Identify `*conclude` intent and expected outputs (completion report, knowledge/architecture docs, classification report).
2. Load required files and aliases:
   - WORKFLOW_FILE → `{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.yaml`
   - REPORT_TEMPLATE → `{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml`
   - ENFORCEMENT_FILE → `{project_root}/sunnycore/po/enforcement/po_project-concluder-enforcement.md`
3. Verify prerequisites (QA passed, plan traceability, QA feedback collected or acknowledged as missing).

### Step 2: Load Mandatory Enforcement Rules (ADAPT)
1. Strictly follow `po_project-concluder-enforcement.md` mandatory clauses:
   - Determinism: Use fixed parameters (temperature=0, top_p=1, seed=42) to ensure stable output ordering and path normalization.
   - Evidence-driven: Every conclusion must have traceable evidence (PRs, commits, files, tests, measurements).
   - Template compliance: Completion report must fully match the template structure; placeholders are forbidden.
   - Markdown standard: Final external documents must be Markdown only.
2. If key files are missing or prerequisites fail, stop immediately and report the blocking reason (fail-fast).

### Step 3: Establish Strategy per Workflow (IMPLEMENT)
1. Use workflow phases to plan conclusion strategy and evidence collection:
   - workflow_initialization → Load workflow/template and verify accessibility.
   - conclusion_strategy → Clarify focus scope and evidence sources.
   - evidence_collection → Collect specs, plans, implementation and quality evidence, QA feedback, repository Markdown analysis.
   - delivery_synthesis → Align with original scope, verify acceptance criteria and test evidence.
   - qa_problem_analysis → Extract QA issues, record status and risks.
   - enhancement_planning → Propose follow-up enhancements with success criteria.
   - report_generation → Generate completion report using the template (no placeholders, include evidence).
   - finalization → Readback check, format validation, and temp file cleanup.

### Step 4: Apply and Coordinate (APPLY)
1. Parallel phase (synchronous with conclude call):
   - `po_project-concluder`: Produce core analysis and report content (final output is Markdown).
   - `po_file-classifier`: Perform file classification/cleanup, produce classification report and feed back risks and cleanup logs.
2. Sequential phase (after report generation):
   - `po_knowledge-curator`: Generate/update `{project_root}/docs/knowledge/engineering-lessons.md`.
   - `po_architecture-documenter`: Generate/update `{project_root}/docs/architecture/architecture.md`.
3. Integrate all agent outputs and perform Cross-Agent Consistency checks.

## Quality Gates
1. Input gate: Workflow/template/enforcement loaded and readable; prerequisites pass.
2. Evidence gate: Every claim in the completion report has a concrete evidence link (PR/commit/docs/tests/measurements).
3. Template gate: Fully aligned with template; no placeholders like `< >` or `{}`; use actual values.
4. Markdown gate: No XML tags in external documents; headings/lists/tables/code blocks are syntactically correct.
5. Consistency gate: Agents are consistent in scope, terminology, paths, metrics, and conclusions.

## Deliverables and Paths
- Completion report: `{{project_root}}/docs/completion-reports/{{task_id}}-completion.md` (Markdown only)
- Knowledge curation: `{{project_root}}/docs/knowledge/engineering-lessons.md`
- Architecture documentation: `{{project_root}}/docs/architecture/architecture.md`
- File classification report: `{{project_root}}/docs/file-classification/file-classification-report.md`

## Failure Handling Strategy
- Missing key files / failed prerequisites: Stop immediately and report (blocker).
- Insufficient evidence: Mark limitations and supplement plan in the report; do not block other sections.
- Template non-compliance: List diffs and a fix plan; require remediation before passing gates.
- Parallel collaboration conflicts: Record conflicts; adjust order or inputs; ensure consistency then retry.

## Best Practices (Prompt Engineering)
- Use Chain of Thought for strategy and integration decisions; final deliverables are Markdown.
- Drive execution with SELF-DISCOVER (SELECT/ADAPT/IMPLEMENT/APPLY).
- XML is for internal reasoning; final external documents are Markdown-only.
- Be evidence-driven throughout; include concrete file/PR/test/measurement links and values.
- Prefer parallel-before-sequential multi-agent execution, then perform consistency checks during integration.

## Definition of Done (DoD)
- All workflow phases completed with corresponding outputs.
- Every section of the completion report is filled with actual content; no placeholders.
- All conclusions are traceable to concrete evidence; all quality gates pass.
- Knowledge and architecture docs updated; file classification report and cleanup logs integrated into the completion report.
- Temporary files cleaned up; documents are ready for stakeholders.


