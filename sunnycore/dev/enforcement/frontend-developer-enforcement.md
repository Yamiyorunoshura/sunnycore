# Frontend Developer Enforcement Standards

<core_execution_protocol>
## Core Execution Protocol

<prerequisite_conditions>
### Mandatory Prerequisites (Relaxed)
- **Recommendation**: Load unified workflow and implementation plans before starting; if missing, record in dev_notes.validation_warnings and continue
- **Workflow Reading**: Should read `{project_root}/sunnycore/dev/workflow/frontend-developer-workflow.md`, record warning if failed
- **Plan Verification**: Attempt to locate and read the implementation plan for task_id; if missing, record warning and continue with minimal context
<!-- prerequisite_conditions>

<scope_compliance -->
### Scope Compliance (Relaxed Recording)
- **Scope Boundaries**: Should maintain within `scope.in_scope`; record warnings with reasons/remedies when deviating
- **Violation Handling**: Do not interrupt process, record in dev_notes.validation_warnings and challenges_and_deviations
- **Change Protocol**: Register decisions first, then supplement formal appendices
<!-- scope_compliance>

<workflow_compliance -->
### Workflow Compliance
- **Stage Integrity**: Never skip workflow stages, execute all stages in sequential order
- **Specialization Requirements**: Must execute specialized actions defined in developer_specializations.frontend
<!-- workflow_compliance>


<frontend_specialization_requirements>
## Frontend Specialization Mandatory Requirements

<ux_usability>
### UX and Usability (Mandatory Execution)
- **UI-IDs Extraction**: Must extract all UI-IDs from the implementation plan
- **Design Assets Verification**: Must verify and apply all design assets
- **User Experience**: Must ensure all interactions conform to expected user flows
<!-- ux_usability>

<routing_state_management -->
### Routing and State Management (Mandatory Implementation)
- **Route Definition**: Must define clear routing structure
- **State Enumeration**: Must enumerate all application states
- **Global State**: Must identify and properly manage global state
- **State Consistency**: Ensure predictability of state changes
<!-- routing_state_management>

<component_architecture -->
### Component Architecture (Mandatory Standards)
- **Component Skeleton**: Must create clear component skeleton
- **Type Definitions**: Must define all types and interfaces
- **Component Contracts**: Must clearly define contracts between components
- **Separation of Concerns**: Must implement appropriate separation of concerns
<!-- component_architecture>

<styling_theming -->
### Styling and Theming (Mandatory Requirements)
- **Design Tokens**: Must apply consistent design tokens
- **Theme System**: Must implement extensible theme system
- **Responsive Design**: Must ensure adaptability across all device sizes
<!-- styling_theming>


<accessibility_requirements>
## Accessibility Requirements (Mandatory but Non-Disruptive)

<mandatory_accessibility_standards>
- **A11Y Compliance**: Should avoid accessibility barriers; if not met, record risks and remediation plans
- **Color Contrast**: Must comply with WCAG color contrast requirements
- **Focus Management**: Must implement appropriate focus management
- **ARIA Labels**: Must add appropriate ARIA labels
- **Keyboard Navigation**: Must support complete keyboard navigation
- **Screen Reader**: Must ensure screen reader compatibility
<!-- mandatory_accessibility_standards>


<performance_requirements>
## Performance Requirements (Mandatory Achievement)

<performance_metrics>
- **Bundle Size**: Must comply with specified bundle size limits
- **LCP (Largest Contentful Paint)**: Must achieve performance targets
- **INP (Interaction to Next Paint)**: Must meet interaction response requirements
- **TTI (Time to Interactive)**: Must achieve time-to-interactive targets
- **Resource Optimization**: Must implement image and resource optimization
<!-- performance_metrics>


<testing_requirements>
## Testing Requirements (Mandatory Execution)

<test_driven_development>
- **Test-First Approach**: Must write tests before implementation
- **Test Types**:
  - Unit Tests: Aligned with UI-IDs
  - E2E Tests: Test complete user flows
  - Accessibility Tests: Ensure A11Y compliance
- **Coverage Threshold**: Must meet specified test coverage requirements
<!-- test_driven_development>


<architectural_principles>
## Architecture Principles (Mandatory Compliance)

<design_principles>
- **Component-Based Design**: Must apply component-based design
- **SOLID Principles**: Must apply SOLID design principles
- **KISS Principle**: Keep interfaces simple and easy to use
- **DRY Principle**: Avoid duplicate UI logic
<!-- design_principles>


<compatibility_requirements>
## Compatibility Requirements (Mandatory Assurance)

<cross_platform_compatibility>
- **Browser Compatibility**: Must work properly in specified browser versions
- **Device Compatibility**: Must display properly across various device sizes
- **Backward Compatibility**: Must maintain existing interface contracts
<!-- cross_platform_compatibility>


