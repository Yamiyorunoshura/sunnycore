# Changelog

本專案的所有重要變更都會記錄在此檔案中。

此檔案格式基於 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.0.0/)，
並且本專案遵循[語義化版本](https://semver.org/lang/zh-TW/)。

## [Unreleased]

## [3.3.15] - 2025-10-10

### Changed
- 增強內容組織指引：在 `claude code/CLAUDE.md` 中優化 GUIDANCE 6，明確 Markdown 格式使用規範
  - 新增說明：「use markdown unordered lists, ordered lists, and body text to organize content appropriately」
  - 要求在組織內容時適當使用 Markdown 的無序列表、有序列表和正文
  - 提升模板內容呈現的結構化與可讀性

## [3.3.14] - 2025-10-10

### Added
- 新增輸出要求強化指引：在 `claude code/CLAUDE.md` 中新增 GUIDANCE 21
  - 要求必須根據實際情況更新已存在的輸出文件
  - 禁止忽略輸出要求，即使文件已存在
  - 提升任務執行的輸出完整性與一致性

## [3.3.13] - 2025-10-10

### Changed
- 優化模板使用指引：在 `claude code/CLAUDE.md` 中增強 GUIDANCE 6 和 7，強調語義重組優先於機械填寫
  - 更新 GUIDANCE 6：從「填寫相關模板字段」改為「根據語義重組內容，同時遵循模板結構」
    * 強調語義理解與內容重組的重要性
    * 要求在遵循模板結構的同時，按語義意義組織內容
    * 保持 Markdown 格式完成的要求
  - 更新 GUIDANCE 7：從「維持層級映射並省略空值內容」改為「維持模板結構層級並在各章節內語義重組內容」
    * 強調在維持模板層級結構的前提下，進行語義重組
    * 禁止破壞層級結構或忽略語義關係
    * 提升內容組織的邏輯性與可讀性
  - 提升模板使用的靈活性與內容質量，避免僵化的填寫方式

## [3.3.12] - 2025-10-10

### Changed
- 增強專案初始化任務：在 `init` 任務中新增目錄結構創建與最小可運行應用驗證功能
  - 更新 `claude code/tasks/init.md`：強化初始化任務的完整性
    * 新增輸出項 3：完整目錄結構（從 {ARCH}/*.md 的 work-directory-structure 提取）
    * 新增輸出項 4：最小可運行應用（Hello World 級別入口點並驗證啟動）
    * 新增約束條款 4：必須從架構文檔創建目錄結構，不可假設目錄結構
    * 新增約束條款 5：最小實現僅包含啟動驗證所需的基本代碼，不實現業務邏輯
    * 新增步驟 3：目錄結構與最小實現（提取 work-directory-structure、創建所有必要目錄、創建 Hello World 應用入口點、配置基本啟動腳本）
    * 更新步驟編號：原步驟 3-4 更新為步驟 4-5
    * 新增初始化指引：目錄結構與最小實現指引（提取目錄結構、創建 Hello World 應用、確保應用啟動並返回基本響應）
    * 更新 DoD：新增目錄結構創建檢查、最小 Hello World 應用實現並通過煙霧測試檢查
    * 擴展三個範例：新增目錄創建和最小應用驗證步驟
      - 範例 1 (Microservices Platform): 新增 src/, services/, config/, docker/, tests/ 目錄創建，Express Hello World server 驗證
      - 範例 2 (Python Data Pipeline): 新增 dags/, plugins/, data/, scripts/, tests/ 目錄創建，Airflow Hello World DAG 驗證
      - 範例 3 (React Native Mobile App): 新增 src/, src/components/, src/screens/, src/navigation/, assets/, tests/ 目錄創建，Hello World screen 驗證
  - 提升專案初始化的完整性與可驗證性

## [3.3.11] - 2025-10-10

### Changed
- 優化任務文檔輸出格式說明：在 10 個任務文件中明確標註輸出為 Markdown 格式，提升文檔清晰度
  - 更新 `claude code/tasks/brownfield-plan.md`：輸出 2 和 3 添加格式標註
    * 修復摘要：從「建議以 MARKDOWN 呈現」改為「Fix summary（無指定格式）」
    * 開發筆記：明確標註「"{DEVNOTES}/{task_id}-dev-notes.md" (Markdown format)」
  - 更新 `claude code/tasks/create-architecture.md`：輸出 2 添加「(Markdown format)」標註
  - 更新 `claude code/tasks/create-brownfield-architecture.md`：輸出 1 添加「(Markdown format)」標註
  - 更新 `claude code/tasks/create-prd.md`：輸出 1 添加「(Markdown format)」標註
  - 更新 `claude code/tasks/create-requirements.md`：輸出 1 添加「(Markdown format)」標註
  - 更新 `claude code/tasks/develop-plan.md`：輸出 1 添加「(Markdown format)」標註
  - 更新 `claude code/tasks/develop-prd.md`：輸出 1 添加「(Markdown format)」標註
  - 更新 `claude code/tasks/document-project.md`：輸出 1 添加「(Markdown format)」標註
  - 更新 `claude code/tasks/fix-acceptance-issues.md`：輸出 1 添加「(Markdown format)」標註
  - 更新 `claude code/tasks/review.md`：輸出 1 添加「(Markdown format)」標註
  - 提升任務文檔的格式規範性與一致性

## [3.3.10] - 2025-10-10

### Changed
- 優化專案模板結構：重構 9 個核心模板文件，提升清晰度與可用性
  - **architecture-tmpl.yaml**：擴展外部 API 文檔結構
    * 新增詳細的 external-apis 結構：包含 API 名稱、提供者、版本、base-url、認證方法、端點資訊、速率限制、錯誤處理、回退策略等欄位
    * 新增結構化的 requirements-traceability：包含需求 ID、標題、架構元素、實作備註、理由等欄位
  - **completion-report-tmpl.yaml**：重構為以核心可交付成果為中心的結構
    * 新增 5 個核心可交付成果區塊：Key Decisions、Technical Choices、Issues and Solutions、Evidence References、Recommendations
    * 移除冗餘欄位：project_duration、team_size、risks-realized、team-performance、knowledge-transfer、source-references
    * 優化 recommendations 結構：新增 immediate-actions 和 future-improvements 的詳細欄位
  - **cutover-report-tmpl.yaml**：簡化並結構化驗收報告格式
    * 將 executive-summary 改為 overall-assessment（單一多行文字欄位）
    * 擴展 configuration-required：新增 config_item、description、location、default_value、notes 等欄位
    * 擴展 acceptance-test-results：新增 requirement_id、test_scenario、expected_result、actual_result、status、evidence 等欄位
    * 擴展 issues-found：新增 severity、category、reproduction_steps、business_impact 等欄位
    * 簡化 sign-off：從多個欄位合併為 approved 和 conditions_for_approval
  - **dev-notes-tmpl.yaml**：重組為更清晰的開發筆記結構
    * 將 implementation-summary 改為多行文字格式並新增高層次摘要指引
    * 重構 technical-decisions：新增 context、rationale、alternatives_considered、impact 等欄位
    * 重構 challenges-and-solutions：新增 context、solution、lessons_learned 等欄位
    * 重構 deviations-from-plan：新增 original_plan、actual_implementation、rationale、impact 等欄位
    * 擴展 testing：新增 tdd-cycle-summary、coverage 詳細欄位、results 分類（unit/integration/e2e）
    * 重構 known-issues 和 technical-debt：新增結構化欄位（severity、workaround、tracking、mitigation_plan 等）
  - **epic-tmpl.yaml**：從分類任務改為統一的任務列表結構
    * 移除 task-overview、functional-tasks、non-functional-tasks、infrastructure-tasks、documentation-tasks、progress-summary 等區塊
    * 新增統一的 tasks 陣列：包含 id、name、description、requirement-mapping、architecture-mapping、dependencies、dod、estimated-duration、status、score 等欄位
    * 重構 task-dependencies：新增 task-id、depends-on、dependency-type 等欄位
    * 擴展 milestones：新增 name、tasks、target-date 等欄位
  - **implementation-plan-tmpl.yaml**：增強 TDD 階段說明與結構
    * 優化 red-phase：新增 objective 說明、擴展 acceptance-to-tests 結構、新增 test-cases 欄位（name、type、scenario、expected_failure）
    * 優化 green-phase：新增 objective 說明、擴展 implementation-steps 結構（step、description、files_affected、architecture_component、test_coverage）、擴展 files 欄位（path、purpose、key_functions）
    * 優化 refactor-phase：新增 objective 說明、擴展 refactoring-targets 結構（target、improvement_type、rationale、tests_affected）
    * 更新 additional-details：將 api-documentation 改為 api-integrations
    * 重構 risk-management：新增 risk、probability、impact、mitigation、rollback 等欄位
  - **prd-tmpl.yaml**：添加詳細的結構定義與欄位
    * 擴展 requirements：新增 functional 和 non-functional 的詳細結構（id、title、description、acceptance-criteria、priority、category、target-metric、measurement-method）
    * 擴展 architecture：新增 components 詳細結構、decisions 區塊、requirements-mapping、impact-analysis（針對 Brownfield 專案）
    * 新增 tasks 區塊：包含 id、name、description、requirement-mapping、architecture-mapping、dependencies、dod、status 等欄位
  - **requirement-tmpl.yaml**：移除冗餘章節並添加結構定義
    * 擴展 functional-requirements：新增詳細結構（id、title、description、acceptance-criteria、priority、dependencies）
    * 擴展 non-functional-requirements：新增詳細結構（id、category、requirement、target-metric、measurement-method、priority）
    * 移除冗餘章節：user-stories、glossary、appendix
  - **review-tmpl.yaml**：重構為領域特定的評分系統
    * 新增 task_name 和 domain 欄位（backend/frontend/database/integration/infrastructure）
    * 重構 quality-scores：改為動態的 dimensions 結構（基於領域的維度）
    * 重構 test-summary：將 all_passed 改為 all_tests_passed、test_output 改為 test_execution_output、新增 performance_metrics
    * 重構 findings：整合 code-review、security-review、performance-review、documentation-review 為統一的 findings 陣列（severity、category、description、location、evidence、recommendation、action_required）
    * 新增 alignment-verification：整合 compliance-check 內容（requirements_fulfilled、requirements_partial、requirements_missing、architecture_alignment、plan_adherence）
    * 新增 risk-assessment 欄位
- 擴展架構設計指引：在 `create-architecture.md` 和 `create-brownfield-architecture.md` 中新增外部 API 文檔步驟
  - 新增「External API Documentation」步驟（步驟 4）：要求詳細記錄每個外部 API 整合
    * API 基本資訊：名稱與提供者、完整端點 URL、base paths、版本
    * 認證與安全：認證方法、憑證管理方式
    * 請求/回應規範：JSON schema、資料類型、必要欄位、API 呼叫方法（REST/GraphQL/RPC）
    * 技術細節：速率限制與重試策略、錯誤處理模式與錯誤碼、版本控制策略、SLA 要求
    * 整合策略：功能描述、系統內整合點、API 不可用時的備援策略
  - `create-brownfield-architecture.md` 額外要求：驗證現有外部 API 整合的持續相容性或記錄所需變更
  - 原「Traceability & Justification」步驟從步驟 4 順延為步驟 5
- 提升模板與任務文檔的一致性、可用性與維護性

## [3.3.9] - 2025-10-10

### Changed
- 增強架構設計指引：在架構任務文件中新增外部 API 文檔化要求，提升 API 整合文檔完整性
  - 更新 `claude code/tasks/create-architecture.md`：新增「External API Documentation」指引章節（步驟 4）
    * 要求詳細記錄每個外部 API 整合：API 名稱與提供者、完整端點 URL、認證方法、請求/回應格式規範
    * 新增 API 技術細節記錄：呼叫方法（REST/GraphQL/RPC）、速率限制與重試策略、錯誤處理模式
    * 新增整合策略要求：系統內整合點、API 不可用時的備援策略、版本控制策略、SLA 要求
  - 更新 `claude code/tasks/create-brownfield-architecture.md`：新增「External API Documentation」指引章節（步驟 4）
    * 包含與 greenfield 相同的外部 API 文檔化要求
    * 新增現有 API 整合檢查：驗證現有外部 API 整合的持續相容性或記錄所需變更
  - 原「Traceability & Justification」章節從步驟 4 順延為步驟 5
  - 提升架構設計的 API 整合透明度與可維護性

## [3.3.8] - 2025-10-10

### Changed
- 重命名任務：將 `brownfield-tasks` 重命名為 `brownfield-plan`，更準確反映任務目的
  - 任務文件：`claude code/tasks/brownfield-tasks.md` → `claude code/tasks/brownfield-plan.md`
  - 更新 GOAL：從「Re-develop tasks that failed review」改為「Re-develop plan that failed review」
  - 更新命令參考：`sunnycore_dev.md` 中的命令從 `*brownfield-tasks` 改為 `*brownfield-plan`
  - 更新文檔引用：在 `README.md` 中更新所有流程說明中的命令參考（4 處）
  - 更新配置文件：在 `index.json` 中更新任務 ID、路徑、關聯關係（7 處）
  - 提升任務命名的語義清晰度與一致性

## [3.3.7] - 2025-10-10

### Changed
- 精簡核心指引系統：在 `claude code/CLAUDE.md` 中移除冗餘的 GUIDANCE 11 和 12，重新編號指引結構
  - 移除 GUIDANCE 11: [Input] Tag - 該驗證規則已整合至任務文檔中，無需在核心指引重複定義
  - 移除 GUIDANCE 12: [Output] Tag - 該交付物規則已整合至任務文檔中，無需在核心指引重複定義
  - 重新編號：原 GUIDANCE 13-23 更新為 GUIDANCE 11-20
  - 提升核心指引的簡潔性與聚焦度，減少冗餘內容

## [3.3.6] - 2025-10-10

### Changed
- 擴展核心指引系統：在 `claude code/CLAUDE.md` 中新增 13 個結構化 GUIDANCE（11-23），提升任務執行的規範性與一致性
  - GUIDANCE 11: [Input] Tag - 要求驗證所有必要輸入存在後再執行，避免缺少輸入導致的錯誤
  - GUIDANCE 12: [Output] Tag - 要求產生所有指定的交付物，確保輸出完整性
  - GUIDANCE 13: [Steps] Tag - 要求順序執行所有步驟並達成預期成果
  - GUIDANCE 14: [DoD] Tag - 要求驗證所有 DoD 檢查項後才能標記任務完成
  - GUIDANCE 15: [Role] & [Skills] Tags - 要求採用指定角色視角並應用技能
  - GUIDANCE 16: [Constraints] Tag - 要求嚴格遵循所有約束條款
  - GUIDANCE 17: [Tools] Tag - 要求在建議步驟使用工具
  - GUIDANCE 18: [Path-Variables] Tag - 要求替換路徑變數為實際路徑
  - GUIDANCE 19: [*-Guidelines] Tags - 要求研究並應用領域指引
  - GUIDANCE 20: [Error-Handling] Tag - 要求諮詢錯誤處理策略
  - GUIDANCE 21: [Decision-Criteria] & [Decision-Rules] Tags - 要求應用決策規則
  - GUIDANCE 22: [Examples] Tag - 要求參考範例理解預期流程
  - GUIDANCE 23: [blocking-conditions] Tag - 明確僅在阻塞條件發生時暫停執行
- 精簡開發任務文檔：優化 `develop-plan.md` 執行流程說明
  - 移除 [Execution] 章節，改為獨立的 [Blocking-Conditions] 章節
  - 移除 [Status-Update-Templates] 章節：刪除 RED/GREEN/REFACTOR 階段的狀態更新模板
  - 移除 [Driver-Pseudocode] 章節：刪除 TDD 循環的偽代碼示範
  - 簡化 TDD Development Phase 步驟說明：移除迭代說明和非停止節奏提示
  - 提升任務文檔的簡潔性，減少冗餘內容
- 標準化阻塞條件引用：在 `sunnycore_dev.md` 中更新約束條款 3
  - 將 "defined blocking conditions" 改為 "[blocking conditions]"
  - 明確引用標籤化的阻塞條件定義，提升引用一致性

## [3.3.5] - 2025-10-10

### Changed
- 強化任務執行連續性：優化任務結論訊息處理機制，確保執行流程不中斷
  - 更新 `claude code/CLAUDE.md`：在 GUIDANCE 10 中新增澄清說明
    * 明確任務結論訊息為微更新，不應導致執行暫停
    * 強調除非存在阻塞條件，否則應立即進行下一步驟
  - 涵蓋文件：`sunnycore_architect.md`、`sunnycore_dev.md`、`sunnycore_pm.md`、`sunnycore_po.md`、`sunnycore_qa.md`
- 精確化約束條件：在 5 個角色命令文件中更新步驟完成要求
  - 更新約束條款 3：從「Must complete all the steps without stopping unless you need to ask user for confirmation」改為「Must complete all steps without stopping; do not pause between sub-phases under [Steps] unless defined blocking conditions occur or the prompt clearly stated that user's confirmations is needed」
  - 明確定義阻塞條件：缺少關鍵輸入、意外測試失敗、需要用戶批准的風險操作、工具缺少非互動標誌
  - 提升命令執行的連續性與可預測性
- 增強開發計劃任務指引：在 `develop-plan.md` 中新增執行流程說明與範例
  - 新增 [Execution] 章節：明確連續節奏、微更新處理、阻塞條件定義
  - 新增 [Status-Update-Templates] 章節：提供 RED、GREEN、REFACTOR 階段的標準更新模板
  - 新增 [Driver-Pseudocode] 章節：提供 TDD 循環的偽代碼示範
  - 優化 TDD Development Phase 步驟說明：強調不間斷節奏，發出微更新後立即繼續
  - 提升開發任務執行的清晰度與一致性

## [3.3.4] - 2025-10-10

### Changed
- 強化任務執行完整性：在所有 5 個角色命令文件中新增完成度約束
  - 新增約束條款：「Must complete all the steps without stopping unless you need to ask user for confirmation.」
  - 涵蓋文件：`sunnycore_architect.md`、`sunnycore_dev.md`、`sunnycore_pm.md`、`sunnycore_po.md`、`sunnycore_qa.md`
  - 確保所有角色命令執行時完成所有步驟,除非需要用戶確認
  - 提升命令執行的完整性與可靠性

## [3.3.3] - 2025-10-10

### Changed
- 強化命令約束：在所有 6 個角色命令文件中新增 GUIDANCE 遵循要求
  - 新增約束條款："Must follow all the GUIDANCE in {C}"
  - 涵蓋文件：`sunnycore_architect.md`、`sunnycore_assistant.md`、`sunnycore_dev.md`、`sunnycore_pm.md`、`sunnycore_po.md`、`sunnycore_qa.md`
  - 確保所有角色命令執行時遵循 CLAUDE.md 中定義的核心指引
  - 提升命令執行的一致性與規範性

## [3.3.2] - 2025-10-10

### Changed
- 優化文檔指引格式：將 `claude code/CLAUDE.md` 和 `cursor/cursor.mdc` 中所有 GUIDANCE (1-9) 從 HTML 註解格式改為強調格式
  - 格式變更：`<!-- ... -->` → `**MUST** ... **MUST NOT** ...`
  - 新增負面約束說明，明確禁止的行為
  - 提升指引的可讀性與強制性表達
- 新增任務結論指引：在兩個文檔中新增 GUIDANCE 10
  - 要求每個任務完成後提供簡短結論
  - 結論格式：「I have completed {task_name}. To {purpose}, I am going to {next_task}」
  - 提升任務執行的連貫性與可追蹤性
- 清理 `cursor/cursor.mdc` 中的重複內容：移除文件末尾重複的 GUIDANCE 1-9 段落

## [3.3.0] - sunnycore v3.3.0

### Added
- 新增 Cursor 編輯器支援：完整移植 Claude Code 版本至 Cursor 平台
  - 新增 `cursor/` 目錄結構：包含所有 Cursor 專用配置與文檔
    * `cursor/commands/`：6 個角色命令文件（sunnycore_architect、sunnycore_assistant、sunnycore_dev、sunnycore_pm、sunnycore_po、sunnycore_qa）
    * `cursor/tasks/`：33 個任務文件（涵蓋完整開發工作流程）
    * `cursor/templates/`：9 個 YAML 模板（架構、需求、PRD、任務、計劃、審查、開發筆記、驗收、完成報告）
    * `cursor/scripts/`：2 個文檔拆分腳本（shard-architecture.py、shard-requirements.py）
    * 配置文件：cursor.mdc、index.json、mcp.json、DEPENDENCIES.md、README.md
  - 新增 Cursor 版本的完整工作流程文檔：
    * 技術支援流程（sunnycore_assistant）
    * PRD 流程（適用於小型變更）
    * Greenfield 專案流程（從零開始）
    * Brownfield 專案流程（現有專案改進）
  - 支援 MCP 伺服器整合：context7、sequential-thinking、playwright

### Changed
- 增強安裝腳本功能：改進 `scripts/install.py` 用戶體驗
  - 優化進度條顯示：新增旋轉動畫符號、漸變效果、緊湊格式輸出
  - 改進時間顯示：優化速度計算、剩餘時間預估、完成狀態提示
  - 新增 `install_cursor()` 方法：支援 Cursor 版本安裝
  - 控制更新頻率：避免過度刷新，提升終端顯示穩定性

## [3.2.11] - sunnycore v3.2.11

### Changed
- 優化任務文檔步驟格式：重構 19 個任務文件的 Steps 部分，採用目標導向結構，提升可讀性與執行清晰度
  - 步驟格式優化：將 "Phase" 風格步驟改為 "目標任務 + 預期成果（Outcome）" 結構
    * 步驟名稱簡化並聚焦行動目標（如 "Preparation Phase" → "Preparation & Analysis"）
    * 每個步驟明確定義核心任務與預期成果（Outcome）
    * 改善步驟描述的目標導向性，使執行者清楚理解每步驟的交付成果
  - 涵蓋任務：brownfield-tasks、conclude、consult、create-architecture、create-brownfield-architecture、create-epic、create-plan、create-prd、create-requirements、curate-knowledge、cutover、develop-plan、develop-prd、document-project、fix-acceptance-issues、fix-design-conflicts、init、review、validate-design
  - 提升任務文檔的執行清晰度、成果可驗證性與專業性

## [3.2.10] - sunnycore v3.2.10

### Changed
- 強化任務管理指引：在 `claude code/CLAUDE.md` 中新增 GUIDANCE 9 - 要求所有 todo 項目必須是原子性且可操作的
  - 新增指引：「All the todo items created must be atomic and actionable」
  - 確保任務拆分符合最佳實踐，提升執行效率與追蹤精確度
  - 提升專案管理品質與任務可執行性

## [3.2.9] - sunnycore v3.2.9

### Changed
- 優化任務文檔步驟格式：簡化 19 個任務文件的 Steps 和 DoD 部分，提升可讀性與一致性
  - 步驟格式重構：將 "Phase" 風格改為 "Task + Expected outcome" 結構
    * 步驟名稱簡化（如 "Preparation Phase" → "Preparation"）
    * 每個步驟明確定義任務（Task）與預期成果（Expected outcome）
    * 移除冗長的子步驟說明，專注於結果導向的目標描述
  - DoD 條目合併與簡化：將重複或相關的檢查項目合併為更簡潔的描述
  - 涵蓋任務：brownfield-tasks、conclude、consult、create-architecture、create-brownfield-architecture、create-epic、create-plan、create-prd、create-requirements、curate-knowledge、cutover、develop-plan、develop-prd、document-project、fix-acceptance-issues、fix-design-conflicts、init、review、validate-design
  - 提升任務文檔的清晰度、一致性與可執行性

## [3.2.8] - sunnycore v3.2.8

### Changed
- 重構文檔指引系統：簡化 `CLAUDE.md` 核心指引，提升可讀性與記憶性
  - 將詳細的 Constraints、Template-Usage-Guidelines、Summary-Instructions 等章節（約 88 行）簡化為 8 個簡潔的 GUIDANCE 段落
  - 採用 HTML 註解格式（`<!-- ... -->`）包裹指引內容，保持結構清晰
  - GUIDANCE 1：強調任務執行的完整性與流程遵循
  - GUIDANCE 2：要求主動請求澄清而非猜測
  - GUIDANCE 3：確保讀取所有必要輸入文件
  - GUIDANCE 4：定義約束衝突處理優先級（CLAUDE.md > commands > tasks）
  - GUIDANCE 5：強制完成所有 todo 項目並驗證 DoD
  - GUIDANCE 6：簡化模板使用說明
  - GUIDANCE 7：簡化 YAML 轉 Markdown 規則說明
  - GUIDANCE 8：精簡對話壓縮指引
  - 減少約 80% 的指引文字量，提升閱讀效率
- 優化任務約束表達方式：在 24 個任務文件中將約束從正面指令改為負面禁止，提升規範清晰度
  - 表達方式轉換：「Must do X」→「Do not fail to do X」或「Do not do Y」
  - 涵蓋任務：brownfield-tasks、conclude、consult、create-architecture、create-brownfield-architecture、create-epic、create-plan、create-prd、create-requirements、curate-knowledge、cutover、develop-plan、develop-prd、document-project、fix-acceptance-issues、fix-design-conflicts、init、review、validate-design
  - 範例轉換：
    * 「Must ensure fixed code runs properly」→「Do not deliver fixes that fail to run properly」
    * 「Must verify all requirements」→「Do not skip requirement verification」
  - 提升約束的明確性與違規行為的識別度
- 精簡命令文檔格式：移除 `sunnycore_architect.md`、`sunnycore_assistant.md`、`sunnycore_po.md` 中的多餘空白行，提升文檔簡潔度

## [3.2.7] - sunnycore v3.2.7

### Changed
- 強化任務完成指引：優化 `CLAUDE.md` 中的 todo 完成規則，明確要求逐一完成且不得跳過任何項目
  - 第 7 條規則：從「Complete all to-do items in the todo list」擴展為「Complete all to-do items one-by-one in the todo list. Never stops when remaining to-do items still exist. Never skip any todo items.」
  - 明確禁止跳過任何 todo 項目，確保任務執行的完整性與連續性
  - 提升任務執行品質與流程遵循度

## [3.2.6] - sunnycore v3.2.6

### Changed
- 優化任務文檔驗收標準措辭：改進 18 個任務文件的 DoD (Definition of Done) 條目，使其更清晰、更具操作性
  - 將被動語態改為主動語態（如「has been」→「is」、「have been」→「are」）
  - 增強完整性描述（如「已讀取」→「fully understood」、「已創建」→「exists」）
  - 明確狀態驗證（如「已完成」→「is complete」、「已通過」→「passing」）
  - 涵蓋任務：consult、create-architecture、create-brownfield-architecture、create-epic、create-plan、create-prd、create-requirements、curate-knowledge、cutover、develop-plan、develop-prd、document-project、fix-acceptance-issues、fix-design-conflicts、help、init、review、validate-design
  - 提升驗收標準的明確性與可驗證性

## [3.2.5] - sunnycore v3.2.5

### Changed
- 優化總結任務文件路徑通用性：在 `conclude.md` 中將版本鎖定檔案引用從 "sunnycore.lock" 改為 "*.lock"
  - 約束條款第 3 項：改為泛化的 "*.lock" 檔案引用，提升任務適用性
  - 約束條款第 5 項：版本解析說明同步更新為 "*.lock" 格式
  - 提升專案總結任務的通用性與可重用性
- 精簡總結任務 DoD 檢查清單：在 `conclude.md` 中移除冗餘檢查項，聚焦核心驗收標準
  - 移除「*.lock 檔案已讀取且版本號已成功解析」（已包含在文檔生成流程中）
  - 移除「工作流程類型已確定」（非核心驗收標準）
  - 移除「完成報告內容完整涵蓋 5 大核心內容項」（已包含在模板合規檢查中）
  - 移除「僅保留 architecture/、knowledge/ 和 completion-report.md 在 docs/ 目錄」（已包含在歸檔檢查中）
  - 保留核心檢查項：文檔掃描、報告生成與模板合規、歸檔完成、參考更新
  - 提升 DoD 清單的簡潔性與關鍵性

## [3.2.4] - sunnycore v3.2.4

### Changed
- 優化架構設計命令參數說明：在 `sunnycore_architect.md` 中為架構設計命令新增可選參數提示
  - `*create-architecture` 改為 `*create-architecture {preferrence(optional)}`：允許用戶提供架構設計偏好
  - `*create-brownfield-architecture` 改為 `*create-brownfield-architecture {preferrence(optional)}`：允許用戶提供遷移架構偏好
  - 提升命令使用的靈活性與用戶自主性
- 優化 TDD 流程說明：澄清 `develop-plan.md` 和 `develop-prd.md` 中的測試失敗預期
  - RED Phase：從「確保所有測試如預期失敗」改為「確保所有測試失敗於預期錯誤而非意外錯誤（如無法編譯、語法錯誤等）」
  - TDD Development Phase：同步優化測試失敗描述，強調預期錯誤與意外錯誤的區別
  - 提升 TDD 實踐指引的準確性與可理解性

## [3.2.3] - sunnycore v3.2.3

### Changed
- 精簡核心指引文檔：簡化 `CLAUDE.md` 中的完成門檻約束，僅保留核心規則
  - 保留核心約束條款：禁止在 ToDo 未完成時結束、合法結束狀態定義（completed/blocked/external-interrupt）
  - 移除詳細的 Wrap-Up-Gatekeeper 擴展約束（10.3-10.8）：驗證前置檢查、最終檢查、工具規則遵循、中斷處理、一致性檢查、優先級擴展
  - 提升文檔簡潔度，聚焦核心執行規則
- 優化開發任務輸出說明：整合 `develop-plan.md` 的輸出要求，強調交付品質
  - 輸出 2：從「高質量、已測試的代碼實作對齊實作計畫」改為「高質量、已測試、已重構的代碼實作高度對齊實作計畫」
  - 移除原輸出 4：「遵循最佳實踐的重構代碼對齊實作計畫」（已整合至輸出 2）
  - 明確要求代碼實作需同時滿足：測試覆蓋、重構品質、計畫對齊三項標準
- 優化 PRD 開發任務輸出說明：強化 `develop-prd.md` 的架構對齊要求
  - 輸出 2：從「高質量、已測試的代碼實作」改為「高質量、已測試、已重構的代碼實作高度對齊架構設計」
  - 明確要求 PRD 實作需嚴格遵循架構設計規範

## [3.2.2] - sunnycore v3.2.2

### Changed
- 強化實作計畫對齊：更新 `claude code/tasks/develop-plan.md` 輸出說明，確保開發成果與實作計畫一致
  - 第 2 項輸出：程式碼實作需符合實作計畫要求
  - 第 3 項輸出：測試覆蓋範圍需符合實作計畫規範
  - 第 4 項輸出：重構程式碼需遵循實作計畫定義的最佳實踐
  - 提升開發流程與計畫文件的一致性

## [3.2.1] - sunnycore v3.2.1

### Changed
- 優化任務規劃流程說明：精確化 `claude code/tasks/create-plan.md` 中的進度追蹤範圍描述
  - Setup Phase：將「所有任務」改為「計劃創建工作」，明確進度追蹤的具體範圍
  - 提升任務說明的精確度與可理解性

## [3.2.0] - sunnycore v3.2.0

### Added
- 新增使用範例章節：為核心代理和命令文件新增完整的實戰範例，提升可用性
  - 新增 `claude code/agents/planner.md` 的 [Examples] 章節：3 個規劃範例
    * Example 1: Simple Feature Addition - 簡單功能新增的規劃方法
    * Example 2: Cross-Module Integration - 跨模組整合的規劃策略
    * Example 3: System-Level Migration - 系統級遷移的規劃路線圖
  - 新增 `claude code/agents/progress-manager.md` 的 [Examples] 章節：3 個記錄範例
    * Example 1: Simple Bug Fix Recording - 簡單 bug 修復的記錄策略
    * Example 2: Optimization with Knowledge Update - 優化工作的進度與知識記錄
    * Example 3: Complex Problem Solving - 複雜問題的多文件記錄策略
  - 新增 `claude code/commands/sunnycore_assistant.md` 的 [Examples] 章節：3 個技術支援範例
    * Example 1: Simple Bug Fix - 簡單 bug 的診斷與修復流程
    * Example 2: Performance Optimization - 效能優化的調查與實施流程
    * Example 3: Architecture Refactoring - 架構重構的規劃與執行流程

### Changed
- 優化工具使用說明：增強核心代理和任務文件中的 MCP 工具描述，提升工具使用指引的清晰度
  - 優化 `claude code/agents/planner.md` 工具說明：
    * claude-context (MCP)：新增「理解現有架構、識別依賴、評估變更範圍」等具體使用場景
    * sequentialthinking (MCP)：新增「系統性推理、評估技術權衡、識別風險與依賴」等使用說明
  - 優化 `claude code/agents/progress-manager.md` 工具說明：
    * 新增 [Tools] 章節，明確定義 sequentialthinking 和 claude-context 的使用場景
    * sequentialthinking：用於分析上下文並進行語意重要性分類
    * claude-context：用於搜尋現有知識文件以避免重複創建
  - 優化 `claude code/commands/sunnycore_assistant.md` 工具說明：
    * todo_write：從「追蹤工作進度」擴展為「創建和更新任務清單以組織工作階段」
    * sequentialthinking：從「推理問題和解決方案」擴展為「系統性推理根因分析、評估解決方案、理解技術權衡」
    * claude-context：從「搜尋相關代碼」擴展為「語意搜尋理解現有實作、識別需修改的文件、尋找參考範例」
    * context7：從「搜尋相關 API 文檔」擴展為「搜尋 API 文檔和庫使用範例，確保正確使用模式」
- 擴展任務工具支援：在 9 個任務文件中新增 context7 和 playwright 工具的使用說明
  - 新增 context7 (MCP) 工具至 7 個任務：
    * `brownfield-tasks.md`：Step 2 修復階段 - 驗證 API 使用或查找官方疑難排解指南
    * `consult.md`：Step 2 需求分析階段 - 評估技術可行性時查詢 API 文檔
    * `create-plan.md`：Step 3 GREEN 階段規劃 - 查詢外部套件的官方 API 使用方式
    * `curate-knowledge.md`：Step 2 知識庫設計階段 - 驗證最佳實踐是否符合官方指引
    * `fix-acceptance-issues.md`：Step 2-6 - 修復涉及外部服務整合或配置時查詢官方文檔
    * `review.md`：Step 2 代碼和測試審查階段 - 驗證外部 API 使用正確性
  - 新增 playwright (MCP) 工具至 4 個任務：
    * `consult.md`：Step 2 需求分析階段 - 研究競品產品實作方式
    * `create-architecture.md`：Step 1-2 - 研究類似系統架構設計和實作案例
    * `create-brownfield-architecture.md`：Step 1-2 - 研究架構遷移模式和整合案例
    * `document-project.md`：Step 1-2 - 研究開源專案的架構文檔結構和呈現方式

## [3.1.1] - sunnycore v3.1.1

### Changed
- 優化任務文檔輸出說明：更新 create-architecture、create-brownfield-architecture、create-requirements 任務的輸出流程
  - 統一輸出格式：先生成單一臨時文件（architecture.md 或 requirements.md），再執行分片腳本
  - `create-architecture.md`：簡化輸出說明，改為生成臨時 architecture.md 並說明需執行 shard-architecture.py 腳本
  - `create-brownfield-architecture.md`：新增臨時 architecture.md 輸出項，明確說明分片腳本執行流程
  - `create-requirements.md`：新增臨時 requirements.md 輸出項，明確說明分片腳本執行流程
  - 提升任務輸出流程的清晰度與一致性

## [3.1.0] - sunnycore v3.1.0

### Changed
- 優化 MCP 工具使用說明：修正並增強所有任務文檔中的 MCP 工具使用指引
  - 工具名稱修正：將 `sequentialthinking` 統一改為 `sequential-thinking` (MCP)
  - 增強使用情境說明：為每個工具添加詳細的「何時使用」(When to use) 說明
  - 優化 `sequential-thinking` 工具描述：
    * 明確各任務階段的推理目標（需求分解、架構評估、設計驗證等）
    * 添加具體使用場景（複雜問題評估、多方案比較、影響分析等）
  - 優化 `claude-context` 工具描述：
    * 提供具體查詢示例（"What is the existing implementation?" "How to integrate with existing system?"）
    * 明確搜尋目標（現有架構邊界、公開契約、整合點等）
  - 優化 `context7` 工具描述：
    * 明確查詢官方文檔和 API 參考的使用情境
    * 添加版本兼容性驗證和架構指引查找的說明
  - 優化 `playwright` 工具描述：
    * 明確網頁研究的具體使用場景（競品分析、UI 流程範例收集等）
  - 涵蓋任務：brownfield-tasks、conclude、consult、create-architecture、create-brownfield-architecture、create-epic、create-plan、create-prd、create-requirements、curate-knowledge、cutover、develop-plan、develop-prd、document-project、fix-acceptance-issues、fix-design-conflicts、init、review、validate-design
- 精簡核心指引文檔：移除 `CLAUDE.md` 中的 [Tool-Guidelines] 章節
  - 原因：工具使用指引已整合至各任務文檔的 [Tools] 章節中
  - 避免指引重複，提升維護效率
  - 減少 token 使用量

## [3.0.0] - sunnycore v3.0.0

### Changed
- 重構文檔架構：將指導方針從角色命令文件遷移至任務文件，提升文檔組織性與可維護性 (**破壞性變更**)
  - 從 5 個角色命令文件中移除大量指導方針章節（約 700 行）
    * `sunnycore_architect.md`：移除 Project-Summary-Guidelines、Knowledge-Management-Guidelines、Architecture-Management-Guidelines
    * `sunnycore_dev.md`：移除 Development-Guidelines
    * `sunnycore_pm.md`：移除 Requirements-Analysis-Guidelines、Architecture-Design-Guidelines、Task-Management-Guidelines
    * `sunnycore_po.md`：移除部分指導方針內容
    * `sunnycore_qa.md`：移除大量審查指導方針
  - 將指導方針整合至對應的任務文件中（約 1500 行新增內容）
    * 在 `brownfield-tasks.md` 中新增 Development-Guidelines（TDD 實踐、程式碼品質標準、測試要求、文檔與風險管理）
    * 在 `create-architecture.md` 中新增 Architecture-Design-Guidelines（模板合規、決策記錄、橫切關注點、可追溯性與正當性）
    * 在所有任務文件中增強結構：新增詳細的步驟說明、完整的示例章節、明確的目標描述
  - 優化任務文件可讀性：
    * 簡化步驟描述，將原本的詳細子步驟改為結果導向的目標描述
    * 統一步驟命名格式，提升文檔一致性
    * 移除冗餘的條件分支說明，專注於核心流程
  - 提升系統可維護性：將通用指導方針集中管理，減少角色文件的複雜度，使任務執行更加聚焦

### BREAKING CHANGES
- **文檔結構變更**：
  - 角色命令文件不再包含詳細的指導方針章節，僅保留核心職責與命令定義
  - 所有詳細的執行指導方針現在位於對應的任務文件中
  - 任務文件的步驟描述從詳細的操作步驟改為結果導向的目標描述
- **影響範圍**：
  - 需要更新任何直接引用舊指導方針章節的外部文檔或腳本
  - 任務執行流程保持不變，僅文檔組織結構發生變化

## [2.1.1] - sunnycore v2.1.1

### Changed
- 優化 Technical Assistant 約束說明：在 `sunnycore_assistant.md` 中補充 progress-manager 的用途描述
  - 第 3 條約束：從「Must call progress-manager sub-agent after completing work」擴展為「Must call progress-manager sub-agent after completing work for recording progress and curating knowledge」
  - 明確 progress-manager 的兩大核心功能：記錄進度與整理知識
  - 提升文檔說明的完整性與清晰度

## [2.1.0] - sunnycore v2.1.0

### Added
- 新增任務規劃代理：新增 planner sub-agent 提供執行前的高層次規劃能力
  - 新增 `claude code/agents/planner.md`：定義 planner 角色職責與規劃框架
    * 核心能力：任務分析與拆解、技術方案評估、風險識別、依賴分析、策略規劃
    * 輸出規劃：步驟概覽、關鍵決策點、預期成果、風險與依賴、成功標準
    * 約束：僅使用唯讀工具（read_file、grep、codebase_search、list_dir、sequentialthinking）
    * 輸出方式：僅在對話中顯示，不保存至文件
  - 更新 `claude code/commands/sunnycore_assistant.md`：強制要求先調用 planner 生成執行計劃
    * 新增約束第 1-2 條：必須先調用 planner sub-agent、必須遵循 planner 生成的計劃
    * 新增 DoD 檢查項：執行計劃已通過 planner sub-agent 生成
    * 優化約束順序：將 planner 相關約束提至 [Constraints] 開頭
  - 提升技術支援工作流程的規劃性與執行品質

## [2.0.0] - sunnycore v2.0.0

### Added
- 新增設計驗證與修復系統:提供設計文檔一致性檢查與自動修復能力
  - 新增 `validate-design` 任務:支援 PRD 和完整流程的設計驗證
    * PRD 驗證:檢查 PRD 內部一致性、與現有架構對齊、內容真實性
    * 完整驗證:檢查需求-架構-任務-計劃的雙向引用、覆蓋率、一致性
    * 輸出驗證報告至 `docs/design-validation.md`
  - 新增 `fix-design-conflicts` 任務:自動修復設計驗證中發現的問題
    * 支援修復捏造內容、破損引用、衝突、不一致性、覆蓋率缺口
    * 提供互動式修復策略確認
    * 修復完成後自動清理驗證報告
  - 更新 PO 角色:新增設計驗證與修復職責

### Changed
- 重構任務命名與工作流程:優化計劃創建與開發流程 (**破壞性變更**)
  - `plan-tasks` → `create-plan`:改為批量創建所有任務的實作計劃
    * 支援為 epic 中所有任務一次性創建 TDD 計劃
    * 整合知識庫最佳實踐至計劃創建流程
    * 輸出格式:`{PLAN}/1-plan.md`, `{PLAN}/2-plan.md`, etc.
  - `develop-tasks` → `develop-plan`:基於計劃執行開發
    * 強調基於預先創建的計劃進行 TDD 開發
    * 明確引用 create-plan 階段產生的計劃文檔
  - `tasks-tmpl` → `epic-tmpl`:任務清單模板重命名，更符合敏捷術語

- 提升文檔品質與可維護性:所有任務文件新增 GOAL 說明
  - 在 17 個任務文件開頭新增簡潔的 GOAL 說明
  - 涵蓋任務:brownfield-tasks、conclude、consult、create-architecture、create-brownfield-architecture、create-epic、create-plan、create-prd、create-requirements、curate-knowledge、cutover、develop-plan、develop-prd、document-project、fix-acceptance-issues、init、review
  - 提升任務文檔的自我描述性與目標明確性

- 優化架構文檔指引:新增工作目錄結構範例
  - 在 `create-architecture.md`、`create-brownfield-architecture.md`、`document-project.md` 中新增 [Example] 章節
  - 提供工作目錄結構的具體範例與描述
  - 改善架構設計階段的實用性指引

- 優化任務規劃流程:`create-plan` 改為批量創建模式
  - 從「為單個任務創建計劃」改為「為所有任務批量創建計劃」
  - 新增知識庫整合:計劃創建時自動參考最佳實踐與經驗教訓
  - 提升計劃創建效率與知識復用

- 更新工作流程文檔:整合設計驗證階段
  - 在 PRD 流程中新增可選的設計驗證步驟 (步驟 2.5)
  - 在完整開發流程中新增可選的設計驗證步驟 (步驟 5)
  - 新增設計驗證與修復流程圖與使用指引
  - 更新流程對比表與角色職責表

### Removed
- 刪除未使用模板:移除 `project-knowledge-tmpl.yaml`
  - 知識庫文檔改為採用語義分類方式管理 (best-practices、errors、problem-solving)
  - 簡化模板系統複雜度

### BREAKING CHANGES
- **任務命名變更**:
  - `/sunnycore_dev *plan-tasks {task_id}` → `/sunnycore_dev *create-plan`
  - `/sunnycore_dev *develop-tasks {task_id}` → `/sunnycore_dev *develop-plan {task_id}`
- **模板命名變更**:
  - `tasks-tmpl.yaml` → `epic-tmpl.yaml`
- **工作流程調整**:
  - create-plan 現在為批量操作，一次性為所有任務創建計劃
  - 步驟編號調整:Greenfield 和 Brownfield 流程中的步驟編號均有變化

## [1.15.7] - sunnycore v1.15.7

### Changed
- 優化文檔化任務使用建議：在 `claude code/README.md` 中為 `*document-project` 命令新增驗收提示
  - 在三個工作流程中（PRD 流程、Greenfield 流程、Brownfield 流程）新增說明：「建議先親身驗收項目，如發現問題可使用 `/sunnycore_assistant` 協助解決」
  - 提升用戶在文檔化前的驗收意識，減少文檔與實際實作不符的風險
  - 強調 Technical Assistant 在問題解決中的支援角色

## [1.15.6] - sunnycore v1.15.6

### Changed
- 增強驗收任務配置安全性：在 `cutover.md` 的環境設置階段新增配置檔案保護提示
  - 新增說明：「必須讀取現有的 ".env" 檔案以避免覆寫現有配置」
  - 確保驗收流程中的環境設置不會意外覆蓋專案現有配置
  - 提升驗收任務的安全性與可靠性

## [1.15.5] - sunnycore v1.15.5

### Changed
- 簡化模板轉換規則：優化 `CLAUDE.md` 中的 YAML to Markdown 轉換規則編號
  - 移除第 1 項「YAML Front Matter」規則（該規則已不再適用於最小化模板設計）
  - 重新編號原本的規則 2-8 為 1-7，保持規則連續性
  - 提升模板使用指引的簡潔度與準確性

## [1.15.4] - sunnycore v1.15.4

### Changed
- 簡化模板使用指引：優化 `CLAUDE.md` 中的 YAML Front Matter 轉換說明
  - 移除冗餘說明：刪除「Preserve the `---` delimited front matter block at the start of the file」
  - 移除冗餘說明：刪除「Front matter contains metadata (not displayed in rendered Markdown body)」
  - 澄清格式定義：改為「Front matter contains metadata in markdown format」
  - 提升模板使用指引的清晰度與準確性

## [1.15.3] - sunnycore v1.15.3

### Changed
- 規範化產品管理命令參數：在 `sunnycore_pm.md` 中為 3 個命令新增必要的 requirements 參數
  - `*consult` 改為 `*consult {requirements}`：明確要求提供需求描述以進行流程諮詢
  - `*create-epic` 改為 `*create-epic {requirements}`：明確要求提供需求描述以創建 Epic
  - `*create-prd` 改為 `*create-prd {requirements}`：明確要求提供需求描述以創建 PRD
  - 提升命令使用的明確性，確保用戶在執行命令時提供必要的上下文信息

## [1.15.2] - sunnycore v1.15.2

### Changed
- 擴展角色命令描述：在所有 5 個角色命令文件中新增自訂命令執行說明
  - 新增說明：「Will execute custom commands base on user's input.」
  - 涵蓋文件：`sunnycore_architect.md`、`sunnycore_dev.md`、`sunnycore_pm.md`、`sunnycore_po.md`、`sunnycore_qa.md`
  - 提升角色命令文檔的功能描述完整性與使用者理解度

## [1.15.1] - sunnycore v1.15.1

### Fixed
- 修正總結任務文檔參考更新說明：更正 `conclude.md` 中的文檔參考處理邏輯
  - 第 7 步驟（Update Document References Phase）：明確說明「必須不編輯指向先前已歸檔文件的文檔參考（例如 "archive/1.14.4/xxx/yyy.md"）」
  - 原說明過於籠統，可能導致誤解為需要更新所有檔案參考
  - 新說明明確排除已歸檔文件的參考，避免錯誤修改歷史歸檔路徑
  - 提升總結任務執行的準確性與文檔歸檔的完整性

## [1.14.5] - sunnycore v1.14.5

### Changed
- 重構模板系統：將所有模板簡化為最小化框架結構，提升靈活性與 token 使用效率
  - 更新 `claude code/CLAUDE.md`：大幅擴展 `[Template-Usage-Guidelines]` 章節
    * 新增「Template Philosophy」說明：強調最小化框架設計理念（使用佔位符 `""`, `[]`, `{}`）
    * 新增「YAML to Markdown Conversion Rules」：8 條詳細轉換規則
      - YAML Front Matter 處理規則
      - Heading Level 轉換規則（h1-h4，避免 h5/h6）
      - Value Type 轉換規則（字串、巢狀物件、多行文字、數字/布林值）
      - List 轉換規則
      - Object Array 轉換規則
      - Empty Value 處理規則（關鍵：空值完全省略，僅顯示有內容的區塊）
      - Special Markers 處理規則
      - Formatting Best Practices
  - 更新 `claude code/templates/architecture-tmpl.yaml`：從詳細結構簡化為最小化框架
    * 移除冗長的註釋與範例說明
    * 所有欄位改為佔位符（空字串、空陣列、空物件）
    * 保留核心結構：executive-summary、technical-stack、system-architecture、api-documentation、requirements-traceability、architecture-decisions、cross-cutting-concerns、deployment、quality-attributes、architecture-diagram、source-references
  - 更新 `claude code/templates/completion-report-tmpl.yaml`：擴展專案完成報告結構
    * 新增欄位：project_duration、team_size
    * 擴展 development-summary：新增 objectives_partial、objectives_deferred
    * 新增區塊：delivery-metrics（計劃與實際功能數、工作量差異）
    * 擴展 quality-summary：新增 defect-metrics、review-scores
    * 新增區塊：technical-debt、risks-realized、team-performance、knowledge-transfer
  - 更新 `claude code/templates/cutover-report-tmpl.yaml`：擴展驗收報告結構
    * 新增欄位：version、pass_rate、setup_time、startup_time、performance
    * 新增區塊：functional-verification、non-functional-verification
    * 擴展 deployment-readiness：新增 monitoring_configured、backup_strategy_documented
    * 擴展 sign-off：新增 deployment_date
  - 更新 `claude code/templates/dev-notes-tmpl.yaml`：擴展開發筆記結構
    * 新增欄位：task_name、developer、start_date、completion_date、actual_duration
    * 重構區塊結構：technical-decisions、implementation-details、testing、quality-metrics、risks-and-maintenance
    * 新增區塊：deviations-from-plan、known-issues、technical-debt、documentation-updates、lessons-learned、next-steps、references
  - 更新 `claude code/templates/implementation-plan-tmpl.yaml`：重構 TDD 實作計劃結構
    * 新增欄位：plan_version、created_by、estimated_duration
    * 新增區塊：task-context（summary、requirements-mapping、architecture-context）
    * 重構 tdd-phases：統一 objective、test-cases、implementation-steps、files、dependencies、refactoring-targets、quality-improvements、checklist
    * 新增區塊：additional-details、risk-management、validation-checklist、notes
  - 更新 `claude code/templates/prd-tmpl.yaml`：簡化 PRD 模板結構
    * 所有陣列欄位改為空陣列佔位符
    * 移除詳細的範例結構說明
  - 更新 `claude code/templates/project-knowledge-tmpl.yaml`：擴展知識庫模板結構
    * 新增欄位：title、project_name、version
    * 新增區塊：design-patterns、architecture-insights、performance-optimizations、security-practices、testing-strategies、code-snippets、tools-and-libraries、process-improvements、metrics-and-kpis、team-learnings、external-resources
  - 更新 `claude code/templates/requirement-tmpl.yaml`：擴展需求文檔模板
    * 新增欄位：title、version、created_date、last_updated、status
    * 新增區塊：project-overview、user-stories、glossary、appendix
  - 更新 `claude code/templates/review-tmpl.yaml`：擴展審查報告模板
    * 新增區塊：compliance-check、code-review、security-review、performance-review、documentation-review
    * 擴展 findings、test-summary、source-references
  - 更新 `claude code/templates/tasks-tmpl.yaml`：擴展任務文檔模板
    * 新增欄位：title、version、created_date、last_updated、total_tasks、completed_tasks
    * 新增區塊：task-overview、infrastructure-tasks、documentation-tasks、milestones、progress-summary、notes
- 提升模板系統的一致性、靈活性與使用者體驗，減少 token 消耗同時保持結構清晰

## [1.14.4] - sunnycore v1.14.4

### Added
- 增強安裝腳本用戶體驗：新增即時進度條與智能並行下載優化（`scripts/install.py`）
  - 新增 `ProgressBar` 類別：提供即時進度條顯示
    * 顯示下載進度百分比與成功/失敗文件數
    * 顯示下載速度（檔/秒）、已用時間、預估剩餘時間
    * 自動格式化時間顯示（秒/分/小時）
  - 優化並行下載策略：智能調整並行數量
    * 預設值從固定 10 個改為自動調整（根據文件總數，上限 200）
    * 允許通過 `--max-workers` 參數手動限制並行數
    * 提升下載速度與資源利用效率
  - 改進使用者回饋：移除逐行文件下載提示，改用統一進度條顯示
  - 新增完成摘要：顯示總耗時與成功/失敗統計

### Changed
- 優化文檔化任務說明：擴展 `document-project.md` 中更新 CLAUDE.md 的範圍
  - 從「更新 Document Index 章節」擴展為「更新 Document Index 章節和任何與架構相關的章節」
  - 確保架構文檔更新時同步更新所有相關章節
  - 提升文檔化流程的完整性

## [1.14.3] - sunnycore v1.14.3

### Changed
- 優化 Technical Assistant 命令文檔結構：簡化 `sunnycore_assistant.md` 格式並增強輸入來源
  - 移除 `[Path-Variables]` 章節：減少冗餘內容，簡化文檔結構
  - 工具定義明確化：從引用 `CLAUDE.md` 改為直接列出 4 個核心工具（todo_write、sequentialthinking、claude-context、context7）
  - 新增輸入源：新增 `"{root}/docs/knowledge"` 知識庫目錄作為輸入，提供更好的上下文支援
  - 提升命令文檔的自包含性與可讀性

## [1.14.2] - sunnycore v1.14.2

### Added
- 增強角色命令文檔可讀性：在所有 6 個角色命令文件中新增 `[Description]` 章節
  - `sunnycore_architect.md`：「Full-stack architect, responsible for designing and maintaining the technical architecture of the project.」
  - `sunnycore_assistant.md`：「Technical assistant, responsible for problem diagnosis, bug fixing, technical consulting, and code optimization.」
  - `sunnycore_dev.md`：「Principal full-stack engineer, responsible for developing the project.」
  - `sunnycore_pm.md`：「Product manager, responsible for product planning, requirements analysis, and cross-functional coordination.」
  - `sunnycore_po.md`：「Product owner, responsible for business requirements analysis, project delivery acceptance, user experience evaluation, and stakeholder management.」
  - `sunnycore_qa.md`：「QA engineer, responsible for systematic quality assessment, test coverage, and architecture compliance.」
  - 提升命令文件的自我描述性，幫助用戶快速理解各角色定位
- 強化進度管理時間記錄要求：在 `progress-manager.md` 中新增第 7 條約束
  - 新增：「Must obtain the exact time by using terminal command」
  - 確保進度記錄包含準確的時間戳記，提升進度追蹤準確性

## [1.14.1] - sunnycore v1.14.1

### Fixed
- 修正文檔格式錯誤：統一章節標題與縮排格式
  - 更正 `claude code/agents/progress-manager.md`：將 `[DoD]` 改為 `## [DoD]`，統一章節標題格式
  - 更正 `claude code/commands/sunnycore_po.md`：修正路徑變數縮排格式（兩處缺少空格）
  - 提升文檔格式一致性與可讀性

## [1.14.0] - sunnycore v1.14.0

### Added
- 新增流程諮詢功能：新增 `*consult` 指令幫助用戶選擇最適合的開發流程
  - 新增 `claude code/tasks/consult.md`：定義流程諮詢任務
    * 自動偵測專案類型（Greenfield/Brownfield）
    * 智能分析需求範圍與影響
    * 提供精準的流程建議（完整開發流程 vs PRD 流程）
    * 基於現有架構分析需求是否需要架構變更
  - 更新 `claude code/commands/sunnycore_pm.md`：在可用命令列表中新增 `*consult`
  - 更新主 `README.md`：新增「快速開始」章節
    * 引導用戶使用 `/sunnycore_pm *consult` 開始任何新需求
    * 說明兩種主要開發流程的適用場景
  - 更新 `claude code/README.md`：新增「如何選擇開發流程？」完整指引
    * 新增流程選擇對照表（需求特徵 vs 建議流程）
    * 詳細說明 *consult 指令的使用步驟與優勢
    * 明確區分完整開發流程與 PRD 流程的適用場景
  - 提升用戶體驗：節省決策時間，提供自動化流程建議

## [1.13.16] - sunnycore v1.13.16

### Changed
- 統一文檔格式：將所有任務與命令文件的章節標題改為 Markdown heading 格式
  - 更新 `claude code/CLAUDE.md`：所有 `[章節名稱]` 改為 `## [章節名稱]`
    * 涵蓋章節：[Constraints]、[Tool-Guidelines]、[Template-Usage-Guidelines]、[Summary-Instructions]
  - 更新 `claude code/agents/progress-manager.md`：所有章節標題改為 heading 格式
    * 涵蓋章節：[Input]、[Output]、[Role]、[Skills]、[Constraints]、[Classification-Guidelines]、[Output-Guidelines]、[Example]
  - 更新 6 個命令文件：統一章節標題格式為 Markdown heading
    * `sunnycore_architect.md`：[Path-Variables]、[Input]、[Output]、[Role]、[Skills]、[Constraints]、[Custom-Commands]、[Project-Summary-Guidelines]、[Knowledge-Management_Guidelines]、[Architecture-Management-Guidelines]、[DoD]
    * `sunnycore_assistant.md`：[Path-Variables]、[Input]、[Output]、[Role]、[Skills]、[Tools]、[Constraints]、[DoD]
    * `sunnycore_dev.md`：[Path-Variables]、[Input]、[Output]、[Role]、[Skills]、[Constraints]、[Custom-Commands]、[Development-Guidelines]、[DoD]
    * `sunnycore_pm.md`：[Path-Variables]、[Input]、[Output]、[Role]、[Skills]、[Constraints]、[Custom-Commands]、[Requirements-Analysis-Guidelines]、[Architecture-Design-Guidelines]、[Task-Management-Guidelines]、[DoD]
    * `sunnycore_po.md`：[Path-Variables]、[Input]、[Output]、[Role]、[Skills]、[Constraints]、[Custom-Commands]、[Acceptance-Guidelines]、[DoD]
    * `sunnycore_qa.md`：[Path-Variables]、[Input]、[Output]、[Role]、[Skills]、[Constraints]、[Custom-Commands]、[Domain-Specific-Review-Guidelines]、[DoD]
  - 更新 25 個任務文件：統一章節標題格式為 Markdown heading
    * 涵蓋任務：brownfield-tasks、conclude、create-architecture、create-brownfield-architecture、create-epic、create-prd、create-requirements、curate-knowledge、cutover、develop-prd、develop-tasks、document-project、fix-acceptance-issues、help、init、plan-tasks、review
    * 涵蓋章節：[Input]、[Output]、[Constraints]、[Tools]、[Steps]、[DoD]、[Error-Handling]、[Example]、[Rules] 等
  - 優化 `sunnycore_qa.md` 中的領域審查指引格式：將所有子章節改為 heading 格式（Overview、Unified Scoring System、Score Calculation、Decision Rules、Risk Assessment Criteria、Common Issues & Anti-patterns）
  - 提升文檔可讀性與 Markdown 渲染效果

## [1.13.15] - sunnycore v1.13.15

### Changed
- 優化 PRD 開發任務的工具使用說明：擴展 claude-context (MCP) 工具的使用描述
  - 更新 `claude code/tasks/develop-prd.md`：改進準備階段的 claude-context 工具說明
    * 從「搜尋程式碼庫以找到 PRD 相關實作」改為「搜尋程式碼庫以準備 PRD 實作 - 理解現有程式碼結構、相關模組、依賴關係和實作模式」
    * 提供更具體的工具使用目的與範圍說明
  - 提升 PRD 開發流程的清晰度與工具使用指引

## [1.13.14] - sunnycore v1.13.14

### Changed
- 精簡核心指引文檔：移除 `CLAUDE.md` 中的 Wrap-Up-Gatekeeper 詳細指引章節
  - 移除約束條款 10.3-10.8：驗證前置檢查、最終檢查、工具規則遵循、中斷處理、一致性檢查、優先級擴展
  - 移除 `[Wrap-Up-Gatekeeper_Guidelines]` 完整章節：ToDo 狀態模型、任務循環、驗證證據、中斷處理、文檔產出等詳細說明
  - 保留核心約束條款 10.1-10.2：禁止在 ToDo 未完成時結束、合法結束狀態定義
  - 提升文檔簡潔度，減少冗餘內容

## [1.13.13] - sunnycore v1.13.13

### Changed
- 重構 PRD 開發任務的 TDD 流程說明：將迭代式 TDD 改為批次式 RED → GREEN → REFACTOR 流程
  - 更新 `claude code/tasks/develop-prd.md`：調整 TDD 開發階段（步驟 2）為批次執行模式
    * RED 階段：先為所有需求撰寫測試案例（單元測試、整合測試），確認測試如預期失敗
    * GREEN 階段：依依賴順序實作所有功能，確保所有測試通過
    * REFACTOR 階段：對所有實作套用程式碼品質標準（SOLID、DRY），重新執行測試驗證重構
  - 優化工具使用說明：todo_write 從「追蹤實作進度」改為「追蹤 TDD 階段進度」，sequentialthinking 從「推理實作策略」改為「推理需求實作策略」
  - 提升 TDD 流程的清晰度與執行效率

## [1.13.12] - sunnycore v1.13.12

### Added
- 新增任務完成守門機制：在 `CLAUDE.md` 中新增 `[Wrap-Up-Gatekeeper]` 約束與指引
  - 新增約束第 10 條：禁止在 ToDo 未完成時輸出「完成」、「總結」等結束語
  - 新增三種合法結束狀態：completed（全部完成）、blocked（外部依賴）、external-interrupt（平台限制）
  - 新增完成前驗證機制：任何標記為 completed 的 ToDo 必須先執行對應驗證步驟並附上證據摘要
  - 新增最終檢查機制：輸出總結前必須重新檢查 ToDo 狀態，若有未完成項目則立即返回執行
  - 新增中斷處理流程：平台限制時生成 `docs/RESUME_PLAN.md` 並提供可立即執行的恢復指令
  - 新增一致性檢查：禁止輸出與實際狀態不符的陳述（如「大部分測試完成」但實際未完成）
- 新增 `[Wrap-Up-Gatekeeper_Guidelines]` 章節：定義 ToDo 狀態模型、任務循環、驗證證據、中斷處理、文檔產出規範

### Changed
- 重構路徑引用系統：在所有命令與任務文件中引入可重用路徑變數，提升可維護性
  - 新增 `[Path-Variables]` 章節至 6 個命令文件（sunnycore_architect.md、sunnycore_assistant.md、sunnycore_dev.md、sunnycore_pm.md、sunnycore_po.md、sunnycore_qa.md）
    * 定義通用路徑變數：{C}（CLAUDE.md）、{T}（tasks/）
    * 定義文檔路徑變數：{REQ}（requirements/）、{ARCH}（architecture/）、{PRD}（PRD.md）、{EPIC}（epic.md）
    * 定義模板與腳本變數：{TMPL}（templates/）、{SCRIPTS}（scripts/）
    * 定義執行產出變數：{PLAN}（implementation-plan/）、{DEVNOTES}（dev-notes/）、{REVIEW}（review-results/）
    * 定義知識管理變數：{KNOWLEDGE}（knowledge/）、{PROGRESS}（progress.md）
    * 定義交付產出變數：{CUTOVER}（cutover.md）、{ARCHIVE}（archive/）、{LOCK}（sunnycore.lock）
  - 更新 25 個任務文件的路徑引用：將硬編碼路徑（如 `{root}/docs/requirements/*.md`）改為路徑變數（如 `{REQ}/*.md`）
    * 涵蓋任務：brownfield-tasks、conclude、create-architecture、create-brownfield-architecture、create-epic、create-prd、create-requirements、curate-knowledge、cutover、develop-prd、develop-tasks、document-project、fix-acceptance-issues、init、plan-tasks、review
  - 優化 `conclude.md` 任務流程：明確區分 Traditional 與 PRD 工作流程的歸檔邏輯（兩者皆保留 architecture/、knowledge/、completion-report.md）
- 優化 `CLAUDE.md` 文檔格式與語言風格：提升專業性與可讀性
  - 統一標點符號使用：句號改為句點、冒號後空格統一、列表項結尾加句點
  - 統一術語翻譯：「perform」→「conduct」、「Retrieve」→「retrieve the」、「Obtain」→「obtain」
  - 統一章節標題格式：使用 em dash（—）取代連字符（-）
  - 優化工具描述：改進 Tool-Guidelines 中各工具的功能說明語句
- 優化 `README.md` 流程圖與步驟說明：新增 conclude 任務至驗收與總結階段
  - 階段三流程更新：新增步驟 6（`/sunnycore_po *conclude`）- 總結文檔並歸檔
  - Greenfield 流程：總步驟數從 5 步增加至 6 步
  - 流程圖更新：cutover → document-project → conclude → Done
  - 流程對比表更新：PRD 流程總步驟數從 5 步更新為 6 步

## [1.13.11] - sunnycore v1.13.11

### Changed
- 重構角色命令文檔結構：優化 5 個角色命令文件的路徑引用與命令描述格式
  - 新增 `[Path-Variables]` 章節：定義可重用的路徑變數 {C} 和 {T}
    * {C} = {root}/sunnycore/CLAUDE.md
    * {T} = {root}/sunnycore/tasks
  - 簡化 `[Input]` 描述：從詳細路徑改為使用路徑變數引用
    * 第 1 項：統一為「用戶指令輸入與任務文檔」
    * 第 2 項：從完整路徑改為 {C} 變數引用
  - 重構 `[Custom-Commands]` 格式：從逐一列舉命令改為模式描述 + 可用命令列表
    * 新增命令模式說明：`Pattern: *{command} → Read and execute: {T}/{command}.md`
    * 改用 `Available commands` 列表取代重複的命令路徑描述
  - 涵蓋文件：
    * `claude code/commands/sunnycore_architect.md`：4 個可用命令
    * `claude code/commands/sunnycore_dev.md`：6 個可用命令
    * `claude code/commands/sunnycore_pm.md`：5 個可用命令
    * `claude code/commands/sunnycore_po.md`：4 個可用命令
    * `claude code/commands/sunnycore_qa.md`：2 個可用命令
  - 提升命令文檔的可維護性與一致性，減少冗餘內容

## [1.13.10] - sunnycore v1.13.10

### Changed
- 重構 PRD 工作流程：從 PRD 創建階段移除任務生成職責
  - 更新 `claude code/tasks/create-prd.md`：移除「任務生成階段」（原步驟 4）
    * 步驟重新編號：原步驟 5「PRD 整合階段」→ 步驟 4、原步驟 6「最終化階段」→ 步驟 5
    * 整合階段調整：「識別任務依賴」→「識別需求依賴」
    * 移除任務相關的錯誤處理規則：「任務生成覆蓋率不足」、「用戶拒絕最終 PRD」中的任務相關描述
    * DoD 更新：移除「功能級任務已生成」、「任務依賴已識別」、「所有任務可驗證且以結果為導向」等檢查項
    * 工具使用說明更新：todo_write 從「創建任務清單」改為「創建待辦清單」
  - 更新 `claude code/tasks/develop-prd.md`：調整為以需求為中心的實作流程
    * 準備階段：從「提取所有任務」改為「理解需求和架構」，新增 TDD 實作策略規劃
    * 迭代 TDD 開發階段：「任務的驗收標準」→「需求的驗收標準」，「任務完成」→「實作完成」
    * 整合測試階段：「所有實作任務的測試套件」→「所有實作的測試套件」，「任務間的整合點」→「實作間的整合點」
    * 文檔階段：「所有任務的實作摘要」→「所有實作的摘要」
    * DoD 更新：「PRD 已讀取且所有任務已提取」→「PRD 已讀取且所有需求已提取」，「待辦清單已創建且任務依賴序排列」→「待辦清單已創建且需求依賴序排列」
  - 更新 `claude code/templates/prd-tmpl.yaml`：移除整個 tasks 區塊
    * 刪除功能級任務模板結構（id、name、requirements、architecture-refs、acceptance-hint、dependencies 欄位）
    * 精簡模板結構，專注於需求與架構定義
- 優化 PRD 定位：PRD 專注於「產品需求文檔」職責，任務拆分交由後續的 plan-tasks 階段處理

## [1.13.9] - sunnycore v1.13.9

### Changed
- 重構角色職責分配：將任務規劃職責從 PM 轉移至 Developer
  - 更新 `claude code/README.md`：修正命令參考與流程圖
    * 步驟 5/6：`/sunnycore_pm *plan-tasks` → `/sunnycore_dev *plan-tasks`
    * 角色職責表：Developer 新增「任務規劃」職責、PM 移除「任務規劃」職責
  - 更新 `claude code/index.json`：調整任務與代理映射關係
    * taskToAgents：plan-tasks 從 `["pm", "dev"]` 改為 `["dev"]`
    * agentToTasks：pm 移除 plan-tasks 任務
  - 優化角色定位：Developer 負責技術實作與任務拆分、PM 專注於產品需求管理
- 擴展 TDD 開發指引：在 `sunnycore_dev.md` 中新增詳細的 TDD 實踐準則
  - 新增 TDD 定義說明：「測試驅動開發是先寫測試再寫實作代碼的軟件開發方法論」
  - 擴展 RED 階段說明：強調測試應定義預期行為和 API 契約、目標是看到測試因正確原因失敗
  - 擴展 GREEN 階段說明：強調實作最簡單代碼使測試通過、避免過度工程化
  - 擴展 REFACTOR 階段說明：
    * 新增「整合真實外部 API、資料庫或服務」要求
    * 新增「替換 mock 實作為實際整合」指引
    * 新增「效能優化與架構改進」說明
  - 新增 TDD 迭代週期說明：「每次迭代應該小而專注，逐步構建完整功能」
- 優化任務文檔清晰度：簡化 4 個任務文檔的 TDD 流程描述
  - `create-prd.md`：新增任務粒度說明
    * 強調任務為功能規格（WHAT），非技術實作步驟（HOW）
    * 驗收提示應為業務導向，非測試導向
  - `develop-prd.md`：簡化 TDD 開發階段流程
    * 移除詳細的 2.1-2.4 子步驟（RED/Fix/GREEN/REFACTOR 路徑）
    * 改為引用 Development-Guidelines 中的 TDD 實踐準則
    * 新增準備階段的 TDD 實作策略規劃說明
  - `develop-tasks.md`：簡化 RED、GREEN、REFACTOR 階段描述
    * 移除詳細的條件分支子步驟（2.1/2.2、3.1/3.2、4.1/4.2）
    * 保留核心流程說明與架構映射要求
  - `plan-tasks.md`：優化約束與步驟說明
    * 約束第 5 條：改為引用 Development-Guidelines 中的 TDD 方法論
    * 簡化 RED、GREEN、REFACTOR 階段的規劃步驟描述

## [1.13.8] - sunnycore v1.13.8

### Changed
- 重構約束管理機制：整合分散在各文件中的約束條款到 `CLAUDE.md` 頂層
  - 更新 `claude code/CLAUDE.md`：將約束條款提升至 [Constraints] 章節
    * 建立三級優先級機制：CLAUDE.md[Constraints] > commands[Constraints] > tasks[Constraints]
    * 整合通用約束：自訂指令執行、任務步驟遵循、輸入文件讀取、工具使用方法、todo 完成、DoD 驗證
    * 新增指引參考約束：讀取並遵循相關指引章節（如 [xxx-Guidelines]）
  - 簡化 6 個角色命令文件的約束條款：
    * `sunnycore_architect.md`、`sunnycore_dev.md`、`sunnycore_pm.md`、`sunnycore_po.md`：約束從 4 條簡化為 1 條（「必須執行自訂指令」）
    * `sunnycore_assistant.md`：約束從 5 條簡化為 3 條（移除重複的「遵循 CLAUDE.md 指引」和「不明確時請求澄清」）
    * `sunnycore_qa.md`：約束從 4 條簡化為 1 條（「必須執行自訂指令」）
  - 優化 14 個任務文件的 DoD 驗證流程：
    * 移除重複的「DoD 驗證階段」步驟描述
    * 移除「確認所有 todo 項目完成」的冗餘檢查項
    * 涵蓋任務：brownfield-tasks、conclude、create-architecture、create-brownfield-architecture、create-epic、create-prd、create-requirements、curate-knowledge、cutover、develop-prd、develop-tasks、document-project、fix-acceptance-issues、plan-tasks、review
  - 提升約束管理的系統性與可維護性
- 簡化安裝腳本下載清單：移除 `scripts/install.py` 中的 config.yaml 下載項目
  - 原因：config.yaml 已在先前版本中移除
  - 保持下載清單與實際文件結構一致

## [1.13.7] - sunnycore v1.13.7

### Changed
- 精簡文檔化任務流程：優化 `document-project.md` 的分析階段步驟
  - 移除「識別計畫架構與實際實作之間的差異」步驟
  - 流程更專注於直接從程式碼、開發筆記、審查報告和知識庫生成架構文檔
  - 提升文檔化任務的執行效率與清晰度

## [1.13.6] - sunnycore v1.13.6

### Changed
- 重構文檔化任務流程：優化 `document-project.md` 架構文檔生成與拆分機制
  - 新增統一架構文檔生成流程：先產生統一的 `{root}/docs/architecture.md`，再執行拆分
  - 新增 Cleanup and Sharding Phase（步驟 3）：刪除舊有架構文檔後執行拆分腳本
  - 調整輸出說明：明確區分統一架構文檔（臨時）與拆分後的架構文檔
  - 優化 Integration Phase 說明：強調統一文檔的完整性與來源參考
  - 擴展輸入源：新增知識庫 (knowledge base) 作為文檔化參考
  - 擴展 DoD 檢查項目：新增舊文檔刪除、拆分腳本執行、原始文檔刪除等檢查點
  - 提升文檔化流程的系統性與可追溯性
- 優化架構模板結構：重構 `architecture-tmpl.yaml` 專案元資料格式
  - 將 project-name、version、last-updated、status 四個欄位整合進 project-metadata 區塊
  - 提升模板結構的層次性與可讀性

### Removed
- 移除配置檔案：刪除 `claude code/config.yaml` 以簡化專案結構
  - 移除 orchestrator-subagent-list 配置
  - 移除 dev-subagent-list 配置（11 個 subagent 定義）
  - 移除 qa-subagent-list 配置（6 個 subagent 定義）
  - 簡化專案維護成本

## [1.13.5] - sunnycore v1.13.5

### Changed
- 優化 claude-context (MCP) 工具使用指引：在 `CLAUDE.md` 中新增工具使用註記
  - 新增說明：「Always use search_code directly for codebase search」
  - 新增說明：「Only use index_codebase when the codebase has not been indexed yet」
  - 新增說明：「Check indexing status first before attempting to index」
  - 提升工具使用的正確性與效率，避免重複索引

## [1.13.4] - sunnycore v1.13.4

### Changed
- 優化任務文檔流程描述：統一 14 個任務文檔的條件分支格式與段落結構
  - 統一條件分支語法：「if X then Y, else Z」→「if X then proceed to Y, else proceed to Z」
  - 優化段落結構：改進縮排與空行使用，提升可讀性
  - 精簡冗餘內容：移除重複描述，合併相關說明
  - 改進步驟說明：
    * brownfield-tasks.md：優化測試執行描述與修復流程
    * conclude.md：合併資訊提取與映射階段，優化步驟編號
    * create-architecture.md：拆分架構設計步驟說明
    * create-prd.md：統一條件分支格式，調整任務生成順序
    * create-requirements.md：優化最終化階段的成功/失敗路徑
    * curate-knowledge.md：重新命名知識庫設計階段，優化步驟順序
    * cutover.md：優化階段順序與專案執行驗證
    * develop-prd.md：重構 TDD 開發階段流程結構
    * develop-tasks.md：統一條件分支格式
    * document-project.md：優化架構文檔更新的條件分支
    * fix-acceptance-issues.md：調整根因分析階段順序
    * init.md：精簡環境設置與文檔生成階段
    * plan-tasks.md：合併複雜度評估說明
    * review.md：統一條件分支格式與審查路徑命名
  - 提升任務文檔的一致性、可讀性與專業性

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
