## Prompt 品質評估報告：review.md

### 待評估的 Prompt
**Input:**
````
<input>
  <context>
  1. {root}/docs/dev-notes/{task_id}-dev-notes.md
  2. {root}/docs/implementation-plan/{task_id}-plan.md
  3. {root}/sunnycore/templates/review-tmpl.yaml
  4. {root}/sunnycore/CLAUDE.md
    - QA rules
  </context>
  <templates>
  1. review-tmpl.yaml
  2. dev-notes-tmpl.yaml
  </templates>
</input>

<output>
1. {root}/docs/review-results/{task_id}-review.md
2. {root}/docs/tasks.md
</output>

<constraints, importance = "Important">
- Must produce machine-checkable Markdown with sections: Overview, Findings, Risks, Action Items.
- Must cross-reference plan/code/notes with file paths, line ranges, or anchors when available.
- Must prioritize requirement mismatches and critical defects over style issues.
- Should keep each finding concise (<= 120 words) and one issue per bullet.
- Must record an acceptance decision with rationale: Accept / Accept with changes / Reject.
</constraints>

<example>
Minimal review result outline:

# Overview
- Scope: ...
- Decision: Accept with changes — rationale: ...

# Findings
- Issue: ...
- Evidence: ...
- Impact: ...
- Recommendation: ...

# Risks
- ...

# Action Items
- [P1] ...
</example>

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
- [ ] stage 1: Review the plan
- [ ] stage 2: Review the code
- [ ] stage 3: Review the dev notes
- [ ] stage 4: Produce the results
</example>

<workflow, importance = "Important">
  <stage id="0: plan-todos">
  <tools: todo-list>
  - Read all working steps
  - Take reference from the example and create a todo item 
  </tools: todo-list, sequential-thinking>
  </stage>

  <stage id="1: review-plan">
  <tools: sequential-thinking>
  - Read and understand the implementation plan
  - Identify verification approach and success criteria
  </tools: sequential-thinking>

  <questions>
  - Are acceptance criteria complete, testable, and measurable?
  - Are assumptions, risks, and rollback strategies explicitly stated?
  </questions>
  </stage>

  <stage id="2: review-code">
  <tools: sequential-thinking>
  - Read and understand the code
  - Check alignment with the plan and the requirements
  - Run tests to verify the code
  </tools: sequential-thinking>
  
  <questions>
  - Do tests cover critical paths, edge cases, and regressions?
  - Are security, performance, and observability concerns addressed?
  </questions>
  </stage>

  <stage id="3: review-dev-notes">
  <tools: sequential-thinking>
  - Read and understand the development notes
  - Check alignment between notes and implementation
  </tools: sequential-thinking>
  </stage>

  <stage id="4: produce-results">
  - Use the template to create the markdown formatted review results
  - Save to {root}/docs/review-results/{task_id}-review.md
  - If there is already an existing review results, update the review results with the new information
  <checks>
  - [ ] All required sections present and consistent
  - [ ] Findings reference plan/code/notes with links or anchors
  - [ ] Acceptance decision recorded with rationale
  - [ ] Action items prioritized and assignable
  </checks>
  </stage>
</workflow>
````
---

### 評估結果

#### 分數計算
1. **正確性 (Correctness)**: 92 分
2. **清晰度與可執行性 (Clarity & Actionability)**: 92 分  
3. **理解負荷與歧義控制 (Cognitive Load & Ambiguity Control)**: 90 分
4. **推理引導適切性 (Reasoning Guidance Appropriateness)**: 92 分
5. **對齊性與相關性 (Alignment & Relevance)**: 96 分
6. **信息完整性與最小充分性 (Completeness & Minimality)**: 90 分
7. **約束設計適切性 (Constraint Design)**: 93 分
8. **用戶體驗 (User Experience)**: 91 分

**總分：92.0 分 / 100 分** *(8 個維度的平均分；預設等權重，可按場景加權)*

#### 品質等級
- **卓越 (Excellent)**

---

### 評分提示（常見誤用的糾偏）
- 語言或推理越長並不代表更好。以「能否準確完成任務」為最高準則。
- 過多的欄位、步驟與約束不是優點。僅保留提升結果品質的必要項。
- 優先把「思考過程」轉為「可驗證的標準/輸出格式」，而非要求冗長思維鏈。

---

### 優勢
- **輸出可驗證導向**：要求產出「machine-checkable Markdown」並固定段落（Overview/Findings/Risks/Action Items），利於一致化與後續自動檢核。
- **風險優先級明確**：強調需求落差與關鍵缺陷優先於風格問題，並限制每則 finding 篇幅與聚焦一議題，提升訊噪比。
- **跨文件追溯性**：要求以路徑、行號或錨點交叉引用計畫/程式/筆記，有助於證據化與審計。
- **分階段工作流**：從計畫、程式、開發筆記到產出收斂（含 checks），促進可重複的審查節奏與 DoD。
- **示例與轉換規則**：提供最小審查大綱與 Markdown 轉換規則、TODO 範例，降低首次執行歧義。
- **決策必填**：強制記錄 Accept/Accept with changes/Reject 與理由，支援治理決策。

### 改進建議（依優先序）
1. **機器可驗證 Schema（必要）**：為 review 結果定義可解析的結構（front matter 或 JSON sidecar），欄位如 `{ task_id, scope, decision, findings[{issue,evidence,impact,recommendation,refs}], risks[{id,severity}], actions[{id,priority,owner,due_date}] }`，並提供驗證規則與失敗處置。
2. **路徑解析與目錄保證（必要）**：規定 `{root}` 解析順序（環境變數→workspace fallback）、在寫入前 `mkdir -p`，並定義無權限/不存在時的錯誤格式（如 `E_ROOT_NOT_FOUND|E_WRITE_DENIED`）。
3. **`task_id` 命名規則（必要）**：限定字元集與長度（例如 `[A-Za-z0-9._-]{1,64}`），避免產物檔名不一致。
4. **`docs/tasks.md` 契約（必要）**：明確該檔的資料模型（欄位、表格欄位或章節 anchor）與更新策略（覆寫/追加/排序）。
5. **完成定義與閾值（建議）**：在各 stage 添增 DoD（如測試通過報表、關鍵路徑/邊界條件覆蓋、必要的安全/性能檢核），並給出最小門檻（例：coverage ≥ 80%、零重大缺陷）。
6. **錯誤處理（建議）**：規範化錯誤輸出 `{ type, code, message, hints, retryable }` 與常見錯誤枚舉（檔案缺失、模板不存在、schema 不符）。
7. **模板存在與回退（建議）**：在使用 `{root}/sunnycore/templates/review-tmpl.yaml` 前進行存在性/版本檢查，提供 fallback 與相容策略。
8. **觀測性（建議）**：記錄可觀測日誌鍵（`event,start_ts,end_ts,duration_ms,status,error_code`），方便自動化追蹤。
9. **語言與非互動模式（建議）**：固定輸出語系為繁中並保留 English technical terms，並假設非互動（deterministic）模式以提升穩定性。
10. **錨點規範（建議）**：對 findings 的引用格式（`path:start-end#anchor`）與多證據列舉方式給出統一樣式，利於機器解析。
11. **Dry-run 模式（可選）**：提供 `--validate-only` 以檢核輸入與預期產物清單而不落地。

---

### 備註
- 本評估以「達成任務效果」與「最小充分性」為原則；以上建議可在不改變既有角色/流程定位下，以增量方式落地。
