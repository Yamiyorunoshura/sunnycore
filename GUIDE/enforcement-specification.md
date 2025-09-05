# Prompt Engineering Enforcement Specification

<specification_metadata>
name: "Prompt Engineering Enforcement Specification"
version: "2.0.0"
category: "prompt_engineering_standard"
locale: "en"
status: "stable"
last_updated: "2025-01-18"
maintainer: "AI Development Team"
compliance_level: "mandatory"
</specification_metadata>

## 1. Document Overview

### 1.1 Purpose and Scope

This specification defines the standardized enforcement framework for prompt engineering in AI-driven development workflows. It establishes mandatory requirements for:

- **Structured Output Generation**: XML-based structured reasoning and human-readable Markdown conversion
- **Reasoning Framework Integration**: Chain-of-Thought and SELF-DISCOVER methodology implementation
- **Evidence-Based Validation**: Traceable citations and reproducible results
- **Deterministic Execution**: Consistent and reliable prompt processing
- **Quality Assurance**: Multi-stage validation and compliance checking

### 1.2 Target Audience

- AI prompt engineers and developers
- Workflow orchestrators and automation systems
- Quality assurance and compliance teams
- Development operations teams

### 1.3 Related Standards

- ISO/IEC 27001 (Information Security Management)
- IEEE 2857 (Privacy Engineering)
- NIST AI Risk Management Framework
- W3C XML Standards

## 2. Core Framework

### 2.1 Design Principles

#### 2.1.1 Structured Reasoning
All complex analysis must be expressed through structured, machine-verifiable formats using standardized XML schemas while maintaining human readability through Markdown conversion.

#### 2.1.2 Evidence-Based Validation
Every assertion, finding, or recommendation must be supported by concrete, traceable evidence including file paths, line ranges, metrics, or external references.

#### 2.1.3 Deterministic Reproducibility
Execution must be deterministic and reproducible across different environments, using fixed parameters and stable ordering mechanisms.

#### 2.1.4 Fail-Safe Operation
Implementation must include comprehensive error handling, fast-stop mechanisms, and minimal viable output generation for critical failures.

### 2.2 Key Concepts

#### 2.2.1 Enforcement Stage
A discrete execution unit with defined inputs, processing rules, outputs, and quality gates.

#### 2.2.2 Quality Gate
A validation checkpoint that must be passed before proceeding to the next stage, with defined criteria and failure actions.

#### 2.2.3 Evidence Citation
A traceable reference to source material that supports a finding or assertion, including location and verification metadata.

#### 2.2.4 Fast-Stop Trigger
An emergency mechanism that immediately halts processing when critical conditions are not met, generating minimal viable output.

## 3. Technical Specifications

### 3.1 XML Schema Registry

The following XML tags constitute the standardized schema for structured outputs:

#### 3.1.1 Core Structure Tags

```xml
<!-- Document Metadata -->
<metadata>
  <name>{specification_name}</name>
  <version>{semantic_version}</version>
  <category>{classification}</category>
  <task_id>{unique_identifier}</task_id>
  <timestamp>{iso8601_datetime}</timestamp>
</metadata>

<!-- Prerequisites Management -->
<prerequisites>
  <file path="{file_path}" required="{true|false|recommended}">
    <failure_action>{emergency_stop|record_warning_continue|minimal_viable_output}</failure_action>
  </file>
</prerequisites>

<!-- Execution Configuration -->
<determinism temperature="{float}" top_p="{float}" top_k="{integer}" seed="{integer}" stable_sort="{boolean}"/>
```

#### 3.1.2 Workflow Definition Tags

```xml
<!-- Workflow Structure -->
<workflow>
  <stage id="{stage_id}" name="{stage_name}" optional="{boolean}" parallel="{allowed|forbidden}">
    <inputs>
      <source path="{source_path}" required="{boolean}"/>
    </inputs>
    <actions>
      <self_discover>
        <select>{selection_methodology}</select>
        <adapt>{adaptation_strategy}</adapt>
        <implement>{implementation_plan}</implement>
        <apply>{application_approach}</apply>
      </self_discover>
    </actions>
    <outputs>
      <evidence path="{evidence_path}" start_line="{integer}" end_line="{integer}" sha256="{hash}"/>
    </outputs>
    <quality_gates>
      <gate name="{gate_name}">
        <criteria>{validation_criteria}</criteria>
        <threshold>{success_threshold}</threshold>
        <failure_action>{action_on_failure}</failure_action>
      </gate>
    </quality_gates>
  </stage>
</workflow>
```

#### 3.1.3 Analysis and Output Tags

