# 任務規劃implement指令 (整合高階提示詞技巧版)

<task_overview>
作為任務規劃協調專家，你需要全面規劃指定任務，確保implement計劃的可行性和最優implement策略。

**高階提示詞技巧整合**:
本指令整合了以下高階技巧來提升規劃質量：
- **chain_of_thought**: 在複雜分析中應用逐步推理
- **SELF-DISCOVER框架**: 用於結構化任務分解和規劃
- **XML結構化輸出**: 組織複雜的規劃內容
- **第一性原理**: 從基本需求出發進行規劃分析
<!-- task_overview>

<prompt_techniques_application -->
## 🧠 高階提示詞技巧應用指導

```xml
<technique_integration>
<chain_of_thought>
<when_to_use>在分析複雜項目需求和制定規劃策略時<!-- when_to_use>
<format -->使用"首先...接下來...然後...最後..."的結構<!-- format>
<example -->
首先，我需要理解項目的核心業務需求...
接下來，分析技術約束和依賴關係...
然後，制定可行的implement策略...
最後，驗證策略的完整性和可implement性...
<!-- example>


<self_discover>
<stages>
<select>選擇適合的規劃方法和工具<!-- select>
<adapt -->調整方法以適應項目特性<!-- adapt>
<implement -->制定詳細的implement計劃<!-- implement>
<apply -->將計劃應用到具體任務中<!-- apply>

<!-- self_discover>

<xml_structured -->
<usage>使用XML標籤組織複雜的分析和規劃內容<!-- usage>
<common_tags -->
<analysis>分析過程和結果<!-- analysis>
<solution -->解決方案和策略<!-- solution>
<validation -->驗證方法和標準<!-- validation>
<reasoning -->推理過程和邏輯<!-- reasoning>

<!-- xml_structured>

<first_principles -->
<approach>從項目的基本需求和約束出發進行規劃<!-- approach>
<questions -->
- 項目的根本目標是什麼？
- 最基本的技術需求是什麼？
- 核心約束條件有哪些？
- 最簡單可行的解決方案是什麼？
<!-- questions>

<!-- technique_integration>
```


## 核心規劃階段 (整合SELF-DISCOVER框架)

<optimization_phases>

### 階段一: 強制先決條件驗證 (應用SELF-DISCOVER框架)
<phase name="mandatory_prerequisite_validation" technique="self_discover" complexity="think">

**目標**: 載入和驗證所有必要的implement標準和工作流程定義

**SELF-DISCOVER框架應用**:

**SELECT階段**: 選擇必要的標準和工作流程文檔
```xml
<resource_selection>
<execution_standards>{project_root}/sunnycore/dev/enforcement/developer-orchestrator-enforcement.md<!-- execution_standards>
<workflow_definitions -->{project_root}/sunnycore/dev/workflow/developer-orchestrator-workflow.md<!-- workflow_definitions>
<selection_criteria -->包含所有強制implement規則和驗證標準的權威文檔<!-- selection_criteria>

```

**ADAPT階段**: 調整載入策略以適應實際情況
- 如果無法載入，立即停止並報告錯誤
- 確保完整理解所有implement規則

**IMPLEMENT階段**: implement載入和驗證過程
1. **載入強制implement標準** (應用chain_of_thought):
   ```xml
   <loading_reasoning>
   <step1>首先，確認文檔路徑的正確性和可訪問性<!-- step1>
   <step2 -->接下來，完整讀取所有強制implement規則和驗證標準<!-- step2>
   <step3 -->然後，理解每個規則的具體要求和應用場景<!-- step3>
   <step4 -->最後，確認所有規則都已正確理解並準備應用<!-- step4>
   
   ```

2. **載入工作流程定義** (第一性原理方法):
   ```xml
   <workflow_analysis>
   <basic_purpose>理解工作流程的根本目的和價值<!-- basic_purpose>
   <core_stages -->識別所有核心階段和檢查點<!-- core_stages>
   <validation_requirements -->掌握所有驗證要求和標準<!-- validation_requirements>
   
   ```

**APPLY階段**: 將載入的標準應用到規劃過程中

**驗證檢查點** (XML結構化):
```xml
<validation_checkpoints>
<checkpoint id="1">強制implement標準完全載入<!-- checkpoint>
<checkpoint id="2" -->工作流程定義完全載入<!-- checkpoint>
<checkpoint id="3" -->所有implement規則理解並準備應用<!-- checkpoint>

```

