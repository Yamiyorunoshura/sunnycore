# 前端開發者工作流程

<enforcement>
## 🔄 工作流程Todo List製作

### 📋 開始執行前的必要準備

**重要提醒**: 在開始執行任何工作流程步驟之前，必須使用使用待辦事項列表來創建一個待辦事項列表來組織這些步驟。

**製作流程**:
1. **分析工作流程結構** - 仔細閱讀整個workflow文件，識別所有階段、步驟和任務
2. **提取關鍵任務** - 將每個階段的核心任務轉換為具體的todo項目
3. **設定優先級** - 根據任務的重要性和依賴關係設定優先級
4. **創建Todo List** - 使用`todo_write`工具創建包含所有步驟的結構化todo list
5. **執行與更新** - 按照todo list順序執行任務，及時更新狀態

### 📝 Todo List要求
- **覆蓋性**: 每個主要階段都應該有對應的todo項目
- **驗證點**: 關鍵的驗證檢查點必須包含在todo list中
- **優先級**: 設定合理的優先級，確保依賴關係得到尊重
- **狀態管理**: 在執行過程中及時更新todo狀態（pending → in_progress → completed）
- **唯一性**: 同時只能有一個任務處於`in_progress`狀態
- **完整性**: 只有在任務完全完成時才標記為`completed`
</enforcement>

---

<workflow type="frontend-developer">

## 強制前置條件驗證
<mandatory-preconditions>

### 1. 載入執行規範

<stage name="載入執行規範" number="1" critical="true">
**強制執行規範載入**
- **描述**: 完整讀取 `~/cursor-claude/core/dev/enforcement/frontend-developer-enforcement.md`
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
  <think>
  前端開發者需要專注於以下類型的專案規範內容：
  
  1. **使用者介面規範**：
     - UI設計系統和組件庫規範
     - 視覺設計指南（顏色、字體、間距）
     - 互動設計模式和動畫效果
     - 響應式設計斷點和佈局策略
  
  2. **使用者體驗規範**：
     - 使用者旅程和流程設計
     - 無障礙設計要求（WCAG合規性）
     - 使用者研究洞察和痛點分析
     - 介面可用性和導航結構
  
  3. **技術架構規範**：
     - 前端框架選擇和配置
     - 狀態管理策略和資料流設計
     - API整合和資料結構定義
     - 組件架構和程式碼組織結構
  
  4. **效能和優化規範**：
     - 載入時間和效能基準
     - 資源優化策略（圖片、字體、程式碼分割）
     - 快取策略和CDN配置
     - SEO要求和meta標籤規範
  
  5. **相容性和測試規範**：
     - 瀏覽器支援矩陣
     - 裝置和螢幕尺寸相容性
     - 測試策略（單元測試、整合測試、E2E測試）
     - 品質保證檢查清單
  </think>
  
  基於上述思維分析，執行以下任務：
  - 理解專案需求、設計系統、使用者體驗要求
  - 建立完整的專案上下文模型
  - 識別UI/UX依賴關係和無障礙要求
  - 特別關注前端系統的組件架構、使用者互動流程和視覺設計規範
  - 確認效能基準和相容性要求
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