# 開發者記錄指南

## 概述

本指南說明如何使用 [`core/templates/dev-notes-tmpl.yaml`](core/templates/dev-notes-tmpl.yaml) 模板來創建和維護開發者實施記錄。開發記錄是專案開發過程中的重要文檔，記錄技術決策、實施細節和經驗教訓。

## 模板結構

開發者記錄模板採用 YAML 格式，包含以下主要部分：

### 1. 元數據 (Metadata)
```yaml
metadata:
  task_id: "必填 - 實際任務識別碼"
  plan_reference: "必填 - 對應的實施計劃路徑"
  project_root: "必填 - 專案根目錄路徑"
```

### 2. 開發記錄條目 (Dev Entries)
每個開發階段都應該添加一個條目，包含：
- `entry_id`: 唯一識別碼
- `developer_type`: 開發者類型
- `timestamp`: 時間戳記
- `task_phase`: 任務階段
- `re_dev_iteration`: 開發迭代次數

### 3. 詳細變化映射 (Detailed Changes Mapped To)
將變化映射到相關的需求ID：
- `F-IDs`: 功能需求ID
- `N-IDs`: 非功能需求ID  
- `UI-IDs`: UI元件ID

### 4. 實施決策 (Implementation Decisions)
記錄技術選型、架構決策和設計模式選擇。

### 5. 風險考量 (Risk Considerations)
識別技術風險並制定緩解措施。

### 6. 維護註記 (Maintenance Notes)
提供後續維護要點和監控建議。

### 7. 挑戰與偏離 (Challenges and Deviations)
記錄技術挑戰和與原計劃的偏離。

### 8. 品質指標 (Quality Metrics)
記錄測試覆蓋率、效能指標等品質數據。

### 9. 整合總結 (Integration Summary)
最後一次開發更新時填寫的整體總結。

## 使用指南

### 步驟 1: 創建新記錄文件
1. 在 `docs/dev-notes/` 目錄下創建新文件
2. 文件名格式: `{task_id}-dev-notes.md`
3. 複製模板內容到新文件

### 步驟 2: 填寫元數據
```yaml
metadata:
  task_id: "TASK-123"
  plan_reference: "plans/implementation-plan-TASK-123.yaml"
  project_root: "/path/to/project"
```

### 步驟 3: 添加開發條目
每次開發迭代都應該添加一個新條目：

```yaml
dev_entries:
  - entry_id: "entry-1"
    developer_type: "backend"
    timestamp: "2024-01-15T10:30:00Z"
    task_phase: "初始實施"
    re_dev_iteration: 1
```

### 步驟 4: 填寫詳細內容
確保每個文字欄位達到最低字數要求：
- `changes_summary`: 至少50字
- `implementation_decisions`: 至少50字
- `risk_considerations`: 至少30字
- `maintenance_notes`: 至少30字
- `challenges_and_deviations`: 至少30字
- `quality_metrics_achieved`: 至少20字

### 步驟 5: 更新整合總結
在最後一次開發時填寫：
```yaml
integration_summary:
  total_entries: 3
  overall_completion_status: "completed"
  key_achievements:
    - "完成用戶認證系統"
    - "實現API速率限制"
  remaining_work:
    - "無"
```

## 最佳實踐

1. **及時記錄**: 在每個開發階段結束後立即填寫記錄
2. **詳細具體**: 提供具體的技術細節和決策理由
3. **保持更新**: 隨開發進度持續更新記錄
4. **版本控制**: 將記錄文件納入版本控制
5. **團隊共享**: 確保團隊成員都能訪問和學習記錄

## 模板引用

完整模板內容可參考: [`core/templates/dev-notes-tmpl.yaml`](core/templates/dev-notes-tmpl.yaml)

## 自動化建議

主代理可以通過以下方式自動化記錄創建：
1. 讀取模板文件並解析YAML結構
2. 根據當前任務自動填充元數據
3. 提示用戶輸入各項詳細內容
4. 驗證字數要求和必填字段
5. 自動生成時間戳和唯一ID

## 範例輸出

完成後的開發記錄應該包含完整的開發歷程，能夠清楚地反映：
- 技術決策過程
- 遇到的挑戰和解決方案
- 達成的品質標準
- 後續維護建議

通過遵循此指南，可以確保開發記錄的完整性和一致性，為專案提供有價值的技術文檔。