# XML 代理系統規範 v1.0

## 概述

本規範定義多代理系統的 XML 結構與標籤規約。該規範為使用結構化 XML 元素定義代理角色、任務、執行流程和安全協議提供標準化框架。

## 1. 根元素結構

### 1.1 主要根元素

```xml
<prompt spec-version="1.0" profile="standard">
  <!-- 內容 -->
</prompt>
```

**屬性說明：**
- `spec-version`: 規範版本標識符（必填）
- `profile`: 執行嚴格程度（必填）
  - `light`: 僅包含基礎任務層、輸入輸出與簡單流程
  - `standard`: 完整框架，包含任務、上下文、流程、安全、輸出與品質層
  - `strict`: 標準框架基礎上增加強制性審計與提交要求

## 2. 任務層

任務層定義代理系統的基本目的與約束條件。

### 2.1 角色定義

```xml
<role name="代理標識符"/>
```

定義代理在系統中的主要職責與功能。

### 2.2 目標聲明

```xml
<goal>主要目標描述</goal>
```

清晰簡潔地陳述要達成的主要任務或結果。

### 2.3 約束條件

```xml
<constraints>
  <item>具體限制或禁止事項</item>
  <item>額外約束條件</item>
</constraints>
```

明確規定管制代理行為與動作的界限與限制。

### 2.4 政策規範

```xml
<policies>
  <policy id="政策標識符" version="1.0">政策內容與規則</policy>
</policies>
```

**屬性說明：**
- `id`: 唯一政策標識符
- `version`: 政策版本，用於追蹤更新

### 2.5 指標設定

```xml
<metrics>
  <metric type="效能指標" target="閾值"/>
</metrics>
```

**屬性說明：**
- `type`: 指標類別或測量類型
- `target`: 預期效能閾值或目標

## 3. 上下文層

上下文層為代理執行提供環境與操作上下文。

### 3.1 倉庫對映

```xml
<context>
  <repo-map>倉庫結構或目錄範圍定義</repo-map>
</context>
```

定義代理運作的檔案系統或倉庫邊界。

### 3.2 檔案引用

```xml
<files>
  <file path="相對/路徑/至/檔案">額外元資料或描述</file>
</files>
```

**屬性說明：**
- `path`: 從倉庫根目錄的相對檔案路徑

### 3.3 相依性

```xml
<dependencies>
  套件、模組或外部相依性規格說明
</dependencies>
```

列出代理運作所需的套件、函式庫或外部系統。

## 4. 工具層

工具層定義可用功能與外部介面。

### 4.1 工具定義

```xml
<tools>
  <tool name="工具標識符" kind="command|api|mcp">工具描述與用法</tool>
</tools>
```

**屬性說明：**
- `name`: 唯一工具標識符
- `kind`: 工具類別
  - `command`: 命令列可執行程式
  - `api`: 外部 API 介面
  - `mcp`: 模型上下文協議伺服器

### 4.2 命令規格

```xml
<commands>
  <command name="命令名稱" bin="可執行檔路徑" timeout="秒數"/>
</commands>
```

**屬性說明：**
- `name`: 命令標識符
- `bin`: 可執行二進位檔案路徑
- `timeout`: 最大執行時間（秒）

### 4.3 MCP 伺服器配置

```xml
<mcp>
  <server id="伺服器標識符" capability="伺服器功能"/>
</mcp>
```

**屬性說明：**
- `id`: 唯一伺服器標識符
- `capability`: 可用伺服器功能或協議

## 5. 流程層

流程層定義執行工作流程與驗證程序。

### 5.1 執行計劃

```xml
<plan allow-reorder="true|false">
  <step id="步驟標識符" type="read|analyze|test|report">步驟描述</step>
</plan>
```

**屬性說明：**
- `allow-reorder`: 步驟是否可以非順序執行
- `id`: 唯一步驟標識符
- `type`: 步驟類別，用於執行最佳化

### 5.2 驗證檢查清單

```xml
<validation_checklist>
  <item>驗證要求或檢查點</item>
</validation_checklist>
```

