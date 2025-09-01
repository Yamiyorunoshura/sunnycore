#!/bin/bash

# 提示用戶輸入安裝路徑
read -p "請輸入要將 roo agent 安裝到的目標路徑: " TARGET_PATH

# 檢查用戶是否輸入了路徑
if [ -z "$TARGET_PATH" ]; then
    echo "錯誤：未輸入目標路徑。腳本將終止。"
    exit 1
fi

# 檢查用戶輸入的路徑是否存在且為一個目錄
if [ ! -d "$TARGET_PATH" ]; then
    echo "錯誤：指定的路徑 '$TARGET_PATH' 不存在或不是一個目錄。腳本將終止。"
    exit 1
fi

# 定義要複製的目錄
SOURCE_DIRS=("agents" "commands" "core")

echo "開始將 roo agent 複製到 '$TARGET_PATH'..."

# 遍歷並複製每個目錄
for dir in "${SOURCE_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "正在複製 '$dir' 目錄..."
        cp -r "$dir" "$TARGET_PATH"
    else
        echo "警告：源目錄 '$dir' 不存在，將跳過。"
    fi
done

echo "roo agent 已成功安裝到 '$TARGET_PATH'！"