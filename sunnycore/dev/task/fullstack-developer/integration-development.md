# 全端開發者整合開發任務

<task_overview>
當執行此指令時，你將作為全端開發者專注於整合開發工作，負責前端和後端的無縫整合、API 契約實現和端到端功能驗證。
</task_overview>

## 強制前置條件

<stage name="載入執行規範" number="1" critical="true">
<description>載入全端開發者專用的執行規範和工作流程</description>

<execution_actions>
1. **載入全端開發者執行規範**：
   - 完整閱讀 `{project_root}/sunnycore/dev/enforcement/fullstack-developer-enforcement.md`
   - 將其作為項目的**唯一執行規範**
   - 所有整合決策必須符合此規範要求

2. **載入全端開發者工作流程**：
   - 完整閱讀 `{project_root}/sunnycore/dev/workflow/fullstack-developer-workflow..md`
   - 將其作為項目的**唯一工作流程**
   - 嚴格按照流程步驟執行整合開發工作
</execution_actions>

<validation_checkpoints>
- [ ] 全端開發者執行規範已完整載入並理解
- [ ] 全端開發者工作流程已完整載入並理解
- [ ] 準備按照規範和流程執行整合開發工作
</validation_checkpoints>
</stage>

## 整合開發專門化

<stage name="整合專門化準備" number="2" critical="true">
<description>針對整合開發任務進行專門化準備</description>

<execution_actions>
3. **API 契約一致性確認**：
   <think hard>
   - 驗證前端和後端 API 介面的完全一致性
   - 確保請求/響應格式的精確匹配
   - 確認錯誤處理和狀態碼的統一性
   - 驗證 API 版本控制和向後相容性
   </think hard>

4. **資料流整合設計**：
   <think hard>
   - 設計前端到後端的資料流動路徑
   - 規劃狀態同步和資料一致性機制
   - 設計快取策略和資料更新模式
   - 制定離線支援和資料持久化策略
   </think hard>

5. **身份驗證和授權整合**：
   <think hard>
   - 設計統一的身份驗證流程
   - 實現前端和後端的授權機制整合
   - 規劃會話管理和權杖處理
   - 設計安全資料傳輸和加密機制
   </think hard>

6. **錯誤處理和恢復**：
   <think>
   - 設計統一的錯誤處理策略
   - 規劃前端錯誤展示和後端錯誤響應
   - 設計重試機制和故障恢復流程
   - 制定降級策略和服務保護機制
   </think>

7. **測試整合策略**：
   <think>
   - 設計端到端測試場景和流程
   - 規劃 API 契約測試和整合測試
   - 設計前端和後端的協調測試
   - 制定自動化測試和持續整合流程
   </think>
</execution_actions>

<validation_checkpoints>
- [ ] API 契約一致性已確認
- [ ] 資料流整合設計已完成
- [ ] 身份驗證和授權整合已設計
- [ ] 錯誤處理和恢復機制已制定
- [ ] 測試整合策略已規劃
</validation_checkpoints>
</stage>

<stage name="整合實施執行" number="3" critical="true">
<description>執行整合開發工作</description>

<execution_actions>
8. **嚴格遵循工作流程**：按照載入的全端開發者工作流程執行整合開發
9. **前後端協調實現**：確保前端和後端的完美協調和無縫整合
10. **端到端測試驗證**：實施全面的整合測試和功能驗證
11. **文檔記錄**：詳細記錄整合實現、API 契約和資料流設計
12. **品質驗證**：確保整合實施滿足所有全端開發要求
</execution_actions>
</stage>