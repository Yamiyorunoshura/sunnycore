---
category: dev
description: 統一架構系統workflows文檔
last_updated: '2025-09-03'
name: unified-task-planning-workflow
prompt_techniques:
- chain_of_thought
- self_discover
- xml_structured
version: '1.0'
---

# 統一任務規劃工作流程 (整合高階提示詞技巧版)

<prompt_techniques_integration>
本工作流程整合了以下高階提示詞技巧：
- **SELF-DISCOVER框架**: 用於複雜任務的結構化分解
- **chain_of_thought**: 確保每個步驟的邏輯性和可追溯性
- **xml_structured_output**: 組織複雜的規劃內容，提高可讀性
- **第一性原理**: 從基本需求出發進行任務分析
<!-- prompt_techniques_integration>

<enforcement -->
## 🔄 工作流程Todo清單創建 (整合chain_of_thought)

### 📋 implement前必要準備

**重要提醒**: 在開始implement任何工作流程步驟前，必須使用chain_of_thought方式創建todo清單來組織這些步驟。

**創建過程 (應用SELF-DISCOVER框架)**:

**SELECT階段**: 選擇適合的分析模組
1. **工作流程結構分析模組** - 仔細閱讀整個工作流程文件，識別所有階段、步驟和任務
2. **關鍵任務提取模組** - 將每個階段的核心任務轉換為具體的todo項目
3. **優先級設定模組** - 根據任務重要性和依賴關係設定優先級

**ADAPT階段**: 調整分析方法
4. **Todo清單創建** - 使用`todo_write`工具創建包含所有步驟的結構化todo清單
5. **implement和更新** - 按照todo清單順序implement任務，及時更新狀態

### 📝 Todo清單要求 (XML結構化標準)
```xml
<todo_requirements>
<coverage>每個主要階段都應有對應的todo項目<!-- coverage>
<verification_points -->關鍵驗證檢查點必須包含在todo清單中<!-- verification_points>
<priorities -->設定合理優先級，確保依賴關係得到尊重<!-- priorities>
<status_management -->implement過程中及時更新todo狀態 (pending → in_progress → completed)<!-- status_management>
<uniqueness -->同一時間只能有一個任務處於`in_progress`狀態<!-- uniqueness>
<completeness -->只有在任務完全完成時才標記為`completed`<!-- completeness>

```
<!-- enforcement>

---

<task_overview -->
作為任務規劃專家，你需要對指定任務進行全面而結構化的規劃，確保implement計劃的可行性、完整性和最優implement策略。

**chain_of_thought啟動**:
在開始任何規劃工作前，我會：
1. 首先理解任務的核心要求和約束條件
2. 分析任務的複雜度和所需資源
3. 制定結構化的分析和implement計劃
4. 持續驗證每個步驟的合理性和完整性
<!-- task_overview>

## 核心規劃階段 (整合SELF-DISCOVER框架)

<optimization_phases -->

### 階段 1: 項目規格理解和分析 (整合SELF-DISCOVER)
<phase name="project_specification_analysis" technique="self_discover" complexity="think_hard">

**目標**: 全面理解項目需求、規格和架構設計

**SELF-DISCOVER框架應用**:

**SELECT階段**: 選擇適合的分析模組
- 需求分析模組: 用於理解業務需求和功能規格
- 架構理解模組: 用於分析系統設計和組件關係
- 約束識別模組: 用於識別技術限制和依賴關係

**ADAPT階段**: 調整分析方法
- 根據項目複雜度調整分析深度
- 適應特定技術棧的要求
- 考慮項目特定的約束條件

**IMPLEMENT階段**: implement結構化分析
1. **項目規格載入** (應用chain_of_thought):
   ```xml
   <analysis>
   首先，讓我理解這個項目的核心業務需求...
   - 完整閱讀 `{project_root}/docs/specs/` 路徑下的所有文檔
   - 分析項目業務需求和功能規格
   - 識別技術約束和依賴關係
   - 建立項目上下文理解模型
   - 提取關鍵設計決策和原則
   <!-- analysis>
   ```

