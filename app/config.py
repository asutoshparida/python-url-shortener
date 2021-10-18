"""
config.py
~~~~~~~~
Module containing environment wise application configuration
"""
import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    CONFIG_NAME = "tests"
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    DEBUG = False
    TESTING = False


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}