## 1. 簡介 (Introduction)

本專案旨在重構既有的 AI 多 Agent 協作工作體系之規範與流程文件，使其由「自然語言描述」全面轉為以 Midscene 結構化 API 為核心的可驗證、可維護、可追蹤之規格。重構範圍包含 `core/`（規範）、`templates/`（輸出模板）與 `workflow/`（作業流程），以 `ai-api.md` 與 `ai-api-convertion.md` 所述觀念為依據，將指令、資料擷取、等待/同步、驗證等行為以結構化方式定義，降低歧義並提升可重複性與穩定性。

目標：
- 以可測試的「行為動詞 + 定位/參數 + 預期輸出」取代含糊的自然語言敘述。
- 將資料擷取改以型別化需求（string/number/JSON/array）描述，落實可驗證的輸出契約。
- 將等待/同步、重試/錯誤處理、報告/觀測等面向納入統一文件規範。

範圍：
- In-scope：`core/`、`templates/`、`workflow/` 文件重構。
- Out-of-scope（本次不變更）：`agents/` 的角色定義、`commands/` 的調用入口（可在後續迭代納入）。

---

## 2. 需求 (Requirements)

### 需求 1：核心規範（core）重構為結構化 API 準則

**使用者故事：** 作為 規範制定者/維護者，我希望以結構化 API 定義互動與資料擷取規則，以便各 Agent 產出的流程可被一致地執行、驗證與維護。

#### 驗收標準

```
1. 當審視 `core/` 底下各 `*-developer-enforcement.md` 文件時，系統應包含以下章節：
   - 互動動作（aiTap/aiInput/aiScroll/aiHover/aiRightClick/aiKeyboardPress）
   - 資料擷取（aiQuery/aiBoolean/aiNumber/aiString/aiAsk）
   - 等待與同步（aiWaitFor 及 sleep 的適用情境、Timeout/Interval 規範）
   - 驗證與斷言（aiAssert 與以 `aiQuery + 標準斷言` 的替代規範）
   - 元素定位（aiLocate 與 xpath 的使用規範）
   - 腳本執行（runYaml 的適用邊界）
   - 頁面上下文凍結（freezePageContext/unfreezePageContext 的使用限制）
   - 截圖與報告（logScreenshot、reportFile 的最低要求）
   - 環境與執行參數（模型/DEBUG/MIDSCENE_RUN_DIR/replanning limit 等設定應如何於文件中被宣告）
2. 當文件提及 `aiAction` 時，系統應明確規範其僅適用於簡單或低風險的單步驟需求；遇到複雜條件/迴圈/分支，系統應要求改寫為結構化 API（參照 `ai-api-convertion.md` 指引）。
3. 當在 `core/` 搜尋自然語言型流程詞彙（如「然後」「接著」「最後」）時，系統應不得在「動作定義」區塊中出現此類自由敘事；若出現，應改為動詞 + 定位/參數的條列式結構。
4. 當需要等待頁面狀態變化時，系統應規定優先以 `aiWaitFor` 撰寫可驗證的條件；若成本考量需使用 sleep，文件應標示為例外並說明風險。
5. 當需要精準定位元素時，系統應規定先使用 xpath（若可得），再回退至快取與 AI 定位；`deepThink` 僅於辨識困難時使用並需文件說明。
```

### 需求 2：模板（templates）以可執行/可驗證欄位重構

**使用者故事：** 作為 任務執行開發者/審查者，我希望所有輸出模板（plan/review/implementation/validation/handover）皆以結構化欄位呈現，以便我可以直接依欄位執行或驗證成果。

#### 驗收標準

```
1. 當檢視 `templates/` 中的各模板（如 `implementation-plan-tmpl.yaml`、`review-tmpl.yaml`、`plan-validation-report-tmpl.yaml`、`completion-report-tmpl.yaml`、`handover-docs-guidance.md`）時，系統應至少包含下列欄位：
   - 前置環境（模型/環境變數/必要權限/瀏覽器或裝置前提）
   - 輸入（任務描述、限制、假設）與 輸出（可驗證之資料格式/檔案/報表）
   - 資料擷取需求（以型別化描述，例如：`string[]`、`number`、`{...}`、`{...}[]`）
   - 互動步驟（每步包含：動詞、定位描述或 xpath、必要 options，如 deepThink/xpath/cacheable）
   - 驗證項目（以可機器驗證之斷言描述，不得以自由敘事替代）
   - 等待條件（條件敘述 + timeout/check interval）
   - 錯誤處理與重試（最大重試次數、退避策略、降級方案）
   - 記錄與截圖（何時 `logScreenshot`、報表存放路徑或連結）
2. 當檢視任一模板之「互動步驟」時，系統應使用限定動詞集合（aiTap/aiInput/aiScroll/aiHover/aiRightClick/aiKeyboardPress），不得以「然後/接著」串接段落式文字。
3. 當檢視「資料擷取需求」時，系統應以 `aiQuery/aiString/aiNumber/aiBoolean/aiAsk` 可滿足之型別/結構描述表達，不得出現「拿到大概的資訊」等不可測試描述。
4. 當檢視「驗證項目」時，系統應使用可判定真偽的描述；若可能受 AI 幻覺影響，文件應提供以 `aiQuery + 標準斷言` 的替代策略。
```

### 需求 3：工作流程（workflow）階段化與可追蹤化

**使用者故事：** 作為 子代理（subagent）維護者，我希望各工作流程以固定階段（感知/規劃/執行/驗證/觀測與收斂）呈現，以便流程可被審核、度量與持續改善。

#### 驗收標準

