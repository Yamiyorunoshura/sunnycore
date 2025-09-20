"""
Multi-Stage Testing Framework

A comprehensive testing framework for validating requirements, architecture,
and implementation artifacts in software development pipelines.
"""

__version__ = "1.0.0"
__author__ = "Development Team"
__email__ = "dev@company.com"

from .validation.contract_validator import ContractValidator, ValidationResult

__all__ = [
    "ContractValidator",
    "ValidationResult",
]