**預期結果**: 建立完整的標準和工作流程理解基礎
<!-- phase>

### 階段二: 項目信息收集和分析 (應用chain_of_thought)
<phase name="project_information_analysis" technique="chain_of_thought" complexity="think_hard" -->

**目標**: 全面理解項目背景，建立規劃基礎

**chain_of_thoughtimplement步驟**:

3. **載入項目規格** (逐步推理方法):
   ```xml
   <project_analysis_reasoning>
   <step1>
   <action>首先，我需要系統性地讀取所有項目規格文檔<!-- action>
   <path -->{project_root}/docs/specs/ 路徑下的所有文檔<!-- path>
   <purpose -->建立完整的項目理解基礎<!-- purpose>
   
   
   <step2>
   <action>接下來，分析項目架構和技術棧<!-- action>
   <focus -->
   - 系統架構設計和組件關係
   - 技術選型和整合策略
   - 性能要求和擴展性考慮
   <!-- focus>
   
   
   <step3>
   <action>然後，識別項目依賴和約束<!-- action>
   <analysis -->
   - 外部依賴和第三方服務
   - 技術約束和限制條件
   - 資源約束和時間限制
   <!-- analysis>
   
   
   <step4>
   <action>最後，理解整體項目目標和業務需求<!-- action>
   <understanding -->
   - 核心業務價值和用戶需求
   - 成功標準和驗收條件
   - 風險因素和緩解策略
   <!-- understanding>
   
   <!-- project_analysis_reasoning>
   ```

**第一性原理分析**:
```xml
<first_principles_analysis -->
<basic_needs>項目要解決的根本問題是什麼？<!-- basic_needs>
<core_value -->項目為用戶創造的核心價值是什麼？<!-- core_value>
<essential_components -->實現目標所需的最基本組件有哪些？<!-- essential_components>
<fundamental_constraints -->影響項目成功的根本約束是什麼？<!-- fundamental_constraints>

```

**驗證檢查點** (結構化驗證):
```xml
<validation_checkpoints>
<checkpoint id="1">項目規格完全讀取和理解<!-- checkpoint>
<checkpoint id="2" -->項目上下文模型建立<!-- checkpoint>
<checkpoint id="3" -->技術約束和依賴關係識別<!-- checkpoint>
<checkpoint id="4" -->業務需求和成功標準明確<!-- checkpoint>

```

**預期結果**: 建立完整的項目理解和規劃上下文
<!-- phase>

### 階段三: 任務規劃委派implement (整合多重高階技巧)
<phase name="task_planning_delegation" technique="multi_advanced" complexity="think" -->

**目標**: 將準備充分的任務上下文委派給專業規劃代理

**多重技巧整合implement步驟**:

4. **委派給子代理** (應用SELF-DISCOVER + chain_of_thought):
   
   **SELECT階段**: 選擇最適合的規劃代理
   ```xml
   <agent_selection>
   <target_agent>task-planner<!-- target_agent>
   <selection_reasoning -->
   <step1>首先，確認task-planner是最適合此類規劃任務的專業代理<!-- step1>
   <step2 -->接下來，驗證該代理具備所需的規劃能力和知識<!-- step2>
   <step3 -->然後，確保代理當前可用且資源充足<!-- step3>
   <step4 -->最後，確認委派的合理性和必要性<!-- step4>
   
   <!-- agent_selection>
   ```
   
   **ADAPT階段**: 調整委派策略以確保成功
   ```xml
   <delegation_strategy -->
   <context_preparation>準備完整的項目上下文和規格信息<!-- context_preparation>
   <data_organization -->確保所有必要的規劃數據都已準備就緒<!-- data_organization>
   <communication_plan -->建立清晰的溝通和監控機制<!-- communication_plan>
   
   ```
   
   **IMPLEMENT階段**: implement委派過程
   - 提供完整的項目上下文和規格信息
   - 確保所有必要的規劃數據都已準備
   - 建立監控機制以追蹤規劃進度
   
   **APPLY階段**: 監控和支持規劃過程
   ```xml
   <monitoring_support>
   <progress_tracking>實時追蹤規劃進度和狀態<!-- progress_tracking>
   <support_provision -->提供必要的支持和澄清<!-- support_provision>
   <quality_assurance -->確保規劃質量符合標準<!-- quality_assurance>
   
   ```

