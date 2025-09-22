# 魯棒性測試層用戶文檔

## 概述

魯棒性測試層是一個自動化輸入變換測試系統，用於驗證系統對輸入變化的穩定性。通過對輸入文本進行語義中性的變換，確保關鍵結論在變換後保持一致性。

## 主要功能

### 1. 變換測試引擎
- **同義詞替換**: 自動替換文本中的詞語為同義詞，保持語義不變
- **段落重排序**: 重新排列文本段落順序，測試結論的穩定性
- **無關內容注入**: 在文本中注入無關內容，測試系統的過濾能力

### 2. 變換驗證系統
- **語義相似性驗證**: 確保變換後的文本保持原始語義
- **結構完整性檢查**: 驗證文本結構的完整性
- **關鍵結論保留**: 確保關鍵結論在變換後仍然存在

### 3. 穩定性分析
- **決策一致性分析**: 分析關鍵決策在不同變換下的一致性
- **結論穩定性評估**: 評估結論在輸入變化下的穩定性
- **信心區間計算**: 計算穩定性指標的統計信心區間

## 快速開始

### 基本使用

```python
from src.behavior.robustness_engine import RobustnessEngine, RobustnessTestConfig
from src.behavior.transformation_validator import TransformationValidator, ValidationConfig
from src.behavior.stability_analyzer import StabilityAnalyzer, StabilityAnalysisConfig
from src.behavior.report_generator import ReportGenerator, ReportConfig

# 1. 初始化魯棒性測試引擎
config = RobustnessTestConfig()
engine = RobustnessEngine(config)

# 2. 準備測試文本
test_text = """
This is a comprehensive test text for robustness testing.
It contains multiple paragraphs and important conclusions.
The system should maintain semantic integrity while applying transformations.
Therefore, we can conclude that the robustness testing is effective.
"""

# 3. 執行魯棒性測試
result = engine.execute_robustness_test("test_001", test_text)

# 4. 查看結果
print(f"Consistency Score: {result.consistency_score}")
print(f"Execution Time: {result.execution_time}s")
print(f"Number of Transformations: {len(result.transformation_results)}")
```

### 高級配置

```python
# 自定義配置
config = RobustnessTestConfig(
    target_consistency_score=0.9,  # 目標一致性分數
    max_processing_time=0.5,        # 最大處理時間（秒）
    enable_performance_tracking=True,  # 啟用性能追蹤
    transformation_config=TransformationConfig(
        random_seed=42,                     # 隨機種子
        max_synonym_replacements=10,        # 最大同義詞替換數
        synonym_confidence_threshold=0.8,   # 同義詞信心閾值
        preserve_key_terms=True             # 保留關鍵詞
    )
)

engine = RobustnessEngine(config)
```

## API 參考

### RobustnessEngine

#### 初始化
```python
RobustnessEngine(config: RobustnessTestConfig)
```

#### 主要方法
```python
# 執行魯棒性測試
execute_robustness_test(test_id: str, text: str) -> TestExecutionResult

# 獲取性能摘要
get_performance_summary() -> Dict[str, Any]

# 導出測試結果
export_test_results(file_path: str) -> bool

# 獲取引擎狀態
get_engine_status() -> Dict[str, Any]
```

#### 返回結果
```python
TestExecutionResult(
    test_id: str                    # 測試ID
    original_text: str              # 原始文本
    consistency_score: float        # 一致性分數 (0.0-1.0)
    execution_time: float           # 執行時間（秒）
    transformation_results: List[TransformationResult]  # 變換結果列表
    success_criteria_met: bool       # 是否達到成功標準
    performance_metrics: Dict[str, Any]  # 性能指標
)
```

### TransformationValidator

#### 初始化
```python
TransformationValidator(config: ValidationConfig)
```

#### 主要方法
```python
# 驗證變換結果
validate_transformation(
    original_text: str,
    transformed_text: str,
    transformation_result: TransformationResult
) -> Dict[str, ValidationResult]

# 生成驗證報告
generate_validation_report(
    validation_results: Dict[str, ValidationResult],
    original_text: str,
    transformed_text: str
) -> Dict[str, Any]
```

### StabilityAnalyzer

#### 初始化
```python
StabilityAnalyzer(config: StabilityAnalysisConfig)
```

#### 主要方法
```python
# 分析穩定性
analyze_stability(test_results: List[TestExecutionResult]) -> StabilityMetrics

# 生成穩定性報告
generate_stability_report(
    stability_metrics: StabilityMetrics,
    test_results: List[TestExecutionResult]
) -> Dict[str, Any]
```

### ReportGenerator

#### 初始化
```python
ReportGenerator(config: ReportConfig)
```

#### 主要方法
```python
# 生成綜合報告
generate_comprehensive_report(
    test_results: List[TestExecutionResult],
    validation_results: Dict[str, List[ValidationResult]],
    stability_metrics: StabilityMetrics
) -> Dict[str, Any]
```

## 配置選項

### RobustnessTestConfig
```python
@dataclass
class RobustnessTestConfig:
    target_consistency_score: float = 0.85
    max_processing_time: float = 0.5
    enable_performance_tracking: bool = True
    transformation_config: TransformationConfig = field(default_factory=TransformationConfig)
```

