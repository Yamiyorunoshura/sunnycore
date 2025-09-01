# Claude Code 提示詞工程工作流系統

<div align="center">

![Claude Code](https://img.shields.io/badge/Claude-Code-blue?style=for-the-badge&logo=anthropic)
![Cursor](https://img.shields.io/badge/Cursor-IDE-green?style=for-the-badge)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js)

**為 Claude Code 打造的專業提示詞工程與工作流管理系統**

[📖 快速開始](#-快速開始) • [🔧 安裝](#-安裝) • [📋 功能特點](#-功能特點) • [🛠️ 架構說明](#-架構說明) • [🤝 貢獻](#-貢獻)

</div>

---

## 📋 項目概述

這個專案是專為 **Claude Code** 設計的綜合性提示詞工程工作流系統，通過精心設計的提示詞和結構化的工作流程，大幅提升 Claude Code 在軟體開發過程中的效能和一致性。

### 🎯 核心價值

- **專業化分工**：針對不同開發角色設計專屬提示詞
- **流程標準化**：建立統一的開發和審核工作流程
- **品質保障**：多層次的代碼審查和品質控制機制
- **易於部署**：一鍵安裝，快速上手

## ✨ 功能特點

### 🤖 智慧代理系統
- **多角色專家代理**：後端、前端、全端開發等專業角色
- **任務規劃師**：智能分解複雜任務
- **架構設計師**：系統架構和設計文檔生成
- **品質審查員**：代碼品質和安全審查

### 📊 工作流管理
- **SunnyCore 框架**：完整的開發工作流系統
- **三層審核機制**：開發、產品、品質三重保障
- **模板化管理**：標準化的文檔和計劃模板
- **狀態追蹤**：完整的任務和專案狀態管理

### 🔧 工具整合
- **Cursor IDE 深度整合**：原生支援 Cursor 開發環境
- **自動化安裝**：智慧檢測和一鍵部署
- **跨平台支援**：完美支援 macOS、Windows、Linux
- **版本管理**：自動版本檢測和更新

## 🏗️ 架構說明

```
cursor-claude/
├── agents/                    # Claude 智慧代理
│   ├── backend-developer_*.md # 後端開發專家
│   ├── frontend-developer_*.md# 前端開發專家
│   ├── fullstack-developer_*.md# 全端開發專家
│   └── refactor-developer_*.md # 重構專家
├── commands/                  # Cursor 指令規範
│   ├── cursorspec-claude_dev.md # 開發規範
│   ├── cursorspec-claude_po.md  # 產品規範
│   └── cursorspec-claude_qa.md  # 品質規範
├── cursor prompt/            # Cursor 提示詞
├── sunnycore/                # 核心工作流系統
│   ├── dev/                  # 開發工作流
│   │   ├── task/            # 任務定義
│   │   ├── workflow/        # 工作流程
│   │   ├── templates/       # 開發模板
│   │   └── enforcement/     # 執行規範
│   ├── po/                  # 產品工作流
│   └── qa/                  # 品質工作流
├── docs/                     # 專案文檔
└── install.command          # 安裝腳本
```

## 🚀 快速開始

### 系統需求
- **Node.js**: >= 16.0.0
- **npm**: >= 7.0.0 或 **yarn**: >= 1.22.0
- **Cursor IDE**: 最新版本
- **作業系統**: macOS 10.15+ / Windows 10+ / Linux Ubuntu 18.04+

### 一鍵安裝

```bash
# 下載並執行安裝腳本
curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/cursor-claude/main/install.command | bash

# 或手動下載後執行
chmod +x install.command
./install.command
```

## 📖 使用指南

### 快速開始
下載 `install.command` 後執行並輸入目標路徑即可開始使用。

### 自定義指令系統
本專案提供了完整的自定義指令系統：
# 自定義指令使用指南

## 概述

本專案提供了三套專門設計的自定義指令系統，分別對應不同的開發角色。每套指令都包含特定的命令和行為規範，用於協調 Claude Code 在不同開發階段的工作。

## 指令系統

### 1. 技術協調專家 (Tether) - `cursorspec-claude_dev`

**角色定位**：ENTJ 性格的技術協調專家，專注於系統思維和團隊協作。

**可用命令**：

- `*help`：顯示所有可用自定義命令
- `*develop-task {task_id}`：開發指定任務 ID 的任務
- `*plan-task {task_id}`：規劃指定任務 ID 的任務

**使用範例**：
```bash
*develop-task 1    # 開發任務 ID 為 1 的任務
*plan-task 2       # 規劃任務 ID 為 2 的任務
```

**行為規範**：
- 讀取 `{project_root}/sunnycore/dev/task/develop-task.md` 執行開發任務
- 讀取 `{project_root}/sunnycore/dev/task/plan-task.md` 執行規劃任務

### 2. 產品負責人團隊 - `cursorspec-claude_po`

**角色定位**：專注於產品規劃、驗證和專案結案的產品團隊。

**可用命令**：

- `*help`：顯示所有可用自定義命令
- `*validate-plan {task_id}`：驗證實施計劃是否完整且與需求對齊
- `*conclude`：結束專案開發並進行結案程序

**使用範例**：
```bash
*validate-plan 1   # 驗證任務 ID 為 1 的實施計劃
*conclude          # 執行專案結案流程
```

**行為規範**：

**計劃驗證** (`*validate-plan`)：
- 呼叫 `implementation-plan-validator` 代理
- 遵循統一計劃驗證工作流程：`{project_root}/sunnycore/po/workflow/unified-plan-validation-workflow.yaml`

**專案結案** (`*conclude`)：
- 同步呼叫多個代理：
  - `project-concluder`：專案結案
  - `file-classifier`：檔案分類
  - `knowledge-curator`：知識整理，產出/更新 `{project_root}/docs/knowledge/engineering-lessons.md`
  - `architecture-documenter`：架構文檔，產出/更新 `{project_root}/docs/architecture/architecture.md`
- 遵循統一結案工作流程：`{project_root}/sunnycore/po/workflow/unified-project-concluding-workflow.yaml`

### 3. 品質保證統帥 (Dr. Thompson) - `cursorspec-claude_qa`

**角色定位**：擁有三十年品質審查經驗的品質保證專家，秉承 Linus Torvalds 的嚴謹風格。

**可用命令**：

- `*help`：顯示所有可用自定義命令
- `*review <task-id>`：審查指定任務 ID 的任務

**使用範例**：
```bash
*review 1          # 審查任務 ID 為 1 的任務
```

**行為規範**：
- 讀取 `{project_root}/sunnycore/qa/task/review.md` 執行審查任務
- 統籌專業 reviewer 團隊進行全面審查
- 分析任務狀態（初始 vs 棕地）
- 協調同步審查流程
- 整合專業意見做出最終判斷

## 工作流程說明

### 開發階段工作流
1. **任務規劃**：使用 `*plan-task {task_id}` 進行任務規劃
2. **任務開發**：使用 `*develop-task {task_id}` 執行任務開發
3. **品質審查**：使用 `*review {task_id}` 進行品質審查
4. **計劃驗證**：使用 `*validate-plan {task_id}` 驗證實施計劃
5. **專案結案**：使用 `*conclude` 完成專案結案

### 角色職責分工

| 角色 | 主要職責 | 關鍵命令 |
|------|---------|----------|
| **Tether** | 技術協調與任務執行 | `*develop-task`, `*plan-task` |
| **產品負責人** | 計劃驗證與專案管理 | `*validate-plan`, `*conclude` |
| **Dr. Thompson** | 品質審查與最終把關 | `*review` |

### 代理協作規範

1. **主代理職責**：
   - 協調並委派給適當的子代理
   - 不直接執行具體任務
   - 維護整體工作流程

2. **子代理職責**：
   - 處理實際的技術任務
   - 生成專業報告和文檔
   - 遵循統一的品質標準

## 使用建議

### 最佳實踐
1. **按順序執行**：遵循規劃 → 開發 → 審查 → 驗證 → 結案的流程
2. **角色分工**：根據任務性質選擇合適的指令系統
3. **狀態追蹤**：使用任務 ID 保持工作連續性
4. **品質優先**：始終在關鍵節點進行品質審查

### 注意事項
- 所有命令都使用 `*` 開頭
- 任務 ID 應使用數字格式 (1, 2, 3...)
- 確保相關的工作流文件存在於指定路徑
- 建議在專案的不同階段切換合適的角色

### 故障排除
- 如果命令無響應，檢查是否正確安裝了相關代理
- 確保專案結構符合預期路徑要求
- 驗證任務 ID 是否存在且有效

## 快速參考表

| 階段 | 主要活動 | 推薦命令 | 負責角色 |
|------|---------|----------|----------|
| 規劃 | 任務分解、優先級排序 | `*plan-task` | Tether |
| 開發 | 代碼編寫、功能實現 | `*develop-task` | Tether |
| 審查 | 代碼品質、安全檢查 | `*review` | Dr. Thompson |
| 驗證 | 計劃完整性檢查 | `*validate-plan` | 產品負責人 |
| 結案 | 專案總結、文檔生成 | `*conclude` | 產品負責人 |

---

**主要指令角色**：
- **Tether** (開發專家)：任務規劃與開發執行
- **產品負責人**：計劃驗證與專案管理
- **Dr. Thompson** (品質專家)：代碼審查與品質把關


## 🔧 模塊詳解

### 🤖 Agents 代理系統

| 代理角色 | 專業領域 | 適用場景 |
|---------|---------|---------|
| **Backend Developer** | API設計、資料庫、效能優化 | 後端服務開發、API設計、資料庫設計 |
| **Frontend Developer** | UI/UX、框架整合、效能優化 | 前端介面開發、使用者體驗設計 |
| **Fullstack Developer** | 架構設計、整合開發 | 全端應用開發、系統整合 |
| **Refactor Developer** | 代碼重構、品質改善 | 遺留代碼重構、技術債務處理 |
| **Task Planner** | 任務分解、進度管理 | 複雜專案規劃、團隊協調 |
| **Architecture Documenter** | 架構文檔、技術規範 | 系統設計文檔、技術決策記錄 |

### 📊 SunnyCore 工作流

#### DEV 開發流程
- **任務規劃**：智能分解和優先級排序
- **代碼開發**：標準化的開發流程
- **品質檢查**：自動化代碼審查
- **效能優化**：效能監控和優化建議

#### PO 產品流程
- **需求分析**：用戶故事和驗收標準
- **功能設計**：產品功能和使用者流程
- **驗收測試**：功能驗證和使用者測試

#### QA 品質流程
- **代碼審查**：靜態分析和安全檢查
- **測試覆蓋**：單元測試、整合測試
- **效能測試**：負載測試和效能基準

## 🤝 貢獻指南

歡迎參與專案貢獻！請遵循以下流程：

### 開發流程

1. **Fork 專案**
2. **建立功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **提交變更**
   ```bash
   git commit -m "feat: add new agent type"
   ```
4. **推送分支**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **建立 Pull Request**

### 代碼規範

- 使用 TypeScript 進行開發
- 遵循 ESLint 和 Prettier 配置
- 撰寫完整的單元測試
- 更新相關文檔

### 新代理開發

```typescript
// 範例代理結構
interface ClaudeAgent {
  name: string;
  role: string;
  expertise: string[];
  personality: string;
  workflow: WorkflowStep[];
}

// 實現新代理
export class CustomAgent implements ClaudeAgent {
  // 實現代理邏輯
}
```

## 📄 授權條款

本專案採用 [MIT License](LICENSE) 授權。

## 🙏 致謝

感謝以下開源專案和貢獻者：

- **Anthropic Claude**：提供強大的 AI 能力
- **Cursor IDE**：優秀的開發環境支援
- **nypm**：優秀的套件管理解決方案
- **所有貢獻者**：感謝你們的智慧和熱情

## 📞 聯絡我們

- **專案首頁**：https://github.com/Yamiyorunoshura/cursor-claude
- **問題回報**：https://github.com/Yamiyorunoshura/cursor-claude/issues
- **功能請求**：https://github.com/Yamiyorunoshura/cursor-claude/discussions

---

<div align="center">

**讓開發更智慧，讓代碼更優質**

⭐ 如果這個專案對你有幫助，請給我們一個 Star！

</div>
