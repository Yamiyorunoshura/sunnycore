# 提示工程使用指南（Prompt Engineering Guide）
本指南說明如何以 XML 風格標籤搭配結構化提示詞，建立一致、可維護、可審查的工作流框架。內容涵蓋：標籤語法、撰寫規範、常見模板（agents/commands/tasks）與示例，協助你快速上手並降低溝通成本。
為提升 token 使用效率與跨語系可移植性：文件敘述採用繁體中文；實際「提示詞內容」一律以英文撰寫。

## 術語對照表（Terminology Reference）
| 中文術語 | 英文術語 | 說明 |
|---------|---------|-----|
| 提示詞 | Prompt | 與 LLM 交互的指令內容 |
| 標籤 | Tag | XML 風格的結構化標記 |
| 約束條件 | Constraints | 任務規範與硬性限制 |
| 檢核點 | Checks | 可驗證的品質檢查項目 |
| 工作流程 | Workflow | 任務執行的階段性流程 |
| 優先等級 | Importance Level | Optional/Normal/Important/Critical |
| 角色設定 | Role | 模型的專業定位與語氣邊界 |
| 模板 | Template | 結構化的提示詞框架 |

# 通用 XML 標籤
本節說明在所有文檔中通用的 XML 風格標籤及其用途與最小建議用法。

## 上下文相關標籤
用於描述任務輸入與期望輸出。
- <input>：任務輸入容器。
    - <context>：LLM 需要讀取的背景與資料來源（要具體、可引用）。
- <output>：明確定義輸出格式與欄位（讓結果可機器判讀或人工快速核對）。
    - <context>：可用於補充輸出的結構化格式說明。
- <constraints>：任務規範與硬性限制（例如長度、格式、不得事項）。
- <example>：示例輸入與輸出（以最小可用示例為主，必要時多樣化）。
- <questions>：自我提問引導模型澄清重點與避免謬誤。
- <checks>：最終自檢清單，聚焦可觀察且可驗證的項目。
- <tools>：工具列表，用於指示模型使用工具。

## 角色相關標籤
- <role, name = "Role Name">：設定模型的專業定位與語氣邊界。
  - 名字：可留空或以職稱替代。
  - 角色：描述職能與決策範圍，避免空泛形容詞。
  - 人格特質：只保留與決策風格或風險偏好相關的特質。

## 工作流程相關標籤
- <workflow, importance = "Optional/Normal/Important/Critical">：定義工作流程骨架，僅保留 3-5 個關鍵階段。
    - importance：標示整體優先等級，用於任務調度或審查。
    - <stage, id = "Stage ID">：工作階段，描述本階段的關鍵產出與檢核點。
        - id：不含空白、具語義（例如 research、draft、review、finalize）。

### 優先等級定義（Importance Level Guidelines）
- **Optional**: 可選項目，不影響核心功能或品質，資源充裕時執行
- **Normal**: 標準項目，正常優先級，按計劃執行
- **Important**: 重要項目，影響整體品質或用戶體驗，需優先分配資源
- **Critical**: 關鍵項目，阻塞性需求，必須立即處理且不可延遲

# 快速入門指南（Quick Start Guide）

## 步驟 1: 選擇模板類型
1. **agents**: 定義獨立的智能助理，具有特定的角色與能力
2. **commands**: 創建帶有子命令的互動工作流
3. **tasks**: 拆解複雜任務為可執行的子項目

## 步驟 2: 遵循決策樹
```
是否需要人格化角色？
│
├── 是 → 使用 agents 模板
│
└── 否 → 是否有子命令？
     │
     ├── 是 → 使用 commands 模板
     │
     └── 否 → 使用 tasks 模板
```

## 步驟 3: 確保必要組件
- [ ] `<input>` 定義清晰的輸入要求
- [ ] `<output>` 明確輸出格式與欄位
- [ ] `<constraints>` 3-5 條可驗證的限制
- [ ] `<checks>` 2-5 個可勾選的檢核點

## 常見錯誤與解決方案

### 錯誤 1: 約束條件過於模糊
**問題**: 使用「更自然」、「更好」等不可驗證的描述  
**解決**: 改為具體指標，例如「平均每句 < 20 詞」

### 錯誤 2: 角色設定過於繁琐
**問題**: 描述冷長的背景故事或人格特質  
**解決**: 只保留與決策風格相關的關鍵特質

