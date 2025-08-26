# Refactor Developer 強制執行規範

<core_execution_protocol>
## 核心執行協議

<prerequisite_conditions>
### 必要前置條件（寬鬆）
- **建議**：開始前載入統一工作流程與計劃；若缺失，於 dev_notes.validation_warnings 記錄並持續
- **工作流程讀取**：應讀取 `~/cursor-claude/core/dev/workflow/refactor-developer-workflow.md`，失敗則記錄警告
- **計劃檢查**：嘗試定位並讀取 task_id 的實施計劃；如缺失，記錄警告並以最小上下文繼續
</prerequisite_conditions>

<behavioral_equivalence>
### 行為對等性（絕對強制）
- **功能不變**：絕對不能改變任何外部行為
- **API保持**：必須保持所有公共介面不變
- **契約維護**：所有現有契約必須完全維護
- **向後相容**：必須確保完全的向後相容性
</behavioral_equivalence>

<scope_compliance>
### 範圍合規性（寬鬆紀錄）
- **範圍邊界**：應維持於 `scope.in_scope`；偏離時記錄警告與原因/補救
- **違規處理**：不中斷流程，於 dev_notes.validation_warnings 與 challenges_and_deviations 記錄
- **影響評估**：若涉及範圍外影響，記錄風險與緩解方案
</scope_compliance>

<workflow_compliance>
### 工作流程合規性
- **階段完整性**：絕不跳過工作流程階段，按順序執行所有階段
- **專門化要求**：必須執行 developer_specializations.refactor 中定義的專門行動
</workflow_compliance>

<refactor_specialized_enforcement>
### 重構專門強制要求

<baseline_capture>
#### 基線捕獲（強制執行）
- **測試套件執行**：必須運行完整的測試套件並確保全部通過
- **API捕獲**：必須捕獲所有公共APIs的簽名和行為
- **效能基線**：必須測量並記錄當前的效能基線
- **行為基線**：必須記錄所有可觀察的外部行為
</baseline_capture>

<characterization_testing>
#### 特性測試（強制實施）
- **行為測試**：必須為所有現有行為創建測試
- **不變量斷言**：必須斷言所有重要的不變量
- **契約測試**：必須為所有契約創建測試
- **回歸測試**：必須創建防止回歸的測試
</characterization_testing>

<incremental_refactoring>
#### 漸進式重構（強制方法）
- **原子提交**：每個變更必須是原子的，可以獨立驗證
- **小步驟**：每次變更必須足夠小，易於審查和理解
- **綠色狀態**：每次提交後測試必須保持通過狀態
- **API遷移**：如需API變更，必須使用漸進式遷移策略
</incremental_refactoring>

<validation_requirements>
#### 驗證要求（強制執行）
- **基線比較**：每次變更後必須與基線進行比較
- **API破壞檢查**：必須確保無API破壞性變更
- **效能驗證**：必須驗證效能沒有回歸
- **行為驗證**：必須驗證外部行為完全一致
</validation_requirements>
</refactor_specialized_enforcement>

<testing_requirements>
### 測試要求（強制維護）
- **覆蓋率維護**：必須維護或改善現有測試覆蓋率
- **測試品質**：重構後的測試必須更清晰、更可維護
- **測試重構**：測試代碼也可能需要重構，但必須保持驗證能力
- **回歸防護**：必須確保重構不會導致測試回歸
</testing_requirements>

<code_quality_principles>
### 代碼品質原則（強制應用）
- **SOLID原則**：必須應用SOLID設計原則
- **KISS原則**：保持代碼簡單明瞭
- **DRY原則**：消除重複，但不過度抽象
- **關注點分離**：確保適當的關注點分離
</code_quality_principles>

<performance_requirements>
### 效能要求（強制維護）
- **效能維護**：必須維護或改善運行時效能
- **記憶體效率**：必須維護或改善記憶體使用
- **回歸避免**：必須避免任何效能回歸
- **基準測試**：重大重構後必須進行基準測試
</performance_requirements>

<incremental_change_requirements>
### 增量變更要求（強制執行）
- **可審查變更**：每個變更必須足夠小，可以有效審查
- **明確檢查點**：每個階段必須有明確的檢查點
- **回滾能力**：每個變更必須可以安全回滾
- **變更記錄**：每個變更必須有清晰的記錄和說明
</incremental_change_requirements>

<standards_compliance>
### 標準合規性（強制遵守）
- **編碼標準**：必須遵循專案的編碼標準
- **工具合規**：必須通過linter和格式化器檢查
- **慣例遵循**：必須遵循語言和框架的最佳實踐
- **文檔標準**：代碼文檔必須符合專案標準
</standards_compliance>

<risk_management>
### 風險管理（強制實施）
- **變更影響評估**：每個變更都必須評估影響範圍
- **依賴分析**：必須分析變更對依賴項的影響
- **回滾計劃**：每個重構階段都必須有回滾計劃
- **風險緩解**：識別的風險必須有對應的緩解措施
</risk_management>

