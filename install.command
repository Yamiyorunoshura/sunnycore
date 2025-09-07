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
AGENTS_COMMANDS_DIR=""
OTHER_FILES_DIR=""
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
    
    echo -e "\n${BLUE}請選擇 Claude Code 安裝類型:${NC}"
    echo "1) 全局安裝 (agents/commands → ~/.claude，其他文件 → 用戶指定路徑/sunnycore)"
    echo "2) 專案安裝 (agents/commands → 專案路徑/.claude，其他文件 → 專案路徑/sunnycore)"
    echo ""
    
    while true; do
        read -p "請輸入選項 (1-2): " choice
        case $choice in
            1)
                INSTALL_TYPE="global"
                AGENTS_COMMANDS_DIR="$HOME/.claude"
                break
                ;;
            2)
                INSTALL_TYPE="project"
                break
                ;;
            *)
                show_error "無效選項，請重新輸入"
                ;;
        esac
    done
}

# 設定安裝路徑
setup_paths() {
    if [ "$VERSION" = "warp code" ]; then
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
            OTHER_FILES_DIR="$project_path/sunnycore"
            break
        done
        return
    fi
    
    # Claude Code 安裝路徑設定
    if [ "$INSTALL_TYPE" = "global" ]; then
        echo -e "\n${BLUE}設定全局安裝路徑${NC}"
        echo -e "agents 和 commands 將安裝到: ${YELLOW}~/.claude${NC}"
        
        # 設定其他檔案的安裝路徑
        while true; do
            read -p "請輸入 sunnycore 等其他檔案的安裝根目錄路徑: " base_path
            if [ -z "$base_path" ]; then
                show_error "路徑不能為空"
                continue
            fi
            
            # 展開波浪號
            base_path="${base_path/#\~/$HOME}"
            
            if [ ! -d "$base_path" ]; then
                read -p "目錄 '$base_path' 不存在，是否創建? (y/N): " create_dir
                if [ "$create_dir" = "y" ] || [ "$create_dir" = "Y" ]; then
                    mkdir -p "$base_path" || {
                        show_error "無法創建目錄 '$base_path'"
                        continue
                    }
                else
                    continue
                fi
            fi
            
            OTHER_FILES_DIR="$base_path/sunnycore"
            break
        done
        
    elif [ "$INSTALL_TYPE" = "project" ]; then
        echo -e "\n${BLUE}設定專案安裝路徑${NC}"
        
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
            
            # 設定 Claude Code 專案安裝的路徑
            AGENTS_COMMANDS_DIR="$project_path/.claude"
            OTHER_FILES_DIR="$project_path/sunnycore"
            break
        done
    fi
}

