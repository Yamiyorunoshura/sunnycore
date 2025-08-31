# 後端開發強制執行規範

<purpose>
後端開發專家強制執行協議，確保安全性、效能和架構完整性
</purpose>

<core_execution_protocol>
## 核心執行協議

<mandatory_prerequisites>
### 必要前置條件
- 載入統一工作流程：讀取 `{project_root}/sunnycore/dev/workflow/backend-developer-workflow.md`
- 檢查實施計劃：定位task_id對應的開發計劃
- 失敗處理：缺失檔案時記錄警告，以最小可行上下文繼續執行
</mandatory_prerequisites>

<workflow_compliance>
### 工作流程合規
- 階段完整性：按順序執行所有工作流程階段
- 絕不跳過任何必要階段
</workflow_compliance>
</core_execution_protocol>

<backend_requirements>
## 後端專門要求

<data_security>
### 資料安全
- 草擬冪等和可逆的資料遷移
- 制定完整的回滾計劃
- 維護ACID交易完整性
</data_security>

<api_security>
### API安全
- 實施完整身份驗證機制
- 建立細粒度授權控制
- 嚴格驗證所有輸入
- 適當清理所有輸出
- 保護敏感資訊不在日誌或回應中暴露
</api_security>

<performance_standards>
### 效能標準
- 達到指定延遲要求
- 滿足吞吐量目標
- 符合記憶體使用限制
- 實施效能監控系統
</performance_standards>

<testing_standards>
### 測試標準
- 測試優先開發：先寫測試後寫實現
- 單元測試與F-IDs對齊
- 整合測試覆蓋服務間互動
- 契約測試確保API合規
- 達到指定測試覆蓋率門檻
</testing_standards>

<architecture_principles>
### 架構原則
- 應用SOLID設計原則
- 實施關注點分離
- 建立完善錯誤處理機制
- 實施結構化日誌記錄
- 部署系統監控
</architecture_principles>

<reliability_requirements>
### 可靠性要求
- 系統優雅故障處理
- API操作冪等性設計
- 實施重試策略
- 部署斷路器模式處理依賴失敗
</reliability_requirements>

<quality_gates>
### 品質門檻
- 通過靜態分析檢查
- 通過安全漏洞掃描
- 通過效能基準測試
- 維護向後相容性
</quality_gates>
</backend_requirements>

<security_checklist>
## 安全檢查清單
- [ ] 輸入驗證和清理
- [ ] 輸出適當編碼
- [ ] 敏感資料加密存儲
- [ ] API認證授權機制
- [ ] 錯誤處理資訊保護
- [ ] 日誌敏感資料過濾
- [ ] 依賴項安全更新
</security_checklist>

<failure_protocol>
## 失敗處理協議
- **計劃缺失**：記錄警告，採用替代資訊來源繼續執行
- **範圍偏離**：記錄偏離原因、影響和補救計劃
- **安全未達標**：記錄風險和緩解措施，標記高優先修復
- **效能未達標**：記錄測量結果和優化計劃，風險可控下繼續
</failure_protocol>