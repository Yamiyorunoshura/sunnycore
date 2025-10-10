#!/usr/bin/env python3
"""
Sunnycore 安裝腳本
從 GitHub 下載並安裝 Sunnycore 系統到指定目錄
"""

import argparse
import os
import sys
import urllib.request
import urllib.parse
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class ProgressBar:
    """帶動畫效果的進度條顯示器"""
    
    # 旋轉動畫符號
    SPINNERS = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    
    def __init__(self, total: int, width: int = 40, prefix: str = "下載進度"):
        """初始化進度條
        
        Args:
            total: 總任務數
            width: 進度條寬度
            prefix: 進度條前綴文字
        """
        self.total = total
        self.width = width
        self.prefix = prefix
        self.current = 0
        self.failed = 0
        self.lock = threading.Lock()
        self.start_time = time.time()
        self.spinner_index = 0
        self.last_update_time = 0
        self.update_interval = 0.1  # 最小更新間隔（秒）
        
    def update(self, increment: int = 1, failed: bool = False):
        """更新進度
        
        Args:
            increment: 增量
            failed: 是否失敗
        """
        with self.lock:
            self.current += increment
            if failed:
                self.failed += increment
            
            # 控制更新頻率，避免刷新太快
            current_time = time.time()
            if current_time - self.last_update_time >= self.update_interval or self.current == self.total:
                self._display()
                self.last_update_time = current_time
    
    def _display(self):
        """顯示進度條（帶動畫效果）"""
        percent = self.current / self.total if self.total > 0 else 0
        filled = int(self.width * percent)
        
        # 使用漸變效果的進度條
        if filled > 0:
            if filled == self.width:
                bar = '█' * self.width
            else:
                bar = '█' * (filled - 1) + '▓' + '░' * (self.width - filled)
        else:
            bar = '░' * self.width
        
        # 計算速度和預估剩餘時間
        elapsed = time.time() - self.start_time
        speed = self.current / elapsed if elapsed > 0 else 0
        remaining = (self.total - self.current) / speed if speed > 0 else 0
        
        # 格式化時間
        elapsed_str = self._format_time(elapsed)
        remaining_str = self._format_time(remaining) if remaining > 0 and self.current < self.total else "完成"
        
        # 旋轉動畫符號（只在未完成時顯示）
        spinner = self.SPINNERS[self.spinner_index % len(self.SPINNERS)] if self.current < self.total else '✓'
        self.spinner_index += 1
        
        # 顯示狀態
        status = f"✓ {self.current - self.failed}"
        if self.failed > 0:
            status += f" ✗ {self.failed}"
        
        # 顯示進度條（緊湊格式）
        print(f"\r{spinner} {self.prefix}: [{bar}] {percent*100:.1f}% ({status}/{self.total}) "
              f"| {speed:.1f} 檔/秒 | {elapsed_str} / {remaining_str}   ",
              end='', flush=True)
    
    def _format_time(self, seconds: float) -> str:
        """格式化時間顯示
        
        Args:
            seconds: 秒數
            
        Returns:
            str: 格式化的時間字符串
        """
        if seconds < 60:
            return f"{seconds:.0f}秒"
        elif seconds < 3600:
            return f"{seconds/60:.1f}分"
        else:
            return f"{seconds/3600:.1f}小時"
    
    def finish(self):
        """完成進度條顯示"""
        with self.lock:
            print()  # 換行
            elapsed = time.time() - self.start_time
            if self.failed > 0:
                print(f"✓ 完成: {self.current - self.failed} 個文件成功, {self.failed} 個失敗 (總耗時: {self._format_time(elapsed)})")
            else:
                print(f"✓ 全部完成: {self.current} 個文件下載成功！(總耗時: {self._format_time(elapsed)})")


