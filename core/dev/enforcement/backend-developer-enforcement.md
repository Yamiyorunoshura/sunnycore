# Backend Developer 強制執行規範

<core_execution_protocol>
## 核心執行協議

<mandatory_prerequisites>
### 必要前置條件
- **建議**：在開始開發前載入統一工作流程與計劃；若缺失，於 dev_notes.validation_warnings 記錄並持續執行
- **工作流程讀取**：應讀取 `{project_root}/cursor-claude/core/dev/workflow/backend-developer-workflow.md`，若失敗則記錄警告
- **計劃檢查**：嘗試定位並讀取task_id的實施計劃；如缺失，記錄警告並以最小可行上下文繼續
</mandatory_prerequisites>

<workflow_compliance>
### 工作流程合規性
- **階段完整性**：絕不跳過工作流程階段，按順序執行所有階段
</workflow_compliance>
</core_execution_protocol>

<backend_specific_requirements>
## 後端專門強制要求

<data_security_integrity>
### 資料安全與完整性
- **資料變更**：必須草擬冪等和可逆的遷移
- **備份策略**：所有資料變更必須有回滾計劃
- **交易完整性**：確保ACID特性維護
</data_security_integrity>

<api_security>
### API安全
- **身份驗證**：必須實施完整的身份驗證機制
- **授權控制**：必須實施細粒度的授權控制
- **輸入驗證**：必須對所有輸入進行嚴格驗證
- **資料清理**：必須對所有輸出進行適當清理
- **機密處理**：絕不在日誌或回應中暴露敏感資訊
</api_security>

<performance_requirements>
### 效能要求
- **延遲目標**：必須達到計劃中指定的延遲要求
- **吞吐量目標**：必須達到計劃中指定的吞吐量要求
- **記憶體目標**：必須符合記憶體使用限制
- **監控實施**：必須實施適當的效能監控
</performance_requirements>

<testing_requirements>
### 測試要求
- **測試優先**：應先寫測試後寫實現；若未達成，記錄原因與補回計劃
- **測試類型**：
  - 單元測試：與F-IDs對齊
  - 整合測試：測試服務間互動
  - 契約測試：確保API契約遵守
- **覆蓋率門檻**：必須達到指定的測試覆蓋率要求
</testing_requirements>

<architecture_principles>
### 架構原則
- **SOLID原則**：必須應用SOLID設計原則
- **清潔架構**：必須實施關注點分離
- **錯誤處理**：必須實施適當的錯誤處理機制
- **日誌記錄**：必須實施結構化日誌記錄
- **監控**：必須實施適當的系統監控
</architecture_principles>

<reliability_requirements>
### 可靠性要求
- **優雅降級**：系統必須能優雅處理故障
- **冪等性**：API操作必須設計為冪等
- **重試機制**：必須實施適當的重試策略
- **斷路器**：必須實施斷路器模式處理依賴失敗
</reliability_requirements>

<quality_gates>
### 品質門檻
- **靜態分析**：代碼必須通過靜態分析檢查
- **安全掃描**：必須通過安全漏洞掃描
- **效能測試**：必須通過效能基準測試
- **相容性測試**：必須維護向後相容性
</quality_gates>
</backend_specific_requirements>

<security_checklist>
## 安全檢查清單
- [ ] 所有輸入都經過驗證和清理
- [ ] 所有輸出都經過適當編碼
- [ ] 敏感資料都經過加密存儲
- [ ] API都實施了適當的認證和授權
- [ ] 錯誤處理不暴露敏感資訊
- [ ] 日誌記錄不包含敏感資料
- [ ] 依賴項都是最新且安全的版本
</security_checklist>

<failure_handling_protocol>
## 失敗處理協議
- **計劃缺失**：記錄警告與已採取的替代資訊來源；繼續最小化實作
- **範圍偏離**：記錄偏離原因、影響與回補計劃；不中斷
- **安全檢查未達標**：記錄風險與緩解措施；標記為高優先修復
- **效能未達標**：記錄測量結果與優化計劃；在可控風險下續行
</failure_handling_protocol>