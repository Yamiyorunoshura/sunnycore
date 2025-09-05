<input>
  <context>
  1. {project_root}/docs/specs/requirements.md
  2. {project_root}/docs/specs/task.md
  3. {project_root}/docs/specs/design.md
  </context>
  <templates>
  4. {project_root}/sunnycore/templates/implementation-plan-tmpl.yaml
  </templates>
</input>

<output>
1. {project_root}/docs/implementation-plan/{task_id}-plan.md
</output>

<constraints, importance = "Critical">
- 必須嚴格遵循工作流程
- 必須閱讀所有輸入文件
- 必須生成所有必要的輸出文件或內容
- 必須確保所有階段性檢查點已被完成
- 若階段性檢查點未完成，必須完成遺漏工作，方可進入下一步驟
- 必須確保所有關鍵問題已被解決
- 若關鍵問題未解決，必須完成遺漏工作，方可進入下一步驟
</constraints>

<workflow, importance = "Critical">
  <stage id="0: 創建todo list", level_of_think = "non-thinking", cache_read_budget = "not more than 190K tokens per request">
  - 閱讀整份workflow
  - 進一步閱讀所有步驟
  - 閱讀所有步驟下的無序列表項
  - 使用todo-list工具為每個無序列表項在todo list中創建一個todo item

  <checks>
    - [ ] todo list創建完成
    - [ ] todo list已經包含所有無序列表項
    - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="1: 實作計劃構思", level_of_think = "Ultra think", cache_read_budget = "not more than 190K tokens per request">
  - 根據task_id，從task.md中提取相關的任務描述
  - 閱讀與任務描述相關的需求
  - 閱讀design.md，查看項目設計規範
  - 根據任務描述以及需求，使用sequential-thinking工具構思實作計劃
  </stage>

  <questions>
    關鍵問題：
    - 實作計劃是否符合需求？
    - 實作計劃是否符合項目設計規範？
    - 實作計劃是否符合實作計劃模板？
  </questions>

  <checks>
    - [ ] 實作計劃構思完成
    - [ ] 實作計劃構思符合需求
    - [ ] 實作計劃構思符合項目設計規範
    - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="2: 實作計劃生成", level_of_think = "Ultra think", cache_read_budget = "not more than 190K tokens per request">
  - 將實作計劃構思結果填入實作計劃模板
  - 將實作計劃模板轉換為markdown格式
  - 將實作計劃模板輸出至{output}
  </stage>

  <questions>
    關鍵問題：
    - 實作計劃是否符合實作計劃模板？
    - 實作計劃是否符合需求？
    - 實作計劃是否符合項目設計規範？
  </questions>

  <checks>
    - [ ] 實作計劃生成完成
    - [ ] 實作計劃符合實作計劃模板
    - [ ] 實作計劃符合需求
    - [ ] 實作計劃符合項目設計規範
    - [ ] todo list更新完成
  </checks>
  </stage>

</workflow>