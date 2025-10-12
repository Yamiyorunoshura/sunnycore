# Context Packages

## 概述

Context Packages 是 SunnyCore 框架的上下文恢復系統，用於在對話壓縮（autocompact）後恢復任務上下文。

## 目的

當 AI 對話進行自動壓縮時，任務執行所需的上下文可能會丟失。Context Packages 系統通過以下方式解決這個問題：

1. **預定義的上下文包**：每個任務都有一個包文件，定義了執行該任務所需的所有上下文文件
2. **自動恢復機制**：通過 `context-restorer` 子代理自動識別進行中的任務並恢復上下文
3. **優先級管理**：確保上下文按正確的優先級順序加載（CLAUDE.md > commands > tasks > templates）

## 包文件結構

每個包文件包含以下信息：

```markdown
# Context Package: {task-name}

## Task Information
- **Task Name**: {任務名稱}
- **Role**: {角色名稱}
- **Description**: {任務描述}

## Required Context Files

### 1. Command
{命令文件路徑}

### 2. Task
{任務文件路徑}

### 3. Template
{模板文件路徑（如果適用）}

### 4. Core Guidance
{CLAUDE.md 路徑}

## Priority Order
1. CLAUDE.md (最高優先級)
2. {command}.md (命令級指導)
3. {task}.md (任務級指導)
4. {template}.yaml (模板結構)

## Usage
當 docs/progress.md 顯示此任務正在進行時應加載此包。
```

## 可用的包

### Product Manager (sunnycore_pm)
- `create-requirements.md` - 創建需求文檔
- `create-prd.md` - 創建產品需求文檔
- `create-epic.md` - 創建 Epic 和任務分解
- `create-plan.md` - 創建實施計劃

### Architect (sunnycore_architect)
- `create-architecture.md` - 創建架構文檔（綠地項目）
- `create-brownfield-architecture.md` - 創建架構文檔（棕地項目）
- `document-project.md` - 項目文檔化

### Developer (sunnycore_dev)
- `develop-plan.md` - 執行實施計劃
- `brownfield-plan.md` - 基於審查反饋重新開發
- `fix-acceptance-issues.md` - 修復驗收問題
- `develop-prd.md` - 基於 PRD 開發
- `init.md` - 初始化項目

### QA Engineer (sunnycore_qa)
- `review.md` - 系統質量評估和代碼審查

### Product Owner (sunnycore_po)
- `curate-knowledge.md` - 整理和組織項目知識
- `conclude.md` - 項目結論和完成報告
- `cutover.md` - 切換計劃和執行
- `validate-design.md` - 驗證設計
- `fix-design-conflicts.md` - 解決設計衝突

### Assistant (sunnycore_assistant)
- `consult.md` - 提供諮詢和指導
- `help.md` - 幫助和文檔

## Context Restorer 子代理

`context-restorer` 是一個特殊的子代理，負責在 autocompact 後恢復上下文：

### 工作流程

1. **自動觸發**：在 autocompact 後自動調用
2. **讀取進度**：從 `docs/progress.md` 讀取當前進行中的任務
3. **加載包**：根據任務名稱加載對應的上下文包
4. **生成指令**：生成上下文恢復指令列表
5. **指導代理**：指導主代理按優先級順序讀取所有必需文件

### 輸出格式

```
🔄 Context Restoration: RESTORED

Active Task Identified:
- Task: {task_name}
- Role: {role_name}
- Status: in_progress

Required Context Files (Priority Order):
1. {root}/sunnycore/CLAUDE.md (Core guidance)
2. {root}/sunnycore/commands/{command_file} (Role definition)
3. {root}/sunnycore/tasks/{task_file} (Task specification)
4. {root}/sunnycore/templates/{template_file} (Output format)

Context Loading Instructions:
Please read the above files in order to restore full task context and resume work.
```

## 進度跟蹤

Progress tracking 是一個完整的生命週期管理系統，從任務開始到完成都會自動追蹤。

### 任務開始時的跟蹤
所有命令都要求在任務開始時更新 `docs/progress.md`：

#### 約束條件
每個命令都包含以下約束：

```
**MUST** mark task as "in_progress" in "{PROGRESS}" at the start of task execution, 
**MUST NOT** skip progress tracking
```

### 任務完成時的跟蹤
`completion-validator` 子代理會在驗證任務成功後自動更新進度：

#### 自動完成標記
- **觸發時機**：當 completion-validator 驗證結果為 PASS 時
- **執行動作**：將任務狀態從 "in_progress" 改為 "completed"
- **約束條件**：只在驗證通過時更新，驗證失敗時保持原狀態