def safe_input(prompt: str) -> str:
    """安全的輸入函數，支援管道執行時從 /dev/tty 讀取
    
    Args:
        prompt: 提示信息
        
    Returns:
        str: 用戶輸入的字符串
        
    Raises:
        EOFError: 無法讀取輸入時
    """
    # 先嘗試從標準輸入讀取
    if sys.stdin.isatty():
        return input(prompt)
    
    # 如果標準輸入不是終端（如管道執行），嘗試從 /dev/tty 讀取
    try:
        with open('/dev/tty', 'r') as tty:
            # 輸出提示到標準輸出
            print(prompt, end='', flush=True)
            return tty.readline().rstrip('\n')
    except (OSError, IOError):
        # 如果無法打開 /dev/tty（例如在完全無終端的環境中）
        raise EOFError("無法讀取用戶輸入")


class SunnycoreInstaller:
    """Sunnycore 安裝器"""
    
    def __init__(self, repo: str = "Yamiyorunoshura/sunnycore", branch: str = "master", max_workers: int = 0):
        self.repo = repo
        self.branch = branch
        self.base_raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}"
        self.base_api_url = f"https://api.github.com/repos/{repo}/contents"
        self.max_workers = max_workers
        self.progress_bar = None
        
    def download_file(self, file_path: str, target_path: Path) -> bool:
        """下載單一文件
        
        Args:
            file_path: GitHub 倉庫中的文件路徑
            target_path: 本地目標路徑
            
        Returns:
            bool: 下載是否成功
        """
        # URL 編碼路徑（處理空格等特殊字符）
        encoded_path = urllib.parse.quote(file_path)
        url = f"{self.base_raw_url}/{encoded_path}"
        try:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            with urllib.request.urlopen(url) as response:
                content = response.read()
                with open(target_path, 'wb') as f:
                    f.write(content)
            
            # 更新進度條
            if self.progress_bar:
                self.progress_bar.update(1, failed=False)
            return True
        except Exception as e:
            # 更新進度條（標記為失敗）
            if self.progress_bar:
                self.progress_bar.update(1, failed=True)
            return False
    
    def get_directory_contents(self, dir_path: str) -> List[Dict]:
        """獲取 GitHub 目錄內容
        
        Args:
            dir_path: GitHub 倉庫中的目錄路徑
            
        Returns:
            List[Dict]: 目錄內容列表
        """
        # URL 編碼路徑（處理空格等特殊字符）
        encoded_path = urllib.parse.quote(dir_path)
        url = f"{self.base_api_url}/{encoded_path}?ref={self.branch}"
        try:
            with urllib.request.urlopen(url) as response:
                return json.loads(response.read().decode())
        except Exception as e:
            print(f"✗ 無法獲取目錄內容: {dir_path} - {e}")
            return []
    
    def collect_directory_files(self, source_dir: str, target_dir: Path, file_list: List[Tuple[str, Path]]) -> bool:
        """遞迴收集目錄中的所有文件
        
        Args:
            source_dir: GitHub 倉庫中的目錄路徑
            target_dir: 本地目標目錄
            file_list: 用於存儲文件信息的列表
            
        Returns:
            bool: 收集是否成功
        """
        contents = self.get_directory_contents(source_dir)
        
        if not contents:
            return False
        
        for item in contents:
            if item['type'] == 'file':
                target_path = target_dir / item['name']
                file_list.append((item['path'], target_path))
            elif item['type'] == 'dir':
                sub_target_dir = target_dir / item['name']
                if not self.collect_directory_files(item['path'], sub_target_dir, file_list):
                    return False
        
        return True
    
    def download_files_parallel(self, file_list: List[Tuple[str, Path]]) -> bool:
        """並行下載多個文件
        
        Args:
            file_list: 要下載的文件列表 [(source_path, target_path), ...]
            
        Returns:
            bool: 所有文件是否都下載成功
        """
        if not file_list:
            return True
        
        total = len(file_list)
        
        # 動態調整並行數量：如果 max_workers 為 None 或 0，則使用文件總數
        # 否則使用指定的 max_workers，但至少使用文件總數（不設上限）
        if self.max_workers is None or self.max_workers <= 0:
            workers = total
        else:
            # 使用 max(self.max_workers, total) 確保能充分利用並行
            # 但設置一個合理的上限（200）避免資源耗盡
            workers = min(max(self.max_workers, total), 200)
        
        print(f"\n開始並行下載 {total} 個文件 ({workers} 個並行任務)...")
        
        # 創建進度條
        self.progress_bar = ProgressBar(total=total, prefix="下載進度")
        
        with ThreadPoolExecutor(max_workers=workers) as executor:
            # 提交所有下載任務
            futures = {
                executor.submit(self.download_file, source, target): (source, target)
                for source, target in file_list
            }
            
            # 等待所有任務完成
            for future in as_completed(futures):
                future.result()  # 獲取結果，觸發異常（如果有）
        
        # 完成進度條
        self.progress_bar.finish()
        
        success = self.progress_bar.failed == 0
        return success
    
    def install_claude_code(self, work_dir: Path, auto_yes: bool = False) -> bool:
        """安裝 claude-code 版本
        
        Args:
            work_dir: 工作目錄
            auto_yes: 自動確認模式
            
        Returns:
            bool: 安裝是否成功
        """
        print(f"\n開始安裝 Sunnycore (claude-code 版本) 到: {work_dir}")
        print("=" * 60)
        
        # 檢查目錄是否存在
        claude_dir = work_dir / ".claude"
        sunnycore_dir = work_dir / "sunnycore"
        
        if claude_dir.exists() or sunnycore_dir.exists():
            if not auto_yes:
                # 使用 safe_input 支援管道執行時的互動
                try:
                    response = safe_input(f"\n目錄已存在，是否覆寫? (y/N): ").strip().lower()
                    if response != 'y':
                        print("安裝已取消")
                        return False
                except EOFError:
                    # 如果無法讀取輸入（例如在完全無終端的環境中）
                    print("\n✗ 無法讀取用戶輸入，請使用 -y 參數自動確認覆寫")
                    return False
        
        # 定義要下載的目錄和目標
        directories = [
            # .claude/ 目錄內容
            ("claude code/agents", claude_dir / "agents"),
            ("claude code/commands", claude_dir / "commands"),
            ("claude code/hooks", claude_dir / "hooks"),
            
            # sunnycore/ 目錄內容
            ("claude code/tasks", sunnycore_dir / "tasks"),
            ("claude code/templates", sunnycore_dir / "templates"),
            ("claude code/scripts", sunnycore_dir / "scripts"),
        ]
        
        # 單獨下載的文件
        single_files = [
            ("claude code/DEPENDENCIES.md", sunnycore_dir / "DEPENDENCIES.md"),
            ("claude code/index.json", sunnycore_dir / "index.json"),
            ("claude code/mcp.json", sunnycore_dir / "mcp.json"),
            ("claude code/README.md", sunnycore_dir / "README.md"),
            ("claude code/CLAUDE.md", sunnycore_dir / "CLAUDE.md"),
        ]
        
        # 收集所有要下載的文件
        print("\n正在掃描目錄結構...")
        all_files = []
        
        # 收集目錄中的所有文件
        for source_dir, target_dir in directories:
            print(f"  掃描: {source_dir}")
            if not self.collect_directory_files(source_dir, target_dir, all_files):
                print(f"  ✗ 無法掃描目錄: {source_dir}")
                return False
        
        # 添加單獨的配置文件
        all_files.extend(single_files)
        
        # 並行下載所有文件
        success = self.download_files_parallel(all_files)
        
        if success:
            print("\n" + "=" * 60)
            print("✓ 安裝完成!")
            print(f"\n安裝結構:")
            print(f"{work_dir}/")
            print(f"├── .claude/              # Claude 專用配置")
            print(f"│   ├── agents/          # Agent 定義")
            print(f"│   ├── commands/        # 角色命令定義")
            print(f"│   └── hooks/           # Claude Hooks")
            print(f"└── sunnycore/           # Sunnycore 系統檔案")
            print(f"    ├── CLAUDE.md        # Claude Code 專案指引")
            print(f"    ├── config.yaml")
            print(f"    ├── tasks/")
            print(f"    ├── templates/")
            print(f"    └── ...")
            print("\n請查看 sunnycore/CLAUDE.md 開始使用 Sunnycore!")
        else:
            print("\n✗ 安裝過程中出現錯誤")
        
        return success
    
    def install_cursor(self, work_dir: Path, auto_yes: bool = False) -> bool:
        """安裝 cursor 版本
        
        Args:
            work_dir: 工作目錄
            auto_yes: 自動確認模式
            
        Returns:
            bool: 安裝是否成功
        """
        print(f"\n開始安裝 Sunnycore (cursor 版本) 到: {work_dir}")
        print("=" * 60)
        
        # 檢查目錄是否存在
        cursor_dir = work_dir / ".cursor"
        sunnycore_dir = work_dir / "sunnycore"
        
        if cursor_dir.exists() or sunnycore_dir.exists():
            if not auto_yes:
                # 使用 safe_input 支援管道執行時的互動
                try:
                    response = safe_input(f"\n目錄已存在，是否覆寫? (y/N): ").strip().lower()
                    if response != 'y':
                        print("安裝已取消")
                        return False
                except EOFError:
                    # 如果無法讀取輸入（例如在完全無終端的環境中）
                    print("\n✗ 無法讀取用戶輸入，請使用 -y 參數自動確認覆寫")
                    return False
        
        # 定義要下載的目錄和目標
        directories = [
            # .cursor/ 目錄內容
            ("cursor/commands", cursor_dir / "commands"),
            
            # sunnycore/ 目錄內容
            ("cursor/tasks", sunnycore_dir / "tasks"),
            ("cursor/templates", sunnycore_dir / "templates"),
            ("cursor/scripts", sunnycore_dir / "scripts"),
        ]
        
        # 單獨下載的文件
        single_files = [
            ("cursor/DEPENDENCIES.md", sunnycore_dir / "DEPENDENCIES.md"),
            ("cursor/index.json", sunnycore_dir / "index.json"),
            ("cursor/mcp.json", sunnycore_dir / "mcp.json"),
            ("cursor/README.md", sunnycore_dir / "README.md"),
            ("cursor/cursor.mdc", sunnycore_dir / "cursor.mdc"),
        ]
        
        # 收集所有要下載的文件
        print("\n正在掃描目錄結構...")
        all_files = []
        
        # 收集目錄中的所有文件
        for source_dir, target_dir in directories:
            print(f"  掃描: {source_dir}")
            if not self.collect_directory_files(source_dir, target_dir, all_files):
                print(f"  ✗ 無法掃描目錄: {source_dir}")
                return False
        
        # 添加單獨的配置文件
        all_files.extend(single_files)
        
        # 並行下載所有文件
        success = self.download_files_parallel(all_files)
        
        if success:
            print("\n" + "=" * 60)
            print("✓ 安裝完成!")
            print(f"\n安裝結構:")
            print(f"{work_dir}/")
            print(f"├── .cursor/              # Cursor 專用配置")
            print(f"│   └── commands/        # 角色命令定義")
            print(f"└── sunnycore/           # Sunnycore 系統檔案")
            print(f"    ├── cursor.mdc     # Cursor 專案指引")
            print(f"    ├── config.yaml")
            print(f"    ├── tasks/")
            print(f"    ├── templates/")
            print(f"    └── ...")
            print("\n請查看 sunnycore/cursor.mdc 開始使用 Sunnycore!")
        else:
            print("\n✗ 安裝過程中出現錯誤")
        
        return success


