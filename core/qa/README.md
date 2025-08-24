# Dr. Thompson QA統帥架構

## 架構概述

Dr. Thompson QA統帥架構是一個專業化的品質審查系統，將原本單一的task-reviewer拆分為多個專業reviewer，由Dr. Thompson統一協調，實現並行審查和專業化評估。

## 核心架構

### Dr. Thompson - QA統帥
- **角色定位**：軟體工程品質的最後防線，擁有三十年品質審查經驗
- **統帥職責**：分析任務類型、組建專業團隊、協調並行審查、整合專業意見、做出最終判斷
- **權威地位**：擁有最終品質判斷權，可以調整、合併或推翻任何reviewer的意見

### 專業Reviewer團隊

#### 核心Reviewer（必選）
- **`task-reviewer:code-quality`** 🟦：代碼品質、架構設計、最佳實踐
- **`task-reviewer:testing`** 🟩：測試覆蓋率、測試策略、自動化測試

#### 專業Reviewer（按需選擇）
- **`task-reviewer:security`** 🔴：安全漏洞、認證授權、數據保護
- **`task-reviewer:performance`** 🟠：性能優化、資源使用、擴展性
- **`task-reviewer:documentation`** 🟣：技術文檔、用戶文檔、API文檔
- **`task-reviewer:integration`** 🔵：系統整合、API設計、數據流

## 工作流程

### 1. 任務分析與團隊組建
- 分析任務類型和複雜度
- 根據任務類型自動選擇專業reviewer
- 支援手動指定reviewer組合

### 2. 並行審查執行
- 所有選定的reviewer同時進行專業審查
- 每個reviewer專注於特定品質維度
- Dr. Thompson監控和協調整個過程

### 3. 結果收集與整合
- 收集所有reviewer的專業意見
- 整合7維度品質評估結果
- 解決reviewer之間的意見衝突

### 4. 最終品質判斷
- Dr. Thompson基於整合結果做出最終判斷
- 確定任務是否通過品質審查
- 設定後續行動和改進要求

### 5. 報告生成與維護
- 生成最終審查報告
- 確保報告品質和完整性
- 維護報告的專業標準

### 6. 任務狀態更新
- 根據最終審查結果更新任務狀態
- 同步更新相關文檔和元數據
- 完成審查流程的閉環

## 任務類型對應表

| 任務類型 | 推薦Reviewer組合 |
|---------|----------------|
| API開發 | code-quality, security, testing, integration |
| 前端UI | code-quality, testing, documentation, performance |
| 數據庫遷移 | code-quality, security, integration, testing |
| 性能優化 | performance, code-quality, testing |
| 安全增強 | security, code-quality, testing |
| 文檔更新 | documentation, code-quality |
| 基礎設施變更 | code-quality, security, integration |
| 重構 | code-quality, testing, performance |

## 手動指定支援

支援手動指定reviewer組合：
```bash
*review TASK-001 --reviewers security,performance,documentation
```

## 品質評估框架

### 7維度品質框架
所有reviewer使用統一的7維度品質框架：

1. **代碼品質**：可讀性、可維護性、最佳實踐遵循
2. **功能品質**：需求完整性、邊界條件處理、錯誤處理
3. **安全品質**：安全漏洞、認證授權、數據保護
4. **性能品質**：響應時間、吞吐量、資源使用
5. **測試品質**：覆蓋率、測試設計、自動化程度
6. **文檔品質**：完整性、準確性、可讀性
7. **維護品質**：可擴展性、可觀測性、運維就緒

### 評級標準
- **Bronze**：基礎交付，滿足最低品質要求
- **Silver**：成熟交付，達到行業標準
- **Gold**：優秀交付，超越行業標準
- **Platinum**：卓越標竿，成為最佳實踐案例

## 文件結構

```
core/qa/
├── README.md                           # 本文件
├── enforcement/
│   ├── task-reviewer-enforcement.md   # 統一執行規範
│   └── reviewer-orchestrator-enforcement.md  # 統帥執行規範
├── workflow/
│   ├── unified-review-workflow.yaml   # 統一工作流程
│   └── reviewer-orchestrator-workflow.yaml  # 統帥工作流程
└── templates/
    └── review-tmpl.yaml               # 報告模板

agents/
├── task-reviewer:code-quality.md      # 代碼品質reviewer
├── task-reviewer:security.md          # 安全reviewer
├── task-reviewer:performance.md       # 性能reviewer
├── task-reviewer:testing.md           # 測試reviewer
├── task-reviewer:documentation.md     # 文檔reviewer
└── task-reviewer:integration.md       # 整合reviewer
```

## 使用方式

### 基本使用
```bash
*review TASK-001
```

### 指定Reviewer
```bash
*review TASK-001 --reviewers security,performance
```

### 查看幫助
```bash
*help
```

## 優勢與效益

### 專業深度
- 每個reviewer專注於特定領域，提供更專業的審查
- 深度專業知識，發現潛在問題

### 效率提升
- 並行審查減少總體審查時間
- 專業分工提高審查質量

### 靈活性
- 可根據任務類型靈活選擇reviewer組合
- 支援手動指定和自動選擇

### 一致性
- 統一的品質標準和評估框架
- 標準化的報告格式

### 可擴展性
- 易於添加新的專業reviewer
- 支援更多品質維度

## 品質承諾

**Dr. Thompson的使命**：確保每個通過審查的專案都能在生產環境安然運行，維護軟體工程的專業標準和職業尊嚴，保護用戶免受糟糕代碼的傷害。

**專業Reviewer的承諾**：每個reviewer都專注於自己的專業領域，提供深度、客觀、證據充分的評估，與Dr. Thompson協作，共同維護最高的品質標準。

## 技術特點

- **並行執行**：支援多個reviewer同時進行專業審查
- **統一標準**：所有reviewer遵循相同的品質框架和評估標準
- **證據驅動**：所有結論都必須有具體證據支持
- **專業分工**：每個reviewer專注於特定品質維度
- **權威統籌**：Dr. Thompson擁有最終決策權威

## 聯繫與支持

如有問題或建議，請聯繫Dr. Thompson品質審查團隊。我們致力於不斷改進和優化這個架構，為軟體工程品質提供最可靠的保障。
