<input>
  <context>
  1. {project_root}/docs/specs/requirements.md
  2. {project_root}/docs/specs/task.md
  3. {project_root}/docs/specs/design.md
  4. {project_root}/docs/review-results/{task_id}-review.md
  5. {project_root}/docs/implementation-plan/{task_id}-plan.md
  </context>
  <templates>
  1. {project_root}/sunnycore/templates/dev-notes-tmpl.yaml
  </templates>
</input>

<output>
1. {project_root}/docs/dev-notes/{task_id}-dev-notes.md
2. 優質的代碼修復
3. Level(bronze/silver/gold/platinum)
4. Score(1-5)
</output>

<workflow, importance = "Critical">
  <stage id="0: 創建todo list", level_of_think = "non-thinking", cache_read_budget = "not more than 190K tokens per request">
  - 閱讀整份workflow
  - 進一步閱讀所有步驟
  - 閱讀所有步驟下的無序列表項
  - 使用Todo-list Tool為每個無序列表項在todo list中創建一個todo item

  <checks>
    - [ ] todo list創建完成
    - [ ] todo list已經包含所有無序列表項
    - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="1: Context Validation", level_of_think = "think", cache_read_budget = "not more than 190K tokens per request">
  - 閱讀所有輸入文件
  - 驗證所有輸入文件存在
  </stage>

  <checks>
    - [ ] 所有輸入文件閱讀完成
    - [ ] 所有輸入文件驗證完成
    - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="2: 分析Project Review Results", level_of_think = "Ultra think", cache_read_budget = "not more than 190K tokens per request">
  - 閱讀、並使用Sequential-thinking Tool分析Implementation Plan
  - 分析Implementation Plan的每一個Functional Requirements與Non-functional Requirements(F-1,N-1)
  - 對檢查結果進行Classification Processing，判斷其問題類別
  - 對問題類別進行Classification Processing，判斷其Fix Task Categories
  </stage>

  <checks>
    - [ ] Project Review Results分析完成
    - [ ] Project Review Results已經被Classification Processing
    - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="3: Context Construction", level_of_think = "think hard", cache_read_budget = "not more than 190K tokens per request">
  - 使用Claude-context Tool索引需要被修改的部分
  - 查看Sub-agent List獲取所有可調用的Sub-agent
  - 使用Sequential-thinking Tool思考Fix Tasks之間的Dependencies
  - 分辨可Parallel Tasks和不可Parallel Tasks，參考相關範例來發配任務給對應的Sub-agent
  - 將Fix Tasks以及檢查結果進行整合，根據範本樣式發送給對應開發任務的Sub-agent
  - 同時啟動所有被呼叫的Sub-agent

  <questions>
    - 構建的Context是否符合Project Review Results？
    - 構建的Context是否符合需求？
    - 構建的Context是否符合規範？
    - 是否已經將所有Context傳遞給所有Sub-agent？
    - 是否已經為所有Sub-agent發配任務？
    - 是否已經啟動所有Sub-agent？
    - 發配給Sub-agent的Fix Tasks是否足夠Atomization？
    - Fix Tasks之間的Dependencies是否已經被考慮？
  </questions>
  
  <checks>
    - [ ] 所有Sub-agent已經被啟動
    - [ ] 所有Sub-agent已經被發配任務
    - [ ] 所有Sub-agent已經被啟動
    - [ ] 發配給Sub-agent的Fix Tasks已經足夠Atomization
    - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="4: 製作dev-notes", level_of_think = "think hard", cache_read_budget = "not more than 190K tokens per request">
  - 根據Sub-agents的輸出結果，製作dev-notes
  - 使用Dev-notes Template製作dev-notes，並將其轉換為Markdown Format
  - 將dev-notes輸出至{output}
  </stage>

  <checks>
    - [ ] dev-notes製作完成
    - [ ] todo list更新完成
  </checks>
  </stage>
</workflow>

<examples>
# 項目檢查結果
- 問題：
  - ERR-1: xxx
  - ERR-2: yyy
  - ERR-3: zzz
  - ...
- 建議改進：
  - REC-1: xxx
  - REC-2: yyy
  - REC-3: zzz
  - ...

# 規範
- xxx
- yyy
- zzz

# 相關代碼片段
- xxx
- yyy
- zzz

# 修復任務
- xxx
- yyy
- zzz
</examples>

<example>
# 並行開發範例
此範例專注於指導如何透過識別依賴關係進行並行開發由此來提升開發效率。

## 任務列表
- 任務A
- 任務B
- 任務C
- 任務D
- 任務E

## 依賴關係
假設：
- 任務B依賴於任務A
- 任務D依賴於任務C
- 任務E沒有依賴關係

## 開發循環
1. 第一輪循環
  - 任務A
  - 任務C
  - 任務E
2. 第二輪循環
  - 任務B
  - 任務D

## 無並行開發（反面範例）
1. 第一輪循環
  - 任務A
2. 第二輪循環
  - 任務C
3. 第三輪循環
  - 任務E
4. 第四輪循環
  - 任務B
5. 第五輪循環
  - 任務D

由此可見，無並行開發的效率遠低於並行開發。
</example>