# Prompt 品質評估報告：brownfield-tasks.md

## 待評估的 Prompt
**Input:**
````
<input>
  <context>
    1. Implementation plan document: {root}/docs/implementation-plan/{task_id}-plan.md
    2. Review results document: {root}/docs/review-results/{task_id}-review.md
  </context>
  <templates>
    1. Development notes template: {root}/sunnycore/templates/dev-notes-tmpl.yaml
  </templates>
</input>

<output>
  1. Code fixes implemented based on review findings
  2. Comprehensive development notes: {root}/docs/dev-notes/{task_id}-dev-notes.md
</output>

<constraints, importance = "Important">
  - Changes must be minimal, reversible, and scoped to identified issues
  - Preserve existing architecture, public APIs, and naming conventions; justify any new dependency in plan/dev-notes
  - Add or update tests to cover each fix/action and run tests after every change
  - Follow project style and lint rules; avoid unrelated reformatting or file churn
  - Keep todos updated per stages and record decisions/risks in the development notes
</constraints>


<example>
markdown文件輸出方式：
	•	YAML 第一層 key 轉換為 Markdown 一級標題 (#)
	•	YAML 第二層 key 轉換為 Markdown 二級標題 (##)
	•	YAML 第三層 key 轉換為 Markdown 三級標題 (###)
	•	YAML value（字串或數字） 轉換為 Markdown 正文文字
</example>

<example>
todo list example:
- [ ] stage 0: Create a todo list
- [ ] stage 1: Analyse the current issues
- [ ] stage 2: Fix the issues
- [ ] stage 3: Enact recommended actions
- [ ] stage 4: Create a development notes
</example>

<workflow, importance = "Normal">
  <stage id="0: Create a todo list">
  <tools: todo-list>
  - Read this file end-to-end
  - Enumerate all stages and sub-steps
  - Take reference from the example and create a todo item 
  </tools: todo-list>

  <questions>
  - Have all steps been enumerated without omission?
  - Are todos atomic and actionable?
  - Is naming consistent with project conventions?
  </questions>
  </stage>

  <stage id="1: Analyse the current issues">
  <tools: sequential-thinking>
  - Read the review results document
  - Analyse current issues and root causes
  - Define the minimal effective fix for each issue
  </tools: sequential-thinking>

  <questions>
  - What are the root causes vs symptoms?
  - Which fixes have highest risk or impact?
  - Do we need design changes or refactors?
  </questions>
  </stage>

  <stage id="2: Fix the issues">
  <tools: todo-list>
  - Update the todo list with concrete steps per solution
  - Implement fixes iteratively, one at a time
  - Run and pass tests after each fix
  </tools: todo-list>

  <questions>
  - Is each change minimal and reversible?
  - Do tests cover the fixed behavior?
  - Any regression risks identified?
  </questions>
  </stage>

  <stage id="3: Enact recommended actions">
  <tools: todo-list>
  - Update the todo list with sequenced steps for the recommended actions
  - Enact the recommended actions iteratively
  - Run and pass tests after each action
  </tools: todo-list>
  
  <questions>
  - Are recommendations prioritized by value/effort?
  - Are acceptance criteria met per action?
  - Do changes align with architecture guidelines?
  </questions>
  </stage>

  <stage id="4: Create a development notes">
  - Conclude the development process and create development notes based on the template
  - If there is already an existing development notes, update the development notes with the new information
  - Save the markdown dev-notes to the stated directory

  <questions>
  - Are decisions and trade-offs documented?
  - Are next steps and risks recorded?
  - Are links to plans and reviews included?
  </questions>
  </stage>

  <checks>
  - [ ] Questions provided (2-3) for each stage
  - [ ] Tests pass after each fix/action
  - [ ] Dev-notes created at {root}/docs/dev-notes/{task_id}-dev-notes.md
  - [ ] No scope creep; todos remain atomic
  </checks>
</workflow>
````
---

## 評估結果

### 分數計算
1. **正確性 (Correctness)**: 93 分
2. **清晰度與可執行性 (Clarity & Actionability)**: 93 分  
3. **理解負荷與歧義控制 (Cognitive Load & Ambiguity Control)**: 90 分
4. **推理引導適切性 (Reasoning Guidance Appropriateness)**: 92 分
5. **對齊性與相關性 (Alignment & Relevance)**: 96 分
6. **信息完整性與最小充分性 (Completeness & Minimality)**: 91 分
7. **約束設計適切性 (Constraint Design)**: 93 分
8. **用戶體驗 (User Experience)**: 92 分

**總分：92.5 分 / 100 分** *(8 個維度的平均分；預設等權重，可按場景加權)*

### 評分提示（常見誤用的糾偏）
- 語言或推理越長並不代表更好。以「能否準確完成任務」為最高準則。
- 過多的欄位、步驟與約束不是優點。僅保留提升結果品質的必要項。
- 優先把「思考過程」轉為「可驗證的標準/輸出格式」，而非要求冗長思維鏈。

### 品質等級
- **卓越 (Excellent)**

---

## 優勢
- **階段化工作流清晰**：`stage 0 → 4` 分層推進，對應 `tools` 與 `questions`，利於原地盤點與迭代式落地。
- **可操作的約束條款**：要求變更「最小、可回滾、聚焦問題」，保留架構與公開 API，並強制測試與 lint 規範，降低風險。
- **輸入/輸出契約明確**：說明 `context/templates` 與最終產物（修復與 `dev-notes` 路徑），有助於自動化與可驗證性。
- **內建檢核清單**：`checks` 確保測試與產出到位，避免 scope creep，推動任務閉環。
- **示例可用性高**：提供 Markdown 轉換規則與 TODO 範例，降低執行歧義並提升一致性。
- **風險控制意識**：每次修復後皆需測試，且在 dev-notes 記錄決策/風險，強化可追溯性。
- **對褐地場景友好**：聚焦最小修補與既有設計對齊，避免大改動，提升在存量系統上的可行性。

## 改進建議
- **路徑與目錄保證**：明確規定在寫入 `{root}/docs/dev-notes/` 前需執行 `mkdir -p`，並說明無權限/路徑不存在時的處置（例：回傳結構化錯誤碼）。
- **命名與解析規則**：定義 `{task_id}` 的允許字元（如 `[A-Za-z0-9._-]{1,64}`）與衝突策略（覆寫/遞增後綴），避免檔名不一致。
- **工具行為約定**：補充 `tools: todo-list` 與 `tools: sequential-thinking` 的最小行為契約（輸入/輸出、前後置條件），便於自動器落地。
- **分階段完成定義**：對每個 `stage` 增補可驗證的完成條件（Definition of Done），例如「已更新 TODO、已附證據、測試通過截圖/報表」。
- **錯誤處理與回報**：規範化錯誤格式（`{ type, code, message, hints, retryable }`），枚舉常見錯誤（檔案缺失、模板不存在、測試失敗）。
- **模板存在性檢查**：在使用 `{root}/sunnycore/templates/dev-notes-tmpl.yaml` 前進行存在性與 schema 檢查，提供 fallback 或清晰錯誤。
- **測試執行標準**：補充測試啟動指令與最低門檻（例如 coverage ≥ 80%），並要求每次修復後附測試輸出摘要。
- **版本與相容策略**：為此工作流規格提供 `spec_version` 與變更說明，確保升級相容與歷史可追蹤。
- **Dry-run 模式**：新增 `--validate-only`/dry-run，以便先驗證輸入與即將產生的檔案清單而不落地，降低失敗成本。
- **時序與並行策略**：聲明可並行與必須串行的步驟，避免在多修復線時出現衝突或測試競態。
- **在地化與語系**：若面向多語專案，建議固定回應語系（如繁中 + 保留 English technical terms）以維持溝通一致性。

---

## 備註
- 本評估遵循「達成任務效果」與「最小充分性」原則；上述建議皆為增量優化，無需改變既有角色或流程定位，即可提升可操作性與可驗證性。
