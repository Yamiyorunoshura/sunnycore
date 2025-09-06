<input>
  <context>
    Task Development workflow for implementing new features based on Implementation Plan specifications using Test-Driven Development methodology
  </context>
  <templates>
    - dev-notes-tmpl.yaml
    - {project_root}/docs/implementation-plan/{task_id}-plan.md
  </templates>
  <subagent-list>
    - Development Notes Template processor
    - TDD Development Process executor  
    - Requirements Analysis engine
  </subagent-list>
</input>

<output>
1. Task Development deliverables
2. docs/dev-notes/{task_id}-dev-notes.md (Markdown Format)
</output>

<constraints importance="Critical">
- 在每完成一個任務後都必須更新Todo-list Tool
- 所有開發工作必須遵循TDD Development Process
- 確保Functional Requirements和Non-functional Requirements完整實現
- Development Notes必須按照Template格式完整填寫
</constraints>

<workflow importance="Critical">
  <stage id="1: todo-list-setup" level_of_think="think" read_token_budget="low" write_token_budget="medium" cache_read_budget="low">
    Todo-list Tool設定和初始化
    - 閱讀整份Workflow
    - 閱讀所有stage的無序列表項
    - 使用Todo-list Tool創建Todo-list  
    - 為每一個Workflow中的無序列表項創建一個todo item
    
    <questions>
    - 是否所有workflow階段都被正確記錄為todo items？
    - Todo-list Tool是否正確初始化？
    </questions>
    
    <checks>
    - 確認Todo-list文件成功創建
    - 驗證所有workflow steps都有對應的todo items
    - 檢查todo items格式符合標準
    </checks>
  </stage>

  <stage id="2: initialization" level_of_think="think" read_token_budget="high" write_token_budget="low" cache_read_budget="medium">
    系統初始化和Context準備
    - 閱讀dev-notes Template了解Development Notes的填入方式
    - 閱讀{task_id}-plan.md了解Task Development需求
    
    <questions>
    - Implementation Plan是否包含清楚的需求定義？
    - Development Notes Template的結構是否理解正確？
    </questions>
    
    <checks>
    - 確認Development Notes Template載入成功
    - 驗證Implementation Plan文件可讀取
    - 檢查Task Development Context完整性
    </checks>
  </stage>

  <stage id="3: requirement-analysis" level_of_think="think hard" read_token_budget="high" write_token_budget="medium" cache_read_budget="high">
    需求分析和Todo-list更新
    - 識別Implementation Plan之中的每一個Functional Requirements
    - 識別Implementation Plan之中的每一個Non-functional Requirements  
    - 修改Todo-list並為每一個Functional Requirements創建一個todo item
    - 修改Todo-list並為每一個Non-functional Requirements創建一個todo item
    
    <questions>
    - 所有Functional Requirements都被正確識別了嗎？
    - Non-functional Requirements是否有遺漏？
    - Requirements之間是否有Dependencies需要考慮？
    </questions>
    
    <checks>
    - 確認所有Functional Requirements都有對應todo items
    - 驗證所有Non-functional Requirements都有對應todo items
    - 檢查Requirements分類的準確性
    - 確保Dependencies關係被正確記錄
    </checks>
  </stage>

  <stage id="4: tdd-development" level_of_think="ultra think" read_token_budget="high" write_token_budget="high" cache_write_budget="high" cache_read_budget="high">
    TDD Development Process執行
    - 開始以TDD Development Process的方式對每一個Functional Requirements進行開發
    - 開始以TDD Development Process的方式對每一個Non-functional Requirements進行開發
    - 遵循TDD Cycle: Red → Green → Refactor
    - 確保Code Quality和Test Coverage達到標準
    
    <questions>
    - 每個requirement是否都有對應的Test Cases？
    - Code Quality是否符合專案標準？
    - Test Coverage是否達到要求的標準？
    - Refactoring是否適當進行？
    </questions>
    
    <checks>
    - 確認每個requirement都遵循TDD Development Process
    - 驗證所有Test Cases都能通過
    - 檢查Code Quality metrics符合標準
    - 確保Functional Requirements正確實現
    - 確保Non-functional Requirements達到目標
    - 驗證Integration Testing成功
    </checks>
  </stage>

  <stage id="5: documentation" level_of_think="think" read_token_budget="medium" write_token_budget="high" cache_write_budget="medium" cache_read_budget="low">
    Documentation和Project Archiving
    - 根據dev notes Template填入Development Notes
    - 將Development Notes以Markdown Format保存在docs/dev-notes/
    - 更新Todo-list狀態為完成
    
    <questions>
    - Development Notes是否完整記錄了開發過程？
    - 所有重要的技術決策是否都有文檔記錄？
    </questions>
    
    <checks>
    - 確認Development Notes格式符合Template要求
    - 驗證Markdown Format正確性
    - 檢查文檔保存路徑正確
    - 確保Todo-list狀態正確更新
    - 驗證Project Archiving完整性
    </checks>
  </stage>
</workflow>

<example>
Task ID: FEAT-001
Implementation Plan: feature-login-system
預期輸出:
1. 成功實現登入系統功能
2. 完整的Test Suite覆蓋
3. docs/dev-notes/FEAT-001-dev-notes.md
4. 更新的Todo-list記錄開發進度
</example>