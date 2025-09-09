#!/usr/bin/env node
/**
 * Create Requirements Task 品質門檻檢查腳本
 * 
 * 此腳本分析promptfoo測試結果，與設定的品質閾值進行比較，
 * 決定CI/CD管道是否可以繼續進行部署。
 */

const fs = require('fs');
const path = require('path');

// 載入環境配置
require('dotenv').config();

// 預設品質閾值
const DEFAULT_THRESHOLDS = {
  agent_consistency: 90,        // Agent一致性測試通過率 (%)
  doc_quality: 85,             // 文檔品質分數 (%)
  tool_usage: 95,              // 工具使用準確率 (%)
  template_compliance: 100,     // 模板合規性 (%)
  overall_success_rate: 90     // 整體成功率 (%)
};

// 從環境變數讀取自定義閾值
const THRESHOLDS = {
  agent_consistency: parseFloat(process.env.AGENT_CONSISTENCY_THRESHOLD) || DEFAULT_THRESHOLDS.agent_consistency,
  doc_quality: parseFloat(process.env.DOC_QUALITY_THRESHOLD) || DEFAULT_THRESHOLDS.doc_quality,
  tool_usage: parseFloat(process.env.TOOL_USAGE_THRESHOLD) || DEFAULT_THRESHOLDS.tool_usage,
  template_compliance: parseFloat(process.env.TEMPLATE_COMPLIANCE_THRESHOLD) || DEFAULT_THRESHOLDS.template_compliance,
  overall_success_rate: parseFloat(process.env.OVERALL_SUCCESS_THRESHOLD) || DEFAULT_THRESHOLDS.overall_success_rate
};

/**
 * 讀取promptfoo測試結果
 */
function readTestResults() {
  const resultsPath = path.resolve(__dirname, '../test-results/latest.json');
  
  if (!fs.existsSync(resultsPath)) {
    console.error(`❌ 測試結果文件不存在: ${resultsPath}`);
    process.exit(1);
  }
  
  try {
    const rawData = fs.readFileSync(resultsPath, 'utf-8');
    return JSON.parse(rawData);
  } catch (error) {
    console.error(`❌ 無法解析測試結果文件: ${error.message}`);
    process.exit(1);
  }
}

/**
 * 分類和分析測試結果
 */
function analyzeTestResults(testResults) {
  const categories = {
    agent_consistency: [],
    doc_quality: [],
    tool_usage: [],
    template_compliance: []
  };
  
  // 整體統計
  const stats = testResults.results.stats;
  const overallSuccessRate = (stats.successes / (stats.successes + stats.failures)) * 100;
  
  // 分析每個測試案例
  testResults.results.results.forEach(result => {
    const testDescription = result.testCase.description || '';
    const score = result.pass ? 100 : 0;
    
    // 根據測試描述分類
    if (testDescription.includes('一致性') || testDescription.includes('consistency')) {
      categories.agent_consistency.push({
        score: score,
        description: testDescription,
        details: result
      });
    } else if (testDescription.includes('品質') || testDescription.includes('quality') || 
               testDescription.includes('完整性') || testDescription.includes('格式')) {
      categories.doc_quality.push({
        score: score,
        description: testDescription,
        details: result
      });
    } else if (testDescription.includes('Tool') || testDescription.includes('工具')) {
      categories.tool_usage.push({
        score: score,
        description: testDescription,
        details: result
      });
    } else if (testDescription.includes('template') || testDescription.includes('模板') || 
               testDescription.includes('Template')) {
      categories.template_compliance.push({
        score: score,
        description: testDescription,
        details: result
      });
    }
  });
  
  // 計算各類別平均分數
  const calculateAverage = (categoryResults) => {
    if (categoryResults.length === 0) return 0;
    const sum = categoryResults.reduce((acc, result) => acc + result.score, 0);
    return sum / categoryResults.length;
  };
  
  const categoryScores = {
    agent_consistency: calculateAverage(categories.agent_consistency),
    doc_quality: calculateAverage(categories.doc_quality),
    tool_usage: calculateAverage(categories.tool_usage),
    template_compliance: calculateAverage(categories.template_compliance),
    overall_success_rate: overallSuccessRate
  };
  
  return {
    categoryScores,
    categories,
    totalTests: stats.successes + stats.failures,
    passedTests: stats.successes,
    failedTests: stats.failures
  };
}

/**
 * 檢查是否通過品質門檻
 */
