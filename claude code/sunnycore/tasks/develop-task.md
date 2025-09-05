<input>
  <context>
  1. {project_root}/docs/specs/requirements.md
  2. {project_root}/docs/specs/task.md
  3. {project_root}/docs/specs/design.md
  4. {project_root}/docs/implementation-plan/{task_id}-plan.md
  </context>
  <templates>
  1. {project_root}/sunnycore/templates/dev-notes-tmpl.yaml
  </templates>
</input>

<output>
1. {project_root}/docs/dev-notes/{task_id}-dev-notes.md
2. 優質的代碼實踐
3. 實踐等級(bronze/silver/gold/platinum)
4. 實踐分數(1-5)
</output>

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

  <stage id="1: 上下文驗證", level_of_think = "think", cache_read_budget = "not more than 190K tokens per request">
  - 閱讀所有輸入文件
  - 驗證所有輸入文件存在
  </stage>

  <checks>
    - [ ] 所有輸入文件閱讀完成
    - [ ] 所有輸入文件驗證完成
    - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="2: 分析實作計劃", level_of_think = "Ultra think", cache_read_budget = "not more than 190K tokens per request">
  - 閱讀、並使用sequential-thinking工具分析實作計劃
  - 分析實作計劃的每一個功能性需求與非功能性需求(F-1,N-1)
  - 對這些需求以及實作計劃進行分類處理，判斷其開發任務類別
  </stage>

  <checks>
    - [ ] 實作計劃分析完成
    - [ ] 實作計劃需求已經被分類處理
    - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="3: 構建上下文", level_of_think = "think hard", cache_read_budget = "not more than 190K tokens per request">
  - 使用claude-context工具索引需要被修改的部分
  - 查看subagent-list獲取所有可調用的子agent
  - 使用sequential-thinking工具思考開發任務之間的依賴性
  - 分辨可並行的任務和不可並行的任務，參考相關範例來發配任務給對應的子agent
  - 將實作計劃以及實際情況、需求、規範進行整合，根據範本樣式發送給對應開發任務的子agent
  - 同時啟動所有被呼叫的子agent

  <questions>
    - 構建的上下文是否符合實作計劃？
    - 構建的上下文是否符合需求？
    - 構建的上下文是否符合規範？
    - 是否已經將所有上下文傳遞給所有子agent？
    - 是否已經為所有子agent發配任務？
    - 是否已經啟動所有子agent？
    - 發配給子agent的開發任務是否足夠原子化？
    - 開發任務之間的依賴性是否已經被考慮？
  </questions>
  
  <checks>
    - [ ] 所有子agent已經被啟動
    - [ ] 所有子agent已經被發配任務
    - [ ] 所有子agent已經被啟動
    - [ ] 發配給子agent的開發任務已經足夠原子化
    - [ ] todo list更新完成
  </checks>
  </stage>

  <stage id="4: 製作dev-notes", level_of_think = "think hard", cache_read_budget = "not more than 190K tokens per request">
  - 根據subagents的輸出結果，製作dev-notes
  - 使用dev-notes-tmpl.yaml模板製作dev-notes，並將其轉換為markdown格式
  - 將dev-notes輸出至{output}
  </stage>

  <checks>
    - [ ] dev-notes製作完成
    - [ ] todo list更新完成
  </checks>
  </stage>
</workflow>

<examples>
# 實作計劃
- 功能性需求：
  - F-1: xxx
  - F-2: yyy
  - F-3: zzz
  - ...
- 非功能性需求：
  - N-1: xxx
  - N-2: yyy
  - N-3: zzz
  - ...

# 規範
- xxx
- yyy
- zzz

# 相關代碼片段
- xxx
- yyy
- zzz

# 開發任務
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