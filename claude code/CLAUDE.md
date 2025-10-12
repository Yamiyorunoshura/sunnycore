# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# General guidelines

## GUIDANCE 1
**MUST** execute only explicitly defined commands and follow all steps, **MUST NOT** skip or simplify processes

## GUIDANCE 2
**MUST** proactively request clarification when instructions are unclear, **MUST NOT** make assumptions or guesses

## GUIDANCE 3
**MUST** read all required input files and context before executing tasks, **MUST NOT** proceed without complete information

## GUIDANCE 4
**MUST** handle conflicts by priority: CLAUDE.md > commands > tasks, **MUST NOT** ignore priority hierarchy

## GUIDANCE 5
**MUST** complete all todo items one-by-one and verify all DoD conditions, **MUST NOT** skip todo items or DoD verification

## GUIDANCE 6: Template Structure
**MUST** follow template section hierarchy to generate markdown headings (section → h1, nested section → h2, etc.), **MUST NOT** skip sections or break heading hierarchy

## GUIDANCE 7: Template Instructions
**MUST** read and follow instruction fields in templates as natural language guidance for generating content, **MUST NOT** treat instructions as content to copy verbatim

## GUIDANCE 8: Repeatable Sections
**MUST** recognize repeatable sections and generate multiple instances as needed (e.g., multiple requirements, multiple decisions), **MUST NOT** limit to single instance when multiple are required

## GUIDANCE 9: Template Output Format
**MUST** generate final output files in pure markdown format without any YAML fields or structure, **MUST NOT** include YAML syntax in the generated documents

## GUIDANCE 12: [Steps] Tag
**MUST** execute all steps sequentially without stopping with their sub-tasks and achieve stated outcomes, **MUST NOT** skip steps or reorder unless dependencies require

## GUIDANCE 13: [DoD] Tag
**MUST** verify all DoD checklist items are satisfied before considering task complete, **MUST NOT** mark task complete with unchecked DoD items

## GUIDANCE 14: [Role] & [Skills] Tags
**MUST** adopt the specified role perspective and apply listed skills during execution, **MUST NOT** deviate from role responsibilities or ignore skill requirements

## GUIDANCE 15: [Constraints] Tag
**MUST** strictly follow all constraints as hard rules throughout execution, **MUST NOT** violate any constraint even if seems reasonable

## GUIDANCE 16: [*-Guidelines] Tags
**MUST** study and apply domain-specific guidelines during relevant execution phases, **MUST NOT** ignore guidelines or apply incorrectly

## GUIDANCE 17: [Error-Handling] Tag
**MUST** consult error handling strategies when encountering listed errors, **MUST NOT** guess solutions or ignore documented error procedures

## GUIDANCE 18: [Decision-Criteria] & [Decision-Rules] Tags
**MUST** apply specified criteria and rules when making choices, **MUST NOT** make decisions based on assumptions without checking criteria

## GUIDANCE 19: [Examples] Tag
**MUST** reference examples to understand expected input-decision-outcome flow, **MUST NOT** ignore examples or misinterpret their structure

## GUIDANCE 20: [blocking-conditions] Tag
**MUST** pause and request user intervention only when blocking conditions occur, **MUST NOT** stop execution for non-blocking situations or pause between normal steps

## GUIDANCE 21: [Output] Tag
**MUST** only generate the output files clearly stated within the output section of the tasks. **MUST NOT** generate any out-of-scope files.

## GUIDANCE 23: Output File Management
**MUST** check if output files already exist before generating content; if exist, read and update them rather than creating new files, **MUST NOT** create duplicate files or ignore existing content. When updating, preserve existing structure and enhance/correct content based on new requirements.

## GUIDANCE 23: [Scope-of-Work] Tag
**MUST** execute all tasks within the [Scope-of-Work] section AND all mandatory requirements in [Constraints] (validation coordination, tool usage), **MUST NOT** perform actions outside defined scope unless required by constraints

## GUIDANCE 24: Step and Task Completion Validation
**MUST** call step-validator after completing each individual step in the [Steps] section (to verify step outcomes), and call completion-validator only after finishing the entire task workflow (to verify DoD achievement); **MUST** wait for PASS responses before proceeding to the next step or marking task complete; **MUST NOT** skip validations, confuse the two validators, or mark the step as done after a FAIL

---

## Template Usage Guide

### Template Structure Overview

All templates follow a consistent instruction-based format:
- **template metadata**: Defines template ID, name, version, and output specifications
- **sections**: Hierarchical content structure with natural language instructions
- **instruction fields**: Guide agents on what content to generate and how to format it
- **repeatable sections**: Mark sections that can occur multiple times

### Reading Templates

