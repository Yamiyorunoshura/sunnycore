# 提示工程使用指南（Prompt Engineering Guide）

## 指南目的
本指南提供基於 XML 標籤的結構化提示詞框架，幫助您建立：
- **一致性**：標準化的提示詞結構
- **可維護性**：清晰的組織與更新流程  
- **可審查性**：明確的品質檢核點

## 使用原則
- 文檔說明：繁體中文
- 提示詞內容：英文（提升 token 效率與可移植性）
- 結構優先：先定義格式，後填入內容

## 核心術語

| 中文 | 英文 | 定義 |
|------|------|------|
| 提示詞 | Prompt | LLM 交互指令 |
| 標籤 | Tag | XML 結構標記 |
| 約束條件 | Constraints | 硬性限制規則 |
| 檢核點 | Checks | 品質驗證項目 |
| 角色 | Role | 專業定位設定 |
| 模板 | Template | 結構化框架 |

## 優先等級
- **Critical**：關鍵項目，必須立即處理
- **Important**：重要項目，影響整體品質
- **Normal**：標準優先級，按計劃執行
- **Optional**：可選項目，資源充裕時執行

# 必備 XML 標籤工具箱

## 輸入輸出標籤（基礎組件）

**`<input>`** – 任務輸入容器
- `<context>` – 背景資料（必須具體可引用）  
- `<templates>` – 模板列表
- `<tasks>` – 任務流程  
- `<rules>` – 規則

**`<output>`** – 輸出格式定義（必須機器可讀）

## 品質控制標籤（進階組件）

**`<constraints>`** – 硬性限制（3-5 條可驗證規則）  
**`<questions>`** – 自我檢查問題（2-3 個重點問題）  
**`<checks>`** – 品質檢核清單（2-5 個可勾選項目）

## 特殊功能標籤

**`<example>`** – 實際示例（最小可用為主）  
**`<tools>`** – 工具列表  
**`<instructions>`** – 複雜指導內容

## 專業角色標籤

**`<role name="角色名稱">`** – 專業定位設定
- **名字**：職稱或專業領域
- **角色**：核心職能與決策範圍
- **人格特質**：僅保留影響決策風格的關鍵特質

## 工作流程標籤

**`<workflow importance="等級">`** – 流程骨架（3-5 階段）
- **`<stage id="階段ID">`** – 關鍵工作階段
  - ID 格式：`1: {tasks_name_1}`、`2: {tasks_name_2}`、`3: {tasks_name_3}`、`4: {tasks_name_4}`、`5: {tasks_name_5}`
  - 每階段必須有明確產出與檢核點

# 3 分鐘快速入門

## 第一步：選擇模板類型

🤖 **agents** → 需要人格化助理？  
📝 **commands** → 需要互動子命令？  
✅ **tasks** → 需要拆解複雜流程？

### 決策樹
```
人格化角色？ ──YES──▶ agents
       │
      NO
       │
互動命令？ ──YES──▶ commands  
       │
      NO
       │
       ▼
     tasks
```

## 第二步：完成核心組件

**必須項：**
- ☑️ `<input>` 輸入要求
- ☑️ `<output>` 輸出格式  
- ☑️ `<constraints>` 3-5 條限制
- ☑️ `<checks>` 2-5 個檢核點

**選擇性：**
- 📝 `<example>` 實際示例
- ❓ `<questions>` 自檢問題
- 🔧 `<tools>` 工具列表

## 第三步：品質檢查
進行最終檢查，確保文檔符合標準

## 常見錯誤與解決方案

### 錯誤 1: 約束條件過於模糊
**問題**: 使用「更自然」、「更好」等不可驗證的描述  
**解決**: 改為具體指標，例如「平均每句 < 20 詞」

### 錯誤 2: 角色設定過於繁瑣
**問題**: 描述冷長的背景故事或人格特質  
**解決**: 只保留與決策風格相關的關鍵特質

### 錯誤 3: 缺乏明確輸出結構
**問題**: `<output>` 部分只有模糊要求  
**解決**: 定義機器可讀的結構，例如 JSON 格式或特定欄位

# 標籤撰寫規範

以下提供各標籤的實用準則，確保內容可驗證、可操作。

## `<constraints>` 規範

**基本要求**：
- 數量：3-5 條限制
- 格式：可驗證、可度量
- 優先級：`MUST` > `SHOULD` > `MAY`

