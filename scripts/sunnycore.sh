#!/usr/bin/env bash

# Sunnycore 安裝腳本
# - 允許選擇安裝版本
# - 目前僅支援安裝 warp-code（會將「warp code/」資料夾下所有內容拷貝到使用者指定路徑的 sunnycore/ 資料夾）
# - claude code 與 codex 版本暫不提供安裝

set -euo pipefail

SCRIPT_NAME="$(basename "$0")"
# 相容在非 bash 來源執行情境下的路徑偵測
if [[ -n "${BASH_SOURCE[0]:-}" ]]; then
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
else
  SCRIPT_DIR="$(pwd -P)"
fi
VERSION="0.2.0"

# 全域變數
DRY_RUN=0
AUTO_YES=0
INSTALL_BASE=""
SELECTED_VERSION=""
REPO_URL="https://github.com/Yamiyorunoshura/sunnycore.git"   # 預設為本倉庫 URL；可被 --repo 覆蓋或自動偵測
BRANCH=""     # 允許以 --branch 指定；未指定時自動偵測
REMOTE_NAME_INPUT=""   # 允許以 --remote-name 指定
TMP_CLONE_DIR=""

# 輔助函式：遠程檢測
detect_remote_name() {
  local repo_dir="$1"
  local repo_url="${2:-}"
  local preferred="${3:-}"
  
  log "偵測遠程名稱 - 倉庫目錄: $repo_dir, URL: ${repo_url:-未提供}, 偏好: ${preferred:-未提供}"

  # 優先使用指定的遠程名
  if [[ -n "$preferred" ]] && git -C "$repo_dir" remote get-url "$preferred" >/dev/null 2>&1; then
    log "使用偏好的遠程名: $preferred"
    echo "$preferred"
    return 0
  fi

  # 嘗試根據 URL 匹配遠程名
  if [[ -n "$repo_url" ]]; then
    log "嘗試根據 URL 匹配遠程名: $repo_url"
    local name
    name="$(git -C "$repo_dir" remote -v 2>/dev/null | awk -v url="$repo_url" '$2==url && $3=="(fetch)"{print $1; exit}')"
    if [[ -n "$name" ]]; then
      log "找到匹配的遠程名: $name"
      echo "$name"
      return 0
    fi
  fi

  # 使用第一個可用的遠程
  log "嘗試使用第一個可用的遠程"
  local remotes
  remotes="$(git -C "$repo_dir" remote 2>/dev/null || true)"
  if [[ -n "$remotes" ]]; then
    local first_remote
    first_remote="$(echo "$remotes" | head -n1)"
    log "使用第一個遠程: $first_remote"
    echo "$first_remote"
    return 0
  fi

  log "無法偵測到任何遠程"
  return 1
}

# 輔助函式：分支檢測
detect_default_branch() {
  local repo_dir="$1"
  local remote="${2:-}"
  
  log "偵測預設分支 - 倉庫目錄: $repo_dir, 遠程: ${remote:-未提供}"

  # 嘗試取得遠程 HEAD 分支
  if [[ -n "$remote" ]]; then
    log "嘗試從遠程 $remote 取得 HEAD 分支"
    local head
    head="$(git -C "$repo_dir" remote show "$remote" 2>/dev/null | awk '/HEAD branch/ {print $NF}' || true)"
    if [[ -n "$head" && "$head" != "(unknown)" ]]; then
      log "從遠程取得預設分支: $head"
      echo "$head"
      return 0
    fi
  fi

  # 嘗試常見的預設分支
  log "嘗試常見的預設分支名稱"
  for b in main master; do
    log "檢查分支: $b"
    if git -C "$repo_dir" rev-parse --verify "$b" >/dev/null 2>&1; then
      log "找到本地分支: $b"
      echo "$b"
      return 0
    fi
    if [[ -n "$remote" ]] && git -C "$repo_dir" ls-remote --exit-code --heads "$remote" "$b" >/dev/null 2>&1; then
      log "找到遠程分支: $remote/$b"
      echo "$b"
      return 0
    fi
  done

  # 使用任一本地分支
  log "嘗試使用任一本地分支"
  local any_local
  any_local="$(git -C "$repo_dir" for-each-ref --format='%(refname:short)' refs/heads 2>/dev/null | head -n1 || true)"
  if [[ -n "$any_local" ]]; then
    log "使用本地分支: $any_local"
    echo "$any_local"
    return 0
  fi

  # 使用任一遠程分支
  if [[ -n "$remote" ]]; then
    log "嘗試使用任一遠程分支"
    local any_remote
    any_remote="$(git -C "$repo_dir" ls-remote --heads "$remote" 2>/dev/null | awk '{print $2}' | sed 's@refs/heads/@@' | head -n1 || true)"
    if [[ -n "$any_remote" ]]; then
      log "使用遠程分支: $any_remote"
      echo "$any_remote"
      return 0
    fi
  fi

  log "無法偵測到任何分支"
  return 1
}

