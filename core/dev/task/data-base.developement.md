<?xml version="1.0" encoding="UTF-8"?>
<database-development-task-guide>
    <title>數據庫開發任務規範</title>
    
    <mandatory-execution-sequence>
        <title>強制執行序列</title>
        <description>在開始任何數據庫開發工作之前，必須按順序執行以下步驟</description>
        
        <step number="1">
            <title>載入開發規範</title>
            <requirement type="mandatory">
                <description>必須完整讀取</description>
                <path>/Users/tszkinlai/Coding/AI workflow/core/dev/workflow/backend-developer-enforcement.md</path>
                <purpose>作為數據庫開發過程的強制性規範和約束條件</purpose>
                <importance>所有開發決策必須符合此規範要求</importance>
            </requirement>
        </step>
        
        <step number="2">
            <title>載入工作流程</title>
            <requirement type="mandatory">
                <description>必須完整讀取</description>
                <path>/Users/tszkinlai/Coding/AI workflow/core/dev/workflow/backend-developer-workflow.md</path>
                <purpose>作為數據庫開發的標準化流程指南</purpose>
                <execution-principle>嚴格按照流程步驟進行開發</execution-principle>
            </requirement>
        </step>
    </mandatory-execution-sequence>
    
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
            <description>在開始實際開發前，確認已成功載入所有必要文檔</description>
        </requirement>
    </execution-requirements>
    
    <emergency-stop-mechanism>
        <title>快停機制</title>
        <trigger-condition>如果無法成功載入任一必要文檔，立即觸發快停機制</trigger-condition>
        
        <actions>
            <action>停止所有後續操作</action>
            <action>輸出錯誤信息並要求修正</action>
            <action>不進行任何推測性的開發工作</action>
        </actions>
    </emergency-stop-mechanism>
</database-development-task-guide>