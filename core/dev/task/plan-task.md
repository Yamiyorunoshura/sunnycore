# 任務規劃執行指令

<task_overview>
作為任務規劃協調專家，您需要對指定任務進行全面規劃，確保實施計劃的可行性和執行策略的最佳化。
</task_overview>

## 核心規劃階段

<optimization_phases>

### 階段一：強制前置條件驗證
<phase name="mandatory_prerequisite_validation" complexity="think">
**目標**: 載入並驗證所有必要的執行規範和工作流程定義

**執行步驟**:
1. **載入強制執行規範**：完整讀取 `~/cursor-claude/core/dev/enforcement/developer-orchestrator-enforcement.md`
   - 這包含所有強制執行規則和驗證標準
   - 如果無法載入，立即停止並報告錯誤

2. **載入工作流程定義**：完整讀取 `~/cursor-claude/core/dev/workflow/developer-orchestrator-workflow.md`
   - 理解所有階段、檢查點和驗證要求
   - 如果無法載入，立即停止並報告錯誤

**驗證檢查點**:
- [ ] 強制執行規範已完整載入
- [ ] 工作流程定義已完整載入
- [ ] 所有執行規則已理解並準備應用

**預期成果**: 建立完整的規範和工作流程理解基礎
</phase>

### 階段二：專案資訊蒐集與分析
<phase name="project_information_analysis" complexity="think hard">
**目標**: 全面了解專案背景和建立規劃基礎

**執行步驟**:
3. **載入專案規範**：完整讀取 `{project_root}/docs/specs/` 路徑下的所有文檔
   - 分析專案架構和技術棧
   - 識別專案依賴關係和約束條件
   - 了解專案整體目標和業務需求

**驗證檢查點**:
- [ ] 專案規範已完整讀取和理解
- [ ] 專案上下文模型已建立
- [ ] 技術約束和依賴關係已識別

**預期成果**: 建立完整的專案理解和規劃上下文
</phase>

### 階段三：任務規劃委派執行
<phase name="task_planning_delegation" complexity="think">
**目標**: 將充分準備的任務上下文委派給專業規劃代理

**執行步驟**:
4. **委派給子代理**：將任務傳遞給子代理 `task-planner`
   - 提供完整的專案上下文和規範資訊
   - 確保所有必要的規劃資料已準備就緒
   - 監控規劃過程並提供必要支援

**驗證檢查點**:
- [ ] 所有必要資訊已準備完整
- [ ] 子代理已成功接收任務
- [ ] 規劃上下文已正確傳遞

**預期成果**: 專業任務規劃的成功啟動和執行
</phase>

</optimization_phases>

## 品質保證機制

<quality_assurance>
<validation_criteria>
- [ ] 規範載入完整性：所有必要規範文檔都已載入並理解
- [ ] 專案理解深度：專案上下文分析充分且準確
- [ ] 委派準備度：所有必要資訊已準備就緒供子代理使用
- [ ] 流程一致性：遵循統一的任務規劃工作流程
- [ ] 錯誤處理：適當的錯誤檢查和異常處理機制
</validation_criteria>
</quality_assurance>