function checkQualityGate(analysisResult) {
  const { categoryScores } = analysisResult;
  const results = {};
  let overallPassed = true;
  
  // 檢查每個類別
  Object.keys(THRESHOLDS).forEach(category => {
    const score = categoryScores[category] || 0;
    const threshold = THRESHOLDS[category];
    const passed = score >= threshold;
    
    results[category] = {
      score: score,
      threshold: threshold,
      passed: passed,
      difference: score - threshold
    };
    
    if (!passed) {
      overallPassed = false;
    }
  });
  
  return {
    overallPassed,
    categoryResults: results
  };
}

/**
 * 生成詳細報告
 */
function generateReport(analysisResult, qualityGateResult) {
  const { categoryScores, categories, totalTests, passedTests, failedTests } = analysisResult;
  const { overallPassed, categoryResults } = qualityGateResult;
  
  const report = {
    summary: {
      passed: overallPassed,
      timestamp: new Date().toISOString(),
      totalTests: totalTests,
      passedTests: passedTests,
      failedTests: failedTests,
      successRate: (passedTests / totalTests) * 100
    },
    qualityMetrics: categoryResults,
    detailedResults: categories,
    thresholds: THRESHOLDS
  };
  
  // 儲存詳細報告
  const reportPath = path.resolve(__dirname, '../test-results/quality-report.json');
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
  
  return report;
}

/**
 * 生成Markdown報告
 */
function generateMarkdownReport(report) {
  const { summary, qualityMetrics } = report;
  
  let markdown = `# Create Requirements Task 品質報告\n\n`;
  markdown += `**生成時間**: ${new Date(summary.timestamp).toLocaleString('zh-TW')}\n\n`;
  
  // 整體結果
  const statusIcon = summary.passed ? '✅' : '❌';
  const statusText = summary.passed ? '通過' : '失敗';
  markdown += `## 整體結果: ${statusIcon} ${statusText}\n\n`;
  
  markdown += `| 指標 | 數值 |\n`;
  markdown += `|------|------|\n`;
  markdown += `| 總測試數 | ${summary.totalTests} |\n`;
  markdown += `| 通過測試 | ${summary.passedTests} |\n`;
  markdown += `| 失敗測試 | ${summary.failedTests} |\n`;
  markdown += `| 成功率 | ${summary.successRate.toFixed(2)}% |\n\n`;
  
  // 品質指標詳情
  markdown += `## 品質指標詳情\n\n`;
  markdown += `| 類別 | 分數 | 閾值 | 狀態 | 差距 |\n`;
  markdown += `|------|------|------|------|------|\n`;
  
  Object.keys(qualityMetrics).forEach(category => {
    const metric = qualityMetrics[category];
    const statusIcon = metric.passed ? '✅' : '❌';
    const categoryName = getCategoryDisplayName(category);
    
    markdown += `| ${categoryName} | ${metric.score.toFixed(1)}% | ${metric.threshold}% | ${statusIcon} | ${metric.difference >= 0 ? '+' : ''}${metric.difference.toFixed(1)}% |\n`;
  });
  
  markdown += `\n`;
  
  // 如果有失敗項目，提供改進建議
  if (!summary.passed) {
    markdown += `## 改進建議\n\n`;
    
    Object.keys(qualityMetrics).forEach(category => {
      const metric = qualityMetrics[category];
      if (!metric.passed) {
        const categoryName = getCategoryDisplayName(category);
        const suggestions = getImprovementSuggestions(category);
        
        markdown += `### ${categoryName}\n`;
        markdown += `當前分數: ${metric.score.toFixed(1)}% (需要: ${metric.threshold}%)\n\n`;
        markdown += `建議改進方向:\n`;
        suggestions.forEach(suggestion => {
          markdown += `- ${suggestion}\n`;
        });
        markdown += `\n`;
      }
    });
  }
  
  // 儲存Markdown報告
  const markdownPath = path.resolve(__dirname, '../test-results/quality-report.md');
  fs.writeFileSync(markdownPath, markdown);
  
  return markdown;
}

/**
 * 獲取類別顯示名稱
 */
function getCategoryDisplayName(category) {
  const displayNames = {
    agent_consistency: 'Agent一致性',
    doc_quality: '文檔品質',
    tool_usage: '工具使用',
    template_compliance: '模板合規性',
    overall_success_rate: '整體成功率'
  };
  return displayNames[category] || category;
}

/**
 * 獲取改進建議
 */
