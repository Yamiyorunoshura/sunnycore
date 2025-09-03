#!/bin/bash

# SunnyCore 安裝腳本

# 語言設定
declare -A LANGUAGES=(
    ["ZH"]="中文 (簡體)"
    ["ZH-TW"]="中文 (繁體)"
    ["ZH-HK"]="中文 (香港)"
    ["ENG"]="English"
)

# 分割線標記
SUNNYCORE_START_MARKER="<!-- === SUNNYCORE AUTO-GENERATED CONTENT START === -->"
SUNNYCORE_END_MARKER="<!-- === SUNNYCORE AUTO-GENERATED CONTENT END === -->"

# 語言回應提示模板
declare -A LANGUAGE_PROMPTS=(
    ["ZH"]="請總是用中文（簡體）回覆我。"
    ["ZH-TW"]="請總是用中文（繁體）回覆我。"
    ["ZH-HK"]="請總是用中文（香港）回覆我。"
    ["ENG"]="Please always reply to me in English."
)

echo "========================================"
echo "        SunnyCore 安裝程式"
echo "========================================"
echo ""

# 函數：選擇語言
select_language() {
    echo "請選擇輸出語言 / Please select output language:"
    echo "1) 中文 (簡體) - ZH"
    echo "2) 中文 (繁體) - ZH-TW" 
    echo "3) 中文 (香港) - ZH-HK"
    echo "4) English - ENG"
    echo ""
    
    while true; do
        read -p "請輸入選擇 (1-4) / Please enter choice (1-4): " lang_choice
        case $lang_choice in
            1) SELECTED_LANGUAGE="ZH"; break ;;
            2) SELECTED_LANGUAGE="ZH-TW"; break ;;
            3) SELECTED_LANGUAGE="ZH-HK"; break ;;
            4) SELECTED_LANGUAGE="ENG"; break ;;
            *) echo "無效選擇，請輸入 1-4 / Invalid choice, please enter 1-4" ;;
        esac
    done
    
    echo "已選擇語言 / Selected language: ${LANGUAGES[$SELECTED_LANGUAGE]}"
    echo ""
}

# 函數：檢測並清理舊版本 CLAUDE.md 內容
clean_old_claude_content() {
    local file_path="$1"
    
    if [ ! -f "$file_path" ]; then
        return 0
    fi
    
    # 檢查是否存在 SunnyCore 標記
    if grep -q "$SUNNYCORE_START_MARKER" "$file_path" && grep -q "$SUNNYCORE_END_MARKER" "$file_path"; then
        echo "檢測到舊版本的 SunnyCore 配置，正在清理..."
        
        # 創建臨時文件，移除舊的 SunnyCore 內容
        local temp_file=$(mktemp)
        local in_sunnycore_section=false
        
        while IFS= read -r line; do
            if [[ "$line" == *"$SUNNYCORE_START_MARKER"* ]]; then
                in_sunnycore_section=true
                continue
            elif [[ "$line" == *"$SUNNYCORE_END_MARKER"* ]]; then
                in_sunnycore_section=false
                continue
            elif [ "$in_sunnycore_section" = false ]; then
                echo "$line" >> "$temp_file"
            fi
        done < "$file_path"
        
        # 替換原文件
        mv "$temp_file" "$file_path"
        echo "✓ 已清理舊版本配置"
    fi
}

# 函數：生成 MCP 工具配置內容
generate_mcp_config() {
    local tool_name="$1"
    local language="$2"
    
    case "$tool_name" in
        "sequential-thinking")
            case "$language" in
                "ENG")
                    cat << 'EOF'

<tool name="Sequential_Thinking">
### Sequential Thinking Tool
**Usage**: Before complex tasks, at key decision points, and during task summarization

<commands>
- `process_thought`: Analyze problem complexity, establish structured thinking framework
- `generate_summary`: Generate progress summaries at important milestones, maintain context continuity
- `clear_history`: Clean context when tasks complete or switch, prepare for next cycle
</commands>
</tool>
EOF
                    ;;
                *)
                    cat << 'EOF'

