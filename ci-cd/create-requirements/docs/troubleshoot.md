# Create Requirements CI/CD 故障排除指南

本文檔收錄在使用 Create Requirements CI/CD 管道時可能遇到的常見問題及其解決方案。

## 🚨 常見錯誤分類

### 1. 環境配置錯誤

#### 問題：API Key 未配置或無效
```
Error: ANTHROPIC_API_KEY is not set or invalid
```

**原因**：
- 環境變數未設定或設定錯誤
- API Key 已過期或無效
- API Key 權限不足

**解決方案**：
```bash
# 1. 檢查環境變數
echo $ANTHROPIC_API_KEY

# 2. 重新設定 API Key
export ANTHROPIC_API_KEY="your_valid_api_key_here"

# 3. 驗證 API Key 有效性
curl -H "x-api-key: $ANTHROPIC_API_KEY" https://api.anthropic.com/v1/messages
```

#### 問題：Node.js 版本不相容
```
Error: Unsupported Node.js version. Required: >=18.0.0
```

**解決方案**：
```bash
# 檢查當前 Node.js 版本
node --version

# 使用 nvm 切換到支援的版本
nvm install 18
nvm use 18

# 或使用 n 版本管理器
npm install -g n
n 18
```

#### 問題：依賴安裝失敗
```
Error: Cannot resolve dependency '@promptfoo/cli'
```

**解決方案**：
```bash
# 清理快取並重新安裝
npm cache clean --force
rm -rf node_modules package-lock.json
npm install

# 或使用 yarn
yarn cache clean
rm -rf node_modules yarn.lock
yarn install
```

### 2. 測試執行錯誤

#### 問題：Promptfoo 配置錯誤
```
Error: Invalid promptfoo configuration
```

**解決方案**：
```bash
# 1. 驗證配置檔案語法
node -c promptfoo.config.js

# 2. 檢查測試檔案是否存在
ls -la tests/

# 3. 手動驗證 YAML 語法
npx js-yaml tests/agent-consistency.yml

# 4. 檢查 prompt 模板檔案
ls -la prompts/
```

#### 問題：測試超時
```
Error: Test timeout after 30000ms
```

**原因**：
- API 回應緩慢
- 網路連接問題
- 測試案例過於複雜

**解決方案**：
```bash
# 1. 增加超時時間
export TEST_TIMEOUT=60

# 2. 減少測試執行次數
export TEST_RUNS=2

# 3. 檢查網路連接
curl -I https://api.anthropic.com

# 4. 使用較簡單的測試案例進行調試
```

#### 問題：API 配額限制
```
Error: 429 Too Many Requests
```

**解決方案**：
```bash
# 1. 降低測試頻率
export TEST_RUNS=1
export RATE_LIMIT_DELAY=2000

# 2. 使用較低的閾值進行開發測試
export AGENT_CONSISTENCY_THRESHOLD=75
export DOC_QUALITY_THRESHOLD=70

# 3. 檢查 API 使用配額
# 登入 Anthropic Console 查看用量
```

### 3. 品質門檻檢查失敗

#### 問題：Agent 一致性測試失敗
```
❌ Agent一致性 75.2% (閾值: 90%)
```

**原因分析**：
- AI 模型輸出隨機性過高
- 測試案例設計不當
- Prompt 模板不夠具體

**解決方案**：
```bash
# 1. 調整模型參數
export ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
# 在 promptfoo.config.js 中設定較低的 temperature

# 2. 增加測試執行次數以獲得更穩定的統計
export TEST_RUNS=5

# 3. 臨時降低閾值進行調試
export AGENT_CONSISTENCY_THRESHOLD=75

# 4. 檢查具體失敗的測試案例
npm run test:agent-consistency -- --verbose
```

#### 問題：文檔品質測試失敗
```
❌ 文檔品質 70.5% (閾值: 85%)
```

**常見原因與解決**：

1. **YAML 格式錯誤**
```bash
# 檢查 YAML 語法
npx js-yaml examples/sample.yaml

# 使用線上 YAML 驗證器
# https://yamlvalidator.com/
```

2. **必要字段缺失**
```bash
# 檢查模板字段完整性
node -e "
const yaml = require('js-yaml');
const fs = require('fs');
const content = fs.readFileSync('test-results/sample-output.yaml');
const parsed = yaml.load(content);
console.log('Missing fields:', Object.keys(parsed).filter(key => !parsed[key]));
"
```

3. **ID 格式不規範**
```bash
# 檢查需求 ID 格式
grep -E "F-[0-9]{3}|NFR-[A-Z]-[0-9]{3}" test-results/sample-output.yaml
```

#### 問題：工具使用測試失敗
```
❌ 工具使用 85.0% (閾值: 95%)
```

**解決方案**：
1. **檢查 Prompt 模板**
```bash
# 確保 Prompt 中明確要求使用工具
grep -i "sequential-thinking\|todo-list" prompts/*.md
```

2. **調整評估標準**
```javascript
// 在 promptfoo.config.js 中調整工具檢測邏輯
customGraders: {
  'tool-usage-check': (output, expected) => {
    const hasSequential = output.toLowerCase().includes('sequential-thinking');
    const hasTodo = output.toLowerCase().includes('todo-list');
    // 調整評分邏輯...
  }
}
```

