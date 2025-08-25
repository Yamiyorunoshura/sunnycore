<?xml version="1.0" encoding="UTF-8"?>
<security-development-task-guide>
    <title>安全開發任務指引</title>
    
    <mandatory-preconditions>
        <title>強制前置條件</title>
        
        <step number="1">
            <title>執行規範載入</title>
            <requirement type="mandatory">
                <description>必須完整讀取並理解</description>
                <path>/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/backend-developer-enforcement.md</path>
                <importance>這是安全開發的**唯一權威規範**</importance>
                <includes>
                    <item>身份驗證機制要求</item>
                    <item>授權控制標準</item>
                    <item>輸入驗證規範</item>
                    <item>資料清理要求</item>
                    <item>機密處理標準</item>
                    <item>安全檢查清單</item>
                </includes>
                <failure-action>如無法載入，立即停止並報告錯誤</failure-action>
            </requirement>
        </step>
        
        <step number="2">
            <title>工作流程遵循</title>
            <requirement type="mandatory">
                <description>必須完整執行</description>
                <path>/Users/tszkinlai/Coding/AI workflow/core/dev/workflow/backend-developer-workflow.md</path>
                <importance>這是安全開發的**唯一標準流程**</importance>
                <includes>
                    <item>強制前置條件驗證</item>
                    <item>專案上下文建立</item>
                    <item>安全專門化準備</item>
                    <item>威脅建模分析</item>
                    <item>安全測試實施</item>
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
            <description>在開始實際安全開發前，確認已成功載入所有必要文檔</description>
        </requirement>
    </execution-requirements>
    
    <emergency-stop-mechanism>
        <title>快停機制</title>
        <trigger-condition>如果無法成功載入任一必要文檔，立即觸發快停機制</trigger-condition>
        
        <actions>
            <action>停止所有後續操作</action>
            <action>輸出錯誤信息並要求修正</action>
            <action>不進行任何推測性的安全開發工作</action>
        </actions>
    </emergency-stop-mechanism>
</security-development-task-guide>