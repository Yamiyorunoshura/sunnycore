#!/usr/bin/env node
/**
 * SUNNYCORE CI/CD 環境變數驗證腳本
 * 驗證 OpenRouter API 配置和測試環境是否正確設置
 */

require('dotenv').config();

console.log('🔍 SUNNYCORE CI/CD 環境驗證開始...\n');

// 檢查必要的環境變數
const requiredEnvVars = [
  'OPENROUTER_API_KEY',
  'OPENROUTER_BASE_URL',
  'ANTHROPIC_API_KEY',
  'ANTHROPIC_BASE_URL'
];

let envCheckPassed = true;

console.log('1. 📋 環境變數檢查:');
requiredEnvVars.forEach(envVar => {
  const value = process.env[envVar];
  const status = value ? '✅' : '❌';
  const displayValue = value ? 
    (envVar.includes('KEY') ? `${value.substring(0, 10)}...` : value) 
    : 'undefined';
  
  console.log(`   ${status} ${envVar}: ${displayValue}`);
  
  if (!value) {
    envCheckPassed = false;
  }
});

console.log('\n2. 🌐 OpenRouter API 連接測試:');
if (process.env.OPENROUTER_API_KEY) {
  // 使用 fetch 或 https 模組測試 API 連接
  const https = require('https');
  
  const options = {
    hostname: 'openrouter.ai',
    port: 443,
    path: '/api/v1/models',
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${process.env.OPENROUTER_API_KEY}`,
      'Content-Type': 'application/json'
    }
  };
  
  const req = https.request(options, (res) => {
    let data = '';
    
    res.on('data', (chunk) => {
      data += chunk;
    });
    
    res.on('end', () => {
      if (res.statusCode === 200) {
        console.log('   ✅ API 連接成功');
        try {
          const models = JSON.parse(data);
          console.log(`   📊 可用模型數量: ${models.data?.length || 0}`);
          
          // 檢查是否有 Claude 模型
          const claudeModels = models.data?.filter(model => 
            model.id.includes('claude') || model.id.includes('anthropic')
          );
          console.log(`   🤖 Claude 相關模型: ${claudeModels?.length || 0}`);
          
        } catch (error) {
          console.log('   ⚠️  回應解析失敗:', error.message);
        }
      } else {
        console.log(`   ❌ API 連接失敗 (HTTP ${res.statusCode})`);
      }
      
      console.log('\n3. 🧪 Promptfoo 配置檢查:');
      console.log(`   📝 PROMPTFOO_PROVIDER: ${process.env.PROMPTFOO_PROVIDER || 'undefined'}`);
      console.log(`   🔑 PROMPTFOO_API_KEY: ${process.env.PROMPTFOO_API_KEY ? '已設置' : '未設置'}`);
      
      console.log('\n4. 📈 測試參數配置:');
      console.log(`   🎯 CONSISTENCY_THRESHOLD: ${process.env.CONSISTENCY_THRESHOLD || '預設 0.85'}`);
      console.log(`   📊 QUALITY_THRESHOLD: ${process.env.QUALITY_THRESHOLD || '預設 80'}`);
      console.log(`   🔄 TEST_RUNS: ${process.env.TEST_RUNS || '預設 3'}`);
      
      console.log('\n' + '='.repeat(50));
      const overallStatus = envCheckPassed && res.statusCode === 200 ? '✅ 通過' : '❌ 失敗';
      console.log(`🏁 整體環境驗證: ${overallStatus}`);
      
      if (envCheckPassed && res.statusCode === 200) {
        console.log('🚀 環境配置完成，可以開始 CI/CD 測試！');
      } else {
        console.log('⚠️  請修正上述問題後重新測試');
        process.exit(1);
      }
    });
  });
  
  req.on('error', (error) => {
    console.log('   ❌ API 連接錯誤:', error.message);
    console.log('\n🏁 整體環境驗證: ❌ 失敗');
    process.exit(1);
  });
  
  req.setTimeout(10000, () => {
    console.log('   ❌ API 連接超時 (10秒)');
    req.destroy();
    console.log('\n🏁 整體環境驗證: ❌ 失敗');
    process.exit(1);
  });
  
  req.end();
  
} else {
  console.log('   ❌ OPENROUTER_API_KEY 未設置，無法測試 API 連接');
  console.log('\n🏁 整體環境驗證: ❌ 失敗');
  process.exit(1);
}
