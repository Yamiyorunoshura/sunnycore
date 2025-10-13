# Sunnycore - 多平台 AI Agent 工作流程系統

一個創新的多平台 AI 助手系統，提供角色化的專業 AI agents 來優化開發工作流程，支援測試驅動開發 (TDD) 和質量保證流程。

> **v4.15.0 更新**：對話內規劃工作流程 (In-Conversation Planning)：所有角色命令新增 `[Planning-Workflow]` 章節，要求在對話中生成和維護書面計劃，不再創建 plan.md 文件；移除統一執行計劃模板，全面遷移至對話式規劃模式。詳見 [CHANGELOG.md](CHANGELOG.md#4150---2025-10-13)。

> **v4.13.0 更新**：治理規則增強：新增「先規劃後執行（sequential-thinking）」強制敘述與細化範例，強化執行紀律與可追溯性。詳見 [CHANGELOG.md](CHANGELOG.md#4130---2025-10-13).
> **v4.12.0 更新**：模板系統全面升級至 v2，新增開發工作流程與品質標準指引，強化任務原子化分解機制，大幅提升 AI 執行計劃品質與工作流程標準化。詳見 [CHANGELOG.md](CHANGELOG.md#4120---2025-10-13)。

> **v4.8.0 之後的變更**：已改為「對話內規劃」模式；不再產生或維護 `plan.md`，也不再引用 `templates/plan-tmpl.yaml`。所有規劃改以對話中之 Planning-Workflow 條目完成並維護。詳見 [CHANGELOG.md](CHANGELOG.md#480---2025-10-13)。

> **v4.7.0 更新**：Assistant 角色強制性計劃工作流程與知識管理增強，新增 [Planning-Workflow] 和 [Knowledge-Management] 章節，要求執行前必須生成書面計劃並引用 curated knowledge，與 v4.5.0/v4.6.0 的正反對比範例系統配合，全面提升執行規範性與架構完整性。詳見 [CHANGELOG.md](CHANGELOG.md#470---2025-10-13)。

> **v4.6.0 更新**：任務文件範例系統全面增強，所有 22 個任務文件統一採用正反對比範例格式（Good Example vs Bad Example），與 v4.5.0 的配置文件增強形成完整教學體系，全面提升 AI 任務執行的準確度與錯誤預防能力。詳見 [CHANGELOG.md](CHANGELOG.md#460---2025-10-12)。

> **v4.5.0 更新**：配置文件範例系統增強，新增正反對比範例（Good Example vs Bad Example），透過明確標示錯誤行為及其後果，大幅提升 AI 對規則的理解準確度與約束力。詳見 [CHANGELOG.md](CHANGELOG.md#450---2025-10-12)。

> **v4.4.0 更新**：強化 Dev 角色架構遵循約束，要求所有實作必須嚴格遵循當前架構設計，禁止偏離架構，確保架構一致性與完整性。詳見 [CHANGELOG.md](CHANGELOG.md#440---2025-10-12)。

> **v4.2.0 更新**：新增 PRD 流程專用驗收與修復任務（`*cutover-prd`、`*fix-prd-issues`），分離 PRD 與傳統流程，提升任務清晰度與可維護性。詳見 [CHANGELOG.md](CHANGELOG.md#420---2025-10-12)。

> **v4.1.0 更新**：統一角色命令 DoD 檢查清單，所有 5 個角色命令現在都包含標準化的 DoD 自檢章節，確保任務完成度驗證和交付品質一致性。詳見 [CHANGELOG.md](CHANGELOG.md#410---2025-10-12)。

> **v4.0.0 重大更新**：移除自動驗證子代理，改為人工自檢與 DoD 審核流程；新增多平台安裝器支援 claude、codex、cursor 三種發佈型態。詳見 [CHANGELOG.md](CHANGELOG.md#400---2025-10-13)。

## 🚀 快速開始

**不確定使用哪個開發流程？**

使用 `/sunnycore_pm *consult` 指令開始任何新需求！AI 會自動分析您的需求並建議最適合的開發流程：

- **完整開發流程** (`*create-requirements`) - 適用於需要架構變更或新增模塊的大型需求
- **PRD 流程** (`*create-prd`) - 適用於現有架構內的小型變更和快速迭代

只需描述您的需求，讓 AI 為您選擇最佳路徑！

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
- **進度追蹤增強** (v4.14.0 新增):
  - 所有角色命令強制要求在每個步驟後更新 `plan.md` 追蹤工作進度
  - 任務完成定義 (DoD) 統一要求標記 `plan.md` 所有項目為完成並刪除檔案
  - 強化執行紀律與進度可追溯性，確保工作流程完整性與一致性
- **驗證鏈鎖控管**: 
  - 每個步驟完成後必須自行執行步驟成果自檢，確認產出、測試與紀錄齊備
  - 任務結束前必須執行 DoD 完成檢查，確認所有交付物完整、風險受控
  - 所有角色在工作流程開始時必須記錄進度至 `docs/progress.md`
  - 進度與檢查結果需手動更新至 `docs/progress.md`（必要時同步 `docs/knowledge`）
- **里程碑追蹤**: 詳細的執行進度和檢查點管理，所有角色統一記錄至 `docs/progress.md`

### 🎯 工作範圍約束機制 (v3.10.0 新增)
- **明確職責邊界**: 每個角色和子代理都有明確定義的工作範圍
- **In Scope / Out of Scope**: 清楚區分每個角色可以執行和禁止執行的任務
- **防止越權操作**: AI 被明確限制只能執行定義範圍內的任務
- **強制性約束**: 使用 **MUST** / **MUST NOT** 格式確保規則嚴格遵循
- **提升執行品質**: 確保每個角色專注於其專業領域，避免職責混淆

## 自定義 Agents 詳細說明

### Dev 全棧開發者 (Biden)
**核心能力**:
- 持續學習和技術追蹤
- 問題解決和系統性思維
- Frontend-Backend 整合開發
- 代碼品質和架構設計
- 測試驅動開發 (TDD)

**代碼品質標準** (v3.13.0 新增):
- **嚴格禁止**在生產代碼中使用：
  - Mock 實作或 stub 代碼
  - 硬編碼值（API keys、credentials、敏感數據）
  - 佔位符代碼（`// TODO: implement`、`throw new Error('Not implemented')`）
- 測試代碼可使用 mocks/stubs/hardcoded test data（允許且預期）

**架構遵循約束** (v4.4.0 新增):
- **必須**遵循當前架構設計進行任何實作
- **禁止**創建偏離當前架構的實作計劃或代碼
- 確保實作與架構設計保持一致，防止架構漂移

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
- 業務驗收與項目交付
- 專案總結與知識管理
- 利害關係人管理

### QA 品質保證工程師
**核心能力**:
- 領域特定品質檢查（支援後端/前端/API/資料庫/DevOps/測試/文檔等 8 個領域）
- 多維度評分系統（Platinum/Gold/Silver/Bronze）
- 測試策略和執行
- 代碼審查和安全檢測
- 效能分析和優化建議
- 文檔品質和整合測試

**質量指標體系** (v4.16.0 新增):
- **測試覆蓋率**：行覆蓋率 80%+、分支覆蓋率 75%+、函數覆蓋率 85%+
- **測試通過率**：單元測試 100%、整合測試 98%+、E2E 測試 95%+
- **代碼質量**：環狀複雜度 < 10、重複率 < 3%、技術債 < 5%
- **缺陷管理**：缺陷密度 < 1/1000 行、關鍵 bug 零容忍、逃逸缺陷 < 2%
- **架構合規**：設計模式 100% 遵循、API 契約 100% 合規、零關鍵安全漏洞
- **性能標準**：響應時間符合 SLA、CPU < 70%、記憶體 < 80%、錯誤率 < 0.1%
- **審查質量**：100% 關鍵路徑審查、24-48 小時周轉、> 80% 可執行發現

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
4. 手動更新 `docs/progress.md`（必要時同步 `docs/knowledge`）紀錄進度與洞察

### 進度與知識紀錄指南
**核心原則**:
- 由角色本人判斷事件重要性並記錄，確保關鍵決策、交付與風險都有文字佐證
- `docs/progress.md` 聚焦重大進展（critical / important）；細節可附加於相關 dev-notes 或任務文件
- `docs/knowledge` 收錄通用性洞察、最佳實踐與復發風險案例

**記錄策略**:
- 標準格式：`{YYYY-MM-DD}:{HH:MM}: {ACTIONS_TAKEN} [{IMPORTANCE}]`
- 起始時標記 `[in_progress]`，完成時更新為 `[completed]` 或記錄具體成果級別
- 提供足夠上下文（任務、檔案、決策）便於日後追溯

### 步驟與完成檢查指南
**步驟自檢 (Step Outcome Self-Check)**:
- 對照任務檔案中的步驟描述，確認輸出、測試、文件均已更新
- 驗證相關測試是否執行且通過，保留測試紀錄或摘要
- 在 progress/dev-notes 內記錄判斷與後續待辦

**完成檢查 (DoD Self-Review)**:
- 逐條對照 DoD 清單，附上文件/測試/驗證證據
- 確認所有風險、阻塞項目已有後續 owner 或完成狀態
- 清理臨時檔案與草稿，確保交付物為最終版本
- 驗證通過後，將 progress 狀態調整為 completed 並總結結果

### 上下文恢復流程
自動子代理已移除，請依下列手動流程恢復上下文：
1. 檢查 `docs/progress.md` 以了解目前進行中的任務與最近進展
2. 依優先順序閱讀 `sunnycore/CLAUDE.md`、對應的 `commands/*` 與 `tasks/*`
3. 若專案有專屬模板/腳本，於 `sunnycore/templates`、`sunnycore/scripts` 中載入
4. 根據任務紀錄整理出所需的歷史輸出（docs/requirements、docs/architecture 等）
5. 建立新的行動清單或重建計畫，再繼續工作

### Sunnycore 自動安裝腳本

Sunnycore 提供了自動化安裝腳本 `scripts/install.py`，可快速安裝到本機。

#### 系統需求
- macOS、Linux 或 Windows 系統
- Python 3.6+
- 網路連線

#### 以 curl 一行安裝（推薦）

互動模式（不帶參數會在終端互動選擇安裝路徑）：
```bash
curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/install.py | python3
```

非互動模式（直接指定路徑並自動確認）：
```bash
curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/install.py | python3 - -v claude -p ~/myproject -y
```

可選參數：
- `-v, --version`：指定版本（支援 `claude`、`codex`、`cursor`，`claude-code` 仍可向後相容）
- `-p, --path`：安裝路徑（支援 `~/` 展開）
- `-y, --yes`：自動同意覆寫與操作
- `--repo`：GitHub 倉庫（預設：Yamiyorunoshura/sunnycore）
- `--branch`：分支名稱（預設：master）

#### 從本地倉庫執行

若已經克隆本倉庫，可直接執行腳本：

**安裝 Claude Code 版本：**
```bash
python3 install.py -v claude -p ~/myproject -y
```

**安裝 Codex 版本：**
```bash
python3 install.py -v codex -p ~/myproject -y
```

**安裝 Cursor 版本：**
```bash
python3 install.py -v cursor -p ~/myproject -y
```

#### 安裝結果

**Claude Code 版本**安裝完成後，目標路徑將包含：
```
工作目錄/
├── .claude/              # Claude 專用配置
│   ├── commands/        # 角色命令定義
│   └── hooks/           # 自動化掛鉤
└── sunnycore/           # Sunnycore 系統檔案
    ├── CLAUDE.md        # Claude Code 指引
    ├── tasks/           # 任務模板
    ├── templates/       # 文檔模板
    └── scripts/         # 輔助腳本
```

**Codex 版本**安裝完成後，目標路徑將包含：
```
~/.codex/
└── prompts/             # Sunnycore 指令（*.prompt.md）

工作目錄/
└── sunnycore/
    ├── AGENTS.md        # Codex 操作指引
    ├── tasks/
    ├── templates/
    └── scripts/
```

**Cursor 版本**安裝完成後，目標路徑將包含：
```
工作目錄/
├── .cursor/             # Cursor 專用命令檔
└── sunnycore/           # Sunnycore 系統檔案
    ├── cursor.mdc       # Cursor 指引
    ├── tasks/
    ├── templates/
    └── scripts/
```

## 快速開始

### Claude Code 版本

閱讀 `sunnycore/CLAUDE.md`

### Codex 版本

閱讀 `sunnycore/AGENTS.md`，並於 `~/.codex/prompts` 查看對應的 `*.prompt.md`

### Cursor 版本

閱讀 `sunnycore/cursor.mdc`

## 貢獻指南

歡迎提交 Issue 和 Pull Request 來改進 Sunnycore 系統。請確保:
- 遵循現有的代碼風格和架構
- 添加適當的測試和文檔
- 更新相關的 CHANGELOG

## 授權

本專案採用 Apache 2.0 授權條款。