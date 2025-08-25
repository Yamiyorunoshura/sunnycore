# 後端開發者 API 開發任務

<task_overview>
當執行此指令時，你將作為後端開發者專注於 API 開發工作。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入後端開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入後端開發者執行規範**：
   - 完整閱讀 `/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/backend-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有開發決策必須符合此規範要求

2. **載入後端開發者工作流程**：
   - 完整閱讀 `/Users/tszkinlai/Coding/AI workflow/core/dev/workflow/backend-developer-workflow.md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行 API 開發工作
</execution_actions>

<validation_checkpoints>
- [ ] 後端開發者執行規範已完整載入並理解
- [ ] 後端開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行 API 開發工作
</validation_checkpoints>
</stage>

## API 開發專門化

<stage name="API 專門化準備" number="2" critical="true">
<description>針對 API 開發任務進行專門化準備</description>

<execution_actions>
3. **API 設計原則確認**：
   <think>
   - 遵循 RESTful 設計原則和 HTTP 標準
   - 確保 API 介面一致性和可擴展性
   - 考慮版本控制和向後相容性策略
   </think>

4. **API 安全性要求特化**：
   <think hard>
   - 身份驗證和授權機制（JWT、OAuth2 等）
   - 輸入驗證和參數清理
   - 速率限制和 DDoS 防護
   - CORS 政策和安全標頭設定
   </think hard>

5. **API 效能監控策略**：
   <think>
   - 響應時間和吞吐量監控
   - 錯誤率和可用性追蹤
   - API 使用分析和效能優化
   - 負載測試和壓力測試計劃
   </think>

6. **API 文檔和規範**：
   <think>
   - OpenAPI/Swagger 規範文檔
   - 請求/響應範例和錯誤碼定義
   - API 使用指南和最佳實踐
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] API 設計原則已確認並理解
- [ ] API 安全性要求已明確定義
- [ ] 效能監控策略已制定
- [ ] API 文檔規範已準備
</validation_checkpoints>
</stage>

<stage name="開發執行" number="3" critical="true">
<description>執行 API 開發工作</description>

<execution_actions>
6. **嚴格遵循工作流程**：按照載入的後端開發者工作流程執行
7. **專項驗證**：確保所有資料庫相關的安全性和效能要求得到滿足
8. **文檔記錄**：詳細記錄資料庫架構、查詢優化和安全措施
</execution_actions>
</stage>