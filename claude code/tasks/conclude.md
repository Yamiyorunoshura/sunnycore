<input>
  <context>
  1. {root}/docs/review-results/*.md - Review Records from development process
  </context>
  <templates>
  1. {root}/sunnycore/templates/completion-report-tmpl.yaml - Project completion report template
  </templates>
</input>

<output>
1. {root}/docs/completion-report.md - Comprehensive Project Completion Report
</output>

<constraints importance="Important">
- MUST: Read only the specified inputs; do not invent content
- MUST: Use the provided completion report template sections; fill 100% with no placeholders
- MUST: Produce concise, action-oriented bullets (each ≤ 16 words; ≤ 5 bullets/section)
- MUST: Output exactly one file at {root}/docs/completion-report.md (overwrite if exists)
- SHOULD: Use English for all generated content (ascii_letter_ratio_v1 ≥ 0.95)
</constraints>

<workflow importance="Important">
  <stage id="1: conclude_current_issues">
  <tools>
    <tool name="sequential_thinking"/>
    <tool name="todo_write"/>
  </tools>
  - Extract all issues from the review records
  - Define the minimal effective fix for each issue
  - Finalise each issue with assigned fix and priority
  
  <questions>
  - What root causes recur across review records?
  - What is the minimal viable fix for each issue?
  - Do any fixes introduce cross-cutting changes?
  </questions>
  </stage>
  
  <stage id="2: conclude_recommended_actions">
  <tools>
    <tool name="sequential_thinking"/>
    <tool name="todo_write"/>
  </tools>
  - Extract all recommended actions from the review records
  - Specify best-practice approach and sequencing per action
  - Finalise the action plan with rationale and sequencing
  
  <questions>
  - Which actions yield the highest impact/effort ratio?
  - What dependencies or sequencing are required?
  - Which best practices or references support each action?
  </questions>
  </stage>
  
  <stage id="3: conclude_completion_report">
  <tools>
    <tool name="sequential_thinking"/>
    <tool name="todo_write"/>
  </tools>
  - Synthesise issues and actions into a coherent summary
  - Draft the completion report using the template
  - Save the Markdown report to the stated path
  
  <questions>
  - Does the report clearly synthesise issues and actions?
  - Does it follow the template sections and structure?
  - Are all referenced paths and links valid?
  </questions>
  
  <checks>
  - [ ] Report saved at {root}/docs/completion-report.md
  - [ ] All template sections are filled without placeholders
  - [ ] Issues, fixes, and actions are cross-referenced consistently
  - [ ] English content ratio ≥ 0.95 (ascii_letter_ratio_v1) in generated report
  </checks>
  </stage>

  <stage id="4: cleanup_for_next_development">
  <tools>
    <tool name="bash"/>
  </tools>
  - Delete {root}/docs/requirements/*.md files to clear requirements documentation
  - Delete {root}/docs/tasks.md to clear task documentation
  - Prepare project structure for next development cycle

  <questions>
  - Are all requirements files in {root}/docs/requirements/ successfully deleted?
  - Is the tasks.md file successfully deleted?
  - Is the project ready for the next development iteration?
  </questions>

  <checks>
  - [ ] All files in {root}/docs/requirements/ directory are deleted
  - [ ] {root}/docs/tasks.md file is deleted
  - [ ] Project structure is cleaned and ready for next development
  </checks>
  </stage>
</workflow>

