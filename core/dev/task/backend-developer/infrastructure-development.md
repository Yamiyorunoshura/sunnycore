# 後端開發者基礎設施開發任務

<task_overview>
當執行此指令時，你將作為後端開發者專注於基礎設施開發工作。
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
   - 嚴格按照流程步驟執行基礎設施開發工作
</execution_actions>

<validation_checkpoints>
- [ ] 後端開發者執行規範已完整載入並理解
- [ ] 後端開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行基礎設施開發工作
</validation_checkpoints>
</stage>

## 基礎設施開發專門化

<stage name="基礎設施專門化準備" number="2" critical="true">
<description>針對基礎設施開發任務進行專門化準備</description>

<execution_actions>
3. **容器化和部署原則確認**：
   - 遵循Docker最佳實踐和容器安全標準
   - 確保容器映像的最小化和安全性
   - 考慮多階段構建和層優化策略

4. **雲端架構要求特化**：
   - 基礎設施即代碼(IaC)原則
   - 自動化部署和CI/CD流水線
   - 資源監控和自動擴展配置

5. **安全性和合規性策略**：
   - 網路安全和防火牆配置
   - 存取控制和身份管理
   - 日誌收集和安全審計

6. **監控和可觀察性設定**：
   - 系統監控和告警機制
   - 效能指標收集和分析
   - 故障檢測和自動恢復
</execution_actions>

<validation_checkpoints>
- [ ] 容器化和部署原則已確認
- [ ] 雲端架構要求已明確
- [ ] 安全性和合規性策略已制定
- [ ] 監控和可觀察性設定已準備
</validation_checkpoints>
</stage>

<stage name="開發執行" number="3" critical="true">
<description>執行基礎設施開發工作</description>

<execution_actions>
7. **嚴格遵循工作流程**：按照載入的後端開發者工作流程執行
8. **專項驗證**：確保所有基礎設施相關的安全性和效能要求得到滿足
9. **文檔記錄**：詳細記錄基礎設施架構、部署流程和監控配置
</execution_actions>
</stage>