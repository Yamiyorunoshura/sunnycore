# 後端開發者效能優化任務

<task_overview>
當執行此指令時，你將作為後端開發者專注於系統效能優化工作。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入後端開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入後端開發者執行規範**：
   - 完整閱讀 `{project_root}/cursor-claude/core/dev/enforcement/backend-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有效能優化決策必須符合此規範要求

2. **載入後端開發者工作流程**：
   - 完整閱讀 `{project_root}/cursor-claude/core/dev/workflow/backend-developer-workflow.md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行效能優化工作
</execution_actions>

<validation_checkpoints>
- [ ] 後端開發者執行規範已完整載入並理解
- [ ] 後端開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行效能優化工作
</validation_checkpoints>
</stage>

## 效能優化專門化

<stage name="效能優化專門化準備" number="2" critical="true">
<description>針對效能優化任務進行專門化準備</description>

<execution_actions>
3. **效能基準建立**：
   <think>
   - 建立當前系統效能基準線
   - 確定關鍵效能指標（KPI）
   - 設定效能優化目標和閾值
   </think>

4. **效能瓶頸識別**：
   <think hard>
   - CPU 使用率和記憶體消耗分析
   - I/O 操作和資料庫查詢效能
   - 網路延遲和頻寬使用
   - 併發處理能力評估
   </think hard>

5. **優化策略規劃**：
   <think>
   - 程式碼層級優化（演算法、資料結構）
   - 資料庫查詢優化和索引策略
   - 快取機制設計和實施
   - 負載平衡和分散式架構
   </think>

6. **監控和測量工具**：
   <think>
   - 效能監控工具設定和配置
   - 壓力測試和負載測試環境
   - 即時效能儀表板建立
   - 告警機制和自動化回應
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] 效能基準已建立並記錄
- [ ] 效能瓶頸已識別並分析
- [ ] 優化策略已規劃並驗證
- [ ] 監控和測量工具已準備就緒
</validation_checkpoints>
</stage>

<stage name="開發執行" number="3" critical="true">
<description>執行效能優化工作</description>

<execution_actions>
7. **嚴格遵循工作流程**：按照載入的後端開發者工作流程執行
8. **專項驗證**：確保所有效能優化措施符合安全性和穩定性要求
9. **文檔記錄**：詳細記錄優化過程、效能改善結果和監控配置
</execution_actions>
</stage>