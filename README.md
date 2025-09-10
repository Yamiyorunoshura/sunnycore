# Sunnycore - 多平台 AI Agent 工作流程系統

一個創新的多平台 AI 助手系統，提供角色化的專業 AI agents 來優化開發工作流程，支援測試驅動開發 (TDD) 和質量保證流程。

## 平台支援

### Sunnycore for Claude Code
專業細分化平台，適合大型團隊和複雜專案
- **Backend Developer Agents**: API、Database、Security、Performance、Testing、Infrastructure
- **Frontend Developer Agents**: UI/UX、Framework、Performance、Accessibility、Testing  
- **Fullstack Developer Agents**: Architecture、Integration、Performance、DevOps
- **Refactor Developer Agents**: Code Quality、Performance
- **QA Reviewer Agents**: Security、Performance、Documentation、Integration、Code Quality、Testing

### Sunnycore for Warp Code
通用角色化平台，適合中小型團隊，強調工作流程和 TDD
- **Dev Agent (Biden)**: 全棧開發工程師，具備完整的技術棧能力
- **PM Agent (Jason)**: 產品經理，專注策略思維和跨功能協調
- **PO Agent**: 產品負責人，負責需求管理和產品規劃
- **QA Agent**: 品質保證工程師，確保代碼品質和測試覆蓋

### Sunnycore for Codex
基礎版本，提供核心的四個角色功能
- 簡化的 agent 系統
- 基本的工作流程支援
- 適合快速原型開發和小型專案

## 核心功能

### 🎭 角色化 AI 助手
每個 agent 都具有明確的:
- **專業領域**: 專注特定技術棧或職能
- **人格特質**: 獨特的工作風格和溝通方式
- **技能組合**: 針對性的專業能力和工具使用

### 🔄 工作流程自動化
- **TDD 開發流程**: 內建測試驅動開發最佳實踐
- **質量保證機制**: 多維度代碼審查和品質檢查
- **模板化管理**: 標準化的開發文檔和流程模板
- **里程碑追蹤**: 詳細的執行進度和檢查點管理

### 🛠️ 自定義指令系統
- **Agent 啟動**: `ac --dev`, `ac --pm`, `ac --po`, `ac --qa`
- **任務管理**: `*help`, `*develop-task {task_id}`, `*brownfield-task {task_id}`
- **工作流程**: 支援 greenfield 和 brownfield 開發場景

## 自定義 Agents 詳細說明

### Dev 全棧開發者 (Biden)
**核心能力**:
- 持續學習和技術追蹤
- 問題解決和系統性思維
- Frontend-Backend 整合開發
- 代碼品質和架構設計
- 測試驅動開發 (TDD)

**工作流程**:
1. 創建詳細的實作計劃和 todo-list
2. 遵循 TDD 開發流程
3. 確保代碼品質和測試覆蓋
4. 生成完整的開發文檔

### PM 產品經理 (Jason)
**核心能力**:
- 策略思維和客戶導向
- 跨功能溝通協調
- 優先級判斷和資源管理
- 利害關係人管理
- 技術理解和業務分析

**工作流程**:
1. 需求分析和架構規劃
2. 實作計劃制定
3. 里程碑管理和進度追蹤
4. 風險評估和問題解決

### PO 產品負責人
**核心能力**:
- 產品願景和策略規劃
- 用戶需求分析
- 功能優先級排序
- 市場趨勢洞察

### QA 品質保證工程師
**核心能力**:
- 多維度品質檢查
- 測試策略和執行
- 代碼審查和安全檢測
- 效能分析和優化建議
- 文檔品質和整合測試

## 快速開始

### 1. 啟動 Agent
```bash
# 啟動開發者 agent
ac --dev

# 啟動產品經理 agent  
ac --pm

# 啟動產品負責人 agent
ac --po

# 啟動品質保證 agent
ac --qa
```

### 2. 使用自定義指令
```bash
# 查看可用指令
*help

# 執行開發任務
*develop-task {task_id}

# 執行既有系統改進任務
*brownfield-task {task_id}
```

### 3. 工作流程範例
1. **需求分析**: 使用 PM agent 進行需求分析和架構規劃
2. **開發實作**: 使用 Dev agent 進行 TDD 開發
3. **品質保證**: 使用 QA agent 進行代碼審查和測試
4. **產品管理**: 使用 PO agent 進行產品規劃和優先級管理

## 技術特色

- **Sequential Thinking**: 深度分析和規劃能力
- **Template System**: 標準化的開發模板和文檔
- **Multi-platform Support**: 支援不同開發環境和需求
- **Quality Assurance**: 內建品質保證和最佳實踐
- **Workflow Automation**: 自動化的開發流程管理

## 貢獻指南

歡迎提交 Issue 和 Pull Request 來改進 Sunnycore 系統。請確保:
- 遵循現有的代碼風格和架構
- 添加適當的測試和文檔
- 更新相關的 CHANGELOG

## 授權

本專案採用 MIT 授權條款。