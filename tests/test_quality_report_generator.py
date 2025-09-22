import unittest
import tempfile
import shutil
import json
from pathlib import Path
from datetime import datetime, timezone
from unittest.mock import Mock, patch

import sys
sys.path.append('src')

from behavior.quality_report_generator import QualityReportGenerator, QualityReportConfig


class TestQualityReportGenerator(unittest.TestCase):
    """Test cases for QualityReportGenerator"""

    def setUp(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.config = QualityReportConfig(
            include_charts=True,
            include_recommendations=True,
            include_trends=True,
            include_executive_summary=True,
            output_formats=["markdown", "json"]
        )
        self.generator = QualityReportGenerator(self.config)

    def tearDown(self):
        """Clean up test environment"""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_initialization(self):
        """Test QualityReportGenerator initialization"""
        self.assertIsInstance(self.generator.config, QualityReportConfig)
        self.assertTrue(self.generator.config.include_charts)
        self.assertTrue(self.generator.config.include_recommendations)
        self.assertEqual(self.generator.config.output_formats, ["markdown", "json"])

    def test_initialization_with_default_config(self):
        """Test initialization with default configuration"""
        generator = QualityReportGenerator()
        self.assertIsInstance(generator.config, QualityReportConfig)
        self.assertEqual(generator.config.output_formats, ["markdown", "html", "json"])

    def test_process_metrics_data(self):
        """Test metrics data processing"""
        raw_metrics = {
            'composite_score': 0.85,
            'quality_level': 'good',
            'individual_metrics': {
                'accuracy': 0.9,
                'completeness': 0.8,
                'performance': 0.95
            },
            'thresholds': {
                'accuracy': 0.85,
                'completeness': 0.90,
                'performance': 0.95
            },
            'test_count': 100
        }

        processed = self.generator._process_metrics_data(raw_metrics)

        self.assertEqual(processed['composite_score'], 0.85)
        self.assertEqual(processed['quality_level'], 'good')
        self.assertEqual(processed['test_count'], 100)

        # Check individual metrics
        self.assertIn('accuracy', processed['individual_metrics'])
        self.assertEqual(processed['individual_metrics']['accuracy']['value'], 0.9)
        self.assertEqual(processed['individual_metrics']['accuracy']['status'], 'pass')

        self.assertIn('completeness', processed['individual_metrics'])
        self.assertEqual(processed['individual_metrics']['completeness']['value'], 0.8)
        self.assertEqual(processed['individual_metrics']['completeness']['status'], 'warning')

        # Check thresholds
        self.assertEqual(processed['thresholds']['accuracy'], 0.85)

    def test_process_trend_data(self):
        """Test trend data processing"""
        raw_trends = {
            'trend': 'improving',
            'slope': 0.01,
            'correlation': 0.8,
            'confidence': 0.85,
            'score_change': 0.05,
            'recent_score': 0.85,
            'oldest_score': 0.80
        }

        processed = self.generator._process_trend_data(raw_trends)

        self.assertEqual(processed['overall_trend'], 'improving')
        self.assertEqual(processed['slope'], 0.01)
        self.assertEqual(processed['correlation'], 0.8)
        self.assertEqual(processed['confidence'], 0.85)
        self.assertEqual(processed['score_change'], 0.05)
        self.assertEqual(processed['recent_score'], 0.85)
        self.assertEqual(processed['oldest_score'], 0.80)

    def test_process_architecture_data(self):
        """Test architecture data processing"""
        raw_architecture = {
            'overall_f1_score': 0.92,
            'component_f1_scores': {
                'service_a': 0.95,
                'service_b': 0.88,
                'service_c': 0.91
            },
            'validation_summary': {
                'total_components': 3,
                'aligned_components': 2,
                'misaligned_components': 1
            },
            'architecture_issues': [
                'Service B has low F1 score'
            ]
        }

        processed = self.generator._process_architecture_data(raw_architecture)

        self.assertEqual(processed['overall_f1_score'], 0.92)
        self.assertEqual(processed['component_scores']['service_a'], 0.95)
        self.assertEqual(processed['component_scores']['service_b'], 0.88)
        self.assertEqual(processed['validation_summary']['total_components'], 3)
        self.assertEqual(len(processed['architecture_issues']), 1)

    def test_process_requirement_data(self):
        """Test requirement data processing"""
        raw_requirements = {
            'total_requirements': 50,
            'covered_requirements': 45,
            'fully_covered_requirements': 40,
            'coverage_distribution': {
                '100%': 40,
                '76-99%': 5,
                '0%': 5
            },
            'requirement_mappings': {
                'F-1': {'coverage_percentage': 1.0},
                'F-2': {'coverage_percentage': 0.8}
            }
        }

        processed = self.generator._process_requirement_data(raw_requirements)

        self.assertEqual(processed['total_requirements'], 50)
        self.assertEqual(processed['covered_requirements'], 45)
        self.assertEqual(processed['fully_covered_requirements'], 40)
        self.assertEqual(processed['coverage_percentage'], 0.9)  # 45/50
        self.assertEqual(processed['coverage_distribution']['100%'], 40)

    def test_calculate_coverage_percentage(self):
        """Test coverage percentage calculation"""
        # Test normal case
        data = {'total_requirements': 20, 'covered_requirements': 15}
        percentage = self.generator._calculate_coverage_percentage(data)
        self.assertEqual(percentage, 0.75)

        # Test zero total
        data = {'total_requirements': 0, 'covered_requirements': 0}
        percentage = self.generator._calculate_coverage_percentage(data)
        self.assertEqual(percentage, 0.0)

        # Test missing data
        data = {}
        percentage = self.generator._calculate_coverage_percentage(data)
        self.assertEqual(percentage, 0.0)

    def test_get_metric_status(self):
        """Test metric status determination"""
        # Test passing metric
        status = self.generator._get_metric_status('accuracy', 0.9)
        self.assertEqual(status, 'pass')

        # Test warning metric
        status = self.generator._get_metric_status('accuracy', 0.75)
        self.assertEqual(status, 'warning')

        # Test failing metric
        status = self.generator._get_metric_status('accuracy', 0.6)
        self.assertEqual(status, 'fail')

        # Test unknown metric (default threshold)
        status = self.generator._get_metric_status('unknown', 0.9)
        self.assertEqual(status, 'pass')

    def test_calculate_health_score(self):
        """Test health score calculation"""
        report_data = {
            'metrics': {
                'composite_score': 0.85
            },
            'requirements': {
                'coverage_percentage': 0.9
            },
            'architecture': {
                'overall_f1_score': 0.92
            },
            'trends': {
                'overall_trend': 'stable'
            }
        }

        health_score = self.generator._calculate_health_score(report_data)
        self.assertIsInstance(health_score, float)
        self.assertGreaterEqual(health_score, 0.0)
        self.assertLessEqual(health_score, 1.0)

    def test_generate_highlights(self):
        """Test highlights generation"""
        report_data = {
            'metrics': {
                'composite_score': 0.95,
                'individual_metrics': {
                    'accuracy': {'value': 0.98},
                    'performance': {'value': 0.96}
                }
            },
            'requirements': {
                'coverage_percentage': 0.96
            }
        }

        highlights = self.generator._generate_highlights(report_data)
        self.assertIsInstance(highlights, list)
        self.assertGreater(len(highlights), 0)
        self.assertTrue(any('Excellent overall quality score' in h for h in highlights))

    def test_generate_concerns(self):
        """Test concerns generation"""
        report_data = {
            'metrics': {
                'individual_metrics': {
                    'accuracy': {'value': 0.6},
                    'reliability': {'value': 0.65}
                }
            },
            'requirements': {
                'coverage_percentage': 0.75
            },
            'trends': {
                'overall_trend': 'declining'
            }
        }

        concerns = self.generator._generate_concerns(report_data)
        self.assertIsInstance(concerns, list)
        self.assertGreater(len(concerns), 0)
        self.assertTrue(any('declining trend' in c for c in concerns))

    def test_generate_executive_message(self):
        """Test executive message generation"""
        # Test excellent health
        report_data = {
            'executive_summary': {
                'overall_health': 0.95
            },
            'metrics': {
                'quality_level': 'excellent'
            },
            'trends': {
                'overall_trend': 'stable'
            }
        }

        message = self.generator._generate_executive_message(report_data)
        self.assertIn('excellent quality', message)
        self.assertIn('95.0%', message)

        # Test poor health
        report_data['executive_summary']['overall_health'] = 0.65
        message = self.generator._generate_executive_message(report_data)
        self.assertIn('requires immediate attention', message)

    def test_generate_recommendations(self):
        """Test recommendations generation"""
        report_data = {
            'metrics': {
                'individual_metrics': {
                    'accuracy': {'value': 0.6, 'status': 'fail'},
                    'completeness': {'value': 0.7, 'status': 'warning'},
                    'performance': {'value': 0.98, 'status': 'pass'}
                }
            },
            'requirements': {
                'coverage_percentage': 0.85
            },
            'architecture': {
                'overall_f1_score': 0.88
            }
        }

        recommendations = self.generator._generate_recommendations(report_data)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

        # Check that failing metrics have high priority recommendations
        accuracy_recs = [r for r in recommendations if r['metric'] == 'accuracy']
        self.assertEqual(len(accuracy_recs), 1)
        self.assertEqual(accuracy_recs[0]['priority'], 'high')

    def test_get_metric_recommendation(self):
        """Test specific metric recommendations"""
        accuracy_rec = self.generator._get_metric_recommendation('accuracy')
        self.assertIn('accuracy', accuracy_rec.lower())
        self.assertIn('prompt engineering', accuracy_rec.lower())

        performance_rec = self.generator._get_metric_recommendation('performance')
        self.assertIn('optimize', performance_rec.lower())

        unknown_rec = self.generator._get_metric_recommendation('unknown')
        self.assertIn('review', unknown_rec.lower())

    def test_generate_charts_data(self):
        """Test charts data generation"""
        report_data = {
            'metrics': {
                'individual_metrics': {
                    'accuracy': {'value': 0.9},
                    'performance': {'value': 0.95}
                },
                'thresholds': {
                    'accuracy': 0.85,
                    'performance': 0.9
                }
            },
            'requirements': {
                'coverage_distribution': {
                    '100%': 10,
                    '76-99%': 5
                }
            },
            'architecture': {
                'component_scores': {
                    'service_a': 0.95,
                    'service_b': 0.88
                }
            }
        }

        charts_data = self.generator._generate_charts_data(report_data)

        self.assertIn('metrics_radar', charts_data)
        self.assertIn('trend_line', charts_data)
        self.assertIn('coverage_pie', charts_data)
        self.assertIn('component_f1_bars', charts_data)

        # Check radar chart structure
        radar = charts_data['metrics_radar']
        self.assertEqual(radar['type'], 'radar')
        self.assertEqual(len(radar['datasets']), 2)
        self.assertEqual(radar['datasets'][0]['label'], 'Actual Values')
        self.assertEqual(radar['datasets'][1]['label'], 'Thresholds')

    def test_generate_metrics_radar_data(self):
        """Test radar chart data generation"""
        report_data = {
            'metrics': {
                'individual_metrics': {
                    'accuracy': {'value': 0.9},
                    'performance': {'value': 0.95}
                },
                'thresholds': {
                    'accuracy': 0.85,
                    'performance': 0.9
                }
            }
        }

        radar_data = self.generator._generate_metrics_radar_data(report_data)

        self.assertEqual(radar_data['type'], 'radar')
        self.assertEqual(radar_data['labels'], ['Accuracy', 'Performance'])
        self.assertEqual(radar_data['datasets'][0]['data'], [0.9, 0.95])
        self.assertEqual(radar_data['datasets'][1]['data'], [0.85, 0.9])

    def test_generate_coverage_pie_data(self):
        """Test coverage pie chart data generation"""
        report_data = {
            'requirements': {
                'coverage_distribution': {
                    '100%': 10,
                    '76-99%': 5,
                    '0%': 2
                }
            }
        }

        pie_data = self.generator._generate_coverage_pie_data(report_data)

        self.assertEqual(pie_data['type'], 'pie')
        self.assertEqual(pie_data['labels'], ['100%', '76-99%', '0%'])
        self.assertEqual(pie_data['datasets'][0]['data'], [10, 5, 2])

    def test_generate_component_f1_bars_data(self):
        """Test component F1 bars chart data generation"""
        report_data = {
            'architecture': {
                'component_scores': {
                    'service_a': 0.95,
                    'service_b': 0.88,
                    'service_c': 0.92
                }
            }
        }

        bars_data = self.generator._generate_component_f1_bars_data(report_data)

        self.assertEqual(bars_data['type'], 'bar')
        self.assertEqual(bars_data['labels'], ['service_a', 'service_b', 'service_c'])
        self.assertEqual(bars_data['datasets'][0]['data'], [0.95, 0.88, 0.92])

    def test_generate_comprehensive_report(self):
        """Test comprehensive report generation"""
        metrics_data = {
            'composite_score': 0.85,
            'quality_level': 'good',
            'individual_metrics': {
                'accuracy': 0.9,
                'completeness': 0.8,
                'performance': 0.95
            },
            'thresholds': {
                'accuracy': 0.85,
                'completeness': 0.90,
                'performance': 0.95
            },
            'test_count': 100
        }

        trend_data = {
            'trend': 'stable',
            'slope': 0.001,
            'correlation': 0.5,
            'confidence': 0.6,
            'score_change': 0.02,
            'recent_score': 0.85,
            'oldest_score': 0.83
        }

        architecture_data = {
            'overall_f1_score': 0.92,
            'component_f1_scores': {
                'service_a': 0.95,
                'service_b': 0.88
            },
            'validation_summary': {
                'total_components': 2,
                'aligned_components': 2
            },
            'architecture_issues': []
        }

        requirement_data = {
            'total_requirements': 20,
            'covered_requirements': 18,
            'fully_covered_requirements': 16,
            'coverage_distribution': {
                '100%': 16,
                '76-99%': 2,
                '0%': 2
            }
        }

        generated_files = self.generator.generate_comprehensive_report(
            metrics_data=metrics_data,
            trend_data=trend_data,
            architecture_data=architecture_data,
            requirement_data=requirement_data,
            output_dir=self.temp_dir
        )

        self.assertIsInstance(generated_files, dict)
        self.assertIn('markdown', generated_files)
        self.assertIn('json', generated_files)

        # Check that files were created
        for file_path in generated_files.values():
            self.assertTrue(Path(file_path).exists())
            self.assertTrue(Path(file_path).stat().st_size > 0)

        # Check markdown content
        with open(generated_files['markdown'], 'r', encoding='utf-8') as f:
            markdown_content = f.read()
            self.assertIn('# Quality Report', markdown_content)
            self.assertIn('Executive Summary', markdown_content)
            self.assertIn('Quality Metrics', markdown_content)
            self.assertIn('0.850', markdown_content)  # Composite score

        # Check JSON content
        with open(generated_files['json'], 'r', encoding='utf-8') as f:
            json_content = json.load(f)
            self.assertIn('timestamp', json_content)
            self.assertIn('metrics', json_content)
            self.assertIn('executive_summary', json_content)
            self.assertEqual(json_content['metrics']['composite_score'], 0.85)

    def test_generate_report_with_minimal_data(self):
        """Test report generation with minimal data"""
        minimal_metrics = {
            'composite_score': 0.7,
            'quality_level': 'fair',
            'individual_metrics': {},
            'thresholds': {},
            'test_count': 10
        }

        generated_files = self.generator.generate_comprehensive_report(
            metrics_data=minimal_metrics,
            output_dir=self.temp_dir
        )

        self.assertIsInstance(generated_files, dict)
        self.assertIn('markdown', generated_files)
        self.assertIn('json', generated_files)

        # Check that files were created even with minimal data
        for file_path in generated_files.values():
            self.assertTrue(Path(file_path).exists())
            self.assertTrue(Path(file_path).stat().st_size > 0)

    def test_error_handling(self):
        """Test error handling in report generation"""
        # Test with invalid data
        with self.assertRaises(Exception):
            self.generator.generate_comprehensive_report(
                metrics_data=None,
                output_dir=self.temp_dir
            )

    def test_markdown_template_content(self):
        """Test markdown template content generation"""
        report_data = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'metadata': {
                'report_version': '1.0'
            },
            'executive_summary': {
                'overall_health': 0.85,
                'quality_assessment': 'good',
                'executive_message': 'System shows good quality',
                'highlights': ['Excellent coverage'],
                'concerns': []
            },
            'metrics': {
                'composite_score': 0.85,
                'quality_level': 'good',
                'test_count': 100,
                'individual_metrics': {
                    'accuracy': {'value': 0.9, 'status': 'pass'}
                },
                'thresholds': {
                    'accuracy': 0.85
                }
            },
            'trends': {},
            'requirements': {},
            'architecture': {},
            'recommendations': []
        }

        markdown_template = self.generator._get_markdown_template()
        markdown_content = markdown_template(report_data)

        self.assertIn('# Quality Report', markdown_content)
        self.assertIn('Executive Summary', markdown_content)
        self.assertIn('Quality Metrics', markdown_content)
        self.assertIn('0.850', markdown_content)
        self.assertIn('Excellent coverage', markdown_content)

    def test_json_template_content(self):
        """Test JSON template content generation"""
        report_data = {
            'timestamp': '2023-01-01T00:00:00Z',
            'metadata': {'report_version': '1.0'},
            'metrics': {'composite_score': 0.85}
        }

        json_template = self.generator._get_json_template()
        json_content = json_template(report_data)

        parsed_json = json.loads(json_content)
        self.assertEqual(parsed_json['timestamp'], '2023-01-01T00:00:00Z')
        self.assertEqual(parsed_json['metrics']['composite_score'], 0.85)


if __name__ == '__main__':
    unittest.main()