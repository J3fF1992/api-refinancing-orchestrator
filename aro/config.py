from os import getenv

import logging


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    DEPLOY_ENV = getenv("DEPLOY_ENV", default="Development")
    LOGS_LEVEL = logging.INFO


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class StagingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    LOGS_LEVEL = getenv("DEPLOY_ENV", default=logging.INFO)
