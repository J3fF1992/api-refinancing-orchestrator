import logging
from http import HTTPStatus

import requests
from flask import current_app

from aro.domain_layer.ports import (
    CreditProposalsService,
    RefinOfferData,
    ProposalsError
)


logger = logging.getLogger("aro")


class ApiCreditProposalsService(CreditProposalsService):
    @classmethod
    def save_refin_offer(cls, offer: RefinOfferData) -> dict:
        path = "/v1/refinancings/offers"
        url = f"{current_app.config['API_CREDIT_PROPOSALS_SERVICES_URI']}{path}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {current_app.config['API_CREDIT_PROPOSALS_SERVICES_KEY']}"
        }

        logger.info(
            "Save Refin Offer",
            extra={
                "props": {
                    "service": "ApiCreditProposalsService",
                    "service_method": "save_refin_offer",
                    "url": url,
                    "method": "POST",
                    "payload": offer
                }
            }
        )

        try:
            response = requests.post(
                url=url,
                headers=headers,
                json=offer
            )
        except Exception as e:
            logger.error(
                "Save Refin Offer Exception",
                extra={
                    "props": {
                        "service": "ApiCreditProposalsService",
                        "service_method": "save_refin_offer",
                        "url": url,
                        "method": "POST",
                        "payload": offer,
                        "error_message": str(e)
                    }
                }
            )
            raise ProposalsError(f"Save Reffin Offer Exception - {str(e)}")

        if response.status_code != HTTPStatus.CREATED:
            logger.info(
                "Save Refin Offer Error",
                extra={
                    "props": {
                        "service": "ApiCreditProposalsService",
                        "service_method": "save_refin_offer",
                        "url": url,
                        "method": "POST",
                        "payload": offer,
                        "status_code": response.status_code,
                        "response_text": response.text
                    }
                }
            )
            raise ProposalsError(f"Save Reffin Offer Error - status_code: {response.status_code}")

        logger.info(
            "Save Refin Offer Successfully",
            extra={
                "props": {
                    "service": "ApiCreditProposalsService",
                    "service_method": "save_refin_offer",
                    "url": url,
                    "method": "POST",
                    "payload": offer,
                    "response_text": response.text
                }
            }
        )
        return response.json()
