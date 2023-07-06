import logging
from os import getenv
import sys

import json_logging
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS


load_dotenv()

ENV = getenv("DEPLOY_ENV", default="Development")


def create_app(deploy_env: str = ENV) -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(f"aro.config.{deploy_env}Config")

    _configure_logger(app=app)

    return app


def _configure_logger(app: Flask) -> None:
    if not json_logging.ENABLE_JSON_LOGGING:
        json_logging.init_flask(enable_json=True)
        json_logging.init_request_instrument(app=app)

    logger = logging.getLogger("aro")
    logger.setLevel(app.config["LOGS_LEVEL"])

    if not logger.hasHandlers():
        logger.addHandler(logging.StreamHandler(sys.stdout))
