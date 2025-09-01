#!/bin/bash

# 自動獲取最新的 roocode 版本分支
REPO_URL="https://github.com/Yamiyorunoshura/sunnycore.git"

echo "正在檢查可用的 roocode 分支版本..."

# 獲取所有 roocode 分支，按版本號排序
LATEST_BRANCH=$(git ls-remote --heads "$REPO_URL" | \
    grep "refs/heads/roocode/" | \
    sed 's/.*refs\/heads\/roocode\///' | \
    sort -V | \
    tail -1)

if [ -z "$LATEST_BRANCH" ]; then
    echo "錯誤：找不到任何 roocode 分支"
    exit 1
fi

echo "找到最新版本：roocode/$LATEST_BRANCH"

# 刪除舊的目錄（如果存在）
if [ -d "sunnycore" ]; then
    echo "刪除舊版本目錄..."
    rm -rf sunnycore
fi

# 克隆最新版本
echo "正在克隆最新版本..."
git clone -b "roocode/$LATEST_BRANCH" "$REPO_URL"

echo "完成！已成功克隆 roocode/$LATEST_BRANCH"