2. **架構文檔分析** (應用第一性原理):
   ```xml
   <architecture_analysis -->
   從系統的基本組成要素出發...
   - 詳細閱讀 `{project_root}/docs/architecture/` 路徑下的所有文檔
   - 理解系統架構設計和組件關係
   - 分析技術棧選擇和整合策略
   - 識別架構約束和性能要求
   - 建立整體系統架構視圖
   <!-- architecture_analysis>
   ```

**APPLY階段**: 應用分析結果
- 建立完整的項目理解基礎
- 為後續任務規劃提供準確的上下文支持

**驗證檢查點** (XML結構化):
```xml
<validation_checkpoints -->
<checkpoint id="1">項目需求已完全理解並記錄<!-- checkpoint>
<checkpoint id="2" -->架構設計已全面分析並掌握<!-- checkpoint>
<checkpoint id="3" -->技術約束和依賴關係已識別<!-- checkpoint>
<checkpoint id="4" -->項目上下文模型已建立<!-- checkpoint>

```

**預期結果**: 建立完整的項目理解基礎，為後續任務規劃提供準確的上下文支持
<!-- phase>

### 階段 2: 任務解析和分解 (整合chain_of_thought)
<phase name="task_decomposition" technique="chain_of_thought" complexity="think_hard" -->

**目標**: 精確解析和分解指定任務及其子任務

**chain_of_thoughtimplement步驟**:

3. **任務文件解析** (逐步推理方法):
   ```xml
   <reasoning_chain>
   <step1>首先，讓我理解任務文件的整體結構...<!-- step1>
   <step2 -->接下來，我將定位與 `{task_id}` 匹配的主任務 (如: 1, 2, 3)<!-- step2>
   <step3 -->然後，提取該任務下的所有子任務 (如: 1.1, 1.2, 1.3)<!-- step3>
   <step4 -->收集每個任務和子任務的無序列表項目<!-- step4>
   <step5 -->最後，分析任務間的依賴關係和implement順序<!-- step5>
   
   ```

4. **任務粒度分解** (應用第一性原理):
   ```xml
   <decomposition_analysis>
   <principle>從任務的基本組成要素出發進行分解<!-- principle>
   <step1 -->將無序列表項目轉換為具體的功能需求 (F-1, F-2...)<!-- step1>
   <step2 -->識別非功能性需求 (N-1, N-2...)<!-- step2>
   <step3 -->為每個需求定義驗收標準和衡量標準<!-- step3>
   <step4 -->建立任務implement的優先級排序<!-- step4>
   
   ```

**驗證檢查點** (結構化驗證):
```xml
<validation_checkpoints>
<checkpoint id="1">指定任務和子任務已正確識別<!-- checkpoint>
<checkpoint id="2" -->任務需求已分解為最小可implement單元<!-- checkpoint>
<checkpoint id="3" -->功能性和非功能性需求已清晰分類<!-- checkpoint>
<checkpoint id="4" -->驗收標準已完整定義<!-- checkpoint>

```

**預期結果**: 生成結構化、可implement的任務分解結果，為implement計劃奠定基礎
<!-- phase>

### 階段 3: implement計劃生成和輸出 (整合多重高階技巧)
<phase name="implementation_plan_generation" technique="multi_advanced" complexity="think_harder" -->

**目標**: 基於模板生成完整的implement計劃文檔

**多重技巧整合implement步驟**:

5. **模板載入和理解** (應用chain_of_thought):
   ```xml
   <template_analysis>
   <step1>首先，讓我理解模板的整體結構...<!-- step1>
   <reasoning -->閱讀模板 `{project_root}/sunnycore/dev/templates/implementation-plan-tmpl.yaml`<!-- reasoning>
   <step2 -->接下來，分析模板結構和必需字段要求<!-- step2>
   <step3 -->然後，分析輸出格式規範和品質標準<!-- step3>
   <step4 -->最後，準備符合模板要求的規劃內容<!-- step4>
   
   ```