### 4. GitHub Actions 錯誤

#### 問題：Workflow 觸發失敗
```
Error: Workflow not triggered on push
```

**解決方案**：
```yaml
# 檢查 .github/workflows/create-requirements-ci.yml 觸發條件
on:
  push:
    branches: [ main, develop ]
    paths:
      - 'general/tasks/create-requirements.md'
      - 'ci-cd/create-requirements/**'
```

#### 問題：環境變數未傳遞
```
Error: Environment variable not found in GitHub Actions
```

**解決方案**：
1. **檢查 Repository Secrets**
```
GitHub Repository → Settings → Secrets and variables → Actions
確認已添加：
- ANTHROPIC_API_KEY
```

2. **檢查 Workflow 配置**
```yaml
env:
  ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

#### 問題：Artifact 上傳失敗
```
Error: No files were found with the provided path
```

**解決方案**：
```yaml
# 確保路徑正確且文件存在
- name: 上傳測試結果
  uses: actions/upload-artifact@v4
  if: always()
  with:
    name: test-results
    path: |
      ci-cd/create-requirements/test-results/
      !ci-cd/create-requirements/test-results/*.tmp
```

### 5. 本地開發環境問題

#### 問題：權限錯誤
```
Error: EACCES permission denied
```

**解決方案**：
```bash
# 修正腳本權限
chmod +x scripts/*.js
chmod +x scripts/*.mjs

# 使用 npm/yarn 執行而非直接執行
npm run quality-gate
```

#### 問題：路徑問題
```
Error: Module not found
```

**解決方案**：
```bash
# 檢查當前工作目錄
pwd

# 確保在正確目錄執行
cd ci-cd/create-requirements

# 檢查相對路徑是否正確
ls -la scripts/
ls -la tests/
```

## 🔧 調試工具和技巧

### 1. 詳細日誌模式

```bash
# 啟用詳細日誌
DEBUG=true npm test
VERBOSE=true npm run quality-gate

# Promptfoo 詳細模式
npx promptfoo eval --verbose --no-cache
```

### 2. 分步調試

```bash
# 只執行特定測試套件
npm run test:agent-consistency
npm run test:doc-quality

# 使用單一測試案例
npx promptfoo eval -c tests/agent-consistency.yml --filter "*簡單*"

# 保存中間結果
SAVE_INTERMEDIATE_RESULTS=true npm test
```

### 3. 配置驗證

```bash
# 檢查環境變數
npm run show-config

# 驗證 API 連接
npm run test-connection

# 驗證配置檔案
npm run validate-config
```

### 4. 手動測試

```bash
# 手動執行品質門檻檢查
node scripts/quality-gate.js

# 手動執行文檔驗證
node scripts/validate-doc-generation.mjs

# 測試特定 prompt
echo "測試輸入" | npx promptfoo eval -c promptfoo.config.js
```

## 📋 故障排除檢查清單

### 環境檢查
- [ ] Node.js 版本 >= 18.0.0
- [ ] npm/yarn 已安裝依賴
- [ ] API Key 已設定且有效
- [ ] 環境變數正確載入

### 配置檢查
- [ ] promptfoo.config.js 語法正確
- [ ] 測試 YAML 檔案格式有效
- [ ] Prompt 模板檔案存在
- [ ] 路徑配置正確

### 測試檢查
- [ ] 網路連接正常
- [ ] API 配額足夠
- [ ] 測試超時設定合理
- [ ] 品質閾值設定合理

### CI/CD 檢查
- [ ] GitHub Secrets 已設定
- [ ] Workflow 觸發條件正確
- [ ] Artifact 路徑配置正確
- [ ] 環境變數傳遞正確

## 🆘 獲取幫助

### 1. 查看日誌
```bash
# 查看最近的測試結果
cat test-results/latest.json | jq .

# 查看品質報告
cat test-results/quality-report.md
```

### 2. 重置環境
```bash
# 完全重置本地環境
rm -rf node_modules package-lock.json
rm -rf test-results/
npm install
```

### 3. 聯繫支援
如果問題持續存在，請提供以下資訊：

- 錯誤訊息的完整輸出
- 環境資訊 (`node --version`, `npm --version`)
- 相關配置檔案內容
- 測試結果和日誌檔案

## 📈 效能優化建議

### 1. 減少 API 調用
```bash
# 開發時使用較少的測試執行次數
export TEST_RUNS=2

# 使用快取避免重複請求
npx promptfoo eval --cache
```

### 2. 並行測試
```bash
# 啟用並行測試（小心 API 限制）
export PARALLEL_TESTS=true
export MAX_PARALLEL_JOBS=2
```

### 3. 選擇性測試
```bash
# 只執行變更相關的測試
export SKIP_AGENT_TESTS=false
export SKIP_DOC_TESTS=true
export SKIP_TOOL_TESTS=true
export SKIP_QUALITY_TESTS=true
```

---

**記住**：大多數問題都與配置錯誤或環境設定有關。系統性地檢查配置和環境通常能解決 80% 的問題。

如果您發現新的問題和解決方案，請更新此文檔以幫助其他開發者。
