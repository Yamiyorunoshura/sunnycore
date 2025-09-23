"""
Security Testing Types and Enums

This module defines the core types and enums used throughout the security testing framework.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union


class VulnerabilityType(Enum):
    """OWASP LLM Top-10 Vulnerability Types"""

    LLM01_PROMPT_INJECTION = "LLM01: Prompt Injection"
    LLM02_INSECURE_OUTPUT = "LLM02: Insecure Output Handling"
    LLM03_DATA_POISONING = "LLM03: Training Data Poisoning"
    LLM04_MODEL_DENIAL_OF_SERVICE = "LLM04: Model Denial of Service"
    LLM05_SUPPLY_CHAIN = "LLM05: Supply Chain Vulnerabilities"
    LLM06_SENSITIVE_INFO_DISCLOSURE = "LLM06: Sensitive Information Disclosure"
    LLM07_INSECURE_PLUGIN = "LLM07: Insecure Plugin Design"
    LLM08_EXCESSIVE_AGENCY = "LLM08: Excessive Agency"
    LLM09_OVERRELIANCE = "LLM09: Overreliance"
    LLM10_MODEL_THEFT = "LLM10: Model Theft"
    PRIVILEGE_ESCALATION = "Privilege Escalation"
    SYSTEM_PROMPT_LEAKAGE = "System Prompt Leakage"


class SeverityLevel(Enum):
    """Security vulnerability severity levels"""

    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    INFO = "Informational"


class TestStatus(Enum):
    """Security test execution status"""

    PENDING = "Pending"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"
    SKIPPED = "Skipped"


@dataclass
class SecurityTestResult:
    """Result of a security test execution"""

    test_id: str
    vulnerability_type: VulnerabilityType
    test_name: str
    status: TestStatus
    severity: SeverityLevel
    description: str
    timestamp: datetime
    execution_time: float
    detected: bool
    confidence_score: float
    details: Dict[str, Any] = field(default_factory=dict)
    recommendations: List[str] = field(default_factory=list)
    affected_components: List[str] = field(default_factory=list)


@dataclass
class TestCase:
    """Security test case definition"""

    test_id: str
    name: str
    description: str
    vulnerability_type: VulnerabilityType
    severity: SeverityLevel
    input_data: Union[str, Dict[str, Any]]
    expected_behavior: str
    test_steps: List[str]
    prerequisites: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)


@dataclass
class SecurityMetrics:
    """Security testing metrics and KPIs"""

    total_tests: int
    passed_tests: int
    failed_tests: int
    skipped_tests: int
    vulnerabilities_detected: int
    critical_vulnerabilities: int
    high_vulnerabilities: int
    medium_vulnerabilities: int
    low_vulnerabilities: int
    attack_success_rate: float
    average_execution_time: float
    coverage_percentage: float
    last_updated: datetime


@dataclass
class IsolationEnvironment:
    """Containerized isolation environment configuration"""

    container_id: str
    environment_type: str
    network_isolated: bool
    resource_limits: Dict[str, Any]
    status: str
    created_at: datetime
    last_reset: Optional[datetime] = None


@dataclass
class SecurityAlert:
    """Security monitoring alert"""

    alert_id: str
    alert_type: str
    severity: SeverityLevel
    message: str
    timestamp: datetime
    source_component: str
    details: Dict[str, Any]
    resolved: bool = False
    resolved_at: Optional[datetime] = None


@dataclass
class SecurityConfig:
    """Security testing configuration"""

    enable_prompt_injection_tests: bool = True
    enable_output_validation: bool = True
    enable_data_poisoning_tests: bool = True
    enable_privilege_escalation_tests: bool = True
    isolation_timeout: int = 300
    max_concurrent_tests: int = 5
    alert_thresholds: Dict[str, float] = field(default_factory=dict)
    monitoring_interval: int = 10
    log_level: str = "INFO"
