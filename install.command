#!/bin/bash

# SunnyCore MCP Tools 安裝腳本
# 版本: 1.0
# 支援平台: macOS, Linux

set -e

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 全域變數
GITHUB_REPO="https://github.com/Yamiyorunoshura/sunnycore.git"
INSTALL_TYPE=""
CLAUDE_DIR=""
SUNNYCORE_DIR=""
VERSION="claude code"
TEMP_DIR=""

# 顯示標題
show_header() {
    echo -e "${BLUE}=================================="
    echo -e "   SunnyCore MCP Tools 安裝程式"
    echo -e "=================================="
    echo -e "${NC}"
}

# 顯示錯誤訊息
show_error() {
    echo -e "${RED}[錯誤] $1${NC}"
}

# 顯示成功訊息
show_success() {
    echo -e "${GREEN}[成功] $1${NC}"
}

# 顯示警告訊息
show_warning() {
    echo -e "${YELLOW}[警告] $1${NC}"
}

# 顯示資訊訊息
show_info() {
    echo -e "${BLUE}[資訊] $1${NC}"
}

# 檢查必要工具
check_prerequisites() {
    show_info "檢查必要工具..."
    
    if ! command -v git &> /dev/null; then
        show_error "Git 未安裝。請先安裝 Git。"
        exit 1
    fi
    
    if ! command -v curl &> /dev/null; then
        show_error "curl 未安裝。請先安裝 curl。"
        exit 1
    fi
    
    show_success "必要工具檢查完成"
}

# 選擇安裝類型
select_install_type() {
    if [ "$VERSION" = "warp code" ]; then
        echo -e "\n${BLUE}Warp Code 安裝類型:${NC}"
        echo "Warp Code 僅支援專案目錄安裝"
        INSTALL_TYPE="project"
        return
    fi
    
    echo -e "\n${BLUE}請選擇安裝類型:${NC}"
    echo "1) 全局安裝 (推薦)"
    echo "2) 自訂路徑安裝"
    echo ""
    
    while true; do
        read -p "請輸入選項 (1-2): " choice
        case $choice in
            1)
                INSTALL_TYPE="global"
                CLAUDE_DIR="$HOME/.claude"
                break
                ;;
            2)
                INSTALL_TYPE="custom"
                break
                ;;
            *)
                show_error "無效選項，請重新輸入"
                ;;
        esac
    done
}

# 設定自訂路徑
setup_custom_paths() {
    if [ "$INSTALL_TYPE" = "project" ]; then
        echo -e "\n${BLUE}設定 Warp Code 專案安裝路徑${NC}"
        
        # 設定專案根目錄
        while true; do
            read -p "請輸入專案根目錄路徑: " project_path
            if [ -z "$project_path" ]; then
                show_error "路徑不能為空"
                continue
            fi
            
            # 展開波浪號
            project_path="${project_path/#\~/$HOME}"
            
            if [ ! -d "$project_path" ]; then
                read -p "目錄 '$project_path' 不存在，是否創建? (y/N): " create_dir
                if [ "$create_dir" = "y" ] || [ "$create_dir" = "Y" ]; then
                    mkdir -p "$project_path" || {
                        show_error "無法創建目錄 '$project_path'"
                        continue
                    }
                else
                    continue
                fi
            fi
            
            # 設定 Warp Code 的安裝路徑
            CLAUDE_DIR="$project_path"
            SUNNYCORE_DIR="$project_path/sunnycore"
            break
        done
        return
    fi
    
    if [ "$INSTALL_TYPE" = "custom" ]; then
        echo -e "\n${BLUE}設定自訂安裝路徑${NC}"
        
        # 設定 Claude 目錄
        while true; do
            read -p "請輸入 agents 和 commands 資料夾的安裝路徑: " claude_path
            if [ -z "$claude_path" ]; then
                show_error "路徑不能為空"
                continue
            fi
            
            # 展開波浪號
            claude_path="${claude_path/#\~/$HOME}"
            
            if [ ! -d "$claude_path" ]; then
                read -p "目錄 '$claude_path' 不存在，是否創建? (y/N): " create_dir
                if [ "$create_dir" = "y" ] || [ "$create_dir" = "Y" ]; then
                    mkdir -p "$claude_path" || {
                        show_error "無法創建目錄 '$claude_path'"
                        continue
                    }
                else
                    continue
                fi
            fi
            
            CLAUDE_DIR="$claude_path"
            break
        done
    fi
    
    # 設定 sunnycore 目錄 (僅對 Claude Code 的 custom 安裝)
    if [ "$VERSION" = "claude code" ] && [ "$INSTALL_TYPE" = "custom" ]; then
        while true; do
            read -p "請輸入 sunnycore 資料夾的安裝路徑: " sunnycore_path
            if [ -z "$sunnycore_path" ]; then
                show_error "路徑不能為空"
                continue
            fi
            
            # 展開波浪號
            sunnycore_path="${sunnycore_path/#\~/$HOME}"
            
            if [ ! -d "$sunnycore_path" ]; then
                read -p "目錄 '$sunnycore_path' 不存在，是否創建? (y/N): " create_dir
                if [ "$create_dir" = "y" ] || [ "$create_dir" = "Y" ]; then
                    mkdir -p "$sunnycore_path" || {
                        show_error "無法創建目錄 '$sunnycore_path'"
                        continue
                    }
                else
                    continue
                fi
            fi
            
            SUNNYCORE_DIR="$sunnycore_path"
            break
        done
    elif [ "$VERSION" = "claude code" ] && [ "$INSTALL_TYPE" = "global" ]; then
        SUNNYCORE_DIR="$HOME/.claude"
    fi
}