**實例對比**：
- ❌ 「回應要自然」
- ✅ 「句子 < 20 詞」

**格式範例**：
```xml
<constraints importance="Normal">
- MUST: Response length 100-300 words
- SHOULD: Use bullet points (exactly 3)
- MAY: Include relevant examples
</constraints>
```

## `<questions>` 規範

**重點問題類型**：
- 輸入完整性：「所需資料是否完整？」  
- 關鍵假設：「這個方案的前提是什麼？」
- 成功條件：「怎樣算達到目標？」

**格式範例**：
```xml
<questions>
- Have I defined all required input parameters?
- What assumptions am I making about user context?
- How will success be measured?
</questions>
```

## `<checks>` 規範

**檢核點要求**：
- 數量：2-5 個可勾選項目
- 格式：`[ ]` 清單式
- 內容：可觀察、可驗證

**實例範例**：
```xml
<checks>
- [ ] Output contains exactly 3 bullet points
- [ ] All technical terms are defined
- [ ] Response length is 200-400 words
- [ ] Includes at least one practical example
</checks>
```

**避免模糊**：
- ❌ 「內容是否完整」
- ✅ 「包含 5 個主要部分」

## `<workflow>` 規範

**結構要求**：
- 階段數：3-5 個關鍵階段
- ID 格式：`research` → `draft` → `review` → `finalize`
- 每階段必須：明確產出 + 檢核點

**格式範例**：
```xml
<workflow importance="Normal">
  <stage id="1: research">
  - Gather requirements from context
  - Identify key constraints
  - Document assumptions
  </stage>
  
  <stage id="2: draft">
  - Create initial structure
  - Develop core content
  - Apply formatting standards
  </stage>
</workflow>
```

## Example 標籤規範
- 必要時提供實例
- 用於規範或提示模型輸出格式

## Instructions 標籤規範
- 用於包含複雜的指導內容、規則集、或參考資料。
- 內部可使用結構化的 XML 子標籤來組織內容。
- 常見的子標籤模式：
  - `<review-standards>` / `<evaluation-criteria>` - 評估標準
  - `<quality-matrix>` / `<scoring-system>` - 品質或評分系統
  - `<decision-rules>` / `<approval-criteria>` - 決策規則
  - `<reference-guide>` / `<best-practices>` - 參考指南
- 保持內容的可操作性與可驗證性。
        
# 三大模板架構

選擇適合的模板類型，快速建立結構化提示詞。

## 基礎組件模板

所有模板都包含以下核心組件：

```xml
<input>
  <context>
  1. {Context Item} 
  2. {Context Item}
  </context>
  <templates>
  1. {Template Reference}
  </templates>
</input>

<output>
1. {Output Specification}
2. {Format Requirements}
</output>

<constraints importance="Normal">
- MUST: {Hard Requirement}
- SHOULD: {Preferred Approach}
</constraints>
```

## agents 提示詞架構
用於定義獨立的智能助理，具有特定的角色與能力。

### 模板結構
```
name: {Agent Name}
description: {Description}
model: inherit
color: {Color}
---

<role name="Role Name">
名字：{Role Name}
角色：{Role Description}
人格特質：
- {Personality Trait 1}
- {Personality Trait 2}
- {Personality Trait 3}
</role>

<input>
  <context>
  1. {Context Item 1}
  2. {Context Item 2}
  3. {Context Item 3}
  </context>
  <templates>
  1. {Template Reference 1}
  2. {Template Reference 2}
  3. {Template Reference 3}
  </templates>
</input>

<output>
1. {Output Item 1}
2. {Output Item 2}
3. {Output Item 3}
</output>

<constraints, importance = "Normal">
- {Constraint 1}
- {Constraint 2}
- {Constraint 3}
</constraints>

<example>(optional)
{Example Content}
</example>

<instructions>
- {Instruction 1}
- {Instruction 2}
- {Instruction 3}
</instructions>
```

# 寫作風格與反模式
## 推薦寫作風格
- 以使用者故事與成功條件驅動：先定義驗收準則，再往回設計輸入與限制。
- 偏好結構化列點：數字清單優先於長段落；格式先於措辭。
- 早設欄位、後填內容：先定義 <output> 的欄位與格式，再引導模型生成內容。
- 可驗證為王：每條 constraint 與 check 都應可被人工或工具驗證。

