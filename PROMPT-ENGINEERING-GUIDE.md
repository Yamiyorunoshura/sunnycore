# 使用技術
本專案使用xml標籤配合結構化提示詞，實現統一工作流框架。在本文檔，我們將會介紹統一的xml標籤格式以及使用方法，協助開發者快速上手。
初次之外，我們還會介紹我們所使用的prompt統一架構，協助你理解我們所使用的prompt技巧。

# 通用xml標籤
在這個部分，我們將會介紹在所有文檔中都會出現的通用xml標籤，協助你理解這些標籤的用途。

## 上下文相關標籤
這些標籤用於描述文檔的上下文。
- <input>：描述文檔的輸入。
    - <context>： 描述文檔的上下文。
- <output>： 定義文檔的輸出。
    - <context>： 描述文檔的上下文。
- <constraints>： 描述工作中的規範
- <example>： 提供實際的例子
- <questions>： 提出讓LLM自行思考的問題
- <checks>： 提出讓LLM自行檢查的項目

## 角色相關標籤
- <role, name = "Role Name">： 描述角色的核心人格。
    - name： 定義角色的名稱。

## 工作流程相關標籤
- <workflow, importance = "Optional/Normal/Important/Critical">： 定義工作流程的開始。
    - importance： 定義工作流程的重要性。
    - <stage, id = "Stage ID", level_of_think = "non-thinking/think/think hard/think harder, Ultra think", read_token_budget = "Customise", write_token_budget = "Customise", cache_write_budget = "Customise", cache_read_budget = "Customise">： 定義工作流程的階段。
        - stage id： 定義工作流程的階段ID。
        - level_of_think： 定義工作流程的階段思考能力。
        - read_token_budget： 定義工作流程的階段讀取token預算。
        - write_token_budget： 定義工作流程的階段寫入token預算。
        - cache_write_budget： 定義工作流程的階段快取寫入token預算。
        - cache_read_budget： 定義工作流程的階段快取讀取token預算。

## Chain-of-Thought 推理相關標籤
- <reasoning_framework, importance = "Optional/Normal/Important/Critical">： 定義推理框架的開始。
    - importance： 定義推理框架的重要性。
    - <step_by_step>： 定義逐步推理的引導內容。
    - <thinking_process>： 定義結構化思考過程。
    - <decision_points>： 定義關鍵決策點。
    - <prefill>： 定義預填充輸出格式，用於控制模型的初始輸出結構。

## 模塊化組件相關標籤
- <modular_components>： 定義模塊化組件的容器。
    - <role_context, name = "Agent Name">： 定義角色上下文內容。
        - name： 指定代理角色名稱。
    - <task_context>： 定義具體任務上下文。
    - <examples_bank, type = "few_shot/zero_shot">： 定義示例集合。
        - type： 指定示例類型。
    - <prefill>： 定義預填充輸出格式。

## 品質保證相關標籤
- <quality_framework>： 定義品質保證框架。
    - <reasoning_validation>： 定義推理過程驗證機制。
    - <output_validation>： 定義輸出品質檢查機制。

# 提示詞架構
在這個部分，我們將會介紹我們所使用的提示詞架構，協助你理解我們所使用的提示詞技巧。

## agents提示詞架構

---
name: {Agent Name}
description: {Description}
model: inherit
color: {Color}
---

<start_sequence>
</start_sequence>

<role name="Role Name">
# 角色
- 你是{Role Name}，一名擁有30年經驗的資深{Role Description}。
- {Role Description}
</role>

<input>
  <context>
  </context>
  <templates>
  </templates>
</input>

<output>
</output>

<constraints, importance = "Optional/Normal/Important/Critical">
</constraints>

<workflow, importance = "Optional/Normal/Important/Critical">
  <stage id="n: stage name", level_of_think = "non-thinking/think/think hard/think harder, Ultra think", cache_read_budget = "customise">

  <checks>
  </checks>
  </stage>
</workflow>

<example>
</example>

## commands提示詞架構
<start_sequence>
</start_sequence>

<role name="Role Name">
# 角色
- 你是{Role Name}，一名擁有30年經驗的資深{Role Description}。
- {Role Description}
</role>

<input>
  <context>
  </context>
  <templates>
  </templates>
  <tasks>
  </tasks>
</input>

<output>
</output>

<constraints, importance = "Optional/Normal/Important/Critical">
</constraints>

<custom_commands>
</custom_commands>

<workflow, importance = "Optional/Normal/Important/Critical">
  <stage id="n: stage name", level_of_think = "non-thinking/think/think hard/think harder, Ultra think", cache_read_budget = "customise">

  <checks>
  </checks>
  </stage>

</workflow>

## workflow提示詞架構
<input>
  <context>
  </context>
  <templates>
  </templates>
  <subagent-list>
  </subagent-list>
</input>

<output>
</output>

<constraints, importance = "Optional/Normal/Important/Critical">
</constraints>

<workflow, importance = "Optional/Normal/Important/Critical">
  <stage id="n: stage name", level_of_think = "non-thinking/think/think hard/think harder, Ultra think", read_token_budget = "customise", write_token_budget = "customise", cache_write_budget = "customise", cache_read_budget = "customise">

  <questions>
  </questions>

  <checks>
  </checks>
  </stage>

</workflow>

<example>
</example>