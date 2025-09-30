<input>
  <context>
  1. {root}/docs/architecture/*.md (context)
  </context>
  <rules>
  2. {root}/sunnycore/CLAUDE.md (rules)
  </rules>
  <template>
  3. {root}/sunnycore/templates/architecture-tmpl.yaml (template)
  </templates>
</input>

<output>
1. {root}/docs/architecture/*.md
Format: Markdown
</output>

<constraints importance="Important">
- MUST: Produce valid JSON exactly matching the schema (additionalProperties=false)
- MUST: Output no text outside JSON when producing deliverables
- SHOULD: Use 3 stages and place <checks> in the last stage
- SHOULD: Map each produced file to at least 1 source reference
- MAY: Include architecture diagrams as fenced Markdown code blocks
</constraints>

<workflow importance="Important">
  <stage id="1: analysis_and_todo">
  <tools>
    <tool name="todo_write" description="Maintain execution todo list and statuses"/>
  </tools>
  - Read all steps and provided inputs; derive a task-level todo list
  - Inventory architecture sources; note gaps and assumptions
  - Plan target document sections according to the template
  - Deliverable: Task-level todo list and source inventory
  </stage>

  <stage id="2: author_architecture_documents">
  <tools>
    <tool name = "todo_write" description="Maintain execution todo list and statuses"/>
    <tool name = "sequential-thinking" description="Aggregate and normalize content; author documents per template"/>
  </tools>
  - Aggregate and normalize content; author documents per template
  - Validate completeness and internal consistency across sections
  - Prepare the JSON deliverable with files[] ready to write
  - Deliverable: files[] conforming to schema, ready to write
  <questions>
  - Are all required sections covered per template?
  - Do files trace back to their source_refs without fabrication?
  - Is each file path under docs/architecture/ and .md?
  </questions>
  </stage>

  <stage id="3: shard_and_finalize">
  <tools>
    <tool name = "todo_write" description="Maintain execution todo list and statuses"/>
  </tools>
  - Run sunnycore/scripts/shard-architecture.py and record shards_created
  - Validate output JSON against schema; fix violations before finalizing
  - Emit final JSON only; do not include explanations
  - Deliverable: Final JSON-only deliverable with shards_created recorded
  <checks>
  - [ ] Template architecture conforms to tasks decision tree (3 stages)
  - [ ] Output JSON passes schema; no additionalProperties
  - [ ] Every output item includes 'Format' and 'Example' lines in this prompt
  - [ ] All file paths under docs/architecture/ with .md extension
  - [ ] Source references present for every file
  </checks>
  </stage>
</workflow>

<example>
{
  "files": [
    {
      "path": "docs/architecture/overview.md",
      "title": "System Overview",
      "content": "# Overview\nThis document provides the high-level system architecture.",
      "source_refs": [
        { "file": "docs/architecture/architecture.md", "lines": "12-45" }
      ],
      "format": "markdown"
    }
  ],
  "shards_created": 0
}
</example>
