<input>
  <context>
  1. {root}/docs/dev-notes/{task_id}-dev-notes.md
  2. {root}/docs/implementation-plan/{task_id}-plan.md
  3. {root}/sunnycore/templates/review-tmpl.yaml
  4. {root}/sunnycore/CLAUDE.md
    - QA rules
  </context>
  <templates>
  1. review-tmpl.yaml
  2. dev-notes-tmpl.yaml
  </templates>
</input>

<output>
1. {root}/docs/review-results/{task_id}-review.md
   Format: Machine-checkable Markdown with sections [Overview, Test Results, Code Alignment Analysis, Findings, Risks, Action Items] and a final Acceptance Decision (Accept/Accept with changes/Reject).
   Example: Create or update the review file with headings, cross-references to plan/code/notes using file paths and line ranges, and a summarized pass/fail test matrix aligned to acceptance criteria.
2. {root}/docs/tasks.md
   Format: Updated tasks status reflecting review outcomes and action items while preserving existing structure.
   Example: Modify the row for {task_id} to include review status, acceptance decision, and prioritized action items.
</output>

<constraints importance="Critical">
- MUST execute all tests created during develop tasks phase and verify test results align with implementation plan.
- MUST verify that all production code strictly follows the implementation plan specifications and acceptance criteria.
- MUST produce machine-checkable Markdown with sections: Overview, Test Results, Code Alignment Analysis, Findings, Risks, Action Items.
- MUST cross-reference plan/code/notes with file paths, line ranges, or anchors when available.
- MUST record an acceptance decision with rationale: Accept / Accept with changes / Reject.
</constraints>

<workflow importance="Important">
  <stage id="1: review_plan">
  <tools>
    <tool name="sequential_thinking" description="Structured reasoning"/>
    <tool name="todo_write" description="Execution tracking"/>
    <tool name="Claude-Context" description="Process large plan documents in segments"/>
  </tools>
  - Read and understand the implementation plan
  - Identify verification approach and success criteria

  <questions>
  - Are acceptance criteria complete, testable, and measurable?
  - Are assumptions, risks, and rollback strategies explicitly stated?
  </questions>
  </stage>

  <stage id="2: review_code">
  <tools>
    <tool name="todo_write" description="Execution tracking"/>
    <tool name="sequential_thinking" description="Analyze code against plan"/>
    <tool name="Claude-Context" description="Process large plan documents in segments"/>
  </tools>
  - Read and understand all production code
  - Execute all tests and document pass/fail with alignment to plan
  - Verify coverage and strict alignment to architecture/design and acceptance criteria

  <questions>
  - Do all tests pass and align with the success criteria defined in the implementation plan?
  - Are security, performance, and observability requirements from the plan properly implemented?
  </questions>
  </stage>

  <stage id="3: review_dev_notes">
  <tools>
    <tool name="sequential_thinking" description="Structured reasoning"/>
    <tool name="todo_write" description="Execution tracking"/>
  </tools>
  - Read and understand the development notes
  - Check alignment between notes and implementation
  </stage>

  <stage id="4: produce_results">
  <tools>
    <tool name="sequential_thinking" description="Synthesize results"/>
    <tool name="todo_write" description="Finalize tracking"/>
  </tools>
  - Create review results using the template, including test execution summary
  - Document test results with pass/fail status and plan alignment; analyze code alignment with specific references
  - Save to {root}/docs/review-results/{task_id}-review.md; update if file exists

  <checks>
  - [ ] All tests executed with documented results and plan alignment verification
  - [ ] Code alignment analysis completed with specific references to plan deviations
  - [ ] All required sections present: Overview, Test Results, Code Alignment Analysis, Findings, Risks, Action Items
  - [ ] Test failures and plan misalignments clearly identified and prioritized
  - [ ] Acceptance decision recorded with rationale based on test results and plan compliance
  </checks>
  </stage>
</workflow>

