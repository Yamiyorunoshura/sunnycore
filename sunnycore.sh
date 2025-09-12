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

  # 優先使用指定的遠程名
  if [[ -n "$preferred" ]] && git -C "$repo_dir" remote get-url "$preferred" >/dev/null 2>&1; then
    echo "$preferred"
    return 0
  fi

  # 嘗試根據 URL 匹配遠程名
  if [[ -n "$repo_url" ]]; then
    local name
    name="$(git -C "$repo_dir" remote -v 2>/dev/null | awk -v url="$repo_url" '$2==url && $3=="(fetch)"{print $1; exit}')"
    if [[ -n "$name" ]]; then
      echo "$name"
      return 0
    fi
  fi

  # 使用第一個可用的遠程
  local remotes
  remotes="$(git -C "$repo_dir" remote 2>/dev/null || true)"
  if [[ -n "$remotes" ]]; then
    echo "$remotes" | head -n1
    return 0
  fi

  return 1
}

# 輔助函式：分支檢測
detect_default_branch() {
  local repo_dir="$1"
  local remote="${2:-}"

  # 嘗試取得遠程 HEAD 分支
  if [[ -n "$remote" ]]; then
    local head
    head="$(git -C "$repo_dir" remote show "$remote" 2>/dev/null | awk '/HEAD branch/ {print $NF}' || true)"
    if [[ -n "$head" && "$head" != "(unknown)" ]]; then
      echo "$head"
      return 0
    fi
  fi

  # 嘗試常見的預設分支
  for b in main master; do
    if git -C "$repo_dir" rev-parse --verify "$b" >/dev/null 2>&1; then
      echo "$b"
      return 0
    fi
    if [[ -n "$remote" ]] && git -C "$repo_dir" ls-remote --exit-code --heads "$remote" "$b" >/dev/null 2>&1; then
      echo "$b"
      return 0
    fi
  done

  # 使用任一本地分支
  local any_local
  any_local="$(git -C "$repo_dir" for-each-ref --format='%(refname:short)' refs/heads 2>/dev/null | head -n1 || true)"
  if [[ -n "$any_local" ]]; then
    echo "$any_local"
    return 0
  fi

  # 使用任一遠程分支
  if [[ -n "$remote" ]]; then
    local any_remote
    any_remote="$(git -C "$repo_dir" ls-remote --heads "$remote" 2>/dev/null | awk '{print $2}' | sed 's@refs/heads/@@' | head -n1 || true)"
    if [[ -n "$any_remote" ]]; then
      echo "$any_remote"
      return 0
    fi
  fi

  return 1
}

# 輔助函式：執行命令（支援 dry-run）
run_cmd() {
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: $*"
    return 0
  else
    "$@"
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
  if [[ $DRY_RUN -eq 1 ]]; then
    printf '+ '
    printf '%q ' "$@"
    printf '\n'
  else
    "$@"
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
    INSTALL_BASE="$input_path"
  fi
}

confirm_overwrite_if_needed() {
  local target_dir="$1"
  if [[ -d "$target_dir" ]]; then
    if [[ $AUTO_YES -eq 1 ]]; then
      info "清空既有目錄：$target_dir"
      run_cmd rm -rf "$target_dir"
      return
    fi
    read -r -p "目標已存在：${target_dir}，是否清空後重新安裝？[y/N]: " yn
    case "$yn" in
      y|Y|yes|YES)
        info "清空既有目錄：$target_dir"
        run_cmd rm -rf "$target_dir"
        ;;
      *)
        echo "已取消。"
        exit 1
        ;;
    esac
  fi
}

install_warp_code() {
  local src dst
  src="${SCRIPT_DIR}/warp code"

  # 若本地來源不存在，嘗試透過 git 拉取
  if [[ ! -d "$src" ]]; then
    info "本地來源不存在：$src"
    # 先嘗試自動偵測當前倉庫的遠程 URL
    if [[ -z "${REPO_URL:-}" ]]; then
      if command -v git >/dev/null 2>&1 && git -C "$SCRIPT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        local detected_remote
        if detected_remote="$(detect_remote_name "$SCRIPT_DIR" "" "${REMOTE_NAME_INPUT:-}")" 2>/dev/null; then
          REPO_URL="$(git -C "$SCRIPT_DIR" remote get-url "$detected_remote" 2>/dev/null || true)"
          info "偵測到遠稍倉庫：$REPO_URL (遠程：$detected_remote)"
        fi
      fi
    fi

    if [[ -z "${REPO_URL:-}" ]]; then
      error "找不到本地來源，且未提供 --repo；請以 --repo <URL> 提供本倉庫的 master/main 分支 URL。"
      exit 1
    fi

    require_cmd git
    TMP_CLONE_DIR="$(mktemp -d 2>/dev/null || mktemp -d -t sunnycore)"
    info "以 git 拉取來源：$REPO_URL"
    
    # 決定要使用的分支
    local target_branch="${BRANCH:-}"
    
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
    else
      # 實際模式：執行真正的操作
      if [[ -z "$target_branch" ]]; then
        # 嘗試偵測預設分支（先做一個淺層克隆）
        info "偵測遠程預設分支..."
        if git clone --depth=1 "$REPO_URL" "$TMP_CLONE_DIR"; then
          if target_branch="$(detect_default_branch "$TMP_CLONE_DIR")"; then
            info "偵測到預設分支：$target_branch"
          else
            target_branch="master"  # fallback
            warn "無法偵測預設分支，使用 master"
          fi
        else
          error "git clone 失敗，請確認網路與倉庫 URL。"
          exit 1
        fi
      else
        info "使用指定分支：$target_branch"
        if ! git clone --depth=1 --branch "$target_branch" --single-branch "$REPO_URL" "$TMP_CLONE_DIR"; then
          error "git clone 失敗（分支：$target_branch）。"
          exit 1
        fi
      fi
    fi

    if [[ $DRY_RUN -eq 1 ]]; then
      src="$TMP_CLONE_DIR/warp code"
      info "dry-run: 假設來源目錄存在於 $src"
    else
      if [[ -d "$TMP_CLONE_DIR/warp code" ]]; then
        src="$TMP_CLONE_DIR/warp code"
      else
        error "遠端倉庫中找不到 'warp code' 來源資料夾。"
        exit 1
      fi
    fi
  fi

  dst="${INSTALL_BASE%/}/sunnycore"
  info "安裝版本：warp-code"
  info "來源：$src"
  info "目標：$dst"

  require_cmd mkdir
  require_cmd cp
  require_cmd rm
  require_cmd find

  confirm_overwrite_if_needed "$dst"
  run_cmd mkdir -p "$dst"

  # 拷貝來源內容（包含隱藏檔）到目標資料夾
  info "開始拷貝檔案…"
  run_cmd cp -a "$src/." "$dst/"

  # 安裝後驗證：目標不應為空（仅在非 dry-run 模式下執行）
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: 將於 $dst 執行安裝後檢查"
  else
    if [[ -d "$dst" ]]; then
      if ! find "$dst" -mindepth 1 -print -quit | grep -q . 2>/dev/null; then
        error "拷貝後目標目錄為空：$dst"
        exit 1
      fi
    else
      warn "安裝目錄不存在：$dst，略過檢查"
    fi
  fi

  ok "已完成拷貝到：$dst"
}

main() {
  parse_args "$@"
  prompt_select_version
  prompt_install_path

  case "$SELECTED_VERSION" in
    warp-code)
      install_warp_code
      ;;
    *)
      error "未知或未支援的版本：$SELECTED_VERSION"
      exit 1
      ;;
  esac
}

main "$@"
