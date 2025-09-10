# 使用技術
本專案使用xml標籤配合結構化提示詞，實現統一工作流框架。在本文檔，我們將會介紹統一的xml標籤格式以及使用方法，協助開發者快速上手。
初次之外，我們還會介紹我們所使用的prompt統一架構，協助你理解我們所使用的prompt技巧。

# 通用xml標籤
在這個部分，我們將會介紹在所有文檔中都會出現的通用xml標籤，協助你理解這些標籤的用途。

## 上下文相關標籤
這些標籤用於描述文檔的上下文。
- <input>：描述文檔的輸入。
    - <context>： 描述LLM需要讀取的上下文
- <output>： 定義文檔的輸出。
    - <context>： 描述LLM需要輸出的上下文
- <constraints>： 描述工作中的規範
- <example>： 提供實際的例子
- <questions>： 提出讓LLM自行思考的問題
- <checks>： 提出讓LLM自行檢查的項目

## 角色相關標籤
- <role, name = "Role Name">
  - 名字： 定義角色的名字。
  - 角色： 定義角色的角色。
  - 人格特質： 定義角色的人格特質。

## 工作流程相關標籤
- <workflow, importance = "Optional/Normal/Important/Critical">： 定義工作流程的開始。
    - importance： 定義工作流程的重要性。
    - <stage, id = "Stage ID", level_of_think = "non-thinking/think/think hard/think harder/ultra think", read_token_budget = "Customise", write_token_budget = "Customise", cache_write_budget = "Customise", cache_read_budget = "Customise">： 定義工作流程的階段。
        - stage id： 定義工作流程的階段ID。
        - level_of_think： 定義工作流程的階段思考能力。
        - read_token_budget： 定義工作流程的階段讀取token預算。
        - write_token_budget： 定義工作流程的階段寫入token預算。
        - cache_write_budget： 定義工作流程的階段快取寫入token預算。
        - cache_read_budget： 定義工作流程的階段快取讀取token預算。

# 提示詞架構
在這個部分，我們將會介紹我們所使用的提示詞架構，協助你理解我們所使用的提示詞技巧。

## agents提示詞架構

---(optional)
name: {Agent Name}
description: {Description}
model: inherit
color: {Color}
---

<start_sequence>
1. xxx
2. yyy
3. zzz
</start_sequence>

<role name="Role Name">
# 角色
- 你是{Role Name}，一名擁有30年經驗的資深{Role Description}。
- {Role Description}
</role>

<input>
  <context>
  1. xxx
  2. yyy
  3. zzz
  </context>
  <templates>
  1. xxx
  2. yyy
  3. zzz
  </templates>
</input>

<output>
1. xxx
2. yyy
3. zzz
</output>

<constraints, importance = "Optional/Normal/Important/Critical">
- xxx
- yyy
- zzz
</constraints>

<workflow, importance = "Optional/Normal/Important/Critical">
  <stage id="n: stage name", level_of_think = "non-thinking/think/think hard/think harder, Ultra think", cache_read_budget = "customise">
  - xxx
  - yyy
  - zzz

  <questions>
  - xxx?
  - yyy?
  - zzz?
  </questions>
  
  <checks>
  - [ ] xxx
  - [ ] yyy
  - [ ] zzz
  </checks>
  </stage>
</workflow>

<example>
</example>

## commands提示詞架構

<role name="Role Name">
名字：{Role Name}
角色：{Role Description}
人格特質：{Role Description}
</role>

<input>
  <context>
  1. xxx
  2. yyy
  3. zzz
  </context>
  <templates>
  1. xxx
  2. yyy
  3. zzz
  </templates>
  <tasks>
  1. xxx
  2. yyy
  3. zzz
  </tasks>
</input>

<output>
1. xxx
2. yyy
3. zzz
</output>

<constraints, importance = "Optional/Normal/Important/Critical">
- xxx
- yyy
- zzz
</constraints>

<custom_commands>
- *xxx
  - 讀取xxx
- *yyy
  - 讀取yyy
- *zzz
  - 讀取zzz
</custom_commands>

<workflow, importance = "Optional/Normal/Important/Critical">
  <stage id="n: stage name", level_of_think = "non-thinking/think/think hard/think harder, Ultra think", cache_read_budget = "customise">
  - xxx
  - yyy
  - zzz

  <checks>
  - [ ] xxx
  - [ ] yyy
  - [ ] zzz
  </checks>
  </stage>

</workflow>

## tasks提示詞架構
<input>
  <context>
  1. xxx
  2. yyy
  3. zzz
  </context>
  <templates>
  1. xxx
  2. yyy
  3. zzz
  </templates>
  <subagent-list>(optional)
  1. xxx
  2. yyy
  3. zzz
  </subagent-list>
</input>

<output>
1. xxx
2. yyy
3. zzz
</output>

<constraints, importance = "Optional/Normal/Important/Critical">
- xxx
- yyy
- zzz
</constraints>

<workflow, importance = "Optional/Normal/Important/Critical">
  <stage id="n: stage name", level_of_think = "non-thinking/think/think hard/think harder, Ultra think", read_token_budget = "customise", write_token_budget = "customise", cache_write_budget = "customise", cache_read_budget = "customise">
  - xxx
  - yyy
  - zzz

  <questions>
  - xxx?
  - yyy?
  - zzz?
  </questions>

  <checks>
  - [ ] xxx
  - [ ] yyy
  - [ ] zzz
  </checks>
  </stage>

</workflow>

<example>(optional)
</example>