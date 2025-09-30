<input>
  <context>
    1. Implementation plan document: {root}/docs/implementation-plan/{task_id}-plan.md
    2. Review results document: {root}/docs/review-results/{task_id}-review.md
  </context>
  <templates>
    1. Development notes template: {root}/sunnycore/templates/dev-notes-tmpl.yaml
  </templates>
</input>

<output>
  1. Code fixes implemented based on review findings
  2. Comprehensive development notes: {root}/docs/dev-notes/{task_id}-dev-notes.md
  Format:
  - 1) Enumerated list of implemented code fixes
  - 2) Markdown file path string for dev-notes
  Example:
  - 1) "Implemented fixes: input validation, error handling, and test coverage improvements"
  - 2) "{root}/docs/dev-notes/ABC-123-dev-notes.md"
</output>

<constraints importance="Important">
  - MUST: Changes are minimal, reversible, and scoped to identified issues
  - MUST: Preserve existing architecture, public APIs, and naming conventions; justify any new dependency in plan/dev-notes
  - MUST: Add or update tests to cover each fix/action and run tests after every change
  - SHOULD: Follow project style and lint rules; avoid unrelated reformatting or file churn
  - SHOULD: Keep todos updated per stages and record decisions/risks in the development notes
</constraints>

<workflow importance="Normal">
  <stage id="1: analyse_the_current_issues">
  <tools>
  <tool name="read_file" description="Review implementation plan and review results documents"/>
  <tool name="sequential_thinking" description="Decompose complex issues and analyze root causes"/>
  <tool name="claude_context" description="Load large review documents in segments if needed"/>
  </tools>
  - Read the review results document
  - Analyse current issues and root causes
  - Define the minimal effective fix for each issue

  <questions>
  - What are the root causes vs symptoms?
  - Which fixes have highest risk or impact?
  - Do we need design changes or refactors?
  </questions>
  </stage>

  <stage id="2: fix_the_issues">
  <tools>
  <tool name="sequential_thinking" description="Implement fixes iteratively, one at a time"/>
  <tool name="todo_write" description="Update todos to track the progress of the fixes"/>
  </tools>
  - Implement fixes iteratively, one at a time
  - Run and pass tests after each fix

  <questions>
  - Is each change minimal and reversible?
  - Do tests cover the fixed behavior?
  - Any regression risks identified?
  </questions>
  </stage>

  <stage id="3: enact_recommended_actions">
  <tools>
  <tool name="sequential_thinking" description="Enact the recommended actions iteratively"/>
  <tool name="todo_write" description="Update todos to track the progress of the actions"/>
  </tools>
  - Enact the recommended actions iteratively
  - Run and pass tests after each action
  
  <questions>
  - Are recommendations prioritized by value/effort?
  - Are acceptance criteria met per action?
  - Do changes align with architecture guidelines?
  </questions>
  </stage>

  <stage id="4: create_development_notes">
  - Conclude the development process and create development notes based on the template
  - If there is already an existing development notes, update the development notes with the new information
  - Save the markdown dev-notes to the stated directory

  <questions>
  - Are decisions and trade-offs documented?
  - Are next steps and risks recorded?
  - Are links to plans and reviews included?
  </questions>
  <checks>
  - [ ] Questions provided (2-3) for each stage
  - [ ] Tests pass after each fix/action
  - [ ] Dev-notes created at {root}/docs/dev-notes/{task_id}-dev-notes.md
  - [ ] No scope creep; todos remain atomic
  </checks>
  </stage>

</workflow>