#### Completion-Validator 約束
```
**MUST** mark task as "completed" in {PROGRESS} after validation PASS, 
**MUST NOT** update progress on validation FAIL
```

### Progress.md 格式範例

```markdown
# Project Progress

## Current Tasks

- [completed] create-requirements - 創建需求文檔 (由 completion-validator 自動標記)
- [in_progress] create-architecture - 創建技術架構文檔 (由 command 手動標記)
- [pending] create-plan - 創建實施計劃
```

### 進度狀態流轉

```
[pending] 
   ↓ (任務開始時，由 command 更新)
[in_progress] 
   ↓ (任務完成驗證通過後，由 completion-validator 自動更新)
[completed]
```

## 使用流程

### 1. 任務開始
當代理開始執行任務時：
1. 更新 `docs/progress.md`，將任務標記為 `in_progress`
2. 讀取所需的上下文文件（CLAUDE.md, command, task, template）
3. 開始執行任務步驟

### 1.5 任務完成驗證
當代理完成任務並調用 completion-validator 時：
1. completion-validator 驗證所有 DoD 項目
2. 如果驗證 PASS：
   - 自動將 `docs/progress.md` 中的任務狀態從 `in_progress` 改為 `completed`
   - 在驗證報告中顯示進度更新狀態
3. 如果驗證 FAIL：
   - 保持任務狀態為 `in_progress`
   - 等待問題修復後重新驗證

### 2. Autocompact 發生
當對話被壓縮時：
1. 系統自動調用 `context-restorer` 子代理
2. `context-restorer` 讀取 `docs/progress.md`
3. 識別所有 `in_progress` 狀態的任務

### 3. 上下文恢復
`context-restorer` 為每個進行中的任務：
1. 加載對應的包文件
2. 提取所需的上下文文件列表
3. 生成按優先級排序的文件列表
4. 指導主代理讀取所有文件

### 4. 任務繼續
主代理：
1. 按優先級順序讀取所有指定的文件
2. 恢復完整的任務上下文
3. 繼續執行任務

## 優先級層次

上下文加載遵循以下優先級：

1. **CLAUDE.md** (最高) - 核心執行規則和指導
2. **Commands** - 角色定義和範圍限制
3. **Tasks** - 任務特定的步驟和 DoD
4. **Templates** - 輸出格式和結構

當出現衝突時，優先級高的規則覆蓋優先級低的規則。

## 後備策略

如果找不到特定任務的包文件，`context-restorer` 會使用後備策略：

1. 識別任務所屬的角色
2. 使用默認上下文集：
   - CLAUDE.md
   - sunnycore_{role}.md
   - {task_name}.md
3. 在報告中註明使用了後備策略

## 維護指南

### 添加新任務包

1. 在 `packages/` 目錄下創建新的 `.md` 文件
2. 遵循標準包文件結構
3. 確定任務所需的所有上下文文件
4. 按優先級列出文件
5. 在此 README 中更新可用包列表

### 更新現有包

1. 當任務需要額外的上下文文件時更新包
2. 當模板結構變化時更新包
3. 保持優先級順序不變

### 測試上下文恢復

1. 開始一個任務並標記為 `in_progress`
2. 模擬 autocompact（手動調用 `context-restorer`）
3. 驗證所有必需的文件都被列出
4. 確認優先級順序正確

## 注意事項

- **不要**直接修改 `context-restorer.md` 子代理，除非需要改變恢復邏輯
- **始終**在開始任務時更新 `progress.md`
- **確保**包文件中的路徑使用 `{root}` 變量而不是絕對路徑
- **保持**包文件的結構一致性，方便維護

## 相關文件

- `agents/context-restorer.md` - 上下文恢復子代理定義（autocompact 後恢復上下文）
- `agents/completion-validator.md` - 完成驗證子代理定義（驗證 DoD 並自動標記任務完成）
- `commands/*.md` - 所有命令文件（包含任務開始時的進度跟蹤約束）
- `tasks/*.md` - 所有任務文件
- `templates/*.yaml` - 所有模板文件
- `CLAUDE.md` - 核心指導文檔

## 版本歷史

- **v1.1** - 進度追蹤增強
  - 更新 completion-validator 以自動標記任務完成
  - 完善了任務狀態的完整生命週期管理
  - 添加了進度更新邏輯和錯誤處理

- **v1.0** - 初始實現
  - 創建了所有任務的上下文包
  - 實現了 context-restorer 子代理
  - 更新了所有命令以支持任務開始時的進度跟蹤

