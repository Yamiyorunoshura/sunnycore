# PO Conclude Task Execution Instructions

<task_metadata>
name: "PO Conclude Task Execution"
version: "2.0"
category: "po"
prompt_techniques: ["chain_of_thought", "self_discover", "markdown_structured", "multi_agent_coordination"]
quality_standards: ["evidence_based", "systematic", "comprehensive", "actionable", "markdown_only_output"]
<!-- task_metadata>

## 任務概述
當使用者呼叫 `*conclude` 指令時，請依據統一結案流程協調多代理同步與序列化執行，完成專案結案、文件產出與知識沉澱。

- **多代理協作目標**：與 `project-concluder`、`file-classifier`、`knowledge-curator`、`architecture-documenter` 協作。
- **遵循工作流程**：`{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.yaml`。
- **強制品質門檻**：遵守 `{project_root}/sunnycore/po/enforcement/project-concluder-enforcement.md`。
- **輸出規範**：所有對外文件必須為純 Markdown（禁止 XML 標籤出現在最終文件）。

## 執行步驟（SELF-DISCOVER 框架）

### Step 1: 需求理解與上下文建立（SELECT）
1. 識別 `*conclude` 指令意圖與輸出期望（完成報告、知識/架構文件、分類報告）。
2. 載入必要檔案與別名：
   - WORKFLOW_FILE → `{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.yaml`
   - REPORT_TEMPLATE → `{project_root}/sunnycore/po/templates/completion-report-tmpl.yaml`
   - ENFORCEMENT_FILE → `{project_root}/sunnycore/po/enforcement/project-concluder-enforcement.md`
3. 確認任務前置條件（QA 全通過、計畫可追溯、QA 反饋已收集或確認缺失）。

### Step 2: 載入強制規範（ADAPT）
1. 嚴格遵循 `project-concluder-enforcement.md` 的強制條款：
   - 決定論：固定參數（temperature=0, top_p=1, seed=42），穩定字典序輸出與路徑正規化。
   - 證據導向：所有結論需有可追溯證據（PR、commit、檔案、測試、量測）。
   - 模板一致：完成報告完全對齊模板結構，嚴禁 placeholder。
   - Markdown 規範：最終對外文件只允許 Markdown。
2. 若關鍵檔案缺失或前置檢查未通過，立即停止並回報阻斷原因（Fail-fast）。

### Step 3: 依工作流程建立策略（IMPLEMENT）
1. 參考工作流程的階段與動作，制定結案策略與證據蒐集計畫：
   - workflow_initialization → 載入 workflow 與模板並驗證可存取。
   - conclusion_strategy → 明確聚焦範疇與證據來源。
   - evidence_collection → 蒐集規格、計畫、實作與品質證據、QA 回饋、專案 Markdown 文檔分析。
   - delivery_synthesis → 對齊原始範疇、核對驗收標準與測試證據。
   - qa_problem_analysis → 萃取 QA 議題、紀錄狀態與風險。
   - enhancement_planning → 擬定後續增強與成功準則。
   - report_generation → 以模板產生完成報告（禁止 placeholder、需附證據）。
   - finalization → 讀回檢查、格式驗證、清理臨時文件。

### Step 4: 套用與協同執行（APPLY）
1. 並行階段（呼叫當下與 conclude 同步）：
   - `project-concluder`：產出結案核心分析與報告內容（最終輸出為 Markdown）。
   - `file-classifier`：執行檔案分類/清理，產出分類報告並回填風險與清理紀錄。
2. 序列階段（在報告生成後觸發）：
   - `knowledge-curator`：生成/更新 `{project_root}/docs/knowledge/engineering-lessons.md`。
   - `architecture-documenter`：生成/更新 `{project_root}/docs/architecture/architecture.md`。
3. 整合所有代理輸出，進行交叉一致性檢查（Cross-Agent Consistency）。

## 關鍵品質關卡（Quality Gates）
1. 輸入關卡：工作流程/模板/規範皆已載入且可讀；任務前置條件通過。
2. 證據關卡：完成報告中每一主張皆有具體證據鏈接（PR/commit/文件/測試/量測）。
3. 模板關卡：完全對齊模板結構，無 `< >`、`{}` 等 placeholder，使用實際值。
4. Markdown 關卡：最終對外文件無任何 XML 標籤，標題層級、清單、表格、程式碼區塊語法正確。
5. 一致性關卡：各代理輸出在範疇、名詞、路徑、度量與結論上相互一致。

## 產出與路徑
- 完成報告：`{{project_root}}/docs/completion-reports/{{task_id}}-completion.md`（純 Markdown）
- 知識沉澱：`{{project_root}}/docs/knowledge/engineering-lessons.md`
- 架構文件：`{{project_root}}/docs/architecture/architecture.md`
- 檔案分類報告：`{{project_root}}/docs/file-classification/file-classification-report.md`

## 失敗處理策略
- 關鍵檔案缺失/前置未過：立即停止並回報（blocker）。
- 證據不足：在報告中標記限制與補充計畫，不阻斷其他章節。
- 模板不合規：列出差異與修正計畫，要求補齊後再通過關卡。
- 並行協作衝突：記錄衝突、調整順序或輸入，確保資料一致性後重試。

## 最佳實踐（Prompt Engineering）
- 運用 Chain of Thought 於策略與整合決策，但最終輸出為 Markdown。
- 以 SELF-DISCOVER 結構驅動四步驟（SELECT/ADAPT/IMPLEMENT/APPLY）。
- 嚴守「XML 僅用於內部思考、最終輸出為 Markdown」原則。
- 全程證據導向，敘述附上具體檔案/PR/測試/量測連結與數值。
- 多代理協作時先平行後序列，並在整合時做一致性審核。

## 完成定義（DoD）
- 所有工作流程階段皆完成且有對應產出。
- 完成報告各章節已依模板填入實際內容且無 placeholder。
- 全部結論均可追溯到具體證據；品質關卡全部通過。
- 知識與架構文檔更新完成，檔案分類報告與清理紀錄已整合至完成報告。
- 臨時文件已清理，文件可交付利害關係人。