1. **Start with template.output**: Understand what file will be generated and where
2. **Review sections hierarchy**: Map sections to markdown heading levels
3. **Read instruction fields**: These contain the actual guidance on what to write
4. **Identify repeatable sections**: Look for `repeatable: true` to know what can repeat

### Generating Content from Templates

1. **Section hierarchy becomes markdown headings**:
   - Top-level section → # Heading 1
   - Nested section → ## Heading 2
   - Deeper nesting → ### Heading 3, #### Heading 4

2. **Follow instructions, not YAML structure**:
   - Instructions describe what content to create
   - Do NOT copy instruction text verbatim into output
   - Use instructions as guidance to generate appropriate content

3. **Handle repeatable sections**:
   - Create as many instances as needed (e.g., REQ-001, REQ-002, REQ-003)
   - Each instance follows the same instruction format
   - Number or ID sequentially

4. **Use markdown formatting**:
   - Headings for structure
   - Lists (ordered/unordered) for items
   - Tables where specified in instructions
   - Code blocks for technical content
   - Bold/italic for emphasis

### Example Template Interpretation

Given this template section:
```yaml
- id: functional-requirements
  title: Functional Requirements
  repeatable: true
  instruction: |
    For each requirement:
    ## REQ-{id}: {Title}
    **Description:** {what the system must do}
```

Generate markdown like:
```markdown
# Functional Requirements

## REQ-001: User Authentication
**Description:** System must authenticate users via email and password

## REQ-002: Password Reset
**Description:** Users must be able to reset forgotten passwords via email
```

### Key Principles

- **Instructions are guidance, not content**: Read instructions to understand what to create, don't copy them
- **Structure guides organization**: Use section hierarchy to organize content logically
- **Completeness matters**: Address all instruction points, don't skip guidance
- **Markdown is output**: Always generate clean, readable markdown documents
- **Context awareness**: Use project-specific information to fill in template placeholders

---

# MCP Tools Usage Guide

The SunnyCore framework integrates four powerful Model Context Protocol (MCP) tools to enhance the development workflow. Each tool serves specific purposes across different phases.

## Available Tools

| Tool | Purpose | Common Use Cases |
|------|---------|-----------------|
| **sequential-thinking** | Structured reasoning and validation | Complex planning, decision analysis, validation |
| **claude-context** | Codebase indexing and semantic search | Finding implementations, understanding existing code |
| **context7** | External library documentation lookup | API verification, package compatibility checks |
| **playwright** | Browser automation for research | Competitor analysis, UI/UX research |

## Sequential Thinking Tool

**Purpose:** Enable structured, step-by-step reasoning for complex problem-solving and validation.

**When to Use:**
- Breaking down complex problems into logical steps
- Evaluating multiple solution approaches
- Validating design decisions and consistency
- Planning multi-phase workflows
- Analyzing trade-offs and dependencies

**Usage Pattern:**
```yaml
Tool: sequential-thinking
Trigger: When facing complex decisions requiring structured analysis
Output: Step-by-step reasoning with clear conclusions
```

**Example Scenarios:**

1. **Requirement Decomposition**
   - Scenario: User provides vague requirements
   - Application: Systematically break down into atomic, verifiable requirements
   - Outcome: Clear requirement structure with dependencies mapped

2. **Architecture Decision Making**
   - Scenario: Multiple technology options available
   - Application: Evaluate pros/cons of each approach systematically
   - Outcome: Justified architecture choice with documented trade-offs

3. **Implementation Planning**
   - Scenario: Complex feature requiring multiple steps
   - Application: Design test-driven development phases (RED → GREEN → REFACTOR)
   - Outcome: Detailed implementation plan with clear acceptance criteria

**Best Practices:**
- Use for decisions requiring justification and documentation
- Apply when multiple stakeholders need to understand reasoning
- Ideal for cross-cutting concerns affecting multiple components

## Claude-Context Tool

**Purpose:** Index and semantically search codebases to understand existing implementations and find relevant code.

**When to Use:**
- Working with existing codebases (Brownfield projects)
- Finding similar functionality patterns
- Locating dependencies and integration points
- Verifying component existence
- Gathering implementation evidence

**Usage Pattern:**
```yaml
Tool: claude-context
Prerequisites: Codebase must be indexed first
Query Style: Natural language questions about code
Output: Relevant code snippets with file locations
```

**Example Scenarios:**

1. **Understanding Existing Architecture**
   - Scenario: New to an existing project
   - Query: "How is authentication implemented?"
   - Application: Search for auth-related modules and patterns
   - Outcome: Understanding of existing authentication flow

2. **Finding Integration Points**
   - Scenario: Need to add new feature to existing system
   - Query: "Where are the database connection configurations?"
   - Application: Locate configuration files and initialization code
   - Outcome: Proper integration without breaking existing functionality

