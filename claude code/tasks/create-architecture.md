<input>
  <context>
  1. {root}/docs/requirements/*.md - Authoritative project requirements
  2. {root}/sunnycore/scripts/shard-architecture.py - Architecture sharding script
  </context>
  <templates>
  1. {root}/sunnycore/templates/architecture-tmpl.yaml - Canonical architecture template
  </templates>
</input>

<output>
1. {root}/docs/architecture/*.md - Comprehensive architecture corpus
</output>

<constraints importance="Critical">
- MUST verify that {root}/docs/requirements/*.md exists and is complete before starting architecture design.
- MUST create explicit requirement-to-architecture mapping to ensure full coverage of functional and non-functional requirements.
- MUST validate that every requirement has corresponding architectural component or design decision.
- Author the draft with the architecture template into {root}/docs/architecture.md; comprehensively cover components, boundaries, data flows, risks, and decisions; strictly preserve section ordering.
- Post-draft, execute the sharding script: '{root}/sunnycore/scripts/shard-architecture.py'; verify materialized files under {root}/docs/architecture/.
- Use clear, concise English and 2-space indentation; refrain from introducing non-existent paths or files.
</constraints>

<workflow importance="Critical">
  <stage id="1: requirement-analysis">
  <tools>
  - read_file: Load and analyze all requirements documents
  - Sequential Thinking Tool: Decompose complex requirements and identify architectural patterns
  - grep: Search for requirement patterns and cross-references
  </tools>
  - Verify completeness and consistency of all requirements under {root}/docs/requirements/*.md.
  - Analyze functional requirements to identify core system components and their responsibilities.
  - Extract non-functional requirements (performance, security, reliability) and translate to architectural constraints.
  - Create explicit mapping matrix: Requirement ID → Architectural Component/Decision.
  - Identify requirement gaps or conflicts that must be resolved before proceeding.

  <questions>
  - Are all functional requirements mapped to specific architectural components?
  - Do non-functional requirements translate to measurable architectural constraints?
  - Are there conflicting requirements that need architectural trade-off decisions?
  - Which external dependencies and integration points are mandated by requirements?
  </questions>
  </stage>

  <stage id="2: architecture-design">
  <tools>
  - Sequential Thinking Tool: Architect system components and validate design decisions
  - Context7 Integration: Fetch external package and architectural pattern references
  </tools>
  - Based on requirement analysis, delineate system components, boundaries, and canonical data flows.
  - Design macro-architecture ensuring every requirement has corresponding architectural element.
  - Define component interaction contracts and data flow patterns.
  - Document architectural decisions with requirement traceability.
  - Address cross-cutting concerns (security, observability, performance) as mandated by non-functional requirements.

  <questions>
  - Does the proposed architecture address all identified requirements?
  - Are architectural decisions traceable back to specific requirements?
  - How will non-functional requirements be validated in this architecture?
  </questions>
  </stage>

  <stage id="3: author">
  <tools>
  - read_file: Load architecture template
  - write: Generate architecture.md document
  - run_terminal_cmd: Execute sharding script to partition document
  </tools>
  - Leverage the architecture template to draft markdown formatted {root}/docs/architecture.md.
  - Include requirement traceability matrix in architecture document.
  - Ensure sections comprehensively cover components, interactions, data flows, risks, and decisions with explicit requirement references.
  - Validate that every requirement from the mapping matrix is addressed in the architecture.
  - Execute the sharding script to partition the document: uv run '{root}/sunnycore/scripts/shard-architecture.py'
  - Verify artifacts appear under {root}/docs/architecture/.
  </stage>

  <stage id="4: finalize">
  <tools>
  - read_file: Cross-validate against requirements documents
  - list_dir: Verify sharded files were generated correctly
  </tools>
  - Cross-validate architecture against all requirements using the mapping matrix.
  - Verify that every functional and non-functional requirement is addressed.
  - Remediate typographical errors and normalize terminology.
  - Confirm architectural decisions are justified by requirements.
  
  <checks>
  - [ ] {root}/docs/architecture.md exists and adheres to the template
  - [ ] All requirements from {root}/docs/requirements/*.md are mapped to architectural elements
  - [ ] Requirement traceability matrix is complete and accurate
  - [ ] Non-functional requirements translate to measurable architectural constraints
  - [ ] Sharded files are generated under {root}/docs/architecture/
  - [ ] Section order and headings exactly match the template
  - [ ] Paths and commands are valid within this repository
  - [ ] Language is clear, concise, and free of typographical errors
  </checks>
  </stage>
</workflow>

