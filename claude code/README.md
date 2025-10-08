# 開發流程

## 🤔 如何選擇開發流程？

> **不確定用哪個流程？使用 `/sunnycore_pm *consult` 讓 AI 為您分析和建議！**

### 📊 流程選擇指引

| 需求特徵 | 建議流程 | 命令 |
|---------|---------|------|
| 🆕 新增系統組件或模塊 | 完整開發流程 | `*create-requirements` |
| 🏗️ 改變核心架構模式 | 完整開發流程 | `*create-requirements` |
| 🔧 新增技術棧或框架 | 完整開發流程 | `*create-requirements` |
| 🔌 新增外部整合或服務 | 完整開發流程 | `*create-requirements` |
| 📦 修改組件邊界或職責 | 完整開發流程 | `*create-requirements` |
| 🛡️ 重大橫切關注點變更 | 完整開發流程 | `*create-requirements` |
| ✏️ 現有組件內的修改 | PRD 流程 | `*create-prd` |
| ✨ 使用現有架構的功能增強 | PRD 流程 | `*create-prd` |
| 🐛 Bug 修復或技術改進 | PRD 流程 | `*create-prd` |
| 🎨 UI/UX 變更（無後端架構變更） | PRD 流程 | `*create-prd` |
| 🔍 小到中型範圍（1-5 個任務） | PRD 流程 | `*create-prd` |

### 🎯 使用 *consult 指令

**步驟：**
1. 執行 `/sunnycore_pm *consult`
2. 描述您的需求
3. AI 會自動分析現有架構（如果是 Brownfield 專案）
4. 獲得明確的流程建議和下一步指令

**優勢：**
- ✅ 自動檢測專案類型（Greenfield/Brownfield）
- ✅ 智能分析需求範圍和影響
- ✅ 提供精準的流程建議
- ✅ 節省決策時間

---

## 🛠️ 技術支援流程（新增）

> 適用於問題解答、Bug 修復、程式碼優化等日常技術支援

### 📋 使用方式

| 步驟 | 命令 | 說明 |
|------|------|------|
| 1 | `/sunnycore_assistant` | 描述您的問題或需要修復的 bug |
| 2 | 自動執行 | Assistant 分析問題並提供解決方案 |
| 3 | 自動執行 | Progress Manager 記錄重要進度和知識 |

**特點：**
- ✅ **快速響應**：即時問題解答和技術支援
- ✅ **智能記錄**：自動分類並記錄重要信息（critical/important）
- ✅ **知識累積**：Bug 修復和重要經驗自動歸檔
- ✅ **適用場景**：問題診斷、Bug 修復、程式碼優化、技術諮詢

### 📊 進度記錄說明

**progress.md 格式：**
```
{YYYY-MM-DD}:{HH:MM}: {動作描述} [{重要性}]
```

**知識庫組織：**
- `docs/progress.md` - 僅記錄 critical 和 important 級別的進度
- `docs/knowledge/*.md` - 按主題分類的 bug 修復和最佳實踐

---

## 🚀 PRD 流程（推薦用於小型變更）

> 適用於小型變更和快速迭代，將需求、架構、任務整合在單一 PRD 文檔中

### 📋 完整流程

| 步驟 | 命令 | 說明 |
|------|------|------|
| 1 | `/sunnycore_architect *document-project` | （可選）若為 Brownfield 專案，先更新架構文檔 |
| 2 | `/sunnycore_pm *create-prd` | 創建 PRD（產品需求文檔），包含需求、架構、任務 |
| 2.5 | `/sunnycore_po *validate-design prd` | （可選）驗證 PRD 內部一致性和與現有架構的對齊 |
| 3 | `/sunnycore_dev *develop-prd` | 基於 PRD 一次性完成所有開發任務 |
| 4 | `/sunnycore_po *cutover` | 項目驗收 |
| 5 | `/sunnycore_architect *document-project` | 更新專案架構文檔（建議先親身驗收項目，如發現問題可使用 `/sunnycore_assistant` 協助解決） |
| 6 | `/sunnycore_po *conclude` | 總結文檔並歸檔 |

**特點：**
- ✅ **簡化流程**：合併需求、架構、任務為單一文檔
- ✅ **快速迭代**：一次性完成所有 PRD 任務
- ✅ **自動判斷**：自動識別 Greenfield/Brownfield 專案類型
- ✅ **適用場景**：小型功能開發、Bug 修復、技術改進

### 🔄 流程圖