# 輔助函式：執行命令（支援 dry-run）
run_cmd() {
  log "執行命令: $*"
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: $*"
    return 0
  else
    log "開始執行: $*"
    local exit_code=0
    "$@" || exit_code=$?
    if [[ $exit_code -eq 0 ]]; then
      log "命令執行成功: $*"
    else
      error "命令執行失敗 (退出碼: $exit_code): $*"
      return $exit_code
    fi
  fi
}

cleanup() {
  # 清理暫存目錄（若有）
  if [[ -n "${TMP_CLONE_DIR:-}" && -d "$TMP_CLONE_DIR" ]]; then
    rm -rf "$TMP_CLONE_DIR" || true
  fi
}

trap cleanup EXIT

usage() {
  cat <<'EOF'
用法：
  bash sunnycore.sh [選項]

選項：
  -v, --version <名稱>   指定要安裝的版本（僅支援：warp-code）
  -p, --path <路徑>       指定安裝路徑（會在該路徑下建立/使用 sunnycore 資料夾）
      --repo <URL>        指定 Git 倉庫 URL（若本機無來源時可用來拉取）
      --branch <名稱>     指定 Git 分支（預設自動偵測遠程 HEAD）
      --remote-name <名稱> 指定 Git 遠程名（預設自動偵測）
      --dry-run           僅顯示將執行的動作，不實際變更
  -y, --yes               安裝時自動同意覆寫動作（若目標已存在）
  -h, --help              顯示此說明

說明：
  - 目前僅可安裝 warp-code；claude code 與 codex 暫不提供安裝。
  - 若未提供 --version 與 --path，腳本會以互動方式詢問。
  - 若專案本地來源資料夾不存在，可搭配 --repo 或自動偵測本機 git origin 進行拉取。
EOF
}

log() { printf '[%s] %s\n' "$(date '+%H:%M:%S')" "$*"; }
info() { printf 'INFO  %s\n' "$*"; }
warn() { printf '警告  %s\n' "$*"; }
error() { printf '錯誤  %s\n' "$*" 1>&2; }
ok() { printf '完成  %s\n' "$*"; }

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || { error "缺少必要指令：$1"; exit 1; }
}

run() {
  log "執行命令: $*"
  if [[ $DRY_RUN -eq 1 ]]; then
    printf '+ '
    printf '%q ' "$@"
    printf '\n'
  else
    log "開始執行: $*"
    local exit_code=0
    "$@" || exit_code=$?
    if [[ $exit_code -eq 0 ]]; then
      log "命令執行成功: $*"
    else
      error "命令執行失敗 (退出碼: $exit_code): $*"
      return $exit_code
    fi
  fi
}

normalize_version() {
  case "${1:-}" in
    warp|warp-code|warp_code)
      printf 'warp-code'
      ;;
    codex|claude|claude-code|claude_code)
      printf 'unsupported'
      ;;
    "")
      printf ''
      ;;
    *)
      printf 'invalid'
      ;;
  esac
}

