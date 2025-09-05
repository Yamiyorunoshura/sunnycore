# XML Agent System Specification v1.0

## Overview

This specification defines the XML structure and tagging conventions for multi-agent systems. The specification provides a standardized framework for defining agent roles, tasks, execution flows, and safety protocols using structured XML elements.

## 1. Root Element Structure

### 1.1 Primary Root Element

```xml
<prompt spec-version="1.0" profile="standard">
  <!-- Content -->
</prompt>
```

**Attributes:**
- `spec-version`: Specification version identifier (required)
- `profile`: Execution strictness level (required)
  - `light`: Basic task layer, I/O, and simple processes only
  - `standard`: Complete framework including task, context, process, safety, output, and quality layers
  - `strict`: Standard framework plus mandatory audit and commit requirements

## 2. Task Layer

The task layer defines the fundamental purpose and constraints of the agent system.

### 2.1 Role Definition

```xml
<role name="agent-identifier"/>
```

Defines the primary responsibility and function of the agent within the system.

### 2.2 Goal Statement

```xml
<goal>Primary objective description</goal>
```

Clear, concise statement of the main task or outcome to be achieved.

### 2.3 Constraints

```xml
<constraints>
  <item>Specific limitation or prohibition</item>
  <item>Additional constraint</item>
</constraints>
```

Explicit boundaries and restrictions governing agent behavior and actions.

### 2.4 Policies

```xml
<policies>
  <policy id="policy-identifier" version="1.0">Policy content and rules</policy>
</policies>
```

**Attributes:**
- `id`: Unique policy identifier
- `version`: Policy version for tracking updates

### 2.5 Metrics

```xml
<metrics>
  <metric type="performance-indicator" target="threshold-value"/>
</metrics>
```

**Attributes:**
- `type`: Metric category or measurement type
- `target`: Expected performance threshold or goal

## 3. Context Layer

The context layer provides environmental and operational context for agent execution.

### 3.1 Repository Mapping

```xml
<context>
  <repo-map>Repository structure or directory scope definition</repo-map>
</context>
```

Defines the file system or repository boundaries within which the agent operates.

### 3.2 File References

```xml
<files>
  <file path="relative/path/to/file">Additional metadata or description</file>
</files>
```

**Attributes:**
- `path`: Relative file path from repository root

### 3.3 Dependencies

```xml
<dependencies>
  Package, module, or external dependency specifications
</dependencies>
```

Lists required packages, libraries, or external systems needed for agent operation.

## 4. Tools Layer

The tools layer defines available capabilities and external interfaces.

### 4.1 Tool Definitions

```xml
<tools>
  <tool name="tool-identifier" kind="command|api|mcp">Tool description and usage</tool>
</tools>
```

**Attributes:**
- `name`: Unique tool identifier
- `kind`: Tool category
  - `command`: Command-line executable
  - `api`: External API interface
  - `mcp`: Model Context Protocol server

### 4.2 Command Specifications

```xml
<commands>
  <command name="command-name" bin="executable-path" timeout="seconds"/>
</commands>
```

**Attributes:**
- `name`: Command identifier
- `bin`: Executable binary path
- `timeout`: Maximum execution time in seconds

### 4.3 MCP Server Configuration

```xml
<mcp>
  <server id="server-identifier" capability="server-capabilities"/>
</mcp>
```

**Attributes:**
- `id`: Unique server identifier
- `capability`: Available server functions or protocols

## 5. Process Layer

The process layer defines execution workflow and validation procedures.

### 5.1 Execution Plan

```xml
<plan allow-reorder="true|false">
  <step id="step-identifier" type="read|analyze|test|report">Step description</step>
</plan>
```

**Attributes:**
- `allow-reorder`: Whether steps can be executed out of sequence
- `id`: Unique step identifier
- `type`: Step category for execution optimization

### 5.2 Validation Checklist

```xml
<validation_checklist>
  <item>Validation requirement or checkpoint</item>
</validation_checklist>
```

Defines quality assurance checkpoints to be verified during or after execution.

## 6. Safety Layer

The safety layer implements protective measures and error handling protocols.

### 6.1 Fast Stop Triggers

```xml
<fast_stop_triggers>
  <trigger id="trigger-identifier">
    <condition>Triggering condition description</condition>
    <action>immediate_stop</action>
    <output>Standardized error message</output>
  </trigger>
</fast_stop_triggers>
```

**Elements:**
- `condition`: Specific circumstance that activates the trigger
- `action`: Always `immediate_stop` for fast triggers
- `output`: Fixed error message to display

### 6.2 Emergency Stop Protocol

```xml
<emergency_stop>
  <fixed_message>Emergency Stop: Detailed stop reason</fixed_message>
  <reason_codes>TOOL_FAILURE|MISSING_REQUIRED_FILE|EMPTY_CONTENT|SECURITY_VIOLATION</reason_codes>
</emergency_stop>
```

**Reason Codes:**
- `TOOL_FAILURE`: External tool or command failure
- `MISSING_REQUIRED_FILE`: Required input file not found
- `EMPTY_CONTENT`: Critical content is empty or corrupted
- `SECURITY_VIOLATION`: Security policy breach detected

### 6.3 Guardrails

```xml
<guardrails>
  <rule id="rule-identifier">Behavioral restriction or safety requirement</rule>
</guardrails>
```

Defines ongoing behavioral constraints and safety boundaries for agent operations.

## 7. Input/Output Layer

The I/O layer specifies data sources and output formatting requirements.

### 7.1 Input Specifications

```xml
<inputs>
  <git_context>
    <message/>
    <changed_files/>
    <diff/>
    <branch/>
  </git_context>
  
  <cicd_report>
    <source_id/>
    <run_id/>
    <raw_logs/>
    <status/>
  </cicd_report>
</inputs>
```