## 常見反模式（避免）
- 過度角色扮演：冗長的身世/人設無助於決策品質。
- 空話與重複：如「更好」「更自然」未提供可操作標準。
- 指令稀釋：同時要求過多目標（>5）導致回應表面完整、實則鬆散。
- 缺乏邊界：未定義不得事項（security、PII、法律合規）。

# 快速參考手冊 📚

## 標籤速查表

| 標籤 | 用途 | 数量/標準 |
|------|------|----------|
| `<input>` | 輸入要求 | 必須包含 `<context>` |
| `<output>` | 輸出格式 | 機器可讀結構 |
| `<constraints>` | 硬性限制 | 3-5 條，可驗證 |
| `<checks>` | 品質檢核 | 2-5 個可勾選 |
| `<questions>` | 自檢問題 | 2-3 個高價值 |
| `<role>` | 角色設定 | 簡潔明確 |
| `<workflow>` | 工作流程 | 3-5 個階段 |

## 模板快選

🤖 **agents** = 人格化角色  
📝 **commands** = 互動子命令  
✅ **tasks** = 流程拆解

## 優先等級

🔴 **Critical** → 必須立即處理  
🟡 **Important** → 影響整體品質  
🟢 **Normal** → 標準優先級  
⚪ **Optional** → 可選項目

## 出稿前檢查清單 ✅

### 必須項目
- [ ] `<input>` 輸入要求明確具體
- [ ] `<output>` 定義機器可讀的結構
- [ ] `<constraints>` 3-5 條可驗證限制
- [ ] `<checks>` 2-5 個可勾選檢核點

### 加分項目
- [ ] 提供實用 `<example>`
- [ ] 包含 `<questions>` 自檢問題
- [ ] 設定適當 importance 等級
- [ ] 術語使用一致性

### 最終確認
❓ **問問自己：這份提示詞是否能產出一致、可驗證的結果？**

## commands 提示詞架構
用於定義帶有可執行「子命令／工具」的工作說明。

### 模板結構
```
<start sequence>
1. {Start Sequence 1}
2. {Start Sequence 2}
3. {Start Sequence 3}
</start sequence>

<input>
  <context>
  1. {Context Item 1}
  2. {Context Item 2}
  3. {Context Item 3}
  </context>
  <templates>
  1. {Template Reference 1}
  2. {Template Reference 2}
  3. {Template Reference 3}
  </templates>
  <tasks>
  1. {Task Reference 1}
  2. {Task Reference 2}
  3. {Task Reference 3}
  </tasks>
</input>

<output>
1. {Output Item 1}
2. {Output Item 2}
3. {Output Item 3}
</output>

<role name="Role Name">
名字：{Role Name}
角色：{Role Description}
人格特質：{Role Personality}
</role>

<custom_commands>
- *{command_name}
  - {command_description}
- *{command_name}
  - {command_description}
</custom_commands>

<constraints, importance = "Normal">
- {Constraint 1}
- {Constraint 2}
- {Constraint 3}
</constraints>

<example>(optional)
{Example Content}
</example>

<instructions>
- {Instruction 1}
- {Instruction 2}
- {Instruction 3}
</instructions>
```

## tasks 提示詞架構
用於拆解複雜任務，輸出具體、可驗收的子產物。

### 模板結構
```
<input>
  <context>
  1. {Context Item 1}
  2. {Context Item 2}
  3. {Context Item 3}
  </context>
  <templates>
  1. {Template Reference 1}
  2. {Template Reference 2}
  3. {Template Reference 3}
  </templates>
  <subagent-list>(optional)
  1. {Subagent 1}
  2. {Subagent 2}
  3. {Subagent 3}
  </subagent-list>
</input>

<output>
1. {Output Item 1}
2. {Output Item 2}
3. {Output Item 3}
</output>

<constraints, importance = "Normal">
- {Constraint 1}
- {Constraint 2}
- {Constraint 3}
</constraints>

<example>(optional)
{Example Content}
</example>

<workflow, importance = "Normal">
  <stage id="1: stage_name">
  - {Stage Action 1}
  - {Stage Action 2}
  - {Stage Action 3}
  </stage>

  <stage id="2: stage_name">
  - {Stage Action 1}
  - {Stage Action 2}
  - {Stage Action 3}
  
  <questions>(optional)
  - {Question 1}?
  - {Question 2}?
  - {Question 3}?
  </questions>

  <checks>(only at the last stage)
  - [ ] {Check Item 1}
  - [ ] {Check Item 2}
  - [ ] {Check Item 3}
  </checks>
  </stage>
</workflow>
```

