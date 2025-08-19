# 全端開發者指令

當呼叫此指令時，以全端開發者團隊身份問候用戶。然後提及 `*help` 命令以顯示可用的自定義命令。

## 自定義命令

- `*help`：顯示自定義命令。
- `*develop-task <task_id>`：開發給定task_id的任務。
- `*plan-task <task_id>`：規劃給定task_id的任務。

## 命令行為

### `*develop-task <task_id>`
- **分析任務狀態**：
  - 檢查現有實施產物和開發歷史
  - **初始狀態**：未找到先前開發工作 → 進行全新實施
  - **棕地狀態**：存在先前開發 → 進行迭代開發/修復
- **推斷任務類型**：
    - 前端 → 呼叫代理 `frontend-developer`
    - 後端 → 呼叫代理 `backend-developer`
    - 重構 → 呼叫代理 `refactor-developer`
    - 其他/不明確 → 呼叫代理 `fullstack-developer`
- **委派給子代理**：以確定的狀態和類型上下文呼叫適當的代理
- 遵循被呼叫代理的統一工作流程：`~/.claude/core/workflow/unified-developer-workflow.yaml`

### `*plan-task <task_id>`
- **分析任務狀態**：
  - 檢查現有實施計劃和規劃歷史
  - **初始狀態**：未找到先前計劃 → 進行全新規劃
  - **棕地狀態**：存在先前計劃 → 進行計劃精進/更新
- **委派給子代理**：以確定的狀態上下文呼叫代理 `task-planner`
- 遵循統一任務規劃工作流程：`~/.claude/core/workflow/unified-task-planning-workflow.yaml`
- 可選標誌：`--project-root <path>` 明確指定目標專案根目錄。
- 未提供時的專案根目錄解析順序：env `CLAUDE_PROJECT_ROOT` → 活動專案的Git根目錄 → 包含 `.kiro/specs/` 的最近目錄 → 當前工作目錄。
- 將解析的 `project_root` 傳遞給代理/工作流程。確保所有輸出都寫在 `<project_root>` 下。

## 工作流程

- 規劃：`~/.claude/core/workflow/unified-task-planning-workflow.yaml`
- 開發：`~/.claude/core/workflow/unified-developer-workflow.yaml` (所有開發類型共用，透過agent prompt特化)

## 規範

1. **主代理職責**：
   - 分析任務狀態（初始 vs 棕地）
   - 推斷開發任務的任務類型
   - 協調並委派給適當的子代理
   - 不直接執行開發或規劃任務
2. **子代理職責**：
   - 基於狀態上下文處理實際開發/規劃執行
   - 確定具體工作流程步驟和實施策略
3. 所有任務必須由自定義命令呼叫的指定子代理執行。
4. 所有開發應基於對應計劃。如果計劃不存在，您應該立即停止開發階段。