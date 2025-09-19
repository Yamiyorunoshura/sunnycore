# 提示工程使用指南（Prompt Engineering Guide）
本指南說明如何以 XML 風格標籤搭配結構化提示詞，建立一致、可維護、可審查的工作流框架。內容涵蓋：標籤語法、撰寫規範、常見模板（agents/commands/tasks）與示例，協助你快速上手並降低溝通成本。
為提升 token 使用效率與跨語系可移植性：文件敘述採用繁體中文；實際「提示詞內容」一律以英文撰寫。

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

## Tools 標籤規範
- 提供工具列表，用於指示模型使用工具。

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

## agents 提示詞架構

name: {Agent Name}
description: {Description}
model: inherit
color: {Color}
---

<start_sequence>
1. xxx
2. yyy
3. zzz
</start_sequence>

<role name="Role Name">
# 角色
名字：{Role Name}
角色：{Role Description}
人格特質：
- xxx
- yyy
- zzz
</role>

<example>(optional)
- xxx
- yyy
- zzz
</example>

<constraints, importance = "Optional/Normal/Important/Critical">
- xxx
- yyy
- zzz
</constraints>

<input>
  <context>
  1. xxx
  2. yyy
  3. zzz
  </context>
  <templates>
  1. xxx
  2. yyy
  3. zzz
  </templates>
</input>

<output>
1. xxx
2. yyy
3. zzz
</output>

<instructions>
- xxx
- yyy
- zzz
</instructions>

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

## 快速檢查表（出稿前自查）
- [ ] <output> 是否定義了機器可讀的結構與欄位？
- [ ] <constraints> 是否 3-5 條且可驗證、可度量？
- [ ] <checks> 是否可逐項勾選且能明確判斷成敗？
- [ ] 是否提供至少一組最小可用 <example>？
- [ ] 是否保留 3-5 個關鍵 <stage>，每階段有產出與檢核？

## commands 提示詞架構
用於定義帶有可執行「子命令／工具」的工作說明。

<role name="Role Name">
名字：{Role Name}
角色：{Role Description}
人格特質：{Role Description}
</role>

<custom_commands>
- *xxx
  - 讀取xxx
- *yyy
  - 讀取yyy
- *zzz
  - 讀取zzz
</custom_commands>

<constraints, importance = "Optional/Normal/Important/Critical">
- xxx
- yyy
- zzz
</constraints>

<example>(optional)
xxx
yyy
zzz
</example>

<input>
  <context>
  1. xxx
  2. yyy
  3. zzz
  </context>
  <templates>
  1. xxx
  2. yyy
  3. zzz
  </templates>
  <tasks>
  1. xxx
  2. yyy
  3. zzz
  </tasks>
</input>

<output>
1. xxx
2. yyy
3. zzz
</output>

<instructions>
- xxx
- yyy
- zzz
</instructions>

## tasks 提示詞架構
用於拆解複雜任務，輸出具體、可驗收的子產物。
<input>
  <context>
  1. xxx
  2. yyy
  3. zzz
  </context>
  <templates>
  1. xxx
  2. yyy
  3. zzz
  </templates>
  <subagent-list>(optional)
  1. xxx
  2. yyy
  3. zzz
  </subagent-list>
</input>

<output>
1. xxx
2. yyy
3. zzz
</output>

<constraints, importance = "Optional/Normal/Important/Critical">
- xxx
- yyy
- zzz
</constraints>

<example>(optional)
範本輸出：

# Functional Requirements
- xxx
- yyy
- zzz

# Non-functional Requirements
- xxx
- yyy
- zzz

# Acceptance Criteria
- xxx
- yyy
- zzz
</example>

<workflow, importance = "Optional/Normal/Important/Critical">
  <stage id="n: stage name">
  <tools: xxx>
  - xxx
  - yyy
  - zzz
  </tools: xxx>
  </stage>

  <stage id="n: stage name">
  - xxx
  - yyy
  - zzz
  
  <questions>(optional, base on the complexity of the task)
  - xxx?
  - yyy?
  - zzz?
  </questions>

  <checks>(only at the last stage)
  - [ ] xxx
  - [ ] yyy
  - [ ] zzz
  </checks>
  </stage>

</workflow>