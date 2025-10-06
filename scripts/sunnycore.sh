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
INSTALL_TYPE=""  # 安裝類型：project（專案安裝）或 custom（指定路徑安裝）
SELECTED_VERSION=""
REPO_URL="https://github.com/Yamiyorunoshura/sunnycore.git"   # 預設為本倉庫 URL；可被 --repo 覆蓋或自動偵測
BRANCH=""     # 允許以 --branch 指定；未指定時自動偵測
REMOTE_NAME_INPUT=""   # 允許以 --remote-name 指定
TMP_CLONE_DIR=""
INTERACTIVE_MODE=0  # 互動模式標誌
QUIET_MODE=0  # 靜默模式：減少詳細日誌輸出

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
      handle_command_error "$exit_code" "$@"
      return $exit_code
    fi
  fi
}

# 輔助函式：處理命令執行錯誤
handle_command_error() {
  local exit_code="$1"
  shift
  local failed_cmd="$*"

  error "❌ 命令執行失敗：$failed_cmd"
  error "   退出碼：$exit_code"

  case "$exit_code" in
    1)
      error "   一般錯誤：命令執行失敗"
      ;;
    2)
      error "   誤用錯誤：命令參數或語法錯誤"
      ;;
    126)
      error "   權限錯誤：命令不可執行"
      ;;
    127)
      error "   命令不存在：$failed_cmd"
      ;;
    128)
      error "   無效參數傳遞"
      ;;
    130)
      error "   被終端中斷 (Ctrl+C)"
      ;;
    137)
      error "   被終止信號 (SIGKILL)"
      ;;
    *)
      error "   未知錯誤"
      ;;
  esac

  # 根據失敗的命令提供具體建議
  case "${failed_cmd%% *}" in
    "git")
      error "   Git 相關建議："
      error "     • 檢查網路連線"
      error "     • 確認 Git 倉庫 URL 正確"
      error "     • 檢查 Git 權限設置"
      ;;
    "mkdir"|"cp"|"rm")
      error "   檔案系統相關建議："
      error "     • 檢查目錄權限"
      error "     • 確認磁碟空間充足"
      error "     • 檢查路徑是否正確"
      ;;
    "curl"|"wget")
      error "   網路相關建議："
      error "     • 檢查網路連線"
      error "     • 確認 URL 可訪問"
      error "     • 檢查防火牆設置"
      ;;
  esac

  if [[ $INTERACTIVE_MODE -eq 1 ]]; then
    echo ""
    local retry_choice
    retry_choice=$(safe_read_with_timeout "是否重試此命令？[y/N]: " 15 "n")
    case "$retry_choice" in
      y|Y|yes|YES)
        info "🔄 重試命令：$failed_cmd"
        if "$@"; then
          ok "✓ 重試成功"
          return 0
        else
          error "❌ 重試仍然失敗"
        fi
        ;;
      *)
        warn "⚠️  跳過失敗的命令"
        ;;
    esac
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
  -p, --path <路徑>       指定安裝路徑（自訂安裝位置）
      --repo <URL>        指定 Git 倉庫 URL（若本機無來源時可用來拉取）
      --branch <名稱>     指定 Git 分支（預設自動偵測遠程 HEAD）
      --remote-name <名稱> 指定 Git 遠程名（預設自動偵測）
      --dry-run           僅顯示將執行的動作，不實際變更
  -y, --yes               安裝時自動同意覆寫動作（若目標已存在）
  -i, --interactive       強制啟用互動模式（curl 使用時建議使用）
  -h, --help              顯示此說明

安裝方式：
  1. 專案安裝（預設）：
     - 安裝到當前專案目錄的 .claude/ 資料夾
     - 適合將 Sunnycore 整合到現有專案中
     - 只安裝 commands/ 和 agents/ 到 .claude/

  2. 指定路徑安裝：
     - 使用 -p 參數指定自訂安裝位置
     - 會在指定路徑下建立 sunnycore/ 和 .claude/ 資料夾
     - 適合獨立安裝或多專案共用

說明：
  - 此腳本會安裝 Claude Code 版本的 Sunnycore。
  - 互動模式下會詢問安裝方式（專案安裝或指定路徑安裝）。
  - 若專案本地來源資料夾不存在，可搭配 --repo 或自動偵測本機 git origin 進行拉取。
  - 使用 curl 快速安裝到當前專案：
    curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/sunnycore.sh | bash
  - 使用 curl 安裝到指定路徑：
    curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/sunnycore.sh | bash -s -- -p ~/my-path
