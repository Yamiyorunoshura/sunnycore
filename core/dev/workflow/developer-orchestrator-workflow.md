# 開發者協調器工作流程

<enforcement>
## 🔄 工作流程Todo List製作

### 📋 開始執行前的必要準備

**重要提醒**: 在開始執行任何工作流程步驟之前，必須使用使用待辦事項列表來創建一個待辦事項列表來組織這些步驟。

**製作流程**:
1. **分析工作流程結構** - 仔細閱讀整個workflow文件，識別所有階段、步驟和任務
2. **提取關鍵任務** - 將每個階段的核心任務轉換為具體的todo項目
3. **設定優先級** - 根據任務的重要性和依賴關係設定優先級
4. **創建Todo List** - 使用`todo_write`工具創建包含所有步驟的結構化todo list
5. **執行與更新** - 按照todo list順序執行任務，及時更新狀態

### 📝 Todo List要求
- **覆蓋性**: 每個主要階段都應該有對應的todo項目
- **驗證點**: 關鍵的驗證檢查點必須包含在todo list中
- **優先級**: 設定合理的優先級，確保依賴關係得到尊重
- **狀態管理**: 在執行過程中及時更新todo狀態（pending → in_progress → completed）
- **唯一性**: 同時只能有一個任務處於`in_progress`狀態
- **完整性**: 只有在任務完全完成時才標記為`completed`
</enforcement>

---

<stage name="計劃驗證階段" number="1">
<description>檢查並驗證實施計劃的存在性和完整性</description>

