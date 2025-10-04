#!/usr/bin/env bash

# Sunnycore 安裝腳本
# - 允許選擇安裝版本
# - 支援安裝 warp-code、codex 與 claude code

set -euo pipefail

SCRIPT_NAME="$(basename "$0")"
# 相容在非 bash 來源執行情境下的路徑偵測
if [[ -n "${BASH_SOURCE[0]:-}" ]]; then
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
else
  SCRIPT_DIR="$(pwd -P)"
fi
VERSION="0.3.0"

# 全域變數
DRY_RUN=0
AUTO_YES=0
INSTALL_BASE=""
SELECTED_VERSION=""
REPO_URL="https://github.com/Yamiyorunoshura/sunnycore.git"   # 預設為本倉庫 URL；可被 --repo 覆蓋或自動偵測
BRANCH=""     # 允許以 --branch 指定；未指定時自動偵測
REMOTE_NAME_INPUT=""   # 允許以 --remote-name 指定
TMP_CLONE_DIR=""
INTERACTIVE_MODE=0  # 互動模式標誌

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
  curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/sunnycore.sh | bash -s -- [選項]

選項：
  -v, --version <名稱>   指定要安裝的版本（支援：warp-code, codex, claude-code）
  -p, --path <路徑>       指定安裝路徑（會在該路徑下建立/使用 sunnycore 資料夾）
      --repo <URL>        指定 Git 倉庫 URL（若本機無來源時可用來拉取）
      --branch <名稱>     指定 Git 分支（預設自動偵測遠程 HEAD）
      --remote-name <名稱> 指定 Git 遠程名（預設自動偵測）
      --dry-run           僅顯示將執行的動作，不實際變更
  -y, --yes               安裝時自動同意覆寫動作（若目標已存在）
  -i, --interactive       強制啟用互動模式（curl 使用時建議使用）
  -h, --help              顯示此說明

說明：
  - 可安裝 warp-code、codex 與 claude code。
  - 若未提供 --version 與 --path，腳本會以互動方式詢問。
  - 若專案本地來源資料夾不存在，可搭配 --repo 或自動偵測本機 git origin 進行拉取。
  - 使用 curl 時建議加上 -i 參數啟用互動模式，或直接使用互動式安裝：
    curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/sunnycore.sh | bash
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
    codex)
      printf 'codex'
      ;;
    claude|claude-code|claude_code)
      printf 'claude-code'
      ;;
    "")
      printf ''
      ;;
    *)
      printf 'invalid'
      ;;
  esac
}

