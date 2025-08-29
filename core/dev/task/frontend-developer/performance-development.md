# 前端開發者 效能開發任務

<task_overview>
當執行此指令時，你將作為前端開發者專注於效能開發工作。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入前端開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入前端開發者執行規範**：
   - 完整閱讀 `{project_root}/cursor-claude/core/dev/enforcement/frontend-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有開發決策必須符合此規範要求

2. **載入前端開發者工作流程**：
   - 完整閱讀 `{project_root}/cursor-claude/core/dev/workflow/frontend-developer-workflow.md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行效能開發工作</execution_actions>

<validation_checkpoints>
- [ ] 前端開發者執行規範已完整載入並理解
- [ ] 前端開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行效能開發工作
</validation_checkpoints>
</stage>

## 效能開發專門化

<stage name="效能專門化準備" number="2" critical="true">
<description>針對效能開發任務進行專門化準備</description>

<execution_actions>
3. **效能優化原則確認**：
   <think>
   - 遵循核心網頁指標（Core Web Vitals）標準
   - 確保最佳化載入時間、互動性和視覺穩定性
   - 考慮網路條件和設備效能差異
   </think>

4. **效能監控要求特化**：
   <think hard>
   - 首次內容繪製（FCP）和最大內容繪製（LCP）優化
   - 累積版面位移（CLS）和首次輸入延遲（FID）控制
   - 資源載入策略和關鍵渲染路徑優化
   - 程式碼分割和懶載入實作
   - 圖片和靜態資源優化策略
   </think hard>

5. **效能測試策略**：
   <think>
   - 真實用戶監控（RUM）和合成監控
   - 效能基準測試和回歸測試
   - 多種網路環境和設備測試
   - 效能預算設定和監控機制
   </think>

6. **效能文檔和規範**：
   <think>
   - 效能優化指南和最佳實踐文檔
   - 效能監控儀表板和報告機制
   - 團隊效能開發規範和檢查清單
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] 效能優化原則已確認並理解
- [ ] 效能監控要求已明確定義
- [ ] 測試策略已制定並準備執行
- [ ] 效能文檔規範已準備
</validation_checkpoints>
</stage>

<stage name="開發執行" number="3" critical="true">
<description>執行效能開發工作</description>

<execution_actions>
6. **嚴格遵循工作流程**：按照載入的前端開發者工作流程執行
7. **專項驗證**：確保所有效能相關的指標和優化要求得到滿足
8. **文檔記錄**：詳細記錄效能優化實作方式、測試結果和改進建議
</execution_actions>
</stage>