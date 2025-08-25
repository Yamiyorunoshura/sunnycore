# 重構開發者工作流程
<workflow type="refactor-developer">

## 強制前置條件驗證
<mandatory-preconditions>

### 1. 載入執行規範

<stage name="載入執行規範" number="1" critical="true">
**強制執行規範載入**
- **描述**: 完整讀取 `~/cursor-claude/core/dev/enforcement/refactor-developer-enforcement.md`
- **要求**:
  <requirements>
  - 理解所有強制規則、重構標準和品質門檻
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
  - 理解專案需求、架構設計、代碼品質標準
  - 建立完整的專案上下文模型
  - 識別現有代碼的技術債務和改進機會
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
  - 驗證計劃完整性、範圍定義和重構可行性
  - 確認重構目標和品質提升要求
  <think hard>
  </requirements>

</stage>

### 3. 重構專門化準備

<stage name="重構專門化準備" number="3" critical="true">
**重構檢查清單準備**
根據強制執行規範準備重構檢查清單：

<refactor-checklist>
<think harder>
- [ ] 分析計劃內容，識別重構範圍和目標
- [ ] 評估現有代碼品質和技術債務
- [ ] 確認重構策略和風險評估
- [ ] 建立漸進式重構和測試驅動開發（TDD）策略
- [ ] 驗證向後相容性和效能影響
<think harder>
</refactor-checklist>

**品質目標確認**
確認並記錄重構品質要求：
<quality-targets>
<think>
- 代碼可讀性和維護性改進目標
- 效能優化和資源使用改善
- 技術債務減少和架構改良指標
<think>
</quality-targets>
</stage>
</mandatory-preconditions>

---

## 開發執行流程
<development-execution>

### 4. 重構分析流程

<stage name="重構分析" number="4" critical="true">
**深度代碼分析**
- **描述**: 全面分析現有代碼結構和重構需求
- **要求**:
  <requirements>
  <Ultra think>
  - 識別代碼異味和設計模式問題
  - 分析依賴關係和耦合度
  - 評估重構風險和影響範圍
  - 制定詳細的重構步驟計劃
  <Ultra think>
  </requirements>

**重構策略制定**
根據分析結果制定重構策略：
<refactor-strategy>
<think harder>
- 確定重構優先級和執行順序
- 選擇適當的重構技術和模式
- 建立安全網測試和回滾機制
- 制定漸進式交付計劃
<think harder>
</refactor-strategy>
</stage>

### 5. TDD重構流程

<stage name="測試驅動重構" number="5" critical="true">
**按照TDD流程進行重構**
- **描述**: 遵循測試先行的重構方法論
- **要求**:
  <requirements>
  <Ultra think>
  - 建立全面的測試覆蓋，確保重構安全
  - 採用小步驟、高頻率的重構策略
  - 持續驗證功能正確性和效能表現
  - 維護代碼品質和設計原則
  <Ultra think>
  </requirements>

**重構執行檢查點**
在重構過程中持續驗證：
<refactor-checkpoints>
<think hard>
- 每個重構步驟後的測試通過率
- 代碼覆蓋率和品質指標改善
- 效能指標和資源使用變化
- 架構一致性和設計原則遵循
<think hard>
</refactor-checkpoints>
</stage>
</development-execution>
</workflow>