# 輔助函式：展開家目錄符號「~」為實際路徑（支援開頭 "~"/"~/"，並移除中間的 "~" 片段）
expand_path() {
  local input="${1:-}"
  if [[ -z "$input" ]]; then
    printf '%s' ""
    return 0
  fi

  # 開頭為 ~ 或 ~/ 的常見情況
  if [[ "${input:0:1}" == "~" ]]; then
    if [[ "${#input}" -eq 1 ]]; then
      printf '%s' "${HOME:-$input}"
      return 0
    fi
    if [[ "${input:0:2}" == "~/" ]]; then
      input="${HOME}/${input#~/}"
    fi
  fi

  # 以分段法處理：移除任何等於 "~" 的路徑片段
  local is_abs=0
  [[ "$input" == /* ]] && is_abs=1
  local IFS='/'
  read -r -a __parts <<< "$input"
  local -a __out=()
  local __idx=0
  local __seg
  for __seg in "${__parts[@]}"; do
    if [[ $is_abs -eq 1 && $__idx -eq 0 && -z "$__seg" ]]; then
      __idx=$((__idx+1))
      continue
    fi
    if [[ "$__seg" == "~" || -z "$__seg" ]]; then
      __idx=$((__idx+1))
      continue
    fi
    __out+=("$__seg")
    __idx=$((__idx+1))
  done

  # 重組路徑
  local __result=""
  if [[ $is_abs -eq 1 ]]; then
    __result="/"
  fi
  local __i
  for __i in "${!__out[@]}"; do
    if [[ -n "$__result" && "${__result: -1}" != "/" ]]; then
      __result="${__result}/"
    fi
    __result="${__result}${__out[$__i]}"
  done
  printf '%s' "$__result"
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
      -i|--interactive)
        INTERACTIVE_MODE=1
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

  # 檢測是否為 curl 方式執行，如果沒有提供任何參數則自動啟用互動模式
  if [[ $INTERACTIVE_MODE -eq 0 && -z "${SELECTED_VERSION:-}" && -z "${INSTALL_BASE:-}" ]]; then
    # 檢查腳本是否從 stdin 讀取（curl 方式）
    if [[ ! -t 0 ]]; then
      info "檢測到從管道執行，自動啟用互動模式"
      INTERACTIVE_MODE=1
      warn "注意：在管道模式下互動可能受限。建議使用以下方式之一："
      warn "1. 下載腳本後執行：curl -fsSL URL -o install.sh && bash install.sh"
      warn "2. 使用參數指定選項：curl -fsSL URL | bash -s -- -v claude-code -p ~/install-path"
      warn "3. 使用強制互動模式：curl -fsSL URL | bash -s -- -i"

      # 嘗試重新定向到終端，如果失敗則使用預設值
      if [[ -t 1 ]] && [[ -c /dev/tty ]]; then
        exec < /dev/tty 2>/dev/null || {
          warn "無法重定向到終端，將使用預設設置"
          SELECTED_VERSION="claude-code"
          INSTALL_BASE="${HOME:-$(pwd -P)}"
        }
      fi
    fi
  fi

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
    codex)
      SELECTED_VERSION="codex"
      ;;
    claude-code)
      SELECTED_VERSION="claude-code"
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

  # 在互動模式下才詢問
  if [[ $INTERACTIVE_MODE -eq 1 ]]; then
    echo "請選擇要安裝的版本："
    echo "  1) warp-code"
    echo "  2) codex"
    echo "  3) claude code"

    # 確保可以從終端讀取輸入
    local input_choice=""
    local read_attempts=0
    local max_attempts=3

    while [[ -z "$input_choice" ]] && [[ $read_attempts -lt $max_attempts ]]; do
      read_attempts=$((read_attempts + 1))

      # 臨時禁用嚴格模式以防止 read 失敗導致腳本退出
      set +e
      if [[ -t 0 ]] && [[ -c /dev/tty ]]; then
        # 嘗試從終端讀取
        read -r -p "輸入選項 [1-3]: " input_choice < /dev/tty 2>/dev/null
        local read_result=$?
      else
        # 直接讀取
        read -r -p "輸入選項 [1-3]: " input_choice
        local read_result=$?
      fi
      set -e  # 重新啟用嚴格模式

      # 檢查 read 是否成功
      if [[ $read_result -ne 0 ]]; then
        # 讀取失敗，使用預設值
        warn "無法讀取用戶輸入，使用預設版本：claude-code"
        SELECTED_VERSION="claude-code"
        return
      fi

      case "$input_choice" in
        1)
          SELECTED_VERSION="warp-code"
          ;;
        2)
          SELECTED_VERSION="codex"
          ;;
        3)
          SELECTED_VERSION="claude-code"
          ;;
        *)
          if [[ $read_attempts -lt $max_attempts ]]; then
            if [[ -n "$input_choice" ]]; then
              echo "無效的選項：$input_choice，請輸入 1、2 或 3"
            else
              echo "無效的選項，請輸入 1、2 或 3"
            fi
            input_choice=""
          else
            warn "超過最大嘗試次數，使用預設版本：claude-code"
            SELECTED_VERSION="claude-code"
            return
          fi
          ;;
      esac
    done
  else
    # 非互動模式且未指定版本，使用預設值
    warn "未指定安裝版本，使用預設版本：claude-code"
    SELECTED_VERSION="claude-code"
  fi
}

prompt_install_path() {
  if [[ -n "${INSTALL_BASE:-}" ]]; then
    return
  fi

  # 在互動模式下才詢問
  if [[ $INTERACTIVE_MODE -eq 1 ]]; then
    local default_path
    # 在 set -u 環境下安全讀取 HOME，若不存在則退回當前工作目錄
    default_path="${HOME:-$(pwd -P)}"
    echo "將在安裝路徑下建立/使用 sunnycore 資料夾。"

    # 確保可以從終端讀取輸入
    local input_path=""

    # 臨時禁用嚴格模式以防止 read 失敗導致腳本退出
    set +e
    if [[ -t 0 ]] && [[ -c /dev/tty ]]; then
      # 嘗試從終端讀取
      read -r -p "請輸入安裝路徑（預設：${default_path}）：" input_path < /dev/tty 2>/dev/null
      local read_result=$?
    else
      # 直接讀取
      read -r -p "請輸入安裝路徑（預設：${default_path}）：" input_path
      local read_result=$?
    fi
    set -e  # 重新啟用嚴格模式

    # 檢查 read 是否成功
    if [[ $read_result -ne 0 ]]; then
      # 讀取失敗，使用預設值
      warn "無法讀取用戶輸入，使用預設路徑：${default_path}"
      INSTALL_BASE="$default_path"
      return
    fi

    if [[ -z "${input_path:-}" ]]; then
      INSTALL_BASE="$default_path"
    else
      INSTALL_BASE="$(expand_path "$input_path")"
    fi
  else
    # 非互動模式且未指定路徑，使用預設值
    local default_path
    default_path="${HOME:-$(pwd -P)}"
    warn "未指定安裝路徑，使用預設路徑：${default_path}"
    INSTALL_BASE="$default_path"
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
    # 在互動模式下才詢問
    if [[ $INTERACTIVE_MODE -eq 1 ]]; then
      log "詢問使用者是否覆寫"

      # 確保可以從終端讀取輸入
      local yn=""
      # 臨時禁用嚴格模式以防止 read 失敗導致腳本退出
      set +e
      if [[ -t 0 ]] && [[ -c /dev/tty ]]; then
        # 嘗試從終端讀取
        read -r -p "目標已存在：${target_dir}，是否清空後重新安裝？[y/N]: " yn < /dev/tty 2>/dev/null
        local read_result=$?
      else
        # 直接讀取
        read -r -p "目標已存在：${target_dir}，是否清空後重新安裝？[y/N]: " yn
        local read_result=$?
      fi
      set -e  # 重新啟用嚴格模式

      # 檢查 read 是否成功
      if [[ $read_result -ne 0 ]]; then
        # 讀取失敗，取消安裝
        warn "無法讀取用戶輸入，為安全起見取消安裝"
        warn "如需覆寫，請使用 -y 參數或手動刪除該目錄：$target_dir"
        exit 1
      fi

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
      # 非互動模式且目標目錄存在，給出警告但不清空
      warn "目標目錄已存在但非互動模式，將保留現有檔案：$target_dir"
      warn "如需覆寫，請使用 -y 參數或手動刪除該目錄"
    fi
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

install_codex() {
  local src dst use_local=0
  
  log "開始 codex 安裝程序"
  log "腳本目錄: $SCRIPT_DIR"
  
  # 優先嘗試從遠端倉庫拉取，除非明確指定使用本地版本或遠端不可用
  log "嘗試從遠端倉庫拉取來源..."
  # 先嘗試自動偵測當前倉庫的遠程 URL（若 REPO_URL 未設定）
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
  local clone_success=0
  if [[ -n "${REPO_URL:-}" ]] && command -v git >/dev/null 2>&1; then
    log "開始從遠端倉庫拉取..."
    
    require_cmd git
    TMP_CLONE_DIR="$(mktemp -d 2>/dev/null || mktemp -d -t sunnycore)"
    log "建立暫存目錄: $TMP_CLONE_DIR"
    info "以 git 拉取來源：$REPO_URL"
    
    local target_branch="${BRANCH:-}"
    log "指定分支: ${BRANCH:-未指定}"
    log "目標分支: ${target_branch:-將自動偵測}"
    
    if [[ -n "${BRANCH:-}" ]]; then
      target_branch="$BRANCH"
      log "使用指定分支: $target_branch"
    fi
    
    if [[ $DRY_RUN -eq 1 ]]; then
      if [[ -z "$target_branch" ]]; then
        info "偵測遠程預設分支..."
        run_cmd git clone --depth=1 "$REPO_URL" "$TMP_CLONE_DIR"
        target_branch="master"
        info "dry-run: 假設預設分支為 $target_branch"
      else
        run_cmd git clone --depth=1 --branch "$target_branch" --single-branch "$REPO_URL" "$TMP_CLONE_DIR"
        info "dry-run: 使用指定分支 $target_branch"
      fi
      clone_success=1
    else
      if [[ -z "$target_branch" ]]; then
        info "偵測遠程預設分支..."
        log "執行: git clone --depth=1 $REPO_URL $TMP_CLONE_DIR"
        if git clone --depth=1 "$REPO_URL" "$TMP_CLONE_DIR"; then
          log "git clone 成功"
          if target_branch="$(detect_default_branch "$TMP_CLONE_DIR")"; then
            info "偵測到預設分支：$target_branch"
          else
            target_branch="master"
            warn "無法偵測預設分支，使用 master"
          fi
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
          clone_success=0
        fi
      fi
    fi
    
    if [[ $clone_success -eq 1 ]]; then
      if [[ $DRY_RUN -eq 1 ]]; then
        src="$TMP_CLONE_DIR/codex"
        info "dry-run: 假設來源目錄存在於 $src"
        run_cmd mkdir -p "$src"
        run_cmd touch "$src/README.md"
      else
        log "檢查克隆目錄內容..."
        log "暫存目錄內容:"
        ls -la "$TMP_CLONE_DIR" || true
        if [[ -d "$TMP_CLONE_DIR/codex" ]]; then
          src="$TMP_CLONE_DIR/codex"
          log "找到 codex 目錄: $src"
          info "成功從遠端倉庫獲取來源"
        else
          warn "遠端倉庫中找不到 'codex' 來源資料夾，將嘗試使用本地來源"
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
    local local_src="${SCRIPT_DIR}/codex"
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
  
  info "安裝版本：codex"
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
  
  # 安裝後驗證：目標不應為空（於非 dry-run 模式）
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

install_claude_code() {
  local src dst_sunnycore dst_claude commands_dst settings_dst use_local=0

  log "開始 claude code 安裝程序"
  log "腳本目錄: $SCRIPT_DIR"

  log "嘗試從遠端倉庫拉取來源..."
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

  local clone_success=0
  if [[ -n "${REPO_URL:-}" ]] && command -v git >/dev/null 2>&1; then
    log "開始從遠端倉庫拉取..."

    require_cmd git
    TMP_CLONE_DIR="$(mktemp -d 2>/dev/null || mktemp -d -t sunnycore)"
    log "建立暫存目錄: $TMP_CLONE_DIR"
    info "以 git 拉取來源：$REPO_URL"

    local target_branch="${BRANCH:-}"
    log "指定分支: ${BRANCH:-未指定}"
    log "目標分支: ${target_branch:-將自動偵測}"

    if [[ -n "${BRANCH:-}" ]]; then
      target_branch="$BRANCH"
      log "使用指定分支: $target_branch"
    fi

    if [[ $DRY_RUN -eq 1 ]]; then
      if [[ -z "$target_branch" ]]; then
        info "偵測遠程預設分支..."
        run_cmd git clone --depth=1 "$REPO_URL" "$TMP_CLONE_DIR"
        target_branch="master"
        info "dry-run: 假設預設分支為 $target_branch"
      else
        run_cmd git clone --depth=1 --branch "$target_branch" --single-branch "$REPO_URL" "$TMP_CLONE_DIR"
        info "dry-run: 使用指定分支 $target_branch"
      fi
      clone_success=1
    else
      if [[ -z "$target_branch" ]]; then
        info "偵測遠程預設分支..."
        log "執行: git clone --depth=1 $REPO_URL $TMP_CLONE_DIR"
        if git clone --depth=1 "$REPO_URL" "$TMP_CLONE_DIR"; then
          log "git clone 成功"
          if target_branch="$(detect_default_branch "$TMP_CLONE_DIR")"; then
            info "偵測到預設分支：$target_branch"
          else
            target_branch="master"
            warn "無法偵測預設分支，使用 master"
          fi
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
          clone_success=0
        fi
      fi
    fi

    if [[ $clone_success -eq 1 ]]; then
      if [[ $DRY_RUN -eq 1 ]]; then
        src="$TMP_CLONE_DIR/claude code"
        info "dry-run: 假設來源目錄存在於 $src"
        run_cmd mkdir -p "$src"
        run_cmd mkdir -p "$src/commands"
        run_cmd touch "$src/README.md"
        run_cmd touch "$src/commands/example.json"
        run_cmd touch "$src/settings.local.json"
      else
        log "檢查克隆目錄內容..."
        log "暫存目錄內容:"
        ls -la "$TMP_CLONE_DIR" || true
        if [[ -d "$TMP_CLONE_DIR/claude code" ]]; then
          src="$TMP_CLONE_DIR/claude code"
          log "找到 claude code 目錄: $src"
          info "成功從遠端倉庫獲取來源"
        else
          warn "遠端倉庫中找不到 'claude code' 來源資料夾，將嘗試使用本地來源"
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

  if [[ $clone_success -eq 0 ]]; then
    local local_src="${SCRIPT_DIR}/claude code"
    log "嘗試使用本地來源: $local_src"
    if [[ -d "$local_src" ]]; then
      src="$local_src"
      log "本地來源目錄存在: $src"
      info "使用本地來源進行安裝"
      use_local=1
    else
      error "無法從遠端拉取，且本地來源不存在：$local_src"
      error "請確認網路連線或使用 --repo 參數指定正確的倉庫 URL"
      exit 1
    fi
  fi

  local commands_src="$src/commands"
  local settings_src="$src/settings.local.json"
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: 假設 commands 來源目錄存在於 $commands_src"
    info "dry-run: 假設 settings.local.json 檔案存在於 $settings_src"
  elif [[ ! -d "$commands_src" ]]; then
    error "來源目錄缺少 commands 子目錄：$commands_src"
    exit 1
  fi

  dst_sunnycore="${INSTALL_BASE%/}/sunnycore"
  dst_claude="${INSTALL_BASE%/}/.claude"
  commands_dst="${dst_claude%/}/commands"
  settings_dst="${dst_claude%/}/settings.local.json"

  log "設定目標目錄"
  log "安裝基礎路徑: $INSTALL_BASE"
  log "Sunnycore 目標目錄: $dst_sunnycore"
  log "Claude commands 目標目錄: $commands_dst"
  log "Claude settings.local.json 目標：$settings_dst"

  info "安裝版本：claude code"
  info "來源：$src"
  info "Sunnycore 目標：$dst_sunnycore"
  info "Claude commands 目標：$commands_dst"
  info "Claude settings.local.json 目標：$settings_dst"

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

  confirm_overwrite_if_needed "$dst_sunnycore"
  confirm_overwrite_if_needed "$commands_dst"
  run_cmd mkdir -p "$dst_sunnycore"
  run_cmd mkdir -p "$dst_claude"

  info "開始拷貝 Sunnycore 檔案…"
  log "執行拷貝命令: cp -a $src/. $dst_sunnycore/"
  run_cmd cp -a "$src/." "$dst_sunnycore/"

  info "開始拷貝 commands 檔案至 .claude…"
  log "執行拷貝命令: cp -a $commands_src $dst_claude/"
  run_cmd cp -a "$commands_src" "$dst_claude/"

  # 拷貝 settings.local.json 檔案（如果存在）
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: 拷貝 settings.local.json 至 .claude…"
    log "dry-run: cp $settings_src $settings_dst"
  elif [[ -f "$settings_src" ]]; then
    info "開始拷貝 settings.local.json 檔案至 .claude…"
    log "執行拷貝命令: cp $settings_src $settings_dst"
    run_cmd cp "$settings_src" "$settings_dst"
  else
    log "settings.local.json 檔案不存在於來源目錄，跳過拷貝"
  fi

  info "移除 Sunnycore 目錄中的 commands 目錄"
  log "執行移除命令: rm -rf $dst_sunnycore/commands"
  run_cmd rm -rf "$dst_sunnycore/commands"

  # 移除 Sunnycore 目錄中的 settings.local.json（如果存在）
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: 移除 Sunnycore 目錄中的 settings.local.json"
    log "dry-run: rm -f $dst_sunnycore/settings.local.json"
  elif [[ -f "$dst_sunnycore/settings.local.json" ]]; then
    info "移除 Sunnycore 目錄中的 settings.local.json"
    log "執行移除命令: rm -f $dst_sunnycore/settings.local.json"
    run_cmd rm -f "$dst_sunnycore/settings.local.json"
  fi

  log "開始安裝後驗證 (sunnycore)…"
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: 將於 $dst_sunnycore 執行安裝後檢查"
  else
    if [[ -d "$dst_sunnycore" ]]; then
      log "檢查 Sunnycore 目錄: $dst_sunnycore"
      local sunnycore_file_count
      sunnycore_file_count=$(find "$dst_sunnycore" -type f | wc -l)
      log "Sunnycore 目標目錄檔案數量: $sunnycore_file_count"

      if [[ -d "$dst_sunnycore/commands" ]]; then
        warn "Sunnycore 目錄中仍存在 commands 目錄，將移除"
        run_cmd rm -rf "$dst_sunnycore/commands"
      fi

      if [[ -f "$dst_sunnycore/settings.local.json" ]]; then
        warn "Sunnycore 目錄中仍存在 settings.local.json 檔案，將移除"
        run_cmd rm -f "$dst_sunnycore/settings.local.json"
      fi

      if [[ $sunnycore_file_count -eq 0 ]]; then
        error "拷貝後 Sunnycore 目標目錄為空：$dst_sunnycore"
        log "Sunnycore 目標目錄內容:"
        ls -la "$dst_sunnycore" || true
        exit 1
      else
        log "Sunnycore 驗證成功，目標目錄包含 $sunnycore_file_count 個檔案"
        log "Sunnycore 目標目錄頂層內容:"
        ls -la "$dst_sunnycore" | head -10 || true
      fi
    else
      warn "Sunnycore 安裝目錄不存在：$dst_sunnycore，略過檢查"
    fi
  fi

  log "開始安裝後驗證 (.claude/commands)…"
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: 將於 $commands_dst 執行安裝後檢查"
  else
    if [[ -d "$commands_dst" ]]; then
      log "檢查 commands 目錄: $commands_dst"
      local commands_file_count
      commands_file_count=$(find "$commands_dst" -type f | wc -l)
      log "commands 目錄檔案數量: $commands_file_count"

      if [[ $commands_file_count -eq 0 ]]; then
        error ".claude/commands 目錄為空：$commands_dst"
        log "commands 目錄內容:"
        ls -la "$commands_dst" || true
        exit 1
      else
        log "commands 驗證成功，目錄包含 $commands_file_count 個檔案"
        log "commands 目錄頂層內容:"
        ls -la "$commands_dst" | head -10 || true
      fi
    else
      error ".claude/commands 目錄不存在：$commands_dst"
      exit 1
    fi
  fi

  ok "Claude code installation completed: $dst_sunnycore, $commands_dst and $settings_dst"
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
    codex)
      log "開始安裝 codex 版本"
      install_codex
      log "codex 安裝完成"
      ;;
    claude-code)
      log "開始安裝 claude code 版本"
      install_claude_code
      log "claude code 安裝完成"
      ;;
    *)
      error "未知或未支援的版本：$SELECTED_VERSION"
      exit 1
      ;;
  esac
  
  log "=== Sunnycore 安裝腳本執行完成 ==="
}

main "$@"
