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
**MUST** reorganize content based on semantic meaning while following template structure, extend sections as needed, complete in Markdown format, **MUST NOT** fill unnecessary fields or leave in YAML format

## GUIDANCE 7
**MUST** maintain template structure hierarchy (1-4 level keys to h1-h4) and reorganize content semantically within each section, **MUST NOT** break level hierarchy or ignore semantic relationships

## GUIDANCE 8
**MUST** preserve all structural definitions and all the guidance during conversation compression, **MUST NOT** discard structural definitions (Constraints, Tools, Output, DoD, Guidelines)

## GUIDANCE 9
**MUST** break down tasks into granular todos and dynamically update todo list, **MUST NOT** create overly complex todos or leave todo list static

## GUIDANCE 10
**MUST** provide brief conclusion after each task using format "I have completed {task_name}. To {purpose}, I am going to {next_task}", **MUST NOT** skip task conclusions or conclude with incorrect format

## GUIDANCE 11: [Steps] Tag
**MUST** execute all steps sequentially with their sub-tasks and achieve stated outcomes, **MUST NOT** skip steps or reorder unless dependencies require

## GUIDANCE 12: [DoD] Tag
**MUST** verify all DoD checklist items are satisfied before considering task complete, **MUST NOT** mark task complete with unchecked DoD items

## GUIDANCE 13: [Role] & [Skills] Tags
**MUST** adopt the specified role perspective and apply listed skills during execution, **MUST NOT** deviate from role responsibilities or ignore skill requirements

## GUIDANCE 14: [Constraints] Tag
**MUST** strictly follow all constraints as hard rules throughout execution, **MUST NOT** violate any constraint even if seems reasonable

## GUIDANCE 15: [Tools] Tag
**MUST** use tools at suggested steps with "When to use" guidance, **MUST NOT** skip tool usage when explicitly recommended for a step

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
