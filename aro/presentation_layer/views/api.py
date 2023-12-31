from flask import Blueprint
from flask_restx import Api, Resource

from aro.presentation_layer.schemas import index_model


VERSION = "0.0.1"
DOC = "Api Refinancing Orchestrator"

blueprint = Blueprint("index", __name__)

api = Api(
    blueprint,
    version=VERSION,
    title="Api Refinancing Orchestrator",
    description=f"{DOC} - Index",
    doc="/docs/swagger"
)

ns = api.namespace("", description=DOC)

ns.add_model(index_model.name, index_model)


@ns.route("/health-status")
class Index(Resource):
    @ns.response(200, "OK", index_model)
    def get(self) -> tuple[dict, int]:
        return dict(
            service=DOC,
            version=VERSION
        ), 200
