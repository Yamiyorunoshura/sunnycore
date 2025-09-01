#!/bin/bash

# SunnyCore 安裝腳本
echo "========================================"
echo "        SunnyCore 安裝程式"
echo "========================================"
echo ""

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

echo ""
echo "開始安裝..."
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
echo "感謝使用 SunnyCore！"