# 選擇版本
select_version() {
    echo -e "\n${BLUE}請選擇要安裝的版本:${NC}"
    echo "1) Claude Code (預設) - 支援全域和自訂安裝"
    echo "2) Warp Code - 僅支援專案目錄安裝"
    echo ""
    
    while true; do
        read -p "請輸入選項 (1-2): " choice
        case $choice in
            1|"")
                VERSION="claude code"
                break
                ;;
            2)
                VERSION="warp code"
                break
                ;;
            *)
                show_error "無效選項，請重新輸入"
                ;;
        esac
    done
}

# 獲取最新版本
get_latest_version() {
    show_info "檢查最新版本..."
    
    # 檢查 release 分支是否存在
    if ! git ls-remote --heads "$GITHUB_REPO" release/* &>/dev/null; then
        show_warning "未找到 release 分支，使用 main 分支"
        LATEST_VERSION="main"
        return
    fi
    
    # 獲取所有 release 分支
    RELEASE_BRANCHES=$(git ls-remote --heads "$GITHUB_REPO" | grep "refs/heads/release/" | awk '{print $2}' | sed 's|refs/heads/||' | sort -V)
    
    if [ -z "$RELEASE_BRANCHES" ]; then
        show_warning "未找到 release 分支，使用 main 分支"
        LATEST_VERSION="main"
    else
        LATEST_VERSION=$(echo "$RELEASE_BRANCHES" | tail -n 1)
        show_info "找到最新版本: $LATEST_VERSION"
    fi
}

# 下載倉庫
download_repository() {
    show_info "下載倉庫..."
    
    TEMP_DIR=$(mktemp -d)
    trap "rm -rf $TEMP_DIR" EXIT
    
    cd "$TEMP_DIR"
    
    if ! git clone --depth 1 --branch "$LATEST_VERSION" "$GITHUB_REPO" . 2>/dev/null; then
        show_error "下載倉庫失敗"
        exit 1
    fi
    
    show_success "倉庫下載完成"
}

# 移除舊配置
remove_old_configs() {
    show_info "檢查並移除舊配置..."
    
    # 移除 Claude 目錄中的舊 agents 和 commands
    if [ -d "$CLAUDE_DIR/agents" ]; then
        show_warning "發現舊的 agents 配置，正在移除..."
        rm -rf "$CLAUDE_DIR/agents"
        show_success "舊 agents 配置已移除"
    fi
    
    if [ -d "$CLAUDE_DIR/commands" ]; then
        show_warning "發現舊的 commands 配置，正在移除..."
        rm -rf "$CLAUDE_DIR/commands"
        show_success "舊 commands 配置已移除"
    fi
    
    # 移除 sunnycore 目錄中的舊配置
    if [ -d "$SUNNYCORE_DIR/sunnycore" ]; then
        show_warning "發現舊的 sunnycore 配置，正在移除..."
        rm -rf "$SUNNYCORE_DIR/sunnycore"
        show_success "舊 sunnycore 配置已移除"
    fi
}

# 安裝檔案
install_files() {
    show_info "開始安裝檔案..."
    
    if [ "$VERSION" = "claude code" ]; then
        # 檢查 claude code 目錄是否存在
        if [ ! -d "$TEMP_DIR/claude code" ]; then
            show_error "找不到 'claude code' 目錄"
            exit 1
        fi
        
        cd "$TEMP_DIR/claude code"
        
        # 安裝 agents 和 commands 到 Claude 目錄
        if [ -d "agents" ]; then
            show_info "安裝 agents 到 $CLAUDE_DIR"
            mkdir -p "$CLAUDE_DIR"
            cp -r agents "$CLAUDE_DIR/"
            show_success "agents 安裝完成"
        else
            show_warning "未找到 agents 目錄"
        fi
        
        if [ -d "commands" ]; then
            show_info "安裝 commands 到 $CLAUDE_DIR"
            mkdir -p "$CLAUDE_DIR"
            cp -r commands "$CLAUDE_DIR/"
            show_success "commands 安裝完成"
        else
            show_warning "未找到 commands 目錄"
        fi
        
        # 安裝 sunnycore 到指定目錄
        if [ -d "sunnycore" ]; then
            show_info "安裝 sunnycore 到 $SUNNYCORE_DIR"
            mkdir -p "$SUNNYCORE_DIR"
            cp -r sunnycore "$SUNNYCORE_DIR/"
            show_success "sunnycore 安裝完成"
        else
            show_warning "未找到 sunnycore 目錄"
        fi
        
    elif [ "$VERSION" = "warp code" ]; then
        # 檢查 warp code 目錄是否存在
        if [ ! -d "$TEMP_DIR/warp code" ]; then
            show_error "找不到 'warp code' 目錄"
            exit 1
        fi
        
        cd "$TEMP_DIR/warp code"
        
        # 複製 warp code 目錄中的所有內容到 sunnycore 目錄
        show_info "安裝 warp code 所有內容到 $SUNNYCORE_DIR"
        mkdir -p "$SUNNYCORE_DIR"
        
        # 複製當前目錄下的所有檔案和資料夾
        if cp -r . "$SUNNYCORE_DIR/"; then
            show_success "warp code 所有內容安裝完成"
        else
            show_error "warp code 內容安裝失敗"
            exit 1
        fi
    fi
}


# 顯示安裝總結
show_summary() {
    echo -e "\n${GREEN}=================================="
    echo -e "        安裝完成！"
    echo -e "==================================${NC}"
    echo -e "\n${BLUE}安裝資訊:${NC}"
    echo -e "版本: $VERSION"
    echo -e "Git 分支: $LATEST_VERSION"
    echo -e "Claude 目錄: $CLAUDE_DIR"
    echo -e "SunnyCore 目錄: $SUNNYCORE_DIR"
    
    echo -e "\n${BLUE}已安裝的組件:${NC}"
    if [ "$VERSION" = "claude code" ]; then
        [ -d "$CLAUDE_DIR/agents" ] && echo -e "✓ Agents"
        [ -d "$CLAUDE_DIR/commands" ] && echo -e "✓ Commands"
        [ -d "$SUNNYCORE_DIR/sunnycore" ] && echo -e "✓ SunnyCore"
    elif [ "$VERSION" = "warp code" ]; then
        if [ -d "$SUNNYCORE_DIR" ] && [ "$(ls -A "$SUNNYCORE_DIR" 2>/dev/null)" ]; then
            echo -e "✓ Warp Code 所有內容已安裝到 sunnycore 目錄"
            # 顯示安裝的主要目錄
            [ -d "$SUNNYCORE_DIR/agents" ] && echo -e "  - Agents"
            [ -d "$SUNNYCORE_DIR/tasks" ] && echo -e "  - Tasks"
            [ -d "$SUNNYCORE_DIR/templates" ] && echo -e "  - Templates"
        else
            echo -e "✗ Warp Code 安裝未完成"
        fi
    fi
    
    echo -e "\n${YELLOW}注意事項:${NC}"
    echo -e "• 請確保 Claude Code 能夠訪問安裝目錄"
    echo -e "• 如果需要更新，請重新執行此安裝腳本"
    echo ""
}

# 主程式
main() {
    show_header
    
    # 檢查必要工具
    check_prerequisites
    
    # 選擇版本 (放在安裝類型之前)
    select_version
    
    # 選擇安裝類型
    select_install_type
    
    # 設定路徑
    setup_custom_paths
    
    # 確認安裝資訊
    echo -e "\n${BLUE}安裝確認:${NC}"
    echo -e "版本: $VERSION"
    echo -e "安裝類型: $INSTALL_TYPE"
    echo -e "Claude 目錄: $CLAUDE_DIR"
    echo -e "SunnyCore 目錄: $SUNNYCORE_DIR"
    echo ""
    
    read -p "確認安裝? (y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        show_info "安裝已取消"
        exit 0
    fi
    
    # 執行安裝 - 統一流程，根據版本安裝不同目錄內容
    get_latest_version
    download_repository
    remove_old_configs
    install_files
    
    # 顯示總結
    show_summary
}

# 執行主程式
main "$@"