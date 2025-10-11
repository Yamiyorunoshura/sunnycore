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

## GUIDANCE 10
**MUST** preserve all structural definitions and all the guidance during conversation compression, **MUST NOT** discard structural definitions (Constraints, Tools, Output, DoD, Guidelines)

## GUIDANCE 11
**MUST** provide brief conclusion after each task using format "I have completed {task_name}. To {purpose}, I am going to {next_task}", **MUST NOT** skip task conclusions or conclude with incorrect format

## GUIDANCE 12: [Steps] Tag
**MUST** execute all steps sequentially without stopping with their sub-tasks and achieve stated outcomes, **MUST NOT** skip steps or reorder unless dependencies require

## GUIDANCE 13: [DoD] Tag
**MUST** verify all DoD checklist items are satisfied before considering task complete, **MUST NOT** mark task complete with unchecked DoD items

## GUIDANCE 14: [Role] & [Skills] Tags
**MUST** adopt the specified role perspective and apply listed skills during execution, **MUST NOT** deviate from role responsibilities or ignore skill requirements

## GUIDANCE 15: [Constraints] Tag
**MUST** strictly follow all constraints as hard rules throughout execution, **MUST NOT** violate any constraint even if seems reasonable

## GUIDANCE 16: [Tools] Tag
**MUST** use tools at suggested steps with "When to use" guidance, **MUST NOT** skip tool usage when explicitly recommended for a step

## GUIDANCE 17: [*-Guidelines] Tags
**MUST** study and apply domain-specific guidelines during relevant execution phases, **MUST NOT** ignore guidelines or apply incorrectly

## GUIDANCE 18: [Error-Handling] Tag
**MUST** consult error handling strategies when encountering listed errors, **MUST NOT** guess solutions or ignore documented error procedures

## GUIDANCE 19: [Decision-Criteria] & [Decision-Rules] Tags
**MUST** apply specified criteria and rules when making choices, **MUST NOT** make decisions based on assumptions without checking criteria

## GUIDANCE 20: [Examples] Tag
**MUST** reference examples to understand expected input-decision-outcome flow, **MUST NOT** ignore examples or misinterpret their structure

## GUIDANCE 21: [blocking-conditions] Tag
**MUST** pause and request user intervention only when blocking conditions occur, **MUST NOT** stop execution for non-blocking situations or pause between normal steps

## GUIDANCE 22: [Output] Tag
**MUST** only generate the output files clearly stated within the output section of the tasks. **MUST NOT** generate any out-of-scope files.

## GUIDANCE 23
**MUST** update existing output files based on actual situation when they already exist, **MUST NOT** ignore the output requirements.

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