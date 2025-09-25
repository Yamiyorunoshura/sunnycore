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
2. {root}/docs/tasks.md
</output>

<constraints, importance = "Critical">
- MUST execute all tests created during develop tasks phase and verify test results align with implementation plan.
- MUST verify that all production code strictly follows the implementation plan specifications and acceptance criteria.
- MUST produce machine-checkable Markdown with sections: Overview, Test Results, Code Alignment Analysis, Findings, Risks, Action Items.
- MUST cross-reference plan/code/notes with file paths, line ranges, or anchors when available.
- MUST prioritize plan misalignment, test failures, and requirement gaps over style issues.
- SHOULD keep each finding concise (<= 120 words) and one issue per bullet.
- MUST record an acceptance decision with rationale: Accept / Accept with changes / Reject.
</constraints>

<workflow, importance = "Important">
  <stage id="1: review-plan">
  - Read and understand the implementation plan
  - Identify verification approach and success criteria

  <questions>
  - Are acceptance criteria complete, testable, and measurable?
  - Are assumptions, risks, and rollback strategies explicitly stated?
  </questions>
  </stage>

  <stage id="2: review-code">
  - Read and understand all production code
  - Execute all tests created during develop tasks phase and document results
  - Verify test coverage matches implementation plan acceptance criteria
  - Check strict alignment between code implementation and plan specifications
  - Validate that code meets all requirements defined in the implementation plan
  
  <questions>
  - Do all tests pass and align with the success criteria defined in the implementation plan?
  - Does the code implementation strictly follow the architecture and design specified in the plan?
  - Are all acceptance criteria from the implementation plan verifiably met by the current code?
  - Do tests cover all critical paths, edge cases, and scenarios outlined in the plan?
  - Are security, performance, and observability requirements from the plan properly implemented?
  </questions>
  </stage>

  <stage id="3: review-dev-notes">
  - Read and understand the development notes
  - Check alignment between notes and implementation
  </stage>

  <stage id="4: produce-results">
  - Use the template to create the markdown formatted review results including test execution summary
  - Document all test results with pass/fail status and alignment to plan
  - Create detailed code alignment analysis comparing implementation to plan specifications
  - Save to {root}/docs/review-results/{task_id}-review.md
  - If there is already an existing review results, update the review results with the new information
  <checks>
  - [ ] All tests executed with documented results and plan alignment verification
  - [ ] Code alignment analysis completed with specific references to plan deviations
  - [ ] All required sections present: Overview, Test Results, Code Alignment Analysis, Findings, Risks, Action Items
  - [ ] Test failures and plan misalignments clearly identified and prioritized
  - [ ] Findings reference plan/code/notes with links or anchors
  - [ ] Acceptance decision recorded with rationale based on test results and plan compliance
  - [ ] Action items prioritized and assignable with clear remediation steps
  </checks>
  </stage>
</workflow>