**Git Context Elements:**
- `message`: Commit message or branch information
- `changed_files`: List of modified files
- `diff`: Code changes or differences
- `branch`: Target branch information

**CI/CD Report Elements:**
- `source_id`: Build system identifier
- `run_id`: Specific execution run identifier
- `raw_logs`: Build or test execution logs
- `status`: Current pipeline status

### 7.2 Output Specifications

```xml
<outputs>
  <final format="json|markdown" schema="schema-identifier"/>
  <output_location>target/file/path</output_location>
</outputs>
```

**Attributes:**
- `format`: Output data format
- `schema`: Reference to output structure definition

## 8. Reasoning and Output Layer

All agents must separate internal reasoning from final deliverables using structured processing blocks.

### 8.1 Core Processing Blocks

```xml
<analysis>Internal analysis and reasoning process</analysis>
<implementation>Actual execution or content generation</implementation>
<validation>Result verification and quality checks</validation>
```

### 8.2 Task-Specific Extensions

Depending on agent function, additional processing blocks may be used:

```xml
<classification>Document or content categorization results</classification>
<curation>Knowledge organization and structuring</curation>
<summary>Project or content summarization</summary>
<quality_assessment>Code review or quality evaluation</quality_assessment>
```

## 9. Testing and Quality Layer

### 9.1 Test Cases

```xml
<tests>
  <case id="test-identifier">
    <setup>Test environment preparation steps</setup>
    <asserts>Expected results and validation criteria</asserts>
  </case>
</tests>
```

### 9.2 Quality Metrics

```xml
<metrics>
  <metric type="schema-compliance" target="100%"/>
  <metric type="coverage" target=">=0.9"/>
  <metric type="performance" target="response-time-ms"/>
</metrics>
```

**Common Metric Types:**
- `schema-compliance`: Adherence to XML specification
- `coverage`: Test or requirement coverage percentage
- `performance`: Response time or processing speed thresholds

## 10. Collaboration Layer

### 10.1 Coordination Protocol

```xml
<coordination_protocol>
  <input_requirements>Required input specifications for multi-agent scenarios</input_requirements>
  <output_format>Standardized format for shared outputs</output_format>
</coordination_protocol>
```

### 10.2 Shared Output Location

```xml
<output_location>shared/output/directory/path</output_location>
```

Defines centralized location for outputs that need to be accessed by multiple agents.

## 11. Profile Implementation Guidelines

### 11.1 Light Profile
Minimal configuration suitable for simple, single-purpose agents:
- Task layer: role, goal, basic constraints
- I/O layer: inputs and outputs only
- Simple linear process flow

### 11.2 Standard Profile
Complete framework for production environments:
- All layers except audit requirements
- Full safety and validation protocols
- Comprehensive context and tool definitions

### 11.3 Strict Profile
Enhanced standard profile with mandatory audit trail:

```xml
<audit>Execution log, risk assessment, and compliance verification</audit>
<commit message="commit-description" branch="target-branch" signoff="true"/>
```

**Commit Attributes:**
- `message`: Descriptive commit message
- `branch`: Target repository branch
- `signoff`: Boolean indicating formal approval required

## 12. Implementation Example

### 12.1 Complete Standard Profile Example

```xml
<prompt spec-version="1.0" profile="standard">
  <role name="Commit Analysis Agent"/>
  <goal>Analyze git commits and CI/CD results to generate structured JSON reports</goal>

  <constraints>
    <item>Must not modify CI scripts or configuration files</item>
    <item>Output must conform to commit_report schema v1.0</item>
  </constraints>

  <context>
    <repo-map>Source code repository excluding vendor and build directories</repo-map>
    <dependencies>
      Git CLI, CI/CD system APIs, JSON schema validation library
    </dependencies>
  </context>

  <tools>
    <tool name="git" kind="command">Git version control operations</tool>
    <tool name="cicd_api" kind="api">CI/CD system data retrieval</tool>
  </tools>

  <plan>
    <step id="1" type="read">Extract git context and CI/CD data</step>
    <step id="2" type="analyze">Process changes and test results</step>
    <step id="3" type="report">Generate structured JSON output</step>
  </plan>

  <fast_stop_triggers>
    <trigger id="missing_commit">
      <condition>No git commit data available</condition>
      <action>immediate_stop</action>
      <output>Error: Missing required git commit information</output>
    </trigger>
  </fast_stop_triggers>

  <analysis>Internal reasoning and data processing</analysis>
  <implementation>JSON report generation</implementation>
  <validation>Schema compliance and data quality verification</validation>

  <outputs>
    <final format="json" schema="commit_report@1.0"/>
    <output_location>reports/commit/commit-analysis.json</output_location>
  </outputs>
</prompt>
```

## 13. Validation Requirements

### 13.1 Schema Compliance
All implementations must validate against the XML structure defined in this specification. Required elements must be present, and all attributes must use specified values.

### 13.2 Profile Consistency
Agents must implement all required elements for their specified profile level. Higher profiles (strict) include all elements from lower profiles (light, standard).

### 13.3 Output Format Validation
Final outputs must conform to declared schema specifications and be deliverable to specified locations.

## 14. Extension Guidelines

### 14.1 Custom Elements
Additional elements may be added within existing layer boundaries provided they do not conflict with core specification requirements.

### 14.2 Schema Evolution
Future specification versions should maintain backward compatibility with previous versions through the `spec-version` attribute.

---

**Specification Version:** 1.0  
**Last Updated:** September 2025  
**Scope:** Multi-agent XML structure and tagging conventions