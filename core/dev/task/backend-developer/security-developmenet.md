# 後端開發者安全開發任務

<task_overview>
當執行此指令時，你將作為後端開發者專注於安全開發工作。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入後端開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入後端開發者執行規範**：
   - 完整閱讀 `/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/backend-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有安全開發決策必須符合此規範要求

2. **載入後端開發者工作流程**：
   - 完整閱讀 `/Users/tszkinlai/Coding/AI workflow/core/dev/workflow/backend-developer-workflow.md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行安全開發工作
</execution_actions>

<validation_checkpoints>
- [ ] 後端開發者執行規範已完整載入並理解
- [ ] 後端開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行安全開發工作
</validation_checkpoints>
</stage>

## 安全開發專門化

<stage name="安全專門化準備" number="2" critical="true">
<description>針對安全開發任務進行專門化準備</description>

<execution_actions>
3. **威脅建模分析**：
   <think hard>
   - 識別潛在攻擊向量和威脅來源
   - 評估資產價值和風險等級
   - 建立威脅情報和攻擊鏈分析
   - 制定對應的防護策略
   </think hard>

4. **安全架構設計**：
   <think>
   - 零信任架構原則應用
   - 深度防禦策略實施
   - 最小權限原則確保
   - 安全邊界和隔離設計
   </think>

5. **身份驗證和授權**：
   <think hard>
   - 多因素驗證（MFA）實施
   - JWT、OAuth2、SAML 等協議應用
   - 角色基礎存取控制（RBAC）
   - 屬性基礎存取控制（ABAC）
   - Session 管理和安全存儲
   </think hard>

6. **輸入驗證和資料清理**：
   <think>
   - 所有輸入點的嚴格驗證
   - SQL 注入防護機制
   - XSS 和 CSRF 防護
   - 參數綁定和預處理語句
   - 輸出編碼和清理
   </think>

7. **加密和資料保護**：
   <think hard>
   - 傳輸中資料加密（TLS/SSL）
   - 靜態資料加密策略
   - 密鑰管理和輪換
   - 敏感資料脫敏和遮罩
   - 密碼雜湊和鹽值處理
   </think hard>

8. **安全監控和日誌**：
   <think>
   - 安全事件監控和告警
   - 日誌收集和分析系統
   - 異常行為檢測
   - 審計追蹤和合規報告
   - 即時威脅回應機制
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] 威脅建模分析已完成並記錄
- [ ] 安全架構設計已制定並驗證
- [ ] 身份驗證和授權機制已設計
- [ ] 輸入驗證和資料清理策略已確認
- [ ] 加密和資料保護措施已規劃
- [ ] 安全監控和日誌系統已準備
</validation_checkpoints>
</stage>

<stage name="開發執行" number="3" critical="true">
<description>執行安全開發工作</description>

<execution_actions>
9. **嚴格遵循工作流程**：按照載入的後端開發者工作流程執行
10. **安全測試實施**：進行滲透測試、漏洞掃描和安全代碼審查
11. **合規性驗證**：確保符合相關安全標準和法規要求
12. **文檔記錄**：詳細記錄安全架構、威脅模型和安全措施
</execution_actions>
</stage>