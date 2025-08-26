# 前端開發者框架開發任務

<task_overview>
當執行此指令時，你將作為前端開發者專注於前端框架開發工作。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入前端開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入前端開發者執行規範**：
   - 完整閱讀 `~/cursor-claude/core/dev/enforcement/frontend-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有開發決策必須符合此規範要求

2. **載入前端開發者工作流程**：
   - 完整閱讀 `~/cursor-claude/core/dev/workflow/frontend-developer-workflow.md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行框架開發工作
</execution_actions>

<validation_checkpoints>
- [ ] 前端開發者執行規範已完整載入並理解
- [ ] 前端開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行框架開發工作
</validation_checkpoints>
</stage>

## 框架開發專門化

<stage name="框架專門化準備" number="2" critical="true">
<description>針對前端框架開發任務進行專門化準備</description>

<execution_actions>
3. **框架架構設計原則確認**：
   <think>
   - 遵循組件化設計原則和SOLID設計模式
   - 確保框架的可重用性和可擴展性
   - 考慮組件間的依賴關係和通信機制
   - 制定一致的API設計和命名規範
   </think>

4. **UI/UX框架要求特化**：
   <think hard>
   - 設計系統和主題管理架構
   - 響應式設計和跨設備適應性
   - 無障礙性（A11Y）框架支援
   - 使用者體驗一致性和互動模式
   - 設計Token系統和樣式架構
   </think hard>

5. **框架效能優化策略**：
   <think>
   - 代碼分割和懶載入機制
   - 組件渲染優化和記憶化策略
   - Bundle大小控制和Tree Shaking
   - 效能監控和測量工具整合
   - 載入時間和互動響應優化
   </think>

6. **框架測試策略**：
   <think>
   - 單元測試框架和測試工具配置
   - 組件測試和整合測試策略
   - E2E測試和視覺回歸測試
   - 無障礙性測試和效能測試
   - 測試覆蓋率目標和品質門檻
   </think>

7. **框架文檔和開發者體驗**：
   <think>
   - 組件API文檔和使用範例
   - Storybook或組件展示系統
   - 開發者指南和最佳實踐文檔
   - TypeScript類型定義和IDE支援
   - 框架升級和遷移指南
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] 框架架構設計原則已確認並理解
- [ ] UI/UX框架要求已明確定義
- [ ] 效能優化策略已制定
- [ ] 測試策略已準備
- [ ] 文檔和開發者體驗要求已明確
</validation_checkpoints>
</stage>

<stage name="框架技術棧專門化" number="3" critical="true">
<description>針對具體的前端框架技術進行專門化配置</description>

<execution_actions>
8. **現代前端框架整合**：
   <think hard>
   - React/Vue/Angular等主流框架適配
   - 狀態管理解決方案（Redux、Vuex、NgRx等）
   - 路由管理和代碼分割策略
   - 服務端渲染（SSR）和靜態生成（SSG）支援
   - 微前端架構考量和實施策略
   </think hard>

9. **開發工具鏈整合**：
   <think>
   - 構建工具配置（Webpack、Vite、Rollup等）
   - 開發服務器和熱重載配置
   - 代碼品質工具（ESLint、Prettier、TypeScript）
   - CI/CD整合和自動化部署
   - 版本管理和發布策略
   </think>

10. **跨平台和相容性**：
    <think>
    - 瀏覽器相容性策略和Polyfill管理
    - 移動端適配和PWA功能支援
    - 多語言國際化（i18n）架構
    - 主題切換和深色模式支援
    - 向後相容性和遷移策略
    </think>
</execution_actions>

<validation_checkpoints>
- [ ] 前端框架技術棧已選定並配置
- [ ] 開發工具鏈已整合並測試
- [ ] 跨平台相容性策略已制定
- [ ] 國際化和主題系統已準備
</validation_checkpoints>
</stage>

<stage name="開發執行" number="4" critical="true">
<description>執行框架開發工作</description>

<execution_actions>
11. **嚴格遵循工作流程**：按照載入的前端開發者工作流程執行
12. **專項驗證**：確保所有框架相關的無障礙性、效能和可用性要求得到滿足
13. **文檔記錄**：詳細記錄框架架構、組件設計和使用指南
14. **品質保證**：執行完整的測試套件和效能審核
</execution_actions>

<validation_checkpoints>
- [ ] 框架開發工作已按流程執行
- [ ] 無障礙性和效能要求已驗證
- [ ] 文檔和使用指南已完成
- [ ] 品質門檻已通過
</validation_checkpoints>
</stage>