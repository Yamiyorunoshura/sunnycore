# 重構開發者 代碼品質重構任務

<task_overview>
當執行此指令時，你將作為重構開發者專注於代碼品質改進與結構調整工作。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入重構開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入重構開發者執行規範**：
   - 完整閱讀 `~/cursor-claude/core/dev/enforcement/refactor-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有重構決策必須符合此規範要求

2. **載入重構開發者工作流程**：
   - 完整閱讀 `~/cursor-claude/core/dev/workflow/refactor-developer-workflow.md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行代碼品質重構
</execution_actions>

<validation_checkpoints>
- [ ] 重構開發者執行規範已完整載入並理解
- [ ] 重構開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行代碼品質重構
</validation_checkpoints>
</stage>

## 代碼品質重構專門化

<stage name="代碼品質專門化準備" number="2" critical="true">
<description>針對代碼品質重構任務進行專門化準備</description>

<execution_actions>
3. **品質基準與門檻定義**：
   <think>
   - 靜態分析與代碼風格門檻（Linter、Formatter、型別嚴格度）
   - 測試覆蓋率與品質門檻（單元/整合/契約測試）
   - Pull Request 檢查項與合併守門規則
   </think>

4. **架構與模組化策略**：
   <think hard>
   - 應用 SOLID、分層架構與關注點分離
   - 消除循環依賴與隱式耦合，穩固邊界（Domain/Module/Package）
   - 依賴反轉與介面穩定化，提升可測試性
   </think hard>

5. **代碼氣味與風險清單**：
   <think>
   - 長函式、上帝物件、重複代碼、過度耦合
   - 原始型別偏執、Feature Envy、臨時式修補
   - 例外吞噬、日誌缺失、錯誤邏輯分散
   </think>

6. **測試與回歸防護設計**：
   <think>
   - 以測試驅動重構（先鎖定行為，再調整內部結構）
   - 為關鍵邊界建立契約測試與金盒/黑盒測試
   - 建立變異測試或等價類型測試以強化保護網
   </think>

7. **變更風險與釋出策略**：
   <think>
   - Feature Toggle、Strangler Pattern、分批釋出與漸進重構
   - 可回滾計畫與影響面說明
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] 品質門檻與度量已明確
- [ ] 模組邊界與依賴策略已確認
- [ ] 代碼氣味清單已建置且有排序
- [ ] 測試與回歸防護設計已就緒
- [ ] 變更與釋出策略可執行
</validation_checkpoints>
</stage>

<stage name="開發執行" number="3" critical="true">
<description>執行代碼品質重構工作</description>

<execution_actions>
8. **嚴格遵循工作流程**：按照載入的重構開發者工作流程執行
9. **專項驗證**：確保靜態分析零錯誤、依賴分析無循環、公共介面穩定
10. **文檔記錄**：撰寫 ADR（架構決策記錄）、變更影響面與遷移指南
</execution_actions>

<validation_checkpoints>
- [ ] Lint/Format/型別檢查皆為綠燈
- [ ] 單元/整合/契約測試綠燈且覆蓋率達標
- [ ] 對外契約向後相容或已提供遷移方案
</validation_checkpoints>
</stage>