# 使用技術
本專案使用xml標籤配合結構化提示詞，實現統一工作流框架。在本文檔，我們將會介紹統一的xml標籤格式以及使用方法，協助開發者快速上手。

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