from os import getenv

import logging


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    DEPLOY_ENV = getenv("DEPLOY_ENV", default="Development")
    LOGS_LEVEL = logging.INFO

    API_CREDIT_PROPOSALS_SERVICES_URI = getenv("API_CREDIT_PROPOSALS_SERVICES_URI")
    API_CREDIT_PROPOSALS_SERVICES_KEY = getenv("API_CREDIT_PROPOSALS_SERVICES_KEY")


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    API_CREDIT_PROPOSALS_SERVICES_URI = "https://api-credit-proposals-service.test.com"
    API_CREDIT_PROPOSALS_SERVICES_KEY = "api-credit-proposals-service-key-test"


class StagingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    LOGS_LEVEL = getenv("LOGS_LEVEL", default=logging.INFO)