6. **計劃內容填充** (應用SELF-DISCOVER框架):
   ```xml
   <content_filling_process>
   <select>選擇適合的內容組織模組<!-- select>
   <adapt -->調整內容以適應模板結構<!-- adapt>
   <implement -->
   - 填入項目元數據和上下文信息
   - 將功能性和非功能性需求映射到模板結構
   - 完成implement步驟和驗證機制
   - 確保內容完整性和一致性
   <!-- implement>
   <apply -->應用填充結果生成最終計劃<!-- apply>
   
   ```

7. **文檔輸出和格式化** (xml_structured_output):
   ```xml
   <document_generation>
   <conversion>將完成的計劃轉換為Markdown格式<!-- conversion>
   <output_path -->`{project_root}/docs/implementation-plan/` 路徑<!-- output_path>
   <naming_convention -->使用標準化文件命名: `{task_id}-plan.md` (如: 1-plan.md, 2-plan.md)<!-- naming_convention>
   <final_validation -->implement最終格式和內容驗證<!-- final_validation>
   
   ```

**品質門檻驗證** (標準化檢查點):
```xml
<quality_gates>
<gate id="template_validation">
<criterion>模板已正確載入和理解<!-- criterion>
<status -->待驗證<!-- status>

<gate id="content_completeness">
<criterion>所有必需字段已完整填寫<!-- criterion>
<status -->待驗證<!-- status>

<gate id="specification_compliance">
<criterion>計劃內容符合模板規範要求<!-- criterion>
<status -->待驗證<!-- status>

<gate id="output_success">
<criterion>文檔已成功輸出到指定路徑<!-- criterion>
<status -->待驗證<!-- status>

<gate id="naming_compliance">
<criterion>文件命名符合標準規範<!-- criterion>
<status -->待驗證<!-- status>

<!-- quality_gates>
```

**預期結果**: 生成高品質、結構化的implement計劃文檔，為任務implement提供完整指導


<!-- optimization_phases>

## 錯誤處理和品質保證 (整合高階驗證技巧)

<quality_assurance -->

### 錯誤處理機制 (應用chain_of_thought)
<error_handling>
```xml
<error_types>
<file_access_error>
<description>當無法讀取指定路徑的文件時<!-- description>
<response -->記錄錯誤並提供替代解決方案<!-- response>
<reasoning -->首先分析錯誤原因，然後制定修復策略<!-- reasoning>


<format_parsing_error>
<description>當文件格式不符合預期時<!-- description>
<response -->implement錯誤報告並嘗試修復<!-- response>
<reasoning -->逐步分析格式問題，提供具體修正建議<!-- reasoning>


<content_validation_failure>
<description>當規劃內容不完整時<!-- description>
<response -->標記缺失項目並請求補充<!-- response>
<reasoning -->系統性檢查所有必需字段，識別具體缺失內容<!-- reasoning>


<output_path_error>
<description>當目標路徑不存在時<!-- description>
<response -->自動創建目錄結構<!-- response>
<reasoning -->分析路徑結構，逐級創建必要目錄<!-- reasoning>

<!-- error_types>
```


### 驗證標準 (XML結構化品質標準)
<validation_criteria>
```xml
<quality_standards>
<completeness_verification>
<criterion>所有必要的項目規格和架構文檔已載入和分析<!-- criterion>
<method -->系統性檢查所有必需文檔的存在性和完整性<!-- method>
<threshold -->100%覆蓋率<!-- threshold>


<accuracy_verification>
<criterion>任務解析結果與原始需求一致<!-- criterion>
<method -->逐項對比解析結果與源需求<!-- method>
<threshold -->零差異容忍<!-- threshold>


<structural_verification>
<criterion>生成的計劃符合模板規範和格式要求<!-- criterion>
<method -->模板結構對照檢查<!-- method>
<threshold -->所有必需字段完整填寫<!-- threshold>


<executability_verification>
<criterion>計劃內容具體、清晰、可操作<!-- criterion>
<method -->可implement性評估和模糊性檢測<!-- method>
<threshold -->所有步驟都有明確的implement指導<!-- threshold>


<traceability_verification>
<criterion>計劃元素與源需求之間存在清晰對應關係<!-- criterion>
<method -->需求追溯矩陣驗證<!-- method>
<threshold -->每個計劃項目都能追溯到具體需求<!-- threshold>


<consistency_verification>
<criterion>術語使用和風格保持統一<!-- criterion>
<method -->術語一致性檢查和風格分析<!-- method>
<threshold -->術語使用100%符合統一標準<!-- threshold>

<!-- quality_standards>
```


