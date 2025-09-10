#!/bin/bash

# 分支同步腳本 - 同步兩個分支的共有文件
# 用途：更新目標分支與源分支共有的內容，同時保留目標分支獨有的文件
# 作者：AI Assistant
# 日期：$(date +%Y-%m-%d)

set -e  # 遇到錯誤時退出

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 函數：顯示使用說明
show_usage() {
    echo -e "${BLUE}分支同步腳本 - 同步共有文件${NC}"
    echo ""
    echo "用途：將源分支的共有文件內容同步到目標分支，保留目標分支獨有文件"
    echo ""
    echo "使用方法："
    echo "  $0 <源分支> <目標分支> [選項]"
    echo ""
    echo "參數："
    echo "  源分支     要同步內容的來源分支"
    echo "  目標分支   要更新的目標分支"
    echo ""
    echo "選項："
    echo "  -h, --help     顯示此幫助信息"
    echo "  -n, --dry-run  預覽模式，不實際執行更改"
    echo "  -y, --yes      自動確認所有操作"
    echo ""
    echo "範例："
    echo "  $0 warp-code/v0.3.0 master"
    echo "  $0 feature/new-feature develop --dry-run"
}

# 函數：檢查 Git 倉庫
check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        echo -e "${RED}錯誤：當前目錄不是 Git 倉庫${NC}"
        exit 1
    fi
}

# 函數：檢查分支是否存在
check_branch_exists() {
    local branch=$1
    if ! git show-ref --verify --quiet refs/heads/$branch && ! git show-ref --verify --quiet refs/remotes/origin/$branch; then
        echo -e "${RED}錯誤：分支 '$branch' 不存在${NC}"
        exit 1
    fi
}

# 函數：獲取共有文件列表
get_common_files() {
    local source_branch=$1
    local target_branch=$2
    local temp_dir="/tmp/sync_branches_$$"
    
    mkdir -p "$temp_dir"
    
    # 獲取兩個分支的文件列表
    git ls-tree -r --name-only "$source_branch" | sort > "$temp_dir/source_files.txt"
    git ls-tree -r --name-only "$target_branch" | sort > "$temp_dir/target_files.txt"
    
    # 找出共有文件（排除 .DS_Store）
    comm -12 "$temp_dir/source_files.txt" "$temp_dir/target_files.txt" | grep -v '\.DS_Store$' > "$temp_dir/common_files.txt"
    
    echo "$temp_dir/common_files.txt"
}

# 函數：顯示文件統計
show_file_stats() {
    local source_branch=$1
    local target_branch=$2
    local common_files_path=$3
    
    local source_count=$(git ls-tree -r --name-only "$source_branch" | wc -l | tr -d ' ')
    local target_count=$(git ls-tree -r --name-only "$target_branch" | wc -l | tr -d ' ')
    local common_count=$(cat "$common_files_path" | wc -l | tr -d ' ')
    local target_only=$((target_count - common_count))
    
    echo -e "${BLUE}文件統計：${NC}"
    echo "  源分支 ($source_branch): $source_count 個文件"
    echo "  目標分支 ($target_branch): $target_count 個文件"
    echo -e "  ${GREEN}共有文件: $common_count 個${NC}"
    echo -e "  ${YELLOW}目標分支獨有: $target_only 個（將被保留）${NC}"
}

# 函數：執行同步
perform_sync() {
    local source_branch=$1
    local target_branch=$2
    local common_files_path=$3
    local dry_run=$4
    
    echo -e "\n${BLUE}開始同步共有文件...${NC}"
    
    local updated_count=0
    
    while IFS= read -r file; do
        if [ -n "$file" ]; then
            if [ "$dry_run" = "true" ]; then
                echo -e "${YELLOW}[預覽] 將更新文件: $file${NC}"
            else
                echo "更新文件: $file"
                git checkout "$source_branch" -- "$file"
            fi
            ((updated_count++))
        fi
    done < "$common_files_path"
    
    echo -e "\n${GREEN}完成！共處理 $updated_count 個文件${NC}"
    
    if [ "$dry_run" = "false" ]; then
        # 檢查是否有更改
        if git diff --cached --quiet; then
            echo -e "${YELLOW}沒有檢測到文件更改${NC}"
        else
            echo -e "\n${BLUE}準備提交更改...${NC}"
            git status --short
        fi
    fi
}