EOF
}

log() { 
  # 在靜默模式下不輸出詳細日誌
  [[ $QUIET_MODE -eq 1 ]] && return 0
  printf '[%s] %s\n' "$(date '+%H:%M:%S')" "$*"
}
info() { printf 'INFO  %s\n' "$*"; }
warn() { printf '警告  %s\n' "$*"; }
error() { printf '錯誤  %s\n' "$*" 1>&2; }
ok() { printf '完成  %s\n' "$*"; }

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    error "❌ 缺少必要指令：$1"

    case "$1" in
      "git")
        error "   安裝 Git："
        error "   • macOS: xcode-select --install 或 brew install git"
        error "   • Ubuntu/Debian: sudo apt-get install git"
        error "   • CentOS/RHEL: sudo yum install git"
        error "   • Windows: 從 https://git-scm.com/ 下載"
        ;;
      "curl")
        error "   安裝 curl："
        error "   • macOS: brew install curl"
        error "   • Ubuntu/Debian: sudo apt-get install curl"
        error "   • CentOS/RHEL: sudo yum install curl"
        error "   • Windows: 從 https://curl.se/ 下載"
        ;;
      "bash")
        error "   安裝 bash："
        error "   • macOS: 預設安裝"
        error "   • Linux: 預設安裝"
        error "   • Windows: 使用 WSL 或 Git Bash"
        ;;
    esac

    if [[ $INTERACTIVE_MODE -eq 1 ]]; then
      echo ""
      local continue_choice
      continue_choice=$(safe_read_with_timeout "是否繼續安裝（可能會失敗）？[y/N]: " 15 "n")
      case "$continue_choice" in
        y|Y|yes|YES)
          warn "⚠️  繼續安裝但可能失敗"
          return
          ;;
        *)
          error "❌ 安裝已取消"
          exit 1
          ;;
      esac
    else
      error "❌ 請安裝 $1 後重新執行"
      exit 1
    fi
  fi
}