<internationalization>
## Internationalization and Localization (Mandatory Implementation)

<i18n_support>
- **i18n Support**: Must implement internationalization architecture
- **Text Externalization**: All display text must be externalized
- **Cultural Adaptation**: Must consider different cultural usage patterns
<!-- i18n_support>


<documentation_traceability>
## Documentation and Traceability

<documentation_requirements>
- **Component Documentation**: Must update Storybook or component documentation
- **Usage Examples**: Must provide component usage examples
- **Traceability**: Must reference task_id in PRs, commits, and code comments
- **Constraint Recording**: Must document all component constraints and limitations
<!-- documentation_requirements>


<dev_notes_requirements>
## DEV_NOTES Documentation Requirements (🚨 Mandatory Recording but Non-Disruptive 🚨)

<mandatory_documentation>
- **handover_docs Stage Execution**: Must execute complete handover_docs stage after development completion
- **detailed_changes Recording**: Must document all implementation changes in detail within dev_notes
- **UI-IDs Mapping**: Mapping gaps do not interrupt; record gap list with provisional mappings/reasons
- **Component Decision Recording**: Must document component design decisions, state management strategies, and interaction design choices
- **Accessibility Implementation Recording**: Must document implemented accessibility features and validation results
- **Performance Optimization Recording**: Must document performance optimization measures and test results
- **Design Assets Usage**: Must document used design assets and reasons for any design deviations
- **Browser Compatibility**: Must document tested browser versions and discovered compatibility issues
- **Documentation Quality Requirements**: dev_notes cannot be omitted or superficial, must provide sufficient detail for future maintenance reference
<!-- mandatory_documentation>


<markdown_conversion>
## Markdown Format Conversion (Absolute Mandatory)

<conversion_rules>
- **YAML to Markdown**: Must completely convert `{project_root}/sunnycore/dev/templates/dev-notes-tmpl.yaml` structure to standard Markdown format
- **Heading Levels**: YAML sections convert to corresponding Markdown headings (# ## ### #### ##### ######)
- **List Format**: YAML arrays convert to Markdown lists (- or 1. format)
- **Code Blocks**: Code snippets use standard Markdown code blocks (```language)
- **Table Format**: Structured data uses Markdown table format | Field | Value |
- **Link Format**: Use standard Markdown link format [text](URL)
- **Block Quotes**: Important notes use > quote format
- **Emphasis Markers**: Use **bold** and *italic* to appropriately emphasize key content
- **Component Specifications**: Component API, style definitions, interaction specifications use appropriate code block markers
<!-- conversion_rules>


<output_configuration>
## Output Configuration (Fixed)

<file_paths>
- **Development Records**: `{{project_root}}/docs/dev-notes/{{task_id}`(e.g. `1`, `2`, `3`...)}-dev-notes.md`
- **Template Reference**: `{project_root}/sunnycore/dev/templates/dev-notes-tmpl.yaml`
<!-- file_paths>


<quality_gates>
## Quality Gates (Mandatory Passage)

<quality_standards>
- **Static Analysis**: Code must pass ESLint and other static analysis checks
- **Type Checking**: Must pass TypeScript type checking
- **Performance Audit**: Must pass Lighthouse performance audit
- **Accessibility Audit**: Must pass accessibility checks
<!-- quality_standards>


<accessibility_checklist>
## Accessibility Checklist (Mandatory Execution)

<a11y_verification>
- [ ] All interactive elements are keyboard accessible
- [ ] All images have appropriate alt text
- [ ] Color contrast meets WCAG AA standards
- [ ] Forms have appropriate labels and error handling
- [ ] Dynamic content changes have appropriate notifications
- [ ] Screen readers can correctly interpret all content
<!-- a11y_verification>


<performance_checklist>
## Performance Checklist (Mandatory Execution)

<performance_verification>
- [ ] Images are optimized and lazy-loaded
- [ ] Code splitting is implemented
- [ ] Unnecessary re-renders have been eliminated
- [ ] Third-party resource loading is optimized
- [ ] Critical rendering path is optimized
<!-- performance_verification>


<failure_handling>
## Failure Handling Protocol (Record and Continue)

<error_handling_protocol>
- **Plan Missing**: Record warnings and alternative information sources; continue
- **Scope Deviation**: Record deviations/impacts/remediation plans; do not interrupt
- **A11Y Not Met**: Record risks and remediation timeline; do not interrupt
- **Performance Not Met**: Record measurements/optimization plans; continue under controlled risk
- **Design Inconsistency**: Record differences and alignment plans; do not interrupt
<!-- error_handling_protocol>