### ValidationConfig
```python
@dataclass
class ValidationConfig:
    semantic_similarity_threshold: float = 0.8
    key_conclusion_preservation_threshold: float = 0.9
    structural_integrity_threshold: float = 0.7
    overall_validation_threshold: float = 0.85
    enable_detailed_analysis: bool = True
    max_validation_time: float = 1.0
```

### StabilityAnalysisConfig
```python
@dataclass
class StabilityAnalysisConfig:
    min_stability_threshold: float = 0.85
    confidence_level: float = 0.95
    min_sample_size: int = 5
    enable_detailed_reporting: bool = True
```

## 最佳實踐

### 1. 測試文本選擇
- 使用包含關鍵結論的文本
- 確保文本長度足夠（建議至少200字符）
- 包含多個段落以測試結構穩定性

### 2. 配置優化
- 根據應用場景調整一致性閾值
- 設置合理的性能限制
- 使用固定的隨機種子以確保結果可重現

### 3. 結果解讀
- **一致性分數 > 0.9**: 優秀的穩定性
- **一致性分數 0.7-0.9**: 良好的穩定性
- **一致性分數 < 0.7**: 需要關注的穩定性問題

### 4. 性能優化
- 批量處理多個測試以提高效率
- 使用緩存機制存儲常用結果
- 監控處理時間並調整配置

## 故障排除

### 常見問題

#### 1. 測試結果一致性低
**可能原因**:
- 輸入文本過短
- 關鍵詞被替換
- 語義變換過大

**解決方案**:
- 增加輸入文本長度
- 啟用關鍵詞保護
- 調整變換參數

#### 2. 處理時間過長
**可能原因**:
- 文本過長
- 複雜的驗證邏輯
- 系統資源不足

**解決方案**:
- 設置最大處理時間
- 簡化驗證配置
- 優化系統資源

#### 3. 內存使用過高
**可能原因**:
- 批量處理大量文本
- 詳細分析開啟
- 緩存過多結果

**解決方案**:
- 分批處理文本
- 關閉詳細分析
- 定期清理緩存

### 調試模式

```python
import logging

# 啟用詳細日誌
logging.basicConfig(level=logging.DEBUG)

# 使用調試配置
config = RobustnessTestConfig(
    enable_performance_tracking=True,
    transformation_config=TransformationConfig(
        preserve_key_terms=True,
        max_synonym_replacements=5
    )
)
```

## 示例場景

### 1. API 文檔測試
```python
# 測試 API 文檔的魯棒性
api_docs = """
The getUser API retrieves user information by ID.
Parameters: id (required), fields (optional)
Returns: User object with id, name, email fields.
If user not found, returns 404 error.
"""

result = engine.execute_robustness_test("api_docs_test", api_docs)
print(f"API Documentation Consistency: {result.consistency_score}")
```

### 2. 產品描述測試
```python
# 測試產品描述的穩定性
product_desc = """
Our flagship product features advanced AI capabilities.
It processes data in real-time with 99.9% accuracy.
The system supports multiple languages and platforms.
Pricing starts at $99/month with volume discounts available.
"""

result = engine.execute_robustness_test("product_desc_test", product_desc)
print(f"Product Description Stability: {result.consistency_score}")
```

### 3. 批量測試
```python
# 批量測試多個文檔
test_documents = {
    "doc1": "Content of document 1...",
    "doc2": "Content of document 2...",
    "doc3": "Content of document 3..."
}

results = {}
for doc_id, content in test_documents.items():
    results[doc_id] = engine.execute_robustness_test(doc_id, content)

# 分析整體表現
avg_consistency = sum(r.consistency_score for r in results.values()) / len(results)
print(f"Average Consistency: {avg_consistency:.3f}")
```

## 性能指標

### 目標性能
- **處理時間**: < 500ms 每次測試
- **內存使用**: < 100MB
- **一致性分數**: > 0.85
- **測試覆蓋率**: > 85%

### 監控指標
- 平均處理時間
- 一致性分數分佈
- 變換成功率
- 系統資源使用率

## 擴展功能

### 自定義變換策略
```python
from src.behavior.transformation_strategies import BaseTransformationStrategy

class CustomTransformationStrategy(BaseTransformationStrategy):
    def transform(self, text: str) -> TransformationResult:
        # 實現自定義變換邏輯
        pass

    def is_applicable(self, text: str) -> bool:
        # 判斷是否適用於給定文本
        pass
```

### 自定義驗證器
```python
from src.behavior.transformation_validator import BaseValidator

class CustomValidator(BaseValidator):
    def validate(self, original_text: str, transformed_text: str) -> ValidationResult:
        # 實現自定義驗證邏輯
        pass
```

## 版本歷史

### v1.0.0 (2025-09-22)
- 初始版本發布
- 實現核心變換測試功能
- 支持三種基本變換策略
- 提供完整的驗證和分析功能

## 支持與反饋

如有問題或建議，請通過以下方式聯繫：
- 創建 GitHub Issue
- 發送郵件至開發團隊
- 參與社區討論

---

*此文檔隨系統更新而更新，最新版本請參考項目倉庫。*