# 輔助函式：系統環境檢測
check_system_environment() {
  log "開始系統環境檢測"

  # 檢測作業系統
  local os_name="unknown"
  local os_version="unknown"

  if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    os_name="Linux"
    if [[ -f /etc/os-release ]]; then
      os_version="$(grep PRETTY_NAME /etc/os-release | cut -d '"' -f 2)"
    fi
  elif [[ "$OSTYPE" == "darwin"* ]]; then
    os_name="macOS"
    os_version="$(sw_vers -productVersion 2>/dev/null || echo "未知版本")"
  elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    os_name="Windows"
    os_version="Windows (Unix-like environment)"
  fi

  log "作業系統: $os_name $os_version"

  # 檢測 Shell 環境
  local shell_name="$SHELL"
  local shell_version="$BASH_VERSION"
  log "Shell: $shell_name"
  [[ -n "$shell_version" ]] && log "Bash 版本: $shell_version"

  # 檢測權限
  local current_dir="$(pwd)"
  local can_write=0
  if [[ -w "$current_dir" ]]; then
    can_write=1
    log "當前目錄可寫: 是"
  else
    log "當前目錄可寫: 否"
  fi

  # 檢測網路連線（可選）
  if command -v ping >/dev/null 2>&1; then
    if ping -c 1 github.com >/dev/null 2>&1; then
      log "網路連線: 正常"
    else
      warn "網路連線: 可能異常（無法連線到 github.com）"
    fi
  fi

  # 檢測磁碟空間
  if command -v df >/dev/null 2>&1; then
    local available_space
    available_space="$(df -h . | awk 'NR==2 {print $4}' 2>/dev/null || echo "未知")"
    log "可用磁碟空間: $available_space"
  fi

  # 在互動模式下顯示摘要
  if [[ $INTERACTIVE_MODE -eq 1 && $QUIET_MODE -eq 0 ]]; then
    echo ""
    info "🖥️  系統環境："
    echo "   作業系統: $os_name $os_version"
    echo "   Shell: $shell_name"
    echo "   當前目錄: $current_dir"
    echo "   目錄權限: $([[ $can_write -eq 1 ]] && echo "可寫" || echo "只讀")"
    echo ""
  fi

  # 檢查關鍵要求
  local issues=0

  if [[ $can_write -eq 0 ]]; then
    warn "⚠️  當前目錄不可寫，安裝可能失敗"
    issues=$((issues + 1))
  fi

  if ! command -v git >/dev/null 2>&1; then
    warn "⚠️  Git 未安裝，無法從遠端倉庫拉取"
    issues=$((issues + 1))
  fi

  if [[ $issues -gt 0 && $INTERACTIVE_MODE -eq 1 ]]; then
    local continue_install
    continue_install=$(safe_read_with_timeout "檢測到 $issues 個問題，是否繼續安裝？[y/N]: " 15 "n")
    case "$continue_install" in
      y|Y|yes|YES)
        info "🔧 將繼續安裝（可能遇到問題）"
        ;;
      *)
        error "❌ 安裝已取消"
        exit 1
        ;;
    esac
  fi

  log "系統環境檢測完成"
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

  # 改進的執行方式檢測和兼容性處理
  detect_execution_method() {
    local execution_method="unknown"
    local is_from_stdin=0
    local is_from_file=0

    # 檢測是否從 stdin 讀取（curl 方式）
    if [[ ! -t 0 ]]; then
      is_from_stdin=1
      execution_method="curl"
      log "檢測到從管道執行 (curl 方式)"
    elif [[ -n "${BASH_SOURCE[0]:-}" ]] && [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
      # 腳本被 source 執行
      execution_method="source"
      log "檢測到 source 執行方式"
    elif [[ -f "$0" ]] && [[ "$(basename "$0")" == "${SCRIPT_NAME}" ]]; then
      # 直接執行腳本檔案
      is_from_file=1
      execution_method="direct"
      log "檢測到直接執行腳本檔案"
    fi

    # 根據執行方式調整設置
    case "$execution_method" in
      "curl")
        # curl 執行方式：自動啟用互動模式
        if [[ $INTERACTIVE_MODE -eq 0 && -z "${INSTALL_BASE:-}" ]]; then
          info "📥 檢測到 curl 執行方式，自動啟用互動模式"
          INTERACTIVE_MODE=1
          QUIET_MODE=1  # 自動啟用靜默模式以減少冗長輸出

          # 嘗試重新定向到終端
          if [[ -t 1 ]] && [[ -c /dev/tty ]]; then
            if exec < /dev/tty 2>/dev/null; then
              log "成功重定向到終端"
            else
              warn "⚠️  無法重定向到終端，將使用預設設置"
              INSTALL_BASE="${HOME:-$(pwd -P)}"
              info "將安裝到預設路徑：$INSTALL_BASE"
            fi
          else
            warn "⚠️  終端不可用，將使用預設設置"
            INSTALL_BASE="${HOME:-$(pwd -P)}"
            info "將安裝到預設路徑：$INSTALL_BASE"
          fi
        fi
        ;;
      "direct")
        # 直接執行：保持現有邏輯
        log "直接執行腳本，保持現有設置"
        ;;
      "source")
        # source 執行：給出警告
        warn "⚠️  檢測到 source 執行方式，建議直接執行腳本"
        ;;
      *)
        # 未知執行方式：保守處理
        log "未知執行方式，使用保守設置"
        if [[ -z "${INSTALL_BASE:-}" ]]; then
          INSTALL_BASE="${HOME:-$(pwd -P)}"
          info "將安裝到預設路徑：$INSTALL_BASE"
        fi
        ;;
    esac

    # 記錄執行環境信息
    log "執行方式: $execution_method"
    log "互動模式: $INTERACTIVE_MODE"
    log "靜默模式: $QUIET_MODE"
    log "stdin 是否為終端: $([[ -t 0 ]] && echo "是" || echo "否")"
    log "stdout 是否為終端: $([[ -t 1 ]] && echo "是" || echo "否")"
    log "/dev/tty 是否可用: $([[ -c /dev/tty ]] && echo "是" || echo "否")"
  }

  # 執行檢測
  detect_execution_method

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

  # 由於只支援 claude-code，直接設定為預設值
  SELECTED_VERSION="claude-code"
  
  # 在互動模式下顯示將要安裝的版本
  if [[ $INTERACTIVE_MODE -eq 1 ]]; then
    info "將安裝 Claude Code 版本"
  fi
}