def main():
    """主函數"""
    parser = argparse.ArgumentParser(
        description="Sunnycore 安裝腳本 - 從 GitHub 下載並安裝 Sunnycore 系統",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  # 互動模式 - 可選擇專案安裝或自訂路徑（預設 claude-code 版本）
  python3 install.py
  
  # 安裝 cursor 版本
  python3 install.py -v cursor -p ~/myproject
  
  # 從管道執行 - 完整支援互動模式
  curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/install.py | python3
  
  # 非互動模式 - 直接指定路徑和版本
  python3 install.py -v cursor -p ~/myproject -y
  
  # 從管道執行 - 安裝 cursor 版本
  curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/install.py | python3 - -v cursor -p ~/myproject -y
  
  # 限制並行數量（例如：限制為 20 個並行任務）
  python3 install.py -v cursor -p ~/myproject --max-workers 20

版本說明:
  1. claude-code: 適用於 Claude Code，安裝 .claude/ 和 sunnycore/ 目錄
  2. cursor: 適用於 Cursor 編輯器，安裝 .cursor/ 和 sunnycore/ 目錄

模式說明:
  1. 專案安裝: 在當前工作目錄建立版本對應的目錄結構
  2. 自訂安裝: 在指定路徑建立版本對應的目錄結構
  
並行下載:
  預設會根據文件數量自動調整並行數（上限 200），實現最快速度
  使用 --max-workers 可以限制並行數量（如網路環境有限制時）
  
特殊支援:
  腳本支援從管道執行時的互動模式，會自動從 /dev/tty 讀取輸入
  若在完全無終端環境中執行，請使用 -p 和 -y 參數
        """
    )
    
    parser.add_argument(
        '-v', '--version',
        choices=['claude-code', 'cursor'],
        default='claude-code',
        help='版本選擇 (claude-code 或 cursor)'
    )
    
    parser.add_argument(
        '-p', '--path',
        type=str,
        help='安裝路徑 (支援 ~/)'
    )
    
    parser.add_argument(
        '-y', '--yes',
        action='store_true',
        help='自動確認所有操作'
    )
    
    parser.add_argument(
        '--repo',
        default='Yamiyorunoshura/sunnycore',
        help='GitHub 倉庫 (預設: Yamiyorunoshura/sunnycore)'
    )
    
    parser.add_argument(
        '--branch',
        default='master',
        help='分支名稱 (預設: master)'
    )
    
    parser.add_argument(
        '--max-workers',
        type=int,
        default=0,
        help='最大並行下載數 (預設: 0 = 自動根據文件數量調整，上限 200)'
    )
    
    args = parser.parse_args()
    
    # 互動模式 - 當沒有指定路徑時進入互動模式
    if not args.path:
        print("Sunnycore 安裝程式")
        print("=" * 60)
        
        try:
            # 版本選擇（如果未通過參數指定）
            if not any(arg in sys.argv for arg in ['-v', '--version']):
                print("\n請選擇安裝版本:")
                print("1. claude-code (適用於 Claude Code)")
                print("2. cursor (適用於 Cursor 編輯器)")
                
                version_choice = safe_input("\n請輸入選項 (1/2，預設: 1): ").strip()
                
                if version_choice == '2':
                    args.version = 'cursor'
                else:
                    args.version = 'claude-code'
            
            # 模式選擇
            print("\n請選擇安裝模式:")
            print("1. 專案安裝 (安裝到當前工作目錄)")
            print("2. 自訂安裝 (自行指定安裝路徑)")
            
            mode = safe_input("\n請輸入選項 (1/2，預設: 1): ").strip()
            
            if mode == '2':
                # 自訂安裝模式
                default_path = os.path.expanduser("~/sunnycore")
                user_input = safe_input(f"\n請輸入安裝路徑 (預設: {default_path}): ").strip()
                install_path = Path(os.path.expanduser(user_input) if user_input else default_path)
            else:
                # 專案安裝模式（預設）
                current_dir = os.getcwd()
                print(f"\n✓ 將安裝到當前工作目錄: {current_dir}")
                install_path = Path(current_dir)
                
        except EOFError:
            # 如果無法讀取輸入（例如在完全無終端的環境中）
            print("\n✗ 無法讀取用戶輸入，請使用 -p 和 -v 參數指定安裝路徑和版本")
            sys.exit(1)
    else:
        # 獲取安裝路徑
        install_path = Path(os.path.expanduser(args.path))
    
    # 創建安裝器
    installer = SunnycoreInstaller(repo=args.repo, branch=args.branch, max_workers=args.max_workers)
    
    # 執行安裝
    try:
        if args.version == 'claude-code':
            success = installer.install_claude_code(install_path, auto_yes=args.yes)
            sys.exit(0 if success else 1)
        elif args.version == 'cursor':
            success = installer.install_cursor(install_path, auto_yes=args.yes)
            sys.exit(0 if success else 1)
        else:
            print(f"✗ 不支援的版本: {args.version}")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n安裝已取消")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ 安裝失敗: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

