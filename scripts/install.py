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
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, List, Optional, Tuple


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
    
    def __init__(self, repo: str = "Yamiyorunoshura/sunnycore", branch: str = "master", max_workers: int = 10):
        self.repo = repo
        self.branch = branch
        self.base_raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}"
        self.base_api_url = f"https://api.github.com/repos/{repo}/contents"
        self.max_workers = max_workers
        self.lock = threading.Lock()
        self.total_files = 0
        self.completed_files = 0
        self.failed_files = 0
        
    def download_file(self, file_path: str, target_path: Path, show_progress: bool = True) -> bool:
        """下載單一文件
        
        Args:
            file_path: GitHub 倉庫中的文件路徑
            target_path: 本地目標路徑
            show_progress: 是否顯示進度
            
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
            
            with self.lock:
                self.completed_files += 1
                if show_progress:
                    print(f"  [{self.completed_files}/{self.total_files}] ✓ {file_path}")
            return True
        except Exception as e:
            with self.lock:
                self.failed_files += 1
                self.completed_files += 1
                if show_progress:
                    print(f"  [{self.completed_files}/{self.total_files}] ✗ {file_path} - {e}")
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
        
        self.total_files = len(file_list)
        self.completed_files = 0
        self.failed_files = 0
        
        print(f"\n開始並行下載 {self.total_files} 個文件 (最多 {self.max_workers} 個並行任務)...")
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有下載任務
            futures = {
                executor.submit(self.download_file, source, target): (source, target)
                for source, target in file_list
            }
            
            # 等待所有任務完成
            for future in as_completed(futures):
                future.result()  # 獲取結果，觸發異常（如果有）
        
        success = self.failed_files == 0
        if success:
            print(f"\n✓ 所有文件下載完成！")
        else:
            print(f"\n✗ {self.failed_files} 個文件下載失敗")
        
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
            
            # sunnycore/ 目錄內容
            ("claude code/tasks", sunnycore_dir / "tasks"),
            ("claude code/templates", sunnycore_dir / "templates"),
            ("claude code/scripts", sunnycore_dir / "scripts"),
        ]
        
        # 單獨下載的文件
        single_files = [
            ("claude code/config.yaml", sunnycore_dir / "config.yaml"),
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
            print(f"│   └── commands/        # 角色命令定義")
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


def main():
    """主函數"""
    parser = argparse.ArgumentParser(
        description="Sunnycore 安裝腳本 - 從 GitHub 下載並安裝 Sunnycore 系統",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  # 互動模式 - 可選擇專案安裝或自訂路徑
  python3 install.py
  
  # 從管道執行 - 完整支援互動模式
  curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/install.py | python3
  
  # 非互動模式 - 直接指定路徑
  python3 install.py -p ~/myproject
  
  # 非互動模式 - 指定路徑並自動確認覆寫
  python3 install.py -p ~/myproject -y
  
  # 從管道執行 - 直接指定路徑和自動確認
  curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/install.py | python3 - -p ~/myproject -y

模式說明:
  1. 專案安裝: 在當前工作目錄建立 .claude/ 和 sunnycore/ 目錄
  2. 自訂安裝: 在指定路徑建立 .claude/ 和 sunnycore/ 目錄
  
特殊支援:
  腳本支援從管道執行時的互動模式，會自動從 /dev/tty 讀取輸入
  若在完全無終端環境中執行，請使用 -p 和 -y 參數
        """
    )
    
    parser.add_argument(
        '-v', '--version',
        choices=['claude-code'],
        default='claude-code',
        help='版本選擇 (目前僅支援 claude-code)'
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
        default=10,
        help='最大並行下載數 (預設: 10)'
    )
    
    args = parser.parse_args()
    
    # 獲取安裝路徑
    if args.path:
        install_path = Path(os.path.expanduser(args.path))
    else:
        # 互動模式
        print("Sunnycore 安裝程式")
        print("=" * 60)
        
        try:
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
            print("\n✗ 無法讀取用戶輸入，請使用 -p 參數指定安裝路徑")
            sys.exit(1)
    
    # 創建安裝器
    installer = SunnycoreInstaller(repo=args.repo, branch=args.branch, max_workers=args.max_workers)
    
    # 執行安裝
    try:
        if args.version == 'claude-code':
            success = installer.install_claude_code(install_path, auto_yes=args.yes)
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