<tool name="Sequential_Thinking">
### Sequential Thinking 工具
**使用時機**: 複雜任務開始前、關鍵決策點、任務總結時

<commands>
- `process_thought`: 分析問題複雜度，建立結構化思維框架
- `generate_summary`: 在重要里程碑生成進度摘要，維護上下文連續性
- `clear_history`: 任務完成或切換時清理上下文，準備下一週期
</commands>
</tool>
EOF
                    ;;
            esac
            ;;
        "context7")
            case "$language" in
                "ENG")
                    cat << 'EOF'

<tool name="Context7">
### Context7 Tool
**Usage**: When needing latest library docs, API references, version-specific information

<commands>
- `resolve-library-id`: Determine correct library identifier, select most relevant match
- `get-library-docs`: Get topic-specific documentation, set appropriate token limit (recommend 10000)
</commands>

<strategy>
**Priority Strategy**: Avoid outdated information, focus on current task-related topics
</strategy>
</tool>
EOF
                    ;;
                *)
                    cat << 'EOF'

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
EOF
                    ;;
            esac
            ;;
        "playwright")
            case "$language" in
                "ENG")
                    cat << 'EOF'

<tool name="Playwright">
### Playwright Tool
**Usage**: Web automation testing, structured web interaction, dynamic content acquisition

<features>
- Use structured accessibility snapshots, avoid dependency on visual models
- Ensure operation reproducibility and stability
- Suitable for frontend functionality verification and end-to-end testing
</features>
</tool>
EOF
                    ;;
                *)
                    cat << 'EOF'

<tool name="Playwright">
### Playwright 工具
**使用時機**: 網頁自動化測試、結構化網頁交互、動態內容獲取時

<features>
- 使用結構化可訪問性快照，避免依賴視覺模型
- 確保操作可重現性和穩定性
- 適用於前端功能驗證和端到端測試
</features>
</tool>
EOF
                    ;;
            esac
            ;;
        "claude-context")
            case "$language" in
                "ENG")
                    cat << 'EOF'

<tool name="Claude_Context">
### Claude Context Tool
**Usage**: All project context establishment tasks

<capabilities>
- Perform semantic search to locate relevant code, establish codebase context understanding
- Identify key modules and dependencies, optimize token usage to reduce costs
- Continuously assist development process, maintain precise context relevance
</capabilities>
</tool>
EOF
                    ;;
                *)
                    cat << 'EOF'

<tool name="Claude_Context">
### Claude Context 工具
**使用時機**: 所有專案上下文建立任務

<capabilities>
- 進行語義搜索定位相關代碼，建立代碼庫上下文理解
- 識別關鍵模塊和依賴關係，優化token使用降低成本
- 持續輔助開發過程，維護精確的上下文相關性
</capabilities>
</tool>
EOF
                    ;;
            esac
            ;;
    esac
}

# 函數：生成工作流程配置
generate_workflow_config() {
    local language="$1"
    
    case "$language" in
        "ENG")
            cat << 'EOF'

<workflow>
## Tool Collaboration Workflow

<phase name="task_initiation">
### Task Initiation Phase
1. **Sequential Thinking** → Analyze task complexity
2. **Claude Context** → Semantic search for related code
3. **Context7** → Get latest technical documentation
</phase>

<phase name="development">
### Development Implementation Phase
1. **Continuous use of Claude Context** → Code understanding and search
2. **Regular use of Sequential Thinking** → Generate progress summaries
3. **Use Playwright as needed** → Web interaction and testing
</phase>

<phase name="completion">
### Task Completion Phase
1. **Sequential Thinking** → Generate final summary
2. **Playwright** → Execute final test verification (if web interaction required)
3. **Sequential Thinking** → Clean context for next task
</phase>
</workflow>