定義執行期間或執行後需要驗證的品質保證檢查點。

## 6. 安全層

安全層實施保護措施與錯誤處理協議。

### 6.1 快速停止觸發器

```xml
<fast_stop_triggers>
  <trigger id="觸發器標識符">
    <condition>觸發條件描述</condition>
    <action>immediate_stop</action>
    <o>標準錯誤訊息</o>
  </trigger>
</fast_stop_triggers>
```

**元素說明：**
- `condition`: 啟動觸發器的具體情況
- `action`: 快速觸發器一律為 `immediate_stop`
- `output`: 顯示的固定錯誤訊息

### 6.2 緊急停止協議

```xml
<emergency_stop>
  <fixed_message>緊急停止：詳細停止原因</fixed_message>
  <reason_codes>TOOL_FAILURE|MISSING_REQUIRED_FILE|EMPTY_CONTENT|SECURITY_VIOLATION</reason_codes>
</emergency_stop>
```

**原因代碼：**
- `TOOL_FAILURE`: 外部工具或命令失效
- `MISSING_REQUIRED_FILE`: 找不到必要輸入檔案
- `EMPTY_CONTENT`: 關鍵內容為空或損壞
- `SECURITY_VIOLATION`: 偵測到安全政策違規

### 6.3 護欄規則

```xml
<guardrails>
  <rule id="規則標識符">行為限制或安全要求</rule>
</guardrails>
```

定義代理操作的持續行為約束與安全邊界。

## 7. 輸入輸出層

輸入輸出層指定資料來源與輸出格式要求。

### 7.1 輸入規格

```xml
<inputs>
  <git_context>
    <message/>
    <changed_files/>
    <diff/>
    <branch/>
  </git_context>
  
  <cicd_report>
    <source_id/>
    <run_id/>
    <raw_logs/>
    <status/>
  </cicd_report>
</inputs>
```

**Git 上下文元素：**
- `message`: 提交訊息或分支資訊
- `changed_files`: 修改檔案清單
- `diff`: 程式碼變更或差異
- `branch`: 目標分支資訊

**CI/CD 報告元素：**
- `source_id`: 建置系統標識符
- `run_id`: 特定執行運行標識符
- `raw_logs`: 建置或測試執行日誌
- `status`: 目前管線狀態

### 7.2 輸出規格

```xml
<outputs>
  <final format="json|markdown" schema="結構定義標識符"/>
  <output_location>目標/檔案/路徑</output_location>
</outputs>
```

**屬性說明：**
- `format`: 輸出資料格式
- `schema`: 輸出結構定義的參考

## 8. 推理與輸出層

所有代理必須使用結構化處理區塊將內部推理與最終交付成果分離。

### 8.1 核心處理區塊

```xml
<analysis>內部分析與推理過程</analysis>
<implementation>實際執行或內容生成</implementation>
<validation>結果驗證與品質檢查</validation>
```

### 8.2 任務特定擴展

根據代理功能，可使用額外的處理區塊：

```xml
<classification>文件或內容分類結果</classification>
<curation>知識組織與結構化</curation>
<summary>專案或內容摘要</summary>
<quality_assessment>程式碼審查或品質評估</quality_assessment>
```

## 9. 測試與品質層

### 9.1 測試案例

```xml
<tests>
  <case id="測試標識符">
    <setup>測試環境準備步驟</setup>
    <asserts>預期結果與驗證標準</asserts>
  </case>
</tests>
```

### 9.2 品質指標

```xml
<metrics>
  <metric type="schema-compliance" target="100%"/>
  <metric type="coverage" target=">=0.9"/>
  <metric type="performance" target="回應時間毫秒"/>
</metrics>
```

**常見指標類型：**
- `schema-compliance`: XML 規範遵循度
- `coverage`: 測試或需求覆蓋率百分比
- `performance`: 回應時間或處理速度閾值

## 10. 協作層

### 10.1 協調協議

```xml
<coordination_protocol>
  <input_requirements>多代理情境下的必要輸入規格</input_requirements>
  <output_format>共享輸出的標準化格式</output_format>
</coordination_protocol>
```

