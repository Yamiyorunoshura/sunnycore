#!/bin/bash

# SunnyCore 安裝腳本 v2.0
# 支援選擇性MCP工具安裝和用戶資料保護

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

# MCP工具配置
declare -A MCP_TOOLS=(
    ["sequential_thinking"]="🧠 Sequential Thinking System"
    ["context7"]="📚 Context7 System"
    ["playwright"]="🌐 Playwright System"
    ["claude_context"]="🔍 Claude Context System"
)

# 工具章節邊界標記（用於識別各工具內容範圍）
declare -A TOOL_SECTION_START=(
    ["sequential_thinking"]="### 🧠 Sequential Thinking System"
    ["context7"]="### 📚 Context7 System"
    ["playwright"]="### 🌐 Playwright System"
    ["claude_context"]="### 🔍 Claude Context System"
)

# 選擇的工具列表
SELECTED_TOOLS=()
SKIP_MCP_SELECTION=false

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

# 函數：MCP工具選擇界面
select_mcp_tools() {
    echo "========================================"
    echo "        MCP 工具選擇"
    echo "========================================"
    echo ""
    echo "請選擇要安裝的 MCP 工具 (可多選):"
    echo "1) 🧠 Sequential Thinking System - 認知架構協調專家"
    echo "2) 📚 Context7 System - 知識資源管理專家"
    echo "3) 🌐 Playwright System - 網頁自動化測試專家"
    echo "4) 🔍 Claude Context System - 代碼庫理解和搜索專家"
    echo "5) 全部安裝"
    echo "6) 跳過 MCP 工具配置"
    echo ""
    
    while true; do
        read -p "請輸入選擇 (用逗號分隔多個選項，如 1,2,3): " tool_choices
        
        # 處理跳過選項
        if [[ "$tool_choices" == "6" ]]; then
            SKIP_MCP_SELECTION=true
            echo "已跳過 MCP 工具配置"
            return 0
        fi
        
        # 處理全部安裝
        if [[ "$tool_choices" == "5" ]]; then
            SELECTED_TOOLS=("sequential_thinking" "context7" "playwright" "claude_context")
            echo "已選擇安裝所有 MCP 工具"
            return 0
        fi
        
        # 解析選擇
        SELECTED_TOOLS=()
        IFS=',' read -ra CHOICES <<< "$tool_choices"
        local valid_choice=true
        
        for choice in "${CHOICES[@]}"; do
            # 移除空格
            choice=$(echo "$choice" | tr -d ' ')
            case $choice in
                1) SELECTED_TOOLS+=("sequential_thinking") ;;
                2) SELECTED_TOOLS+=("context7") ;;
                3) SELECTED_TOOLS+=("playwright") ;;
                4) SELECTED_TOOLS+=("claude_context") ;;
                *) 
                    echo "無效選擇: $choice"
                    valid_choice=false
                    break
                    ;;
            esac
        done
        
        if [ "$valid_choice" = true ] && [ ${#SELECTED_TOOLS[@]} -gt 0 ]; then
            echo "已選擇安裝以下工具:"
            for tool in "${SELECTED_TOOLS[@]}"; do
                echo "  - ${MCP_TOOLS[$tool]}"
            done
            return 0
        else
            echo "請輸入有效的選擇 (1-6)"
        fi
    done
}

# 函數：從CLAUDE.md提取指定工具的章節內容
extract_tool_section() {
    local source_file="$1"
    local tool_name="$2"
    local output_file="$3"
    
    if [ ! -f "$source_file" ]; then
        echo "錯誤: 找不到源文件 $source_file"
        return 1
    fi
    
    local start_pattern="${TOOL_SECTION_START[$tool_name]}"
    if [ -z "$start_pattern" ]; then
        echo "錯誤: 未知的工具名稱 $tool_name"
        return 1
    fi
    
    # 找到所有工具章節的行號
    local tool_sections=()
    for tool in "${!TOOL_SECTION_START[@]}"; do
        local line_num=$(grep -n "^${TOOL_SECTION_START[$tool]}" "$source_file" | cut -d: -f1)
        if [ -n "$line_num" ]; then
            tool_sections+=("$line_num:$tool")
        fi
    done
    
    # 排序章節按行號
    IFS=$'\n' tool_sections=($(sort -n <<< "${tool_sections[*]}"))
    
    # 找到目標工具的開始行號和結束行號
    local start_line=""
    local end_line=""
    
    for i in "${!tool_sections[@]}"; do
        local section="${tool_sections[i]}"
        local line_num="${section%%:*}"
        local section_tool="${section##*:}"
        
        if [ "$section_tool" = "$tool_name" ]; then
            start_line="$line_num"
            # 找下一個章節作為結束點
            if [ $((i + 1)) -lt ${#tool_sections[@]} ]; then
                local next_section="${tool_sections[$((i + 1))]}"
                end_line="${next_section%%:*}"
                end_line=$((end_line - 1))
            else
                # 如果是最後一個工具，找到</technical_expertise>標籤
                end_line=$(grep -n "</technical_expertise>" "$source_file" | cut -d: -f1)
                if [ -n "$end_line" ]; then
                    end_line=$((end_line - 1))
                fi
            fi
            break
        fi
    done
    
    if [ -z "$start_line" ]; then
        echo "錯誤: 在 $source_file 中找不到工具 $tool_name 的章節"
        return 1
    fi
    
    # 提取指定範圍的內容
    if [ -n "$end_line" ]; then
        sed -n "${start_line},${end_line}p" "$source_file" > "$output_file"
    else
        # 如果沒有找到結束行，提取到文件末尾
        sed -n "${start_line},\$p" "$source_file" > "$output_file"
    fi
    
    echo "✓ 已提取 ${MCP_TOOLS[$tool_name]} 內容 (行 $start_line-${end_line:-EOF})"
    return 0
}

# 函數：安全插入MCP工具配置到CLAUDE.md
safe_insert_mcp_tools() {
    local claude_md_path="$1"
    
    if [ "$SKIP_MCP_SELECTION" = true ]; then
        echo "跳過 MCP 工具配置"
        return 0
    fi
    
    if [ ${#SELECTED_TOOLS[@]} -eq 0 ]; then
        echo "未選擇任何 MCP 工具"
        return 0
    fi
    
    # 確保目標文件存在
    if [ ! -f "$claude_md_path" ]; then
        touch "$claude_md_path"
        echo "已創建新的 CLAUDE.md 文件"
    fi
    
    # 清理舊的 SunnyCore 內容
    clean_old_claude_content "$claude_md_path"
    
    # 準備要插入的內容
    local temp_content=$(mktemp)
    local source_claude_md=""
    
    # 優先使用本地克隆的 CLAUDE.md
    local local_repo_path="$TEMP_DIR/sunnycore"
    local local_claude_md="$local_repo_path/CLAUDE.md"
    if [ -f "$local_claude_md" ]; then
        source_claude_md="$local_claude_md"
        echo "使用本地 CLAUDE.md: $source_claude_md"
    else
        # 回退到 GitHub 下載
        source_claude_md=$(fetch_claude_md_from_github "$BRANCH")
        if [ $? -ne 0 ] || [ ! -f "$source_claude_md" ]; then
            echo "✗ 無法獲取 CLAUDE.md 源文件"
            return 1
        fi
        echo "使用下載的 CLAUDE.md: $source_claude_md"
    fi
    
    # 生成插入內容
    echo "" > "$temp_content"
    echo "$SUNNYCORE_START_MARKER" >> "$temp_content"
    echo "" >> "$temp_content"
    echo "# SunnyCore MCP Tools Configuration" >> "$temp_content"
    echo "## Auto-generated content - Do not edit manually" >> "$temp_content"
    echo "" >> "$temp_content"
    
    # 提取並插入選定的工具章節
    for tool in "${SELECTED_TOOLS[@]}"; do
        echo "正在提取 ${MCP_TOOLS[$tool]} 配置..."
        local tool_temp=$(mktemp)
        
        if extract_tool_section "$source_claude_md" "$tool" "$tool_temp"; then
            echo "" >> "$temp_content"
            cat "$tool_temp" >> "$temp_content"
            echo "" >> "$temp_content"
        else
            echo "⚠ 提取 ${MCP_TOOLS[$tool]} 失敗，跳過"
        fi
        
        rm -f "$tool_temp"
    done
    
    echo "" >> "$temp_content"
    echo "$SUNNYCORE_END_MARKER" >> "$temp_content"
    
    # 插入內容到目標文件末尾
    cat "$temp_content" >> "$claude_md_path"
    
    # 清理臨時文件
    rm -f "$temp_content"
    [ -n "$source_claude_md" ] && [ "$source_claude_md" != "$local_claude_md" ] && rm -f "$source_claude_md"
    
    echo "✓ 已成功插入選定的 MCP 工具配置到 $claude_md_path"
    echo "✓ 用戶原有內容已保留，新配置添加在文件末尾"
    
    return 0
}

# （已移除）生成 MCP 工具配置與工作流程的內嵌模板，改為統一從 GitHub 取得 CLAUDE.md

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
        "ZH"|"ZH-CN")
            language_mapping="Simplified Chinese"
            ;;
        "ZH-TW"|"ZH-HK")
            language_mapping="Traditional Chinese"
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

# 函數：從GitHub獲取CLAUDE.md內容
fetch_claude_md_from_github() {
    local branch="$1"
    local temp_file
    local repo_url="https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore"
    local api_repo_url="https://github.com/Yamiyorunoshura/sunnycore.git"
    local ref="$branch"
    local curl_exit_code
    local file_size
    
    # 創建臨時文件
    temp_file=$(mktemp) || {
        echo "✗ 無法創建臨時文件"
        return 1
    }
    
    echo "正在從GitHub獲取CLAUDE.md內容..."
    echo "分支: $branch"
    
    # 嘗試用 commit SHA 以支援包含斜線的分支名稱
    local commit_sha=$(git ls-remote --heads "$api_repo_url" "$branch" | awk '{print $1}' | head -n1)
    if [ -n "$commit_sha" ]; then
        ref="$commit_sha"
        echo "使用 commit SHA 下載: $commit_sha"
    else
        echo "未能解析 commit SHA，回退使用分支名下載"
    fi
    
    local file_url="$repo_url/$ref/CLAUDE.md"
    echo "URL: $file_url"
    echo "臨時文件: $temp_file"
    
    # 使用curl獲取文件內容，添加更詳細的錯誤處理
    curl -s -f -L --connect-timeout 30 --max-time 60 "$file_url" -o "$temp_file" 2>/dev/null
    curl_exit_code=$?
    
    if [ $curl_exit_code -eq 0 ] && [ -f "$temp_file" ]; then
        file_size=$(wc -l < "$temp_file" 2>/dev/null || echo "0")
        
        # 驗證文件內容是否有效（至少包含一些預期內容）
        if [ "$file_size" -gt 10 ] && grep -q "primary_language\|MCP\|Claude" "$temp_file" 2>/dev/null; then
            echo "✓ 成功從GitHub獲取CLAUDE.md內容 ($file_size 行)"
            echo "✓ 文件內容驗證通過"
            echo "$temp_file"
            return 0
        else
            echo "✗ 獲取的文件內容無效或為空 ($file_size 行)"
            [ "$file_size" -gt 0 ] && echo "文件前幾行:" && head -3 "$temp_file" 2>/dev/null
            rm -f "$temp_file"
            return 1
        fi
    else
        echo "✗ 無法從GitHub獲取CLAUDE.md內容"
        case $curl_exit_code in
            6) echo "  - 無法解析主機名" ;;
            7) echo "  - 無法連接到服務器" ;;
            22) echo "  - HTTP錯誤（可能是404或403）" ;;
            28) echo "  - 操作超時" ;;
            *) echo "  - curl錯誤代碼: $curl_exit_code" ;;
        esac
        echo "  - 檢查網路連接"
        echo "  - 檢查分支是否存在: $branch"
        rm -f "$temp_file"
        return 1
    fi
}