# 選擇版本
select_version() {
    echo -e "\n${BLUE}請選擇要安裝的版本:${NC}"
    echo "1) Claude Code (預設) - 支援全域和自訂安裝"
    echo "2) Warp Code - 僅支援專案目錄安裝"
    echo "3) Codex Code - 支援全域和自訂安裝"
    echo ""
    
    while true; do
        read -p "請輸入選項 (1-3): " choice
        case $choice in
            1|"")
                VERSION="claude code"
                break
                ;;
            2)
                VERSION="warp code"
                break
                ;;
            3)
                VERSION="codex code"
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
    show_info "檢查舊配置..."
    
    local old_configs_found=false
    local configs_to_remove=()
    
    if [ "$VERSION" = "claude code" ]; then
        # 檢查 agents 和 commands 目錄中的舊配置
        if [ -d "$AGENTS_COMMANDS_DIR/agents" ]; then
            old_configs_found=true
            configs_to_remove+=("agents 配置目錄: $AGENTS_COMMANDS_DIR/agents")
        fi
        
        if [ -d "$AGENTS_COMMANDS_DIR/commands" ]; then
            old_configs_found=true
            configs_to_remove+=("commands 配置目錄: $AGENTS_COMMANDS_DIR/commands")
        fi
        
        # 檢查 sunnycore 目錄中的舊配置
        if [ -d "$OTHER_FILES_DIR" ] && [ "$(ls -A "$OTHER_FILES_DIR" 2>/dev/null)" ]; then
            old_configs_found=true
            configs_to_remove+=("sunnycore 配置目錄: $OTHER_FILES_DIR")
        fi
        
    elif [ "$VERSION" = "warp code" ]; then
        # 檢查 warp code 目錄中的舊配置
        if [ -d "$OTHER_FILES_DIR" ] && [ "$(ls -A "$OTHER_FILES_DIR" 2>/dev/null)" ]; then
            old_configs_found=true
            configs_to_remove+=("warp code 配置目錄: $OTHER_FILES_DIR")
        fi
    fi
    
    # 如果找到舊配置，詢問用戶是否移除
    if [ "$old_configs_found" = true ]; then
        echo -e "\n${YELLOW}發現以下舊配置:${NC}"
        for config in "${configs_to_remove[@]}"; do
            echo -e "  - $config"
        done
        echo ""
        
        read -p "是否移除這些舊配置? (y/N): " confirm_remove
        if [ "$confirm_remove" = "y" ] || [ "$confirm_remove" = "Y" ]; then
            show_info "開始移除舊配置..."
            
            if [ "$VERSION" = "claude code" ]; then
                # 移除 agents 和 commands 目錄中的舊配置
                if [ -d "$AGENTS_COMMANDS_DIR/agents" ]; then
                    show_warning "移除舊的 agents 配置..."
                    rm -rf "$AGENTS_COMMANDS_DIR/agents"
                    show_success "舊 agents 配置已移除"
                fi
                
                if [ -d "$AGENTS_COMMANDS_DIR/commands" ]; then
                    show_warning "移除舊的 commands 配置..."
                    rm -rf "$AGENTS_COMMANDS_DIR/commands"
                    show_success "舊 commands 配置已移除"
                fi
                
                # 移除 sunnycore 目錄中的舊配置
                if [ -d "$OTHER_FILES_DIR" ] && [ "$(ls -A "$OTHER_FILES_DIR" 2>/dev/null)" ]; then
                    show_warning "移除舊的 sunnycore 配置..."
                    rm -rf "$OTHER_FILES_DIR"/*
                    show_success "舊 sunnycore 配置已移除"
                fi
                
            elif [ "$VERSION" = "warp code" ]; then
                # 移除整個 warp code 目錄中的舊配置
                if [ -d "$OTHER_FILES_DIR" ] && [ "$(ls -A "$OTHER_FILES_DIR" 2>/dev/null)" ]; then
                    show_warning "移除舊的 warp code 配置..."
                    rm -rf "$OTHER_FILES_DIR"/*
                    show_success "舊 warp code 配置已移除"
                fi
            fi
        else
            show_warning "保留舊配置，可能會與新安裝產生衝突"
        fi
    else
        show_success "未發現舊配置，可以直接安裝"
    fi
}

# 安裝檔案
install_files() {
    show_info "開始安裝檔案..."

    # 先安裝 general 檔案至 $OTHER_FILES_DIR
    if [ -d "$TEMP_DIR/general" ]; then
        show_info "安裝 general 檔案到 $OTHER_FILES_DIR"
        mkdir -p "$OTHER_FILES_DIR"
        if cp -a "$TEMP_DIR/general/." "$OTHER_FILES_DIR/"; then
            show_success "general 檔案安裝完成"
        else
            show_error "general 檔案安裝失敗"
            exit 1
        fi
    else
        show_warning "找不到 'general' 目錄，跳過通用檔案安裝"
    fi

    if [ "$VERSION" = "claude code" ]; then
        # 檢查 claude code 目錄是否存在
        if [ ! -d "$TEMP_DIR/claude code" ]; then
            show_error "找不到 'claude code' 目錄"
            exit 1
        fi
        
        cd "$TEMP_DIR/claude code"
        
        # 安裝 agents 和 commands 到指定目錄
        if [ -d "agents" ]; then
            show_info "安裝 agents 到 $AGENTS_COMMANDS_DIR"
            mkdir -p "$AGENTS_COMMANDS_DIR"
            cp -r agents "$AGENTS_COMMANDS_DIR/"
            show_success "agents 安裝完成"
        else
            show_warning "未找到 agents 目錄"
        fi
        
        if [ -d "commands" ]; then
            show_info "安裝 commands 到 $AGENTS_COMMANDS_DIR"
            mkdir -p "$AGENTS_COMMANDS_DIR"
            cp -r commands "$AGENTS_COMMANDS_DIR/"
            show_success "commands 安裝完成"
        else
            show_warning "未找到 commands 目錄"
        fi
        
        # 安裝其他檔案（sunnycore 等）到指定目錄
        show_info "安裝其他檔案到 $OTHER_FILES_DIR"
        mkdir -p "$OTHER_FILES_DIR"
        
        # 複製除了 agents 和 commands 之外的所有檔案和目錄
        for item in *; do
            if [ "$item" != "agents" ] && [ "$item" != "commands" ]; then
                if [ -e "$item" ]; then
                    # CLAUDE.md 檔案特殊處理
                    if [ "$item" = "CLAUDE.md" ] && [ -f "$OTHER_FILES_DIR/CLAUDE.md" ]; then
                        echo -e "\n${YELLOW}發現現有的 CLAUDE.md 檔案${NC}"
                        echo "現有檔案: $OTHER_FILES_DIR/CLAUDE.md"
                        echo "新檔案: $PWD/$item"
                        echo ""
                        echo "請選擇處理方式:"
                        echo "1) 備份現有檔案並安裝新檔案"
                        echo "2) 保留現有檔案，跳過新檔案"
                        echo "3) 覆蓋現有檔案（不備份）"
                        echo ""
                        
                        while true; do
                            read -p "請輸入選項 (1-3): " claude_choice
                            case $claude_choice in
                                1)
                                    # 備份現有檔案
                                    backup_file="$OTHER_FILES_DIR/CLAUDE.md.backup.$(date +%Y%m%d_%H%M%S)"
                                    mv "$OTHER_FILES_DIR/CLAUDE.md" "$backup_file"
                                    show_success "現有 CLAUDE.md 已備份至 $backup_file"
                                    cp "$item" "$OTHER_FILES_DIR/"
                                    show_success "已安裝新的 CLAUDE.md"
                                    break
                                    ;;
                                2)
                                    show_info "保留現有 CLAUDE.md，跳過新檔案"
                                    break
                                    ;;
                                3)
                                    cp "$item" "$OTHER_FILES_DIR/"
                                    show_success "已覆蓋 CLAUDE.md"
                                    break
                                    ;;
                                *)
                                    show_error "無效選項，請重新輸入"
                                    ;;
                            esac
                        done
                    else
                        # 其他檔案正常複製
                        cp -r "$item" "$OTHER_FILES_DIR/"
                        show_success "已安裝 $item"
                    fi
                fi
            fi
        done
        
    elif [ "$VERSION" = "warp code" ]; then
        # 檢查 warp code 目錄是否存在
        if [ ! -d "$TEMP_DIR/warp code" ]; then
            show_error "找不到 'warp code' 目錄"
            exit 1
        fi
        
        cd "$TEMP_DIR/warp code"
        
        # 複製 warp code 目錄中的所有內容到 sunnycore 目錄
        show_info "安裝 warp code 所有內容到 $OTHER_FILES_DIR"
        mkdir -p "$OTHER_FILES_DIR"
        
        # 複製當前目錄下的所有檔案和資料夾
        if cp -r . "$OTHER_FILES_DIR/"; then
            show_success "warp code 所有內容安裝完成"
        else
            show_error "warp code 內容安裝失敗"
            exit 1
        fi
    elif [ "$VERSION" = "codex code" ]; then
        # 檢查 codex code 目錄是否存在
        if [ ! -d "$TEMP_DIR/codex code" ]; then
            show_error "找不到 'codex code' 目錄"
            exit 1
        fi

        cd "$TEMP_DIR/codex code"

        # 若有 agents/commands，則安裝到 AGENTS_COMMANDS_DIR
        if [ -d "agents" ]; then
            show_info "安裝 agents 到 $AGENTS_COMMANDS_DIR"
            mkdir -p "$AGENTS_COMMANDS_DIR"
            cp -r agents "$AGENTS_COMMANDS_DIR/"
            show_success "agents 安裝完成"
        fi
        if [ -d "commands" ]; then
            show_info "安裝 commands 到 $AGENTS_COMMANDS_DIR"
            mkdir -p "$AGENTS_COMMANDS_DIR"
            cp -r commands "$AGENTS_COMMANDS_DIR/"
            show_success "commands 安裝完成"
        fi

        # 其餘檔案安裝到 OTHER_FILES_DIR（sunnycore）
        show_info "安裝 codex code 其他檔案到 $OTHER_FILES_DIR"
        mkdir -p "$OTHER_FILES_DIR"
        for item in *; do
            if [ "$item" != "agents" ] && [ "$item" != "commands" ]; then
                [ -e "$item" ] && cp -r "$item" "$OTHER_FILES_DIR/" && show_success "已安裝 $item"
            fi
        done
    fi
}


# 顯示安裝總結
show_summary() {
    echo -e "\n${GREEN}=================================="
    echo -e "        安裝完成！"
    echo -e "==================================${NC}"
    echo -e "\n${BLUE}安裝資訊:${NC}"
    echo -e "版本: $VERSION"
    echo -e "安裝類型: $INSTALL_TYPE"
    echo -e "Git 分支: $LATEST_VERSION"
    
    if [ "$VERSION" = "claude code" ] || [ "$VERSION" = "codex code" ]; then
        echo -e "Agents/Commands 目錄: $AGENTS_COMMANDS_DIR"
        echo -e "其他檔案目錄: $OTHER_FILES_DIR"
    elif [ "$VERSION" = "warp code" ]; then
        echo -e "安裝目錄: $OTHER_FILES_DIR"
    fi
    
    echo -e "\n${BLUE}已安裝的組件:${NC}"
    if [ "$VERSION" = "claude code" ] || [ "$VERSION" = "codex code" ]; then
        [ -d "$AGENTS_COMMANDS_DIR/agents" ] && echo -e "✓ Agents (安裝至 $AGENTS_COMMANDS_DIR)"
        [ -d "$AGENTS_COMMANDS_DIR/commands" ] && echo -e "✓ Commands (安裝至 $AGENTS_COMMANDS_DIR)"
        
        # 檢查其他檔案是否存在
        if [ -d "$OTHER_FILES_DIR" ] && [ "$(ls -A "$OTHER_FILES_DIR" 2>/dev/null)" ]; then
            echo -e "✓ 其他檔案已安裝至 $OTHER_FILES_DIR"
            [ -d "$OTHER_FILES_DIR/sunnycore" ] && echo -e "  - SunnyCore"
            [ -f "$OTHER_FILES_DIR/CLAUDE.md" ] && echo -e "  - CLAUDE.md"
            [ -f "$OTHER_FILES_DIR/install.command" ] && echo -e "  - install.command"
        fi
    elif [ "$VERSION" = "warp code" ]; then
        if [ -d "$OTHER_FILES_DIR" ] && [ "$(ls -A "$OTHER_FILES_DIR" 2>/dev/null)" ]; then
            echo -e "✓ Warp Code 所有內容已安裝到 $OTHER_FILES_DIR"
            # 顯示安裝的主要目錄
            [ -d "$OTHER_FILES_DIR/agents" ] && echo -e "  - Agents"
            [ -d "$OTHER_FILES_DIR/tasks" ] && echo -e "  - Tasks"
            [ -d "$OTHER_FILES_DIR/templates" ] && echo -e "  - Templates"
        else
            echo -e "✗ Warp Code 安裝未完成"
        fi
    fi
    
    echo -e "\n${YELLOW}注意事項:${NC}"
    echo -e "• 請確保 Claude Code 能夠訪問安裝目錄"
    if [ "$VERSION" = "claude code" ]; then
        echo -e "• Agents 和 Commands 位於: $AGENTS_COMMANDS_DIR"
        echo -e "• 其他檔案位於: $OTHER_FILES_DIR"
    fi
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
    setup_paths
    
    # 確認安裝資訊
    echo -e "\n${BLUE}安裝確認:${NC}"
    echo -e "版本: $VERSION"
    echo -e "安裝類型: $INSTALL_TYPE"
    
    if [ "$VERSION" = "claude code" ]; then
        echo -e "Agents/Commands 安裝目錄: $AGENTS_COMMANDS_DIR"
        echo -e "其他檔案安裝目錄: $OTHER_FILES_DIR"
    elif [ "$VERSION" = "warp code" ]; then
        echo -e "安裝目錄: $OTHER_FILES_DIR"
    fi
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