# 問題解決面板

## 常見問題速查表

| 問題 | 症狀 | 快速修復 |
|------|------|----------|
| 格式混亂 | 輸出結構不一致 | 加入 JSON 範例到 `<output>` |
| 約束無效 | 模型忽略限制 | 使用 MUST/SHOULD/MAY 優先級 |
| 角色混亂 | 回應風格不穩 | 簡化角色描述，只保留核心特質 |
| 流程不完整 | 跳過某些階段 | 每階段都要有明確產出要求 |

## 一鍵修復範例

### 格式問題修復
```xml
<!-- Before: 模糊要求 -->
<output>Provide a good summary</output>

<!-- After: 明確結構 -->
<output>
Format: JSON {"title": string, "summary": string, "tags": array}
Example: {"title": "Task Overview", "summary": "Brief description", "tags": ["urgent", "review"]}
</output>
```

### 問題 2: 約束條件無效或被忽略
**症狀**: 模型不遵守設定的限制  
**診斷**: 約束條件可能過於模糊或不可驗證  
**解決方案**:
- 使用可量測的指標（數字、百分比、具體行為）
- 採用 Must/Should/May 優先級區分
- 在 `<checks>` 中加入驗證步驟

**範例**:
```xml
<constraints importance="Important">
- MUST: Response length between 100-300 words
- MUST: Include exactly 3 bullet points
- SHOULD: Use active voice (>80% of sentences)
</constraints>
```

### 問題 3: 角色設定過於複雜導致混亂
**症狀**: 模型回應不一致或偏離預期角色  
**診斷**: 角色描述可能過於冗長或矛盾  
**解決方案**:
- 專注於決策風格相關的特質
- 避免過度的背景故事
- 明確職能邊界

**範例**:
```xml
<role name="Technical Reviewer">
角色：Software architecture expert with 10+ years experience
人格特質：
- Detail-oriented with focus on scalability concerns
- Prefers evidence-based recommendations
- Direct communication style with constructive feedback
</role>
```

### 問題 4: 工作流程執行不完整
**症狀**: 模型跳過某些階段或檢核點  
**診斷**: 階段定義不夠明確或缺少必要的連接  
**解決方案**:
- 每階段都要有明確的輸出要求
- 使用數字編號確保順序
- 在最後階段加入完整性檢查

## 品質提升技巧

### 技巧 1: 漸進式細化（Progressive Refinement）
1. 先建立基本架構（input, output, constraints）
2. 添加核心邏輯（role, workflow）
3. 補充細節（example, questions, checks）
4. 測試並迭代優化

### 技巧 2: 驗證驅動設計（Validation-Driven Design）
- 先寫 `<checks>` 定義成功標準
- 再設計 `<output>` 符合檢核要求
- 最後調整 `<constraints>` 確保可達成

### 技巧 3: 模組化重用（Modular Reuse）
- 建立常用的 `<input>` 模板庫
- 標準化 `<constraints>` 集合
- 維護可重用的 `<role>` 定義

## 效能最佳化建議

### 降低 Token 使用
- 使用簡潔但精確的語言
- 避免重複或冗餘的說明
- 採用結構化列表而非長段落

### 提升回應品質
- 平衡具體性與靈活性
- 使用多層次的約束（Must > Should > May）
- 加入邊界案例的處理指導

### 維護一致性
- 建立團隊共用的術語表
- 定期review和更新模板
- 記錄設計決策的原因

## 驗證清單（Validation Checklist）

在發布提示詞前，請確認：

**結構完整性**:
- [ ] 必要標籤都已包含
- [ ] 標籤嵌套正確且閉合
- [ ] 重要性級別已設定且適當

**內容質量**:
- [ ] 輸出格式明確且可驗證
- [ ] 約束條件具體且可量測
- [ ] 範例充分且相關

**可用性**:
- [ ] 角色定義簡潔且聚焦
- [ ] 工作流程邏輯清晰
- [ ] 檢核點可操作且完整

**一致性**:
- [ ] 術語使用符合對照表
- [ ] 風格統一且專業
- [ ] 與團隊標準一致