```mermaid
flowchart TD
    Start([開始 PRD 流程]) --> A0
    
    subgraph Phase1 ["📋 PRD 創建階段"]
        A0["1️⃣ /sunnycore_architect<br/>*document-project<br/>📖 更新專案文件（可選）"]
        A1["2️⃣ /sunnycore_pm<br/>*create-prd<br/>📝 創建 PRD"]
        A0 -.->|"Brownfield"| A1
        Start -.->|"Greenfield"| A1
    end
    
    subgraph Phase2 ["💻 開發階段"]
        B1["3️⃣ /sunnycore_dev<br/>*develop-prd<br/>⚙️ 完成所有開發任務"]
    end
    
    subgraph Phase3 ["📊 驗收與總結階段"]
        C0["4️⃣ /sunnycore_po<br/>*cutover<br/>✅ 項目驗收"]
        C1["5️⃣ /sunnycore_architect<br/>*document-project<br/>📖 更新專案文件"]
        C2["6️⃣ /sunnycore_po<br/>*conclude<br/>📋 總結文檔並歸檔"]
    end
    
    D1{"✅ Cutover<br/>通過?"}
    R1["🔧 /sunnycore_dev<br/>*fix-acceptance-issues<br/>修復問題"]
    
    Done([✨ 完成])
    
    A1 --> B1
    B1 --> C0
    C0 --> D1
    D1 -->|"❌ 否"| R1
    R1 --> C0
    D1 -->|"✅ 是"| C1
    C1 --> C2
    C2 --> Done
    
    style Start fill:#e1f5e1
    style Done fill:#e1f5e1
    style D1 fill:#fff4e6
    style R1 fill:#ffe6e6
    style Phase1 fill:#f0f8ff
    style Phase2 fill:#f5f0ff
    style Phase3 fill:#fff0f5
```

---

## 🌱 Greenfield 專案流程

> 適用於從零開始的新專案開發

### 📋 階段一：需求分析與計劃

| 步驟 | 命令 | 說明 |
|------|------|------|
| 1 | `/sunnycore_pm *create-requirements` | 互動式創建需求文檔 |
| 2 | `/sunnycore_architect *create-architecture` | 互動式創建架構文檔 |
| 3 | `/sunnycore_pm *create-epic` | 互動式創建任務文檔 |
| 4 | `/sunnycore_dev *create-plan` | 為所有任務創建實作計劃 |
| 5 | `/sunnycore_po *validate-design full` | （可選）驗證需求、架構、任務、計劃之間的完整一致性 |

### 💻 階段二：開發迭代

| 步驟 | 命令 | 說明 |
|------|------|------|
| 6 | `/sunnycore_dev *init` | 初始化開發環境與專案文檔 |
| 7 | `/sunnycore_dev *develop-plan {task_id}` | 基於計劃開發特定 task |
| 8 | `/sunnycore_qa *review {task_id}` | 審查特定 task 的文檔 |

**流程控制：**
- ✅ **Review 通過**：檢查是否還有其他任務
  - 有任務 → 回到步驟 7
  - 無任務 → 進入階段三
- ❌ **Review 未通過**：使用 `/sunnycore_dev *brownfield-tasks {task_id}` 進行重開發，回到步驟 7

### 📊 階段三：驗收與總結

| 步驟 | 命令 | 說明 |
|------|------|------|
| 9 | `/sunnycore_po *cutover` | 項目驗收 |
| 10 | `/sunnycore_architect *document-project` | 產出專案架構文件（建議先親身驗收項目，如發現問題可使用 `/sunnycore_assistant` 協助解決） |
| 11 | `/sunnycore_architect *curate-knowledge` | 整理知識文檔 |
| 12 | `/sunnycore_po *conclude` | 總結文檔 |

**流程控制：**
- ✅ **Cutover 通過**：進入總結流程（步驟 10）
- ❌ **Cutover 未通過**：使用 `/sunnycore_dev *fix-acceptance-issues` 進行修復，回到步驟 9

## ⚙️ 配置說明

### MCP 伺服器配置

本專案使用 Model Context Protocol (MCP) 伺服器提供增強功能。配置文件位於 `mcp.json`。

**必要步驟：配置 API Keys**

在使用前，請先在 `mcp.json` 中填入您自己的 API keys：

1. **Context7** - 需要填入 `CONTEXT7_API_KEY`
2. **Claude Context** - 需要填入以下環境變數：
   - `EMBEDDING_MODEL`: 嵌入模型名稱
   - `OPENAI_API_KEY`: OpenAI API key
   - `OPENAI_BASE_URL`: OpenAI API 基礎 URL
   - `MILVUS_TOKEN`: Milvus 向量資料庫 token

**配置範例**：
```json
{
  "mcpServers": {
    "context7": {
      "env": {
        "CONTEXT7_API_KEY": "ctx7sk-your-actual-key-here"
      }
    }
  }
}
```

