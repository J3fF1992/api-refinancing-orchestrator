import logging

from aro.application_layer.adapters import ApiCreditProposalsService
from aro.domain_layer.models import (
    CreateOffersContext,
    CreateOffersHandler
)
from aro.domain_layer.ports import OffersResult
from aro.presentation_layer.mappings import CreateOffersRequestMapping


logger = logging.getLogger("aro")


class OffersUseCase():
    @classmethod
    def create_refin_offers(cls, request_data: CreateOffersRequestMapping) -> tuple[OffersResult, dict]:
        logger.info(
            "Create Refin Offers",
            extra={
                "props": {
                    "id": request_data.id,
                    "user_uuid": request_data.user_uuid
                }
            }
        )

        context = CreateOffersContext(request_data=request_data)

        create_offers_handler = CreateOffersHandler(
            api_credit_proposals_service=ApiCreditProposalsService
        )

        response = create_offers_handler.handle(context=context)

        if context.deny_step:
            denied_response = {
                "code": context.deny_code,
                "message": context.deny_description
            }
            logger.info(
                "Create Refin Offer Denied",
                extra={
                    "props": {
                        "id": request_data.id,
                        "user_uuid": request_data.user_uuid,
                        **denied_response,
                        "status": OffersResult.DENIED.name
                    }
                }
            )
            return OffersResult.DENIED, denied_response

        logger.info(
            "Create Refin Offers Accepted",
            extra={
                "props": {
                    "id": request_data.id,
                    "user_uuid": request_data.user_uuid
                }
            }
        )

        return OffersResult.ACCEPTED, response