# 函數：提交更改
commit_changes() {
    local source_branch=$1
    local target_branch=$2
    local updated_count=$3
    
    local commit_message="同步 $source_branch 分支的共有文件內容到 $target_branch

- 更新了兩個分支共有的 $updated_count 個文件
- 保留了 $target_branch 分支獨有的文件
- 確保只同步共有內容，避免覆蓋分支特有檔案

自動生成於: $(date '+%Y-%m-%d %H:%M:%S')"
    
    git add .
    git commit -m "$commit_message"
    
    echo -e "${GREEN}更改已成功提交！${NC}"
}

# 主函數
main() {
    local source_branch=""
    local target_branch=""
    local dry_run="false"
    local auto_yes="false"
    
    # 解析命令行參數
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                show_usage
                exit 0
                ;;
            -n|--dry-run)
                dry_run="true"
                shift
                ;;
            -y|--yes)
                auto_yes="true"
                shift
                ;;
            -*)
                echo -e "${RED}錯誤：未知選項 $1${NC}"
                show_usage
                exit 1
                ;;
            *)
                if [ -z "$source_branch" ]; then
                    source_branch="$1"
                elif [ -z "$target_branch" ]; then
                    target_branch="$1"
                else
                    echo -e "${RED}錯誤：過多的參數${NC}"
                    show_usage
                    exit 1
                fi
                shift
                ;;
        esac
    done
    
    # 檢查必需參數
    if [ -z "$source_branch" ] || [ -z "$target_branch" ]; then
        echo -e "${RED}錯誤：缺少必需的參數${NC}"
        show_usage
        exit 1
    fi
    
    # 檢查 Git 倉庫和分支
    check_git_repo
    check_branch_exists "$source_branch"
    check_branch_exists "$target_branch"
    
    # 保存當前分支
    local current_branch=$(git branch --show-current)
    
    echo -e "${BLUE}分支同步操作${NC}"
    echo "源分支: $source_branch"
    echo "目標分支: $target_branch"
    echo "當前分支: $current_branch"
    
    if [ "$dry_run" = "true" ]; then
        echo -e "${YELLOW}模式: 預覽模式（不會實際修改文件）${NC}"
    fi
    
    # 獲取共有文件
    echo -e "\n${BLUE}分析分支文件...${NC}"
    local common_files_path=$(get_common_files "$source_branch" "$target_branch")
    
    # 顯示統計信息
    show_file_stats "$source_branch" "$target_branch" "$common_files_path"
    
    # 確認操作
    if [ "$auto_yes" = "false" ] && [ "$dry_run" = "false" ]; then
        echo -e "\n${YELLOW}是否繼續執行同步操作？ (y/N)${NC}"
        read -r response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            echo "操作已取消"
            exit 0
        fi
    fi
    
    # 切換到目標分支
    if [ "$current_branch" != "$target_branch" ] && [ "$dry_run" = "false" ]; then
        echo -e "\n${BLUE}切換到目標分支 $target_branch...${NC}"
        git checkout "$target_branch"
    fi
    
    # 執行同步
    perform_sync "$source_branch" "$target_branch" "$common_files_path" "$dry_run"
    
    # 提交更改（非預覽模式）
    if [ "$dry_run" = "false" ] && ! git diff --cached --quiet; then
        local updated_count=$(cat "$common_files_path" | wc -l | tr -d ' ')
        
        if [ "$auto_yes" = "false" ]; then
            echo -e "\n${YELLOW}是否提交這些更改？ (y/N)${NC}"
            read -r response
            if [[ "$response" =~ ^[Yy]$ ]]; then
                commit_changes "$source_branch" "$target_branch" "$updated_count"
            else
                echo -e "${YELLOW}更改已暫存但未提交${NC}"
            fi
        else
            commit_changes "$source_branch" "$target_branch" "$updated_count"
        fi
    fi
    
    # 清理臨時文件
    rm -rf "/tmp/sync_branches_$$"
    
    echo -e "\n${GREEN}同步操作完成！${NC}"
}

# 執行主函數
main "$@"