# 輔助函式：展開家目錄符號「~」為實際路徑（僅支援當前使用者）
expand_path() {
  local input="${1:-}"
  if [[ -z "$input" ]]; then
    printf '%s' ""
    return 0
  fi
  if [[ "${input:0:1}" == "~" ]]; then
    if [[ "${#input}" -eq 1 ]]; then
      printf '%s' "${HOME:-$input}"
      return 0
    fi
    if [[ "${input:0:2}" == "~/" ]]; then
      printf '%s' "${HOME}/${input#~/}"
      return 0
    fi
  fi
  printf '%s' "$input"
}

parse_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      -v|--version)
        [[ $# -ge 2 ]] || { error "--version 需要參數"; exit 1; }
        SELECTED_VERSION="$2"
        shift 2
        ;;
      -p|--path)
        [[ $# -ge 2 ]] || { error "--path 需要參數"; exit 1; }
        INSTALL_BASE="$2"
        shift 2
        ;;
      --repo)
        [[ $# -ge 2 ]] || { error "--repo 需要參數 (Git URL)"; exit 1; }
        REPO_URL="$2"
        shift 2
        ;;
      --branch)
        [[ $# -ge 2 ]] || { error "--branch 需要參數 (分支名稱)"; exit 1; }
        BRANCH="$2"
        shift 2
        ;;
      --remote-name)
        [[ $# -ge 2 ]] || { error "--remote-name 需要參數 (遠程名稱)"; exit 1; }
        REMOTE_NAME_INPUT="$2"
        shift 2
        ;;
      --dry-run)
        DRY_RUN=1
        shift
        ;;
      -y|--yes)
        AUTO_YES=1
        shift
        ;;
      -h|--help)
        usage
        exit 0
        ;;
      *)
        error "未知參數：$1"
        usage
        exit 1
        ;;
    esac
  done

  # 將使用者提供的安裝路徑中的「~」展開為實際家目錄
  if [[ -n "${INSTALL_BASE:-}" ]]; then
    INSTALL_BASE="$(expand_path "$INSTALL_BASE")"
  fi

  local v
  v=$(normalize_version "${SELECTED_VERSION:-}")
  case "$v" in
    warp-code)
      SELECTED_VERSION="warp-code"
      ;;
    unsupported)
      error "目前僅支援安裝 warp-code；claude code 與 codex 暫不提供。"
      exit 1
      ;;
    invalid)
      error "不支援的版本名稱：${SELECTED_VERSION}"
      exit 1
      ;;
    *)
      SELECTED_VERSION=""
      ;;
  esac
}

prompt_select_version() {
  if [[ -n "${SELECTED_VERSION:-}" ]]; then
    return
  fi
  echo "請選擇要安裝的版本："
  echo "  1) warp-code（可安裝）"
  echo "  2) codex（尚未開放）"
  echo "  3) claude code（尚未開放）"
  read -r -p "輸入選項 [1-3]: " choice
  case "$choice" in
    1)
      SELECTED_VERSION="warp-code"
      ;;
    2|3)
      error "目前僅支援安裝 warp-code；所選版本尚未開放。"
      exit 1
      ;;
    *)
      error "無效的選項：$choice"
      exit 1
      ;;
  esac
}

prompt_install_path() {
  if [[ -n "${INSTALL_BASE:-}" ]]; then
    return
  fi
  local default_path
  # 在 set -u 環境下安全讀取 HOME，若不存在則退回當前工作目錄
  default_path="${HOME:-$(pwd -P)}"
  echo "將在安裝路徑下建立/使用 sunnycore 資料夾。"
  read -r -p "請輸入安裝路徑（預設：${default_path}）：" input_path
  if [[ -z "${input_path:-}" ]]; then
    INSTALL_BASE="$default_path"
  else
    INSTALL_BASE="$(expand_path "$input_path")"
  fi
}