⚠️ **安全提醒**：
- 請勿將包含真實 API keys 的 `mcp.json` 提交到版本控制
- 建議將此文件加入 `.gitignore`
- 使用環境變數管理敏感資訊

### 依賴清單

詳見 `DEPENDENCIES.md` 查看所需的 MCP 伺服器列表。

---

### 🔄 流程圖

```mermaid
flowchart TD
    Start([開始 Greenfield 專案]) --> A1
    
    subgraph Phase1 ["📋 階段一：需求分析與計劃"]
        A1["1️⃣ /sunnycore_pm<br/>*create-requirements<br/>📝 建立需求"]
        A2["2️⃣ /sunnycore_architect<br/>*create-architecture<br/>🏗️ 建立架構"]
        A3["3️⃣ /sunnycore_pm<br/>*create-epic<br/>📌 建立任務"]
        A4["4️⃣ /sunnycore_dev<br/>*create-plan<br/>🗓️ 建立計劃"]
        A5["5️⃣ /sunnycore_po<br/>*validate-design full<br/>✅ 驗證設計（可選）"]
        A1 --> A2 --> A3 --> A4
        A4 -.->|"可選"| A5
    end
    
    subgraph Phase2 ["💻 階段二：開發迭代"]
        B0["6️⃣ /sunnycore_dev<br/>*init<br/>⚙️ 初始化專案"]
        B1["7️⃣ /sunnycore_dev<br/>*develop-plan<br/>⚙️ 開發實作"]
        B2["8️⃣ /sunnycore_qa<br/>*review<br/>🔍 文件審查"]
        B0 --> B1 --> B2
    end
    
    D1{"✅ Review<br/>通過?"}
    D2{"📝 還有<br/>任務?"}
    R1["🔄 /sunnycore_dev<br/>*brownfield-tasks<br/>重新開發"]
    
    subgraph Phase3 ["📊 階段三：驗收與總結"]
        C0["9️⃣ /sunnycore_po<br/>*cutover<br/>✅ 項目驗收"]
        C1["🔟 /sunnycore_architect<br/>*document-project<br/>📖 產出專案文件"]
        C2["1️⃣1️⃣ /sunnycore_architect<br/>*curate-knowledge<br/>📚 整理知識"]
        C3["1️⃣2️⃣ /sunnycore_po<br/>*conclude<br/>📋 總結文檔"]
        C0 --> C1 --> C2 --> C3
    end
    
    D3{"✅ Cutover<br/>通過?"}
    R2["🔧 /sunnycore_dev<br/>*fix-acceptance-issues<br/>修復問題"]
    
    Done([✨ 完成開發 Cycle])
    
    A5 --> B0
    A4 --> B0
    B2 --> D1
    D1 -->|"❌ 否"| R1
    R1 --> B1
    D1 -->|"✅ 是"| D2
    D2 -->|"📝 是"| B1
    D2 -->|"✅ 否"| C0
    C0 --> D3
    D3 -->|"❌ 否"| R2
    R2 --> C0
    D3 -->|"✅ 是"| C1
    C3 --> Done
    
    style Start fill:#e1f5e1
    style Done fill:#e1f5e1
    style D1 fill:#fff4e6
    style D2 fill:#fff4e6
    style D3 fill:#fff4e6
    style R1 fill:#ffe6e6
    style R2 fill:#ffe6e6
    style Phase1 fill:#f0f8ff
    style Phase2 fill:#f5f0ff
    style Phase3 fill:#fff0f5
```

---

## 🏗️ Brownfield 專案流程

> 適用於現有專案的擴展與維護

### 📋 階段一：需求分析與計劃

| 步驟 | 命令 | 說明 |
|------|------|------|
| 1 | `/sunnycore_architect *document-project` | 確保專案架構文件是最新的 |
| 2 | `/sunnycore_pm *create-requirements` | 互動式創建需求文檔 |
| 3 | `/sunnycore_pm *create-brownfield-architecture` | 互動式創建架構文檔 |
| 4 | `/sunnycore_pm *create-epic` | 互動式創建任務文檔 |
| 5 | `/sunnycore_dev *create-plan` | 為所有任務創建實作計劃 |
| 6 | `/sunnycore_po *validate-design full` | （可選）驗證需求、架構、任務、計劃之間的完整一致性 |

### 💻 階段二：開發迭代

| 步驟 | 命令 | 說明 |
|------|------|------|
| 7 | `/sunnycore_dev *init` | 初始化開發環境與專案文檔 |
| 8 | `/sunnycore_dev *develop-plan {task_id}` | 基於計劃開發特定 task |
| 9 | `/sunnycore_qa *review {task_id}` | 審查特定 task 的文檔 |

