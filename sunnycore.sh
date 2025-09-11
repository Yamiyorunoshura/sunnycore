#!/usr/bin/env bash

set -euo pipefail

#
# sunnycore 安裝腳本
# 功能：
# - 遠端抓取 sunnycore 專案到暫存目錄
# - 安裝至使用者指定路徑下的 sunnycore 目錄
# - 先安裝 general，再覆蓋版本專屬檔（warp code / claude code / codex）
# - 支援乾跑（--dry-run）、非互動（--yes）、舊配置刪除或備份
#

SCRIPT_NAME="$(basename "$0")"
VERSION="0.1.0"

# 預設
REPO_URL="https://github.com/Yamiyorunoshura/sunnycore.git"
# 若未指定分支，將自動偵測遠端預設分支（失敗時嘗試 master/main）
BRANCH=""
SELECTED_VARIANT=""
DEST_PATH=""
YES_ALL=false
DRY_RUN=false
KEEP_TMP=false
DO_BACKUP=false
SOURCE_PATH=""   # 本地源（跳過遠端抓取）

TMP_ROOT=""
SRC_DIR=""       # 暫存抓取後的專案根目錄

log()   { printf "[INFO] %s\n" "$*"; }
warn()  { printf "[WARN] %s\n" "$*" 1>&2; }
error() { printf "[ERROR] %s\n" "$*" 1>&2; }
die()   { error "$*"; exit 1; }

usage() {
  cat <<EOF
用法：
  $SCRIPT_NAME [選項]

選項：
  --repo <URL>           指定 sunnycore 遠端 repo（預設：https://github.com/Yamiyorunoshura/sunnycore.git）
  --branch <NAME>        指定分支（預設：自動偵測；失敗時嘗試 master/main）
  --version <VARIANT>    指定版本：warp | claude | codex（必要或互動選）
  --path <DEST>          指定安裝根路徑（將安裝到 <DEST>/sunnycore）
  --source-path <PATH>   使用本地來源（跳過遠端抓取，用於離線或開發）
  --yes                  非互動模式，全數預設為是
  --dry-run              乾跑模式，只顯示將執行的動作
  --keep-tmp             保留暫存目錄（預設腳本結束會清理）
  --backup               若存在舊的 sunnycore，先備份後再安裝
  --help                 顯示說明
  --version              顯示腳本版本

說明：
  - 若提供 --repo，腳本將以 git clone --depth 1 抓取該專案到暫存。
  - 未提供 --repo 時，可用 --source-path 指向本地專案根目錄做為來源。
  - 安裝順序固定為 general -> 版本目錄覆蓋，版本目錄對應：
      warp  -> "warp code/"
      claude-> "claude code/"
      codex -> "codex/"
EOF
}

print_version() {
  printf "%s %s\n" "$SCRIPT_NAME" "$VERSION"
}

cleanup() {
  if [ -n "$TMP_ROOT" ] && [ -d "$TMP_ROOT" ] && [ "$KEEP_TMP" = false ]; then
    rm -rf "$TMP_ROOT" || true
  fi
}
trap cleanup EXIT

confirm() {
  if [ "$YES_ALL" = true ]; then
    return 0
  fi
  printf "%s [y/N]: " "$1"
  read -r ans || true
  case "${ans:-}" in
    y|Y|yes|YES) return 0 ;;
    *) return 1 ;;
  esac
}

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "找不到指令：$1"
}

parse_args() {
  while [ $# -gt 0 ]; do
    case "$1" in
      --repo)
        REPO_URL=${2:-}; shift 2 ;;
      --branch)
        BRANCH=${2:-}; shift 2 ;;
      --version)
        SELECTED_VARIANT=${2:-}; shift 2 ;;
      --path)
        DEST_PATH=${2:-}; shift 2 ;;
      --source-path)
        SOURCE_PATH=${2:-}; shift 2 ;;
      --yes)
        YES_ALL=true; shift ;;
      --dry-run)
        DRY_RUN=true; shift ;;
      --keep-tmp)
        KEEP_TMP=true; shift ;;
      --backup)
        DO_BACKUP=true; shift ;;
      --help|-h)
        usage; exit 0 ;;
      --version|-V)
        print_version; exit 0 ;;
      *)
        die "未知參數：$1（使用 --help 查看說明）" ;;
    esac
  done
}

abs_path() {
  # 將輸入轉為絕對路徑；支援 ~ 展開
  # 用法：abs_path <path>
  local p="$1"
  # shellcheck disable=SC2086
  eval p="${p}"
  if [ -d "$p" ]; then
    (cd "$p" && pwd -P)
  else
    local d
    d=$(dirname -- "$p")
    local b
    b=$(basename -- "$p")
    (cd "$d" 2>/dev/null && printf "%s/%s\n" "$(pwd -P)" "$b")
  fi
}

