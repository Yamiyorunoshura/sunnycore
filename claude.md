<agent_config>
# MCP 智能代理配置指南

## 基礎設定
<language_preference>
總是用繁體中文回應。
</language_preference>

## 工具組合

<tool name="Sequential_Thinking">
### Sequential Thinking 工具
**使用時機**: 複雜任務開始前、關鍵決策點、任務總結時

<commands>
- `process_thought`: 分析問題複雜度，建立結構化思維框架
- `generate_summary`: 在重要里程碑生成進度摘要，維護上下文連續性
- `clear_history`: 任務完成或切換時清理上下文，準備下一週期
</commands>
</tool>

<tool name="Context7">
### Context7 工具
**使用時機**: 需要最新庫文檔、API參考、版本特定資訊時

<commands>
- `resolve-library-id`: 確定正確的庫標識符，選擇最相關匹配
- `get-library-docs`: 獲取特定主題文檔，設置適當token限制（建議10000）
</commands>

<strategy>
**優先策略**: 避免使用過時資訊，專注當前任務相關主題
</strategy>
</tool>

<tool name="Playwright">
### Playwright 工具
**使用時機**: 網頁自動化測試、結構化網頁交互、動態內容獲取時

<features>
- 使用結構化可訪問性快照，避免依賴視覺模型
- 確保操作可重現性和穩定性
- 適用於前端功能驗證和端到端測試
</features>
</tool>

<tool name="Claude_Context">
### Claude Context 工具
**使用時機**: 所有專案上下文建立任務

<capabilities>
- 進行語義搜索定位相關代碼，建立代碼庫上下文理解
- 識別關鍵模塊和依賴關係，優化token使用降低成本
- 持續輔助開發過程，維護精確的上下文相關性
</capabilities>
</tool>

<workflow>
## 工具協同使用流程

<phase name="task_initiation">
### 任務開始階段
1. **Sequential Thinking** → 分析任務複雜度
2. **Claude Context** → 語義搜索相關代碼
3. **Context7** → 獲取最新技術文檔
</phase>

<phase name="development">
### 開發實施階段
1. **持續使用 Claude Context** → 代碼理解與搜索
2. **定期使用 Sequential Thinking** → 生成進度摘要
3. **按需使用 Playwright** → 網頁交互與測試
</phase>

<phase name="completion">
### 任務完成階段
1. **Sequential Thinking** → 生成最終總結
2. **Playwright** → 執行最終測試驗證（如有網頁交互需求）
3. **Sequential Thinking** → 清理上下文準備下一任務
</phase>
</workflow>

<optimization_principles>
## ⚡ 效率優化原則
- **Token優化**: 優先使用Claude Context進行代碼搜索，Context7獲取精確文檔片段
- **執行效率**: 合理安排工具使用順序，避免重複檢索
- **錯誤處理**: 為每個工具準備備用方案，建立優雅降級策略
- **上下文維護**: 使用Sequential Thinking的摘要功能建立檢查點機制
</optimization_principles>
</agent_config>
