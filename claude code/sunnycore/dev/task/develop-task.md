# 開發任務implement指令 (整合高階提示詞技巧版)

<task_overview>
當此指令被調用時，你將作為developerimplement全面的開發任務。

**高階提示詞技巧整合**:
本指令整合了以下高階技巧來提升開發質量和效率：
- **chain_of_thought**: 在複雜開發決策中應用逐步推理
- **SELF-DISCOVER框架**: 用於結構化問題解決和開發流程
- **XML結構化輸出**: 組織複雜的開發記錄和分析
- **第一性原理**: 從基本需求出發進行開發決策
<!-- task_overview>

<advanced_development_principles -->
## 🧠 高階開發原則 (第一性原理指導)

```xml
<development_philosophy>
<first_principles_approach>
<basic_need>滿足用戶的根本需求<!-- basic_need>
<core_value -->創造真正有價值的功能<!-- core_value>
<essential_quality -->確保代碼的基本品質和可維護性<!-- essential_quality>
<fundamental_constraints -->遵循項目的基本約束和標準<!-- fundamental_constraints>


<chain_of_thought_development>
<reasoning_pattern>
在每個開發決策前應用chain_of_thought：
<step1>首先，理解要解決的具體問題<!-- step1>
<step2 -->接下來，分析可能的解決方案<!-- step2>
<step3 -->然後，評估每個方案的優缺點<!-- step3>
<step4 -->最後，選擇最佳方案並implement<!-- step4>

<!-- chain_of_thought_development>

<self_discover_problem_solving -->
<framework_application>
在遇到複雜開發問題時使用SELF-DISCOVER框架：
<select>選擇適合的開發方法和工具<!-- select>
<adapt -->調整方法以適應具體情況<!-- adapt>
<implement -->制定詳細的implement計劃<!-- implement>
<apply -->implement計劃並validate結果<!-- apply>

<!-- self_discover_problem_solving>

```
<!-- advanced_development_principles>

## Execution Steps

<stage name="強制先決條件validate" number="1" critical="true" technique="self_discover" -->
<description>載入和validate所有必要的implement標準和工作流程定義<!-- description>

**SELF-DISCOVER框架應用**:

<execution_actions -->
**SELECT階段**: 選擇必要的標準和工作流程文檔
```xml
<resource_identification>
<execution_standards>{project_root}/sunnycore/dev/enforcement/developer-orchestrator-enforcement.md<!-- execution_standards>
<workflow_definitions -->{project_root}/sunnycore/dev/workflow/developer-orchestrator-workflow.md<!-- workflow_definitions>
<selection_reasoning -->這些文檔包含所有強制implement規則和validate標準<!-- selection_reasoning>

```

**ADAPT階段**: 調整載入策略以確保成功
- 如果無法載入，立即停止並報告錯誤
- 建立錯誤處理和恢復機制

**IMPLEMENT階段**: implement載入和validate過程
1. **載入強制implement標準** (chain_of_thought):
   ```xml
   <loading_reasoning>
   <step1>首先，確認文檔路徑的正確性和可訪問性<!-- step1>
   <step2 -->接下來，完整讀取所有強制implement規則和validate標準<!-- step2>
   <step3 -->然後，理解每個規則的具體要求和應用場景<!-- step3>
   <step4 -->最後，確認所有規則都已正確理解並準備應用<!-- step4>
   
   ```

2. **載入工作流程定義** (第一性原理):
   ```xml
   <workflow_understanding>
   <basic_purpose>理解工作流程的根本目的<!-- basic_purpose>
   <core_stages -->掌握所有階段、檢查點和validate要求<!-- core_stages>
   <application_readiness -->確保能夠正確應用到開發過程中<!-- application_readiness>
   
   ```

**APPLY階段**: 將載入的標準應用到開發過程中
<!-- execution_actions>

<validation_checkpoints -->
```xml
<checkpoints>
<checkpoint id="1">強制implement標準完全載入<!-- checkpoint>
<checkpoint id="2" -->工作流程定義完全載入<!-- checkpoint>
<checkpoint id="3" -->所有implement規則理解並準備應用<!-- checkpoint>

```
<!-- validation_checkpoints>


