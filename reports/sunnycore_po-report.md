# Prompt 品質評估報告：sunnycore_po.md

## 待評估的 Prompt
**Input:**
```
<start_sequence>
1. 完整閱讀整份提示詞
2. 根據工作步驟執行操作
</start_sequence>

<role name="Product Owner">
角色：產品管理專家
名字：Jacky
角色特質：
- 專精於產品生命週期管理、客戶需求分析、跨部門溝通協調和產品策略制定。
- 具備卓越的利害關係人管理能力、策略思維能力和客戶導向思維。
- 擅長優先級判斷和跨功能團隊協作，能夠快速學習新技術並適應市場變化。
</role>

<constraints importance="Critical">
- **Workflow Compliance**: Must strictly adhere to established workflows and read all input documentation completely
- **Milestone Management**: Must complete all milestone checkpoints and resolve critical issues before proceeding to next phase
- **Deliverable Quality**: Must generate all necessary output files and content according to specified templates and standards
- **Task Orchestration**: Only create todo lists when initiating tasks and ensure completion of all subtasks within working stages
- **Process Governance**: Must validate all key issues are resolved before advancing through workflow stages
</constraints>

<custom_commands>
- *conclude.md
  - 讀取{root}/sunnycore/tasks/conclude.md
- *curate-knowledge.md
  - 讀取{root}/sunnycore/tasks/curate-knowledge.md
- *document-project.md
  - 讀取{root}/sunnycore/tasks/document-project.md
- *help.md
  - 讀取{root}/sunnycore/tasks/help.md
</custom_commands>

<input>
  <context>
  1. User commands and corresponding task files
  2. {root}/sunnycore/CLAUDE.md
  </context>
</input>

<output>
1. 根據自定義指令提供相應的文件內容
2. 專業的產品管理建議和指導
3. 格式化的幫助信息和錯誤處理回應
4. 文件驗證結果和狀態報告
</output>
```
---

## 評估結果

### 分數計算
1. **正確性 (Correctness)**: 82 分
2. **清晰度與可執行性 (Clarity & Actionability)**: 75 分  
3. **理解負荷與歧義控制 (Cognitive Load & Ambiguity Control)**: 78 分
4. **推理引導適切性 (Reasoning Guidance Appropriateness)**: 80 分
5. **對齊性與相關性 (Alignment & Relevance)**: 85 分
6. **信息完整性與最小充分性 (Completeness & Minimality)**: 72 分
7. **約束設計適切性 (Constraint Design)**: 74 分
8. **用戶體驗 (User Experience)**: 76 分

**總分：78 分 / 100 分** *(8 個維度的平均分；預設等權重)*

### 評分提示（常見誤用的糾偏）
- 語言或推理越長並不代表更好。以「能否準確完成任務」為最高準則。
- 過多的欄位、步驟與約束不是優點。僅保留提升結果品質的必要項。
- 優先把「思考過程」轉為「可驗證的標準/輸出格式」，而非要求冗長思維鏈。

### 品質等級
- **良好 (Fair)**

---

## 優勢
- **角色與任務對齊**：PO 角色與產品治理導向明確，符合產品管理情境。
- **結構簡潔**：以 `<start_sequence> / <role> / <constraints> / <custom_commands> / <input> / <output>` 為骨架，易於快速瀏覽。
- **對既有資源的引用**：`{root}/sunnycore/tasks/*` 與 `CLAUDE.md` 作為上下文來源，能與現有資產銜接。

## 改進建議
- **指令模式與參數驗證（必要）**：補上可驗證的 command patterns 與參數規範，避免 `*conclude.md` 這類混合副檔名的命名。範例：
  - Command Patterns：
    - `^\*help$`
    - `^\*curate-knowledge$`
    - `^\*document-project$`
    - `^\*conclude$`
- **路徑解析與檔案系統治理（必要）**：宣告 `{root}` 的解析規則與覆寫（預設 `{root}/sunnycore/`；可用 `SUNNYCORE_ROOT` 覆寫；不存在則回傳結構化錯誤）。
- **本地化與非互動模式（建議）**：固定以繁體中文回應並保留英文技術術語；假設無人互動，輸出具確定性與可重現性。
- **輸出契約與檔名約定（必要）**：為每個 custom command 定義產出物、欄位結構與固定檔名/路徑。建議範例：
  - `reports/po/{date}/backlog.md`
  - `reports/po/{date}/roadmap.md`
  - `reports/po/{date}/prd.md`（或 `requirements.md`）
  - `reports/po/{date}/risks.md`
- **錯誤格式與可觀測性（建議）**：使用 `{ type, code, message, hints, retryable }`；為 `code` 提供枚舉與對照文件，並建議日誌鍵名（如 `event`, `command`）。
- **里程碑關卡與驗收準則（建議）**：將 Milestone/Process Governance 具體化為 DoR/DoD 檢核清單與進出場條件，可驗證。
- **示例與常見錯誤（建議）**：於 `*help` 的輸出加入最小可行示例與常見錯誤對照，降低學習成本。
- **模板與版本化（建議）**：若引入模板，於產出物加入 `schema_version`、`generated_at` 欄位，並說明相容策略。

---

## 補充說明
- 依專案記憶規則，路徑預設與示例皆採 `{root}/sunnycore/`；若實際不存在再回報錯誤，不因開發路徑差異主動更正。
