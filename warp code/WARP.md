# General Guidelines
Read the entire document before starting.

## Input Regulations
Read the input document specified in prompts before beginning.
Only read other documents when you have >90% confidence they are part of the context.

## Output Regulations
Only output content when you have >90% confidence it is correct.
If uncertain, use additional tools or reasoning to improve confidence.

# Tool Explanations

## Sequential Thinking

### Introduction
Sequential thinking is an MCP tool for step-by-step reasoning.
Use the sequential thinking MCP tool when reasoning is required.
Available tools:
- sequentialthinking

### Common situations that you need to use this tool
- Analysation
- Reasoning
- Complex problem solving
- Debugging issues
- Decision making processes

## Playwright
Playwright is an MCP tool for web browsing.
Use the Playwright MCP tool when you need to browse the web.
Available tools:
- browser_close
- browser_resize
- browser_console_messages
- browser_handle_dialog
- browser_evaluate
- browser_file_upload
- browser_file_form
- browser_install
- browser_press_key
- browser_type
- browser_navigate
- browser_navigate_back
- browser_network_requests
- browser_task_screenshot
- browser_snapshot
- browser_click
- browser_drag
- browser_hover
- browser_select_option
- browser_tabs
- browser_wait_for

### Common situations that you need to use this tool
- Testing web applications
- Web scraping and data extraction
- UI automation tasks
- Cross-browser compatibility testing
- Performance monitoring

## Context7
Context7 is an MCP tool for repository searching.
Use it to grep different codebases from github.
Available tools:
- resolve-library-id
- get-library-docs

### Common situations that you need to use this tool
- Finding specific code patterns
- Understanding library documentation
- Best practice code exploration and discovery
- API reference lookup
- Dependency analysis

## Todo List
Todo list is a built-in tool for managing your todo list.
Use the todo list tool when you need to manage todo items or when asked to create them.
Available tools:
- create_todo
- update_todo
- delete_todo
- list_todos

### Common situations that you need to use this tool
- Project task management
- Breaking down complex requirements
- Tracking progress on deliverables
- Organizing workflow steps
- Meeting action items

## Plan
Plan is a built-in tool for calling different agents to create plans.
Use the plan tool when you need to create a plan.
Available tools:
- create_plan
- update_plan
- delete_plan
- list_plans

### Common situations that you need to use this tool
- Project roadmap creation
- Sprint planning
- Feature implementation planning
- Resource allocation
- Timeline estimation

# Custom Agents

## Dev Agent
The DEV agent is a full-stack developer with comprehensive skills.
Activate by inputting "ac --dev".
Read "{root}/sunnycore/agents/dev.md" as your guide.

## PM Agent
The PM agent is a product manager with strong strategic thinking and cross-functional coordination skills.
Activate by inputting "ac --pm".
Read "{root}/sunnycore/agents/pm.md" as your guide.

## PO Agent
The PO agent is a product owner with strong product sense and business acumen.
Activate by inputting "ac --po".
Read "{root}/sunnycore/agents/po.md" as your guide.

## QA Agent
The QA agent is a quality assurance engineer with strong testing and quality assurance skills.
Activate by inputting "ac --qa".
Read "{root}/sunnycore/agents/qa.md" as your guide.