### 10.2 共享輸出位置

```xml
<output_location>共享/輸出/目錄/路徑</output_location>
```

定義需要被多個代理存取的輸出集中位置。

## 11. 配置檔實施指引

### 11.1 Light 配置檔
適用於簡單單一目的代理的最小配置：
- 任務層：角色、目標、基本約束
- 輸入輸出層：僅輸入與輸出
- 簡單線性流程

### 11.2 Standard 配置檔
生產環境的完整框架：
- 除審計要求外的所有層級
- 完整安全與驗證協議
- 全面的上下文與工具定義

### 11.3 Strict 配置檔
強化標準配置檔，包含強制性審計軌跡：

```xml
<audit>執行日誌、風險評估與合規驗證</audit>
<commit message="提交描述" branch="目標分支" signoff="true"/>
```

**提交屬性：**
- `message`: 描述性提交訊息
- `branch`: 目標倉庫分支
- `signoff`: 布林值，表示是否需要正式核准

## 12. 實施範例

### 12.1 完整標準配置檔範例

```xml
<prompt spec-version="1.0" profile="standard">
  <role name="提交分析代理"/>
  <goal>分析 git 提交與 CI/CD 結果以生成結構化 JSON 報告</goal>

  <constraints>
    <item>不得修改 CI 腳本或配置檔案</item>
    <item>輸出必須符合 commit_report 結構定義 v1.0</item>
  </constraints>

  <context>
    <repo-map>原始碼倉庫，排除供應商與建置目錄</repo-map>
    <dependencies>
      Git CLI、CI/CD 系統 API、JSON 結構定義驗證函式庫
    </dependencies>
  </context>

  <tools>
    <tool name="git" kind="command">Git 版本控制操作</tool>
    <tool name="cicd_api" kind="api">CI/CD 系統資料檢索</tool>
  </tools>

  <plan>
    <step id="1" type="read">提取 git 上下文與 CI/CD 資料</step>
    <step id="2" type="analyze">處理變更與測試結果</step>
    <step id="3" type="report">生成結構化 JSON 輸出</step>
  </plan>

  <fast_stop_triggers>
    <trigger id="missing_commit">
      <condition>無可用 git 提交資料</condition>
      <action>immediate_stop</action>
      <o>錯誤：缺少必要的 git 提交資訊</o>
    </trigger>
  </fast_stop_triggers>

  <analysis>內部推理與資料處理</analysis>
  <implementation>JSON 報告生成</implementation>
  <validation>結構定義合規性與資料品質驗證</validation>

  <outputs>
    <final format="json" schema="commit_report@1.0"/>
    <output_location>reports/commit/commit-analysis.json</output_location>
  </outputs>
</prompt>
```

## 13. 驗證要求

### 13.1 結構定義合規性
所有實施必須根據本規範中定義的 XML 結構進行驗證。必要元素必須存在，所有屬性必須使用指定值。

### 13.2 配置檔一致性
代理必須實施其指定配置檔級別的所有必要元素。較高配置檔（strict）包含較低配置檔（light、standard）的所有元素。

### 13.3 輸出格式驗證
最終輸出必須符合宣告的結構定義規格，並能夠交付至指定位置。

## 14. 擴展指引

### 14.1 自訂元素
可在現有層級邊界內新增額外元素，惟不得與核心規範要求衝突。

### 14.2 結構定義演進
未來規範版本應透過 `spec-version` 屬性與先前版本維持向後相容性。

## 15. 實用建議

### 15.1 標籤命名規約
建議採用英文標籤名稱以確保跨國團隊協作的一致性。中文內容應置於標籤內容或屬性值中。

### 15.2 錯誤處理最佳實務
實施時應確保每個安全層級都有適當的錯誤處理機制，特別是在多代理協作環境中。

### 15.3 效能考量
在設計複雜工作流程時，應考慮步驟執行的效能影響，善用 `allow-reorder` 屬性來最佳化執行順序。

---

**規範版本：** 1.0  
**最後更新：** 2025年9月  
**適用範圍：** 多代理 XML 結構與標籤規約