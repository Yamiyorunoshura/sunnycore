const fs = require('fs');
const path = require('path');

// 載入環境變數
require('dotenv').config();

// 預設配置
const config = {
  anthropic: {
    apiKey: process.env.ANTHROPIC_API_KEY,
    baseUrl: process.env.ANTHROPIC_BASE_URL || 'https://api.anthropic.com',
    model: process.env.ANTHROPIC_MODEL || 'claude-3-5-sonnet-20241022'
  },
  openai: {
    apiKey: process.env.OPENAI_API_KEY,
    baseUrl: process.env.OPENAI_BASE_URL || 'https://api.openai.com/v1',
    model: process.env.OPENAI_MODEL || 'gpt-4'
  },
  testing: {
    consistency_threshold: parseFloat(process.env.CONSISTENCY_THRESHOLD) || 0.85,
    quality_threshold: parseFloat(process.env.QUALITY_THRESHOLD) || 80,
    runs_count: parseInt(process.env.TEST_RUNS) || 3
  }
};

// Promptfoo 配置
module.exports = {
  description: 'Create Requirements Task CI/CD Testing Suite',
  
  providers: [
    {
      id: 'claude-sonnet',
      type: 'anthropic',
      config: {
        model: config.anthropic.model,
        apiKey: config.anthropic.apiKey,
        apiBaseUrl: config.anthropic.baseUrl,
        temperature: 0.1,  // 確保一致性
      }
    }
  ],

  // 測試套件配置
  tests: [
    'tests/agent-consistency.yml',
    'tests/doc-generation-consistency.yml',
    'tests/tool-usage-consistency.yml',
    'tests/quality-assurance.yml'
  ],

  // 輸出設定
  outputDir: './test-results',
  
  // 全域變數
  defaultTest: {
    options: {
      provider: 'claude-sonnet',
    },
  },

  // 客製化評估函數
  customGraders: {
    'yaml-structure': (output, expected) => {
      try {
        const yaml = require('js-yaml');
        const parsed = yaml.load(output);
        
        // 檢查必要的結構
        const hasProjectInfo = parsed.project_info && 
                              parsed.project_info.name && 
                              parsed.project_info.description;
        
        const hasFunctionalReqs = parsed.functional_requirements && 
                                Array.isArray(parsed.functional_requirements) &&
                                parsed.functional_requirements.length > 0;
        
        const hasNonFunctionalReqs = parsed.non_functional_requirements &&
                                   Array.isArray(parsed.non_functional_requirements) &&
                                   parsed.non_functional_requirements.length > 0;
        
        const score = (hasProjectInfo ? 33 : 0) + 
                     (hasFunctionalReqs ? 33 : 0) + 
                     (hasNonFunctionalReqs ? 34 : 0);
        
        return {
          pass: score >= 80,
          score: score / 100,
          reason: `YAML結構完整性: ${score}% (需要≥80%)`
        };
      } catch (error) {
        return {
          pass: false,
          score: 0,
          reason: `YAML解析失敗: ${error.message}`
        };
      }
    },

    'requirements-completeness': (output, expected) => {
      try {
        const yaml = require('js-yaml');
        const parsed = yaml.load(output);
        
        let totalRequirements = 0;
        let completeRequirements = 0;
        
        // 檢查功能性需求完整性
        if (parsed.functional_requirements) {
          parsed.functional_requirements.forEach(req => {
            totalRequirements++;
            if (req.id && req.title && req.description && 
                req.acceptance_criteria && req.acceptance_criteria.length > 0) {
              completeRequirements++;
            }
          });
        }
        
        // 檢查非功能性需求完整性
        if (parsed.non_functional_requirements) {
          parsed.non_functional_requirements.forEach(req => {
            totalRequirements++;
            if (req.id && req.description && req.metric && req.target_value) {
              completeRequirements++;
            }
          });
        }
        
        const completenessScore = totalRequirements > 0 ? 
                                (completeRequirements / totalRequirements) * 100 : 0;
        
        return {
          pass: completenessScore >= 90,
          score: completenessScore / 100,
          reason: `需求完整性: ${completenessScore.toFixed(1)}% (${completeRequirements}/${totalRequirements})`
        };
      } catch (error) {
        return {
          pass: false,
          score: 0,
          reason: `需求完整性檢查失敗: ${error.message}`
        };
      }
    }
  }
};