confirm_overwrite_if_needed() {
  local target_dir="$1"
  log "檢查是否需要覆寫目標目錄: $target_dir"
  if [[ -d "$target_dir" ]]; then
    log "目標目錄已存在"
    if [[ $AUTO_YES -eq 1 ]]; then
      info "清空既有目錄：$target_dir"
      log "自動模式，直接清空目錄"
      run_cmd rm -rf "$target_dir"
      return
    fi
    log "詢問使用者是否覆寫"
    read -r -p "目標已存在：${target_dir}，是否清空後重新安裝？[y/N]: " yn
    log "使用者回應: $yn"
    case "$yn" in
      y|Y|yes|YES)
        info "清空既有目錄：$target_dir"
        log "使用者同意覆寫，清空目錄"
        run_cmd rm -rf "$target_dir"
        ;;
      *)
        log "使用者取消安裝"
        echo "已取消。"
        exit 1
        ;;
    esac
  else
    log "目標目錄不存在，無需覆寫"
  fi
}

install_warp_code() {
  local src dst use_local=0
  
  log "開始 warp-code 安裝程序"
  log "腳本目錄: $SCRIPT_DIR"
  
  # 優先嘗試從遠端倉庫拉取，除非明確指定使用本地版本或遠端不可用
  log "嘗試從遠端倉庫拉取來源..."
  # 先嘗試自動偵測當前倉庫的遠程 URL
  log "當前 REPO_URL: ${REPO_URL:-未設定}"
  if [[ -z "${REPO_URL:-}" ]]; then
    log "嘗試自動偵測 git 倉庫資訊..."
    if command -v git >/dev/null 2>&1; then
      log "git 命令可用"
      if git -C "$SCRIPT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        log "當前目錄位於 git 工作樹中"
        local detected_remote
        if detected_remote="$(detect_remote_name "$SCRIPT_DIR" "" "${REMOTE_NAME_INPUT:-}")" 2>/dev/null; then
          REPO_URL="$(git -C "$SCRIPT_DIR" remote get-url "$detected_remote" 2>/dev/null || true)"
          info "偵測到遠程倉庫：$REPO_URL (遠程：$detected_remote)"
        else
          warn "無法偵測到遠程倉庫"
        fi
      else
        warn "當前目錄不在 git 工作樹中"
      fi
    else
      warn "git 命令不可用"
    fi
  fi

  # 嘗試從遠端拉取
  if [[ -n "${REPO_URL:-}" ]] && command -v git >/dev/null 2>&1; then
    log "開始從遠端倉庫拉取..."

    require_cmd git
    TMP_CLONE_DIR="$(mktemp -d 2>/dev/null || mktemp -d -t sunnycore)"
    log "建立暫存目錄: $TMP_CLONE_DIR"
    info "以 git 拉取來源：$REPO_URL"
    
    # 決定要使用的分支
    local target_branch="${BRANCH:-}"
    log "指定分支: ${BRANCH:-未指定}"
    log "目標分支: ${target_branch:-將自動偵測}"
    
    # 確保 target_branch 不為空字符串但有值時正確設置
    if [[ -n "${BRANCH:-}" ]]; then
      target_branch="$BRANCH"
      log "使用指定分支: $target_branch"
    fi
    
    local clone_success=0
    if [[ $DRY_RUN -eq 1 ]]; then
      # dry-run 模式：僅模擬操作
      if [[ -z "$target_branch" ]]; then
        info "偵測遠程預設分支..."
        run_cmd git clone --depth=1 "$REPO_URL" "$TMP_CLONE_DIR"
        target_branch="master"  # dry-run 預設使用 master
        info "dry-run: 假設預設分支為 $target_branch"
      else
        run_cmd git clone --depth=1 --branch "$target_branch" --single-branch "$REPO_URL" "$TMP_CLONE_DIR"
        info "dry-run: 使用指定分支 $target_branch"
      fi
      clone_success=1
    else
      # 實際模式：執行真正的操作
      if [[ -z "$target_branch" ]]; then
        # 嘗試偵測預設分支（先做一個淺層克隆）
        info "偵測遠程預設分支..."
        log "執行: git clone --depth=1 $REPO_URL $TMP_CLONE_DIR"
        if git clone --depth=1 "$REPO_URL" "$TMP_CLONE_DIR"; then
          log "git clone 成功"
          if target_branch="$(detect_default_branch "$TMP_CLONE_DIR")"; then
          info "偵測到預設分支：$target_branch"
        else
          target_branch="master"  # fallback
          warn "無法偵測預設分支，使用 master"
        fi
        # 確保 target_branch 不為空
        if [[ -z "$target_branch" ]]; then
          target_branch="master"
          warn "target_branch 為空，強制設為 master"
        fi
          clone_success=1
        else
          warn "git clone 失敗，將嘗試使用本地來源"
          clone_success=0
        fi
      else
        info "使用指定分支：$target_branch"
        log "執行: git clone --depth=1 --branch $target_branch --single-branch $REPO_URL $TMP_CLONE_DIR"
        if git clone --depth=1 --branch "$target_branch" --single-branch "$REPO_URL" "$TMP_CLONE_DIR"; then
          log "git clone 成功"
          clone_success=1
        else
          warn "git clone 失敗（分支：$target_branch）"
          # 如果指定的分支不存在，嘗試使用最新的 warp-code 版本分支
          if [[ "$target_branch" == "warp-code" ]]; then
            log "嘗試使用最新的 warp-code 版本分支..."
            local latest_warp_branch="warp-code/v1.0.1"
            info "嘗試使用分支：$latest_warp_branch"
            log "執行: git clone --depth=1 --branch $latest_warp_branch --single-branch $REPO_URL $TMP_CLONE_DIR"
            if git clone --depth=1 --branch "$latest_warp_branch" --single-branch "$REPO_URL" "$TMP_CLONE_DIR"; then
              log "git clone 成功（使用 $latest_warp_branch）"
              clone_success=1
            else
              warn "git clone 失敗（分支：$latest_warp_branch），將嘗試使用本地來源"
              clone_success=0
            fi
          else
            warn "將嘗試使用本地來源"
            clone_success=0
          fi
        fi
      fi
    fi

    if [[ $clone_success -eq 1 ]]; then
      if [[ $DRY_RUN -eq 1 ]]; then
        src="$TMP_CLONE_DIR/warp code"
        info "dry-run: 假設來源目錄存在於 $src"
        # 在 dry-run 模式下，我們需要創建假的目錄結構以便後續檢查
        run_cmd mkdir -p "$src"
        run_cmd touch "$src/WARP.md"
      else
        log "檢查克隆目錄內容..."
        log "暫存目錄內容:"
        ls -la "$TMP_CLONE_DIR" || true
        if [[ -d "$TMP_CLONE_DIR/warp code" ]]; then
          src="$TMP_CLONE_DIR/warp code"
          log "找到 warp code 目錄: $src"
          info "成功從遠端倉庫獲取來源"
        else
          warn "遠端倉庫中找不到 'warp code' 來源資料夾，將嘗試使用本地來源"
          log "可用的目錄:"
          find "$TMP_CLONE_DIR" -type d -maxdepth 2 || true
          clone_success=0
        fi
      fi
    fi
  else
    log "無法從遠端拉取（REPO_URL 未設定或 git 不可用），將嘗試使用本地來源"
    clone_success=0
  fi
  
  # 如果遠端拉取失敗，回退到本地來源
  if [[ $clone_success -eq 0 ]]; then
    local local_src="${SCRIPT_DIR}/warp code"
    log "嘗試使用本地來源: $local_src"
    if [[ -d "$local_src" ]]; then
      src="$local_src"
      log "本地來源目錄存在: $src"
      info "使用本地來源進行安裝"
    else
      error "無法從遠端拉取，且本地來源不存在：$local_src"
      error "請確認網路連線或使用 --repo 參數指定正確的倉庫 URL"
      exit 1
    fi
  fi

  dst="${INSTALL_BASE%/}/sunnycore"
  log "設定目標目錄"
  log "安裝基礎路徑: $INSTALL_BASE"
  log "目標目錄: $dst"
  
  info "安裝版本：warp-code"
  info "來源：$src"
  info "目標：$dst"
  
  log "檢查來源目錄內容..."
  if [[ $DRY_RUN -eq 1 ]]; then
    log "dry-run: 跳過來源目錄實際檢查"
    info "dry-run: 假設來源目錄包含必要檔案"
  elif [[ -d "$src" ]]; then
    log "來源目錄存在，內容:"
    ls -la "$src" | head -10 || true
    log "來源目錄檔案數量: $(find "$src" -type f | wc -l)"
  else
    error "來源目錄不存在: $src"
    exit 1
  fi

  require_cmd mkdir
  require_cmd cp
  require_cmd rm
  require_cmd find

  log "檢查目標目錄狀態..."
  if [[ -d "$dst" ]]; then
    log "目標目錄已存在: $dst"
    log "目標目錄內容:"
    ls -la "$dst" | head -5 || true
  else
    log "目標目錄不存在，將建立: $dst"
  fi
  
  confirm_overwrite_if_needed "$dst"
  run_cmd mkdir -p "$dst"

  # 拷貝來源內容（包含隱藏檔）到目標資料夾
  info "開始拷貝檔案…"
  log "執行拷貝命令: cp -a $src/. $dst/"
  run_cmd cp -a "$src/." "$dst/"

  # 安裝後驗證：目標不應為空（仅在非 dry-run 模式下執行）
  log "開始安裝後驗證..."
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: 將於 $dst 執行安裝後檢查"
  else
    if [[ -d "$dst" ]]; then
      log "檢查目標目錄: $dst"
      local file_count
      file_count=$(find "$dst" -type f | wc -l)
      log "目標目錄檔案數量: $file_count"
      
      if [[ $file_count -eq 0 ]]; then
        error "拷貝後目標目錄為空：$dst"
        log "目標目錄內容:"
        ls -la "$dst" || true
        exit 1
      else
        log "驗證成功，目標目錄包含 $file_count 個檔案"
        log "目標目錄頂層內容:"
        ls -la "$dst" | head -10 || true
      fi
    else
      warn "安裝目錄不存在：$dst，略過檢查"
    fi
  fi

  ok "已完成拷貝到：$dst"
}

