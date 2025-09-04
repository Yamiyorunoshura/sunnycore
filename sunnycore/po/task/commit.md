# Commit Task Specification

## Task Overview
協助完成軟體開發過程中文檔（README、CHANGELOG、specs 等）的編輯、更新與合規驗證任務。

## Core Objectives
### Primary Goal (主要目標)
- **任務驅動**: 依據 commit-workflow.md、commit-enforcement.md XML 規範驅動文檔編輯與更新
- **代理架構**: 最多 5 個平行 commit-agents，共用同一規範，分工並行，最後收斂結果
- **快停策略**: 若規範或文件缺失、CI/CD 失敗，立即產出「最小可行輸出」並退出

### Success Criteria (成功標準)
1. **文檔完整性**: README.md、CHANGELOG.md 依模板規範完整更新
2. **合規驗證**: 通過 commit-enforcement.md 所有 XML 規範檢查
3. **CI/CD 狀態**: 驗證 CI/CD 流程成功或產出失敗原因報告
4. **規格同步**: requirements/design/task specs 與實際開發狀態同步

## Agent Architecture (代理架構)
### Parallel Agent Distribution (平行代理分配)
```xml
<parallel_agents>
  <agent id="commit-parser" role="解析與上下文分析">
    <responsibility>解析 commit 訊息、分析變更內容、建立上下文</responsibility>
    <output_format>JSON: 變更分析報告</output_format>
  </agent>
  
  <agent id="document-updater" role="文檔更新實作">
    <responsibility>依據模板更新 README.md、CHANGELOG.md</responsibility>
    <output_format>JSON: 文檔更新結果</output_format>
  </agent>
  
  <agent id="compliance-validator" role="合規品質驗證">
    <responsibility>執行 commit-enforcement.md 規範檢查</responsibility>
    <output_format>JSON: 合規驗證報告</output_format>
  </agent>
  
  <agent id="cicd-monitor" role="CI/CD 狀態監控">
    <responsibility>驗證 CI/CD 流程狀態，產出失敗報告</responsibility>
    <output_format>JSON: CI/CD 狀態報告</output_format>
  </agent>
  
  <agent id="specs-synchronizer" role="規格同步稽核">
    <responsibility>同步 specs 與實際開發狀態，準備重開發</responsibility>
    <output_format>JSON: 規格同步報告</output_format>
  </agent>
</parallel_agents>
```

### Convergence Strategy (收斂策略)
```xml
<convergence_framework>
  <barrier_check>
    <file_existence>驗證必要文件與模板存在性</file_existence>
    <template_validation>檢查模板結構完整性</template_validation>
    <fast_stop_triggers>快停條件觸發檢查</fast_stop_triggers>
  </barrier_check>
  
  <result_merging>
    <severity_matrix>依嚴重度矩陣仲裁衝突結果</severity_matrix>
    <consensus_building>建立共識並產出最終文檔</consensus_building>
    <minimal_viable_output>快停時產出最小可行結果</minimal_viable_output>
  </result_merging>
</convergence_framework>
```

## Workflow Integration (工作流整合)
### Input Requirements (輸入需求)
1. **Git Commit Context**: 當前 commit 訊息、變更文件列表、差異內容
2. **Project Documentation**: 現有 README.md、CHANGELOG.md、specs 文檔
3. **CI/CD Status**: 當前 CI/CD 流程執行狀態
4. **Enforcement Rules**: commit-enforcement.md XML 規範內容