<documentation_and_traceability>
### 文檔和可追溯性
- **重構決策記錄**：重要的重構決策必須記錄
- **變更說明**：每個變更必須有清晰的說明
- **可追溯性**：必須在PR、提交和程式碼註釋中引用task_id
- **影響文檔**：重構對系統的影響必須記錄
</documentation_and_traceability>

<dev_notes_requirements>
### DEV_NOTES填寫要求（🚨 強制記錄但不中斷 🚨）
- **handover_docs階段執行**：重構完成後必須執行完整的handover_docs階段
- **detailed_changes記錄**：必須在dev_notes中詳細記錄所有重構變更
- **F-IDs/N-IDs映射**：映射缺漏不中斷；記錄缺漏清單與暫行對應/理由
- **重構策略記錄**：必須記錄採用的重構策略、漸進式步驟和決策理由
- **行為保持驗證**：必須記錄行為不變的驗證過程和測試結果
- **效能影響分析**：必須記錄重構前後的效能比較和優化結果
- **風險緩解記錄**：必須記錄識別的風險、緩解措施和回滾計劃
- **代碼品質改善**：必須記錄代碼品質的改善指標和維護性提升
- **技術債務清理**：必須記錄清理的技術債務和未來的改善建議
- **填寫品質要求**：dev_notes不可省略、不可敷衍，必須提供足夠的細節供後續維護參考
</dev_notes_requirements>

<markdown_format_conversion>
### Markdown格式轉換（絕對強制）
- **YAML到Markdown**：必須將 `~/cursor-claude/core/dev/templates/dev-notes-tmpl.yaml` 結構完整轉換為標準Markdown格式
- **標題層級**：YAML section轉換為對應的Markdown標題（# ## ### #### ##### ######）
- **清單格式**：YAML陣列轉換為Markdown清單（- 或 1. 格式）
- **代碼區塊**：代碼片段使用標準Markdown代碼塊（```language）
- **表格格式**：結構化資料使用Markdown表格格式 | 欄位 | 值 |
- **鏈結格式**：使用標準Markdown鏈結格式 [文字](URL)
- **區塊引用**：重要備註使用 > 引用格式
- **強調標記**：使用 **粗體** 和 *斜體* 適當強調關鍵內容
- **重構專用**：重構前後對比、效能測試結果、程式碼品質量測使用適當的表格和代碼區塊標記
</markdown_format_conversion>

<validation_checklist>
### 驗證檢查清單（強制執行）
- [ ] 所有測試仍然通過
- [ ] 沒有API破壞性變更
- [ ] 效能基線得到維護或改善
- [ ] 代碼覆蓋率得到維護或改善
- [ ] 外部行為完全一致
- [ ] 所有公共介面保持不變
- [ ] 編碼標準得到遵循
- [ ] 文檔得到適當更新
</validation_checklist>

<output_locations>
### 輸出位置（固定）
- **開發記錄**：`{{project_root}}/docs/dev-notes/{{task_id}`(如`1`, `2`, `3`...)}-dev-notes.md`
- **模板參考**：`~/cursor-claude/core/dev/templates/dev-notes-tmpl.yaml`
</output_locations>

<quality_gates>
### 品質門檻（強制通過）
- **靜態分析**：重構後的代碼必須通過所有靜態分析檢查
- **安全掃描**：必須確保重構沒有引入安全問題
- **效能測試**：必須通過所有效能測試
- **相容性測試**：必須通過所有相容性測試
</quality_gates>
</core_execution_protocol>

<refactor_stage_checkpoints>
## 重構階段檢查點（強制驗證）

<preparation_stage>
### 準備階段
- [ ] 基線測試全部通過
- [ ] 效能基線已記錄
- [ ] API簽名已捕獲
- [ ] 重構計劃已制定
</preparation_stage>

<execution_stage>
### 執行階段
- [ ] 每次變更後測試仍通過
- [ ] 變更足夠小且原子
- [ ] API沒有破壞性變更
- [ ] 效能沒有明顯回歸
</execution_stage>

<verification_stage>
### 驗證階段
- [ ] 與基線完全一致
- [ ] 所有測試通過
- [ ] 代碼品質得到改善
- [ ] 文檔得到更新
</verification_stage>
</refactor_stage_checkpoints>

<failure_handling_protocol>
## 失敗處理協議（記錄並續行）
- **計劃缺失**：記錄警告與替代資訊來源；繼續
- **基線測試未全綠**：記錄風險與補救計劃；必要時降級範圍
- **行為變更風險**：記錄檢測結果與回滾策略；不中斷
- **效能回歸**：記錄測量與優化計劃；在可控風險下續行
- **測試覆蓋下滑**：記錄缺口與補回時程
</failure_handling_protocol>