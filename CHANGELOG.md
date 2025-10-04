# Claude code v1.7.18

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

# Claude code v1.7.17

## Changed
- 簡化指令文檔格式：將所有 command 檔案（dev、pm、po、qa）從複雜的 XML 結構簡化為清晰的中文 Markdown 格式
- 移除冗餘配置：刪除 `CLAUDE.md` 大型配置文件，將核心規則精簡整合至各指令檔案中
- 優化指引內容：保留核心指引（任務管理、專案總結、知識管理、架構管理、評分標準），移除過度複雜的結構化標籤

## Removed
- `claude code/CLAUDE.md` - 560 行的大型配置文件，內容已精簡整合至各指令檔案

# Claude code v1.7.16

## Changed
- 統一任務提示詞格式：將 `develop-tasks`、`help`、`review` 從 XML 格式改為 Markdown 格式
- 強化任務提示詞結構：在 `develop-tasks` 和 `review` 中新增工具指引、DoD 檢查清單等章節以提升執行品質
- 優化 README：重構 Greenfield/Brownfield 流程說明，採用結構化表格與 Mermaid 流程圖，增強可讀性與視覺化呈現

# Claude code v1.7.15

## Changed
- 統一核心任務提示詞格式：將 `create-architecture`、`create-brownfield-architecture`、`create-requirements`、`create-tasks`、`plan-tasks` 從 XML 格式改為 Markdown 格式
- 強化工作流程結構：新增工具指引、DoD 檢查清單、異常處理等章節以提升任務執行品質
- 新增 concluded-architecture-tmpl 模板並關聯至 document-project 任務

# Claude code v1.7.14

## Changed
- 統一任務提示詞格式：將`brownfield-tasks`、`conclude`、`curate-knowledge`、`document-project`從XML格式改為Markdown格式
- 更新審查報告：優化`brownfield-tasks`、`conclude`、`curate-knowledge`、`document-project`、`prompt-reviewer`的審查報告結構與評分機制

# Claude code v1.7.13

## Changed
- 修正README中安裝腳本名稱為`scripts/sunnycore.sh`
- 優化`brownfield-tasks`提示詞，使其更符合實際需求

# Claude code v1.7.11

## Added
- README：新增以 curl 一行指令執行 `scripts/sunnycore.sh` 的安裝教學

## Changed
- README：將安裝腳本名稱由 `sunnycore.command` 更正為 `scripts/sunnycore.sh`