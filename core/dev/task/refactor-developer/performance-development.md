# 重構開發者 效能優化重構任務

<task_overview>
當執行此指令時，你將作為重構開發者專注於效能剖析、瓶頸移除與系統穩定性的改進工作。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入重構開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入重構開發者執行規範**：
   - 完整閱讀 `/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/refactor-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有重構決策必須符合此規範要求

2. **載入重構開發者工作流程**：
   - 完整閱讀 `/Users/tszkinlai/Coding/AI workflow/core/dev/workflow/refactor-developer-workflow.md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行效能優化重構
</execution_actions>

<validation_checkpoints>
- [ ] 重構開發者執行規範已完整載入並理解
- [ ] 重構開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行效能優化重構
</validation_checkpoints>
</stage>

## 效能優化重構專門化

<stage name="效能專門化準備" number="2" critical="true">
<description>針對效能優化重構任務進行專門化準備</description>

<execution_actions>
3. **效能目標與SLO定義**：
   <think>
   - 延遲 P50/P95/P99、吞吐量、錯誤率與資源使用率目標
   - 服務等級目標（SLO）與服務等級指標（SLI）
   - 監控與基準測試方法（負載、壓力、容量）
   </think>

4. **剖析與可觀察性策略**：
   <think hard>
   - 端到端追蹤（Tracing）、指標（Metrics）、日誌（Logs）三支柱
   - 採集慢查詢、GC、鎖競爭、I/O等待與網路延遲
   - 對關鍵交易路徑建立 profiling 報告與Heatmap
   </think hard>

5. **瓶頸識別與優化路徑**：
   <think>
   - 演算法複雜度、資料結構與記憶體配置
   - 資料庫存取（索引、查詢計劃、N+1、批量化）
   - 快取階層化（本地/分散式），TTL、失效策略與一致性
   - 併發與非同步模型、背壓與排程策略
   </think>

6. **架構級優化策略**：
   <think>
   - 隔離關鍵路徑（CQRS、讀寫分離、事件驅動）
   - 分片、分區與資料熱點緩解
   - 服務降級、熔斷、重試、超時與逾時保護
   </think>

7. **釋出與風險控制**：
   <think>
   - 金絲雀釋出、灰度、A/B，把握對比度量
   - 可回滾與影響面評估，明確容量預案
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] SLO/SLI 與效能目標已定義
- [ ] 可觀察性覆蓋關鍵路徑並可重現問題
- [ ] 瓶頸清單與優化順序已確立
- [ ] 釋出與回滾策略已準備
</validation_checkpoints>
</stage>

<stage name="開發執行" number="3" critical="true">
<description>執行效能優化重構工作</description>

<execution_actions>
8. **嚴格遵循工作流程**：按照載入的重構開發者工作流程執行
9. **專項驗證**：以基準測試驗證每次改動的效益與回歸
10. **文檔記錄**：保留剖析報告、效能測量、調參依據與結果對照
</execution_actions>

<validation_checkpoints>
- [ ] 基準測試可重現且統計顯著（多次測量區間收斂）
- [ ] 端到端延遲/吞吐/資源指標達標
- [ ] 故障率未上升且穩定性不下降
</validation_checkpoints>
</stage>