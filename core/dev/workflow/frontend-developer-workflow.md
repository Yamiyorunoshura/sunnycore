# 前端開發者工作流程
<workflow type="frontend-developer">

## 強制前置條件驗證
<mandatory-preconditions>

### 1. 載入執行規範

<stage name="載入執行規範" number="1" critical="true">
**強制執行規範載入**
- **描述**: 完整讀取 `/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/frontend-developer-enforcement.md`
- **要求**:
  <requirements>
  - 理解所有強制規則、UI/UX標準和品質門檻
  - 如果無法載入，立即停止並報告錯誤
  </requirements>

</stage>

### 2. 專案上下文建立

<stage name="專案上下文建立" number="2" critical="true">

**專案規範理解**

- **描述**: 讀取 `{project_root}/docs/specs/` 路徑下的所有文檔
- **要求**:
  <requirements>
  <think hard>
  - 理解專案需求、設計系統、使用者體驗要求
  - 建立完整的專案上下文模型
  - 識別UI/UX依賴關係和無障礙要求
  <think hard>
  </requirements>

**實施計劃驗證**
- **描述**: 確認 `{project_root}/docs/implementation-plan/{task_id}`(如`1`, `2`, `3`...)-plan.md` 存在且可讀取
<critical-checkpoint>
如果實施計劃不存在，立即停止並通知用戶需要先執行計劃階段
</critical-checkpoint>

- **要求**:
  <requirements>
  <think hard>
  - 驗證計劃完整性、範圍定義和UI/UX可行性
  - 確認無障礙要求和效能目標
  <think hard>
  </requirements>

</stage>

### 3. 前端專門化準備

<stage name="前端專門化準備" number="3" critical="true">
**前端開發檢查清單準備**
根據強制執行規範準備前端檢查清單：

<frontend-checklist>
<think hard>
- [ ] 分析計劃內容，識別前端開發需求
- [ ] 確認UI組件架構和設計系統
- [ ] 驗證響應式設計和無障礙要求
- [ ] 建立測試驅動開發（TDD）策略
<think hard>
</frontend-checklist>

**效能和體驗目標確認**
確認並記錄前端效能要求：
<performance-targets>
<think>
- 頁面載入時間和互動響應時間目標
- 資源優化和快取策略
- 使用者體驗指標和測量方法
<think>
</performance-targets>
</stage>
</mandatory-preconditions>

---

## 開發執行流程
<development-execution>

### 4. TDD開發流程

<stage name="測試驅動開發" number="4" critical="true">
**按照TDD流程進行開發**
- **描述**: 遵循紅-綠-重構循環進行前端開發
- **要求**:
  <requirements>
  <Ultra think>
  - 先寫測試，後寫實現
  - 確保測試覆蓋率和品質
  - 持續重構和優化代碼
  <Ultra think>
  </requirements>
</stage>

</development-execution>
</workflow>