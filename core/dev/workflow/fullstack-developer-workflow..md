# 全端開發者工作流程
<workflow type="fullstack-developer">

## 強制前置條件驗證
<mandatory-preconditions>

### 1. 載入執行規範

<stage name="載入執行規範" number="1" critical="true">
**強制執行規範載入**
- **描述**: 完整讀取 `/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/fullstack-developer-enforcement.md`
- **要求**:
  <requirements>
  - 理解所有強制規則、全端開發標準和品質門檻
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
  - 理解專案需求、架構設計、前後端整合要求
  - 建立完整的專案上下文模型
  - 識別前後端依賴關係、API設計和資料流
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
  - 驗證計劃完整性、範圍定義和全端技術可行性
  - 確認前後端整合要求和效能目標
  <think hard>
  </requirements>

</stage>

### 3. 全端專門化準備

<stage name="全端專門化準備" number="3" critical="true">
**全端開發檢查清單準備**
根據強制執行規範準備全端檢查清單：

<fullstack-checklist>
<think hard>
- [ ] 分析計劃內容，識別前端和後端開發需求
- [ ] 確認API設計和資料庫架構
- [ ] 驗證前後端整合策略和安全要求
- [ ] 建立統一的測試驅動開發（TDD）策略
- [ ] 確認部署和DevOps流程
<think hard>
</fullstack-checklist>

**效能和安全目標確認**
確認並記錄全端效能要求：
<performance-targets>
<think>
- 前端載入時間和後端API響應時間目標
- 資料庫查詢效能和系統擴展性要求
- 安全性、可用性和監控策略
<think>
</performance-targets>
</stage>
</mandatory-preconditions>

---

## 執行協議
<execution-protocol>

### TDD全端開發流程
<stage name="TDD全端開發流程" number="4" critical="true">

#### 測試優先全端開發
嚴格遵循TDD原則進行全端開發：
<tdd-requirements>
<think harder>
- **先寫測試後寫實現（前端和後端）**
- **確保前後端整合測試覆蓋率達到要求門檻**
- **實施單元測試、整合測試、端到端測試**
- **API契約測試和資料庫測試**
<think harder>
</tdd-requirements>

#### 全端架構原則應用
在開發過程中應用以下原則：
<architecture-principles>
<think harder>
1. **前後端分離和API設計原則**
2. **統一的錯誤處理和日誌記錄機制**
3. **資料一致性和事務管理**
4. **安全性設計和身份驗證整合**
<think harder>
</architecture-principles>
</stage>

### 品質保證
<stage name="品質保證" number="5" critical="true">
#### 持續驗證
在開發過程中持續執行：
<quality-validations>
<think hard>
- **前後端靜態分析檢查**
- **全端安全漏洞掃描**
- **API效能和前端載入效能測試**
- **跨瀏覽器和響應式設計驗證**
- **資料庫效能和資料完整性檢查**
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
| **前後端整合失敗** | 記錄整合問題並制定修復計劃 |
| **效能未達標** | 記錄測量結果並制定優化計劃 |
| **安全檢查未通過** | 記錄風險並要求修復後繼續 |

<critical-failures>
**任何關鍵失敗都必須立即停止流程並報告**
</critical-failures>

</failure-handling>

</workflow>