```
1. 當檢視 `workflow/` 中各統一流程（如 `unified-developer-workflow.yaml`、`unified-task-planning-workflow.yaml`、`unified-review-workflow.yaml`、`unified-plan-validation-workflow.yaml`、`unified-project-concluding-workflow.yaml`）時，系統應將流程拆解為：
   - 感知（Perceive）：以 `aiQuery/aiAsk` 萃取上下文與需求
   - 規劃（Plan）：以結構化步驟/資料需求/驗證目標產出計畫
   - 執行（Act）：以限定動詞集合執行互動
   - 驗證（Validate）：以 `aiAssert` 或 `aiQuery + 標準斷言` 驗證輸出
   - 觀測與收斂（Observe & Conclude）：以 `logScreenshot` 與報告彙整結果
2. 當流程需要等待狀態變更時，系統應使用 `aiWaitFor` 定義可觀測條件與 `timeoutMs/checkIntervalMs`；不得僅以自由敘事要求「等待一下」。
3. 當流程含大量並行查詢時，系統應允許以「頁面上下文凍結」策略（freeze/unfreeze）包覆查詢區段，並於文件明訂限制（不得在互動步驟內使用、需及時解凍）。
4. 當流程包含失敗重試時，系統應文件化最大重試次數與退避策略；若持續失敗，應記錄並轉交審查（包含報告與截圖）。
```

### 需求 4：自然語言到結構化之轉換規則與覆蓋率

**使用者故事：** 作為 文件重構執行者，我希望有明確的自然語言→結構化映射規則與完成標準，以便能高效率且一致地完成改寫。

#### 驗收標準

```
1. 當對 `core/`、`templates/`、`workflow/` 進行盤點時，系統應提供映射規則（至少包含）：
   - 「點擊/輕觸…」→ aiTap
   - 「輸入…於…」→ aiInput
   - 「滾動到…/向下滾動…」→ aiScroll（direction/scrollType/distance 應被明確化）
   - 「滑過/懸停於…」→ aiHover
   - 「右鍵點擊…」→ aiRightClick
   - 「按下鍵盤…」→ aiKeyboardPress
   - 「檢索/擷取…資料」→ aiQuery（以型別化格式定義輸出）
   - 「是否存在/是否為真」→ aiBoolean
   - 「擷取數量/數值」→ aiNumber
   - 「擷取文字/字串」→ aiString
   - 「詢問/解答…」→ aiAsk
   - 「等待直到…成立」→ aiWaitFor（含 timeout/checkInterval）
   - 「驗證…」→ aiAssert 或 `aiQuery + 標準斷言`
   - 「定位元素…」→ aiLocate（優先 xpath）
   - 「以 YAML 自動化…」→ runYaml
   - 「截圖/保存畫面」→ logScreenshot
2. 當完成改寫後，系統應達成 100% 覆蓋（不留自然語言型流程陳述）；抽樣檢視各文件之「動作/資料/驗證/等待」章節，不得出現段落式自由敘事。
3. 當遇到 `aiAction` 的多步驟自然語言提示時，系統應提供對應拆解示意（以結構化步驟/查詢/判斷/迴圈方式重構），並於文件中標註替代策略與風險差異。
```

### 需求 5：同步、等待與錯誤處理策略標準化

**使用者故事：** 作為 工作流程設計者，我希望等待條件、超時、重試與降級策略可被明確文件化，以便降低偶發性失敗並提升可預期性。

#### 驗收標準

```
1. 當定義等待條件時，系統應優先以 `aiWaitFor('可觀測的條件')` 表達，並要求標註 `timeoutMs` 與 `checkIntervalMs`；若以 sleep 取代，應附風險註記與使用限制。
2. 當發生互動失敗（如定位失敗/元素被遮擋）時，系統應文件化重試次數、退避策略（exponential/backoff）與降級行為（如改用 xpath、調整 deepThink）。
3. 當流程需要導航或多分頁時，系統應在文件中規範 `forceSameTabNavigation` 的預設行為與例外情境。
```

### 需求 6：可觀測性與報告（Logging/Report）

**使用者故事：** 作為 品質保證人員，我希望每個流程與輸出在報告中可追溯，並能快速定位失敗原因。

#### 驗收標準

```
1. 當流程進行關鍵步驟（前/後置檢查、失敗重試、驗證）時，系統應規範以 `logScreenshot(title, { content })` 留存；文件須定義至少在關鍵節點需截圖之清單。
2. 當產出報告時，系統應能提供 reportFile 路徑或連結，並於模板中預留欄位（例如「執行報告」）。
3. 當需要分析成本/效能時，系統應文件化如何以 `DEBUG=midscene:ai:profile:stats` 觀測每次 AI 呼叫資訊；必要時提供 `MIDSCENE_RUN_DIR` 客製化輸出位置的欄位。
```

### 需求 7：治理（Governance）與品質門檻

**使用者故事：** 作為 專案管理者，我希望以文件層級的檢核與門檻避免回歸到自然語言敘事，確保長期一致性。

#### 驗收標準

```
1. 當提交對 `core/`、`templates/`、`workflow/` 的變更時，系統應提供 PR 檢核清單（Checklist），至少覆蓋：
   - 是否僅使用允許之動詞集合定義互動
   - 是否以型別化格式描述資料擷取
   - 是否將等待條件以 `aiWaitFor` 定義
   - 是否提供驗證項目與可機器判定的成功準則
   - 是否補充必要的截圖/報告欄位
2. 當進行文件審查時，系統應阻擋含段落式自由敘事的「動作/資料/驗證/等待」章節之合併，直到改為結構化條列。
3. 當需新增例外（如允許 `aiAction` 作為主流程），系統應要求於文件明確標註例外理由、失敗風險與替代方案。
```
