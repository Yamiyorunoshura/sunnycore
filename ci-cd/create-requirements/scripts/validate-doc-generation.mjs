#!/usr/bin/env node
/**
 * Create Requirements 文檔生成一致性驗證腳本
 * 
 * 此腳本驗證YAML需求文檔與Markdown格式之間的轉換一致性，
 * 確保兩種格式包含相同的資訊且結構正確。
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import yaml from 'js-yaml';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// 配置
const CONFIG = {
  inputDir: path.resolve(__dirname, '../examples'),
  outputDir: path.resolve(__dirname, '../test-results/validation'),
  toleranceLevel: 0.85, // 內容相似度容忍度
  verbose: process.env.VERBOSE === 'true'
};

/**
 * 日誌輸出工具
 */
class Logger {
  static info(message) {
    console.log(`ℹ️  ${message}`);
  }
  
  static success(message) {
    console.log(`✅ ${message}`);
  }
  
  static warning(message) {
    console.log(`⚠️  ${message}`);
  }
  
  static error(message) {
    console.error(`❌ ${message}`);
  }
  
  static verbose(message) {
    if (CONFIG.verbose) {
      console.log(`🔍 ${message}`);
    }
  }
}

/**
 * YAML 內容分析器
 */
class YAMLAnalyzer {
  constructor(yamlContent) {
    try {
      this.data = yaml.load(yamlContent);
    } catch (error) {
      throw new Error(`YAML 解析失敗: ${error.message}`);
    }
  }
  
  getProjectInfo() {
    return this.data.project_info || {};
  }
  
  getFunctionalRequirements() {
    return this.data.functional_requirements || [];
  }
  
  getNonFunctionalRequirements() {
    return this.data.non_functional_requirements || [];
  }
  
  extractKeywords() {
    const keywords = new Set();
    
    // 從專案資訊提取關鍵字
    const projectInfo = this.getProjectInfo();
    if (projectInfo.name) keywords.add(projectInfo.name);
    if (projectInfo.description) {
      projectInfo.description.split(/\s+/).forEach(word => {
        if (word.length > 3) keywords.add(word.toLowerCase());
      });
    }
    
    // 從功能需求提取關鍵字
    this.getFunctionalRequirements().forEach(req => {
      if (req.title) keywords.add(req.title);
      if (req.description) {
        req.description.split(/\s+/).forEach(word => {
          if (word.length > 3) keywords.add(word.toLowerCase());
        });
      }
    });
    
    // 從非功能需求提取關鍵字
    this.getNonFunctionalRequirements().forEach(req => {
      if (req.description) {
        req.description.split(/\s+/).forEach(word => {
          if (word.length > 3) keywords.add(word.toLowerCase());
        });
      }
    });
    
    return Array.from(keywords);
  }
  
  getStructuralElements() {
    return {
      hasProjectInfo: Boolean(this.data.project_info),
      functionalRequirementsCount: this.getFunctionalRequirements().length,
      nonFunctionalRequirementsCount: this.getNonFunctionalRequirements().length,
      totalRequirements: this.getFunctionalRequirements().length + this.getNonFunctionalRequirements().length
    };
  }
}

/**
 * Markdown 內容分析器
 */
class MarkdownAnalyzer {
  constructor(markdownContent) {
    this.content = markdownContent;
    this.lines = markdownContent.split('\n');
  }
  
