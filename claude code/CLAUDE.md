# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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

## GUIDANCE 6
**MUST** fill only relevant template fields, extend as needed, convert to Markdown when complete, **MUST NOT** fill unnecessary fields or leave in YAML format

## GUIDANCE 7
**MUST** maintain level mapping (1-4 level keys to h1-h4) and omit empty value content, **MUST NOT** include empty values or break level hierarchy

## GUIDANCE 8
**MUST** preserve all structural definitions and all the guidance during conversation compression, **MUST NOT** discard structural definitions (Constraints, Tools, Output, DoD, Guidelines)

## GUIDANCE 9
**MUST** break down tasks into granular todos and dynamically update todo list, **MUST NOT** create overly complex todos or leave todo list static

## GUIDANCE 10
**MUST** provide brief conclusion after each task using format "I have completed {task_name}. To {purpose}, I am going to {next_task}", **MUST NOT** skip task conclusions or conclude with incorrect format

## GUIDANCE 11: [Input] Tag
**MUST** verify all inputs listed in [Input] exist before execution, **MUST NOT** proceed with missing required inputs unless marked "(Conditional)"

## GUIDANCE 12: [Output] Tag
**MUST** produce all deliverables specified in [Output] with correct format and location, **MUST NOT** skip any output items or modify output paths

## GUIDANCE 13: [Steps] Tag
**MUST** execute all steps sequentially with their sub-tasks and achieve stated outcomes, **MUST NOT** skip steps or reorder unless dependencies require

## GUIDANCE 14: [DoD] Tag
**MUST** verify all DoD checklist items are satisfied before considering task complete, **MUST NOT** mark task complete with unchecked DoD items

## GUIDANCE 15: [Role] & [Skills] Tags
**MUST** adopt the specified role perspective and apply listed skills during execution, **MUST NOT** deviate from role responsibilities or ignore skill requirements

## GUIDANCE 16: [Constraints] Tag
**MUST** strictly follow all constraints as hard rules throughout execution, **MUST NOT** violate any constraint even if seems reasonable

## GUIDANCE 17: [Tools] Tag
**MUST** use tools at suggested steps with "When to use" guidance, **MUST NOT** skip tool usage when explicitly recommended for a step

## GUIDANCE 18: [Path-Variables] Tag
**MUST** replace path variables with actual paths when reading or writing files, **MUST NOT** use variable names as literal paths

## GUIDANCE 19: [*-Guidelines] Tags
**MUST** study and apply domain-specific guidelines during relevant execution phases, **MUST NOT** ignore guidelines or apply incorrectly

## GUIDANCE 20: [Error-Handling] Tag
**MUST** consult error handling strategies when encountering listed errors, **MUST NOT** guess solutions or ignore documented error procedures

## GUIDANCE 21: [Decision-Criteria] & [Decision-Rules] Tags
**MUST** apply specified criteria and rules when making choices, **MUST NOT** make decisions based on assumptions without checking criteria

## GUIDANCE 22: [Examples] Tag
**MUST** reference examples to understand expected input-decision-outcome flow, **MUST NOT** ignore examples or misinterpret their structure

## GUIDANCE 23: [blocking-conditions] Tag
**MUST** pause and request user intervention only when blocking conditions occur, **MUST NOT** stop execution for non-blocking situations or pause between normal steps