3. **Locating Test Patterns**
   - Scenario: Writing tests for new feature
   - Query: "What testing patterns are used for API endpoints?"
   - Application: Find existing test examples and patterns
   - Outcome: Consistent testing approach with existing codebase

**Best Practices:**
- Index codebase before starting work on Brownfield projects
- Use full questions rather than keywords for semantic search
- Verify search results by reading actual code
- Fall back to grep for exact text matching when needed

## Context7 Tool

**Purpose:** Query official documentation for external libraries, frameworks, and APIs to ensure correct usage.

**When to Use:**
- Integrating with external APIs or services
- Verifying package version compatibility
- Finding official best practices
- Troubleshooting integration issues
- Checking API changes and deprecations

**Usage Pattern:**
```yaml
Tool: context7
Input: Library name or specific API question
Query: Focused questions about official documentation
Output: Official documentation excerpts and examples
```

**Example Scenarios:**

1. **API Integration**
   - Scenario: Integrating payment gateway
   - Query: "Stripe API authentication methods"
   - Application: Verify correct API usage patterns
   - Outcome: Secure and correct API implementation

2. **Version Compatibility**
   - Scenario: Upgrading framework version
   - Query: "React 18 breaking changes"
   - Application: Identify migration requirements
   - Outcome: Smooth upgrade with handled breaking changes

3. **Configuration Guidance**
   - Scenario: Setting up deployment configuration
   - Query: "Docker multi-stage build best practices"
   - Application: Learn official recommended patterns
   - Outcome: Optimized and maintainable configuration

**Best Practices:**
- Query before implementing external integrations
- Verify version-specific documentation
- Cross-reference with official examples
- Use for troubleshooting integration errors

## Playwright Tool

**Purpose:** Automate browser interactions for research and learning from existing implementations.

**When to Use:**
- Researching competitor features and UX patterns
- Studying open-source project implementations
- Collecting real-world UI/UX examples
- Understanding industry-standard patterns
- Gathering reference implementations

**Usage Pattern:**
```yaml
Tool: playwright
Purpose: Research and learning (not production automation)
Target: Publicly accessible websites and open-source projects
Output: Observations and patterns for reference
```

**Example Scenarios:**

1. **Competitor Feature Research**
   - Scenario: Designing new user onboarding flow
   - Application: Study how leading products handle onboarding
   - Observation: Multi-step wizard vs. single-page approach
   - Outcome: Informed UX design decisions

2. **Architecture Pattern Study**
   - Scenario: Designing system architecture
   - Application: Review open-source projects with similar requirements
   - Observation: Component structure and integration patterns
   - Outcome: Proven architecture patterns to adapt

3. **UI Component Research**
   - Scenario: Building complex data visualization
   - Application: Study how others implement similar visualizations
   - Observation: Interaction patterns and accessibility features
   - Outcome: Better user experience design

**Best Practices:**
- Use for research and inspiration, not copying
- Focus on publicly accessible resources
- Respect robots.txt and rate limits
- Combine with official documentation (context7) for validation
- Document findings for team knowledge sharing

## Tool Selection Guide

**Decision Framework:**

```
Start with your current task:
│
├─ Need to make a complex decision?
│  → Use sequential-thinking
│  
├─ Need to understand existing code?
│  → Use claude-context
│  
├─ Need external API/library info?
│  → Use context7
│  
└─ Need research/UX reference?
   → Use playwright
```

**Common Tool Combinations:**

| Situation | Tool Combination | Purpose |
|-----------|------------------|---------|
| **Brownfield Feature** | sequential-thinking + claude-context | Analyze existing code, plan integration |
| **External Integration** | context7 + sequential-thinking | Verify API usage, plan implementation |
| **New Architecture** | sequential-thinking + context7 + playwright | Evaluate options, study patterns |
| **Requirement Analysis** | sequential-thinking + playwright | Understand needs, research solutions |

**Task Type Mapping:**

- **Planning & Analysis** → sequential-thinking (primary)
- **Code Understanding** → claude-context (primary)
- **API Integration** → context7 (primary)
- **UX Research** → playwright (primary)

## Best Practices & Common Pitfalls

**General Guidelines:**

✅ **Do:**
- Choose tools based on specific task needs
- Combine tools strategically for complex tasks
- Use sequential-thinking for decisions requiring documentation
- Index codebase early in Brownfield projects
- Query context7 before implementing external integrations
- Use playwright for research and learning

❌ **Don't:**
- Use sequential-thinking for trivial decisions
- Query claude-context on non-indexed codebases
- Use context7 for internal documentation (use claude-context)
- Use playwright for production automation
- Apply all tools simultaneously without clear purpose

**Tool-Specific Tips:**

