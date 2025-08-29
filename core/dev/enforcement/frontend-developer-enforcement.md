# Frontend Developer 強制執行規範

<core_execution_protocol>
## 核心執行協議

<prerequisite_conditions>
### 必要前置條件（寬鬆）
- **建議**：開始前載入統一工作流程與計劃；若缺失，於 dev_notes.validation_warnings 記錄並持續
- **工作流程讀取**：應讀取 `{project_root}/cursor-claude/core/dev/workflow/frontend-developer-workflow.md`，失敗則記錄警告
- **計劃檢查**：嘗試定位並讀取 task_id 的實施計劃；如缺失，記錄警告並以最小上下文繼續
</prerequisite_conditions>

<scope_compliance>
### 範圍合規性（寬鬆紀錄）
- **範圍邊界**：應維持於 `scope.in_scope`；偏離時記錄警告與原因/補救
- **違規處理**：不中斷流程，於 dev_notes.validation_warnings 與 challenges_and_deviations 記錄
- **變更協議**：先決策登記，後補正式附錄
</scope_compliance>

<workflow_compliance>
### 工作流程合規性
- **階段完整性**：絕不跳過工作流程階段，按順序執行所有階段
- **專門化要求**：必須執行 developer_specializations.frontend 中定義的專門行動
</workflow_compliance>
</core_execution_protocol>

<frontend_specialization_requirements>
## 前端專門強制要求

<ux_usability>
### UX和可用性（強制執行）
- **UI-IDs提取**：必須從計劃中提取所有UI-IDs
- **設計資產檢查**：必須檢查並應用所有設計資產
- **使用者體驗**：必須確保所有互動符合預期的使用者流程
</ux_usability>

<routing_state_management>
### 路由和狀態管理（強制實施）
- **路由定義**：必須定義清晰的路由結構
- **狀態枚舉**：必須枚舉所有應用狀態
- **全域狀態**：必須識別並正確管理全域狀態
- **狀態一致性**：確保狀態變更的可預測性
</routing_state_management>

<component_architecture>
### 組件架構（強制標準）
- **組件骨架**：必須創建清晰的組件骨架
- **Types定義**：必須定義所有types和interfaces
- **組件契約**：必須明確定義組件間的契約
- **關注點分離**：必須實施適當的關注點分離
</component_architecture>

<styling_theming>
### 樣式和主題（強制要求）
- **設計Tokens**：必須應用一致的設計tokens
- **主題系統**：必須實施可擴展的主題系統
- **響應式設計**：必須確保所有裝置的適應性
</styling_theming>
</frontend_specialization_requirements>

<accessibility_requirements>
## 無障礙性要求（強制但不中斷）

<mandatory_accessibility_standards>
- **A11Y合規**：應避免無障礙性阻礙；若未達標，記錄風險與補救計劃
- **色彩對比**：必須符合WCAG色彩對比要求
- **焦點管理**：必須實施適當的焦點管理
- **ARIA標籤**：必須添加適當的ARIA標籤
- **鍵盤導航**：必須支援完整的鍵盤導航
- **螢幕閱讀器**：必須確保螢幕閱讀器相容性
</mandatory_accessibility_standards>
</accessibility_requirements>

<performance_requirements>
## 效能要求（強制達標）

<performance_metrics>
- **Bundle大小**：必須符合指定的bundle大小限制
- **LCP (Largest Contentful Paint)**：必須達到效能目標
- **INP (Interaction to Next Paint)**：必須符合互動回應要求
- **TTI (Time to Interactive)**：必須達到可互動時間目標
- **資源優化**：必須實施圖片和資源優化
</performance_metrics>
</performance_requirements>

<testing_requirements>
## 測試要求（強制執行）

<test_driven_development>
- **測試優先**：必須先寫測試後寫實現
- **測試類型**：
  - 單元測試：與UI-IDs對齊
  - E2E測試：測試完整使用者流程
  - 無障礙測試：確保A11Y合規
- **覆蓋率門檻**：必須達到指定的測試覆蓋率要求
</test_driven_development>
</testing_requirements>

<architectural_principles>
## 架構原則（強制遵守）

<design_principles>
- **組件化設計**：必須應用基於組件的設計
- **SOLID原則**：必須應用SOLID設計原則
- **KISS原則**：保持介面簡潔易用
- **DRY原則**：避免重複的UI邏輯
</design_principles>
</architectural_principles>

<compatibility_requirements>
## 相容性要求（強制確保）

<cross_platform_compatibility>
- **瀏覽器相容性**：必須在指定的瀏覽器版本中正常運作
- **裝置相容性**：必須在各種裝置尺寸中正常顯示
- **向後相容性**：必須維護現有介面契約
</cross_platform_compatibility>
</compatibility_requirements>

