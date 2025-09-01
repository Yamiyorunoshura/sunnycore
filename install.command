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

# 獲取安裝目錄
read -p "請輸入安裝目錄 (絕對路徑或 ~ 路徑): " INSTALL_DIR

# 處理 ~ 路徑
if [[ "$INSTALL_DIR" == ~* ]]; then
    # 展開 ~ 路徑
    eval INSTALL_DIR="$INSTALL_DIR"
fi

# 檢查目錄是否存在，如果不存在則創建
if [ ! -d "$INSTALL_DIR" ]; then
    echo "目錄不存在，正在創建: $INSTALL_DIR"
    mkdir -p "$INSTALL_DIR"
    if [ $? -ne 0 ]; then
        echo "錯誤: 無法創建目錄 $INSTALL_DIR"
        exit 1
    fi
fi

echo "安裝目錄: $INSTALL_DIR"
echo ""

# 選擇版本
echo "請選擇要安裝的版本:"
echo "1) claude (自動選擇最新版本)"
echo "2) deepseek (自動選擇最新版本)"
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
            VERSION_TYPE="deepseek"
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

# 需要複製的文件夾
FOLDERS=("agents" "commands" "sunnycore")

for folder in "${FOLDERS[@]}"; do
    if [ -d "$TEMP_DIR/sunnycore/$folder" ]; then
        echo "複製 $folder..."
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

echo ""

# 清理臨時文件
echo "清理臨時文件..."
rm -rf "$TEMP_DIR"

echo ""
echo "========================================"
echo "        安裝完成！"
echo "========================================"
echo ""
echo "已安裝文件至: $INSTALL_DIR"
echo "安裝的分支: $BRANCH"
echo "版本類型: $VERSION_TYPE"
echo ""
echo "安裝的文件:"
for folder in "${FOLDERS[@]}"; do
    if [ -d "$INSTALL_DIR/$folder" ]; then
        echo "✓ $INSTALL_DIR/$folder"
    else
        echo "✗ $INSTALL_DIR/$folder (安裝失敗)"
    fi
done

echo ""
echo "感謝使用 SunnyCore！"
