# 後端開發者工作流程
<workflow type="backend-developer">

## 強制前置條件驗證
<mandatory-preconditions>

### 1. 載入執行規範

<stage name="載入執行規範" number="1" critical="true">
**強制執行規範載入**
- **描述**: 完整讀取 `/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/backend-developer-enforcement.md`
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
  <think hard>
  - 理解專案需求、架構設計、技術約束
  - 建立完整的專案上下文模型
  - 識別關鍵依賴關係和安全要求
  <think hard>
  </requirements>

**實施計劃驗證**
- **描述**: 確認 `{project_root}/docs/implementation-plan/{task_id}-plan.md` 存在且可讀取
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
