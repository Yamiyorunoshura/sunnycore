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
  2. Comprehensive development notes: {root}/docs/dev-notes/{task_id}-notes.md
</output>

<workflow, importance = "Normal">
  <stage id="0: Create a todo list">
  - Read the entire document
  - Recognise all the steps
  - create a todo item for each step

  <questions>
  - Have all steps been enumerated without omission?
  - Are todos atomic and actionable?
  - Is naming consistent with project conventions?
  </questions>
  </stage>

  <stage id="1: Analyse the current issues">
  - Read the review results document
  - Analyse the current issues
  - Think about the best solution to fix the issues

  <questions>
  - What are the root causes vs symptoms?
  - Which fixes have highest risk or impact?
  - Do we need design changes or refactors?
  </questions>
  </stage>

  <stage id="2: Fix the issues">
  - Update the todo list with the steps of the best solution
  - Fix the issues one by one
  - Test if the code works after each fix

  <questions>
  - Is each change minimal and reversible?
  - Do tests cover the fixed behavior?
  - Any regression risks identified?
  </questions>
  </stage>

  <stage id="3: Enact recommended actions">
  - Update the todo list with the steps of the recommended actions
  - Enact the recommended actions one by one
  - Test if the code works after each recommended action

  <questions>
  - Are recommendations prioritized by value/effort?
  - Are acceptance criteria met per action?
  - Do changes align with architecture guidelines?
  </questions>
  </stage>

  <stage id="4: Create a development notes">
  - Conclude the development process
  - Create a development notes based on the template
  - Output the markdown format dev-notes to the stated directory

  <questions>
  - Are decisions and trade-offs documented?
  - Are next steps and risks recorded?
  - Are links to plans and reviews included?
  </questions>
  </stage>

  <checks>
  - [ ] Questions provided (2-3) for each stage
  - [ ] Tests pass after each fix/action
  - [ ] Dev-notes created at {root}/docs/dev-notes/{task_id}-notes.md
  - [ ] No scope creep; todos remain atomic
  </checks>
</workflow>