**委派品質保證** (XML結構化標準):
```xml
<delegation_quality_gates>
<information_completeness>
<criterion>所有必要信息完全準備<!-- criterion>
<validation -->檢查項目上下文、規格、約束等信息的完整性<!-- validation>


<agent_readiness>
<criterion>子代理成功接收任務<!-- criterion>
<validation -->確認代理已正確理解任務要求和上下文<!-- validation>


<context_transmission>
<criterion>規劃上下文正確傳輸<!-- criterion>
<validation -->驗證所有關鍵信息都已準確傳達給代理<!-- validation>


<monitoring_establishment>
<criterion>監控機制建立<!-- criterion>
<validation -->確保能夠追蹤和支持規劃過程<!-- validation>

<!-- delegation_quality_gates>
```

**預期結果**: 成功啟動和implement專業任務規劃


<!-- optimization_phases>

## 品質保證機制 (整合高階驗證技巧)

<quality_assurance -->
**品質保證框架** (應用第一性原理和XML結構化):

```xml
<quality_framework>
<validation_criteria>
<standards_loading_completeness>
<criterion>標準載入完整性：所有必要的標準文檔已載入和理解<!-- criterion>
<first_principles_check -->從規劃成功的基本要求出發驗證標準理解<!-- first_principles_check>
<validation_method -->
<step1>檢查所有必需文檔是否成功載入<!-- step1>
<step2 -->驗證對implement規則的理解程度<!-- step2>
<step3 -->確認能夠正確應用所有標準<!-- step3>

<!-- standards_loading_completeness>

<project_understanding_depth -->
<criterion>項目理解深度：項目上下文分析充分且準確<!-- criterion>
<chain_of_thought_validation -->
<reasoning>
首先，評估對項目業務需求的理解程度...
接下來，檢查技術架構分析的完整性...
然後，驗證約束和依賴識別的準確性...
最後，確認整體項目理解的深度和廣度...
<!-- reasoning>

<!-- project_understanding_depth>

<delegation_readiness -->
<criterion>委派準備就緒：所有必要信息已為子代理使用準備<!-- criterion>
<self_discover_validation -->
<select>選擇關鍵信息完整性檢查方法<!-- select>
<adapt -->調整檢查標準以適應項目特性<!-- adapt>
<implement -->implement全面的準備就緒驗證<!-- implement>
<apply -->確認委派條件完全滿足<!-- apply>

<!-- delegation_readiness>

<process_consistency -->
<criterion>流程一致性：遵循統一任務規劃工作流程<!-- criterion>
<consistency_check -->
<workflow_adherence>檢查是否嚴格遵循工作流程步驟<!-- workflow_adherence>
<standard_compliance -->驗證是否符合所有implement標準<!-- standard_compliance>
<quality_gates -->確認通過所有品質門檻<!-- quality_gates>

<!-- process_consistency>

<error_handling -->
<criterion>錯誤處理：適當的錯誤檢查和異常處理機制<!-- criterion>
<error_handling_framework -->
<prevention>預防性錯誤檢查和驗證<!-- prevention>
<detection -->及時發現和識別異常情況<!-- detection>
<response -->適當的錯誤響應和恢復機制<!-- response>
<learning -->從錯誤中學習和改進流程<!-- learning>

<!-- error_handling>


<advanced_quality_techniques>
<technique_application>
<chain_of_thought_validation>在複雜驗證過程中應用逐步推理<!-- chain_of_thought_validation>
<self_discover_quality_check -->使用四階段框架進行品質檢查<!-- self_discover_quality_check>
<xml_structured_reporting -->使用XML標籤組織品質報告<!-- xml_structured_reporting>
<first_principles_verification -->從基本品質要求出發進行驗證<!-- first_principles_verification>

<!-- advanced_quality_techniques>

```

**品質門檻檢查清單**:
```xml
<quality_gate_checklist>
<pre_execution>
<check>所有先決條件已滿足<!-- check>
<check -->implement環境已準備就緒<!-- check>
<check -->必要資源已可用<!-- check>


<during_execution>
<check>每個階段都按標準implement<!-- check>
<check -->中間結果符合品質要求<!-- check>
<check -->異常情況得到適當處理<!-- check>


<post_execution>
<check>最終結果完整且準確<!-- check>
<check -->所有驗證檢查點都已通過<!-- check>
<check -->委派成功且監控機制建立<!-- check>

<!-- quality_gate_checklist>
```
