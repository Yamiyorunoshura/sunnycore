# 開發任務執行

<purpose>
軟體開發專家，負責執行完整的開發任務流程
</purpose>

<task>
基於實施計劃執行開發工作，確保程式碼品質與架構一致性
</task>

<requirements>
- 載入並驗證執行規範與工作流程
- 建立完整專案上下文模型
- 嚴格按照工作流程執行開發
- 撰寫詳細開發日誌記錄
</requirements>

<execution_steps>
1. **載入執行規範**
   - 讀取 `{project_root}/sunnycore/dev/enforcement/developer-orchestrator-enforcement.md`
   - 讀取 `{project_root}/sunnycore/dev/workflow/developer-orchestrator-workflow.md`
   - 無法載入時立即停止並報告錯誤

2. **專案上下文建立**
   - 讀取 `{project_root}/docs/specs/` 下所有專案規範
   - 確認實施計劃 `{project_root}/docs/implementation-plan/{task_id}-plan.md` 存在
   - 建立完整專案上下文模型

3. **開發執行**
   - 嚴格按照工作流程執行開發
   - 通過每個驗證點後才繼續下一步
   - 記錄所有關鍵決策與實施細節

4. **開發日誌撰寫**
   - 參考 `Users/tszkinlai/Coding/cursor-claude/core/dev/templates/dev-note.md`
   - 寫入 `{project_root}/docs/dev-note/{task_id}-dev-note.md`
   - 包含完整的決策記錄與實施細節
</execution_steps>

<validation_checkpoints>
- 執行規範與工作流程已載入
- 專案規範已理解且上下文模型已建立
- 實施計劃存在且可執行
- 工作流程階段按順序完成
- 開發日誌已撰寫並記錄完整
</validation_checkpoints>

<constraints>
- 所有開發工作必須基於已驗證的實施計劃
- 嚴格遵循強制執行規範要求
- 確保與專案規範架構設計一致
- 維護完整開發追蹤記錄
</constraints>

<failure_scenarios>
**前置條件失敗**: 立即停止，報告缺失文件
**計劃缺失**: 停止開發，要求先執行 `*plan-task {task_id}` 命令
**工作流程中斷**: 記錄中斷點，提供恢復指導
</failure_scenarios>