### 錯誤 3: 缺乏明確輸出結構
**問題**: `<output>` 部分只有模糊要求  
**解決**: 定義機器可讀的結構，例如 JSON 格式或特定欄位

# 提示詞規範
本節提供撰寫 Constraints、Questions、Checks 的可操作準則，避免過度指示與冗語。

## Constraints 標籤規範
- 重點聚焦在「限制」與「不可違反的規則」，建議 3-5 條。
- 以可驗證的述句撰寫：可度量、可真偽檢驗、可透過工具檢查。
- 規範應與工作步驟相關。
- 優先順序明確；必要時以「Must/Should/May」區分強弱。
- 避免空泛要求（如「更自然」），改為具體（如「用短句，平均每句 < 20 詞」）。

## Questions 標籤規範
- 以 2-3 個高價值問題引導模型釐清不確定性。
- 著重：輸入完整性、關鍵假設、成功條件、風險與邊界案例。
- 問題應可由當前上下文回答或引導生成可驗證的補充需求。

## Checks 標籤規範
- 於工作流程末尾執行；列出 2-5 個可觀察、可勾選的檢核點。
- 每一項應對應到可量測的輸出特徵或格式要求。
- 鼓勵加入「失敗案例」對照（例如：若未包含欄位 X，則失敗）。

## Workflow 標籤規範
- 僅保留 3-5 個階段；每階段皆要有明確輸出與檢核。
- 階段描述避免流程化細節，聚焦於決策與產物。
- 可用 importance 標註任務級別，幫助排程與審查。

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
        
# 提示詞架構
本節提供 agents / commands / tasks 三種常用模板的結構化格式、欄位說明與最小示例。模板中的實際內容請以英文撰寫。

## 通用模板組件（Common Template Components）
以下組件為所有模板共用，保持一致的結構與格式：

### 基本輸入結構
```xml
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
```

### 基本輸出結構
```xml
<output>
1. {Output Item 1}
2. {Output Item 2}
3. {Output Item 3}
</output>
```

### 約束條件結構
```xml
<constraints, importance = "Normal">
- {Constraint 1}
- {Constraint 2}
- {Constraint 3}
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

## 快速參考卡（Quick Reference Card）

### 核心標籤速查
| 標籤 | 用途 | 最佳實踐 |
|------|------|----------|
| `<input>` | 定義輸入要求 | 包含 `<context>` 和 `<templates>` |
| `<output>` | 明確輸出格式 | 機器可讀、有明確欄位 |
| `<constraints>` | 任務限制 | 3-5 條，可驗證 |
| `<questions>` | 自我提問 | 2-3 個高價值問題 |
| `<checks>` | 品質檢核 | 2-5 個可勾選項目 |
| `<role>` | 角色設定 | 避免冗長背景故事 |
| `<workflow>` | 工作流程 | 3-5 個階段 |

### 重要性級別速查
- **Optional**: 可選項目，資源充裕時執行
- **Normal**: 標準優先級，按計劃執行  
- **Important**: 影響整體品質，需優先分配資源
- **Critical**: 關鍵項目，必須立即處理

### 常用模板選擇器
```
需要角色扮演？ → agents
需要子命令？   → commands  
需要任務拆解？ → tasks
```

## 快速檢查表（出稿前自查）
- [ ] <output> 是否定義了機器可讀的結構與欄位？
- [ ] <constraints> 是否 3-5 條且可驗證、可度量？
- [ ] <checks> 是否可逐項勾選且能明確判斷成敗？
- [ ] 是否提供至少一組最小可用 <example>？
- [ ] 是否保留 3-5 個關鍵 <stage>，每階段有產出與檢核？
- [ ] 術語使用是否一致（參考術語對照表）？
- [ ] 重要性級別是否明確且適當？

## commands 提示詞架構
用於定義帶有可執行「子命令／工具」的工作說明。

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

# 故障排除與最佳實踐（Troubleshooting & Best Practices）

## 常見問題診斷與解決

### 問題 1: 模型回應不符預期格式
**症狀**: 輸出格式混亂、缺少欄位或結構不正確  
**診斷**: 檢查 `<output>` 是否足夠明確  
**解決方案**:
- 使用具體的格式範例，如 JSON schema
- 在 `<constraints>` 中明確要求格式驗證
- 提供失敗案例對比

**範例**:
```xml
<output>
Format: JSON with fields: {title, summary, tags}
Example: {"title": "Task Name", "summary": "Brief description", "tags": ["tag1", "tag2"]}
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