<internationalization>
## 國際化和本地化（強制實施）

<i18n_support>
- **i18n支援**：必須實施國際化架構
- **文字外部化**：所有顯示文字必須外部化
- **文化適應**：必須考慮不同文化的使用習慣
</i18n_support>
</internationalization>

<documentation_traceability>
## 文檔和可追溯性

<documentation_requirements>
- **組件文檔**：必須更新Storybook或組件文檔
- **使用範例**：必須提供組件使用範例
- **可追溯性**：必須在PR、提交和程式碼註釋中引用task_id
- **約束記錄**：必須記錄所有組件約束和限制
</documentation_requirements>
</documentation_traceability>

<dev_notes_requirements>
## DEV_NOTES填寫要求（🚨 強制記錄但不中斷 🚨）

<mandatory_documentation>
- **handover_docs階段執行**：開發完成後必須執行完整的handover_docs階段
- **detailed_changes記錄**：必須在dev_notes中詳細記錄所有實施變更
- **UI-IDs映射**：映射缺漏不中斷；記錄缺漏清單與暫行對應/理由
- **組件決策記錄**：必須記錄組件設計決策、狀態管理策略和交互設計選擇
- **無障礙性實施記錄**：必須記錄實施的無障礙性功能和驗證結果
- **效能優化記錄**：必須記錄實施的效能優化措施和測試結果
- **設計資產使用**：必須記錄使用的設計資產和任何設計偏離的原因
- **瀏覽器相容性**：必須記錄測試的瀏覽器版本和發現的相容性問題
- **填寫品質要求**：dev_notes不可省略、不可敷衍，必須提供足夠的細節供後續維護參考
</mandatory_documentation>
</dev_notes_requirements>

<markdown_conversion>
## Markdown格式轉換（絕對強制）

<conversion_rules>
- **YAML到Markdown**：必須將 `{project_root}/cursor-claude/core/dev/templates/dev-notes-tmpl.yaml` 結構完整轉換為標準Markdown格式
- **標題層級**：YAML section轉換為對應的Markdown標題（# ## ### #### ##### ######）
- **清單格式**：YAML陣列轉換為Markdown清單（- 或 1. 格式）
- **代碼區塊**：代碼片段使用標準Markdown代碼塊（```language）
- **表格格式**：結構化資料使用Markdown表格格式 | 欄位 | 值 |
- **鏈結格式**：使用標準Markdown鏈結格式 [文字](URL)
- **區塊引用**：重要備註使用 > 引用格式
- **強調標記**：使用 **粗體** 和 *斜體* 適當強調關鍵內容
- **組件規範**：組件API、樣式定義、互動規格使用適當的代碼區塊標記
</conversion_rules>
</markdown_conversion>

<output_configuration>
## 輸出位置（固定）

<file_paths>
- **開發記錄**：`{{project_root}}/docs/dev-notes/{{task_id}`(如`1`, `2`, `3`...)}-dev-notes.md`
- **模板參考**：`{project_root}/cursor-claude/core/dev/templates/dev-notes-tmpl.yaml`
</file_paths>
</output_configuration>

<quality_gates>
## 品質門檻（強制通過）

<quality_standards>
- **靜態分析**：代碼必須通過ESLint和其他靜態分析
- **型別檢查**：必須通過TypeScript型別檢查
- **效能審核**：必須通過Lighthouse效能審核
- **無障礙審核**：必須通過無障礙性檢查
</quality_standards>
</quality_gates>

<accessibility_checklist>
## 無障礙性檢查清單（強制執行）

<a11y_verification>
- [ ] 所有互動元素都可用鍵盤訪問
- [ ] 所有圖片都有適當的alt文字
- [ ] 色彩對比度符合WCAG AA標準
- [ ] 表單都有適當的標籤和錯誤處理
- [ ] 動態內容變更都有適當的通知
- [ ] 螢幕閱讀器可以正確解讀所有內容
</a11y_verification>
</accessibility_checklist>

<performance_checklist>
## 效能檢查清單（強制執行）

<performance_verification>
- [ ] 圖片都經過優化和懶載入
- [ ] 代碼分割實施完成
- [ ] 不必要的重新渲染已被消除
- [ ] 第三方資源載入已優化
- [ ] 關鍵渲染路徑已優化
</performance_verification>
</performance_checklist>

<failure_handling>
## 失敗處理協議（記錄並續行）

<error_handling_protocol>
- **計劃缺失**：記錄警告與替代資訊來源；繼續
- **範圍偏離**：記錄偏離/影響/補救計劃；不中斷
- **A11Y未達標**：記錄風險與修復時程；不中斷
- **效能未達標**：記錄測量/優化計劃；在可控風險下續行
- **設計不一致**：記錄差異與對齊計劃；不中斷
</error_handling_protocol>
</failure_handling>