select_version_if_needed() {
  if [ -n "$SELECTED_VARIANT" ]; then
    case "$SELECTED_VARIANT" in
      warp|claude|codex) return 0 ;;
      *) die "不支援的版本：$SELECTED_VARIANT（可用：warp|claude|codex）" ;;
    esac
  fi

  if [ "$YES_ALL" = true ]; then
    die "非互動模式需提供 --version（warp|claude|codex）"
  fi

  printf "請選擇版本（輸入數字）：\n"
  printf "  1) warp\n  2) claude\n  3) codex\n> "
  local choice
  read -r choice || true
  case "${choice:-}" in
    1) SELECTED_VARIANT="warp" ;;
    2) SELECTED_VARIANT="claude" ;;
    3) SELECTED_VARIANT="codex" ;;
    *) die "無效選擇" ;;
  esac
}

resolve_variant_dirname() {
  case "$1" in
    warp)   printf "warp code" ;;
    claude) printf "claude code" ;;
    codex)  printf "codex" ;;
    *)      die "未知版本：$1" ;;
  esac
}

prepare_tmp() {
  if [ -z "$TMP_ROOT" ]; then
    TMP_ROOT="$(mktemp -d 2>/dev/null || mktemp -d -t sunnycore)"
    log "建立暫存目錄：$TMP_ROOT"
  fi
}

fetch_remote() {
  if [ -n "$SOURCE_PATH" ]; then
    SRC_DIR="$(abs_path "$SOURCE_PATH")"
    [ -d "$SRC_DIR" ] || die "本地來源不存在：$SRC_DIR"
    log "使用本地來源：$SRC_DIR（跳過遠端抓取）"
    return 0
  fi

  [ -n "$REPO_URL" ] || die "請提供 --repo <URL> 或改用 --source-path <PATH>"
  need_cmd git

  prepare_tmp
  local dst="$TMP_ROOT/src"
  if [ "$DRY_RUN" = true ]; then
    local label
    if [ -n "$BRANCH" ]; then label="$BRANCH"; else label="<auto>"; fi
    log "[dry-run] 將以 git clone --depth 1 --branch '${label}' '${REPO_URL}' '${dst}'（<auto> 代表自動偵測預設分支）"
    SRC_DIR="$dst"
    return 0
  fi

  # 解析要使用的分支：優先採用使用者指定；否則嘗試偵測遠端預設分支
  local branch_to_use="${BRANCH}"
  if [ -z "$branch_to_use" ]; then
    local detected
    detected=$(git ls-remote --symref "$REPO_URL" HEAD 2>/dev/null | sed -n 's#^ref: refs/heads/\(.*\)\tHEAD$#\1#p') || true
    if [ -n "$detected" ]; then
      branch_to_use="$detected"
      log "偵測遠端預設分支: ${branch_to_use}"
    else
      branch_to_use="master"
      warn "無法偵測預設分支，先嘗試 'master'（將於失敗時回退 'main'）"
    fi
  fi

  log "抓取遠端: ${REPO_URL} # 分支: ${branch_to_use}"
  if git clone --depth 1 --branch "$branch_to_use" "$REPO_URL" "$dst"; then
    :
  else
    warn "抓取失敗（分支: ${branch_to_use}），嘗試備選"
    local alt
    if [ "$branch_to_use" = "main" ]; then alt="master"; else alt="main"; fi
    log "改用分支: ${alt}"
    git clone --depth 1 --branch "$alt" "$REPO_URL" "$dst" || die "無法抓取分支：${branch_to_use} 或 ${alt}。請以 --branch 指定正確分支（例如 'master'）。"
    branch_to_use="$alt"
  fi

  SRC_DIR="$dst"

  # 記錄 commit
  (
    cd "$SRC_DIR"
    local rev
    rev=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
    log "抓取完成, 分支=${branch_to_use}, commit=${rev}"
  )
}

validate_source_structure() {
  if [ "$DRY_RUN" = true ]; then
    if [ ! -d "$SRC_DIR" ]; then
      warn "[dry-run] 來源目錄不存在：${SRC_DIR} (模擬繼續)"
      return 0
    fi
    if [ ! -d "$SRC_DIR/general" ]; then
      warn "[dry-run] 來源缺少 general/ (模擬繼續)"
    fi
    local variant_dir
    variant_dir="$(resolve_variant_dirname "$SELECTED_VARIANT")"
    if [ ! -d "$SRC_DIR/$variant_dir" ]; then
      warn "[dry-run] 來源缺少版本目錄：${variant_dir}/ (模擬繼續)"
    fi
    return 0
  fi

  [ -d "$SRC_DIR" ] || die "來源目錄不存在：$SRC_DIR"
  [ -d "$SRC_DIR/general" ] || die "來源缺少必需目錄：general/"

  local variant_dir
  variant_dir="$(resolve_variant_dirname "$SELECTED_VARIANT")"
  [ -d "$SRC_DIR/$variant_dir" ] || die "來源缺少版本目錄：$variant_dir/"
}