# 函數：創建或更新 CLAUDE.md 文件
create_or_update_claude_md() {
    local claude_md_path="$1"
    local branch_name="${2:-$BRANCH}"  # 接受分支參數，如果沒有則使用全局變數
    
    echo "調試信息："
    echo "  - CLAUDE.md路徑: $claude_md_path"
    echo "  - 使用分支: $branch_name"
    echo "  - 全局BRANCH變數: $BRANCH"
    
    # 確保目錄存在
    local claude_md_dir=$(dirname "$claude_md_path")
    if [ ! -d "$claude_md_dir" ]; then
        mkdir -p "$claude_md_dir"
    fi
    
    # 驗證分支變數是否可用
    if [ -z "$branch_name" ]; then
        echo "警告: 分支變數為空，使用master作為預設值"
        branch_name="master"
    fi
    
    # 優先從本地已克隆倉庫複製 CLAUDE.md
    local local_repo_path="$TEMP_DIR/sunnycore"
    local local_claude_md="$local_repo_path/CLAUDE.md"
    if [ -f "$local_claude_md" ]; then
        echo "優先使用本地克隆倉庫中的 CLAUDE.md: $local_claude_md"
        cp "$local_claude_md" "$claude_md_path"
        github_claude_md=""
    else
        # 回退到 GitHub 下載
        echo "嘗試從GitHub獲取CLAUDE.md內容，分支: $branch_name"
        local github_claude_md=$(fetch_claude_md_from_github "$branch_name")
    fi
    
    if [ -f "$claude_md_path" ]; then
        echo "已獲取 CLAUDE.md 內容"
        
        # 清理臨時文件（若存在）
        [ -n "$github_claude_md" ] && [ -f "$github_claude_md" ] && rm -f "$github_claude_md"
        
        # 更新語言配置
        if update_claude_language_config "$claude_md_path" "$SELECTED_LANGUAGE"; then
            echo "✓ 語言配置更新成功"
        else
            echo "⚠ 語言配置更新失敗，但文件內容已獲取"
        fi
        
        echo "✓ 已使用GitHub最新內容創建CLAUDE.md並更新語言配置"
    else
        echo "✗ 無法取得 CLAUDE.md，已跳過生成。"
        echo "  - 已嘗試本地副本與 GitHub 下載 (分支: $branch_name)"
        return 1
    fi
    
    echo ""
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

echo ""
# 呼叫MCP工具選擇函數
select_mcp_tools

echo ""
echo "開始安裝..."
echo ""

# 清理舊安裝
cleanup_old_installation "$INSTALL_DIR"

echo ""

# 創建臨時目錄用於下載
TEMP_DIR=$(mktemp -d)
echo "臨時目錄: $TEMP_DIR"

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

# 注意：延後清理臨時目錄到安裝總結之後，避免影響 MCP 下載回退方案

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
echo "========================================"
echo "        配置 MCP 工具"
echo "========================================"
echo ""

# 決定 CLAUDE.md 文件位置
if [ "$INSTALL_TYPE" = "global" ]; then
    CLAUDE_MD_PATH="$INSTALL_DIR/CLAUDE.md"
    echo "全局安裝模式：CLAUDE.md 位於 $CLAUDE_MD_PATH"
else
    CLAUDE_MD_PATH="$PROJECT_ROOT/CLAUDE.md"
    echo "專案安裝模式：CLAUDE.md 位於 $CLAUDE_MD_PATH"
fi

echo "調試：MCP配置階段的變數狀態"
echo "  - BRANCH: $BRANCH"
echo "  - VERSION_TYPE: $VERSION_TYPE"
echo "  - CLAUDE_MD_PATH: $CLAUDE_MD_PATH"
echo "  - 選擇的工具數量: ${#SELECTED_TOOLS[@]}"
echo ""

# 使用新的安全插入邏輯
if safe_insert_mcp_tools "$CLAUDE_MD_PATH"; then
    echo ""
    echo "✓ MCP 工具配置完成！"
    echo "配置文件位置: $CLAUDE_MD_PATH"
    if [ ${#SELECTED_TOOLS[@]} -gt 0 ]; then
        echo "已安裝的工具:"
        for tool in "${SELECTED_TOOLS[@]}"; do
            echo "  - ${MCP_TOOLS[$tool]}"
        done
    fi
    echo ""
else
    echo ""
    echo "✗ MCP 工具配置失敗。"
    echo "  - 您可以稍後重試或手動配置。"
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
if [ "$SKIP_MCP_SELECTION" != true ]; then
    if [ -f "$CLAUDE_MD_PATH" ]; then
        echo "  - CLAUDE.md 配置: $CLAUDE_MD_PATH"
        if [ ${#SELECTED_TOOLS[@]} -gt 0 ]; then
            echo "  - 已安裝的 MCP 工具:"
            for tool in "${SELECTED_TOOLS[@]}"; do
                echo "    • ${MCP_TOOLS[$tool]}"
            done
        fi
    else
        echo "  - CLAUDE.md 配置: (未生成)"
    fi
else
    echo "  - MCP 工具配置: (已跳過)"
fi
echo ""
echo "感謝使用 SunnyCore！"
