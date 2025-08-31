# 開發者協調器工作流程

## 工作流程執行準備

### 執行前準備要求

執行工作流程前必須創建詳細的待辦事項列表來組織所有步驟。

**準備流程**:
1. 分析workflow文件結構，識別所有階段和任務
2. 將每個階段的核心任務轉換為具體todo項目
3. 根據任務重要性和依賴關係設定優先級
4. 使用`todo_write`工具創建結構化todo list
5. 按todo list順序執行，及時更新狀態

**Todo List標準**:
- 覆蓋所有主要階段和驗證點
- 設定合理優先級，確保依賴關係
- 及時更新狀態（pending → in_progress → completed）
- 同時只能有一個任務處於`in_progress`狀態

---

## 階段一：計劃驗證

**目標**: 檢查實施計劃完整性

**執行任務**:
- 讀取`{project_root}/docs/implementation-plan/{task_id}-plan.md`實施計劃
- 驗證計劃格式和必要欄位
- 確認計劃範圍和約束條件
- 驗證sources路徑可解析性

**驗證要求**:
- 計劃文件存在且可讀取
- 必要欄位完整（task_id、project_name、owner、date）
- 範圍定義清晰可執行
- 約束條件明確合理

## 階段二：任務分類

**目標**: 分析計劃內容並分類任務類型

**執行任務**:
- 分析計劃涉及的技術領域和複雜度
- 識別前端、後端、全端或重構需求
- 評估任務依賴關係和並行執行可能性
- 計算任務複雜度和資源需求
- 檢查`docs/review-results/{task_id}-review.md`是否存在（棕地狀態檢測）
- 若為棕地狀態，讀取審查文件中的問題清單、修復建議和優先級

**驗證要求**:
- 技術領域正確識別
- 任務類型準確分類
- 依賴關係清晰映射
- 棕地狀態正確檢測

## 階段三：代理分配

**目標**: 智能分配專門代理執行任務

**執行任務**:
- 根據`{project_root}/sunnycore/dev/enforcement/developer-orchestrator-enforcement.md`的映射規則選擇代理
- 啟動並行執行協議
- 應用代理映射規則:

**後端領域**:
- `database` → `backend-developer_database`
- `api` → `backend-developer_api`
- `security` → `backend-developer_security`
- `performance` → `backend-developer_performance`
- `testing` → `backend-developer_testing`
- `infrastructure` → `backend-developer_infrastructure`

**前端領域**:
- `ui_ux` → `frontend-developer_ui-ux`
- `framework` → `frontend-developer_framework`
- `performance` → `frontend-developer_performance`
- `accessibility` → `frontend-developer_accessibility`
- `testing` → `frontend-developer_testing`

**全端領域**:
- `architecture` → `fullstack-developer_architecture`
- `integration` → `fullstack-developer_integration`
- `performance` → `fullstack-developer_performance`
- `devops` → `fullstack-developer_devops`

**重構領域**:
- `code_quality` → `refactor-developer_code-quality`
- `performance` → `refactor-developer_performance`

- 建立代理協調機制和衝突解決策略
- 傳遞完整任務上下文和品質要求
- 若為棕地狀態，精確傳遞問題清單和修復建議

**驗證要求**:
- 代理選擇符合任務需求
- 並行執行策略合理
- 協調機制建立完成
- 上下文傳遞完整

## 階段四：進度監控

**目標**: 實時監控代理執行狀態

**執行任務**:
- 建立實時追蹤儀表板
- 監控系統資源使用情況
- 檢測瓶頸、風險和異常模式
- 維護執行狀態日誌和時間線記錄
- 若為棕地狀態，特別監控問題修復進度
- 實施預警機制

**驗證要求**:
- 所有代理狀態可見
- 資源使用在合理範圍
- 無阻塞性瓶頸
- 執行日誌完整記錄

## 階段五：問題解決

**目標**: 解決執行過程中的問題和衝突

**執行任務**:
- 檢測代理間衝突、依賴問題和資源競爭
- 協調技術決策衝突和實施策略分歧
- 實施異常恢復和手動干預機制
- 動態優化執行策略和資源分配
- 若為棕地狀態，確保先前問題得到適當解決和驗證
- 建立問題升級機制

**驗證要求**:
- 代理間衝突已解決
- 技術決策達成一致
- 異常情況已恢復
- 棕地問題修復完成

## 階段六：完成報告

**目標**: 生成開發記錄和最終報告

**執行任務**:
- 收集整合所有代理執行結果、決策記錄和產出物
- 讀取標準模板`{project_root}/sunnycore/dev/templates/dev-notes-tmpl.yaml`
- 根據模板填入內容轉換為markdown格式
- 輸出到`{project_root}/docs/dev-notes/{task_id}-dev-notes.md`
- 驗證開發記錄格式完整性和內容準確性
- 若為棕地狀態，詳細記錄問題修復情況、驗證結果和品質改進
- 生成執行摘要、關鍵決策記錄和後續建議
- 建立可追溯的交付物清單和品質檢查報告

**驗證要求**:
- 所有代理結果已收集
- 開發記錄格式正確
- 內容完整且準確
- 棕地修復情況已記錄，dev notes文件已更新
- 交付物清單完整
