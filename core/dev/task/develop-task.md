# 開發任務執行指令

<task_overview>
當呼叫此指令時，你將作為開發者執行全面的開發任務。
</task_overview>

## 執行步驟

<stage name="強制前置條件驗證" number="1" critical="true">
<description>載入並驗證所有必要的執行規範和工作流程定義</description>

<execution_actions>
1. **載入強制執行規範**：完整讀取 `/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/developer-orchestrator-enforcement.md`
   - 這包含所有強制執行規則和驗證標準
   - 如果無法載入，立即停止並報告錯誤

2. **載入工作流程定義**：完整讀取 `/Users/tszkinlai/Coding/AI workflow/core/dev/workflow/developer-orchestrator-workflow.md`
   - 理解所有階段、檢查點和驗證要求
   - 如果無法載入，立即停止並報告錯誤
</execution_actions>

<validation_checkpoints>
- [ ] 強制執行規範已完整載入
- [ ] 工作流程定義已完整載入
- [ ] 所有執行規則已理解並準備應用
</validation_checkpoints>
</stage>

<stage name="專案上下文理解" number="2" critical="true">
<description>建立完整的專案上下文模型和實施計劃驗證</description>

<execution_actions>
3. **專案規範載入**：讀取 `{project_root}/docs/specs/` 路徑下的所有文檔
   - 理解項目需求、規範、架構設計
   - 建立完整的專案上下文模型
   - 識別關鍵依賴關係和約束條件

4. **實施計劃驗證**：確認 `{project_root}/docs/implementation-plan/{task_id}`(如`1`, `2`, `3`...)-plan.md` (如`1-plan.md`, `2-plan.md`, `3-plan.md`...)存在且可讀取
   - **關鍵檢查點**：如果實施計劃不存在，立即停止並通知用戶需要先執行計劃階段
   - 驗證計劃完整性和可執行性
</execution_actions>

<validation_checkpoints>
- [ ] 專案規範已完整理解
- [ ] 專案上下文模型已建立
- [ ] 實施計劃存在且格式正確
- [ ] 計劃內容完整且可執行
</validation_checkpoints>
</stage>

<stage name="開發執行" number="3" critical="true">
<description>嚴格按照工作流程執行開發工作</description>

<execution_actions>
5. **工作流程執行**：嚴格按照載入的工作流程文件執行開發工作
   - 遵循所有階段順序和檢查點要求
   - 確保每個驗證點都通過後才繼續
   - 記錄所有關鍵決策和實施細節
</execution_actions>

<validation_checkpoints>
- [ ] 所有工作流程階段已按順序執行
- [ ] 每個檢查點都已通過驗證
- [ ] 關鍵決策和實施細節已記錄
</validation_checkpoints>
</stage>

<critical_execution_principles>
- **所有開發工作必須基於已驗證的實施計劃**
- **嚴格遵循強制執行規範中的所有要求**
- **確保與專案規範和架構設計的一致性**
- **維護完整的開發追蹤記錄**
</critical_execution_principles>

<failure_handling>
<scenario type="前置條件失敗">
立即停止，報告具體缺失的文件或條件
</scenario>

<scenario type="計劃缺失">
停止開發，引導用戶先執行 `*plan-task {task_id}`(如`1`, `2`, `3`...)` 命令
</scenario>

<scenario type="工作流程中斷">
記錄中斷點，提供恢復指導
</scenario>
</failure_handling>