```xml
<!-- Reasoning Framework -->
<reasoning>
  <analysis>{decomposed_analysis}</analysis>
  <findings>{key_discoveries}</findings>
  <decisions>{decision_rationale}</decisions>
  <rationale>{supporting_logic}</rationale>
  <validation>{verification_method}</validation>
</reasoning>

<!-- Evidence System -->
<evidence path="{file_path}" start_line="{integer}" end_line="{integer}" sha256="{hash}">
  <description>{evidence_description}</description>
  <relevance>{relevance_explanation}</relevance>
</evidence>

<!-- Output Structure -->
<output>
  <report>
    <summary>{executive_summary}</summary>
    <details>{detailed_findings}</details>
    <checklist>
      <item checked="{boolean}">{checklist_item}</item>
    </checklist>
  </report>
</output>
```

#### 3.1.4 Safety and Security Tags

```xml
<!-- Fast-Stop Mechanism -->
<fast_stop_mechanism>
  <trigger_conditions>
    <condition type="{condition_type}">
      <description>{condition_description}</description>
      <action>{immediate_action}</action>
    </condition>
  </trigger_conditions>
  <minimal_viable_output>
    <status>{emergency_status}</status>
    <partial_results>{available_results}</partial_results>
  </minimal_viable_output>
</fast_stop_mechanism>

<!-- Security Controls -->
<security>
  <read_only_paths>
    <path>{protected_path}</path>
  </read_only_paths>
  <sensitive_filters>
    <filter pattern="{regex_pattern}" action="{filter_action}"/>
  </sensitive_filters>
  <access_control>
    <permission level="{access_level}" scope="{access_scope}"/>
  </access_control>
</security>
```

### 3.2 Execution Model

#### 3.2.1 Deterministic Processing Requirements

- **Temperature**: Must be set to 0 for reproducible outputs
- **Top-p**: Must be set to 0 to disable nucleus sampling
- **Top-k**: Must be set to 1 for deterministic token selection
- **Seed**: Must be explicitly set and documented
- **Stable Sorting**: All list outputs must use lexicographic ordering

#### 3.2.2 Parallel Execution Rules

- **Intra-stage Parallelism**: Allowed for read-only operations within the same stage
- **Cross-stage Dependencies**: Must be preserved in sequential order
- **Resource Isolation**: Parallel operations must not interfere with each other
- **Error Propagation**: Failures in parallel operations must be properly aggregated

#### 3.2.3 Caching Strategy

- **Content-based Hashing**: Use SHA-256 for content verification
- **Invalidation Triggers**: File modification time and content hash changes
- **Cache Scope**: Limited to read-only operations and idempotent analyses
- **Cache Location**: Temporary directory with automatic cleanup

## 4. Implementation Guide

### 4.1 Stage-by-Stage Implementation

#### 4.1.1 Prerequisites Validation
1. Load required workflow files and templates
2. Validate file accessibility and permissions
3. Record warnings for missing non-critical resources
4. Trigger emergency stop for missing critical dependencies

#### 4.1.2 Deterministic Configuration
1. Apply required decoding parameters
2. Initialize random seed for reproducibility
3. Configure stable sorting mechanisms
4. Validate configuration consistency

#### 4.1.3 Workflow Execution
1. Process stages in defined sequence
2. Execute quality gates at each checkpoint
3. Collect and validate evidence citations
4. Generate structured outputs using XML schema

#### 4.1.4 Output Processing
1. Convert XML structures to human-readable Markdown
2. Clean placeholder content and invalid references
3. Apply security filters and access controls
4. Generate final deliverables

### 4.2 Markdown Conversion Rules

#### 4.2.1 Structure Mapping
- **YAML Sections** → Markdown headers (`#` to `######`)
- **Arrays** → Unordered lists (`-`) or ordered lists (`1.`)
- **Code Blocks** → Fenced code blocks with language specification
- **Tables** → Markdown table format (`| Column | Value |`)
- **Links** → Standard Markdown links (`[text](URL)`)

#### 4.2.2 Content Cleanup
- Remove all placeholder content (e.g., `{{placeholder}}`, `TBD`, `N/A`)
- Convert XML entities to Unicode characters
- Normalize whitespace and line endings
- Validate Markdown syntax compliance

## 5. Compliance Requirements

### 5.1 Mandatory Quality Gates

#### 5.1.1 Gate 1: Prerequisites Validation
- **Criteria**: All required resources accessible
- **Threshold**: 100% success rate
- **Failure Action**: Emergency stop with diagnostic report

#### 5.1.2 Gate 2: Evidence Completeness
- **Criteria**: All findings supported by evidence citations
- **Threshold**: 100% coverage
- **Failure Action**: Continue with warnings, require manual review