<optimization_principles>
## ⚡ Efficiency Optimization Principles
- **Token Optimization**: Prioritize Claude Context for code search, Context7 for precise documentation snippets
- **Execution Efficiency**: Arrange tool usage order reasonably, avoid duplicate retrieval
- **Error Handling**: Prepare backup plans for each tool, establish graceful degradation strategy
- **Context Maintenance**: Use Sequential Thinking's summary function to establish checkpoint mechanism
</optimization_principles>
</agent_config>
EOF
            ;;
        *)
            cat << 'EOF'

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
EOF
            ;;
    esac
}

# 函數：更新 CLAUDE.md 文件中的語言配置
update_claude_language_config() {
    local claude_md_path="$1"
    local target_language="$2"
    
    if [ ! -f "$claude_md_path" ]; then
        echo "警告: CLAUDE.md 文件不存在: $claude_md_path"
        return 1
    fi
    
    # 語言對應表
    local language_mapping
    case "$target_language" in
        "ENG")
            language_mapping="English"
            ;;
        "ZH-TW")
            language_mapping="Traditional Chinese"
            ;;
        "ZH-CN")
            language_mapping="Simplified Chinese"
            ;;
        *)
            language_mapping="Traditional Chinese"
            ;;
    esac
    
    # 使用 sed 更新 <primary_language> 標籤內容
    if grep -q "<primary_language>" "$claude_md_path"; then
        # 創建臨時文件進行安全的替換
        local temp_file=$(mktemp)
        
        # 逐行處理文件，更新包含 <primary_language> 的行
        while IFS= read -r line; do
            if [[ "$line" == *"<primary_language>"*"</primary_language>"* ]]; then
                # 提取標籤前後的內容並重新組合
                local prefix="${line%%<primary_language>*}"
                local suffix="${line##*</primary_language>}"
                echo "${prefix}<primary_language>${language_mapping}</primary_language>${suffix}" >> "$temp_file"
            else
                echo "$line" >> "$temp_file"
            fi
        done < "$claude_md_path"
        
        # 替換原文件
        mv "$temp_file" "$claude_md_path"
        echo "✓ 已更新 CLAUDE.md 中的語言配置為: $language_mapping"
    else
        echo "警告: 在 CLAUDE.md 中未找到 <primary_language> 標籤"
        return 1
    fi
}

# 函數：創建或更新 CLAUDE.md 文件
create_or_update_claude_md() {
    local claude_md_path="$1"
    
    # 確保目錄存在
    local claude_md_dir=$(dirname "$claude_md_path")
    if [ ! -d "$claude_md_dir" ]; then
        mkdir -p "$claude_md_dir"
    fi
    
    # 檢查是否為現有文件且需要更新語言配置
    if [ -f "$claude_md_path" ]; then
        echo "發現現有的 CLAUDE.md 文件，正在更新語言配置..."
        update_claude_language_config "$claude_md_path" "$SELECTED_LANGUAGE"
    fi
    
    # 清理舊版本內容
    clean_old_claude_content "$claude_md_path"
    
    # 如果文件不存在，創建基礎結構
    if [ ! -f "$claude_md_path" ]; then
        case "$SELECTED_LANGUAGE" in
            "ENG")
                cat > "$claude_md_path" << EOF
<agent_config>
# MCP Smart Agent Configuration Guide

## Basic Settings
<language_preference>
${LANGUAGE_PROMPTS[$SELECTED_LANGUAGE]}
</language_preference>

## Tool Combination
EOF
                ;;
            *)
                cat > "$claude_md_path" << EOF
<agent_config>
# MCP 智能代理配置指南

## 基礎設定
<language_preference>
${LANGUAGE_PROMPTS[$SELECTED_LANGUAGE]}
</language_preference>