<execution_actions>
- 從`{project_root}/docs/implementation-plan/{task_id}`(如`1`, `2`, `3`...)-plan.md`（如`1-plan.md`, `2-plan.md`, `3-plan.md`...）讀取task_id對應的實施計劃
- 驗證計劃格式和必要欄位（metadata、scope、assumptions、constraints）
- 確認計劃範圍和約束條件
- 驗證sources路徑的可解析性
</execution_actions>

<validation_checkpoints>
- 計劃文件存在且可讀取
- 必要欄位完整（task_id、project_name、owner、date）
- 範圍定義清晰且可執行
- 約束條件明確且合理
</validation_checkpoints>
</stage>

<stage name="任務分類階段" number="2">
<description>分析計劃內容並分類任務類型和技術領域</description>

<think harder>
<execution_actions>
- 深度分析計劃內容涉及的技術領域和複雜度
- 智能識別前端、後端、全端或重構需求
- 評估任務間的依賴關係和並行執行可能性
- 計算任務複雜度和所需資源估算
- 檢查`docs/review-results/{task_id}-review.md`（如`1-review.md`, `2-review.md`, `3-review.md`...）是否存在先前的審查文件（棕地狀態檢測）
- 如為棕地狀態，讀取`docs/review-results/{task_id}-review.md`（如`1-review.md`, `2-review.md`, `3-review.md`...）中的問題清單、修復建議和優先級，並將其作為任務分類的參考。
</execution_actions>
</think harder>

<classification_checkpoints>
- 技術領域正確識別
- 任務類型準確分類
- 依賴關係清晰映射
- 棕地狀態正確檢測
</classification_checkpoints>
</stage>

<stage name="代理分配階段" number="3">
<description>根據任務分類智能分配並調度相應的專門代理</description>

<think harder>
<execution_actions>
- 根據`~/cursor-claude/core/dev/enforcement/developer-orchestrator-enforcement.md`中的任務類型映射規則選擇最適當的子代理
- 啟動並行執行協議（當任務間無強依賴時）
- 應用智能代理映射規則:

    <agent_mapping category="後端領域專家">
    - `database` → `backend-developer_database` (數據庫設計、優化、遷移)
    - `api` → `backend-developer_api` (RESTful API、GraphQL、微服務)
    - `security` → `backend-developer_security` (認證、授權、安全防護)
    - `performance` → `backend-developer_performance` (效能優化、負載測試)
    - `testing` → `backend-developer_testing` (測試策略、自動化測試)
    - `infrastructure` → `backend-developer_infrastructure` (部署、監控、DevOps)
    </agent_mapping>

    <agent_mapping category="前端領域專家">
    - `ui_ux` → `frontend-developer_ui-ux` (用戶界面、用戶體驗)
    - `framework` → `frontend-developer_framework` (React、Vue、Angular)
    - `performance` → `frontend-developer_performance` (前端優化、打包優化)
    - `accessibility` → `frontend-developer_accessibility` (無障礙設計)
    - `testing` → `frontend-developer_testing` (前端測試、E2E測試)
    </agent_mapping>

    <agent_mapping category="全端領域專家">
    - `architecture` → `fullstack-developer_architecture` (系統架構、技術選型)
    - `integration` → `fullstack-developer_integration` (系統整合、第三方服務)
    - `performance` → `fullstack-developer_performance` (全棧效能優化)
    - `devops` → `fullstack-developer_devops` (CI/CD、容器化、雲端部署)
    </agent_mapping>

    <agent_mapping category="重構領域專家">
    - `code_quality` → `refactor-developer_code-quality` (代碼重構、架構改進)
    - `performance` → `refactor-developer_performance` (效能重構、優化重構)
    </agent_mapping>

- 建立代理間的實時協調機制和衝突解決策略
- 傳遞完整的任務上下文、執行參數和品質要求
- 如為棕地狀態，將審查文件中的問題清單和修復建議精確傳遞給相關代理
</execution_actions>
</think harder>

<assignment_checkpoints>
- 代理選擇符合任務  需求
- 並行執行策略合理
- 協調機制建立完成
- 上下文傳遞完整
</assignment_checkpoints>
</stage>

<stage name="進度監控階段" number="4">
<description>實時監控所有活躍代理的執行狀態和進度</description>

<execution_actions>
- 建立代理執行進度的實時追蹤儀表板
- 監控系統資源使用情況（CPU、內存、網絡）
- 智能檢測潛在的瓶頸、風險和異常模式
- 維護詳細的執行狀態日誌和時間線記錄
- 如為棕地狀態，特別監控問題修復的進度和品質
- 實施預警機制，提前識別可能的執行問題
</execution_actions>

<monitoring_checkpoints>
- 所有代理狀態可見
- 資源使用在合理範圍
- 無阻塞性瓶頸
- 執行日誌完整記錄
</monitoring_checkpoints>
</stage>

<stage name="問題解決階段" number="5">
<description>識別並解決執行過程中的問題和衝突</description>

<think>
<execution_actions>
- 智能檢測代理間的衝突、依賴問題和資源競爭
- 協調技術決策衝突和實施策略分歧
- 實施異常情況的自動恢復和手動干預機制
- 動態優化執行策略和資源分配
- 如為棕地狀態，確保先前審查中的所有問題都得到適當解決和驗證
- 建立問題升級機制，處理複雜技術決策
</execution_actions>
</think>

<resolution_checkpoints>
- 代理間衝突已解決
- 技術決策達成一致
- 异常情况已恢复
- 棕地问题修复完成
</resolution_checkpoints>
</stage>

<stage name="完成報告階段" number="6">
<description>生成開發記錄和最終報告</description>

<think hard>
<execution_actions>
- 收集並整合所有代理的執行結果、決策記錄和產出物
- 讀取標準模板`~/cursor-claude/core/dev/templates/dev-notes-tmpl.yaml`
- 根據模板填入內容並轉換為markdown格式輸出到`{project_root}/docs/dev-notes/`路徑下，文件名稱為`{task_id}`(如`1`, `2`, `3`...)-dev-notes.md`（如`1-dev-notes.md`, `2-dev-notes.md`, `3-dev-notes.md`...）
- 驗證開發記錄的格式完整性和內容準確性
- 如為棕地狀態，在開發記錄中詳細記錄問題修復情況、驗證結果和品質改進
- 生成執行摘要、關鍵決策記錄和後續建議
- 建立可追溯的交付物清單和品質檢查報告
</execution_actions>
</think hard>

<completion_checkpoints>
- 所有代理結果已收集
- 開發記錄格式正確
- 內容完整且準確
- 棕地修復情況已記錄，並已更新dev notes文件（特別是迭代次數相關擊落）
- 交付物清單完整
</completion_checkpoints>
</stage>
