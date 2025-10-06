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
from pathlib import Path
from typing import Dict, List, Optional


class SunnycoreInstaller:
    """Sunnycore 安裝器"""
    
    def __init__(self, repo: str = "Yamiyorunoshura/sunnycore", branch: str = "master"):
        self.repo = repo
        self.branch = branch
        self.base_raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}"
        self.base_api_url = f"https://api.github.com/repos/{repo}/contents"
        
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
            print(f"  下載: {file_path} → {target_path}")
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            with urllib.request.urlopen(url) as response:
                content = response.read()
                with open(target_path, 'wb') as f:
                    f.write(content)
            return True
        except Exception as e:
            print(f"  ✗ 下載失敗: {file_path} - {e}")
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
    
    def download_directory(self, source_dir: str, target_dir: Path) -> bool:
        """遞迴下載整個目錄
        
        Args:
            source_dir: GitHub 倉庫中的目錄路徑
            target_dir: 本地目標目錄
            
        Returns:
            bool: 下載是否成功
        """
        print(f"下載目錄: {source_dir}")
        contents = self.get_directory_contents(source_dir)
        
        if not contents:
            return False
        
        success = True
        for item in contents:
            if item['type'] == 'file':
                target_path = target_dir / item['name']
                if not self.download_file(item['path'], target_path):
                    success = False
            elif item['type'] == 'dir':
                sub_target_dir = target_dir / item['name']
                if not self.download_directory(item['path'], sub_target_dir):
                    success = False
        
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
                # 檢查是否可以進行互動
                if not sys.stdin.isatty():
                    print("\n✗ 目錄已存在，請使用 -y 參數自動確認覆寫，或手動刪除現有目錄")
                    return False
                response = input(f"\n目錄已存在，是否覆寫? (y/N): ").strip().lower()
                if response != 'y':
                    print("安裝已取消")
                    return False
        
        # 定義要下載的目錄和目標
        downloads = [
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
            ("claude code/CLAUDE.md", work_dir / "CLAUDE.md"),
        ]
        
        success = True
        
        # 下載目錄
        for source, target in downloads:
            if not self.download_directory(source, target):
                success = False
        
        # 下載單獨文件
        print("\n下載配置文件:")
        for source, target in single_files:
            if not self.download_file(source, target):
                success = False
        
        if success:
            print("\n" + "=" * 60)
            print("✓ 安裝完成!")
            print(f"\n安裝結構:")
            print(f"{work_dir}/")
            print(f"├── .claude/              # Claude 專用配置")
            print(f"│   ├── agents/          # Agent 定義")
            print(f"│   └── commands/        # 角色命令定義")
            print(f"├── sunnycore/           # Sunnycore 系統檔案")
            print(f"│   ├── config.yaml")
            print(f"│   ├── tasks/")
            print(f"│   ├── templates/")
            print(f"│   └── ...")
            print(f"└── CLAUDE.md            # Claude Code 專案指引")
            print("\n請查看 CLAUDE.md 開始使用 Sunnycore!")
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
  # 互動模式（終端執行）
  python3 install.py
  
  # 非互動模式（指定路徑和自動確認）
  python3 install.py -v claude-code -p ~/myproject -y
  
  # 從管道執行（自動使用預設路徑 ~/sunnycore）
  curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/install.py | python3
  
  # 從管道執行（指定路徑）
  curl -fsSL https://raw.githubusercontent.com/Yamiyorunoshura/sunnycore/master/scripts/install.py | python3 - -p ~/myproject -y
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
    
    args = parser.parse_args()
    
    # 獲取安裝路徑
    if args.path:
        install_path = Path(os.path.expanduser(args.path))
    else:
        # 互動模式
        print("Sunnycore 安裝程式")
        print("=" * 60)
        default_path = os.path.expanduser("~/sunnycore")
        
        # 檢查是否可以進行互動
        if not sys.stdin.isatty():
            print(f"\n✓ 使用預設安裝路徑: {default_path}")
            print("  (通過管道執行時自動使用預設值，或使用 -p 參數指定路徑)")
            install_path = Path(default_path)
        else:
            user_input = input(f"請輸入安裝路徑 (預設: {default_path}): ").strip()
            install_path = Path(os.path.expanduser(user_input) if user_input else default_path)
    
    # 創建安裝器
    installer = SunnycoreInstaller(repo=args.repo, branch=args.branch)
    
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