## 工具組合
EOF
                ;;
        esac
    fi
    
    # 添加分割線開始標記和 SunnyCore 內容
    echo "正在配置 CLAUDE.md 文件: $claude_md_path"
    echo ""
    echo "$SUNNYCORE_START_MARKER" >> "$claude_md_path"
    
    # 添加選定的工具配置
    for tool in "${!MCP_TOOLS[@]}"; do
        if [ "${MCP_TOOLS[$tool]}" = true ]; then
            echo "添加 $tool 配置..."
            generate_mcp_config "$tool" "$SELECTED_LANGUAGE" >> "$claude_md_path"
            echo "✓ 已添加 $tool 配置"
        fi
    done
    
    # 添加工作流程配置
    generate_workflow_config "$SELECTED_LANGUAGE" >> "$claude_md_path"
    echo "✓ 已添加工作流程配置"
    
    # 添加分割線結束標記
    echo "$SUNNYCORE_END_MARKER" >> "$claude_md_path"
    
    echo "CLAUDE.md 配置完成: $claude_md_path"
}

# 函數：獲取最新版本分支
get_latest_branch() {
    local prefix=$1
    local repo_url="https://github.com/Yamiyorunoshura/sunnycore.git"

    echo "正在檢查最新版本..." >&2

    # 使用 git ls-remote 獲取所有分支
    local branches=$(git ls-remote --heads "$repo_url" | grep "refs/heads/$prefix" | awk '{print $2}' | sed 's|refs/heads/||')

    if [ -z "$branches" ]; then
        echo "未找到 $prefix 相關的分支" >&2
        return 1
    fi

    # 解析版本號並找到最新版本
    local latest_branch=""
    local latest_version="0.0.0"

    while IFS= read -r branch; do
        # 提取版本號 (例如: claude/1.0.0 -> 1.0.0)
        local version=$(echo "$branch" | sed "s|^$prefix||")

        # 比較版本號
        if [ "$(printf '%s\n%s' "$latest_version" "$version" | sort -V | tail -n1)" = "$version" ]; then
            latest_version="$version"
            latest_branch="$branch"
        fi
    done <<< "$branches"

    echo "$latest_branch"
}

# 函數：獲取所有可用版本
get_available_versions() {
    local repo_url="https://github.com/Yamiyorunoshura/sunnycore.git"

    echo "正在獲取可用版本..." >&2

    # 獲取所有相關分支
    local branches=$(git ls-remote --heads "$repo_url" | grep -E "refs/heads/(claude|deepseek)/" | awk '{print $2}' | sed 's|refs/heads/||')

    echo "$branches"
}

# 選擇安裝類型
echo "請選擇安裝類型:"
echo "1) 全局安裝 (安裝到 ~/.claude)"
echo "2) 自定義安裝 (安裝到項目目錄下的 .claude 文件夾)"
echo ""

while true; do
    read -p "請輸入選擇 (1-2): " INSTALL_TYPE_CHOICE
    
    case $INSTALL_TYPE_CHOICE in
        1)
            INSTALL_TYPE="global"
            INSTALL_DIR="$HOME/.claude"
            echo "選擇全局安裝"
            echo "agents 和 commands 安裝目錄: $INSTALL_DIR"
            
            # 獲取 sunnycore 安裝路徑
            read -p "請輸入 sunnycore 安裝目錄 (絕對路徑或 ~ 路徑): " SUNNYCORE_DIR
            
            # 處理 ~ 路徑
            if [[ "$SUNNYCORE_DIR" == ~* ]]; then
                # 展開 ~ 路徑
                eval SUNNYCORE_DIR="$SUNNYCORE_DIR"
            fi
            
            echo "sunnycore 安裝目錄: $SUNNYCORE_DIR"
            break
            ;;
        2)
            INSTALL_TYPE="custom"
            read -p "請輸入項目根目錄 (絕對路徑或 ~ 路徑): " PROJECT_ROOT
            
            # 處理 ~ 路徑
            if [[ "$PROJECT_ROOT" == ~* ]]; then
                # 展開 ~ 路徑
                eval PROJECT_ROOT="$PROJECT_ROOT"
            fi
            
            INSTALL_DIR="$PROJECT_ROOT/.claude"
            SUNNYCORE_DIR="$PROJECT_ROOT"
            echo "選擇自定義安裝，項目根目錄: $PROJECT_ROOT"
            echo "agents 和 commands 安裝目錄: $INSTALL_DIR"
            echo "sunnycore 安裝目錄: $SUNNYCORE_DIR"
            break
            ;;
        *)
            echo "無效選擇，請輸入 1 或 2。"
            ;;
    esac
