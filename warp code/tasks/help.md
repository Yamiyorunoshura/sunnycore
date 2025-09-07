輸入：
1. agents/dev.m
2. agents/pm.md
3. agents/po.md
4. agents/qa.md

輸出
1. agents文件中的自定義指令以及其簡介

步驟1: 識別用戶呼叫的agent
- 識別用戶呼叫的agent
- 讀取agents文件中的自定義指令以及其簡介
- 若用戶呼叫dev agent，則讀取dev.md
- 若用戶呼叫pm agent，則讀取pm.md
- 若用戶呼叫po agent，則讀取po.md
- 若用戶呼叫qa agent，則讀取qa.md
- 若用戶呼叫的agent不存在，則向用戶提示不存在該agent