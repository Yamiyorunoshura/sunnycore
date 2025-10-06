# Changelog

本專案的所有重要變更都會記錄在此檔案中。

此檔案格式基於 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.0.0/)，
並且本專案遵循[語義化版本](https://semver.org/lang/zh-TW/)。

## [Unreleased]

## [1.13.3] - sunnycore v1.13.3

### Changed
- 重構任務粒度管理：將任務拆分策略從「原子任務」改為「功能級任務 + TDD 原子拆分」兩階段模式
  - 更新 `claude code/tasks/create-epic.md`：任務粒度從原子任務改為功能級任務
    * 約束調整：「必須創建原子、可驗證的任務（≤14 字元）」→「必須創建功能級任務，代表模組內的主要功能」
    * 新增說明：原子拆分將於 plan-tasks 階段使用 TDD RED/GREEN/REFACTOR 週期處理
    * DoD 更新：「每個任務是原子的」→「每個任務是功能級的」
  - 更新 `claude code/tasks/create-prd.md`：任務生成策略改為功能級
    * 任務生成階段：「生成原子、可驗證的任務（≤50 字元）」→「生成功能級任務，每個任務代表模組內的主要功能」
    * 新增說明：原子拆分將於 plan-tasks 階段使用 TDD RED/GREEN/REFACTOR 週期處理
    * DoD 更新：「原子任務已生成」→「功能級任務已生成」
  - 更新 `claude code/tasks/plan-tasks.md`：新增功能級任務拆分為原子步驟的詳細說明
    * 輸入描述：「任務清單」→「功能級任務清單」
    * 輸出格式：新增「將功能級任務拆分為原子實作步驟」說明
    * 新增約束：「必須將功能級任務拆分為原子、可執行的步驟」、「每個原子步驟應該最小化且可直接追溯到特定驗收標準」
    * 步驟優化：在 Setup、RED、GREEN 階段新增功能級任務拆分說明
  - 提升任務管理的靈活性與 TDD 流程的清晰度
- 擴展架構模板功能：新增 API 文檔區塊
  - 更新 `claude code/templates/architecture-tmpl.yaml`：新增 `api-documentation` 區塊
    * 新增欄位：internal-apis（內部 API 文檔：端點、方法、參數、回應、認證）
    * 新增欄位：external-apis（外部 API 文檔：服務、函式庫、版本、文檔 URL、使用情境）
    * 新增欄位：api-standards（API 標準：版本控制、認證、錯誤處理、速率限制）
  - 提升架構文檔的 API 描述完整性
- 優化任務與 PRD 模板：新增功能級任務說明與註釋
  - 更新 `claude code/templates/prd-tmpl.yaml`：新增任務粒度說明
    * 新增註釋：「任務應為功能級（例如：'實作登入功能'）」
    * 新增註釋：「原子拆分將於 plan-tasks 階段使用 TDD RED/GREEN/REFACTOR 週期處理」
  - 更新 `claude code/templates/tasks-tmpl.yaml`：新增功能級任務說明與註釋
    * 新增註釋：「任務應為功能級（例如：'實作使用者認證'）」
    * 新增註釋：「原子拆分將於 plan-tasks 階段使用 TDD RED/GREEN/REFACTOR 週期處理」
  - 提升模板的使用指引清晰度
- 強化文檔化任務：新增缺失架構文檔的自動生成功能
  - 更新 `claude code/tasks/document-project.md`：新增架構文檔缺失處理邏輯
    * 新增條件分支：若架構文檔缺失或不存在，則基於現有程式碼生成新架構文檔
    * 新增條件分支：若文檔結構與通用架構模板不符，則重構文檔結構並重新命名檔案
    * 新增生成流程：搜尋程式碼庫理解實作架構、根據通用架構模板生成文檔、執行 shard-architecture.py 拆分大型文檔
  - 提升文檔化任務的完整性與自動化能力

### Fixed
- 修正任務模板錯字：更正 `claude code/templates/tasks-tmpl.yaml` 中的 ID 錯字
  - 非功能任務第一項：`id: "Task-N1"r` → `id: "Task-N1"`
  - 提升模板格式正確性

## [1.13.2] - sunnycore v1.13.2

### Changed
- 重構任務文檔工具使用說明：統一12個任務文件中的 claude-context (MCP) 工具使用格式
  - 工具使用說明統一化：將 "Process large ..." 格式改為 "Search codebase for ..." 格式
  - 涵蓋任務：brownfield-tasks、create-brownfield-architecture、create-prd、create-requirements、curate-knowledge、develop-prd、develop-tasks、document-project、init、plan-tasks、review
  - 提升工具使用說明的語義清晰度與一致性
- 重構架構模板系統：將兩個架構模板合併為通用模板
  - 新增 `claude code/templates/architecture-tmpl.yaml`：全新的通用架構模板設計
    * 統一支援：初始架構設計、實作中的架構更新、最終架構總結
    * 新增欄位：last-updated（最後更新時間）、status（Draft|In Progress|Active）
    * 新增區塊：deployment（部署架構）、quality-attributes（架構品質）、source-references（來源參考）
    * 擴展技術堆疊：新增 development-tools 欄位
    * 擴展橫切關注點：新增 observability（可觀測性）區塊
    * 優化需求追溯：新增 implementation 和 status 欄位
  - 刪除 `claude code/templates/concluded-architecture-tmpl.yaml`：舊的總結架構模板（已合併至通用模板）
- 優化專案文檔化任務：簡化 document-project.md 工作流程
  - 更新 `claude code/tasks/document-project.md`：移除 shard-architecture.py 執行步驟
    * 輸入源調整：使用通用架構模板、新增 dev-notes 和 review-results 作為輸入
    * 流程簡化：直接根據實作狀況更新 architecture/*.md 文件，不再執行拆分腳本
    * 步驟重構：Step 2（Write → Update）、Step 3（移除 Sharding 改為 Finalization）
    * 新增約束：基於實際實作狀態更新、保留現有架構結構
    * 新增 DoD：新增 codebase 搜尋、dev-notes 和 review-reports 檢視檢查項
  - 提升文檔化流程的實用性與可維護性

## [1.13.1] - sunnycore v1.13.1

### Changed
- 優化知識整理任務文檔：新增完整的知識管理架構範例與分類指引
  - 更新 `claude code/tasks/curate-knowledge.md`：新增 [Example] 章節
    * 文檔類型與命名規範：best-practices-{topic}.md、errors-{topic}.md、problem-solving-{topic}.md
    * 語義分類範例：詳細列舉各類文檔的主題範例（api-design、error-handling、authentication 等）
    * 文檔格式模板：提供三種文檔類型的完整格式範本
    * 具體範例：展示多條目文檔的實際結構
    * 分類指引：強調語義主題分類原則與文件拆分建議
- 優化進度管理文檔格式：統一知識庫記錄範例格式
  - 更新 `claude code/agents/progress-manager.md`：knowledge/*.md 格式範例改進
    * 中文化範例欄位佔位符（YYYY-MM-DD、描述、錯誤類型等）
    * 統一文檔格式架構：best-practices、errors、problem-solving 三類文檔
    * 新增語義分類範例與分類指引
    * 新增具體範例（errors-{topic}.md 格式）

### Fixed
- 修正 PRD 開發任務輸出路徑錯誤：更正 `claude code/tasks/develop-prd.md` 中的開發筆記輸出路徑
  - 輸出路徑：`{root}/docs/dev-notes/prd-dev-notes.md` → `{root}/docs/prd-dev-notes.md`
  - 提升路徑引用的一致性

## [1.13.0] - sunnycore v1.13.0

### Changed
- 重構專案總結流程：優化角色職責與工作流程順序
  - 更新 `claude code/index.json`：將 conclude 任務從 architect 轉移至 po
    * taskToAgents 映射：conclude 任務由 po 負責
    * agentToTasks 映射：architect 移除 conclude、po 新增 conclude
  - 更新 `claude code/README.md`：調整 Greenfield 和 Brownfield 流程階段三步驟順序
    * Greenfield 流程：步驟 9（document-project）、步驟 10（curate-knowledge）、步驟 11（conclude）
    * Brownfield 流程：步驟 10（document-project）、步驟 11（curate-knowledge）、步驟 12（conclude）
    * 原因：先完成技術文檔產出與知識整理，最後由 PO 執行業務總結
- 增強專案總結任務：大幅擴展 conclude 任務功能與自動化能力
  - 更新 `claude code/tasks/conclude.md`：全面重構輸入源、輸出項與執行流程
    * 輸入源擴展：從特定文件改為遞迴掃描整個 `{root}/docs/` 目錄，確保完整資訊收集
    * 新增版本管理：從 `sunnycore.lock` 自動解析版本號（格式：`version = x.x.x`）
    * 新增檔案歸檔功能：自動將 docs/ 中的文件移至 `archive/{version}/`，但保留 architecture/、knowledge/、completion-report.md
    * 新增文檔參考更新：自動更新 architecture/ 和 knowledge/ 中指向已歸檔文件的路徑
    * 優化執行步驟：新增版本解析階段、檔案歸檔階段、文檔參考更新階段
    * 更新 DoD：新增版本解析、遞迴掃描、檔案歸檔、路徑更新等檢查項目
- 擴展完成報告模板：支援版本追蹤與歸檔記錄
  - 更新 `claude code/templates/completion-report-tmpl.yaml`：新增 version 欄位與 archived_files 區塊
    * 新增欄位：version（從 sunnycore.lock 讀取）
    * 新增區塊：archived_files（記錄歸檔位置與項目清單）
    * 擴展參考來源：新增 cutover_reports、progress_records、other_docs 等參考類型
- 版本號升級：sunnycore.lock 從 1.12.8 升級至 1.13.0

## [1.12.8] - sunnycore v1.12.8

### Fixed
- 修正知識整理任務輸入路徑錯誤：更正 `claude code/tasks/curate-knowledge.md` 中的 cutover 報告路徑引用
  - 第 4 項輸入：`{root}/cutover.md` → `{root}/docs/cutover.md`
  - 提升路徑引用的正確性與知識整理流程的可靠性

## [1.12.7] - sunnycore v1.12.7

### Fixed
- 修正總結任務輸入路徑錯誤：更正 `claude code/tasks/conclude.md` 中的兩個文檔路徑引用
  - 第 5 項輸入：`{root}/cutover.md` → `{root}/docs/cutover.md`
  - 第 6 項輸入：`{root}/docs/cutover-dev-notes.md` → `{root}/docs/cutover-fixes-dev-notes.md`
  - 提升路徑引用的正確性與專案總結流程的可靠性

## [1.12.6] - sunnycore v1.12.6

### Changed
- 增強安裝腳本管道執行支援：優化 `scripts/install.py` 的互動體驗（`scripts/install.py`）
  - 新增 `safe_input()` 函數：支援管道執行時從 `/dev/tty` 讀取用戶輸入
  - 改進錯誤處理：當無法讀取輸入時提供更清晰的提示信息
  - 更新說明文檔：新增管道執行的互動模式說明與完整支援聲明

## [1.12.5] - sunnycore v1.12.5

### Changed
- 重構角色職責分配：將專案總結與知識管理任務從 Architect 轉移至 PO
  - 更新 `claude code/commands/sunnycore_architect.md`：移除 *conclude 和 *curate-knowledge 命令
  - 更新 `claude code/commands/sunnycore_po.md`：新增 *conclude 和 *curate-knowledge 命令
  - 更新 `claude code/README.md`：調整 Greenfield 和 Brownfield 流程中的步驟 9 和 10，改為由 PO 執行總結與知識整理
  - 優化角色定位：PO 專注於業務驗收與專案交付，Architect 專注於技術架構設計
- 增強任務輸入源：優化總結與知識整理任務的資訊收集範圍
  - `claude code/tasks/conclude.md`：新增 cutover.md、cutover-dev-notes.md、progress.md 作為輸入源
  - `claude code/tasks/curate-knowledge.md`：新增 cutover.md、cutover-dev-notes.md、progress.md 作為輸入源
  - 提升專案總結與知識庫的完整性與準確性
- 優化文件歸檔流程：擴大歸檔範圍並增強自動化
  - `claude code/tasks/conclude.md`：新增 implementation-plan/ 目錄至歸檔清單
  - `claude code/tasks/curate-knowledge.md`：新增自動歸檔 review-results/ 和 dev-notes/ 至 archive/{version_name}/
  - 提升專案文件管理的系統性與可追溯性
- 修正模板路徑引用：統一任務文檔中的路徑格式
  - `claude code/tasks/conclude.md`：將模板路徑從 "{root}/claude code/templates/" 更正為 "{root}/sunnycore/templates/"
  - 提升路徑引用的一致性與正確性
- 優化文檔化任務：新增臨時文檔保存步驟
  - `claude code/tasks/document-project.md`：新增將臨時文檔保存為 "{root}/docs/architecture.md" 的步驟
  - 改善文檔產出流程的可檢視性

## [1.12.4] - sunnycore v1.12.4

### Added
- 安裝腳本並行下載功能：大幅提升安裝速度與用戶體驗（`scripts/install.py`）
  - 新增 ThreadPoolExecutor 並行下載機制：支援最多 10 個並行下載任務
  - 新增即時進度顯示：顯示 `[已完成/總數]` 格式的下載進度與狀態
  - 新增 `collect_directory_files` 方法：遞迴收集所有文件後再批量並行下載
  - 新增 `download_files_parallel` 方法：協調並行下載任務並統計成功/失敗數量
  - 新增 `--max-workers` 參數：允許用戶自訂最大並行下載數（預設 10）
  - 新增線程安全機制：使用 `threading.Lock` 保護共享變數（進度計數器）

### Changed
- 優化安裝腳本互動體驗：改進用戶互動流程與模式選擇（`scripts/install.py`）
  - 互動模式新增安裝模式選擇：1) 專案安裝（當前工作目錄）2) 自訂安裝（指定路徑）
  - 移除 TTY 檢測限制：允許在管道執行時也能進行互動輸入（改用 EOFError 捕獲）
  - 優化錯誤提示：當無法讀取用戶輸入時提供明確的參數使用建議
  - 改進安裝路徑提示：將預設路徑顯示調整至專案安裝模式說明中
  - 優化安裝完成訊息：調整目錄結構顯示，將 `CLAUDE.md` 移至 `sunnycore/` 下
  - 更新說明文檔：改進範例說明與模式說明章節
- 統一文檔路徑引用格式：所有任務與命令文檔中的路徑引用加上雙引號（提升可讀性）
  - 涵蓋文件：所有 `claude code/agents/`, `claude code/commands/`, `claude code/tasks/` 下的文檔
  - 格式變更：`{root}/docs/...` → `"{root}/docs/..."`
  - 提升文檔專業性與視覺一致性

## [1.12.3] - sunnycore v1.12.3

### Fixed
- 改進安裝腳本在非互動環境下的用戶體驗（`scripts/install.py`）
  - 新增 TTY 檢測：使用 `sys.stdin.isatty()` 判斷是否為互動式終端
  - 優化錯誤提示：當通過管道執行且目錄已存在時，明確提示使用 `-y` 參數或手動刪除目錄
  - 自動路徑處理：通過管道執行且未指定路徑時，自動使用預設路徑 `~/sunnycore` 並顯示提示訊息
  - 更新使用範例：在幫助文檔中新增「從管道執行（指定路徑）」的範例說明

## [1.12.2] - sunnycore v1.12.2

### Changed
- 重構安裝腳本：從 Bash 改為 Python，提升跨平台支援能力
  - 新增 `scripts/install.py`：使用 Python 3.6+ 實作安裝腳本
    * 跨平台支援：支援 macOS、Linux、Windows 系統
    * 標準庫實作：使用 urllib、argparse、pathlib 等標準庫
    * 智能下載：從 GitHub API 遞迴獲取目錄內容並下載文件
    * URL 編碼處理：正確處理包含空格的文件路徑（如 "claude code/"）
    * 互動模式：支援互動式路徑選擇與自動確認模式
    * 參數支援：-v (版本)、-p (路徑)、-y (自動確認)、--repo、--branch
  - 移除 `scripts/sunnycore.sh`：舊的 Bash 安裝腳本（1520 行）
  - 移除 `scripts/sync-common-files.sh`：分支同步腳本（274 行）
- 更新 README.md：反映新的 Python 安裝腳本
  - 系統需求更新：macOS/Linux → macOS/Linux/Windows，Bash → Python 3.6+
  - 安裝指令更新：`curl ... | bash` → `curl ... | python3`
  - 參數說明調整：移除 Bash 特定參數，新增 Python 腳本參數
  - 安裝路徑範例更新：從 `~/sunnycore` 改為 `~/myproject`
  - 目錄結構說明優化：更清晰地說明 `.claude/` 與 `sunnycore/` 的作用

## [1.12.1] - sunnycore v1.12.1

### Changed
- 品牌統一：將版本鎖定檔案從 `claude code/claude-code.lock` 重命名為 `sunnycore.lock`
  - 刪除 `claude code/claude-code.lock`（版本 1.12.0）
  - 新增 `sunnycore.lock`（版本 1.12.1）
  - 統一 CHANGELOG.md 中所有歷史版本標題格式：從 "Claude code vX.X.X" 改為 "sunnycore vX.X.X"
- 優化任務流程：在 5 個核心任務中新增用戶批准草稿的互動流程
  - `create-architecture.md`：新增步驟 3（Writing Phase）的用戶批准機制
    * 3.1: Write Final Documents - 用戶批准後寫入最終文檔
    * 3.2: Revise Based on Feedback - 根據用戶反饋修訂草稿
    * DoD 新增：「User approval has been obtained for architecture draft」
  - `create-brownfield-architecture.md`：新增步驟 3（Writing and Sharding Phase）的用戶批准機制
    * 3.1: Write Final Documents - 用戶批准後寫入最終文檔並執行拆分
    * 3.2: Revise Based on Feedback - 根據用戶反饋修訂草稿
    * 新增輸入源：`{root}/docs/knowledge/*.md` - 專案知識庫
    * DoD 新增：「User approval has been obtained for architecture draft」
  - `create-epic.md`：新增步驟 4（Finalization Phase）的用戶批准機制
    * 4.1: Write Final Document - 用戶批准後寫入任務清單
    * 4.2: Revise Based on Feedback - 根據用戶反饋修訂任務清單
    * DoD 新增：「User approval has been obtained for task list draft」
  - `create-requirements.md`：新增步驟 5（Finalization Phase）的用戶批准機制
    * 5.1: Write Final Documents - 用戶批准後寫入需求文檔並執行拆分
    * 5.2: Revise Based on Feedback - 根據用戶反饋修訂需求文檔
  - `curate-knowledge.md`：新增輸入源 `{root}/docs/knowledge/*.md` - 現有知識庫
- 大幅增強安裝腳本（`scripts/sunnycore.sh`）的錯誤處理與用戶體驗
  - 新增 `handle_command_error` 函式：提供詳細的錯誤診斷與重試機制
    * 自動識別退出碼並提供具體建議（git/檔案系統/網路相關錯誤）
    * 互動模式下支援命令重試
  - 新增 `check_system_environment` 函式：全面的系統環境檢測
    * 檢測作業系統、Shell 環境、目錄權限、網路連線、磁碟空間
    * 在互動模式下顯示環境摘要並允許用戶確認
  - 新增 `safe_read_with_timeout` 函式：安全的用戶輸入讀取
    * 支援超時機制（預設 30 秒）
    * 自動處理終端重定向問題
  - 改進 `require_cmd` 函式：提供缺失指令的安裝建議
    * 針對不同作業系統（macOS/Ubuntu/CentOS/Windows）提供具體安裝指令
    * 互動模式下允許用戶選擇是否繼續
  - 改進 `detect_execution_method` 函式：智能檢測執行方式
    * 自動識別 curl、direct、source 執行方式
    * 針對不同執行方式自動調整設置
  - 改進用戶互動流程：
    * `prompt_install_type`：新增詳細的選項說明（emoji、功能描述、適用場景）
    * `prompt_install_path`：新增路徑驗證與父目錄創建機制
    * `confirm_overwrite_if_needed`：改進覆寫確認提示與錯誤處理
  - 新增安裝摘要與最終確認：在安裝前顯示完整摘要並請求用戶確認
  - 新增安裝完成提示：顯示成功訊息與後續操作建議

### Fixed
- 修正 `claude code/tasks/conclude.md` 路徑錯誤：將輸入路徑從 `{root}/docs/review_results/{task_id}-review.md` 更正為 `{root}/docs/review-results/{task_id}-review.md`

## [1.12.0] - sunnycore v1.12.0

### Removed
- 移除 Warp Code 版本：完全刪除 `warp code/` 目錄及其所有內容
  - 刪除 agents (dev.md, pm.md, po.md, qa.md)
  - 刪除 scripts (shard-architecture.py, shard-requirements.py)
  - 刪除 tasks (14 個任務文檔)
  - 刪除 templates (8 個模板文件)
  - 刪除配置文件 (index.json, warp-code.lock)
- 移除 Codex 版本：完全刪除 `codex/` 目錄及其所有內容
  - 刪除 agents (dev.md, pm.md, po.md, qa.md)
  - 刪除 scripts (shard-architecture.sh, shard-requirements.sh)
  - 刪除 tasks (11 個任務文檔)
  - 刪除 templates (8 個模板文件)
  - 刪除配置文件 (index.json, AGENTS.md, DEPENDENCIES.md, README.md)

### Changed
- 專案架構簡化：統一使用 Claude Code 作為唯一支援版本
  - 保留 `claude code/` 作為主要開發版本
  - 簡化維護成本與版本管理複雜度
  - 優化專案結構清晰度

## [1.11.0] - sunnycore v1.11.0

### Added
- 新增技術支援工作流程：提供快速問題解答、Bug 修復、程式碼優化等日常技術支援
  - 新增 `claude code/commands/sunnycore_assistant.md`：定義 Technical Assistant 角色
    * 核心能力：問題診斷、Bug 分析與修復、技術諮詢、程式碼審查與優化、知識轉移
    * 自動調用 progress-manager 記錄重要進度和知識
  - 新增 `claude code/agents/progress-manager.md`：定義 Progress Manager 代理
    * 智能上下文分析與語意重要性分類（critical/important/normal/not-important）
    * 進度記錄管理：僅記錄 critical 和 important 級別信息至 `docs/progress.md`
    * 知識庫維護：有條件地記錄 bug 修復和重要經驗至 `docs/knowledge/*.md`
  - 更新 `claude code/README.md`：新增「技術支援流程」章節
    * 詳細說明 `/sunnycore_assistant` 使用方式與特點
    * 新增進度記錄格式與知識庫組織說明
  - 更新根目錄 `README.md`：新增 Assistant 和 Progress Manager 的角色說明與核心能力描述
- 更新配置檔案：`claude code/index.json` 反映新的代理註冊
  - 新增 assistant 和 progress-manager agents 定義
  - 更新代理清單順序（assistant 置於 architect 後、progress-manager 置於 po 後）

### Changed
- 版本號升級：claude-code.lock 從 1.10.1 升級至 1.11.0

## [1.10.1] - sunnycore v1.10.1

### Changed
- 重構工具使用指引文檔結構：將分散在各任務文檔中的 [Tool-Guidelines] 章節整合至 `CLAUDE.md` 集中管理
  - 新增 `claude code/CLAUDE.md` 的 [Tool-Guidelines] 章節：詳細說明 5 個核心工具使用場景
    * **todo_write**：任務追蹤與多階段工作流程管理
    * **sequentialthinking (MCP)**：結構化推理與複雜問題分析（含推理步驟建議）
    * **claude-context (MCP)**：代碼庫語義搜尋與索引建構
    * **context7 (MCP)**：外部套件參考與 API 文檔檢索
    * **playwright_browser (MCP)**：網頁瀏覽與產業標準研究
  - 移除 15 個任務文檔中的重複 [Tool-Guidelines] 章節：提升可維護性並減少 token 使用量
    * 涵蓋任務：brownfield-tasks、conclude、create-architecture、create-brownfield-architecture、create-epic、create-prd、create-requirements、curate-knowledge、cutover、develop-prd、develop-tasks、document-project、fix-acceptance-issues、init、plan-tasks、review
  - 優化 `claude code/CLAUDE.md` 的 [Summary-Instructions] 章節：將 [Tool-Guidelines] 標註為必須保留內容
- 版本號升級：claude-code.lock 從 1.10.0 升級至 1.10.1

## [1.10.0] - sunnycore v1.10.0

### Added
- 新增 PRD 工作流程：提供小型變更與快速迭代的輕量化開發流程
  - 新增 `claude code/tasks/create-prd.md`：定義 PRD（產品需求文檔）創建任務
    * 自動偵測專案類型（Greenfield/Brownfield）
    * 整合需求、架構、任務於單一文檔
    * 支援需求可追溯性（requirement-to-architecture-to-task）
  - 新增 `claude code/tasks/develop-prd.md`：定義 PRD 開發任務
    * 一次性完成所有 PRD 任務
    * 遵循 TDD 開發流程（RED-GREEN-REFACTOR）
    * 自動產生統一開發筆記 `prd-dev-notes.md`
  - 新增 `claude code/templates/prd-tmpl.yaml`：PRD 模板
    * 包含需求、架構、任務三大區塊
    * 支援功能與非功能需求定義
    * 提供技術棧與資料流程描述結構
- 新增 Architect 角色架構設計命令：在 `sunnycore_architect.md` 中新增架構設計職責
  - 新增第 5 項命令：`*create-architecture` - 創建 Greenfield 架構
  - 新增第 6 項命令：`*create-brownfield-architecture` - 創建 Brownfield 架構
  - 強化 Architect 技術決策支援能力

### Changed
- 重構角色職責分配：優化 PM、Architect、Dev 三個角色的職責邊界
  - PM (`sunnycore_pm.md`)：專注於產品需求管理與 PRD 創建
    * 移除 `*create-architecture` 與 `*create-brownfield-architecture` 命令
    * 新增 `*create-prd` 命令（第 5 項）
  - Architect (`sunnycore_architect.md`)：接管所有架構設計任務
    * 新增 `*create-architecture` 和 `*create-brownfield-architecture` 命令
  - Dev (`sunnycore_dev.md`)：新增 PRD 開發能力
    * 新增 `*develop-prd` 命令（第 6 項）
- 優化現有任務以支援 PRD 流程：更新驗收與修復任務以支援 PRD 作為輸入源
  - `cutover.md`：新增條件分支支援 PRD.md 作為主要需求來源
    * 優先從 PRD.md 讀取需求與架構（若存在）
    * 回退至傳統 requirements/*.md 與 architecture/*.md（若 PRD.md 不存在）
  - `fix-acceptance-issues.md`：新增條件分支支援 PRD.md 作為需求與架構來源
    * 輸出路徑調整為 `{root}/docs/cutover-fixes-dev-notes.md`
- 更新開發流程文檔：在 `claude code/README.md` 中新增 PRD 流程說明與比較表
  - 新增「PRD 流程」章節：完整的 5 步驟工作流程與 Mermaid 流程圖
  - 更新「流程說明」章節：新增 PRD vs Greenfield vs Brownfield 比較表
  - 更新「角色職責」章節：反映新的角色分工（Architect 負責架構設計、PM 負責 PRD 創建）
- 簡化根目錄 README：優化內容結構與可讀性
  - 移除重複的安裝方法與快速開始章節
  - 改為引用 `claude code/README.md` 作為 Claude code 版本的使用指引
  - 更新授權條款說明（從 MIT 改為 Apache 2.0）
- 更新配置檔案：`claude code/index.json` 反映新的任務與角色關聯
  - 新增 create-prd、develop-prd 任務註冊
  - 新增 prd-tmpl 模板註冊
  - 更新任務與代理的對應關係（architect 接管架構任務、pm 負責 PRD 創建）
  - 更新任務與模板的依賴關係
- 版本號升級：claude-code.lock 從 1.9.1 升級至 1.10.0

## [1.9.1] - sunnycore v1.9.1

### Added
- 新增開發者指令快捷方式：在 `claude code/commands/sunnycore_dev.md` 中新增 `*fix-acceptance-issues` 指令
  - 新增第 4 項自訂指令：`*fix-acceptance-issues` - 讀取 `{root}/sunnycore/tasks/fix-acceptance-issues.md`
  - 原第 4 項 `*init` 指令順延為第 5 項
  - 完善驗收失敗後的修復流程可訪問性

### Changed
- 版本號升級：claude-code.lock 從 1.9.0 升級至 1.9.1

## [1.9.0] - sunnycore v1.9.0

### Added
- 新增 Technical Architect 角色：專注於技術架構設計、知識管理和文檔化
  - 新增 `claude code/commands/sunnycore_architect.md` 定義 Architect 角色職責與技能
  - 核心職責：技術架構設計、技術決策支援、架構文檔管理、跨領域關注（安全性、效能、擴展性）
  - 管理命令：*conclude、*curate-knowledge、*document-project
- 新增項目驗收流程（Cutover）：在總結階段前增加業務驗收環節
  - 新增 `claude code/tasks/cutover.md` 定義驗收任務流程
  - 新增 `claude code/tasks/fix-acceptance-issues.md` 定義驗收問題修復流程
  - 新增 `claude code/templates/cutover-report-tmpl.yaml` 驗收報告模板
  - 驗收內容：需求驗證、用戶體驗評估、配置驗證、問題記錄、業務價值確認

### Changed
- 重構 Product Owner 角色定位：從技術型 PO 轉變為業務導向 PO
  - 更新 `claude code/commands/sunnycore_po.md`，移除技術架構相關職責
  - PO 專注於：業務需求分析、用戶驗收測試、利害關係人管理、項目交付驗收
  - 移除命令：*conclude、*curate-knowledge、*document-project（轉移至 Architect）
  - 新增命令：*cutover（業務驗收）
- 優化開發工作流程：重新定義階段三為「驗收與總結」
  - 更新 `claude code/README.md` Greenfield 和 Brownfield 流程
  - 階段三步驟調整：
    * 步驟 8/9：`/sunnycore_po *cutover` - 項目驗收
    * 步驟 9/10：`/sunnycore_architect *conclude` - 總結文檔
    * 步驟 10/11：`/sunnycore_architect *curate-knowledge` - 整理知識
    * 步驟 11/12：`/sunnycore_architect *document-project` - 產出專案文件
  - 新增驗收失敗處理分支：`/sunnycore_dev *fix-acceptance-issues` 修復驗收問題
  - 總步驟數從 10/11 步增加至 11/12 步
- 角色職責表更新：在 README 中新增明確的角色職責對照表
  - Architect：技術架構設計、知識管理、技術決策支持
  - Developer：開發實作、技術實現、問題修復
  - PM：需求分析、任務規劃、架構設計
  - PO：業務驗收、需求確認、項目交付
  - QA：代碼審查、質量保證
- 更新配置檔案：`claude code/index.json` 反映新的角色分工與任務關聯
  - 新增 architect agent 定義
  - 更新任務與角色的對應關係
  - 新增 cutover 和 fix-acceptance-issues 任務註冊
- 版本號升級：claude-code.lock 從 1.8.7 升級至 1.9.0

## [1.8.7] - sunnycore v1.8.7

### Changed
- 強化架構設計任務的 context7 工具使用指引：在 `create-architecture.md` 和 `create-brownfield-architecture.md` 中新增 API 文檔檢索功能說明
  - 新增功能描述：「可檢索函式庫與框架的最新 API 文檔，確保架構設計使用當前最佳實踐與 API」
  - 提升架構設計階段對最新技術標準的掌握度與準確性

## [1.8.6] - sunnycore v1.8.6

### Added
- 新增對話壓縮指引：在 `CLAUDE.md` 中新增 `[Summary-Instructions]` 章節，定義 AI 自動壓縮對話時的內容保留與丟棄規則
  - 必須保留內容：[Constraints]、[Tools]、[Output]、[DoD]、所有 [xxx-Guidelines] 相關指引
  - 可壓縮內容：任務狀態資訊（進度、結果等），保留關鍵資訊並摘要
  - 可丟棄內容：已完成任務的測試結果與輸出內容（如已寫入的文檔、程式碼等）
  - 提升 token 使用效率並維持關鍵指引的完整性

## [1.8.5] - sunnycore v1.8.5

### Added
- 強化審查流程追蹤機制：在 `review.md` 的 DoD 檢查清單中新增 epic 更新要求
  - 新增檢查項目：「{root}/docs/epic.md has been updated with completion status and score」
  - 確保審查完成後同步更新 epic 文檔的任務完成狀態與評分
  - 提升專案進度追蹤的完整性與一致性

## [1.8.4] - sunnycore v1.8.4

### Added
- 強化文檔化任務功能：在 `document-project.md` 中新增知識庫整合與專案指引自動更新機制
  - 新增輸入源：`{root}/docs/knowledge/*.md` 知識庫文檔作為文檔化參考
  - 新增輸出項：`{root}/CLAUDE.md` 專案指引文檔的文檔索引自動更新
  - 新增約束條款：「必須在創建架構文檔後更新 {root}/CLAUDE.md 的 Document Index 章節」
  - 新增 DoD 檢查項目：「{root}/CLAUDE.md Document Index 章節已更新並包含新創建的架構文檔」
  - 優化 Steps：在 Sharding and Finalization Phase 新增「更新 CLAUDE.md 文檔索引」步驟
  - 提升文檔化流程完整性與專案指引同步性

## [1.8.3] - sunnycore v1.8.3

### Changed
- 標準化任務文檔章節標題格式：將所有任務文檔中的空格分隔章節標題改為連字符格式，提升文檔格式一致性
  - 格式變更：`[Tool Guidelines]` → `[Tool-Guidelines]`、`[Error Handling]` → `[Error-Handling]`
  - 涵蓋任務：brownfield-tasks、conclude、create-architecture、create-brownfield-architecture、create-epic、create-requirements、curate-knowledge、develop-tasks、document-project、init、plan-tasks、review
- 國際化核心指引文檔：將 `CLAUDE.md` 從繁體中文完整翻譯為英文，提升國際用戶可用性
  - 翻譯範圍涵蓋：通用指引、工具指引、約束指引、任務指引、模板使用指引
  - 保持文檔結構與邏輯不變，僅進行語言轉換
- 版本號更新：claude-code.lock 從 1.8.2 升級至 1.8.3

## [1.8.2] - sunnycore v1.8.2

### Changed
- 國際化任務文檔：將所有任務文檔從繁體中文完整翻譯為英文，提升國際用戶可用性
  - 翻譯範圍涵蓋 14 個任務文檔的所有章節：[Input]、[Output]、[Constraints]、[Tools]、[Tool Guidelines]、[Steps]、[DoD]
  - 涵蓋任務：brownfield-tasks、conclude、create-architecture、create-brownfield-architecture、create-epic、create-requirements、curate-knowledge、develop-tasks、document-project、help、init、plan-tasks、review
  - 保持原有文檔結構與邏輯不變，僅進行語言轉換
  - 版本號更新：claude-code.lock 從 1.8.1 升級至 1.8.2

## [1.8.1] - sunnycore v1.8.1

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

## [1.8.0] - sunnycore v1.8.0

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

## [1.7.39] - sunnycore v1.7.39

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

## [1.7.38] - sunnycore v1.7.38

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

## [1.7.37] - sunnycore v1.7.37

### Added
- 強化審查流程：在 `review.md` 中新增整合測試驗證機制，確保新實作不影響現有程式碼
  - 審查程式碼階段新增：「執行整合測試確認實作不影響原有程式碼」檢查點
  - DoD 新增檢查項目：「已執行整合測試確認實作不影響原有程式碼並紀錄結果」
  - 提升程式碼審查品質與系統穩定性保證

## [1.7.36] - sunnycore v1.7.36

### Changed
- 重構任務命令命名：將 `create-tasks` 重命名為 `create-epic`，更符合敏捷開發中的 Epic 概念
  - README.md：更新所有命令參考（Greenfield 與 Brownfield 流程）
  - commands/sunnycore_pm.md：更新第 5 項自訂指令從 `*create-tasks` 改為 `*create-epic`
  - index.json：更新任務 ID、路徑映射、模板關聯、代理關聯等配置
  - tasks/create-epic.md：將輸出檔案從 `{root}/docs/tasks.md` 改為 `{root}/docs/epic.md`
  - tasks/plan-tasks.md：將輸入檔案從 `{root}/docs/tasks.md` 改為 `{root}/docs/epic.md`
- 版本號更新：claude-code.lock 從 1.7.35 升級至 1.7.36

## [1.7.35] - sunnycore v1.7.35

### Changed
- 國際化指令文件：將所有角色指令檔案（sunnycore_dev.md, sunnycore_pm.md, sunnycore_po.md, sunnycore_qa.md）從繁體中文完整翻譯為英文，提升國際用戶可用性
  - 翻譯範圍涵蓋所有章節：輸入、輸出、角色、技能、約束、自訂指令、專業指引
  - sunnycore_dev.md：開發指引（TDD 實踐準則、程式碼品質標準、測試策略、文檔規範、風險管理）全面英文化
  - sunnycore_pm.md：需求分析指引、架構設計指引、任務管理指引全面英文化
  - sunnycore_po.md：專案總結指引、知識管理指引、架構管理指引全面英文化
  - sunnycore_qa.md：評分指引（7 維度評分標準、品質矩陣、決策規則）全面英文化

## [1.7.34] - sunnycore v1.7.34

### Added
- 新增通用指引：在 `CLAUDE.md` 中新增「工具指引」與「約束指引」章節，明確定義工具使用方法與約束優先級規則
  - 工具指引：強制要求按照 [工具] 中定義的方法執行任務
  - 約束指引：建立三級優先級機制（commands[約束] > tasks[約束] > 預設約束），解決多層級約束衝突問題

### Changed
- 優化 `CLAUDE.md` 文檔結構：調整章節順序，將通用指引提至文檔開頭，提升規則可見度與理解順序

## [1.7.33] - sunnycore v1.7.33

### Changed
- 簡化檔案讀取約束規則：優化四個角色指令檔案（dev、pm、po、qa）中的約束條款，將「除相關程式碼或指令文檔額外要求讀取之文檔外，僅讀取[輸入]中明確定義的檔案」精簡為「必須閱讀所有[輸入]中明確定義的檔案」，提升規則清晰度與可理解性
  - `sunnycore_dev.md`：約束第4條文字簡化
  - `sunnycore_pm.md`：約束第4條文字簡化
  - `sunnycore_po.md`：約束第4條文字簡化
  - `sunnycore_qa.md`：約束第4條文字簡化

## [1.7.32] - sunnycore v1.7.32

### Changed
- 統一指令文檔輸入描述：將四個角色指令檔案（dev、pm、po、qa）中的「輸入」第一項描述統一為「用戶指令輸入與對應之任務文檔」，提升文檔一致性與可讀性
  - `sunnycore_dev.md`：「用戶指令輸入與任務檔案規範」→「用戶指令輸入與對應之任務文檔」
  - `sunnycore_pm.md`：「用戶指令與對應任務檔案」→「用戶指令輸入與對應之任務文檔」
  - `sunnycore_po.md`：「符合自訂指令模式的用戶指令」→「用戶指令輸入與對應之任務文檔」
  - `sunnycore_qa.md`：「用戶指令與對應任務檔案」→「用戶指令輸入與對應之任務文檔」

## [1.7.31] - sunnycore v1.7.31

### Changed
- 精簡指令文檔：移除四個角色指令檔案（dev、pm、qa）中的範例說明，減少冗餘內容並提升文檔簡潔度
  - `sunnycore_dev.md`：移除 `*develop-tasks` 和 `*brownfield-tasks` 的範例說明
  - `sunnycore_pm.md`：移除 `*plan-tasks` 的範例說明
  - `sunnycore_qa.md`：移除 `*review` 的範例說明

### Added
- 新增靜態語言編譯要求：在 `sunnycore_dev.md` 的開發指引中新增「編譯成功要求」約束條款，強制靜態語言專案確保所有程式碼編譯通過

## [1.7.30] - sunnycore v1.7.30

### Changed
- 優化自訂指令格式：統一將所有角色指令檔案（dev、pm、po、qa）中的自訂指令格式從雙星號（`**指令**`）改為單星號（`*指令`），提升視覺簡潔度
- 新增指令使用範例：為需要參數的指令（`*develop-tasks`、`*brownfield-tasks`、`*plan-tasks`、`*review`）增加「範例」說明，改善使用者體驗

## [1.7.29] - sunnycore v1.7.29

### Changed
- 強化檔案讀取約束規則：在所有角色指令檔案（dev、pm、po、qa）中新增「除相關程式碼外或提示詞額外要求外，僅讀取[輸入]中明確定義的檔案」約束條款，優化 token 使用效率並減少非必要檔案讀取

## [1.7.28] - sunnycore v1.7.28

### Changed
- 強化指令約束規則：在所有角色指令檔案（dev、pm、po、qa）中統一新增「必須根據[自訂指令]中的步驟進行操作」約束條款，進一步澄清指令執行流程的規範性要求

## [1.7.27] - sunnycore v1.7.27

### Changed
- 強化所有任務的 DoD（Definition of Done）驗證機制：
  - 在 11 個核心任務文件中統一新增「DoD 驗證階段」
  - 新增「逐項檢查所有 DoD 項目是否已滿足」與「確認所有待辦項目已完成」檢查點
  - 涵蓋任務：brownfield-tasks、create-architecture、create-brownfield-architecture、create-requirements、create-tasks、curate-knowledge、develop-tasks、document-project、help、plan-tasks、review
  - 提升任務執行品質與完成度追蹤一致性

### Added
- brownfield-tasks.md：新增 5 個 DoD 檢查項目（單元測試、整合測試、修復總結、架構符合性、待辦項目完成）
- help.md：新增 DoD 檢查清單

## [1.7.26] - sunnycore v1.7.26

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

## [1.7.25] - sunnycore v1.7.25

## Fixed
- 修正所有指令檔案中的文檔參考路徑：將 `SUNNYCORE.md` 更正為 `CLAUDE.md`
- 修正 `sunnycore_qa.md` 中的錯字：將「測試覆蓋率s架構合規性」更正為「測試覆蓋率與架構合規性」

## [1.7.24] - sunnycore v1.7.24

## Changed
- 優化 `review.md` 審查流程：新增「如果審查通過的話更新 task.md 反映項目進展」步驟，強化審查後的項目追蹤機制

## [1.7.23] - sunnycore v1.7.23

## Changed
- 重構文檔結構：將 `claude code/SUNNYCORE.md` 重命名為 `claude code/CLAUDE.md`，統一文檔命名規範與平台識別

## [1.7.22] - sunnycore v1.7.22

## Changed
- 優化 Context7 工具使用說明：統一 `create-architecture.md` 與 `create-brownfield-architecture.md` 中的 context7 使用場景描述，強調避免重複造輪子的核心目的
- 優化任務文檔格式：改進 `create-requirements.md` 工具部分的格式與描述，提升可讀性

## [1.7.21] - sunnycore v1.7.21

## Changed
- 更新 `plan-tasks.md` 範例路徑：將實作計畫範例從 `ABC-123-plan.md` 修正為 `1-plan.md`，統一檔案命名規範

## [1.7.20] - sunnycore v1.7.20

## Changed
- 優化任務模板格式：將 `tasks-tmpl.yaml` 改為 checkbox 清單格式，提升任務追蹤的可讀性

## [1.7.19] - sunnycore v1.7.19

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

## [1.7.18] - sunnycore v1.7.18
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

## [1.7.17] - sunnycore v1.7.17

## Changed
- 簡化指令文檔格式：將所有 command 檔案（dev、pm、po、qa）從複雜的 XML 結構簡化為清晰的中文 Markdown 格式
- 移除冗餘配置：刪除 `CLAUDE.md` 大型配置文件，將核心規則精簡整合至各指令檔案中
- 優化指引內容：保留核心指引（任務管理、專案總結、知識管理、架構管理、評分標準），移除過度複雜的結構化標籤

## Removed
- `claude code/CLAUDE.md` - 560 行的大型配置文件，內容已精簡整合至各指令檔案

## [1.7.16] - sunnycore v1.7.16

## Changed
- 統一任務提示詞格式：將 `develop-tasks`、`help`、`review` 從 XML 格式改為 Markdown 格式
- 強化任務提示詞結構：在 `develop-tasks` 和 `review` 中新增工具指引、DoD 檢查清單等章節以提升執行品質
- 優化 README：重構 Greenfield/Brownfield 流程說明，採用結構化表格與 Mermaid 流程圖，增強可讀性與視覺化呈現

## [1.7.15] - sunnycore v1.7.15

## Changed
- 統一核心任務提示詞格式：將 `create-architecture`、`create-brownfield-architecture`、`create-requirements`、`create-tasks`、`plan-tasks` 從 XML 格式改為 Markdown 格式
- 強化工作流程結構：新增工具指引、DoD 檢查清單、異常處理等章節以提升任務執行品質
- 新增 concluded-architecture-tmpl 模板並關聯至 document-project 任務

## [1.7.14] - sunnycore v1.7.14

## Changed
- 統一任務提示詞格式：將`brownfield-tasks`、`conclude`、`curate-knowledge`、`document-project`從XML格式改為Markdown格式
- 更新審查報告：優化`brownfield-tasks`、`conclude`、`curate-knowledge`、`document-project`、`prompt-reviewer`的審查報告結構與評分機制

## [1.7.13] - sunnycore v1.7.13

## Changed
- 修正README中安裝腳本名稱為`scripts/sunnycore.sh`
- 優化`brownfield-tasks`提示詞，使其更符合實際需求

## [1.7.11] - sunnycore v1.7.11

## Added
- README：新增以 curl 一行指令執行 `scripts/sunnycore.sh` 的安裝教學

## Changed
- README：將安裝腳本名稱由 `sunnycore.command` 更正為 `scripts/sunnycore.sh`