**Sequential Thinking:**
- Break complex problems into 5-10 logical steps
- Document reasoning for future reference
- Use for decisions affecting multiple components

**Claude-Context:**
- Write queries as complete questions
- Be specific about what you're looking for
- Verify results by examining actual code

**Context7:**
- Include version numbers in queries when relevant
- Look for official examples and patterns
- Cross-reference multiple documentation sources

**Playwright:**
- Focus on patterns and concepts, not exact implementations
- Respect website terms of service
- Document insights for team knowledge base

**Performance Considerations:**
- Index codebases once at project start
- Cache playwright research results
- Use semantic search first, grep for exact matches
- Combine tool outputs for comprehensive understanding

## Quick Reference

| Need to... | Use Tool | Example Query |
|------------|----------|---------------|
| Break down complex problem | sequential-thinking | "Analyze trade-offs between microservices vs monolith" |
| Find existing implementation | claude-context | "How is user authentication handled?" |
| Verify API usage | context7 | "Stripe payment intent API usage" |
| Research UX patterns | playwright | "Study e-commerce checkout flows" |
| Make architecture decision | sequential-thinking | "Evaluate database options for time-series data" |
| Locate integration points | claude-context | "Where are external API calls made?" |
| Check package compatibility | context7 | "React 18 with TypeScript 5 compatibility" |
| Study competitor features | playwright | "Analyze dashboard UX of leading tools" |

**When in Doubt:**
1. Start with sequential-thinking for complex decisions
2. Use claude-context for code-related questions
3. Query context7 for external dependencies
4. Research with playwright for UX/pattern inspiration

---

# Summary Instructions

When performing compact conversation compression, use the following classifications to determine what to keep, conditionally keep, or ignore:

## KEEP

**Core execution structures that MUST be fully preserved:**

### GUIDANCE Rules
- All guidance rules (core execution rules)

### Tagged Structure Definitions
- [Description] - Command/task/agent descriptions
- [Path-Variables] - Path variable definitions
- [Input] - Input requirements
- [Output] - Output requirements
- [Role] - Role definitions
- [Skills] - Skill requirements
- [Scope-of-Work] - Work scope boundaries
- [Constraints] - Execution constraints (hard rules)
- [DoD] - Definition of Done checklists
- [Steps] - Execution steps with their Outcomes
- [Tools] - Tool usage guidance
- [Blocking-Conditions] - Blocking conditions
- [Custom-Commands] - Custom command lists
- [Validation-Steps] - Validation steps

### Template Core Structure
- template metadata (id, name, version, output)
- sections (id, title, repeatable, instruction)
- Template Structure Overview (how to read and generate)

### MCP Tools Reference
- Available Tools table (overview of all 4 tools)
- Tool Selection Guide (decision framework and combinations)
- Quick Reference table (task-to-tool mapping)

### Summmary instructions
- Summmary instructions (preserve if current task involves summary compression)

### Agent Metadata
- YAML front matter (name, description, model, color)

## MAY IGNORE

**Auxiliary content for understanding but not core to execution; conditionally preserve:**

- [Examples] - Example explanations (preserve based on context relevance)
- [Decision-Criteria] & [Decision-Rules] - Decision criteria (preserve if current task involves decision-making)
- [Error-Handling] - Error handling strategies (preserve if encountering related errors)
- [*-Guidelines] tags - Domain-specific guidelines (e.g., Development-Guidelines, Requirements-Analysis-Guidelines)
  - Preserve if current step involves that domain
  - Otherwise may omit
- Detailed explanation paragraphs in Template Usage Guide
- MCP Tools detailed sections (Example Scenarios, Best Practices, Tool-Specific Tips)
  - Preserve Available Tools table and Quick Reference table
  - Preserve when current task involves tool selection
  - Otherwise may omit detailed explanations

## IGNORE

**Non-execution content that can be completely omitted:**

- Mermaid diagrams in README.md
- Tabular explanations in README.md (workflow selection guides, role responsibility tables)
- Configuration instructions (MCP server config, dependency lists)
- Detailed annotations and example outputs in Templates
- Complete example demonstrations in Example sections (full Input/Decision/Outcome examples)
- Visual elements in workflow descriptions (emojis, charts)

## Compression Principles

1. **Priority ordering**: KEEP > MAY IGNORE > IGNORE
2. **Context-dependent**: MAY IGNORE category decisions are dynamic based on current task/step being executed
3. **Structural integrity**: When preserving KEEP category content, maintain original tag structure and hierarchy
4. **Execution-oriented**: All definitions and constraints directly related to task execution must be preserved
5. **Unlabeled content**: For other conversation content not explicitly categorized above (e.g., generated code, chat messages, user interactions, intermediate outputs), use your judgment to determine whether to preserve based on relevance to ongoing tasks and context continuity
