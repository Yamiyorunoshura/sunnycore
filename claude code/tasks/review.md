[輸入]
  1. {root}/docs/dev-notes/{task_id}-dev-notes.md --開發筆記
  2. {root}/docs/implementation-plan/{task_id}-plan.md --實作計畫
  3. {root}/sunnycore/templates/review-tmpl.yaml --審查模板

[輸出]
  1. {root}/docs/review-results/{task_id}-review.md
  2. {root}/docs/epic.md

[約束]
  1. 必須執行 develop-tasks 任務階段創建的所有測試，並驗證測試結果與實作計畫對齊
  2. 必須驗證所有正式程式碼嚴格遵循實作計畫規格與驗收標準；任何偏離處需明確記錄並說明理由
  3. 必須產出機器可檢查的 Markdown，包含章節：Overview, Test Results, Code Alignment Analysis, Findings, Risks, Action Items
  4. 必須使用檔案路徑、行範圍或錨點（若可用）交叉參照計畫/程式碼/筆記
  5. 必須記錄驗收決策與理由：Accept / Accept with changes / Reject

[工具]
  1. **sequentialthinking (MCP)** - 結構化推理工具，用於複雜邏輯分析
    - [步驟1:推理任務領域識別與評分標準選擇;步驟2:推理領域特定評分邏輯與對齊分析;步驟3:推理筆記與實作對齊關係;步驟4:推理問題優先級、風險評估與決策理由]
  2. **todo_write** - 任務追蹤工具，用於管理待辦清單
    - [步驟1:創建待辦清單;步驟2-4:執行追蹤]
  3. **claude-context (MCP)** - 程式碼庫語義搜尋與索引工具，用於大型文件分段處理
    - [步驟1:分段處理大型計畫文件;步驟2:分段處理大型程式碼文件]

[工具指引]
  1. **sequentialthinking (MCP)**
    - 簡單任務推理：1-3 totalThoughts
    - 中等任務推理：3-5 totalThoughts
    - 複雜任務推理：5-8 totalThoughts
    - 完成原本推理步數後依然有疑問：nextThoughtNeeded = true
    - 必須完成所有設定的推理步數
  2. **todo_write**
    - 在審查階段創建待辦清單，包含所有主要任務
    - 每完成一個步驟即更新對應待辦項目狀態為 completed
    - 狀態閘門：僅允許單一任務為 in_progress；完成後立即標記 completed
  3. **claude-context (MCP)**
    - 使用場景：當計畫文件過大需要分段處理時
    - 可用於分段讀取與理解複雜的計畫文件

[步驟]
  1. 審查計劃階段
    - 閱讀實作計畫並理解其內容
    - **識別任務領域**：根據實作計畫內容判斷任務屬於哪個領域（後端/前端/API/資料庫/DevOps/測試/文檔/通用）
    - 識別驗證方法與成功標準
    - 創建 todo list 以追蹤後續審查任務

  2. 審查程式碼階段
    - 閱讀所有正式程式碼並理解其實作
    - **應用領域特定審查標準**：根據步驟1識別的任務領域，依照該領域的評分維度進行審查
    - 執行所有測試並記錄通過/失敗狀態與計畫對齊情況
    - 執行整合測試以確認實作不影響原有程式碼
    - 驗證測試覆蓋率
    - 驗證程式碼嚴格對齊架構/設計及驗收標準
    - **記錄領域特定的評分**：為每個領域維度評分並計算整體分數 

  3. 審查開發筆記階段
    - 閱讀開發筆記並理解其內容
    - 檢查筆記與實作之間的對齊情況

  4. 產出結果階段
    - 使用模板創建審查結果，包含測試執行摘要
    - 記錄測試結果與通過/失敗狀態及計畫對齊情況；分析程式碼對齊情況與特定參照
    - 儲存至 {root}/docs/review-results/{task_id}-review.md；若檔案存在，則更新
    - 如果審查通過，則更新 epic.md 以反映項目進展
    - 逐項檢查所有 DoD 項目是否已滿足
    - 確認所有待辦項目已完成

[DoD]
  - [ ] 已識別任務領域並應用對應的領域特定審查標準
  - [ ] 已根據領域特定的評分維度進行評分
  - [ ] 已執行所有測試並記錄結果
  - [ ] 已執行整合測試確認實作不影響原有程式碼並紀錄結果
  - [ ] 已驗證測試結果與計畫對齊
  - [ ] 程式碼對齊分析已完成，包含對計畫偏離的特定參照
  - [ ] 所有必要章節已呈現：Overview, Test Results, Code Alignment Analysis, Findings, Risks, Action Items
  - [ ] 測試失敗與計畫不對齊情況已清楚識別並優先化
  - [ ] 已記錄驗收決策與基於測試結果及計畫遵循的理由
  - [ ] 所有待辦項目已完成
