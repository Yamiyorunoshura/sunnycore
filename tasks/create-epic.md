**GOAL**: Create feature-level task list breaking down requirements into executable tasks.

## [Context]
**You must read the following context:**
- `{REQ}/*.md`(Only the related documents) - Requirements documents
- `{ARCH}/*.md`(Only the related documents) - Architecture documents
- `{TMPL}/epic-tmpl.yaml` - Epic output format template

## [Products]
- `{EPIC}` - Feature-level task list with full requirement-architecture traceability

## [Constraints]
- **MUST** create feature-level tasks, **MUST NOT** go below feature granularity
- **MUST** focus on deliverables, **MUST NOT** include operational actions unless requested
- **MUST** use kebab-case, **MUST NOT** use spaces in file names
- **MUST** achieve 100% requirement coverage (every REQ-XXX and NFR-XXX mapped to tasks)
- **MUST** map tasks to architecture components from Components section

## [Instructions]
1. **Step 1: Parse Source Material**
- **GOAL:** Assemble the complete requirements and architecture inputs needed for epic planning.
- **STEPS:**
  - Identify relevant `{REQ}/*.md` files and list every REQ-XXX and NFR-XXX with their titles and acceptance criteria tags.
  - Review related `{ARCH}/*.md` sections to capture Components, Technical Stack selections, and component status (New/Modified/Existing).
  - Extract the Requirements Traceability Matrix rows that link requirements to architecture elements.
  - Record component responsibilities, interfaces, and dependencies that influence sequencing.
- **QUESTIONS:**
  - Have all referenced REQ-XXX and NFR-XXX been captured with sufficient context for task creation?
  - Which architecture components correspond to each requirement in the traceability matrix?
  - What dependencies or technology constraints are specified for each component?
- **CHECKLIST:**
  - [ ] Complete inventory of applicable REQ-XXX and NFR-XXX captured.
  - [ ] Component details, technical stack notes, and status recorded.
  - [ ] Traceability Matrix mappings extracted for later use.
  - [ ] Component responsibilities, interfaces, and dependencies documented.

2. **Step 2: Select Feature Candidates**
- **GOAL:** Translate architecture components into feature-level deliverables that align with requirements.
- **STEPS:**
  - Prioritize components marked New or Modified, or referenced directly by requirements or traceability notes.
  - Confirm requirement-to-component mappings using the extracted matrix and capture multi-component relationships.
  - Evaluate infrastructure or cross-cutting elements to decide whether they require discrete feature tasks.
  - Adjust candidate scope by splitting oversized components or merging undersized ones to stay within a 1-3 day effort.
- **QUESTIONS:**
  - Does each component candidate have clear requirement coverage?
  - Are any components missing requirements or marked Existing but still needed for fulfillment?
  - Which infrastructure or NFR-driven elements warrant their own tasks?
- **CHECKLIST:**
  - [ ] Every candidate maps to at least one requirement or justified NFR.
  - [ ] Components without coverage flagged for follow-up.
  - [ ] Oversized or undersized candidates normalized to feature-level scope.
  - [ ] Infrastructure and cross-cutting needs evaluated for inclusion.

3. **Step 3: Draft Feature-Level Tasks**
- **GOAL:** Create task entries that reflect deliverable features with traceability to requirements and architecture.
- **STEPS:**
  - Name each task using `verb-noun` kebab-case with ≤14 characters (e.g., `implement-auth`).
  - Write concise descriptions referencing component responsibilities and relevant technology choices.
  - Attach requirement IDs and architecture components to each task using the traceability data.
  - Estimate duration at 1-3 focused workdays and note any preliminary dependencies observed.
- **QUESTIONS:**
  - Does each task remain at feature granularity rather than sub-feature or multi-feature scale?
  - Are requirement and architecture references explicit enough for reviewers to verify traceability?
  - Do task descriptions communicate the feature’s value and scope without detailing implementation minutiae?
- **CHECKLIST:**
  - [ ] Tasks follow `verb-noun` kebab-case naming ≤14 characters.
  - [ ] Each task lists mapped REQ-XXX/NFR-XXX and architecture components.
  - [ ] Descriptions capture feature intent and primary technology context.
  - [ ] Estimated durations fall within the 1-3 day guideline.

4. **Step 4: Validate Coverage and Dependencies**
- **GOAL:** Ensure comprehensive requirement coverage and accurate sequencing across the task list.
- **STEPS:**
  - Build a coverage table linking each requirement and NFR to the corresponding tasks and components.
  - Confirm every task references at least one requirement and resolve or justify any orphan items.
  - Translate component dependencies into explicit task dependencies and identify critical paths.
  - Review NFR handling to confirm whether they are satisfied by tasks or architectural decisions.
- **QUESTIONS:**
  - Which requirements or NFRs remain unmapped or insufficiently addressed?
  - Do any task dependencies conflict or create circular relationships?
  - Where can work proceed in parallel without violating dependency rules?
- **CHECKLIST:**
  - [ ] Coverage table shows 100% of REQ-XXX linked to tasks.
  - [ ] NFR-XXX either mapped to tasks or documented as architecture-covered.
  - [ ] Task dependencies mirror component relationships without cycles.
  - [ ] No orphan requirements or tasks remain.

5. **Step 5: Finalize Epic Output**
- **GOAL:** Package the epic in template format with quality gates ready for stakeholder review.
- **STEPS:**
  - Populate `{EPIC}` using `epic-tmpl.yaml`, numbering tasks sequentially and preserving required fields.
  - Document the dependency graph/table and note parallel execution opportunities or independence.
  - Apply quality gates derived from acceptance criteria, component interfaces, relevant NFR targets, and testing standards (e.g., unit coverage ≥80%, integration checks passing).
  - Review constraints, naming rules, and save the finalized epic for approval.
- **QUESTIONS:**
  - Does the epic structure match the template expectations for tasks, dependencies, and notes?
  - Are all quality gates actionable and traceable back to the source documents?
  - Have naming, coverage, and constraint rules been satisfied before presenting for approval?
- **CHECKLIST:**
  - [ ] `{EPIC}` file contains sequentially numbered feature-level tasks.
  - [ ] Dependency section updated or explicitly states independence.
  - [ ] Quality gates per task reflect acceptance criteria, interfaces, testing, and performance thresholds.
  - [ ] Epic saved and ready for stakeholder approval.

## [Quality-Gates]
All gates **MUST** pass before marking complete:
- [ ] Epic at "{EPIC}" with feature-level, outcome-oriented tasks mapped to requirements
- [ ] 100% requirement coverage
- [ ] kebab-case file names