resolve_dest_path_if_needed() {
  if [ -z "$DEST_PATH" ]; then
    if [ "$YES_ALL" = true ]; then
      die "非互動模式需提供 --path <DEST>"
    fi
    printf "請輸入安裝根路徑（將安裝到 <路徑>/sunnycore）：\n> "
    read -r DEST_PATH || true
    [ -n "$DEST_PATH" ] || die "未輸入路徑"
  fi
  DEST_PATH="$(abs_path "$DEST_PATH")"
  log "安裝根路徑: ${DEST_PATH}"
}

ensure_dest_writable() {
  local parent
  parent="$(dirname -- "$DEST_PATH")"
  if [ ! -d "$parent" ]; then
    if confirm "父目錄不存在，建立 $parent ？"; then
      [ "$DRY_RUN" = true ] || mkdir -p "$parent"
    else
      die "父目錄不存在：$parent"
    fi
  fi
  if [ ! -d "$DEST_PATH" ]; then
    if confirm "建立安裝根路徑 ${DEST_PATH} ？"; then
      [ "$DRY_RUN" = true ] || mkdir -p "$DEST_PATH"
    else
      die "安裝根路徑不存在: ${DEST_PATH}"
    fi
  fi
  if [ ! -w "$DEST_PATH" ]; then
    warn "目標路徑可能不可寫：$DEST_PATH"
  fi
}

prepare_clean_target() {
  local target_root="$DEST_PATH/sunnycore"
  if [ -e "$target_root" ]; then
    if [ "$DO_BACKUP" = true ]; then
      local ts
      ts=$(date +%Y%m%d-%H%M%S)
      local backup_dir="$DEST_PATH/sunnycore.backup-$ts"
      log "檢測到舊配置，將備份至: ${backup_dir}"
      if [ "$DRY_RUN" = true ]; then
        log "[dry-run] mv '$target_root' '$backup_dir'"
      else
        mv "$target_root" "$backup_dir"
      fi
    else
      if confirm "檢測到舊配置，刪除 ${target_root} 以重建？"; then
        if [ "$DRY_RUN" = true ]; then
          log "[dry-run] rm -rf '$target_root'"
        else
          rm -rf "$target_root"
        fi
      else
        die "使用者取消，未清理舊配置"
      fi
    fi
  fi
  # 建立乾淨的目錄
  if [ "$DRY_RUN" = true ]; then
    log "[dry-run] mkdir -p '$target_root'"
  else
    mkdir -p "$target_root"
  fi
}

have_rsync=false
detect_tools() {
  if command -v rsync >/dev/null 2>&1; then
    have_rsync=true
  else
    warn "找不到 rsync，將以 cp -a 進行複製（較慢且無 dry-run 差異摘要）"
  fi
}

copy_tree() {
  # 用途：將 $1 目錄內容複製到 $2
  # 排除 .git 與暫存資料夾
  local src="$1"
  local dst="$2"
  if [ "$DRY_RUN" = true ] && [ ! -d "$src" ]; then
    log "[dry-run] 假設來源存在：'$src/' -> '$dst/'"
    return 0
  fi

  if [ "$have_rsync" = true ]; then
    # -a 保留屬性；-c 以 checksum 比對，確保版本檔案能可靠覆蓋同名檔案
    local rsync_flags=("-a" "-c" "--exclude" ".git" "--exclude" "*/.git" )
    if [ "$DRY_RUN" = true ]; then
      rsync_flags+=("--dry-run")
    fi
    rsync "${rsync_flags[@]}" "$src/" "$dst/"
  else
    if [ "$DRY_RUN" = true ]; then
      log "[dry-run] cp -a -f '$src/' -> '$dst/'"
    else
      (cd "$src" && find . -mindepth 1 -maxdepth 1 ! -name ".git" -exec cp -a -f {} "$dst/" \;)
    fi
  fi
}

# 若來源目錄中存在 sunnycore/ 子目錄，則以該子目錄為實際負載來源；
# 否則以該來源目錄本身為負載來源。
resolve_payload_dir() {
  local base="$1"
  if [ -d "$base/sunnycore" ]; then
    printf "%s\n" "$base/sunnycore"
  else
    printf "%s\n" "$base"
  fi
}

perform_install() {
  local target_root="$DEST_PATH/sunnycore"
  local variant_dir
  variant_dir="$(resolve_variant_dirname "$SELECTED_VARIANT")"

  local general_src
  general_src="$(resolve_payload_dir "${SRC_DIR}/general")"
  log "安裝 general 來源=${general_src} -> ${target_root}"
  copy_tree "${general_src}" "${target_root}"

  local variant_src
  variant_src="$(resolve_payload_dir "${SRC_DIR}/${variant_dir}")"
  log "覆蓋版本(${SELECTED_VARIANT}: ${variant_dir}) 來源=${variant_src} -> ${target_root}"
  copy_tree "${variant_src}" "${target_root}"
}

main() {
  parse_args "$@"
  select_version_if_needed
  resolve_dest_path_if_needed
  ensure_dest_writable

  fetch_remote
  validate_source_structure

  detect_tools
  prepare_clean_target
  perform_install

  log "安裝完成: 版本=${SELECTED_VARIANT}, 路徑=${DEST_PATH}/sunnycore"
}

main "$@"
