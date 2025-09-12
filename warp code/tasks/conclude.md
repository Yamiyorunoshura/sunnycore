<input>
  <context>
  1. {root}/docs/review-results/*.md - Review Records from development process
  2. {root}/sunnycore/templates/completion-report-tmpl.yaml - Completion Report Template
  </context>
  <templates>
  1. {root}/sunnycore/completion-report-tmpl.yaml - Project completion report template
  </templates>
</input>

<output>
1. {root}/docs/completion-report.md - Comprehensive Project Completion Report
</output>

<constraints, importance = "Important">
- Read only the specified inputs; do not invent content
- Keep 3–5 workflow stages; 2–3 items for questions/checks
- Produce concise, action-oriented bullets
- Use the provided completion report template sections
- Output exactly one file at the stated path
</constraints>

<workflow, importance = "Important">
  <stage id="0: create todo list">
  - Read the entire document
  - Recognise all the steps
  - Create a todo item for each step

  <questions>
  - Are all steps captured as actionable todos?
  - Is each todo unambiguous and outcome-focused?
  - Do todos map cleanly to the workflow stages?
  </questions>

  <checks>
  - [ ] Todos cover every stage in this file
  - [ ] Each todo has a clear completion outcome
  - [ ] Only one stage is in progress at a time
  </checks>
  </stage>

  <stage id="1: conclude the current issues">
  - Recognise all the issues from review results document
  - Think about the best solution to fix the issues
  - Conclude the issues with best solution

  <questions>
  - What root causes recur across review records?
  - What is the minimal viable fix for each issue?
  - Do any fixes introduce cross-cutting changes?
  </questions>

  <checks>
  - [ ] Each issue maps to a concrete, feasible fix
  - [ ] Fixes are scoped and prioritised
  - [ ] No identified issue is left without action
  </checks>
  </stage>

  <stage id="2: conclude the recommended actions">
  - Recognise all the recommended actions from review results document
  - Think about the best practices to enact the recommended actions
  - Conclude the recommended actions with best practices

  <questions>
  - Which actions yield the highest impact/effort ratio?
  - What dependencies or sequencing are required?
  - Which best practices or references support each action?
  </questions>

  <checks>
  - [ ] Actions are prioritised with brief rationale
  - [ ] Best practices are cited or summarised
  - [ ] Each action has measurable acceptance criteria
  </checks>
  </stage>

  <stage id="3: conclude the completion report">
  - Think about how to sum up the current issues and recommended actions
  - Create a completion report based on the template
  - Output the markdown format completion-report to the stated directory

  <questions>
  - Does the report clearly synthesise issues and actions?
  - Does it follow the template sections and structure?
  - Are all referenced paths and links valid?
  </questions>

  <checks>
  - [ ] Report saved at {root}/docs/completion-report.md
  - [ ] All template sections are filled without placeholders
  - [ ] Issues, fixes, and actions are cross-referenced consistently
  </checks>
  </stage>
</workflow>