**流程控制：**
- ✅ **Review 通過**：檢查是否還有其他任務
  - 有任務 → 回到步驟 8
  - 無任務 → 進入階段三
- ❌ **Review 未通過**：使用 `/sunnycore_dev *brownfield-tasks {task_id}` 進行重開發，回到步驟 8

### 📊 階段三：驗收與總結

| 步驟 | 命令 | 說明 |
|------|------|------|
| 10 | `/sunnycore_po *cutover` | 項目驗收 |
| 11 | `/sunnycore_architect *document-project` | 更新專案架構文件（建議先親身驗收項目，如發現問題可使用 `/sunnycore_assistant` 協助解決） |
| 12 | `/sunnycore_architect *curate-knowledge` | 整理知識文檔 |
| 13 | `/sunnycore_po *conclude` | 總結文檔 |

**流程控制：**
- ✅ **Cutover 通過**：進入總結流程（步驟 11）
- ❌ **Cutover 未通過**：使用 `/sunnycore_dev *fix-acceptance-issues` 進行修復，回到步驟 10

### 🔄 流程圖

```mermaid
flowchart TD
    Start([開始 Brownfield 專案]) --> A0
    
    subgraph Phase1 ["📋 階段一：需求分析與計劃"]
        A0["1️⃣ /sunnycore_architect<br/>*document-project<br/>📖 更新專案文件"]
        A1["2️⃣ /sunnycore_pm<br/>*create-requirements<br/>📝 建立需求"]
        A2["3️⃣ /sunnycore_pm<br/>*create-brownfield-architecture<br/>🏗️ 建立架構"]
        A3["4️⃣ /sunnycore_pm<br/>*create-epic<br/>📌 建立任務"]
        A4["5️⃣ /sunnycore_dev<br/>*create-plan<br/>🗓️ 建立計劃"]
        A5["6️⃣ /sunnycore_po<br/>*validate-design full<br/>✅ 驗證設計（可選）"]
        A0 --> A1 --> A2 --> A3 --> A4
        A4 -.->|"可選"| A5
    end
    
    subgraph Phase2 ["💻 階段二：開發迭代"]
        B0["7️⃣ /sunnycore_dev<br/>*init<br/>⚙️ 初始化專案"]
        B1["8️⃣ /sunnycore_dev<br/>*develop-plan<br/>⚙️ 開發實作"]
        B2["9️⃣ /sunnycore_qa<br/>*review<br/>🔍 文件審查"]
        B0 --> B1 --> B2
    end
    
    D1{"✅ Review<br/>通過?"}
    D2{"📝 還有<br/>任務?"}
    R1["🔄 /sunnycore_dev<br/>*brownfield-tasks<br/>重新開發"]
    
    subgraph Phase3 ["📊 階段三：驗收與總結"]
        C0["🔟 /sunnycore_po<br/>*cutover<br/>✅ 項目驗收"]
        C1["1️⃣1️⃣ /sunnycore_architect<br/>*document-project<br/>📖 更新專案文件"]
        C2["1️⃣2️⃣ /sunnycore_architect<br/>*curate-knowledge<br/>📚 整理知識"]
        C3["1️⃣3️⃣ /sunnycore_po<br/>*conclude<br/>📋 總結文檔"]
        C0 --> C1 --> C2 --> C3
    end
    
    D3{"✅ Cutover<br/>通過?"}
    R2["🔧 /sunnycore_dev<br/>*fix-acceptance-issues<br/>修復問題"]
    
    Done([✨ 完成開發 Cycle])
    
    A5 --> B0
    A4 --> B0
    B2 --> D1
    D1 -->|"❌ 否"| R1
    R1 --> B1
    D1 -->|"✅ 是"| D2
    D2 -->|"📝 是"| B1
    D2 -->|"✅ 否"| C0
    C0 --> D3
    D3 -->|"❌ 否"| R2
    R2 --> C0
    D3 -->|"✅ 是"| C1
    C3 --> Done
    
    style Start fill:#e1f5e1
    style Done fill:#e1f5e1
    style D1 fill:#fff4e6
    style D2 fill:#fff4e6
    style D3 fill:#fff4e6
    style R1 fill:#ffe6e6
    style R2 fill:#ffe6e6
    style Phase1 fill:#f0f8ff
    style Phase2 fill:#f5f0ff
    style Phase3 fill:#fff0f5
```

---

## 📝 流程說明

### 🚀 PRD vs 🌱 Greenfield vs 🏗️ Brownfield

