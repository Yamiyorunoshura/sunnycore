<input>
  <context>
  1. {project_root}/docs/review-results/{task_id}-review.md
  </context>
  <templates>
  2. {project_root}/sunnycore/templates/dev-notes-tmpl.yaml
  </templates>
</input>

<output>
1. Brownfield Development deliverables and Code Fix implementations
2. {project_root}/docs/dev-notes/{task_id}-dev-notes.md (Markdown Format)
</output>

<constraints importance="Critical">
- 在每完成一個任務後都必須更新Todo-list Tool
- 所有修復工作必須遵循TDD Development Process
- 確保Backward compatibility不被破壞
- 必須進行System Integration Testing驗證
- Development Notes必須記錄所有Code Fix和Risk Assessment
- 保護既有系統的Stability和Data Integrity
</constraints>

<workflow importance="Critical">
  <stage id="1: todo-list-setup" level_of_think="think" read_token_budget="low" write_token_budget="medium" cache_read_budget="low">
    Todo-list Tool設定和初始化
    - 閱讀整份Workflow
    - 閱讀所有stage的無序列表項
    - 使用Todo-list Tool創建Todo-list
    - 為每一個Workflow中的無序列表項創建一個todo item
    
    <questions>
    - 是否所有Brownfield Development階段都被正確記錄？
    - Todo-list Tool是否適合追蹤Code Fix進度？
    </questions>
    
    <checks>
    - 確認Todo-list文件成功創建
    - 驗證所有workflow steps都有對應的todo items
    - 檢查todo items格式符合Brownfield Development需求
    </checks>
  </stage>

  <stage id="2: initialization" level_of_think="think" read_token_budget="high" write_token_budget="low" cache_read_budget="medium">
    系統初始化和Review Results分析準備
    - 閱讀dev-notes Template了解Development Notes的填入方式
    - 閱讀{task_id}-review.md了解Code Review findings和Quality Assurance results
    
    <questions>
    - Review Results是否包含完整的Issue Identification？
    - 是否有足夠的Context理解existing system架構？
    </questions>
    
    <checks>
    - 確認Development Notes Template載入成功
    - 驗證Review Results文件可正確讀取
    - 檢查Brownfield Development Context完整性
    - 確保現有系統架構資訊充足
    </checks>
  </stage>

  <stage id="3: issue-analysis" level_of_think="think hard" read_token_budget="high" write_token_budget="medium" cache_read_budget="high">
    Issue Identification和Recommendations分析
    - 識別Review Results之中的每一個Issues Found in Review（ERR-xxx）
    - 識別Review Results之中的每一個Review Findings - Recommendations（REC-xxx）
    - 修改Todo-list並為每一個Issues Found in Review創建一個todo item
    - 修改Todo-list並為每一個Review Findings - Recommendations創建一個todo item
    - 進行Risk Assessment和Priority Assessment
    
    <questions>
    - 所有Issues Found in Review都被正確識別了嗎？
    - Recommendations是否有Clear implementation path？
    - 是否存在Dependencies需要特殊處理？
    - Risk Assessment是否充分？
    </questions>
    
    <checks>
    - 確認所有ERR-xxx items都有對應todo items
    - 驗證所有REC-xxx items都有對應todo items
    - 檢查Issue Categories分類準確性
    - 確保Priority Assessment合理
    - 驗證Risk Assessment完整性
    </checks>
  </stage>

  <stage id="4: tdd-remediation" level_of_think="ultra think" read_token_budget="high" write_token_budget="high" cache_write_budget="high" cache_read_budget="high">
    TDD Development Process Code Fix執行
    - 開始以TDD Development Process的方式對每一個Issues Found in Review進行修復
    - 開始以TDD Development Process的方式實施每一個Review Findings - Recommendations
    - 遵循TDD Cycle: Red → Green → Refactor，特別注意Brownfield Development constraints
    - 確保Code Quality改進同時維護Backward compatibility
    - 執行Regression Testing和System Integration Testing
    
    <questions>
    - 每個Code Fix是否都有對應的Test Cases？
    - Backward compatibility是否得到保障？
    - Regression Testing是否覆蓋所有相關功能？
    - System Integration是否正常運作？
    </questions>
    
    <checks>
    - 確認每個issue都遵循TDD Development Process修復
    - 驗證所有Test Cases都能通過
    - 檢查Code Quality improvements達到標準
    - 確保Issues Found in Review得到正確解決
    - 確保Recommendations正確實施
    - 驗證Backward compatibility維持
    - 確認System Integration Testing成功
    - 檢查Regression Testing覆蓋度
    </checks>
  </stage>

  <stage id="5: documentation" level_of_think="think" read_token_budget="medium" write_token_budget="high" cache_write_budget="medium" cache_read_budget="low">
    Documentation和Project Archiving
    - 根據dev notes Template填入Development Notes
    - 特別記錄Code Fix details和Risk mitigation措施
    - 將Development Notes以Markdown Format保存在docs/dev-notes/
    - 更新Todo-list狀態為完成
    
    <questions>
    - Development Notes是否完整記錄了所有Code Fix？
    - Risk mitigation措施是否都有文檔？
    - Brownfield Development的特殊考量是否都被記錄？
    </questions>
    
    <checks>
    - 確認Development Notes格式符合Template要求
    - 驗證所有Code Fix都有詳細記錄
    - 檢查Risk Assessment結果被適當記錄
    - 確認Markdown Format正確性
    - 驗證文檔保存路徑正確
    - 確保Todo-list狀態正確更新
    </checks>
  </stage>
</workflow>

<example>
Task ID: FIX-001
Review Results: security-vulnerabilities-analysis
預期輸出:
1. 修復所有已識別的Security Vulnerabilities
2. 實施安全強化Recommendations
3. 完整的Regression Testing suite
4. docs/dev-notes/FIX-001-dev-notes.md
5. 更新的Todo-list記錄修復進度
</example>