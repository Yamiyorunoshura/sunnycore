# 後端開發者測試開發任務

<task_overview>
當執行此指令時，你將作為後端開發者專注於測試開發工作。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入後端開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入後端開發者執行規範**：
   - 完整閱讀 `/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/backend-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有測試開發決策必須符合此規範要求

2. **載入後端開發者工作流程**：
   - 完整閱讀 `/Users/tszkinlai/Coding/AI workflow/core/dev/workflow/backend-developer-workflow.md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行測試開發工作
</execution_actions>

<validation_checkpoints>
- [ ] 後端開發者執行規範已完整載入並理解
- [ ] 後端開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行測試開發工作
</validation_checkpoints>
</stage>

## 測試開發專門化

<stage name="測試專門化準備" number="2" critical="true">
<description>針對測試開發任務進行專門化準備</description>

<execution_actions>
3. **測試策略確立**：
   <think>
   - 確定測試金字塔策略（單元測試、整合測試、端對端測試）
   - 制定測試驅動開發（TDD）流程
   - 建立測試覆蓋率目標和品質門檻
   </think>

4. **測試類型專門化**：
   <think hard>
   - 單元測試：函數、方法、類別層級的隔離測試
   - 整合測試：組件間交互和外部依賴測試
   - 契約測試：API 介面和資料契約驗證
   - 效能測試：負載、壓力、容量測試
   - 安全測試：漏洞掃描和安全性驗證
   </think hard>

5. **測試工具和框架選擇**：
   <think>
   - 單元測試框架配置和最佳實踐
   - Mock 和 Stub 工具使用策略
   - 測試資料生成和管理
   - 持續整合測試管道設計
   </think>

6. **測試品質保證**：
   <think>
   - 測試程式碼品質標準
   - 測試可維護性和可讀性要求
   - 測試執行效能優化
   - 失敗測試的診斷和修復流程
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] 測試策略已確立並文檔化
- [ ] 各類型測試要求已明確定義
- [ ] 測試工具和框架已選擇配置
- [ ] 測試品質保證標準已建立
</validation_checkpoints>
</stage>

<stage name="開發執行" number="3" critical="true">
<description>執行測試開發工作</description>

<execution_actions>
7. **嚴格遵循工作流程**：按照載入的後端開發者工作流程執行
8. **專項驗證**：確保所有測試相關的覆蓋率和品質要求得到滿足
9. **文檔記錄**：詳細記錄測試架構、測試案例和自動化配置
</execution_actions>
</stage>