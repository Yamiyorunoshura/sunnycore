# 重構開發者工作流程

<purpose>
專業重構開發專家，專注於代碼品質提升和技術債務消除
</purpose>

<enforcement>
## 🔄 工作流程Todo List製作

### 📋 開始執行前的必要準備

**重要提醒**: 在開始執行任何工作流程步驟之前，必須使用待辦事項列表來創建一個待辦事項列表來組織這些步驟。

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

<workflow type="refactor-developer">

## 強制前置條件驗證

### 1. 載入執行規範

<task>
完整讀取 `{project_root}/sunnycore/dev/enforcement/refactor-developer-enforcement.md`
</task>

<requirements>
- 理解所有強制規則、重構標準和品質門檻
- 如果無法載入，立即停止並報告錯誤
</requirements>

### 2. 專案上下文建立

<task>
建立完整的專案重構上下文，包含規範理解和實施計劃驗證
</task>

<requirements>
- 讀取 `{project_root}/docs/specs/` 路徑下的所有文檔
- 理解專案需求、現有架構設計和代碼品質標準
- 建立技術債務、效能瓶頸和維護性問題的上下文模型
- 識別重構目標區域、風險點和依賴關係
- 確認實施計劃存在：`{project_root}/docs/implementation-plan/{task_id}-plan.md`
- 驗證計劃完整性、範圍定義和重構可行性
</requirements>

<constraints>
如果實施計劃不存在，立即停止並通知用戶需要先執行計劃階段
</constraints>

### 3. 重構專門化準備

<task>
根據執行規範準備重構檢查清單和品質目標
</task>

<requirements>
- 分析計劃內容，識別重構範圍和目標
- 評估現有代碼品質和技術債務
- 確認重構策略和風險評估
- 建立漸進式重構和TDD策略
- 驗證向後相容性和效能影響
- 設定代碼可讀性、效能優化和技術債務減少目標
</requirements>

## 開發執行流程

### 4. 重構分析流程

<task>
執行深度代碼分析並制定重構策略
</task>

<requirements>
- 識別代碼異味和設計模式問題
- 分析依賴關係和耦合度
- 評估重構風險和影響範圍
- 制定詳細的重構步驟計劃
- 確定重構優先級和執行順序
- 選擇適當的重構技術和模式
- 建立安全網測試和回滾機制
- 制定漸進式交付計劃
</requirements>

### 5. TDD重構執行

<task>
按照測試驅動開發流程執行重構
</task>

<requirements>
- 建立全面的測試覆蓋，確保重構安全
- 採用小步驟、高頻率的重構策略
- 持續驗證功能正確性和效能表現
- 維護代碼品質和設計原則
- 監控測試通過率和覆蓋率
- 追蹤效能指標和資源使用變化
- 確保架構一致性和設計原則遵循
</requirements>

<output_format>
- 重構執行報告（包含改進指標）
- 測試結果和覆蓋率報告
- 效能基準對比分析
- 技術債務減少量化報告
</output_format>

</workflow>