<stage name="項目上下文理解" number="2" critical="true" technique="chain_of_thought">
<description>建立完整的項目上下文模型和implement計劃validate<!-- description>

**chain_of_thoughtimplement**:

<execution_actions -->
3. **項目規格載入** (逐步推理方法):
   ```xml
   <project_loading_reasoning>
   <step1>
   <action>首先，我需要系統性地讀取所有項目規格文檔<!-- action>
   <path -->{project_root}/docs/specs/ 路徑下的所有文檔<!-- path>
   <purpose -->建立完整的項目理解基礎<!-- purpose>
   
   
   <step2>
   <action>接下來，理解項目需求、規格和架構設計<!-- action>
   <focus -->
   - 業務需求和功能規格
   - 系統架構和技術設計
   - 性能要求和品質標準
   <!-- focus>
   
   
   <step3>
   <action>然後，建立完整的項目上下文模型<!-- action>
   <components -->
   - 技術棧和依賴關係
   - 約束條件和限制
   - 成功標準和驗收條件
   <!-- components>
   
   
   <step4>
   <action>最後，識別關鍵依賴和約束<!-- action>
   <analysis -->
   - 外部依賴和整合點
   - 技術約束和限制
   - 時間和資源約束
   <!-- analysis>
   
   <!-- project_loading_reasoning>
   ```

4. **implement計劃validate** (SELF-DISCOVER框架):
   ```xml
   <plan_validation_framework -->
   <select>選擇適合的計劃validate方法<!-- select>
   <adapt -->調整validate標準以適應項目特性<!-- adapt>
   <implement -->
   - 確認 `{project_root}/docs/implementation-plan/{task_id}-plan.md` 存在且可讀
   - **關鍵檢查點**: 如果implement計劃不存在，立即停止並通知用戶需要先implement規劃階段
   - validate計劃完整性和可implement性
   <!-- implement>
   <apply -->將validate結果應用到開發過程中<!-- apply>
   
   ```

**第一性原理validate**:
```xml
<first_principles_validation>
<basic_completeness>計劃是否包含實現目標所需的基本要素？<!-- basic_completeness>
<core_feasibility -->計劃是否在技術和資源約束下可行？<!-- core_feasibility>
<essential_clarity -->計劃是否足夠清晰以指導實際開發？<!-- essential_clarity>

```
<!-- execution_actions>

<validation_checkpoints -->
```xml
<checkpoints>
<checkpoint id="1">項目規格完全理解<!-- checkpoint>
<checkpoint id="2" -->項目上下文模型建立<!-- checkpoint>
<checkpoint id="3" -->implement計劃存在且格式正確<!-- checkpoint>
<checkpoint id="4" -->計劃內容完整且可implement<!-- checkpoint>

```
<!-- validation_checkpoints>


<stage name="開發implement" number="3" critical="true" technique="multi_advanced">
<description>嚴格按照工作流程implement開發工作<!-- description>

**多重高階技巧整合implement**:

