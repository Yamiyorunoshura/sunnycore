# 統一任務規劃工作流程
<workflow type="unified-task-planning">

## 強制前置條件驗證
<mandatory-preconditions>

### 1. 載入專案規範與上下文
<stage name="載入專案規範與上下文" number="1" critical="true">
- **描述**: 完整閱讀 `{project_root}/docs/specs/` 中的所有文檔，建立任務 `{task_id}`(如`1`, `2`, `3`...)`(如`1`, `2`, `3`...) 的完整上下文。
- **要求**:
  <requirements>
  <think hard>
  - 解析需求、架構、相依關係與限制條件
  - 匯總對 `{task_id}`(如`1`, `2`, `3`...)`(如`1`, `2`, `3`...) 的明確目標與非功能性要求
  - 輸出關鍵依據清單，確保後續計劃可追溯
  <think hard>
  </requirements>
- **驗證檢查**:
  <validation_checkpoints>
  - [ ] `{project_root}/docs/specs/` 可讀且已完整掃描
  - [ ] `{task_id}`(如`1`, `2`, `3`...)`(如`1`, `2`, `3`...) 在需求中有明確對應
  - [ ] 已形成初步上下文摘要（1-3 句）
  </validation_checkpoints>
</stage>

### 2. 載入實施計劃模板
<stage name="載入實施計劃模板" number="2" critical="true">
- **模板路徑**: `/Users/tszkinlai/Coding/AI workflow/core/dev/templates/implementation-plan-tmpl.yaml`
- **描述**: 讀取並理解計劃模板結構與欄位定義，作為後續規劃輸入。
- **要求**:
  <requirements>
  <think>
  - 確認 metadata/context/objectives/scope/approach/test_strategy/quality_gates 等區段完整性
  - 建立需求項與計劃項目的可追溯映射（如 F-IDs, N-IDs）
  <think>
  </requirements>
- **關鍵檢查點**:
  <critical-checkpoint>
  - 若模板不可讀或缺失，立即停止並回報
  </critical-checkpoint>
</stage>

</mandatory-preconditions>

---

## 規劃執行協議
<execution-protocol>

### 3. 建立實施計劃初稿（YAML）
<stage name="建立實施計劃初稿（YAML）" number="3" critical="true">
- **輸入**: 來自 specs 的上下文、相依與品質門檻
- **動作**:
  <plan-drafting>
  <think hard>
  - 填寫 `metadata`（含 `{task_id}`(如`1`, `2`, `3`...)`、`{project_root}`、來源清單與日期）
  - 於 `objectives` 中列出功能/非功能需求與可測量指標
  - 明確 `scope` 的 in/out 與邊界假設
  - 在 `approach` 中分解架構、模組、資料與遷移策略
  - 設定 `test_strategy` 與 `quality_gates`（例如覆蓋率與 p95）
  - 補齊 `risks`、`open_questions`、`dependencies`、`timeline`、`estimation`
  - 完成後不需要輸出文件。
  <think hard>
  </plan-drafting>
- **驗證檢查**:
  <validation_checkpoints>
  - [ ] 每個需求項均有對應計劃與驗收準則
  - [ ] 風險具備緩解與應急方案
  - [ ] 測試與品質門檻具體、可量測
  </validation_checkpoints>
</stage>

### 4. 計劃品質驗證（內審）
<stage name="計劃品質驗證（內審）" number="4" critical="true">
- **持續驗證**:
  <quality-validations>
  <think harder>
  - 一致性：需求、設計、測試、驗收條件彼此對齊
  - 完整性：無缺漏欄位，所有關鍵模組均覆蓋
  - 可測量性：門檻與 KPI 具體可測
  - 可追溯性：每個計劃項皆可追溯至來源文檔
  <think harder>
  </quality-validations>
- **驗證檢查**:
  <validation_checkpoints>
  - [ ] 追溯矩陣完成（F-IDs/N-IDs 對應）
  - [ ] 風險等級與緩解策略經複核
  - [ ] 測試策略覆蓋單元/整合/驗收/契約（如適用）
  </validation_checkpoints>
</stage>

</execution-protocol>

---

## 產出與存檔
<deliverables>

### 5. 格式轉換與輸出
<stage name="格式轉換與輸出" number="5" critical="true">
- **描述**: 在輸出前，將計劃從 YAML 轉換為 Markdown，並存檔。
- **動作**:
  <conversion>
  <think>
  - 轉換前執行 YAML 結構校驗（空值/必要欄位）
  - 轉換為 Markdown 後，檢查標題階層與清單渲染
  - 若支援自動工具，應使用非互動方式完成轉換
  <think>
  </conversion>
- **輸出路徑**:
  <paths>
  - `{project_root}/docs/implementation-plan/{task_id}`(如`1`, `2`, `3`...)-plan.md`
  </paths>
- **驗證檢查**:
  <validation_checkpoints>
  - [ ] 轉換後 Markdown 可讀且段落完整
  - [ ] 文件已正確存至指定路徑
  - [ ] 封面中含 `{task_id}`(如`1`, `2`, `3`...)`、日期與版本資訊
  </validation_checkpoints>
</stage>

</deliverables>

---

## 失敗處理機制
<failure-handling>
| 失敗情境 | 處理動作 |
|---------|---------|
| **模板缺失/不可讀** | 立即停止，報告並請求補齊模板 |
| **規範不可讀** | 停止並回報；不得以過時或不完整資訊規劃 |
| **關鍵欄位缺漏** | 標記高風險，補齊後方可進入輸出 |
| **轉換失敗** | 修復 YAML 結構或工具設定，重試至成功 |

<critical-failures>
**任何關鍵失敗都必須立即停止流程並報告**
</critical-failures>

</failure-handling>

---

## 附錄：參考路徑與模板
<appendix>
- 模板：`/Users/tszkinlai/Coding/AI workflow/core/dev/templates/implementation-plan-tmpl.yaml`
- 規範：`{project_root}/docs/specs/`
- 計劃輸出：`{project_root}/docs/implementation-plan/{task_id}`(如`1`, `2`, `3`...)-plan.md`
</appendix>

</workflow>
1. 完整閱讀`{project_root}/docs/specs/`中的所有文檔，並理解整個項目的架構以及{task_id}`(如`1`, `2`, `3`...)對應的需求
2. 讀取模板`Users/tszkinlai/Coding/AI workflow/core/dev/templates/implementation-plan-tmpl.yaml`
3. 依據模板填入開發計劃，並將其保存到`{project_root}/docs/implementation-plan/`中，文件名為`{task_id}`(如`1`, `2`, `3`...)-plan.md`
4. 在輸出文檔前，必須將文檔從yaml格式轉換為markdown格式