### 品質門檻檢查點 (標準化驗證流程)
```xml
<quality_gate_process>
<pre_execution_checks>
<check>項目上下文完整性驗證<!-- check>
<check -->任務需求清晰度評估<!-- check>
<check -->模板可用性確認<!-- check>


<mid_execution_checks>
<check>階段性輸出品質驗證<!-- check>
<check -->進度與計劃一致性檢查<!-- check>
<check -->中間結果準確性驗證<!-- check>


<post_execution_checks>
<check>最終輸出完整性驗證<!-- check>
<check -->格式規範符合性檢查<!-- check>
<check -->可implement性最終確認<!-- check>

<!-- quality_gate_process>
```



## 輸出格式規範 (XML結構化標準)

<output_format>
```xml
<format_specifications>
<file_path>`{project_root}/docs/implementation-plan/{task_id}-plan.md`<!-- file_path>

<naming_conventions -->
<example task="1">1-plan.md<!-- example>
<example task="2" -->2-plan.md<!-- example>
<example task="3" -->3-plan.md<!-- example>
<pattern -->{task_id}-plan.md<!-- pattern>


<content_structure>
<requirement>嚴格遵循 `implementation-plan-tmpl.yaml` 模板規範<!-- requirement>
<completeness -->確保所有必需字段完整填寫<!-- completeness>
<specificity -->避免使用"根據需要"或"待定"等通用陳述<!-- specificity>
<traceability -->每個計劃項目都應能追溯到具體需求<!-- traceability>


<quality_requirements>
<clarity>所有描述都應清晰具體<!-- clarity>
<actionability -->每個步驟都應可implement<!-- actionability>
<measurability -->驗收標準應可衡量<!-- measurability>
<consistency -->術語使用應保持一致<!-- consistency>


<advanced_techniques_integration>
<chain_of_thought>在複雜分析中應用逐步推理<!-- chain_of_thought>
<self_discover -->在任務分解中使用SELF-DISCOVER框架<!-- self_discover>
<xml_structured -->使用XML標籤組織複雜內容<!-- xml_structured>
<first_principles -->從基本原理出發進行分析<!-- first_principles>

<!-- format_specifications>
```


## 高階提示詞技巧應用指南

<advanced_prompt_techniques>
```xml
<technique_application_guide>
<chain_of_thought>
<when_to_use>處理複雜邏輯問題和多步驟分析時<!-- when_to_use>
<implementation -->
- 在分析前明確說明推理步驟
- 使用"首先...接下來...然後...最後..."的結構
- 在每個步驟後驗證邏輯合理性
<!-- implementation>


<self_discover_framework>
<when_to_use>面對複雜任務需要結構化分解時<!-- when_to_use>
<stages -->
<select>選擇適合的推理模組和方法<!-- select>
<adapt -->調整方法以適應具體情況<!-- adapt>
<implement -->制定詳細的implement計劃<!-- implement>
<apply -->將計劃應用到具體實例<!-- apply>

<!-- self_discover_framework>

<xml_structured_output -->
<when_to_use>組織複雜信息和提高可讀性時<!-- when_to_use>
<best_practices -->
- 使用語義化的標籤名稱
- 保持標籤結構的一致性
- 適當嵌套以反映信息層次
<!-- best_practices>


<first_principles_thinking>
<when_to_use>需要從根本上理解和解決問題時<!-- when_to_use>
<approach -->
- 識別問題的基本組成要素
- 質疑現有假設和慣例
- 從基礎原理重新構建解決方案
<!-- approach>

<!-- technique_application_guide>
```
