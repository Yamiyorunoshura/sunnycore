# QA系統架構說明

## 文件職責分工

### 1. **`agents/task-reviewer.md`** - Agent系統提示詞
- **職責**：定義AI代理的人格特質、工作風格、品質哲學
- **內容**：Dr. Thompson的角色設定、強制啟動序列、快停機制
- **特點**：提供態度指導和行為框架，不包含具體技術參數

### 2. **`enforcement/task-reviewer-enforcement.md`** - 強制執行規則
- **職責**：定義具體的執行規範、約束條件、品質門檻
- **內容**：詳細的檢查清單、評估標準、失敗處理協議
- **特點**：提供執行約束和驗證規則，引用統一配置

### 3. **`workflow/unified-review-workflow.yaml`** - 實際工作流程
- **職責**：定義結構化的執行步驟和階段定義
- **內容**：6個核心階段的具體行動、工具調用、檢查點
- **特點**：提供執行藍圖，引用enforcement和配置

### 4. **`templates/review-tmpl.yaml`** - 報告範本
- **職責**：定義審查報告的結構和格式
- **內容**：報告章節、評估維度、輸出格式
- **特點**：提供標準化的報告結構

## 引用關係圖

```
task-reviewer.md (Agent)
    ↓ 引用
task-reviewer-enforcement.md (Enforcement)
    ↑ 被引用
    ↓ 引用
unified-review-workflow.yaml (Workflow)
    ↑ 被引用
    ↓ 引用
review-tmpl.yaml (Template)
```

## 配置管理原則

### 1. **職責分離**
- **Agent**：人格和態度指導
- **Enforcement**：執行規則和約束
- **Workflow**：執行步驟和流程
- **Template**：輸出格式和結構

### 2. **引用優先**
- 優先使用引用而非重複定義
- 明確標示引用關係和文件路徑
- 避免配置不一致的問題

### 3. **維護性**
- 修改技術參數只需更新配置文件
- 各文件職責明確，便於維護和擴展
- 減少重複內容，提高一致性

## 使用指南

### 開發者
1. 修改執行規則：更新 `task-reviewer-enforcement.md`
2. 修改工作流程：更新 `unified-review-workflow.yaml`
3. 修改代理行為：更新 `task-reviewer.md`
5. 修改報告格式：更新 `review-tmpl.yaml`

### AI代理
1. 啟動時按順序載入所有必要文件
2. 嚴格遵循引用關係，不重複定義配置
3. 使用統一的技術參數和執行規則
4. 按照工作流程執行審查任務

## 版本控制

- 所有文件都應保持版本同步
- 重大變更時更新所有相關文件的引用
- 維護文件間的依賴關係文檔