prompt_install_type() {
  if [[ -n "${INSTALL_TYPE:-}" ]]; then
    return
  fi

  # 在互動模式下才詢問
  if [[ $INTERACTIVE_MODE -eq 1 ]]; then
    echo ""
    echo "🔧 請選擇安裝方式："
    echo ""
    echo "  1️⃣  專案安裝（安裝到當前專案目錄）"
    echo "     • 適合將 Sunnycore 整合到現有專案中"
    echo "     • 只安裝 commands/ 和 agents/ 到 .claude/"
    echo ""
    echo "  2️⃣  指定路徑安裝（自訂安裝位置）"
    echo "     • 適合獨立安裝或多專案共用"
    echo "     • 會在指定路徑下建立 sunnycore/ 和 .claude/ 資料夾"
    echo ""

    local input_choice=""
    local max_attempts=3
    local attempt=0

    while [[ $attempt -lt $max_attempts ]]; do
      attempt=$((attempt + 1))

      local prompt_text="請輸入選項 [1-2]（預設：1）: "
      if [[ $attempt -gt 1 ]]; then
        prompt_text="請輸入有效選項 [1-2]（預設：1，剩餘嘗試：$((max_attempts - attempt + 1))）: "
      fi

      # 使用改進的讀取函式
      input_choice=$(safe_read_with_timeout "$prompt_text" 30 "1")
      local read_result=$?

      if [[ $read_result -ne 0 ]]; then
        warn "⚠️  無法讀取用戶輸入，使用預設選項：專案安裝"
        INSTALL_TYPE="project"
        return
      fi

      # 如果用戶直接按 Enter 或預設值，使用預設值
      if [[ -z "$input_choice" || "$input_choice" == "1" ]]; then
        echo ""
        info "✓ 選擇：專案安裝"
        echo "   將安裝到當前專案目錄的 .claude/ 資料夾"
        echo ""
        INSTALL_TYPE="project"
        return
      fi

      case "$input_choice" in
        2)
          echo ""
          info "✓ 選擇：指定路徑安裝"
          echo "   將詢問自訂安裝位置"
          echo ""
          INSTALL_TYPE="custom"
          return
          ;;
        *)
          if [[ $attempt -lt $max_attempts ]]; then
            warn "❌ 無效的選項：$input_choice，請輸入 1 或 2"
          else
            warn "⚠️  超過最大嘗試次數，使用預設選項：專案安裝"
            echo ""
            INSTALL_TYPE="project"
            return
          fi
          ;;
      esac
    done
  else
    # 非互動模式，檢查是否有指定路徑
    if [[ -n "${INSTALL_BASE:-}" ]]; then
      INSTALL_TYPE="custom"
      log "非互動模式：檢測到指定路徑，設定為指定路徑安裝"
    else
      INSTALL_TYPE="project"
      log "非互動模式：未指定路徑，設定為專案安裝"
    fi
  fi
}

prompt_install_path() {
  if [[ -n "${INSTALL_BASE:-}" ]]; then
    return
  fi

  # 根據安裝類型決定安裝路徑
  if [[ "${INSTALL_TYPE:-}" == "project" ]]; then
    # 專案安裝：使用當前工作目錄
    INSTALL_BASE="$(pwd -P)"
    if [[ $INTERACTIVE_MODE -eq 1 ]]; then
      echo ""
      info "📁 專案安裝模式："
      echo "   安裝路徑：${INSTALL_BASE}/.claude"
      echo ""
    else
      log "專案安裝模式：將安裝到 ${INSTALL_BASE}/.claude"
    fi
    return
  fi

  # 指定路徑安裝：詢問用戶路徑
  if [[ $INTERACTIVE_MODE -eq 1 ]]; then
    local default_path
    default_path="${HOME:-$(pwd -P)}"
    echo ""
    echo "📂 指定路徑安裝模式："
    echo "   將在指定路徑下建立："
    echo "   • sunnycore/ - 主程式檔案"
    echo "   • .claude/ - Claude Code 整合檔案"
    echo ""

    local input_path=""
    local max_attempts=3
    local attempt=0

    while [[ $attempt -lt $max_attempts ]]; do
      attempt=$((attempt + 1))

      local prompt_text="請輸入安裝路徑（預設：${default_path}）："
      if [[ $attempt -gt 1 ]]; then
        prompt_text="請輸入有效路徑（預設：${default_path}，剩餘嘗試：$((max_attempts - attempt + 1))）："
      fi

      # 使用改進的讀取函式
      input_path=$(safe_read_with_timeout "$prompt_text" 45 "$default_path")
      local read_result=$?

      if [[ $read_result -ne 0 ]]; then
        warn "⚠️  無法讀取用戶輸入，使用預設路徑：${default_path}"
        INSTALL_BASE="$default_path"
        echo ""
        return
      fi

      # 處理空輸入
      if [[ -z "$input_path" ]]; then
        input_path="$default_path"
      fi

      # 展開路徑
      local expanded_path
      expanded_path="$(expand_path "$input_path")"

      # 驗證路徑
      if [[ -z "$expanded_path" ]]; then
        if [[ $attempt -lt $max_attempts ]]; then
          warn "❌ 無效的路徑：${input_path}"
        else
          warn "⚠️  超過最大嘗試次數，使用預設路徑：${default_path}"
          expanded_path="$default_path"
        fi
        continue
      fi

      # 檢查父目錄是否存在或可創建
      local parent_dir
      parent_dir="$(dirname "$expanded_path")"
      if [[ ! -d "$parent_dir" ]]; then
        warn "⚠️  父目錄不存在：${parent_dir}"
        if [[ $attempt -lt $max_attempts ]]; then
          local create_parent
          create_parent=$(safe_read_with_timeout "是否嘗試創建父目錄？[y/N]: " 15 "n")
          case "$create_parent" in
            y|Y|yes|YES)
              if mkdir -p "$parent_dir" 2>/dev/null; then
                info "✓ 成功創建父目錄：${parent_dir}"
              else
                warn "❌ 無法創建父目錄，請選擇其他路徑"
                continue
              fi
              ;;
            *)
              continue
              ;;
          esac
        else
          warn "⚠️  無法創建父目錄，使用預設路徑：${default_path}"
          expanded_path="$default_path"
        fi
      fi

      # 成功獲得有效路徑
      INSTALL_BASE="$expanded_path"
      echo ""
      info "✓ 選擇的安裝路徑：${INSTALL_BASE}"
      echo ""
      return
    done
  else
    # 非互動模式且未指定路徑，使用預設值
    local default_path
    default_path="${HOME:-$(pwd -P)}"
    warn "⚠️  未指定安裝路徑，使用預設路徑：${default_path}"
    INSTALL_BASE="$default_path"
  fi
}

