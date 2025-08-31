# 效能優化重構任務

<purpose>
重構開發者，專注於效能剖析、瓶頸識別與系統穩定性優化
</purpose>

<task>
執行效能優化重構，包含延遲降低、吞吐量提升與資源使用率優化
</task>

<requirements>
- 完整閱讀 `{project_root}/sunnycore/dev/enforcement/refactor-developer-enforcement.md` 執行規範
- 完整閱讀 `{project_root}/sunnycore/dev/workflow/refactor-developer-workflow.md` 工作流程
- 建立 SLO/SLI 效能目標與基準測試
- 實施端到端可觀察性覆蓋
- 識別並優化關鍵瓶頸路徑
- 執行統計顯著的效能驗證
</requirements>

<optimization_focus>
## 效能目標定義
- 延遲指標：P50/P95/P99 目標值
- 吞吐量：QPS/TPS 容量規劃
- 資源使用率：CPU/記憶體/I/O 效率
- 錯誤率與可用性維持

## 剖析與診斷
- 端到端追蹤與指標收集
- 慢查詢、GC、鎖競爭分析
- 關鍵交易路徑 profiling
- 熱點與瓶頸定位

## 優化策略
- 演算法與資料結構改進
- 資料庫存取優化（索引、查詢、批量化）
- 快取階層化與失效策略
- 併發模型與非同步處理
- 架構級分離與隔離
</optimization_focus>

<output_format>
- 效能剖析報告
- 瓶頸識別清單
- 優化實施代碼
- 基準測試結果對比
- 釋出與回滾計畫
</output_format>

<constraints>
- 所有變更必須通過基準測試驗證
- 維持系統穩定性不下降
- 遵循載入的執行規範與工作流程
- 確保統計顯著的效能改進
- 建立可重現的測試環境
</constraints>