  extractHeadings() {
    const headings = {
      h1: [],
      h2: [],
      h3: []
    };
    
    this.lines.forEach(line => {
      const h1Match = line.match(/^# (.+)$/);
      const h2Match = line.match(/^## (.+)$/);
      const h3Match = line.match(/^### (.+)$/);
      
      if (h1Match) headings.h1.push(h1Match[1].trim());
      if (h2Match) headings.h2.push(h2Match[1].trim());
      if (h3Match) headings.h3.push(h3Match[1].trim());
    });
    
    return headings;
  }
  
  extractKeywords() {
    const keywords = new Set();
    const text = this.content.replace(/[#*_`-]/g, ''); // 移除markdown標記
    
    text.split(/\s+/).forEach(word => {
      const cleanWord = word.replace(/[^\w\u4e00-\u9fff]/g, '').toLowerCase();
      if (cleanWord.length > 3) {
        keywords.add(cleanWord);
      }
    });
    
    return Array.from(keywords);
  }
  
  getStructuralElements() {
    const headings = this.extractHeadings();
    return {
      hasMainTitle: headings.h1.length > 0,
      sectionCount: headings.h2.length,
      subsectionCount: headings.h3.length,
      hasTables: this.content.includes('|'),
      hasLists: /^[\s]*[-*+]|\d+\./.test(this.content),
      hasTaskLists: this.content.includes('- [ ]') || this.content.includes('- [x]')
    };
  }
  
  extractRequirementIDs() {
    const functionalIDs = this.content.match(/F-\d{3}/g) || [];
    const nonFunctionalIDs = this.content.match(/NFR-[A-Z]-\d{3}/g) || [];
    
    return {
      functional: [...new Set(functionalIDs)],
      nonFunctional: [...new Set(nonFunctionalIDs)],
      total: functionalIDs.length + nonFunctionalIDs.length
    };
  }
}

/**
 * 內容一致性比較器
 */
class ConsistencyComparator {
  constructor(yamlAnalyzer, markdownAnalyzer) {
    this.yaml = yamlAnalyzer;
    this.markdown = markdownAnalyzer;
  }
  
  compareKeywords() {
    const yamlKeywords = new Set(this.yaml.extractKeywords());
    const markdownKeywords = new Set(this.markdown.extractKeywords());
    
    const intersection = new Set([...yamlKeywords].filter(x => markdownKeywords.has(x)));
    const union = new Set([...yamlKeywords, ...markdownKeywords]);
    
    const similarity = intersection.size / union.size;
    
    return {
      similarity,
      yamlKeywords: yamlKeywords.size,
      markdownKeywords: markdownKeywords.size,
      commonKeywords: intersection.size,
      passed: similarity >= CONFIG.toleranceLevel
    };
  }
  
  compareStructure() {
    const yamlStruct = this.yaml.getStructuralElements();
    const markdownStruct = this.markdown.getStructuralElements();
    const markdownIDs = this.markdown.extractRequirementIDs();
    
    const results = {
      projectInfoConsistency: {
        expected: yamlStruct.hasProjectInfo,
        actual: markdownStruct.hasMainTitle,
        passed: Boolean(yamlStruct.hasProjectInfo) === Boolean(markdownStruct.hasMainTitle)
      },
      
      functionalRequirementsConsistency: {
        expected: yamlStruct.functionalRequirementsCount,
        actual: markdownIDs.functional.length,
        difference: Math.abs(yamlStruct.functionalRequirementsCount - markdownIDs.functional.length),
        passed: Math.abs(yamlStruct.functionalRequirementsCount - markdownIDs.functional.length) <= 1
      },
      
      nonFunctionalRequirementsConsistency: {
        expected: yamlStruct.nonFunctionalRequirementsCount,
        actual: markdownIDs.nonFunctional.length,
        difference: Math.abs(yamlStruct.nonFunctionalRequirementsCount - markdownIDs.nonFunctional.length),
        passed: Math.abs(yamlStruct.nonFunctionalRequirementsCount - markdownIDs.nonFunctional.length) <= 1
      },
      
      markdownFormatting: {
        hasTables: markdownStruct.hasTables,
        hasLists: markdownStruct.hasLists,
        sectionCount: markdownStruct.sectionCount,
        passed: markdownStruct.hasTables && markdownStruct.hasLists && markdownStruct.sectionCount >= 2
      }
    };
    
    results.overallPassed = Object.values(results).every(result => 
      typeof result === 'object' ? result.passed : true
    );
    
    return results;
  }
  
  generateComparisonReport() {
    const keywordComparison = this.compareKeywords();
    const structureComparison = this.compareStructure();
    
    const overallScore = (
      (keywordComparison.similarity * 0.6) +
      (structureComparison.overallPassed ? 0.4 : 0)
    ) * 100;
    
    return {
      overallScore,
      passed: overallScore >= (CONFIG.toleranceLevel * 100),
      keywordComparison,
      structureComparison,
      recommendations: this.generateRecommendations(keywordComparison, structureComparison)
    };
  }
  
  generateRecommendations(keywordComp, structComp) {
    const recommendations = [];
    
    if (keywordComp.similarity < 0.8) {
      recommendations.push('關鍵字相似度偏低，建議檢查 YAML 到 Markdown 的內容轉換是否完整');
    }
    
    if (!structComp.functionalRequirementsConsistency.passed) {
      recommendations.push(`功能需求數量不一致：YAML ${structComp.functionalRequirementsConsistency.expected} vs Markdown ${structComp.functionalRequirementsConsistency.actual}`);
    }
    
    if (!structComp.nonFunctionalRequirementsConsistency.passed) {
      recommendations.push(`非功能需求數量不一致：YAML ${structComp.nonFunctionalRequirementsConsistency.expected} vs Markdown ${structComp.nonFunctionalRequirementsConsistency.actual}`);
    }
    
    if (!structComp.markdownFormatting.hasTables) {
      recommendations.push('Markdown 格式缺少表格，建議使用表格展示需求資訊');
    }
    
    if (!structComp.markdownFormatting.hasLists) {
      recommendations.push('Markdown 格式缺少列表，建議使用列表結構化呈現資訊');
    }
    
    if (recommendations.length === 0) {
      recommendations.push('文檔轉換品質良好，無需特別改進');
    }
    
    return recommendations;
  }
}

/**
 * 測試用例生成器
 */
class TestCaseGenerator {
  static generateSampleYAML() {
    return `
project_info:
  name: "線上書店系統"
  version: "1.0.0"
  description: "提供書籍瀏覽、購買和管理功能的電子商務平台"
  background: "為了滿足數位閱讀需求，建立全方位的線上書店服務"
  objectives:
    - "提供便利的書籍購買體驗"
    - "支援多種支付方式"
    - "建立完善的庫存管理系統"

functional_requirements:
  - id: "F-001"
    title: "用戶註冊與認證"
    description: "用戶可以通過電子郵件註冊帳戶，並使用帳號密碼或社交媒體登入系統"
    priority: "High"
    user_story: "作為一個新用戶，我希望能夠快速註冊並登入系統，以便開始使用服務"
    acceptance_criteria:
      - "用戶可以使用有效的電子郵件地址註冊"
      - "系統發送驗證郵件確認帳戶"
      - "用戶可以使用Google或Facebook登入"
      - "登入失敗3次後暫時鎖定帳戶"
    business_rules: []
    dependencies: []
    effort_estimate: "3-5天"
    notes: "考慮整合第三方認證服務"

  - id: "F-002"
    title: "書籍搜索與瀏覽"
    description: "提供多維度的書籍搜索功能，支援關鍵字、分類、作者等搜索條件"
    priority: "High"
    user_story: "作為一個讀者，我希望能夠輕鬆找到想要的書籍"
    acceptance_criteria:
      - "支援全文搜索功能"
      - "可以按分類、價格、評分篩選"
      - "搜索結果支援排序"
      - "提供搜索建議和自動完成"
    business_rules: []
    dependencies: ["F-001"]
    effort_estimate: "5-7天"
    notes: "需要建立搜索索引"

non_functional_requirements:
  - id: "NFR-P-001"
    description: "系統回應時間要求"
    metric: "頁面載入時間"
    type: "performance"
    target_value: "< 2秒"
    test_method: "使用負載測試工具進行壓力測試"
    
  - id: "NFR-S-001"
    description: "用戶資料安全性"
    compliance_standard: "GDPR, PCI DSS"
    type: "security"
    risk_level: "High"
    mitigation_approach: "實施端到端加密和定期安全審計"
`;
  }
  
  static generateExpectedMarkdown() {
    return `# 線上書店系統需求規格

## 專案概述

**專案名稱**: 線上書店系統  
**版本**: 1.0.0  
**描述**: 提供書籍瀏覽、購買和管理功能的電子商務平台

### 專案背景
為了滿足數位閱讀需求，建立全方位的線上書店服務

### 專案目標
- 提供便利的書籍購買體驗
- 支援多種支付方式  
- 建立完善的庫存管理系統

## 功能需求

### F-001: 用戶註冊與認證

**優先級**: High  
**用戶故事**: 作為一個新用戶，我希望能夠快速註冊並登入系統，以便開始使用服務

**需求描述**: 用戶可以通過電子郵件註冊帳戶，並使用帳號密碼或社交媒體登入系統

**驗收標準**:
- [ ] 用戶可以使用有效的電子郵件地址註冊
- [ ] 系統發送驗證郵件確認帳戶
- [ ] 用戶可以使用Google或Facebook登入
- [ ] 登入失敗3次後暫時鎖定帳戶

**預估工期**: 3-5天  
**備註**: 考慮整合第三方認證服務

### F-002: 書籍搜索與瀏覽

**優先級**: High  
**用戶故事**: 作為一個讀者，我希望能夠輕鬆找到想要的書籍

**需求描述**: 提供多維度的書籍搜索功能，支援關鍵字、分類、作者等搜索條件

**驗收標準**:
- [ ] 支援全文搜索功能
- [ ] 可以按分類、價格、評分篩選
- [ ] 搜索結果支援排序
- [ ] 提供搜索建議和自動完成

**依賴需求**: F-001  
**預估工期**: 5-7天  
**備註**: 需要建立搜索索引

## 非功能需求

| 需求ID | 類型 | 描述 | 目標值 | 測試方法 |
|--------|------|------|--------|----------|
| NFR-P-001 | performance | 系統回應時間要求 | < 2秒 | 使用負載測試工具進行壓力測試 |
| NFR-S-001 | security | 用戶資料安全性 | GDPR, PCI DSS合規 | 實施端到端加密和定期安全審計 |

## 總結

本需求規格書定義了線上書店系統的核心功能和品質要求，為後續的系統設計和開發提供了明確的指引。
`;
  }
}

/**
 * 驗證執行器
 */
class ValidationRunner {
  constructor() {
    this.results = [];
  }
  
  async runValidation(yamlContent, markdownContent, testName = 'unnamed') {
    Logger.info(`開始執行 ${testName} 驗證...`);
    
    try {
      const yamlAnalyzer = new YAMLAnalyzer(yamlContent);
      const markdownAnalyzer = new MarkdownAnalyzer(markdownContent);
      const comparator = new ConsistencyComparator(yamlAnalyzer, markdownAnalyzer);
      
      const result = {
        testName,
        timestamp: new Date().toISOString(),
        ...comparator.generateComparisonReport()
      };
      
      this.results.push(result);
      
      if (result.passed) {
        Logger.success(`${testName} 驗證通過 (評分: ${result.overallScore.toFixed(1)}%)`);
      } else {
        Logger.error(`${testName} 驗證失敗 (評分: ${result.overallScore.toFixed(1)}%)`);
        result.recommendations.forEach(rec => Logger.warning(rec));
      }
      
      return result;
      
    } catch (error) {
      Logger.error(`${testName} 驗證過程中發生錯誤: ${error.message}`);
      const errorResult = {
        testName,
        timestamp: new Date().toISOString(),
        passed: false,
        overallScore: 0,
        error: error.message
      };
      this.results.push(errorResult);
      return errorResult;
    }
  }
  
  async runAllValidations() {
    Logger.info('開始執行文檔生成一致性驗證...');
    
    // 確保輸出目錄存在
    if (!fs.existsSync(CONFIG.outputDir)) {
      fs.mkdirSync(CONFIG.outputDir, { recursive: true });
    }
    
    // 執行內建測試用例
    Logger.info('執行內建測試用例...');
    const builtinYaml = TestCaseGenerator.generateSampleYAML();
    const builtinMarkdown = TestCaseGenerator.generateExpectedMarkdown();
    
    await this.runValidation(builtinYaml, builtinMarkdown, '內建範例測試');
    
    // 搜索並執行自定義測試用例
    if (fs.existsSync(CONFIG.inputDir)) {
      Logger.info('搜索自定義測試用例...');
      
      const files = fs.readdirSync(CONFIG.inputDir);
      const yamlFiles = files.filter(f => f.endsWith('.yaml') || f.endsWith('.yml'));
      
      for (const yamlFile of yamlFiles) {
        const baseName = path.parse(yamlFile).name;
        const markdownFile = files.find(f => 
          f.startsWith(baseName) && f.endsWith('.md')
        );
        
        if (markdownFile) {
          const yamlPath = path.join(CONFIG.inputDir, yamlFile);
          const markdownPath = path.join(CONFIG.inputDir, markdownFile);
          
          const yamlContent = fs.readFileSync(yamlPath, 'utf-8');
          const markdownContent = fs.readFileSync(markdownPath, 'utf-8');
          
          await this.runValidation(yamlContent, markdownContent, `自定義測試: ${baseName}`);
        }
      }
    }
    
    this.generateSummaryReport();
  }
  
  generateSummaryReport() {
    const totalTests = this.results.length;
    const passedTests = this.results.filter(r => r.passed).length;
    const failedTests = totalTests - passedTests;
    const averageScore = this.results.reduce((sum, r) => sum + (r.overallScore || 0), 0) / totalTests;
    
    const summary = {
      timestamp: new Date().toISOString(),
      totalTests,
      passedTests,
      failedTests,
      successRate: (passedTests / totalTests) * 100,
      averageScore,
      details: this.results
    };
    
    // 儲存 JSON 報告
    const jsonReportPath = path.join(CONFIG.outputDir, 'validation-report.json');
    fs.writeFileSync(jsonReportPath, JSON.stringify(summary, null, 2));
    
    // 生成 Markdown 報告
    this.generateMarkdownReport(summary);
    
    // 控制台輸出摘要
    Logger.info('\n=== 文檔生成一致性驗證摘要 ===');
    Logger.info(`總測試數: ${totalTests}`);
    Logger.info(`通過測試: ${passedTests}`);
    Logger.info(`失敗測試: ${failedTests}`);
    Logger.info(`成功率: ${summary.successRate.toFixed(1)}%`);
    Logger.info(`平均評分: ${averageScore.toFixed(1)}%`);
    
    if (passedTests === totalTests) {
      Logger.success('🎉 所有文檔生成一致性測試均已通過！');
    } else {
      Logger.error('💥 部分測試未通過，請檢查詳細報告');
    }
    
    Logger.info(`詳細報告已保存至: ${jsonReportPath}`);
  }
  
  generateMarkdownReport(summary) {
    let markdown = '# 文檔生成一致性驗證報告\n\n';
    markdown += `**生成時間**: ${new Date(summary.timestamp).toLocaleString('zh-TW')}\n\n`;
    
    // 摘要表格
    markdown += '## 驗證摘要\n\n';
    markdown += '| 指標 | 數值 |\n';
    markdown += '|------|------|\n';
    markdown += `| 總測試數 | ${summary.totalTests} |\n`;
    markdown += `| 通過測試 | ${summary.passedTests} |\n`;
    markdown += `| 失敗測試 | ${summary.failedTests} |\n`;
    markdown += `| 成功率 | ${summary.successRate.toFixed(1)}% |\n`;
    markdown += `| 平均評分 | ${summary.averageScore.toFixed(1)}% |\n\n`;
    
    // 詳細結果
    markdown += '## 詳細測試結果\n\n';
    
    summary.details.forEach(result => {
      const status = result.passed ? '✅' : '❌';
      const score = result.overallScore?.toFixed(1) || 'N/A';
      
      markdown += `### ${status} ${result.testName}\n\n`;
      markdown += `**評分**: ${score}%\n`;
      markdown += `**時間**: ${new Date(result.timestamp).toLocaleString('zh-TW')}\n\n`;
      
      if (result.error) {
        markdown += `**錯誤**: ${result.error}\n\n`;
      } else if (result.recommendations) {
        markdown += '**建議**:\n';
        result.recommendations.forEach(rec => {
          markdown += `- ${rec}\n`;
        });
        markdown += '\n';
      }
    });
    
    // 儲存 Markdown 報告
    const markdownReportPath = path.join(CONFIG.outputDir, 'validation-report.md');
    fs.writeFileSync(markdownReportPath, markdown);
    Logger.info(`Markdown 報告已保存至: ${markdownReportPath}`);
  }
}

/**
 * 主執行函數
 */
async function main() {
  try {
    const runner = new ValidationRunner();
    await runner.runAllValidations();
    
    // 根據結果設定退出碼
    const allPassed = runner.results.every(r => r.passed);
    process.exit(allPassed ? 0 : 1);
    
  } catch (error) {
    Logger.error(`驗證過程發生未預期的錯誤: ${error.message}`);
    process.exit(1);
  }
}

// 如果直接執行此腳本
if (import.meta.url === `file://${process.argv[1]}`) {
  main();
}

export {
  YAMLAnalyzer,
  MarkdownAnalyzer,
  ConsistencyComparator,
  ValidationRunner,
  TestCaseGenerator
};
