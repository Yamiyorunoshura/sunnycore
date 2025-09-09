# Create Requirements CI/CD 環境配置指南

本文檔說明如何配置環境變數來自定義 create-requirements 任務的 CI/CD 測試行為。

## 環境變數概覽

系統支援通過 `.env` 文件配置以下環境變數：

### AI模型配置
```bash
# Anthropic Claude 配置
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_BASE_URL=https://api.anthropic.com  # 可選，覆寫預設URL
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022     # 可選，覆寫預設模型

# OpenAI 配置（備用）
OPENAI_API_KEY=your_openai_key_here
OPENAI_BASE_URL=https://api.openai.com/v1     # 可選
OPENAI_MODEL=gpt-4                            # 可選
```

### 測試行為配置
```bash
# 測試執行次數
TEST_RUNS=3                    # 預設：3次，dev環境：2次

# 一致性閾值（0.0-1.0）
CONSISTENCY_THRESHOLD=0.85     # 預設：0.85，dev環境：0.80

# 基本品質閾值（0-100）
QUALITY_THRESHOLD=85           # 預設：85，dev環境：75
```

### 品質門檻配置
```bash
# Agent一致性測試閾值（百分比）
AGENT_CONSISTENCY_THRESHOLD=90     # 預設：90%，dev環境：80%

# 文檔品質閾值（百分比）
DOC_QUALITY_THRESHOLD=85           # 預設：85%，dev環境：75%

# 工具使用準確率閾值（百分比）
TOOL_USAGE_THRESHOLD=95            # 預設：95%，dev環境：90%

# 模板合規性閾值（百分比）
TEMPLATE_COMPLIANCE_THRESHOLD=100  # 固定：100%

# 整體成功率閾值（百分比）
OVERALL_SUCCESS_THRESHOLD=90       # 預設：90%，dev環境：85%
```

## 環境特定配置

### 開發環境 (.env.dev)
```bash
NODE_ENV=development
ANTHROPIC_API_KEY=your_dev_api_key

# 較寬鬆的測試設定
TEST_RUNS=2
CONSISTENCY_THRESHOLD=0.80
QUALITY_THRESHOLD=75

# 較低的品質門檻
AGENT_CONSISTENCY_THRESHOLD=80
DOC_QUALITY_THRESHOLD=75
TOOL_USAGE_THRESHOLD=90
OVERALL_SUCCESS_THRESHOLD=85
```

### 測試環境 (.env.test)
```bash
NODE_ENV=test
ANTHROPIC_API_KEY=your_test_api_key

# 標準測試設定
TEST_RUNS=3
CONSISTENCY_THRESHOLD=0.85
QUALITY_THRESHOLD=85

# 標準品質門檻
AGENT_CONSISTENCY_THRESHOLD=90
DOC_QUALITY_THRESHOLD=85
TOOL_USAGE_THRESHOLD=95
OVERALL_SUCCESS_THRESHOLD=90
```

### 生產環境 (.env.prod)
```bash
NODE_ENV=production
ANTHROPIC_API_KEY=your_prod_api_key

# 嚴格的測試設定
TEST_RUNS=5
CONSISTENCY_THRESHOLD=0.90
QUALITY_THRESHOLD=90

# 高品質門檻
AGENT_CONSISTENCY_THRESHOLD=95
DOC_QUALITY_THRESHOLD=90
TOOL_USAGE_THRESHOLD=98
OVERALL_SUCCESS_THRESHOLD=95
```

## 配置文件載入順序

系統按以下順序載入配置文件：

1. `.env` - 基礎配置
2. `.env.local` - 本地覆寫配置（不應提交到git）
3. `.env.{NODE_ENV}` - 環境特定配置
4. `.env.{NODE_ENV}.local` - 環境特定本地配置
5. 系統環境變數 - 最高優先級

## GitHub Actions 環境變數設定

在 GitHub Repository 的 Settings > Secrets and variables > Actions 中設定：

