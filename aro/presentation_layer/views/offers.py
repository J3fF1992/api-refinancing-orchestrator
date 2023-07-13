from flask import Blueprint, request
from flask_restx import Api, Resource

from aro.application_layer.use_cases import OffersUseCase
from aro.domain_layer.ports import OffersResult
from aro.presentation_layer.mappings import CreateOffersRequestMapping
from aro.presentation_layer.schemas import (
    create_offers_model,
    create_offers_response_model,
    generic_response_model
)
from .api import DOC, VERSION

blueprint = Blueprint("offers", __name__, url_prefix="/v1/offers")

api = Api(
    blueprint,
    version=VERSION,
    title="Api Refinancing Orchestrator",
    description=f"{DOC} - Offers",
    doc="/docs/swagger"
)

ns = api.namespace("", description=DOC)

ns.add_model(create_offers_model.name, create_offers_model)
ns.add_model(create_offers_response_model.name, create_offers_response_model)
ns.add_model(generic_response_model.name, generic_response_model)


@ns.route("")
class Offers(Resource):
    @ns.expect(create_offers_model)
    @ns.response(200, "OK", create_offers_response_model)
    @ns.response(400, "Bad Request", generic_response_model)
    def post(self) -> tuple[dict, int]:
        mapping = CreateOffersRequestMapping(payload=request.json)

        try:
            result_decision, result_data = OffersUseCase.create_refin_offers(request_data=mapping)
        except Exception as e:
            return {
                "code": "400",
                "message": str(e)
            }, 400

        if result_decision == OffersResult.DENIED:
            return result_data, 400

        return result_data, 200
