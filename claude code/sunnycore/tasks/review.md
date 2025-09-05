<input>
  <context>
  1. {project_root}/docs/dev-notes/{task_id}-dev-notes.md
    - dev_entries
    - integration_summary
  2. {project_root}/docs/implementation-plan/{task_id}-plan.md
    - context
    - approach
    - risks
    - dev_notes_note
  </context>
  <templates>
  3. {project_root}/sunnycore/templates/review-tmpl.yaml
  </templates>
  <subagent-list>
  4. {project_root}/sunnycore/config.yaml
    - qa-subagent-list
  </subagent-list>
</input>

<output>
1. 總結各個子代理的審查結果後得出的綜合報告{task_id}-review.md
2. 實踐等級(bronze/silver/gold/platinum)
3. 實踐分數(1-5)
4. 優秀的代碼實踐
5. 審查發現的問題
6. 審查發現的潛在問題
</output>

<constraints, importance = "Critical">
- 每完成一步，必須更新todo list。
- 必須嚴格遵循工作流程
- 必須閱讀所有輸入文件
- 必須生成所有必要的輸出文件或內容
- 審查過程中不可修改任何程式碼
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
    階段性檢查點：
    - [ ] todo list創建完成
    - [ ] todo list已經包含所有無序列表項
    - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="1: 根據輸入文件構建專案上下文", level_of_think = "Ultra think", cache_read_budget = "not more than 190K tokens per request">
  - 使用claude context工具查找輸入文件
  - 閱讀並所有輸入文件
  - 使用sequential-thinking工具協助思考和分析所有輸入文件
  - 將輸入文件按照審查類型分類

  <questions>
    關鍵問題：
    - 所有上下文是否有證據依據？
    - 現有架構的是否有潛在薄弱點需要被重點審查？
  </questions>

  <checks>
    階段性檢查點：
    - [ ] 所有輸入文件閱讀完成
    - [ ] 所有輸入文件分析完成
    - [ ] 輸入文件分類完成
  </checks>
  </stage>

  <stage id="2: 子代理任務分配與啟動", level_of_think = "think", cache_read_budget = "not more than 190K tokens per request">
  - 閱讀qa-subagent-list獲取可調用的子代理列表
  - 根據輸入文件判斷審查類型，並查看審查類型所對應的子代理
  - 按照範例格式構建給每位子代理的上下文，並將上下文傳遞給每位子代理
  - 為每位子代理發配任務，並同時啟動所有選中的子代理

  <questions>
  關鍵問題：
  - 審查任務的類型是否正確？
  - 是否只調用了被允許的子代理？
  - 傳遞給子代理的上下文是否符合範例格式？
  - 是否已經將所有上下文以及審查任務傳遞給所有子代理？
  - 分配給子代理的審查任務是否足夠原子化？
  </questions>

  <checks>
  階段性檢查點：
  - [ ] 所有子代理任務分配完成
  - [ ] 所有子代理啟動完成
  - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="3: 根據每位子代理的審查結果，構建綜合報告", level_of_think = "think hard", cache_read_budget = "not more than 190K tokens per request">
  - 使用sequential-thinking工具協助思考和分析每位子代理的審查結果
  - 根據輸入文件中的審查報告模板，填入分析過後的審查結果
  - 將填寫完畢的審查報告轉換為markdown格式
  - 將轉換為markdown格式的完整審查報告保存到{project_root}/docs/review-results/並命名為{task_id}-review.md

  <questions>
    關鍵問題：
  - 審查結果是否有證據依據？
  - 審查報告是否符合審查報告模板？
  - 審查報告是否完整？
  </questions>

  <checks>
  階段性檢查點：
  - [ ] 審查結果分析完成
  - [ ] 審查報告模板填寫完成
  - [ ] 審查報告轉換為markdown格式完成
  - [ ] 審查報告保存完成
  </checks>
  </stage>

  <stage id="4: 根據審查結果，構建實踐等級和實踐分數判斷審查是否通過", level_of_think = "think hard", cache_read_budget = "not more than 190K tokens per request">
  - 根據審查結果，構建實踐等級和實踐分數
  - 判斷實踐等級和實踐分數是否符合審查標準
  - 若符合審查標準，則審查通過
  - 若不符合審查標準，則審查不通過
  - 按照範例更新task.md來反應審查是否通過

  <questions>
    關鍵問題：
    - 實踐等級和實踐分數是否符合審查標準？
    - 審查是否通過？
    - 通過的理由是什麼呢？
    - 不通過的理由是什麼呢？
  </questions>

  <checks>
  階段性檢查點：
  - [ ] 實踐等級和實踐分數構建完成
  - [ ] 審查是否通過判斷完成
  - [ ] task.md更新完成
  - [ ] todo list更新完成
  </checks>
  </stage>
</workflow>

<example>
# 專案狀態
- brownfield/greenfield

# 審查狀態
- initial/follow_up/re_review

# 審查迭代
- 1/2/3/...

# 重點關注問題
- xxx
- yyy
- zzz

# 潛在風險
- xxx
- yyy
- zzz

# 審查任務
- xxx
- yyy
- zzz
</example>

<example>
# 原task.md
- [ ] Task 1: xxx
  - [ ] Task 1.1: yyy
  - [ ] Task 1.2: zzz
- [ ] Task 2: xxx
  - [ ] Task 2.1: yyy
  - [ ] Task 2.2: zzz
- [ ] Task 3: xxx
  - [ ] Task 3.1: yyy
  - [ ] Task 3.2: zzz
- ...

# 更新後的task.md（通過審查）
- [x] Task 1: xxx
  - [x] Task 1.1: yyy
  - [x] Task 1.2: zzz
- [x] Task 2: xxx
  - [x] Task 2.1: yyy
  - [x] Task 2.2: zzz
- [x] Task 3: xxx
  - [x] Task 3.1: yyy
  - [x] Task 3.2: zzz
- ...

# 更新後的task.md（不通過審查）
- [-] Task 1: xxx
  - [-] Task 1.1: yyy
  - [-] Task 1.2: zzz
- [-] Task 2: xxx
  - [-] Task 2.1: yyy
  - [-] Task 2.2: zzz
- [-] Task 3: xxx
  - [-] Task 3.1: yyy
  - [-] Task 3.2: zzz
- ...
</example>