### Repository Secrets
```
ANTHROPIC_API_KEY - Anthropic Claude API 密鑰
OPENAI_API_KEY - OpenAI API 密鑰（可選）
```

### Repository Variables （可選覆寫）
```
ANTHROPIC_BASE_URL - 自定義 Anthropic API 端點
ANTHROPIC_MODEL - 自定義 Claude 模型版本
CONSISTENCY_THRESHOLD - 自定義一致性閾值
QUALITY_THRESHOLD - 自定義品質閾值
```

## 本地開發配置

### 1. 建立 .env 文件
```bash
# 複製範本
cp .env.example .env

# 編輯配置
nano .env
```

### 2. 基本配置範例
```bash
# .env
ANTHROPIC_API_KEY=sk-ant-api03-...
NODE_ENV=development

# 可選：降低測試要求以節省費用
TEST_RUNS=2
AGENT_CONSISTENCY_THRESHOLD=75
DOC_QUALITY_THRESHOLD=70
```

### 3. 驗證配置
```bash
# 測試環境載入
npm run test:config

# 或直接執行測試
npm test
```

## 高級配置選項

### 自定義測試範圍
```bash
# 只執行特定類型的測試
SKIP_AGENT_TESTS=false
SKIP_DOC_TESTS=false
SKIP_TOOL_TESTS=false
SKIP_QUALITY_TESTS=false
```

### 調試和日誌
```bash
# 啟用詳細日誌
VERBOSE_LOGGING=true
DEBUG_MODE=true

# 保存中間測試結果
SAVE_INTERMEDIATE_RESULTS=true
```

### 性能調優
```bash
# 並行測試執行
PARALLEL_TESTS=true
MAX_PARALLEL_JOBS=3

# 測試超時設定（秒）
TEST_TIMEOUT=30
QUALITY_CHECK_TIMEOUT=60
```

## 故障排除

### 常見問題

1. **API配額限制**
   ```bash
   # 降低測試頻率
   TEST_RUNS=1
   CONSISTENCY_THRESHOLD=0.70
   ```

2. **測試超時**
   ```bash
   # 增加超時時間
   TEST_TIMEOUT=60
   QUALITY_CHECK_TIMEOUT=120
   ```

3. **品質門檻過高**
   ```bash
   # 調整閾值
   AGENT_CONSISTENCY_THRESHOLD=75
   DOC_QUALITY_THRESHOLD=70
   ```

### 配置驗證

檢查配置載入是否正確：

```bash
# 顯示當前配置
npm run show-config

# 驗證 API 連接
npm run test-connection

# 執行配置檢查
npm run validate-config
```

## 最佳實踐

1. **安全性**
   - 永不將 API 密鑰提交到版本控制
   - 使用 `.env.local` 進行本地覆寫
   - 定期輪換 API 密鑰

2. **效能優化**
   - 開發時使用較低的測試次數
   - 生產環境使用更嚴格的閾值
   - 適當設定並行度避免API限制

3. **版本控制**
   - 提交 `.env.example` 作為範本
   - 將實際的 `.env` 文件加入 `.gitignore`
   - 在 README 中說明必要的環境變數

4. **團隊協作**
   - 建立統一的環境配置標準
   - 文檔化所有環境變數
   - 提供快速設定腳本

---

## 配置範本文件

### .env.example
```bash
# AI 模型配置
ANTHROPIC_API_KEY=your_anthropic_api_key_here
# ANTHROPIC_BASE_URL=https://api.anthropic.com
# ANTHROPIC_MODEL=claude-3-5-sonnet-20241022

# 測試配置
# TEST_RUNS=3
# CONSISTENCY_THRESHOLD=0.85
# QUALITY_THRESHOLD=85

# 品質門檻配置
# AGENT_CONSISTENCY_THRESHOLD=90
# DOC_QUALITY_THRESHOLD=85
# TOOL_USAGE_THRESHOLD=95
# TEMPLATE_COMPLIANCE_THRESHOLD=100
# OVERALL_SUCCESS_THRESHOLD=90
```

複製此文件為 `.env` 並填入您的實際配置。
