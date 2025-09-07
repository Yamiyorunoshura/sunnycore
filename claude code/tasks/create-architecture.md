<input>
  <context>
  1. {project_root}/docs/requirements/*.md - Project Requirements Documentation
  2. {project_root}/sunnycore/scripts/shard-architecture.sh - Architecture Script
  </context>
  <templates>
  1. {project_root}/sunnycore/templates/architecture-tmpl.yaml - Architecture Template
  </templates>
</input>

<output>
1. {project_root}/docs/architecture/*.md - Complete Architecture Documentation
</output>

<constraints importance="Critical">
- 必須在完成所有steps後更新Todo List Status
- 每個Functional Requirements和Non-functional Requirements都必須有對應的Architecture Design
- 必須在完成每個Architecture Design後詢問User是否滿意
- Architecture Document必須完全符合Template Format
- 使用Sequential-thinking Tool進行深度分析
- 使用Todo-list Tool進行Task Management
</constraints>

<workflow importance="Critical">
  <stage id="0: Create Todo List", level_of_think="think", cache_read_budget="low">
  - 閱讀整份Workflow
  - 進一步閱讀所有Steps
  - 閱讀所有Steps下的無序列表項
  - 使用Todo-list Tool為每個無序列表項在Todo List中創建一個Todo Item
  
  <checks>
  - [ ] 確認已為所有Task Items創建對應的Todo Items
  - [ ] 驗證Todo List結構完整性
  </checks>
  </stage>
  
  <stage id="1: Create Architecture Design for Functional Requirements", level_of_think="think hard", cache_read_budget="medium">
  - 閱讀{project_root}/docs/requirements/functional-requirements/*.md
  - 使用Sequential-thinking Tool協助理解User Requirements
  - 使用context7搜索是否有可滿足相關Functional Requirements的Architecture Design
  - 識別Requirements Document當中的Functional Requirements
  - 為每個Functional Requirement創建一個Architecture Design
  - 在完成每一個Functional Requirement的Architecture Design後，必須詢問User是否滿意
  - 若User滿意、則將Architecture Design填入Architecture Template
  - 若User不滿意，則重複上述Steps，直到User滿意為止
  
  <checks>
  - [ ] 確認所有Functional Requirements都已識別
  - [ ] 驗證每個Functional Requirement都有對應的Architecture Design
  - [ ] 確認User對每個Design的滿意度
  - [ ] 驗證Architecture Design已正確填入Template
  </checks>
  </stage>
  
  <stage id="2: Create Architecture Design for Non-functional Requirements", level_of_think="think hard", cache_read_budget="medium">
  - 閱讀{project_root}/docs/requirements/non-functional-requirements/*.md
  - 使用Sequential-thinking Tool協助理解User Requirements
  - 識別Requirements Document當中的Non-functional Requirements
  - 使用context7搜索是否有可滿足相關Non-functional Requirements的Architecture Design
  - 為每個Non-functional Requirement創建一個Architecture Design
  - 在完成每一個Non-functional Requirement的Architecture Design後，必須詢問User是否滿意
  - 若User滿意、則將Architecture Design填入Architecture Template
  - 若User不滿意，則重複上述Steps，直到User滿意為止
  
  <checks>
  - [ ] 確認所有Non-functional Requirements都已識別
  - [ ] 驗證每個Non-functional Requirement都有對應的Architecture Design
  - [ ] 確認User對每個Design的滿意度
  - [ ] 驗證Architecture Design已正確填入Template
  </checks>
  </stage>
  
  <stage id="3: Final Architecture Document Review", level_of_think="think", cache_read_budget="low">
  - 詢問User是否滿意完整的Architecture Document
  - 將完整的Architecture Document以markdown格式輸出到{project_root}/docs/architecture.md
  - 運行{project_root}/sunnycore/scripts/shard-architecture.sh將architecture.md分割為多個文件
  
  <checks>
  - [ ] 確認User對完整Architecture Document的滿意度
  - [ ] template中所有需要填入的項目都已填入
  - [ ] 確認Final Document已成功輸出到指定Path
  - [ ] 確認shard-architecture.sh已正確運行
  </checks>
  </stage>
</workflow>