# 輔助函式：安全讀取用戶輸入，支援超時
safe_read_with_timeout() {
  local prompt="$1"
  local timeout="${2:-30}"  # 預設 30 秒超時
  local default_value="${3:-}"  # 預設值
  local result_var="$4"  # 結果變數名稱

  local response=""
  local read_result=0

  # 臨時禁用嚴格模式
  set +e

  if [[ -t 0 ]] && [[ -c /dev/tty ]]; then
    # 嘗試從終端讀取，支援超時
    if command -v timeout >/dev/null 2>&1; then
      # 使用 timeout 命令
      response=$(timeout "$timeout" bash -c "read -r -p '$prompt' response; echo \\\$response" < /dev/tty 2>/dev/null)
      read_result=$?
    else
      # 沒有 timeout 命令，使用普通 read
      read -r -p "$prompt" response < /dev/tty 2>/dev/null
      read_result=$?
    fi
  else
    # 嘗試直接讀取
    if command -v timeout >/dev/null 2>&1; then
      response=$(timeout "$timeout" bash -c "read -r -p '$prompt' response; echo \\\$response" 2>/dev/null)
      read_result=$?
    else
      read -r -p "$prompt" response
      read_result=$?
    fi
  fi

  set -e  # 重新啟用嚴格模式

  # 處理結果
  if [[ $read_result -eq 0 ]]; then
    # 讀取成功
    if [[ -z "$response" && -n "$default_value" ]]; then
      response="$default_value"
    fi
  elif [[ $read_result -eq 124 ]]; then
    # 超時
    warn "讀取用戶輸入超時 (${timeout}秒)，使用預設值：${default_value:-取消操作}"
    response="$default_value"
    read_result=0
  else
    # 讀取失敗
    if [[ -n "$default_value" ]]; then
      warn "無法讀取用戶輸入，使用預設值：$default_value"
      response="$default_value"
      read_result=0
    fi
  fi

  # 將結果賦值給指定變數
  if [[ -n "$result_var" ]]; then
    printf -v "$result_var" '%s' "$response"
  else
    echo "$response"
  fi

  return $read_result
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
      echo ""
      warn "⚠️  目標目錄已存在：${target_dir}"
      echo "此操作將會刪除該目錄下的所有檔案並重新安裝。"
      echo ""

      local yn=""
      local read_result=0

      # 使用改進的讀取函式
      yn=$(safe_read_with_timeout "是否清空後重新安裝？[y/N]: " 30 "n")
      read_result=$?

      if [[ $read_result -ne 0 ]]; then
        # 讀取完全失敗
        echo ""
        warn "❌ 無法讀取用戶輸入"
        echo "解決方案："
        echo "  1. 使用 -y 參數自動同意覆寫：bash $SCRIPT_NAME -y"
        echo "  2. 手動刪除目錄：rm -rf $target_dir"
        echo "  3. 選擇其他安裝路徑"
        echo ""
        exit 1
      fi

      log "使用者回應: $yn"
      case "$yn" in
        y|Y|yes|YES)
          echo ""
          info "✓ 同意覆寫，清空既有目錄：$target_dir"
          log "使用者同意覆寫，清空目錄"
          run_cmd rm -rf "$target_dir"
          ;;
        n|N|no|NO|"")
          echo ""
          warn "❌ 使用者取消安裝"
          echo "已取消安裝。如需重新安裝，請："
          echo "  1. 使用 -y 參數自動同意覆寫"
          echo "  2. 手動刪除目錄後重新執行"
          echo "  3. 選擇其他安裝路徑"
          echo ""
          exit 1
          ;;
        *)
          echo ""
          warn "❌ 無效的選項：$yn"
          warn "   將取消安裝以避免意外操作"
          echo ""
          exit 1
          ;;
      esac
    else
      # 非互動模式且目標目錄存在，給出警告但不清空
      warn "⚠️  目標目錄已存在但非互動模式，將保留現有檔案：$target_dir"
      warn "   如需覆寫，請使用 -y 參數或手動刪除該目錄"
    fi
  else
    log "目標目錄不存在，無需覆寫"
  fi
}


