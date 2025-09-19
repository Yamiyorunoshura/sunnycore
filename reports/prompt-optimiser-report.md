### Prompt 品質評估報告 — prompt-optimiser.md

#### 待評估的 Prompt
- 檔案：`prompt-optimiser.md`

---

### 分數計算
1. 正確性（Correctness）: 88 分
2. 清晰度與可執行性（Clarity & Actionability）: 94 分  
3. 理解負荷與歧義控制（Cognitive Load & Ambiguity Control）: 92 分
4. 推理引導適切性（Reasoning Guidance Appropriateness）: 93 分
5. 對齊性與相關性（Alignment & Relevance）: 97 分
6. 信息完整性與最小充分性（Completeness & Minimality）: 90 分
7. 約束設計適切性（Constraint Design）: 93 分
8. 用戶體驗（User Experience）: 92 分

**總分：92.4 分 / 100 分**（8 維度等權平均）

### 品質等級
- 卓越（Excellent）

---

### 評分提示（常見誤用的糾偏）
- 語言或推理越長不代表更好；以能否準確完成任務為最高準則。
- 過多欄位、步驟與約束不是優點；僅保留提升結果品質的必要項。
- 優先把「思考過程」轉為「可驗證的標準／輸出格式」，避免冗長思維鏈要求。

---

### 優勢
- 清晰結構與高可執行性：採用 `role / input / output / constraints / workflow / instructions / example` 的分層設計，並提供三階段工作流程與檢核清單，行動導向明確。
- 對齊任務目標：強調「報告一致性、結構規範、可驗證性與最小充分性」，與優化任務高度一致。
- 可驗證導向：在 `<workflow>` 的 validation 階段給出明確的勾選式檢核項，有助於穩定與可重複輸出。
- 擴充友好：明確指出需遵循《提示工程使用指南》，並支援 agents/commands/tasks 三種架構模板，便於在不同場景下複用。

---

### 改進建議（依優先序）
1. 明確化與強化輸出契約（提升：正確性、完整性、用戶體驗）
   - 問題：目前僅描述四項輸出，缺少「機器可判讀」的固定結構與檔名約定。
   - 建議：定義嚴格的輸出結構與檔名規範，包含欄位必填與型別說明；對於錯誤與例外輸出也給出固定格式。
   - 範例（建議片段）：
```xml
<deliverables>
  <analysis-report path="reports/{input_basename}-analysis.md" required="true" />
  <optimized-prompt path="optimized/{input_basename}.md" schema="agents|commands|tasks" required="true" />
  <improvement-summary path="reports/{input_basename}-improvements.md" required="true" />
  <self-check path="reports/{input_basename}-self-check.json" format="json" required="true" />
</deliverables>
```

2. 完整 XML 結構與根元素（提升：正確性、清晰度）
   - 問題：目前文件以多個頂層節點呈現，若需機器解析，建議添加單一根元素與版本資訊。
   - 建議：以單一根元素包裹，提供 `id`、`version`、`language` 與 `target-quality` 等中繼資料。
   - 範例：
```xml
<prompt-spec id="prompt-optimiser" version="1.0" language="zh-Hant" target-quality="Excellent">
  <!-- 既有 role/input/output/constraints/workflow/instructions/example 節點置於此 -->
</prompt-spec>
```

3. 強化錯誤處理與回退流程（提升：用戶體驗、完整性）
   - 問題：若評估報告缺失、格式不符或內容不足，缺少明確回應機制。
   - 建議：在 validation 階段加入錯誤輸出契約與回退策略（如最小可行優化、需人工補件清單）。
   - 範例：
```xml
<errors>
  <error code="E-MISSING-REPORT" action="request-attachment">缺少評估報告，請提供 reports/{input_basename}-report.md</error>
  <error code="E-SCHEMA-MISMATCH" action="fallback-minimal">評估報告格式不符，將僅套用必要優化清單</error>
</errors>
```

4. 指令與限制更具體可檢驗（提升：約束設計、清晰度）
   - 建議將關鍵約束改為可量化條款，例如：
   - 「輸出應包含 3–5 條可驗證約束，每條以動詞開頭並具有具體檢核條件」
   - 「單一回應字元上限與各段落最大長度」
   - 「所有輸出一律使用 Chinese-traditional」

5. 提供更具體的樣例與通用骨架（提升：清晰度、用戶體驗）
   - 問題：`<example>` 中「（完整優化內容）」為佔位符，示例不易直接套用。
   - 建議：補充一份可直接複製使用的「最小可行」優化後提示詞骨架，並對 agents/commands/tasks 三類各給一例。

6. 增補版本與追溯中繼資料（提升：對齊性、完整性）
   - 建議：在輸出中加入 `source-report-path`、`optimiser-version`、`timestamp`、`hash` 等欄位，便於審計與回溯。

7. 工具使用與禁止事項（提升：正確性、風險控管）
   - 建議：在 `<tools>` 明確列出允許的工具與禁用操作（如不得執行有副作用的命令、不得寫入非指定路徑）。

---

### 備註
- 本評估以「達成任務效果」為核心，偏好可驗證、可執行且最小充分的設計；建議皆可在不改變原始角色定位下以漸進式方式落地。
