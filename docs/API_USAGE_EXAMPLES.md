# API 使用示例

## 概述

本文檔提供了 Multi-Stage Testing Framework 主要 API 的使用示例和最佳實踐。

## Golden Set Manager 使用示例

### 基本使用

```python
from src.behavior.golden_set_manager import GoldenSetManager

# 初始化 Golden Set Manager
manager = GoldenSetManager("golden_set.json")

# 添加測試案例
test_case = {
    "id": "test_001",
    "description": "基礎功能測試",
    "input": "測試輸入數據",
    "expected_output": "預期輸出結果",
    "category": "unit_test"
}
manager.add_test_case(test_case)

# 獲取測試案例
retrieved_case = manager.get_test_case("test_001")
print(f"檢索到的測試案例: {retrieved_case['description']}")

# 執行驗證
validation_result = manager.validate_against_golden_set(test_input_data)
print(f"驗證結果: {validation_result.is_valid}")
```

### 版本控制

```python
# 創建新版本
manager.create_version("v1.1.0", "新增測試案例")

# 切換到特定版本
manager.switch_to_version("v1.0.0")

# 獲取版本歷史
history = manager.get_version_history()
for version in history:
    print(f"版本 {version['version']}: {version['description']}")
```

## Promptfoo 集成使用示例

### 基本配置

```python
from src.behavior.promptfoo_integration import PromptfooIntegration

# 初始化 Promptfoo 集成
integration = PromptfooIntegration(
    config_path="promptfooconfig.yaml",
    workspace_dir="./promptfoo_workspace"
)

# 添加測試案例
test_case = {
    "description": "LLM 響應質量測試",
    "vars": {
        "input": "測試輸入提示",
        "expected_output": "預期輸出類型"
    },
    "assert": [
        {
            "type": "contains",
            "value": "預期關鍵詞"
        }
    ]
}
integration.add_test_case(test_case)

# 執行 A/B 測試
result = integration.run_ab_test(
    prompts=["提示詞 A", "提示詞 B"],
    test_cases=[test_case]
)
print(f"A/B 測試結果: {result}")
```

### 評估指標

```python
from src.behavior.metrics_calculator import MetricsCalculator

# 計算質量指標
calculator = MetricsCalculator()
metrics = calculator.calculate_quality_metrics(test_results)

print(f"準確率: {metrics['accuracy']}")
print(f"召回率: {metrics['recall']}")
print(f"F1 分數: {metrics['f1_score']}")
```

## DeepEval 集成使用示例

### 架構驗證

```python
from src.behavior.deepeval_integration import DeepEvalIntegration
from src.behavior.architecture_validator import ArchitectureValidator

# 初始化 DeepEval 集成
deepeval = DeepEvalIntegration()

# 執行架構對齊驗證
validator = ArchitectureValidator()
alignment_result = validator.validate_architecture_alignment(
    implemented_components=components,
    requirements_spec=requirements
)

print(f"架構對齊 F1 分數: {alignment_result.f1_score}")
print(f"通過的組件數量: {alignment_result.passed_components}")
```

### 測試斷言

```python
# 使用 DeepEval 進行測試斷言
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

# 創建測試案例
test_case = LLMTestCase(
    input="什麼是機器學習？",
    actual_output="機器學習是人工智能的一個分支...",
    expected_output="應該包含監督學習、無監督學習等概念"
)

# 定義評估指標
metric = AnswerRelevancyMetric(
    threshold=0.7,
    model="gpt-4"
)

# 執行評估
metric.measure(test_case)
print(f"相關性分數: {metric.score}")
print(f"通過評估: {metric.is_successful()}")
```

## 完整工作流程示例

### 端到端測試流程

