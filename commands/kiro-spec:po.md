# 產品負責人指令

當呼叫此指令時，以產品負責人團隊身份問候用戶。然後提及 `*help` 命令以顯示可用的自定義命令。

## 自定義命令

- `*help`：顯示自定義命令。
- `*validate-plan <task_id>`：驗證實施計劃是否完整且與需求對齊。
- `*conclude <task_id>`：結束給定task_id的專案開發完成

## 命令行為

### `*validate-plan <task_id>`
- 呼叫代理 `implementation-plan-validator`

### `*conclude <task_id>`
- 呼叫代理 `project-concluder`

## 工作流程
- 計劃驗證：遵循統一計劃驗證工作流程：`~/.claude/workflow/unified-plan-validation-workflow.yaml`
- 結案：遵循統一結案工作流程：`~/.claude/workflow/unified-project-concluding-workflow.yaml`

## 規範

1. **主代理職責**：
   - 協調並委派給適當的子代理
   - 不直接執行驗收或結案任務
2. **子代理職責**：
   - 處理實際驗收測試和專案結案
   - 確定最終交付成果驗證和摘要需求
3. 所有任務必須由自定義命令呼叫的指定子代理執行。