#### 5.1.3 Gate 3: Structural Compliance
- **Criteria**: XML output conforms to registered schema
- **Threshold**: ≥95% compliance score
- **Failure Action**: Require correction before proceeding

#### 5.1.4 Gate 4: Security Validation
- **Criteria**: No security violations detected
- **Threshold**: 100% compliance
- **Failure Action**: Emergency stop with security alert

### 5.2 Security Compliance

#### 5.2.1 Access Control
- Enforce read-only access to specification directories
- Implement role-based permissions for sensitive operations
- Log all access attempts and permission changes
- Validate user credentials before processing

#### 5.2.2 Data Protection
- Filter sensitive information from outputs
- Encrypt data in transit and at rest
- Implement secure deletion for temporary files
- Comply with relevant privacy regulations

## 6. Appendices

### 6.1 Example Implementation

```xml
<prompt_enforcement>
  <metadata>
    <name>Code Review Enforcement</name>
    <version>2.0.0</version>
    <category>quality_assurance</category>
    <task_id>CR-2025-001</task_id>
    <timestamp>2025-01-18T10:30:00Z</timestamp>
  </metadata>

  <prerequisites>
    <file path="sunnycore/qa/workflow/unified-review-workflow.md" required="recommended">
      <failure_action>record_warning_continue</failure_action>
    </file>
    <file path="sunnycore/qa/templates/review-tmpl.yaml" required="true">
      <failure_action>emergency_stop</failure_action>
    </file>
  </prerequisites>

  <determinism temperature="0" top_p="0" top_k="1" seed="42" stable_sort="true"/>

  <workflow>
    <stage id="S1" name="code_analysis" parallel="allowed">
      <inputs>
        <source path="src/**/*.js" required="true"/>
      </inputs>
      <actions>
        <self_discover>
          <select>Static analysis and pattern detection</select>
          <adapt>Apply project-specific coding standards</adapt>
          <implement>Execute automated review checks</implement>
          <apply>Generate findings with recommendations</apply>
        </self_discover>
      </actions>
      <outputs>
        <evidence path="src/components/UserAuth.js" start_line="15" end_line="25" sha256="abc123..."/>
      </outputs>
      <quality_gates>
        <gate name="syntax_validation">
          <criteria>No syntax errors detected</criteria>
          <threshold>100%</threshold>
          <failure_action>emergency_stop</failure_action>
        </gate>
      </quality_gates>
    </stage>
  </workflow>

  <reasoning>
    <analysis>Code structure and quality patterns evaluated</analysis>
    <findings>3 security vulnerabilities identified</findings>
    <decisions>Prioritize authentication fixes</decisions>
    <rationale>Security vulnerabilities pose immediate risk</rationale>
    <validation>Cross-referenced with OWASP guidelines</validation>
  </reasoning>

  <output>
    <report>
      <summary>Code review completed with 3 critical findings</summary>
      <details>Security vulnerabilities in authentication module require immediate attention.</details>
      <checklist>
        <item checked="true">All source files analyzed</item>
        <item checked="true">Security patterns validated</item>
        <item checked="false">Performance benchmarks completed</item>
      </checklist>
    </report>
  </output>

  <fast_stop_mechanism>
    <trigger_conditions>
      <condition type="missing_critical_file">
        <description>Required review template not found</description>
        <action>immediate_stop</action>
      </condition>
    </trigger_conditions>
    <minimal_viable_output>
      <status>EMERGENCY_STOP</status>
      <partial_results>Basic syntax validation completed</partial_results>
    </minimal_viable_output>
  </fast_stop_mechanism>
</prompt_enforcement>
```

### 6.2 Glossary

- **Deterministic Execution**: Processing that produces identical outputs given identical inputs
- **Evidence Citation**: A traceable reference to source material supporting a finding
- **Fast-Stop Mechanism**: Emergency halt procedure for critical failures
- **Quality Gate**: Validation checkpoint with pass/fail criteria
- **Self-Discover**: Reasoning framework: SELECT, ADAPT, IMPLEMENT, APPLY
- **Stable Sorting**: Consistent ordering algorithm producing reproducible results

### 6.3 References

- W3C XML Schema Definition Language: https://www.w3.org/XML/Schema
- ISO/IEC 27001:2022 Information Security Management
- NIST AI Risk Management Framework 1.0
- IEEE 2857-2021 Privacy Engineering
- OWASP Application Security Verification Standard

### 6.4 Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2025-01-18 | Complete restructure with enhanced compliance framework |
| 1.0.0 | 2024-12-01 | Initial specification release |

---

*This specification is maintained by the AI Development Team and is subject to regular review and updates. For questions or suggestions, please contact the maintainer.*
