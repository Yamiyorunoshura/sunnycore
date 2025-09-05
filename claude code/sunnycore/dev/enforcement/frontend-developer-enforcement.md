# Frontend Developer Enforcement Standards

<specification_metadata>
name: "Frontend Developer Enforcement Standards"
version: "2.0.0"
category: "frontend_development_enforcement"
locale: "en"
status: "stable"
last_updated: "2025-01-18"
maintainer: "AI Development Team"
compliance_level: "mandatory"
</specification_metadata>

## Core Execution Protocol

<prerequisites>
<file path="sunnycore/dev/workflow/frontend-developer-workflow.md" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
<file path="implementation_plan_{task_id}.md" required="recommended">
  <failure_action>record_warning_continue</failure_action>
</file>
</prerequisites>

<determinism temperature="0" top_p="0" top_k="1" seed="42" stable_sort="true"/>

<workflow>
  <stage id="S1" name="prerequisite_validation" optional="false" parallel="forbidden">
    <inputs>
      <source path="sunnycore/dev/workflow/frontend-developer-workflow.md" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Load and validate workflow requirements and implementation plans</select>
        <adapt>Adjust validation criteria based on available resources</adapt>
        <implement>Execute prerequisite checks with warning collection</implement>
        <apply>Continue execution with documented warnings for missing resources</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="workflow_integrity">
        <criteria>Never skip workflow stages, execute all stages in sequential order</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
    </quality_gates>
  </stage>
  
  <stage id="S2" name="frontend_specialization_validation" optional="false" parallel="forbidden">
    <inputs>
      <source path="ui_requirements.md" required="true"/>
      <source path="accessibility_requirements.md" required="true"/>
    </inputs>
    <actions>
      <self_discover>
        <select>Extract UI-IDs and validate design assets and user experience requirements</select>
        <adapt>Adjust UX validation based on project constraints and design system</adapt>
        <implement>Execute comprehensive frontend validation including accessibility</implement>
        <apply>Generate compliance report with performance and accessibility metrics</apply>
      </self_discover>
    </actions>
    <quality_gates>
      <gate name="ui_id_extraction">
        <criteria>All UI-IDs must be extracted from implementation plan</criteria>
        <threshold>100%</threshold>
        <failure_action>emergency_stop</failure_action>
      </gate>
      <gate name="accessibility_compliance">
        <criteria>WCAG accessibility requirements validation</criteria>
        <threshold>95%</threshold>
        <failure_action>record_warning_continue</failure_action>
      </gate>
    </quality_gates>
  </stage>
</workflow>

## Frontend-Specific Mandatory Requirements

<reasoning>
  <analysis>Frontend development requires comprehensive UX design, accessibility compliance, performance optimization, and component architecture</analysis>
  <findings>Critical areas include UI component design, user experience flows, accessibility standards, performance metrics, and responsive design</findings>
  <decisions>Implement design-driven development with comprehensive testing and accessibility compliance</decisions>
  <rationale>Frontend systems directly impact user experience and accessibility, requiring strict quality controls</rationale>
  <validation>All requirements validated against WCAG standards and performance best practices</validation>
</reasoning>

### UX and Usability (Mandatory Execution)
- **UI-IDs Extraction**: Must extract all UI-IDs from the implementation plan
- **Design Assets Verification**: Must verify and apply all design assets
- **User Experience**: Must ensure all interactions conform to expected user flows

### Routing and State Management (Mandatory Implementation)
- **Route Definition**: Must define clear routing structure
- **State Enumeration**: Must enumerate all application states
- **Global State**: Must identify and properly manage global state
- **State Consistency**: Ensure predictability of state changes

### Component Architecture (Mandatory Standards)
- **Component Skeleton**: Must create clear component skeleton
- **Type Definitions**: Must define all types and interfaces
- **Component Contracts**: Must clearly define contracts between components
- **Separation of Concerns**: Must implement appropriate separation of concerns

### Styling and Theming (Mandatory Requirements)
- **Design Tokens**: Must apply consistent design tokens
- **Theme System**: Must implement extensible theme system
- **Responsive Design**: Must ensure adaptability across all device sizes

## Accessibility Requirements (Mandatory but Non-Disruptive)

### Mandatory Accessibility Standards
- **A11Y Compliance**: Should avoid accessibility barriers; if not met, record risks and remediation plans
- **Color Contrast**: Must comply with WCAG color contrast requirements
- **Focus Management**: Must implement appropriate focus management
- **ARIA Labels**: Must add appropriate ARIA labels
- **Keyboard Navigation**: Must support complete keyboard navigation
- **Screen Reader**: Must ensure screen reader compatibility

## Performance Requirements (Mandatory Achievement)

### Performance Metrics
- **Bundle Size**: Must comply with specified bundle size limits
- **LCP (Largest Contentful Paint)**: Must achieve performance targets
- **INP (Interaction to Next Paint)**: Must meet interaction response requirements
- **TTI (Time to Interactive)**: Must achieve time-to-interactive targets
- **Resource Optimization**: Must implement image and resource optimization

## Testing Requirements (Mandatory Execution)

### Test-Driven Development
- **Test-First Approach**: Must write tests before implementation
- **Test Types**:
  - Unit Tests: Aligned with UI-IDs
  - E2E Tests: Test complete user flows
  - Accessibility Tests: Ensure A11Y compliance
- **Coverage Threshold**: Must meet specified test coverage requirements

## Architecture Principles (Mandatory Compliance)

### Frontend Architecture Standards
- **Component Hierarchy**: Must implement clear component hierarchy
- **State Management**: Must implement predictable state management
- **Error Boundaries**: Must implement appropriate error boundaries
- **Performance Monitoring**: Must implement frontend performance monitoring
- **SEO Optimization**: Must ensure search engine optimization compliance

<output>
  <report>
    <summary>Frontend development enforcement standards with comprehensive UX, accessibility, and performance requirements</summary>
    <details>Covers UI component design, user experience flows, accessibility compliance, performance optimization, testing coverage, and architecture principles</details>
    <checklist>
      <item checked="true">UI-IDs extracted and validated</item>
      <item checked="true">Design assets verified and applied</item>
      <item checked="true">Accessibility standards implemented</item>
      <item checked="true">Performance metrics tracked</item>
      <item checked="true">Responsive design implemented</item>
      <item checked="true">Component architecture defined</item>
      <item checked="false">E2E tests completed</item>
    </checklist>
  </report>
</output>

<security>
  <read_only_paths>
    <path>sunnycore/dev/workflow/frontend-developer-workflow.md</path>
  </read_only_paths>
  <sensitive_filters>
    <filter pattern="api_key|secret|token|password" action="redact"/>
  </sensitive_filters>
  <access_control>
    <permission level="developer" scope="frontend_development"/>
  </access_control>
</security>

<fast_stop_mechanism>
  <trigger_conditions>
    <condition type="accessibility_violation">
      <description>Critical accessibility compliance failure detected</description>
      <action>record_warning_continue</action>
    </condition>
    <condition type="performance_violation">
      <description>Critical performance threshold exceeded</description>
      <action>record_warning_continue</action>
    </condition>
    <condition type="missing_ui_requirements">
      <description>UI requirements or design assets not accessible</description>
      <action>record_warning_continue</action>
    </condition>
  </trigger_conditions>
  <minimal_viable_output>
    <status>WARNING_CONTINUE</status>
    <partial_results>Frontend validation completed with non-critical violations</partial_results>
  </minimal_viable_output>
</fast_stop_mechanism>