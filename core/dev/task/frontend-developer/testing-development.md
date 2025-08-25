# 前端開發者 測試開發任務

<task_overview>
當執行此指令時，你將作為前端開發者專注於測試開發工作。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入前端開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入前端開發者執行規範**：
   - 完整閱讀 `~/cursor-claude/core/dev/enforcement/frontend-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有開發決策必須符合此規範要求

2. **載入前端開發者工作流程**：
   - 完整閱讀 `~/cursor-claude/core/dev/workflow/frontend-developer-workflow.md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行測試開發工作
</execution_actions>

<validation_checkpoints>
- [ ] 前端開發者執行規範已完整載入並理解
- [ ] 前端開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行測試開發工作
</validation_checkpoints>
</stage>

## 測試開發專門化

<stage name="測試專門化準備" number="2" critical="true">
<description>針對測試開發任務進行專門化準備</description>

<execution_actions>
3. **測試策略確認**：
   <think>
   - 遵循測試金字塔原則（單元測試、整合測試、端到端測試）
   - 確保測試覆蓋率和測試品質平衡
   - 考慮不同瀏覽器和設備的相容性測試
   </think>

4. **測試技術要求特化**：
   <think hard>
   - 單元測試框架和工具選擇（Jest、Vitest 等）
   - 組件測試和視覺回歸測試
   - 端到端測試工具整合（Playwright、Cypress 等）
   - 效能測試和負載測試機制
   - 無障礙測試和使用者體驗測試
   </think hard>

5. **測試自動化策略**：
   <think>
   - CI/CD 流程中的測試自動化
   - 測試報告和覆蓋率分析
   - 失敗測試的偵錯和修復流程
   - 測試資料管理和模擬服務
   </think>

6. **測試品質保證**：
   <think>
   - 測試案例設計和維護標準
   - 測試環境配置和管理
   - 測試程式碼審查和重構
   - 測試文檔和知識分享
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] 測試策略已確認並理解
- [ ] 測試技術要求已明確定義
- [ ] 自動化策略已制定並準備執行
- [ ] 測試品質保證標準已建立
</validation_checkpoints>
</stage>

<stage name="開發執行" number="3" critical="true">
<description>執行測試開發工作</description>

<execution_actions>
6. **嚴格遵循工作流程**：按照載入的前端開發者工作流程執行
7. **專項驗證**：確保所有測試相關的覆蓋率和品質要求得到滿足
8. **文檔記錄**：詳細記錄測試架構、測試案例和測試結果分析
</execution_actions>
</stage>