function getImprovementSuggestions(category) {
  const suggestions = {
    agent_consistency: [
      '檢查prompt模板的一致性，確保相同輸入產生相似輸出',
      '調整AI模型的temperature參數，降低輸出隨機性',
      '增加更多的測試執行次數以獲得更穩定的統計結果',
      '檢查測試輸入是否過於模糊，導致AI輸出不穩定'
    ],
    doc_quality: [
      '確保所有必要的模板字段都被正確填寫',
      '檢查YAML格式的正確性和完整性',
      '提高需求描述的詳細程度和專業性',
      '確保驗收標準具體可測試',
      '增強非功能需求的量化指標'
    ],
    tool_usage: [
      '確保在適當的階段調用Sequential-thinking Tool',
      '檢查Todo-list Tool的使用是否符合工作流程要求',
      '驗證工具調用的順序和邏輯',
      '提高工具使用的一致性和規範性'
    ],
    template_compliance: [
      '嚴格按照requirement-tmpl.yaml格式輸出',
      '檢查所有必要字段是否完整',
      '確保ID格式符合規範（如F-001, NFR-P-001）',
      '驗證優先級和類型字段的有效值',
      '確保YAML語法正確無誤'
    ],
    overall_success_rate: [
      '分析失敗的測試案例，找出共同問題',
      '檢查測試環境和配置',
      '優化prompt設計和測試用例',
      '考慮調整品質閾值設定'
    ]
  };
  
  return suggestions[category] || ['檢查相關配置和實現'];
}

/**
 * 輸出控制台報告
 */
function printConsoleReport(report) {
  const { summary, qualityMetrics } = report;
  
  console.log('\n=== Create Requirements Task 品質門檻檢查報告 ===\n');
  
  // 整體結果
  const statusIcon = summary.passed ? '✅' : '❌';
  const statusText = summary.passed ? '通過' : '失敗';
  console.log(`整體結果: ${statusIcon} ${statusText}`);
  console.log(`測試統計: ${summary.passedTests}/${summary.totalTests} 通過 (${summary.successRate.toFixed(2)}%)\n`);
  
  // 各類別詳情
  console.log('品質指標詳情:');
  console.log('─'.repeat(70));
  
  Object.keys(qualityMetrics).forEach(category => {
    const metric = qualityMetrics[category];
    const statusIcon = metric.passed ? '✅' : '❌';
    const categoryName = getCategoryDisplayName(category).padEnd(12);
    const scoreDisplay = `${metric.score.toFixed(1)}%`.padStart(8);
    const thresholdDisplay = `${metric.threshold}%`.padStart(6);
    const differenceDisplay = `${metric.difference >= 0 ? '+' : ''}${metric.difference.toFixed(1)}%`.padStart(8);
    
    console.log(`${statusIcon} ${categoryName} ${scoreDisplay} (閾值: ${thresholdDisplay}, 差距: ${differenceDisplay})`);
  });
  
  console.log('─'.repeat(70));
  
  // 失敗情況下的改進建議
  if (!summary.passed) {
    console.log('\n改進建議:');
    Object.keys(qualityMetrics).forEach(category => {
      const metric = qualityMetrics[category];
      if (!metric.passed) {
        const categoryName = getCategoryDisplayName(category);
        console.log(`\n${categoryName} (${metric.score.toFixed(1)}% < ${metric.threshold}%):`);
        const suggestions = getImprovementSuggestions(category);
        suggestions.slice(0, 2).forEach(suggestion => {  // 只顯示前兩個建議
          console.log(`  • ${suggestion}`);
        });
      }
    });
  }
  
  console.log(`\n詳細報告已儲存至: test-results/quality-report.json`);
  console.log(`Markdown報告已儲存至: test-results/quality-report.md\n`);
}

/**
 * 主執行函數
 */
function main() {
  console.log('🔍 開始執行品質門檻檢查...\n');
  
  // 讀取測試結果
  const testResults = readTestResults();
  console.log(`📊 已載入測試結果: ${testResults.results.stats.successes + testResults.results.stats.failures} 個測試案例`);
  
  // 分析測試結果
  const analysisResult = analyzeTestResults(testResults);
  console.log(`📈 分析完成: ${analysisResult.passedTests} 通過, ${analysisResult.failedTests} 失敗`);
  
  // 檢查品質門檻
  const qualityGateResult = checkQualityGate(analysisResult);
  
  // 生成報告
  const report = generateReport(analysisResult, qualityGateResult);
  generateMarkdownReport(report);
  
  // 輸出控制台報告
  printConsoleReport(report);
  
  // 根據結果決定退出碼
  const exitCode = qualityGateResult.overallPassed ? 0 : 1;
  const resultText = qualityGateResult.overallPassed ? '通過' : '失敗';
  
  console.log(`🏁 品質門檻檢查結果: ${resultText}`);
  process.exit(exitCode);
}

// 如果直接執行此腳本
if (require.main === module) {
  main();
}

module.exports = {
  readTestResults,
  analyzeTestResults,
  checkQualityGate,
  generateReport,
  THRESHOLDS
};