| 特性 | PRD 流程 | Greenfield | Brownfield |
|------|---------|-----------|------------|
| **適用場景** | 小型變更、快速迭代 | 全新專案 | 現有專案擴展/維護 |
| **文檔結構** | 單一 PRD 文檔 | 分離的需求、架構、任務、計劃文檔 | 分離的需求、架構、任務、計劃文檔 |
| **起始步驟** | 創建 PRD | 直接建立需求 | 先更新專案文件 |
| **需求命令** | `*create-prd` | `*create-requirements` | `*create-requirements` |
| **架構命令** | 內建於 PRD | `*create-architecture` | `*create-brownfield-architecture` |
| **任務命令** | 內建於 PRD | `*create-epic` | `*create-epic` |
| **計劃命令** | 內建於 PRD | `*create-plan`（批量） | `*create-plan`（批量） |
| **開發命令** | `*develop-prd`（一次性） | `*develop-plan`（逐個） | `*develop-plan`（逐個） |
| **總步驟數** | 6 步 | 12 步 | 13 步 |
| **適合規模** | 小型（1-5 個任務） | 中大型（5+ 個任務） | 中大型（5+ 個任務） |

### 🎯 關鍵決策點

1. **Review 檢查點**
   - 每個任務完成後都需要經過 QA 審查
   - 確保代碼質量和符合需求

2. **任務迭代**
   - Review 通過：繼續下一個任務或進入驗收階段
   - Review 未通過：使用 brownfield-tasks 命令重新開發

3. **Cutover 驗收檢查點** ⭐ 新增
   - 從業務和用戶角度驗收項目交付
   - Cutover 通過：進入總結和文檔化階段
   - Cutover 未通過：使用 fix-acceptance-issues 命令修復問題

4. **文檔更新**
   - Greenfield：結束時產出專案文件
   - Brownfield：開始前和結束時都要更新專案文件

### 👥 角色職責

| 角色 | 職責 | 關鍵命令 |
|------|------|----------|
| **Architect** | 技術架構設計、知識管理、技術決策支持 | *create-architecture, *create-brownfield-architecture, *conclude, *curate-knowledge, *document-project |
| **Developer** | 開發實作、任務規劃、技術實現、問題修復 | *init, *create-plan, *develop-plan, *develop-prd, *fix-acceptance-issues |
| **PM** | 產品需求管理、PRD 創建 | *create-requirements, *create-prd, *create-epic |
| **PO** | 業務驗收、需求確認、項目交付、設計驗證與修復 | *cutover, *validate-design, *fix-design-conflicts |
| **QA** | 代碼審查、質量保證 | *review |

### 💡 最佳實踐

- 📌 每個階段完成後進行檢查點確認
- 🔄 保持文檔與代碼同步
- ✅ 確保所有 Review 問題都已解決再進入下一階段
- 📚 及時整理和歸檔知識文檔

### 🔍 設計驗證與修復

#### 何時使用設計驗證？

**推薦在以下時機使用 `*validate-design`：**
- ✅ **PRD 創建後**：驗證 PRD 內部一致性和與現有架構的對齊
- ✅ **需求分析階段完成後**：確保需求、架構、任務之間完整對齊
- ✅ **開發前**：避免基於有問題的設計文檔進行開發
- ✅ **發現文檔不一致時**：主動檢查和修復問題

#### 設計驗證工作流程

**PRD 驗證流程：**
```
/sunnycore_po *validate-design prd
↓
查看 docs/design-validation.md
↓ (如有問題)
/sunnycore_po *fix-design-conflicts
↓
重新驗證確認修復
```

**完整驗證流程：**
```
/sunnycore_po *validate-design full
↓
查看 docs/design-validation.md
↓ (如有問題)
/sunnycore_po *fix-design-conflicts
↓
重新驗證確認修復
```

#### 驗證內容說明

| 驗證類型 | 檢查項目 | 輸出 |
|---------|---------|------|
| **PRD 驗證** | • PRD 內部一致性<br>• 需求-架構-任務對齊<br>• 與現有架構的兼容性<br>• 內容真實性（無捏造引用） | `docs/design-validation.md` |
| **完整驗證** | • 雙向引用完整性<br>• 覆蓋率分析（100%）<br>• 跨文檔一致性<br>• 衝突檢測<br>• 內容真實性 | `docs/design-validation.md` |

#### 修復衝突流程

`*fix-design-conflicts` 命令會：
1. 讀取驗證報告中的所有問題
2. 按嚴重性排序（Critical → High → Medium → Low）
3. 與用戶互動確認修復策略
4. 自動修改相關文檔
5. 完成後刪除驗證報告
6. 建議重新運行驗證確認
