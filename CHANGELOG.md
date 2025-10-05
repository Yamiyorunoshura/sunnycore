# Changelog

本專案的所有重要變更都會記錄在此檔案中。

此檔案格式基於 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.0.0/)，
並且本專案遵循[語義化版本](https://semver.org/lang/zh-TW/)。

## [Unreleased]

## [1.8.4] - Claude code v1.8.4

### Added
- 強化文檔化任務功能：在 `document-project.md` 中新增知識庫整合與專案指引自動更新機制
  - 新增輸入源：`{root}/docs/knowledge/*.md` 知識庫文檔作為文檔化參考
  - 新增輸出項：`{root}/CLAUDE.md` 專案指引文檔的文檔索引自動更新
  - 新增約束條款：「必須在創建架構文檔後更新 {root}/CLAUDE.md 的 Document Index 章節」
  - 新增 DoD 檢查項目：「{root}/CLAUDE.md Document Index 章節已更新並包含新創建的架構文檔」
  - 優化 Steps：在 Sharding and Finalization Phase 新增「更新 CLAUDE.md 文檔索引」步驟
  - 提升文檔化流程完整性與專案指引同步性

## [1.8.3] - Claude code v1.8.3

### Changed
- 標準化任務文檔章節標題格式：將所有任務文檔中的空格分隔章節標題改為連字符格式，提升文檔格式一致性
  - 格式變更：`[Tool Guidelines]` → `[Tool-Guidelines]`、`[Error Handling]` → `[Error-Handling]`
  - 涵蓋任務：brownfield-tasks、conclude、create-architecture、create-brownfield-architecture、create-epic、create-requirements、curate-knowledge、develop-tasks、document-project、init、plan-tasks、review
- 國際化核心指引文檔：將 `CLAUDE.md` 從繁體中文完整翻譯為英文，提升國際用戶可用性
  - 翻譯範圍涵蓋：通用指引、工具指引、約束指引、任務指引、模板使用指引
  - 保持文檔結構與邏輯不變，僅進行語言轉換
- 版本號更新：claude-code.lock 從 1.8.2 升級至 1.8.3

## [1.8.2] - Claude code v1.8.2

### Changed
- 國際化任務文檔：將所有任務文檔從繁體中文完整翻譯為英文，提升國際用戶可用性
  - 翻譯範圍涵蓋 14 個任務文檔的所有章節：[Input]、[Output]、[Constraints]、[Tools]、[Tool Guidelines]、[Steps]、[DoD]
  - 涵蓋任務：brownfield-tasks、conclude、create-architecture、create-brownfield-architecture、create-epic、create-requirements、curate-knowledge、develop-tasks、document-project、help、init、plan-tasks、review
  - 保持原有文檔結構與邏輯不變，僅進行語言轉換
  - 版本號更新：claude-code.lock 從 1.8.1 升級至 1.8.2

## [1.8.1] - Claude code v1.8.1

### Changed
- 優化任務流程控制：在 `develop-tasks.md`、`brownfield-tasks.md`、`review.md` 中新增詳細的條件分支流程（if-then-else），提升流程清晰度與錯誤處理能力
  - develop-tasks.md：
    * 移除「3次嘗試後升級」的失敗處理約束
    * 新增 RED 階段條件分支（測試正確失敗 vs 測試部分通過路徑）
    * 新增 GREEN 階段條件分支（測試全部通過 vs 測試部分失敗路徑）
    * 新增 REFACTOR 階段條件分支（重構後測試通過 vs 失敗路徑）
  - brownfield-tasks.md：
    * 新增修復階段的測試通過/失敗分支流程
    * 詳細定義測試失敗後的回退與重試機制
  - review.md：
    * 優化約束描述，明確「嚴格遵循」的檢查重點與範圍
    * 增強工具指引的使用場景說明（claude-context 使用時機、todo_write 更新頻率）
    * 新增審查程式碼階段的測試通過/失敗分支流程（2.1 vs 2.2）
    * 新增產出結果階段的決策分支流程（Accept/Accept with changes/Reject 路徑）
- 統一文檔命名：修正 README.md 中的命令參考，將 `*create-brownfield-epic` 統一改為 `*create-epic`
- 版本號更新：claude-code.lock 從 1.8.0 升級至 1.8.1

## [1.8.0] - Claude code v1.8.0

### Added
- 新增專案初始化任務：新增 `init` 任務支援開發環境與專案文檔的自動初始化
  - 新增 `claude code/tasks/init.md`：提供專案初始化的完整工作流程
    * 環境初始化：自動設置開發環境（虛擬環境、工具鏈、數據庫、依賴套件）
    * 文檔生成：創建 `{root}/CLAUDE.md` 專案指導文檔（包含技術棧、開發規範、需求概述、項目目標、文檔索引）
    * 代碼庫索引：使用 claude-context (MCP) 工具建立代碼庫索引
    * 環境驗證：確保所有工具已安裝且配置正確
  - 更新 `claude code/commands/sunnycore_dev.md`：新增第 4 項自訂指令 `*init`
  - 更新 `claude code/index.json`：註冊 init 任務及其與 dev agent 的關聯
  - 版本號更新：claude-code.lock 從 1.7.39 升級至 1.8.0

### Changed
- 優化開發工作流程：在 README.md 中將 `init` 任務整合為階段二的第一步（步驟 4），確保開發環境在任務規劃前完成初始化
  - Greenfield 流程：步驟 4 為 `/sunnycore_dev *init`，後續步驟順延（plan-tasks 為步驟 5、develop-tasks 為步驟 6、review 為步驟 7）
  - Brownfield 流程：步驟 5 為 `/sunnycore_dev *init`，後續步驟順延（plan-tasks 為步驟 6、develop-tasks 為步驟 7、review 為步驟 8）
  - 階段三步驟編號相應調整
  - 更新流程圖以反映新的步驟順序

## [1.7.39] - Claude code v1.7.39

### Changed
- 重構 QA 審查系統：將通用 7 維度評分系統改為領域特定審查指引，提升審查精準度與適用性
  - 新增 8 個領域專屬審查標準：
    * Backend (7 維度)：API 設計、資料驗證、錯誤處理、資料庫互動、認證授權、並發處理、測試覆蓋
    * Frontend (7 維度)：UI/UX 一致性、狀態管理、渲染效能、打包優化、無障礙性、瀏覽器相容性、響應式設計
    * API (7 維度)：RESTful/GraphQL 標準、版本控制、錯誤碼標準化、文檔完整性、速率限制、安全性、向後相容
    * Database (6 維度)：Schema 設計、索引策略、遷移腳本、查詢效能、資料完整性、備份策略
    * DevOps (6 維度)：CI/CD 配置、容器化、監控告警、日誌策略、備份恢復、部署策略
    * Testing (6 維度)：測試策略、覆蓋率要求、Mock 策略、測試資料管理、測試可維護性、測試執行效率
    * Documentation (6 維度)：內容完整性、範例有效性、格式標準、版本同步、可讀性、準確性
    * General (4 維度)：功能需求合規、程式碼品質、測試完整性、文檔完整性（作為無法識別領域時的備案）
  - 保留統一的 4 級評分系統（Platinum/Gold/Silver/Bronze）與決策規則
  - 新增常見問題與反模式說明，提供具體審查指引
- 統一任務文檔工具標註格式：優化 11 個任務文檔的工具使用說明，提升文檔一致性
  - 統一工具標註格式：將使用場景描述簡化為簡短的步驟標註（例如：`[步驟1:追蹤任務;步驟2-4:追蹤任務狀態]`）
  - 新增 MCP 工具標註：明確標示 MCP 工具（例如：`sequentialthinking (MCP)`、`claude-context (MCP)`）
  - 涵蓋任務：brownfield-tasks、conclude、create-architecture、create-brownfield-architecture、create-epic、create-requirements、curate-knowledge、develop-tasks、document-project、plan-tasks、review
  - 提升工具使用指引的清晰度與可讀性

## [1.7.38] - Claude code v1.7.38

### Changed
- 標準化任務提示詞語言風格：重寫 12 個核心任務文件，統一指令性語言與動詞使用
  - 指令性語言標準化：「你需要」→「必須」、「你必須」→「必須」，完全去除「你」作為主詞
  - 動詞使用統一：
    * 創建類：統一使用「創建」（不用「建立」）、「產生」（不用「產出」）
    * 執行類：統一使用「執行」（不用「運行」）、「檢視」（不用「查看」）
    * 整合類：統一使用「整合」（不用「組裝」）
  - 句式標準化：
    * 條件分支：「若X則Y」→「若X，則Y」（統一標點使用）
    * 步驟動作：增加目的性說明（「閱讀X並理解Y」、「閱讀X以Y」）
  - 涵蓋任務：brownfield-tasks、conclude、create-architecture、create-brownfield-architecture、create-epic、create-requirements、curate-knowledge、develop-tasks、document-project、plan-tasks、review
  - 提升文檔專業性、一致性與可讀性

## [1.7.37] - Claude code v1.7.37

### Added
- 強化審查流程：在 `review.md` 中新增整合測試驗證機制，確保新實作不影響現有程式碼
  - 審查程式碼階段新增：「執行整合測試確認實作不影響原有程式碼」檢查點
  - DoD 新增檢查項目：「已執行整合測試確認實作不影響原有程式碼並紀錄結果」
  - 提升程式碼審查品質與系統穩定性保證

## [1.7.36] - Claude code v1.7.36

### Changed
- 重構任務命令命名：將 `create-tasks` 重命名為 `create-epic`，更符合敏捷開發中的 Epic 概念
  - README.md：更新所有命令參考（Greenfield 與 Brownfield 流程）
  - commands/sunnycore_pm.md：更新第 5 項自訂指令從 `*create-tasks` 改為 `*create-epic`
  - index.json：更新任務 ID、路徑映射、模板關聯、代理關聯等配置
  - tasks/create-epic.md：將輸出檔案從 `{root}/docs/tasks.md` 改為 `{root}/docs/epic.md`
  - tasks/plan-tasks.md：將輸入檔案從 `{root}/docs/tasks.md` 改為 `{root}/docs/epic.md`
- 版本號更新：claude-code.lock 從 1.7.35 升級至 1.7.36

## [1.7.35] - Claude code v1.7.35

### Changed
- 國際化指令文件：將所有角色指令檔案（sunnycore_dev.md, sunnycore_pm.md, sunnycore_po.md, sunnycore_qa.md）從繁體中文完整翻譯為英文，提升國際用戶可用性
  - 翻譯範圍涵蓋所有章節：輸入、輸出、角色、技能、約束、自訂指令、專業指引
  - sunnycore_dev.md：開發指引（TDD 實踐準則、程式碼品質標準、測試策略、文檔規範、風險管理）全面英文化
  - sunnycore_pm.md：需求分析指引、架構設計指引、任務管理指引全面英文化
  - sunnycore_po.md：專案總結指引、知識管理指引、架構管理指引全面英文化
  - sunnycore_qa.md：評分指引（7 維度評分標準、品質矩陣、決策規則）全面英文化

## [1.7.34] - Claude code v1.7.34

### Added
- 新增通用指引：在 `CLAUDE.md` 中新增「工具指引」與「約束指引」章節，明確定義工具使用方法與約束優先級規則
  - 工具指引：強制要求按照 [工具] 中定義的方法執行任務
  - 約束指引：建立三級優先級機制（commands[約束] > tasks[約束] > 預設約束），解決多層級約束衝突問題

### Changed
- 優化 `CLAUDE.md` 文檔結構：調整章節順序，將通用指引提至文檔開頭，提升規則可見度與理解順序

## [1.7.33] - Claude code v1.7.33

### Changed
- 簡化檔案讀取約束規則：優化四個角色指令檔案（dev、pm、po、qa）中的約束條款，將「除相關程式碼或指令文檔額外要求讀取之文檔外，僅讀取[輸入]中明確定義的檔案」精簡為「必須閱讀所有[輸入]中明確定義的檔案」，提升規則清晰度與可理解性
  - `sunnycore_dev.md`：約束第4條文字簡化
  - `sunnycore_pm.md`：約束第4條文字簡化
  - `sunnycore_po.md`：約束第4條文字簡化
  - `sunnycore_qa.md`：約束第4條文字簡化

## [1.7.32] - Claude code v1.7.32

### Changed
- 統一指令文檔輸入描述：將四個角色指令檔案（dev、pm、po、qa）中的「輸入」第一項描述統一為「用戶指令輸入與對應之任務文檔」，提升文檔一致性與可讀性
  - `sunnycore_dev.md`：「用戶指令輸入與任務檔案規範」→「用戶指令輸入與對應之任務文檔」
  - `sunnycore_pm.md`：「用戶指令與對應任務檔案」→「用戶指令輸入與對應之任務文檔」
  - `sunnycore_po.md`：「符合自訂指令模式的用戶指令」→「用戶指令輸入與對應之任務文檔」
  - `sunnycore_qa.md`：「用戶指令與對應任務檔案」→「用戶指令輸入與對應之任務文檔」

## [1.7.31] - Claude code v1.7.31

### Changed
- 精簡指令文檔：移除四個角色指令檔案（dev、pm、qa）中的範例說明，減少冗餘內容並提升文檔簡潔度
  - `sunnycore_dev.md`：移除 `*develop-tasks` 和 `*brownfield-tasks` 的範例說明
  - `sunnycore_pm.md`：移除 `*plan-tasks` 的範例說明
  - `sunnycore_qa.md`：移除 `*review` 的範例說明

### Added
- 新增靜態語言編譯要求：在 `sunnycore_dev.md` 的開發指引中新增「編譯成功要求」約束條款，強制靜態語言專案確保所有程式碼編譯通過

## [1.7.30] - Claude code v1.7.30

### Changed
- 優化自訂指令格式：統一將所有角色指令檔案（dev、pm、po、qa）中的自訂指令格式從雙星號（`**指令**`）改為單星號（`*指令`），提升視覺簡潔度
- 新增指令使用範例：為需要參數的指令（`*develop-tasks`、`*brownfield-tasks`、`*plan-tasks`、`*review`）增加「範例」說明，改善使用者體驗

## [1.7.29] - Claude code v1.7.29

### Changed
- 強化檔案讀取約束規則：在所有角色指令檔案（dev、pm、po、qa）中新增「除相關程式碼外或提示詞額外要求外，僅讀取[輸入]中明確定義的檔案」約束條款，優化 token 使用效率並減少非必要檔案讀取

## [1.7.28] - Claude code v1.7.28

### Changed
- 強化指令約束規則：在所有角色指令檔案（dev、pm、po、qa）中統一新增「必須根據[自訂指令]中的步驟進行操作」約束條款，進一步澄清指令執行流程的規範性要求

## [1.7.27] - Claude code v1.7.27

### Changed
- 強化所有任務的 DoD（Definition of Done）驗證機制：
  - 在 11 個核心任務文件中統一新增「DoD 驗證階段」
  - 新增「逐項檢查所有 DoD 項目是否已滿足」與「確認所有待辦項目已完成」檢查點
  - 涵蓋任務：brownfield-tasks、create-architecture、create-brownfield-architecture、create-requirements、create-tasks、curate-knowledge、develop-tasks、document-project、help、plan-tasks、review
  - 提升任務執行品質與完成度追蹤一致性

### Added
- brownfield-tasks.md：新增 5 個 DoD 檢查項目（單元測試、整合測試、修復總結、架構符合性、待辦項目完成）
- help.md：新增 DoD 檢查清單

## [1.7.26] - Claude code v1.7.26

### Added
- 新增文檔拆分腳本自動清理功能：`shard-architecture.py` 與 `shard-requirements.py` 完成拆分後自動刪除原始文檔

### Changed
- 優化 `develop-tasks.md` 任務說明：
  - 精簡約束條款，將「保留縮排風格」限定於開發筆記
  - 補充「計畫外檔案」定義，明確包含共用工具類、配置檔案等
  - 新增失敗重試機制：3次嘗試後升級至項目負責人處理
  - 強化工具使用指引：明確 `sequentialthinking` 與 `todo_write` 的具體使用場景
  - 優化 TDD 階段說明：為 RED、GREEN、REFACTOR 階段新增明確的轉換條件
  - 補充關鍵術語定義：升級處理（escalation）與回退機制（rollback）的具體操作方式

## [1.7.25] - Claude code v1.7.25

## Fixed
- 修正所有指令檔案中的文檔參考路徑：將 `SUNNYCORE.md` 更正為 `CLAUDE.md`
- 修正 `sunnycore_qa.md` 中的錯字：將「測試覆蓋率s架構合規性」更正為「測試覆蓋率與架構合規性」

## [1.7.24] - Claude code v1.7.24

## Changed
- 優化 `review.md` 審查流程：新增「如果審查通過的話更新 task.md 反映項目進展」步驟，強化審查後的項目追蹤機制

## [1.7.23] - Claude code v1.7.23

## Changed
- 重構文檔結構：將 `claude code/SUNNYCORE.md` 重命名為 `claude code/CLAUDE.md`，統一文檔命名規範與平台識別

## [1.7.22] - Claude code v1.7.22

## Changed
- 優化 Context7 工具使用說明：統一 `create-architecture.md` 與 `create-brownfield-architecture.md` 中的 context7 使用場景描述，強調避免重複造輪子的核心目的
- 優化任務文檔格式：改進 `create-requirements.md` 工具部分的格式與描述，提升可讀性

## [1.7.21] - Claude code v1.7.21

## Changed
- 更新 `plan-tasks.md` 範例路徑：將實作計畫範例從 `ABC-123-plan.md` 修正為 `1-plan.md`，統一檔案命名規範

## [1.7.20] - Claude code v1.7.20

## Changed
- 優化任務模板格式：將 `tasks-tmpl.yaml` 改為 checkbox 清單格式，提升任務追蹤的可讀性

## [1.7.19] - Claude code v1.7.19

## Added
- 新增 `claude code/SUNNYCORE.md` - 集中化的模板與工具使用指引文檔
  - 提供 YAML 轉 Markdown 的格式轉換指引
  - 強調 MCP 工具優先使用原則

## Changed
- 更新所有指令檔案 (`sunnycore_dev.md`, `sunnycore_pm.md`, `sunnycore_po.md`, `sunnycore_qa.md`) - 新增 SUNNYCORE.md 作為輸入參考文檔
- 優化 `claude code/tasks/create-requirements.md` - 將輸出路徑從 `{root}/docs/requirements/` 統一為 `{root}/docs/requirements.md`
- 大幅改進 `scripts/sunnycore.sh` 安裝腳本：
  - ✨ 新增互動模式支援 (`-i, --interactive` 參數)
  - 🚀 支援 curl 一行指令安裝（互動與非互動模式）
  - 🔍 自動偵測 curl 管道執行環境，智能啟用互動模式
  - 💬 改善用戶提示與預設值處理
  - 📝 更新使用說明文檔，新增 curl 安裝範例

## [1.7.18] - Claude code v1.7.18
## Changed
- 精簡所有模板文件：將 9 個 YAML 模板從複雜結構簡化為精簡版本，顯著減少 token 使用量
- 優化架構模板：`architecture-tmpl.yaml` 從 282 行簡化至 60 行，轉為需求導向設計
- 優化實作計劃模板：`implementation-plan-tmpl.yaml` 對齊 TDD 流程（Red-Green-Refactor）
- 優化需求模板：`requirement-tmpl.yaml` 移除冗餘欄位，保留核心需求資訊
- 優化審查模板：`review-tmpl.yaml` 簡化為 7 維度評分系統（功能合規、代碼品質、安全效能、測試覆蓋、架構對齊、文檔、部署就緒）
- 優化開發筆記模板：`dev-notes-tmpl.yaml` 精簡為核心實作資訊記錄
- 優化任務模板：`tasks-tmpl.yaml` 採用扁平化結構，移除複雜巢狀層級
- 優化完成報告模板：`completion-report-tmpl.yaml` 精簡為關鍵專案總結資訊
- 優化總結架構模板：`concluded-architecture-tmpl.yaml` 聚焦最終實作狀態記錄
- 優化知識庫模板：`project-knowledge-tmpl.yaml` 精簡為最佳實踐與錯誤案例記錄

## [1.7.17] - Claude code v1.7.17

## Changed
- 簡化指令文檔格式：將所有 command 檔案（dev、pm、po、qa）從複雜的 XML 結構簡化為清晰的中文 Markdown 格式
- 移除冗餘配置：刪除 `CLAUDE.md` 大型配置文件，將核心規則精簡整合至各指令檔案中
- 優化指引內容：保留核心指引（任務管理、專案總結、知識管理、架構管理、評分標準），移除過度複雜的結構化標籤

## Removed
- `claude code/CLAUDE.md` - 560 行的大型配置文件，內容已精簡整合至各指令檔案

## [1.7.16] - Claude code v1.7.16

## Changed
- 統一任務提示詞格式：將 `develop-tasks`、`help`、`review` 從 XML 格式改為 Markdown 格式
- 強化任務提示詞結構：在 `develop-tasks` 和 `review` 中新增工具指引、DoD 檢查清單等章節以提升執行品質
- 優化 README：重構 Greenfield/Brownfield 流程說明，採用結構化表格與 Mermaid 流程圖，增強可讀性與視覺化呈現

## [1.7.15] - Claude code v1.7.15

## Changed
- 統一核心任務提示詞格式：將 `create-architecture`、`create-brownfield-architecture`、`create-requirements`、`create-tasks`、`plan-tasks` 從 XML 格式改為 Markdown 格式
- 強化工作流程結構：新增工具指引、DoD 檢查清單、異常處理等章節以提升任務執行品質
- 新增 concluded-architecture-tmpl 模板並關聯至 document-project 任務

## [1.7.14] - Claude code v1.7.14

## Changed
- 統一任務提示詞格式：將`brownfield-tasks`、`conclude`、`curate-knowledge`、`document-project`從XML格式改為Markdown格式
- 更新審查報告：優化`brownfield-tasks`、`conclude`、`curate-knowledge`、`document-project`、`prompt-reviewer`的審查報告結構與評分機制

## [1.7.13] - Claude code v1.7.13

## Changed
- 修正README中安裝腳本名稱為`scripts/sunnycore.sh`
- 優化`brownfield-tasks`提示詞，使其更符合實際需求

## [1.7.11] - Claude code v1.7.11

## Added
- README：新增以 curl 一行指令執行 `scripts/sunnycore.sh` 的安裝教學

## Changed
- README：將安裝腳本名稱由 `sunnycore.command` 更正為 `scripts/sunnycore.sh`
