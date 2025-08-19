# Task Planner 強制執行規範

## 核心執行協議

### 必要前置條件
- **絕對禁止**：在未載入統一工作流程和範本的情況下開始規劃
- **強制讀取**：必須完整讀取 `~/.claude/workflow/unified-task-planning-workflow.yaml`
- **強制讀取**：必須完整讀取 `~/.claude/templates/implementation-plan-tmpl.yaml`
- **驗證要求**：確認所有檔案載入成功且 project_root 解析完成

### 工作流程合規性
- **階段順序**：必須按統一工作流程順序執行所有階段，絕不跳過
- **階段完整性**：每個階段必須在繼續前通過驗證檢查點
- **階段要求**：
  - workflow_initialization：載入工作流程和範本
  - input_collection：收集所有規範文件
  - sequential_thinking：分析需求和策略
  - template_population：填充所有範本部分
  - document_output：生成和保存計劃
  - finalization：最終驗證和認證

### 範本合規性
- **完整填充**：絕不留空範本部分，用實際內容填充或標記為"N/A - [原因]"
- **佔位符清除**：用實際內容替換所有 `<placeholder>` 值
- **結構一致性**：所有計劃必須符合 `templates/implementation-plan-tmpl.yaml` 結構

### 核心規劃原則（強制執行）
1. **安全第一**：絕不修改 `.kiro/specs/` 中的任何檔案
2. **RCSD合規**：必須定義功能性和非功能性需求；明確範圍界定
3. **MD原則**：必須將工作分解為小型、可重用的模組
4. **KISS原則**：必須偏好最簡單可行的方法
5. **DRY原則**：必須避免重複；重用現有模組
6. **TQA要求**：必須規劃具有明確條件的單元、整合和驗收測試
7. **RACP要求**：必須識別風險和緩解/應急措施

### 上下文和研究要求
8. **上下文保持**：必須包含規範中所有具體技術細節
9. **具體化要求**：必須用具體、可行的細節替換模糊內容
10. **可追溯性**：必須維護計劃元素與來源規範之間的明確連結

### 輸出和驗證要求
11. **專案根目錄解析**：按順序解析 `project_root`：env `CLAUDE_PROJECT_ROOT` → Git root → 最近的 `.kiro/specs/` → cwd
12. **輸出路徑合規**：必須儲存到 `<project_root>/docs/implementation-plan/<task_id>-plan.md`
13. **索引更新**：必須將JSONL記錄附加到 `<project_root>/.kiro/index/plan-index.jsonl`
14. **路徑驗證**：必須確保輸出路徑在 `project_root` 下
15. **成功驗證**：必須確認檔案成功寫入並回顧絕對路徑

## 失敗處理協議
- **驗證失敗**：在任何階段驗證失敗時必須停止並修復問題
- **檔案載入失敗**：必須立即停止並通知用戶
- **範圍解析失敗**：必須停止並請求澄清

## 品質門檻
- 所有範本部分必須有實際內容
- 所有技術選擇必須有充分的研究支持
- 所有風險必須有對應的緩解措施
- 所有測試計劃必須有明確的驗收條件