install_claude_code() {
  local src dst_sunnycore dst_claude commands_dst agents_dst settings_dst use_local=0

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
        run_cmd mkdir -p "$src/agents"
        run_cmd touch "$src/README.md"
        run_cmd touch "$src/commands/example.json"
        run_cmd touch "$src/agents/example.md"
        run_cmd touch "$src/settings.local.json"
      else
        log "檢查克隆目錄內容..."
        if [[ $QUIET_MODE -eq 0 ]]; then
          log "暫存目錄內容:"
          ls -la "$TMP_CLONE_DIR" || true
        fi
        if [[ -d "$TMP_CLONE_DIR/claude code" ]]; then
          src="$TMP_CLONE_DIR/claude code"
          log "找到 claude code 目錄: $src"
          info "成功從遠端倉庫獲取來源"
        else
          warn "遠端倉庫中找不到 'claude code' 來源資料夾，將嘗試使用本地來源"
          if [[ $QUIET_MODE -eq 0 ]]; then
            log "可用的目錄:"
            find "$TMP_CLONE_DIR" -type d -maxdepth 2 || true
          fi
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
  local agents_src="$src/agents"
  local settings_src="$src/settings.local.json"
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: 假設 commands 來源目錄存在於 $commands_src"
    info "dry-run: 假設 agents 來源目錄存在於 $agents_src"
    info "dry-run: 假設 settings.local.json 檔案存在於 $settings_src"
  elif [[ ! -d "$commands_src" ]]; then
    error "來源目錄缺少 commands 子目錄：$commands_src"
    exit 1
  fi

  # 根據安裝類型設定目標目錄
  local install_sunnycore=1
  if [[ "${INSTALL_TYPE:-}" == "project" ]]; then
    # 專案安裝：只安裝 .claude 目錄
    install_sunnycore=0
    dst_sunnycore=""
    dst_claude="${INSTALL_BASE%/}/.claude"
  else
    # 指定路徑安裝：安裝 sunnycore 和 .claude 目錄
    install_sunnycore=1
    dst_sunnycore="${INSTALL_BASE%/}/sunnycore"
    dst_claude="${INSTALL_BASE%/}/.claude"
  fi
  
  commands_dst="${dst_claude%/}/commands"
  agents_dst="${dst_claude%/}/agents"
  settings_dst="${dst_claude%/}/settings.local.json"

  log "設定目標目錄"
  log "安裝基礎路徑: $INSTALL_BASE"
  log "安裝類型: ${INSTALL_TYPE:-custom}"
  if [[ $install_sunnycore -eq 1 ]]; then
    log "Sunnycore 目標目錄: $dst_sunnycore"
  fi
  log "Claude commands 目標目錄: $commands_dst"
  log "Claude agents 目標目錄: $agents_dst"
  log "Claude settings.local.json 目標：$settings_dst"

  info "安裝版本：claude code"
  info "來源：$src"
  if [[ $install_sunnycore -eq 1 ]]; then
    info "Sunnycore 目標：$dst_sunnycore"
  fi
  info "Claude commands 目標：$commands_dst"
  info "Claude agents 目標：$agents_dst"
  info "Claude settings.local.json 目標：$settings_dst"

  if [[ $DRY_RUN -eq 1 ]]; then
    log "dry-run: 跳過來源目錄實際檢查"
    info "dry-run: 假設來源目錄包含必要檔案"
  elif [[ -d "$src" ]]; then
    if [[ $QUIET_MODE -eq 0 ]]; then
      log "來源目錄存在，內容:"
      ls -la "$src" | head -10 || true
    fi
    log "來源目錄檔案數量: $(find "$src" -type f | wc -l)"
  else
    error "來源目錄不存在: $src"
    exit 1
  fi

  require_cmd mkdir
  require_cmd cp
  require_cmd rm
  require_cmd find

  # 根據安裝類型確認是否需要覆寫
  if [[ $install_sunnycore -eq 1 ]]; then
    confirm_overwrite_if_needed "$dst_sunnycore"
  fi
  confirm_overwrite_if_needed "$commands_dst"
  
  # 創建必要的目錄
  if [[ $install_sunnycore -eq 1 ]]; then
    run_cmd mkdir -p "$dst_sunnycore"
  fi
  run_cmd mkdir -p "$dst_claude"

  # 只在指定路徑安裝時拷貝 Sunnycore 檔案
  if [[ $install_sunnycore -eq 1 ]]; then
    info "開始拷貝 Sunnycore 檔案…"
    log "執行拷貝命令: cp -a $src/. $dst_sunnycore/"
    run_cmd cp -a "$src/." "$dst_sunnycore/"
  fi

  info "開始拷貝 commands 檔案至 .claude…"
  log "執行拷貝命令: cp -a $commands_src $dst_claude/"
  run_cmd cp -a "$commands_src" "$dst_claude/"

  # 拷貝 agents 目錄（如果存在）
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: 拷貝 agents 至 .claude…"
    log "dry-run: cp -a $agents_src $dst_claude/"
  elif [[ -d "$agents_src" ]]; then
    info "開始拷貝 agents 檔案至 .claude…"
    log "執行拷貝命令: cp -a $agents_src $dst_claude/"
    run_cmd cp -a "$agents_src" "$dst_claude/"
  else
    log "agents 目錄不存在於來源目錄，跳過拷貝"
  fi

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

  # 只在指定路徑安裝時才需要清理 sunnycore 目錄
  if [[ $install_sunnycore -eq 1 ]]; then
    info "移除 Sunnycore 目錄中的 commands 目錄"
    log "執行移除命令: rm -rf $dst_sunnycore/commands"
    run_cmd rm -rf "$dst_sunnycore/commands"

    # 移除 Sunnycore 目錄中的 agents 目錄（如果存在）
    if [[ $DRY_RUN -eq 1 ]]; then
      info "dry-run: 移除 Sunnycore 目錄中的 agents 目錄"
      log "dry-run: rm -rf $dst_sunnycore/agents"
    elif [[ -d "$dst_sunnycore/agents" ]]; then
      info "移除 Sunnycore 目錄中的 agents 目錄"
      log "執行移除命令: rm -rf $dst_sunnycore/agents"
      run_cmd rm -rf "$dst_sunnycore/agents"
    fi

    # 移除 Sunnycore 目錄中的 settings.local.json（如果存在）
    if [[ $DRY_RUN -eq 1 ]]; then
      info "dry-run: 移除 Sunnycore 目錄中的 settings.local.json"
      log "dry-run: rm -f $dst_sunnycore/settings.local.json"
    elif [[ -f "$dst_sunnycore/settings.local.json" ]]; then
      info "移除 Sunnycore 目錄中的 settings.local.json"
      log "執行移除命令: rm -f $dst_sunnycore/settings.local.json"
      run_cmd rm -f "$dst_sunnycore/settings.local.json"
    fi
  fi

  # 只在指定路徑安裝時驗證 sunnycore 目錄
  if [[ $install_sunnycore -eq 1 ]]; then
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

        if [[ -d "$dst_sunnycore/agents" ]]; then
          warn "Sunnycore 目錄中仍存在 agents 目錄，將移除"
          run_cmd rm -rf "$dst_sunnycore/agents"
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
          if [[ $QUIET_MODE -eq 0 ]]; then
            log "Sunnycore 目標目錄頂層內容:"
            ls -la "$dst_sunnycore" | head -10 || true
          fi
        fi
      else
        warn "Sunnycore 安裝目錄不存在：$dst_sunnycore，略過檢查"
      fi
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
        if [[ $QUIET_MODE -eq 0 ]]; then
          log "commands 目錄頂層內容:"
          ls -la "$commands_dst" | head -10 || true
        fi
      fi
    else
      error ".claude/commands 目錄不存在：$commands_dst"
      exit 1
    fi
  fi

  log "開始安裝後驗證 (.claude/agents)…"
  if [[ $DRY_RUN -eq 1 ]]; then
    info "dry-run: 將於 $agents_dst 執行安裝後檢查"
  else
    if [[ -d "$agents_dst" ]]; then
      log "檢查 agents 目錄: $agents_dst"
      local agents_file_count
      agents_file_count=$(find "$agents_dst" -type f | wc -l)
      log "agents 目錄檔案數量: $agents_file_count"
      
      if [[ $agents_file_count -eq 0 ]]; then
        warn ".claude/agents 目錄為空：$agents_dst"
      else
        log "agents 驗證成功，目錄包含 $agents_file_count 個檔案"
        if [[ $QUIET_MODE -eq 0 ]]; then
          log "agents 目錄頂層內容:"
          ls -la "$agents_dst" | head -10 || true
        fi
      fi
    else
      log ".claude/agents 目錄不存在，略過檢查"
    fi
  fi

  # 根據安裝類型顯示不同的成功訊息
  if [[ $install_sunnycore -eq 1 ]]; then
    ok "Claude code installation completed: $dst_sunnycore, $commands_dst, $agents_dst and $settings_dst"
  else
    ok "Claude code installation completed: $commands_dst, $agents_dst and $settings_dst"
  fi
}

