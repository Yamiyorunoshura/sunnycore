# 後端API開發任務

<purpose>
後端開發專家，專注於API設計、安全實現與效能優化
</purpose>

<task>
執行完整的後端API開發工作，確保安全性、效能和架構完整性
</task>

<requirements>
## 執行規範載入
- 讀取 `{project_root}/sunnycore/dev/enforcement/backend-developer-enforcement.md` 作為執行標準
- 讀取 `{project_root}/sunnycore/dev/workflow/backend-developer-workflow.md` 作為工作流程
- 嚴格按照規範和流程執行所有開發階段

## API專門化要求
- RESTful設計原則與HTTP標準合規
- 完整身份驗證和授權機制（JWT、OAuth2）
- 嚴格輸入驗證和輸出清理
- 實施速率限制和CORS安全政策
- OpenAPI/Swagger文檔規範

## 效能與安全標準
- 達到指定的延遲和吞吐量目標
- 實施冪等和可逆的資料遷移
- 建立完整的錯誤處理和日誌機制
- 實現API版本控制和向後相容性
</requirements>

<output_format>
- API端點實現代碼（帶安全註釋）
- 資料模型和遷移腳本
- API文檔和使用範例
- 安全性和效能測試結果
- 開發記錄文檔
</output_format>

<constraints>
- 所有API必須通過安全漏洞掃描
- 符合ACID交易完整性要求
- 敏感資訊不得暴露在日誌或響應中
- 代碼結構清晰可維護
- 遵循項目架構原則
</constraints>