done

# 清理舊安裝的函數
cleanup_old_installation() {
    local target_dir="$1"
    local components=("agents" "commands" "sunnycore")
    
    echo "檢查並清理舊安裝文件..."
    
    for component in "${components[@]}"; do
        local component_path
        if [ "$component" = "sunnycore" ]; then
            component_path="$SUNNYCORE_DIR/$component"
        else
            component_path="$target_dir/$component"
        fi
        
        if [ -d "$component_path" ]; then
            echo "發現舊的 $component，正在清理: $component_path"
            rm -rf "$component_path"
            if [ $? -eq 0 ]; then
                echo "✓ 已清理舊的 $component"
            else
                echo "✗ 清理 $component 失敗"
            fi
        fi
    done
    
    echo "舊文件清理完成"
}

# 檢查並創建必要的目錄
if [ ! -d "$INSTALL_DIR" ]; then
    echo "目錄不存在，正在創建: $INSTALL_DIR"
    mkdir -p "$INSTALL_DIR"
    if [ $? -ne 0 ]; then
        echo "錯誤: 無法創建目錄 $INSTALL_DIR"
        exit 1
    fi
fi

if [ ! -d "$SUNNYCORE_DIR" ]; then
    echo "目錄不存在，正在創建: $SUNNYCORE_DIR"
    mkdir -p "$SUNNYCORE_DIR"
    if [ $? -ne 0 ]; then
        echo "錯誤: 無法創建目錄 $SUNNYCORE_DIR"
        exit 1
    fi
fi

echo ""

# 選擇版本
echo "請選擇要安裝的版本:"
echo "1) claude (自動選擇最新版本)"
echo "2) deepseek (尚未完成)"
echo "3) 顯示所有可用版本"
echo ""

while true; do
    read -p "請輸入選擇 (1-3): " VERSION_CHOICE

    case $VERSION_CHOICE in
        1)
            VERSION_TYPE="claude"
            echo "正在檢查 claude 系列的最新版本..."
            BRANCH=$(get_latest_branch "claude/")
            if [ $? -eq 0 ] && [ -n "$BRANCH" ]; then
                VERSION="$BRANCH"
                echo "選擇版本: $BRANCH"
                break
            else
                echo "錯誤: 無法獲取 claude 最新版本"
                exit 1
            fi
            ;;
        2)
            VERSION_TYPE="deepseek(暫未完成)"
            echo "正在檢查 deepseek 系列的最新版本..."
            BRANCH=$(get_latest_branch "deepseek/")
            if [ $? -eq 0 ] && [ -n "$BRANCH" ]; then
                VERSION="$BRANCH"
                echo "選擇版本: $BRANCH"
                break
            else
                echo "錯誤: 無法獲取 deepseek 最新版本"
                exit 1
            fi
            ;;
        3)
            echo ""
            echo "所有可用版本:"
            echo "==============="
            available_versions=$(get_available_versions)
            if [ -n "$available_versions" ]; then
                echo "$available_versions" | sort -V
            else
                echo "無法獲取版本信息"
            fi
            echo ""
            echo "請重新選擇:"
            echo "1) claude (自動選擇最新版本)"
            echo "2) deepseek (自動選擇最新版本)"
            ;;
        *)
            echo "無效選擇，請輸入 1、2 或 3。"
            ;;
    esac
done

# 語言選擇
echo ""
echo "========================================"
echo "        語言選擇"
echo "========================================"
echo ""
select_language

