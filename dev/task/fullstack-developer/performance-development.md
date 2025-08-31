# 全端開發者效能開發任務

<purpose>
全端開發專家，專注於前後端效能優化與監控系統設計
</purpose>

<task>
執行全端應用的效能開發工作，包含前端Core Web Vitals優化、後端API響應優化、資料庫效能調優和端到端監控系統建置
</task>

<requirements>
- 載入並遵循全端開發者執行規範（fullstack-developer-enforcement.md）
- 載入並執行全端開發者工作流程（fullstack-developer-workflow.md）
- 前端效能：LCP < 2.5s、INP < 200ms、TTI < 3s
- 後端效能：API響應時間 < 200ms、吞吐量 > 1000 req/s
- 資料庫查詢優化：90%查詢 < 50ms
- 實施完整的效能監控和告警機制
</requirements>

<execution_steps>
1. **載入執行規範**
   - 完整讀取fullstack-developer-enforcement.md作為唯一執行標準
   - 完整讀取fullstack-developer-workflow.md作為工作流程基準

2. **前端效能優化**
   - 分析Core Web Vitals指標並制定優化策略
   - 實施代碼分割、懶載入、預載入技術
   - 優化JavaScript、CSS、圖片資源載入
   - 設計前端快取和CDN策略

3. **後端效能優化**
   - 分析API響應時間和吞吐量瓶頸
   - 實施資料庫查詢優化和索引設計
   - 設計快取策略和連接池管理
   - 優化非同步處理和並發控制

4. **端到端監控建置**
   - 設計統一效能監控架構
   - 實施前後端指標收集系統
   - 建置效能異常檢測和告警機制
   - 設計效能趨勢分析儀表板

5. **效能測試實施**
   - 設計負載測試和壓力測試場景
   - 建立效能基準測試套件
   - 實施A/B測試和效能比較機制
   - 建置持續效能監控和回歸測試

6. **持續改善機制**
   - 建立效能優化反饋迴圈
   - 實施自動化效能監測
   - 設計效能優化建議引擎
   - 建立效能最佳實踐知識庫
</execution_steps>

<output_format>
- 效能優化實施方案（含技術細節）
- 監控系統架構設計文檔
- 效能測試報告和基準數據
- 持續改善機制說明
- 完整的效能開發文檔記錄
</output_format>

<constraints>
- 必須同時關注前端使用者體驗和後端系統效能
- 所有優化措施須有量化指標驗證
- 避免過度優化導致系統複雜度增加
- 優先考慮可維護性和擴展性
- 確保效能優化不影響功能正確性
</constraints>