```python
import asyncio
from src.behavior.golden_set_manager import GoldenSetManager
from src.behavior.promptfoo_integration import PromptfooIntegration
from src.behavior.deepeval_integration import DeepEvalIntegration

async def complete_behavioral_test_workflow():
    # 1. 初始化所有組件
    golden_manager = GoldenSetManager("test_golden_set.json")
    promptfoo = PromptfooIntegration()
    deepeval = DeepEvalIntegration()

    # 2. 從 Golden Set 加載測試案例
    test_cases = golden_manager.get_all_test_cases()

    # 3. 使用 Promptfoo 執行 A/B 測試
    ab_test_results = []
    for case in test_cases:
        result = promptfoo.run_ab_test(
            prompts=[case["prompt_a"], case["prompt_b"]],
            test_cases=[case]
        )
        ab_test_results.append(result)

    # 4. 使用 DeepEval 進行質量評估
    quality_results = []
    for result in ab_test_results:
        quality_metric = deepeval.evaluate_quality(
            input=result["input"],
            output=result["output"],
            expected_output=result["expected"]
        )
        quality_results.append(quality_metric)

    # 5. 生成綜合報告
    final_report = {
        "test_cases_count": len(test_cases),
        "ab_test_results": ab_test_results,
        "quality_metrics": quality_results,
        "overall_pass_rate": sum(1 for q in quality_results if q["pass"]) / len(quality_results)
    }

    return final_report

# 執行工作流程
report = asyncio.run(complete_behavioral_test_workflow())
print(f"整體通過率: {report['overall_pass_rate']:.2%}")
```

## 錯誤處理示例

### 基本錯誤處理

```python
from src.behavior.golden_set_manager import GoldenSetManager
import logging

# 配置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # 初始化管理器
    manager = GoldenSetManager("golden_set.json")

    # 嘗試添加測試案例
    test_case = {
        "id": "test_001",
        "description": "測試案例",
        "input": "輸入數據",
        "expected_output": "預期輸出"
    }

    success = manager.add_test_case(test_case)
    if success:
        logger.info("測試案例添加成功")
    else:
        logger.error("測試案例添加失敗")

except FileNotFoundError as e:
    logger.error(f"文件未找到: {e}")
except Exception as e:
    logger.error(f"未預期的錯誤: {e}")
```

### 依賴檢查

```python
def check_dependencies():
    """檢查所有必要的依賴是否已安裝"""
    dependencies = {
        "yaml": "PyYAML",
        "jsonschema": "jsonschema",
        "deepeval": "DeepEval",
        "ragas": "RAGAS"
    }

    missing_deps = []
    for module, name in dependencies.items():
        try:
            __import__(module)
            print(f"✓ {name} 已安裝")
        except ImportError:
            missing_deps.append(name)
            print(f"✗ {name} 缺失")

    if missing_deps:
        print(f"請安裝缺失的依賴: {', '.join(missing_deps)}")
        return False
    return True

# 檢查依賴
if check_dependencies():
    print("所有依賴都已正確安裝")
else:
    print("請先安裝缺失的依賴")
```

## 性能優化建議

### 批量處理

```python
# 使用批量處理提高性能
def batch_process_test_cases(manager, test_cases, batch_size=10):
    """批量處理測試案例以提高性能"""
    results = []

    for i in range(0, len(test_cases), batch_size):
        batch = test_cases[i:i + batch_size]

        # 批量添加測試案例
        for case in batch:
            manager.add_test_case(case)

        # 批量驗證
        batch_results = manager.validate_batch(batch)
        results.extend(batch_results)

        print(f"已處理 {min(i + batch_size, len(test_cases))}/{len(test_cases)} 個測試案例")

    return results
```

### 快取機制

```python
from functools import lru_cache

class CachedGoldenSetManager(GoldenSetManager):
    """帶快取的 Golden Set 管理器"""

    @lru_cache(maxsize=100)
    def get_test_case_cached(self, test_id: str):
        """帶快取的測試案例獲取"""
        return self.get_test_case(test_id)

    @lru_cache(maxsize=50)
    def validate_against_golden_set_cached(self, input_hash: str):
        """帶快取的驗證"""
        return self.validate_against_golden_set(input_hash)
```

---

## 總結

本文檔提供了 Multi-Stage Testing Framework 的主要 API 使用示例。關鍵要點：

1. **正確初始化**: 確保在使用任何 API 前正確初始化相關組件
2. **錯誤處理**: 始終包含適當的錯誤處理機制
3. **依賴管理**: 使用前檢查所有必要的依賴是否已安裝
4. **性能優化**: 對於大量數據，考慮使用批量處理和快取
5. **日誌記錄**: 使用日誌來追蹤 API 使用情況和調試問題

如需更多詳細信息，請參考各個模組的源代碼文檔。