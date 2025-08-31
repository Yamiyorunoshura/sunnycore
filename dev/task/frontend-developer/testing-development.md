# 前端開發者 測試開發任務

<purpose>
前端開發專家，專注於現代前端測試架構設計與實施
</purpose>

<task>
執行前端測試開發工作，建立完整的測試體系和自動化測試流程
</task>

## 前置配置

<requirements>
1. **執行規範載入**：
   - 讀取 `{project_root}/sunnycore/dev/enforcement/frontend-developer-enforcement.md`
   - 作為唯一執行標準

2. **工作流程載入**：
   - 讀取 `{project_root}/sunnycore/dev/workflow/frontend-developer-workflow.md`
   - 嚴格按照流程執行

3. **測試技術規範**：
   - 單元測試：Jest/Vitest + Testing Library
   - 整合測試：組件交互和API測試
   - E2E測試：Playwright/Cypress
   - 視覺回歸：Chromatic/Percy
   - 效能測試：Lighthouse CI
</requirements>

## 測試策略配置

<test_pyramid>
- **單元測試 (70%)**：組件邏輯、工具函數、狀態管理
- **整合測試 (20%)**：組件交互、API整合、路由測試  
- **E2E測試 (10%)**：關鍵用戶流程、跨瀏覽器測試
</test_pyramid>

<automation_requirements>
- CI/CD流程整合
- 自動測試報告生成
- 覆蓋率分析和監控
- 失敗測試自動重試機制
- 測試數據管理和清理
</automation_requirements>

## 測試實施要求

<code_quality>
- 測試覆蓋率：分支覆蓋 ≥ 80%，行覆蓋 ≥ 90%
- 測試命名：描述性命名，清楚表達測試意圖
- 測試組織：按功能模組分組，使用describe/context結構
- 測試數據：使用Factory模式或Mock Service Worker
</code_quality>

<testing_practices>
- 遵循AAA模式（Arrange-Act-Assert）
- 每個測試只測試一個行為
- 使用數據測試驅動複雜場景
- 模擬外部依賴和API調用
- 測試錯誤處理和邊界條件
</testing_practices>

## 輸出要求

<deliverables>
- 完整測試套件實施
- 測試配置和設定文件
- CI/CD測試流程配置
- 測試文檔和執行指南
- 測試覆蓋率報告分析
</deliverables>

<constraints>
- 避免脆弱測試（brittle tests）
- 優先測試行為而非實現細節
- 保持測試執行速度和穩定性
- 確保測試環境隔離性
</constraints>