# MCP 工具選擇
echo ""
echo "========================================"
echo "        MCP 工具配置"
echo "========================================"
echo ""
echo "請選擇您想要使用的 MCP 工具 (可多選，用空格分隔):"
echo "1) claude-context (代碼庫語義搜索)"
echo "2) sequential-thinking (結構化思維)"
echo "3) context7 (最新庫文檔)"
echo "4) playwright (網頁自動化)"
echo "5) 全部選擇"
echo "6) 跳過 MCP 工具配置"
echo ""

declare -A MCP_TOOLS
MCP_TOOLS["claude-context"]=false
MCP_TOOLS["sequential-thinking"]=false
MCP_TOOLS["context7"]=false
MCP_TOOLS["playwright"]=false

while true; do
    read -p "請輸入選擇 (1-6, 可用空格分隔多個選項): " MCP_CHOICES
    
    if [[ "$MCP_CHOICES" == "6" ]]; then
        echo "跳過 MCP 工具配置"
        SKIP_MCP=true
        break
    elif [[ "$MCP_CHOICES" == "5" ]]; then
        echo "選擇全部 MCP 工具"
        MCP_TOOLS["claude-context"]=true
        MCP_TOOLS["sequential-thinking"]=true
        MCP_TOOLS["context7"]=true
        MCP_TOOLS["playwright"]=true
        SKIP_MCP=false
        break
    else
        # 重置選擇
        MCP_TOOLS["claude-context"]=false
        MCP_TOOLS["sequential-thinking"]=false
        MCP_TOOLS["context7"]=false
        MCP_TOOLS["playwright"]=false
        
        valid_choice=true
        for choice in $MCP_CHOICES; do
            case $choice in
                1)
                    MCP_TOOLS["claude-context"]=true
                    ;;
                2)
                    MCP_TOOLS["sequential-thinking"]=true
                    ;;
                3)
                    MCP_TOOLS["context7"]=true
                    ;;
                4)
                    MCP_TOOLS["playwright"]=true
                    ;;
                *)
                    echo "無效選擇: $choice"
                    valid_choice=false
                    break
                    ;;
            esac
        done
        
        if [ "$valid_choice" = true ]; then
            echo "已選擇的 MCP 工具:"
            for tool in "${!MCP_TOOLS[@]}"; do
                if [ "${MCP_TOOLS[$tool]}" = true ]; then
                    echo "✓ $tool"
                fi
            done
            SKIP_MCP=false
            break
        else
            echo "請重新選擇"
        fi
    fi
done

echo ""
echo "開始安裝..."
echo ""

# 清理舊安裝
cleanup_old_installation "$INSTALL_DIR"

echo ""

# 創建臨時目錄用於下載
TEMP_DIR=$(mktemp -d)
echo "臨時目錄: $TEMP_DIR"

# 下載 GitHub 倉庫
REPO_URL="https://github.com/Yamiyorunoshura/sunnycore.git"
echo "從 GitHub 下載: $REPO_URL"
echo "分支: $BRANCH"

if git clone --branch "$BRANCH" --depth 1 "$REPO_URL" "$TEMP_DIR/sunnycore"; then
    echo "下載完成！"
else
    echo "錯誤: 無法從 GitHub 下載倉庫"
    rm -rf "$TEMP_DIR"
    exit 1
fi

echo ""

# 檢查並複製文件
echo "正在複製文件..."

# 複製 agents 和 commands 到指定目錄
FOLDERS=("agents" "commands")
echo "複製 agents 和 commands 到 $INSTALL_DIR"

for folder in "${FOLDERS[@]}"; do
    if [ -d "$TEMP_DIR/sunnycore/$folder" ]; then
        echo "複製 $folder 到 $INSTALL_DIR..."
        cp -r "$TEMP_DIR/sunnycore/$folder" "$INSTALL_DIR/"
        if [ $? -eq 0 ]; then
            echo "✓ $folder 複製成功"
        else
            echo "✗ $folder 複製失敗"
        fi
    else
        echo "警告: 找不到 $folder 文件夾"
    fi
done

