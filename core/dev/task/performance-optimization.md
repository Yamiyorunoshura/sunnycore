<?xml version="1.0" encoding="UTF-8"?>
<performance-optimization-task-guide>
    <title>效能優化任務指引</title>
    
    <mandatory-preconditions>
        <title>強制前置條件</title>
        
        <step number="1">
            <title>執行規範載入</title>
            <requirement type="mandatory">
                <description>必須完整讀取並理解</description>
                <path>/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/backend-developer-enforcement.md</path>
                <importance>這是效能優化的**唯一權威規範**</importance>
                <includes>
                    <item>延遲目標要求</item>
                    <item>吞吐量目標要求</item>
                    <item>記憶體使用限制</item>
                    <item>效能監控實施</item>
                    <item>效能測試標準</item>
                </includes>
                <failure-action>如無法載入，立即停止並報告錯誤</failure-action>
            </requirement>
        </step>
        
        <step number="2">
            <title>工作流程遵循</title>
            <requirement type="mandatory">
                <description>必須完整執行</description>
                <path>/Users/tszkinlai/Coding/AI workflow/core/dev/workflow/backend-developer-workflow.md</path>
                <importance>這是效能優化的**唯一標準流程**</importance>
                <includes>
                    <item>強制前置條件驗證</item>
                    <item>專案上下文建立</item>
                    <item>效能專門化準備</item>
                    <item>基準測試建立</item>
                </includes>
                <execution-rule>每個步驟都必須按序完成並通過驗證</execution-rule>
            </requirement>
        </step>
    </mandatory-preconditions>
    
    <execution-requirements>
        <title>執行要求</title>
        
        <requirement name="順序性">
            <description>必須先完成規範載入，再進行流程載入</description>
        </requirement>
        
        <requirement name="完整性">
            <description>兩個文檔都必須完整讀取，不可跳過任何部分</description>
        </requirement>
        
        <requirement name="一致性">
            <description>開發過程中的所有決策都必須與載入的規範和流程保持一致</description>
        </requirement>
        
        <requirement name="驗證性">
            <description>在開始實際優化前，確認已成功載入所有必要文檔</description>
        </requirement>
    </execution-requirements>
    
    <emergency-stop-mechanism>
        <title>快停機制</title>
        <trigger-condition>如果無法成功載入任一必要文檔，立即觸發快停機制</trigger-condition>
        
        <actions>
            <action>停止所有後續操作</action>
            <action>輸出錯誤信息並要求修正</action>
            <action>不進行任何推測性的效能優化工作</action>
        </actions>
    </emergency-stop-mechanism>
</performance-optimization-task-guide>