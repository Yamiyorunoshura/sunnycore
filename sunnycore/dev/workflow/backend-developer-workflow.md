# 後端開發者工作流程

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

<workflow type="backend-developer">

## 強制前置條件驗證
<mandatory-preconditions>

### 1. 載入執行規範

<stage name="載入執行規範" number="1" critical="true">
**強制執行規範載入**
- **描述**: 完整讀取 `{project_root}/sunnycore/dev/enforcement/backend-developer-enforcement.md`
- **要求**:
  <requirements>
  - 理解所有強制規則、安全要求和品質門檻
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
  後端開發者需要專注於以下類型的專案規範內容：
  
  1. **系統架構規範**：
     - 微服務架構設計
     - 資料庫設計和關係模型
     - API介面設計和通訊協議
     - 系統整合點和外部依賴
  
  2. **安全性規範**：
     - 身份驗證和授權策略
     - 資料加密和隱私保護要求
     - API安全標準和速率限制
     - 安全漏洞防護機制
  
  3. **效能和可擴展性規範**：
     - 效能指標和基準測試要求
     - 負載處理和擴展策略
     - 快取策略和資料優化
     - 監控和日誌記錄要求
  
  4. **資料管理規範**：
     - 資料模型和結構設計
     - 資料遷移和版本控制策略
     - 備份和災難恢復計劃
     - 資料完整性和一致性要求
  
  5. **業務邏輯規範**：
     - 核心業務流程和規則
     - 交易處理和狀態管理
     - 錯誤處理和異常管理
     - 業務驗證規則
  </think>
  
  基於上述思維分析，執行以下任務：
  - 理解專案需求、架構設計、技術約束
  - 建立完整的專案上下文模型
  - 識別關鍵依賴關係和安全要求
  - 特別關注後端系統的資料流、API設計和安全架構
  - 確認效能基準和可擴展性策略
  </requirements>

**實施計劃驗證**
- **描述**: 確認 `{project_root}/docs/implementation-plan/{task_id}`(如`1`, `2`, `3`...)-plan.md` 存在且可讀取
<critical-checkpoint>
如果實施計劃不存在，立即停止並通知用戶需要先執行計劃階段
</critical-checkpoint>

- **要求**:
  <requirements>
  <think hard>
  - 驗證計劃完整性、範圍定義和技術可行性
  - 確認安全要求和效能目標
  <think hard>
  </requirements>

</stage>

### 3. 後端專門化準備

<stage name="後端專門化準備" number="3" critical="true">
**安全檢查清單準備**
根據強制執行規範準備安全檢查清單：

<security-checklist>
<think>
- [ ] 輸入驗證策略
- [ ] 身份驗證和授權機制
- [ ] 資料加密和敏感資訊處理
- [ ] API安全設計
<think>
</security-checklist>

**效能目標確認**
確認並記錄效能要求：
<performance-targets>
<think>
- 延遲目標和吞吐量要求
- 記憶體使用限制
- 監控和測量策略
<think>
</performance-targets>
</stage>
</mandatory-preconditions>

---

## 執行協議
<execution-protocol>

### TDD開發流程
<stage name="TDD開發流程" number="4" critical="true">

#### 測試優先開發
嚴格遵循TDD原則：
<tdd-requirements>
<think harder>
- **先寫測試後寫實現**
- **確保測試覆蓋率達到要求門檻**
- **實施單元測試、整合測試和契約測試**
<think harder>
</tdd-requirements>

#### 架構原則應用
在開發過程中應用以下原則：
<architecture-principles>
<think harder>
1. **SOLID設計原則**
2. **清潔架構和關注點分離**
3. **錯誤處理和日誌記錄機制**
<think harder>
</architecture-principles>
</stage>

### 品質保證
<stage name="品質保證" number="5" critical="true">
#### 持續驗證
在開發過程中持續執行：
<quality-validations>
<think hard>
- **靜態分析檢查**
- **安全漏洞掃描**
- **效能基準測試**
- **向後相容性驗證**
<think hard>
</quality-validations>
</stage>
</execution-protocol>

---

## 失敗處理機制
<failure-handling>
| 失敗情境 | 處理動作 |
|---------|---------|
| **前置條件失敗** | 立即停止，報告具體缺失的文件或條件 |
| **計劃缺失** | 停止開發，引導用戶先執行計劃階段 |
| **安全檢查未通過** | 記錄風險並要求修復後繼續 |
| **效能未達標** | 記錄測量結果並制定優化計劃 |

<critical-failures>
**任何關鍵失敗都必須立即停止流程並報告**
</critical-failures>

</failure-handling>

</workflow>