<execution_actions -->
5. **工作流程implement** (整合所有高階技巧):

   **chain_of_thought指導的implement過程**:
   ```xml
   <execution_reasoning>
   <step1>
   <action>首先，我需要按照載入的工作流程文檔嚴格implement開發工作<!-- action>
   <approach -->遵循所有階段順序和檢查點要求<!-- approach>
   
   
   <step2>
   <action>接下來，確保每個validate點都通過後再繼續<!-- action>
   <quality_control -->建立嚴格的品質控制機制<!-- quality_control>
   
   
   <step3>
   <action>然後，記錄所有關鍵決策和implement細節<!-- action>
   <documentation -->維護完整的開發追蹤記錄<!-- documentation>
   
   
   <step4>
   <action>最後，持續validate開發結果符合計劃要求<!-- action>
   <validation -->確保開發質量和進度符合預期<!-- validation>
   
   <!-- execution_reasoning>
   ```

   **SELF-DISCOVER框架應用於開發過程**:
   ```xml
   <development_framework -->
   <select>
   - 選擇適合的開發方法和工具
   - 識別最佳的implement策略
   - 確定關鍵的技術決策點
   <!-- select>
   
   <adapt -->
   - 調整開發方法以適應項目特性
   - 根據實際情況優化implement策略
   - 適應技術約束和資源限制
   <!-- adapt>
   
   <implement -->
   - 制定詳細的開發implement計劃
   - 建立清晰的里程碑和檢查點
   - 設置品質保證和validate機制
   <!-- implement>
   
   <apply -->
   - implement開發計劃並監控進度
   - 應用品質標準和最佳實踐
   - 持續改進和優化開發過程
   <!-- apply>
   
   ```

   **XML結構化開發記錄**:
   ```xml
   <development_record>
   <decisions>記錄所有關鍵技術決策和理由<!-- decisions>
   <implementations -->詳細記錄implement過程和方法<!-- implementations>
   <validations -->記錄所有validate結果和品質檢查<!-- validations>
   <issues -->記錄遇到的問題和解決方案<!-- issues>
   <improvements -->記錄改進建議和優化機會<!-- improvements>
   
   ```

   **第一性原理指導的開發決策**:
   ```xml
   <decision_principles>
   <user_value>每個開發決策都應考慮對用戶價值的影響<!-- user_value>
   <technical_soundness -->確保技術決策基於可靠的工程原理<!-- technical_soundness>
   <maintainability -->優先考慮代碼的長期可維護性<!-- maintainability>
   <simplicity -->選擇最簡單可行的解決方案<!-- simplicity>
   
   ```
<!-- execution_actions>

<validation_checkpoints -->
```xml
<advanced_checkpoints>
<workflow_compliance>
<criterion>所有工作流程階段按順序implement<!-- criterion>
<validation_method -->使用chain_of_thoughtvalidate每個階段的完成度<!-- validation_method>


<checkpoint_validation>
<criterion>每個檢查點都通過validate<!-- criterion>
<validation_method -->應用SELF-DISCOVER框架確保validate的全面性<!-- validation_method>


<documentation_completeness>
<criterion>關鍵決策和implement細節已記錄<!-- criterion>
<validation_method -->使用XML結構化格式組織和validate記錄完整性<!-- validation_method>


<quality_assurance>
<criterion>開發結果符合第一性原理要求<!-- criterion>
<validation_method -->從基本品質要求出發validate開發成果<!-- validation_method>

<!-- advanced_checkpoints>
```

<!-- stage>

<stage name="Write Development Log" number="4" critical="true" -->
<description>Write development log and record all key decisions and implementation details<!-- description>

<execution_actions -->
6. **Development Log Writing**: Write development log and record all key decisions and implementation details
   - Read the `development execution` stage from `Users/tszkinlai/Coding/cursor-claude/core/dev/templates/dev-note.md`
   - Write development log to `{project_root}/docs/dev-note/{task_id}`(e.g.`1`, `2`, `3`...)-dev-note.md` (e.g.`1-dev-note.md`, `2-dev-note.md`, `3-dev-note.md`...)
   - Development log must contain all key decisions and implementation details
<!-- execution_actions>

<validation_checkpoints -->
- [ ] Development log written
- [ ] Development log records all key decisions and implementation details
<!-- validation_checkpoints>


<critical_execution_principles>
- **All development work must be based on validated implementation plans**
- **Strictly follow all requirements in mandatory execution standards**
- **Ensure consistency with project specifications and architecture design**
- **Maintain complete development tracking records**
<!-- critical_execution_principles>

<failure_handling -->
<scenario type="Prerequisites Failure">
Immediately stop, report specific missing files or conditions
<!-- scenario>

<scenario type="Plan Missing" -->
Stop development, guide user to execute `*plan-task {task_id}`(e.g.`1`, `2`, `3`...)` command first
<!-- scenario>

<scenario type="Workflow Interruption" -->
Record interruption point, provide recovery guidance
<!-- scenario>