### Processing Phases (處理階段)
```xml
<processing_workflow>
  <phase1 name="Context Analysis">
    <action>解析 commit 上下文與變更內容</action>
    <validation>檢查必要文件存在性</validation>
    <fast_stop_condition>缺失 commit-enforcement.md</fast_stop_condition>
  </phase1>
  
  <phase2 name="Parallel Execution">
    <action>5個 agent 平行執行各自任務</action>
    <validation>Barrier 檢查文件與模板</validation>
    <fast_stop_condition>關鍵模板缺失</fast_stop_condition>
  </phase2>
  
  <phase3 name="Result Convergence">
    <action>收斂 JSON 結果，仲裁衝突</action>
    <validation>合規檢查與品質驗證</validation>
    <fast_stop_condition>嚴重合規失敗</fast_stop_condition>
  </phase3>
  
  <phase4 name="Document Output">
    <action>產出最終文檔更新或失敗報告</action>
    <validation>最終品質確認</validation>
    <fast_stop_condition>無法產出有效結果</fast_stop_condition>
  </phase4>
</processing_workflow>
```

### Output Requirements (輸出需求)
#### Success Output (成功輸出)
1. **Updated README.md**: 依據 README 模板規範更新
2. **Updated CHANGELOG.md**: 依據 CHANGELOG 模板規範更新  
3. **Compliance Report**: commit-enforcement.md 合規驗證報告
4. **CI/CD Status Report**: 流程執行狀態確認

#### Failure Output (失敗輸出)
1. **CI/CD Failure Report**: 詳細失敗原因分析
2. **Specs Update Preparation**: requirements/design/task specs 更新準備
3. **Remediation Plan**: 重開發所需的修正計劃
4. **Minimal Viable Output**: 快停時的最小可行結果

## Quality Standards (品質標準)
### Compliance Framework (合規框架)
```xml
<quality_gates>
  <documentation_quality>
    <requirement>README.md 必須包含所有必要章節</requirement>
    <requirement>CHANGELOG.md 必須遵循語義化版本規範</requirement>
    <requirement>模板填充率達 95% 以上</requirement>
  </documentation_quality>
  
  <enforcement_compliance>
    <requirement>通過所有 commit-enforcement.md XML 檢查</requirement>
    <requirement>無嚴重安全或品質警告</requirement>
    <requirement>符合分支、訊息格式規範</requirement>
  </enforcement_compliance>
  
  <integration_integrity>
    <requirement>CI/CD 流程正常運行或產出詳細失敗報告</requirement>
    <requirement>specs 與實際開發狀態同步</requirement>
    <requirement>重開發準備完整性</requirement>
  </integration_integrity>
</quality_gates>
```

## Fast-Stop Mechanism (快停機制)
### Trigger Conditions (觸發條件)
```xml
<fast_stop_triggers>
  <missing_enforcement>commit-enforcement.md 不存在或無效</missing_enforcement>
  <missing_workflow>commit-workflow.md 不存在或無效</missing_workflow>
  <template_failure>關鍵模板文件缺失或損壞</template_failure>
  <critical_cicd_failure>CI/CD 系統性失敗</critical_cicd_failure>
  <agent_coordination_failure>多於 50% agent 執行失敗</agent_coordination_failure>
</fast_stop_triggers>
```

### Minimal Viable Output (最小可行輸出)
```markdown
**Emergency Stop Output Template**:
- **Status**: EMERGENCY_STOP
- **Trigger**: [觸發條件代碼]
- **Available Results**: [已完成的部分結果]
- **Required Actions**: [恢復所需的最小動作]
- **Continuation Plan**: [系統恢復後的繼續方案]
```

## Dependencies (依賴關係)
### Required Files (必要文件)
1. `commit-enforcement.md` - XML 執行規範
2. `commit-workflow.md` - 5 個 agent 協作工作流
3. Template files in `sunnycore/po/templates/`
4. Git repository context and CI/CD integration

### Integration Points (整合點)
- **Git Hooks**: Pre-commit 和 post-commit 整合
- **CI/CD Pipeline**: 持續整合流程整合
- **Documentation System**: 專案文檔系統整合
- **Quality Gates**: 品質閘門系統整合

---

**Task Specification Version**: 1.0  
**Created**: 2025-01-15  
**Status**: ACTIVE  
**Priority**: HIGH
