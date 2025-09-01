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
下載install.command後執行並輸入目標路徑即可

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

## ⚙️ 配置說明

### 環境變數

```bash
# 設定代理偏好
export CLAUDE_AGENT_PREFERENCE=backend-developer

# 設定工作流模式
export CLAUDE_WORKFLOW_MODE=strict

# 設定日誌等級
export CLAUDE_LOG_LEVEL=info
```

### 自訂配置

在 `~/.claude/config.json` 中可以自訂：

```json
{
  "agents": {
    "default_model": "claude-3-5-sonnet-20241022",
    "max_tokens": 4096,
    "temperature": 0.7
  },
  "workflow": {
    "auto_commit": true,
    "backup_enabled": true,
    "notification_enabled": true
  },
  "templates": {
    "custom_templates_path": "~/my-templates"
  }
}

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