main() {
  log "=== Sunnycore 安裝腳本開始執行 ==="
  log "腳本版本: $VERSION"
  log "腳本路徑: $0"
  log "腳本目錄: $SCRIPT_DIR"
  log "傳入參數: $*"
  log "當前工作目錄: $(pwd)"
  log "當前使用者: $(whoami)"

  # 設置錯誤處理
  set -euo pipefail

  # 捕獲中斷信號
  trap 'echo ""; warn "安裝被用戶中斷"; cleanup; exit 130' INT TERM

  parse_args "$@"

  log "參數解析完成"
  log "DRY_RUN: $DRY_RUN"
  log "AUTO_YES: $AUTO_YES"
  log "INSTALL_BASE: ${INSTALL_BASE:-未設定}"
  log "SELECTED_VERSION: ${SELECTED_VERSION:-未設定}"
  log "REPO_URL: ${REPO_URL:-未設定}"
  log "BRANCH: ${BRANCH:-未設定}"

  # 系統環境檢測
  check_system_environment

  # 歡迎信息
  if [[ $INTERACTIVE_MODE -eq 1 && $QUIET_MODE -eq 0 ]]; then
    echo ""
    info "🌞 歡迎使用 Sunnycore 安裝程式！"
    info "   版本：$VERSION"
    echo ""
  fi

  prompt_select_version
  log "選擇的版本: $SELECTED_VERSION"

  prompt_install_type
  log "安裝類型: $INSTALL_TYPE"

  prompt_install_path
  log "安裝路徑: $INSTALL_BASE"

  # 最後確認
  if [[ $INTERACTIVE_MODE -eq 1 && $AUTO_YES -eq 0 ]]; then
    echo ""
    info "📋 安裝摘要："
    echo "   版本：Claude Code"
    echo "   類型：$([[ $INSTALL_TYPE == "project" ]] && echo "專案安裝" || echo "指定路徑安裝")"
    echo "   路徑：$INSTALL_BASE"
    if [[ -d "$INSTALL_BASE/.claude" ]] || [[ -d "$INSTALL_BASE/sunnycore" ]]; then
      echo "   狀態：⚠️  目標目錄已存在，將覆寫"
    else
      echo "   狀態：✓ 目標目錄可用"
    fi
    echo ""

    local final_confirm
    final_confirm=$(safe_read_with_timeout "確認開始安裝？[Y/n]: " 20 "y")
    case "$final_confirm" in
      n|N|no|NO)
        warn "❌ 用戶取消安裝"
        exit 1
        ;;
      *)
        ok "✓ 開始安裝..."
        ;;
    esac
  fi

  case "$SELECTED_VERSION" in
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

  # 成功完成
  if [[ $INTERACTIVE_MODE -eq 1 || $QUIET_MODE -eq 0 ]]; then
    echo ""
    ok "🎉 Sunnycore 安裝完成！"
    echo ""
    info "接下來可以："
    echo "   1. 重啟 Claude Code"
    echo "   2. 檢查 .claude/ 目錄中的檔案"
    echo "   3. 開始使用 Sunnycore 功能"
    echo ""
  fi

  log "=== Sunnycore 安裝腳本執行完成 ==="
}

main "$@"
