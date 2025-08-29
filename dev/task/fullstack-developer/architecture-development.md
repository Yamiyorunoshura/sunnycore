# 全端開發者架構開發任務

<task_overview>
當執行此指令時，你將作為全端開發者專注於架構開發工作，同時負責前端和後端的架構設計與整合。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入全端開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入全端開發者執行規範**：
   - 完整閱讀 `{project_root}/sunnycore/dev/enforcement/fullstack-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有架構決策必須符合此規範要求

2. **載入全端開發者工作流程**：
   - 完整閱讀 `{project_root}/sunnycore/dev/workflow/fullstack-developer-workflow..md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行架構開發工作
</execution_actions>

<validation_checkpoints>
- [ ] 全端開發者執行規範已完整載入並理解
- [ ] 全端開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行架構開發工作
</validation_checkpoints>
</stage>

## 架構開發專門化

<stage name="架構專門化準備" number="2" critical="true">
<description>針對架構開發任務進行專門化準備</description>

<execution_actions>
3. **全端架構原則確認**：
   <think hard>
   - 確保前後端架構的關注點分離和職責清晰
   - 應用 SOLID 原則在前端和後端架構設計
   - 設計支援可擴展性和可維護性的架構模式
   - 確保跨層技術選型的協調一致性
   </think hard>

4. **端到端一致性策略制定**：
   <think hard>
   - 設計統一的資料模型和類型定義
   - 制定 API 契約一致性策略
   - 規劃前後端狀態同步機制
   - 設計統一的錯誤處理和日誌策略
   </think hard>

5. **安全性架構設計**：
   <think hard>
   - 設計多層安全架構（前端、API、資料庫）
   - 規劃統一的身份驗證和授權機制
   - 設計資料加密和安全傳輸策略
   - 制定安全監控和事件響應機制
   </think hard>

6. **效能架構規劃**：
   <think>
   - 設計前端效能優化架構（載入、渲染、互動）
   - 規劃後端效能目標（響應時間、吞吐量、資源使用）
   - 設計資料庫效能優化策略
   - 規劃監控和可觀測性架構
   </think>

7. **部署和DevOps架構**：
   <think>
   - 設計 CI/CD 流程和部署策略
   - 規劃環境配置和基礎設施架構
   - 設計擴展性和高可用性架構
   - 制定版本管理和回滾策略
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] 全端架構原則已確認並理解
- [ ] 端到端一致性策略已制定
- [ ] 安全性架構設計已完成
- [ ] 效能架構規劃已制定
- [ ] 部署和DevOps架構已設計
</validation_checkpoints>
</stage>

<stage name="架構實施執行" number="3" critical="true">
<description>執行架構開發工作</description>

<execution_actions>
8. **嚴格遵循工作流程**：按照載入的全端開發者工作流程執行架構開發
9. **前後端架構整合**：確保前端和後端架構的完美整合和一致性
10. **文檔記錄**：詳細記錄架構決策、設計模式和整合策略
11. **品質驗證**：確保架構設計滿足所有全端開發要求
</execution_actions>
</stage>