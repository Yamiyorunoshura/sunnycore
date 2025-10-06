# Sunnycore - 多平台 AI Agent 工作流程系統

一個創新的多平台 AI 助手系統，提供角色化的專業 AI agents 來優化開發工作流程，支援測試驅動開發 (TDD) 和質量保證流程。

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
- 領域特定品質檢查（支援後端/前端/API/資料庫/DevOps/測試/文檔等 8 個領域）
- 多維度評分系統（Platinum/Gold/Silver/Bronze）
- 測試策略和執行
- 代碼審查和安全檢測
- 效能分析和優化建議
- 文檔品質和整合測試

**審查領域**:
- **Backend**: API 設計、資料驗證、錯誤處理、資料庫互動、認證授權、並發處理、測試覆蓋
- **Frontend**: UI/UX 一致性、狀態管理、渲染效能、打包優化、無障礙性、瀏覽器相容性、響應式設計
- **API**: RESTful/GraphQL 標準、版本控制、錯誤碼標準化、文檔完整性、速率限制、安全性、向後相容
- **Database**: Schema 設計、索引策略、遷移腳本、查詢效能、資料完整性、備份策略
- **DevOps**: CI/CD 配置、容器化、監控告警、日誌策略、備份恢復、部署策略
- **Testing**: 測試策略、覆蓋率要求、Mock 策略、測試資料管理、測試可維護性、測試執行效率
- **Documentation**: 內容完整性、範例有效性、格式標準、版本同步、可讀性、準確性
- **General**: 功能需求合規、程式碼品質、測試完整性、文檔完整性（備案）

### Assistant 技術助理
**核心能力**:
- 通用技術問題解答
- Bug 診斷與修復
- 程式碼優化建議
- 開發支援與諮詢

**工作流程**:
1. 接收用戶問題或 bug 報告
2. 分析並提供解決方案
3. 執行修復或優化
4. 自動調用 progress-manager 記錄進度

### Progress Manager 進度管理員
**核心能力**:
- 智能上下文分析
- 語意重要性分類（critical/important/normal/not-important）
- 進度記錄管理（僅記錄 critical 和 important 信息）
- 知識庫維護（bug 修復、最佳實踐、經驗教訓）

**記錄策略**:
- **progress.md**: 僅記錄 critical 和 important 級別的信息
- **knowledge/*.md**: 有條件地記錄 bug 修復和重要經驗

### Sunnycore 自動安裝腳本

Sunnycore 提供了自動化安裝腳本 `scripts/sunnycore.sh`，可快速安裝不同版本到本機。

#### 系統需求
- macOS 或 Linux 系統
- Git（必須已安裝）
- Bash shell
- 網路連線

#### 以 curl 一行安裝（推薦）

互動模式（不帶參數會在終端互動選擇版本與安裝路徑）：
```bash
curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/sunnycore.sh | bash
```

非互動模式（直接指定版本與路徑，並自動確認）：
```bash
curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/sunnycore.sh | bash -s -- -v warp-code -p ~/sunnycore -y
```

可用版本代號：`warp-code`、`codex`、`claude-code`

可選參數：
- `-v, --version`：指定版本（如 `warp-code`）
- `-p, --path`：安裝基礎路徑（會在該路徑下建立 `sunnycore/`）
- `-y, --yes`：自動同意覆寫與操作
- `--repo`、`--branch`、`--remote-name`：進階 Git 來源/分支控制

#### 從本地倉庫執行

若已經克隆本倉庫，可直接執行腳本：
```bash
bash scripts/sunnycore.sh -v warp-code -p ~/sunnycore -y
```

#### 安裝結果
安裝完成後，目標路徑將包含：
```
目標路徑/
├── sunnycore/           # 主要系統檔案
│   ├── config.yaml     # 配置檔案
│   ├── agents/         # Agent 定義
│   ├── tasks/          # 任務模板
│   └── templates/      # 文檔模板
└── [VERSION].md        # 版本特定文檔
```

## 快速開始

### Claude code version

閱讀[`claude code/README.md`](claude code/README.md)

## 貢獻指南

歡迎提交 Issue 和 Pull Request 來改進 Sunnycore 系統。請確保:
- 遵循現有的代碼風格和架構
- 添加適當的測試和文檔
- 更新相關的 CHANGELOG

## 授權

本專案採用 Apache 2.0 授權條款。