<?xml version="1.0" encoding="UTF-8"?>
<backend-developer-workflow>
    <title>後端開發者工作流程</title>
    
    <mandatory-preconditions>
        <title>強制前置條件驗證</title>
        
        <step number="1">
            <title>載入執行規範</title>
            <actions>
                <action priority="1">
                    <name>強制執行規範載入</name>
                    <description>完整讀取 `/Users/tszkinlai/Coding/AI workflow/core/dev/enforcement/backend-developer-enforcement.md`</description>
                    <requirements>
                        <think hard>
                        <requirement>理解所有強制規則、安全要求和品質門檻</requirement>
                        <requirement>如果無法載入，立即停止並報告錯誤</requirement>
                        <think hard>
                    </requirements>
                </action>
            </actions>
        </step>
        
        <step number="2">
            <title>專案上下文建立</title>
            <actions>
                <action priority="2">
                    <name>專案規範理解</name>
                    <description>讀取 `{project_root}/docs/specs/` 路徑下的所有文檔</description>
                    <requirements>
                        <think hard>
                        <requirement>理解專案需求、架構設計、技術約束</requirement>
                        <requirement>建立完整的專案上下文模型</requirement>
                        <requirement>識別關鍵依賴關係和安全要求</requirement>
                        <think hard>
                    </requirements>
                </action>
                
                <action priority="3">
                    <name>實施計劃驗證</name>
                    <description>確認 `{project_root}/docs/implementation-plan/{task_id}-plan.md` 存在且可讀取</description>
                    <critical-checkpoint>如果實施計劃不存在，立即停止並通知用戶需要先執行計劃階段</critical-checkpoint>
                    <requirements>
                        <think hard>
                        <requirement>驗證計劃完整性、範圍定義和技術可行性</requirement>
                        <requirement>確認安全要求和效能目標</requirement>
                        <think hard>
                    </requirements>
                </action>
            </actions>
        </step>
        
        <step number="3">
            <title>後端專門化準備</title>
            <actions>
                <action priority="4">
                    <name>安全檢查清單準備</name>
                    <description>根據強制執行規範準備安全檢查清單</description>
                    <checklist>
                        <think>
                        <item>輸入驗證策略</item>
                        <item>身份驗證和授權機制</item>
                        <item>資料加密和敏感資訊處理</item>
                        <item>API安全設計</item>
                        <think>
                    </checklist>
                </action>
                
                <action priority="5">
                    <name>效能目標確認</name>
                    <description>確認並記錄效能要求</description>
                    <targets>
                        <think>
                        <target>延遲目標和吞吐量要求</target>
                        <target>記憶體使用限制</target>
                        <target>監控和測量策略</target>
                        <think>
                    </targets>
                </action>
            </actions>
        </step>
    </mandatory-preconditions>
    
    <execution-protocol>
        <title>執行協議</title>
        
        <phase name="tdd-development">
            <title>TDD開發流程</title>
            <actions>
                <action priority="6">
                    <name>測試優先開發</name>
                    <description>嚴格遵循TDD原則</description>
                    <requirements>
                        <think harder>
                        <requirement>先寫測試後寫實現</requirement>
                        <requirement>確保測試覆蓋率達到要求門檻</requirement>
                        <requirement>實施單元測試、整合測試和契約測試</requirement>
                        <think harder>
                    </requirements>
                </action>
                
                <action priority="7">
                    <name>架構原則應用</name>
                    <description>在開發過程中應用</description>
                    <principles>
                        <think harder>
                        <principle>SOLID設計原則</principle>
                        <principle>清潔架構和關注點分離</principle>
                        <principle>錯誤處理和日誌記錄機制</principle>
                        <think harder>
                    </principles>
                </action>
            </actions>
        </phase>
        
        <phase name="quality-assurance">
            <title>品質保證</title>
            <actions>
                <action priority="8">
                    <name>持續驗證</name>
                    <description>在開發過程中持續執行</description>
                    <validations>
                        <think hard>
                        <validation>靜態分析檢查</validation>
                        <validation>安全漏洞掃描</validation>
                        <validation>效能基準測試</validation>
                        <validation>向後相容性驗證</validation>
                        <think hard>
                    </validations>
                </action>
            </actions>
        </phase>
    </execution-protocol>
    
    <failure-handling>
        <title>失敗處理機制</title>
        <scenarios>
            <scenario type="precondition-failure">
                <description>前置條件失敗</description>
                <action>立即停止，報告具體缺失的文件或條件</action>
            </scenario>
            
            <scenario type="plan-missing">
                <description>計劃缺失</description>
                <action>停止開發，引導用戶先執行計劃階段</action>
            </scenario>
            
            <scenario type="security-check-failed">
                <description>安全檢查未通過</description>
                <action>記錄風險並要求修復後繼續</action>
            </scenario>
            
            <scenario type="performance-below-threshold">
                <description>效能未達標</description>
                <action>記錄測量結果並制定優化計劃</action>
            </scenario>
        </scenarios>
    </failure-handling>
</backend-developer-workflow>