main() {
  log "=== Sunnycore 安裝腳本開始執行 ==="
  log "腳本版本: $VERSION"
  log "腳本路徑: $0"
  log "腳本目錄: $SCRIPT_DIR"
  log "傳入參數: $*"
  log "當前工作目錄: $(pwd)"
  log "當前使用者: $(whoami)"
  
  parse_args "$@"
  
  log "參數解析完成"
  log "DRY_RUN: $DRY_RUN"
  log "AUTO_YES: $AUTO_YES"
  log "INSTALL_BASE: ${INSTALL_BASE:-未設定}"
  log "SELECTED_VERSION: ${SELECTED_VERSION:-未設定}"
  log "REPO_URL: ${REPO_URL:-未設定}"
  log "BRANCH: ${BRANCH:-未設定}"
  
  prompt_select_version
  log "選擇的版本: $SELECTED_VERSION"
  
  prompt_install_path
  log "安裝路徑: $INSTALL_BASE"

  case "$SELECTED_VERSION" in
    warp-code)
      log "開始安裝 warp-code 版本"
      install_warp_code
      log "warp-code 安裝完成"
      ;;
    *)
      error "未知或未支援的版本：$SELECTED_VERSION"
      exit 1
      ;;
  esac
  
  log "=== Sunnycore 安裝腳本執行完成 ==="
}

main "$@"