# 複製 sunnycore 到指定目錄
if [ -d "$TEMP_DIR/sunnycore/sunnycore" ]; then
    echo "複製 sunnycore 到 $SUNNYCORE_DIR..."
    cp -r "$TEMP_DIR/sunnycore/sunnycore" "$SUNNYCORE_DIR/"
    if [ $? -eq 0 ]; then
        echo "✓ sunnycore 複製成功到 $SUNNYCORE_DIR/sunnycore"
    else
        echo "✗ sunnycore 複製失敗"
    fi
else
    echo "警告: 找不到 sunnycore 文件夾"
fi

echo ""

# 清理臨時文件
echo "清理臨時文件..."
rm -rf "$TEMP_DIR"

echo ""
echo "========================================"
echo "        安裝完成！"
echo "========================================"
echo ""
echo "安裝類型: $INSTALL_TYPE"
echo "安裝的分支: $BRANCH"
echo "版本類型: $VERSION_TYPE"
echo ""

if [ "$INSTALL_TYPE" = "global" ]; then
    echo "全局安裝完成！"
    echo "agents 和 commands 已安裝至: $INSTALL_DIR"
    echo "sunnycore 已安裝至: $SUNNYCORE_DIR/sunnycore"
else
    echo "自定義安裝完成！"
    echo "agents 和 commands 已安裝至: $INSTALL_DIR"
    echo "sunnycore 已安裝至: $SUNNYCORE_DIR/sunnycore"
fi

echo ""
echo "安裝的文件:"
for folder in "${FOLDERS[@]}"; do
    if [ -d "$INSTALL_DIR/$folder" ]; then
        echo "✓ $INSTALL_DIR/$folder"
    else
        echo "✗ $INSTALL_DIR/$folder (安裝失敗)"
    fi
done

if [ -d "$SUNNYCORE_DIR/sunnycore" ]; then
    echo "✓ $SUNNYCORE_DIR/sunnycore"
else
    echo "✗ $SUNNYCORE_DIR/sunnycore (安裝失敗)"
fi

echo ""

# 配置 MCP 工具
if [ "$SKIP_MCP" != true ]; then
    echo "========================================"
    echo "        配置 MCP 工具"
    echo "========================================"
    echo ""
    
    # 決定 CLAUDE.md 文件位置
    if [ "$INSTALL_TYPE" = "global" ]; then
        CLAUDE_MD_PATH="$INSTALL_DIR/CLAUDE.md"
        echo "全局安裝模式：CLAUDE.md 將創建於 $CLAUDE_MD_PATH"
    else
        CLAUDE_MD_PATH="$PROJECT_ROOT/CLAUDE.md"
        echo "專案安裝模式：CLAUDE.md 將創建於 $CLAUDE_MD_PATH"
    fi
    
    # 創建或更新 CLAUDE.md 文件
    create_or_update_claude_md "$CLAUDE_MD_PATH"
    
    echo ""
    echo "✓ MCP 工具配置完成！"
    echo "配置文件位置: $CLAUDE_MD_PATH"
    echo ""
    echo "已配置的 MCP 工具:"
    for tool in "${!MCP_TOOLS[@]}"; do
        if [ "${MCP_TOOLS[$tool]}" = true ]; then
            echo "  - $tool"
        fi
    done
    echo ""
else
    echo "已跳過 MCP 工具配置"
    echo ""
fi

echo "========================================"
echo "        安裝總結"
echo "========================================"
echo ""
echo "安裝類型: $INSTALL_TYPE"
echo "安裝的分支: $BRANCH"
echo "版本類型: $VERSION_TYPE"
echo ""
echo "安裝位置:"
echo "  - agents 和 commands: $INSTALL_DIR"
echo "  - sunnycore: $SUNNYCORE_DIR/sunnycore"
if [ "$SKIP_MCP" != true ]; then
    echo "  - CLAUDE.md 配置: $CLAUDE_MD_PATH"
fi
echo ""
echo "感謝使用 SunnyCore！"
