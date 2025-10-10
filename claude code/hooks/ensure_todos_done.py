#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stop hook: 若 transcript 裡的 Todo 還沒清空，就 block 停止並要求繼續。
需求依據：
- Stop hook 可回傳 JSON：{"decision": "block", "reason": "..."} 來阻擋停止。  # docs
- hook 透過 stdin 給出 {"transcript_path": "...", "stop_hook_active": bool}。       # docs
"""

import json, os, sys, re
from pathlib import Path

def emit_block(reason: str):
    # Stop/SubagentStop 的控制介面需要 decision=block 並提供 reason。 # docs
    print(json.dumps({"decision": "block", "reason": reason}, ensure_ascii=False))
    sys.exit(0)

def load_jsonl(path: Path):
    try:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line=line.strip()
                if not line: 
                    continue
                try:
                    yield json.loads(line)
                except Exception:
                    continue
    except FileNotFoundError:
        return

def find_latest_todowrite(transcript_path: Path):
    latest = None
    for obj in load_jsonl(transcript_path):
        # 兼容不同訊息風格：stream-json 會有 message 物件，content 可能含 tool_use 區段。 # headless docs
        # 嘗試在多種欄位位置尋找 TodoWrite 的輸入。
        # 1) 直接在內容陣列找 tool_use
        msg = obj.get("message") or obj
        content = msg.get("content") if isinstance(msg, dict) else None
        if isinstance(content, list):
            for c in content:
                # 兩種常見鍵名："tool_use".name 或 "tool_name"
                if (c.get("type") == "tool_use" and c.get("name") == "TodoWrite") or \
                   (c.get("tool_name") == "TodoWrite"):
                    latest = c
        # 2) 有些轉錄器會把工具呼叫拍扁到頂層
        if obj.get("tool_name") == "TodoWrite" or obj.get("name") == "TodoWrite":
            latest = obj
    return latest

def extract_todos(tool_call_obj):
    # 依不同實作，todos 可能在 input/todos、parameters/todos 或 args/todos
    for key1 in ("input","parameters","args","tool_input"):
        payload = tool_call_obj.get(key1) or {}
        if isinstance(payload, str):
            try:
                payload = json.loads(payload)
            except Exception:
                continue
        for key2 in ("todos","todo","items"):
            todos = payload.get(key2)
            if isinstance(todos, list):
                return todos
            # 有時候模型把 JSON 當字串塞進去，嘗試 parse
            if isinstance(todos, str):
                try:
                    val = json.loads(todos)
                    if isinstance(val, list):
                        return val
                except Exception:
                    pass
    return []

def has_unfinished(todos):
    # 常見三態：pending / in_progress / completed
    # 外部參考對這三個狀態有說明。 # community explainer
    unfinished = []
    for t in todos:
        status = (t.get("status") or t.get("state") or "").lower()
        # todo_write 工具使用 "content" 作為主要欄位名
        title  = t.get("content") or t.get("title") or t.get("task") or t.get("text") or ""
        if status in ("pending","in_progress","in progress","todo","doing","started",""):
            unfinished.append(title.strip() or "(未命名待辦項目)")
    return unfinished

def main():
    try:
        hook_input = json.load(sys.stdin)
    except Exception:
        # 無法解析就不擋，避免卡死
        sys.exit(0)

    transcript_path = hook_input.get("transcript_path")
    stop_hook_active = bool(hook_input.get("stop_hook_active"))
    project_dir = Path(os.environ.get("CLAUDE_PROJECT_DIR","."))

    # 防自鎖：如果已經因 stop hook 繼續過一次，就最多再擋一定次數
    retry_file = project_dir/".claude/state/stop_retry_count"
    retry_file.parent.mkdir(parents=True, exist_ok=True)
    try:
        n = int(retry_file.read_text().strip())
    except Exception:
        n = 0

    MAX_RETRIES = 3
    if n >= MAX_RETRIES:
        # 達到最大重試次數，清空計數並放行
        try: retry_file.unlink()
        except Exception: pass
        sys.exit(0)

    todos = []
    if transcript_path:
        latest = find_latest_todowrite(Path(transcript_path))
        if latest:
            todos = extract_todos(latest)

    unfinished = has_unfinished(todos)
    if unfinished:
        # 只在 stop_hook_active 時才累加重試計數
        if stop_hook_active:
            retry_file.write_text(str(n+1))
        reason = (
            "待辦項目：\n- "
            + "\n- ".join(unfinished[:10])
            + ("\n…(其餘略)" if len(unfinished) > 10 else "")
            + "\n\n請繼續完成。"
        )
        emit_block(reason)
    else:
        # 都完成了，清掉計數並放行
        try: retry_file.unlink()
        except Exception: pass
        sys.exit(0)

if __name__ == "__main__":
    main()