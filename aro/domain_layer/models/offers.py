import logging

from .base_handlers import CreateOffersContext, Handler
from aro.domain_layer.ports import (
    CreditProposalsService,
    OffersResult,
    ProposalsError,
    ProposalsErrorCodes,
    RefinOfferData
)
from aro.presentation_layer.mappings import CreateOffersRequestMapping


logger = logging.getLogger("aro")


class CreateOffersHandler(Handler):
    step_name = "create_offers"

    def __init__(self, api_credit_proposals_service: CreditProposalsService) -> None:
        super().__init__()
        self._service = api_credit_proposals_service

    def _create_refin_offers(self, offer: RefinOfferData) -> dict:
        return self._service.save_refin_offer(offer=offer)

    def _prepare_offer_data(self, offer: CreateOffersRequestMapping) -> RefinOfferData:
        return RefinOfferData(
            id=offer.id,
            user_uuid=offer.user_uuid,
            offered_at=offer.offered_at,
            expiration_at=offer.expiration_at,
            date_base_at=offer.date_base_at,
            iof_amount_cents=offer.iof_amount_cents,
            cet_am=offer.cet_am,
            cet_aa=offer.cet_aa,
            tax_am=offer.tax_am,
            tax_aa=offer.tax_aa,
            grace_period=offer.grace_period,
            deposit_amount_cents=offer.deposit_amount_cents,
            installments=offer.installments,
            monthly_amount_cents=offer.monthly_amount_cents,
            refinanced_amount_cents=offer.refinanced_amount_cents,
            previous_contract_id=offer.previous_contract_id,
            previous_partner_contract_id=offer.previous_partner_contract_id,
            product_type=offer.product_type,
            previous_deposit_at=offer.previous_deposit_at,
            with_disccount=offer.with_discount,
            trigger_at=offer.trigger_at
        )

    def _run(self, context: CreateOffersContext) -> None:
        if context.deny_step:
            return

        logger.info(
            f"Starting {self.step_name} handler",
            extra={
                "props": {
                    "id": context.request_data.id,
                    "user_uuid": context.request_data.user_uuid
                }
            }
        )

        offer = self._prepare_offer_data(offer=context.request_data)

        try:
            response = self._create_refin_offers(offer=offer)
        except ProposalsError as e:
            step_result = OffersResult.DENIED
            context.deny_code = ProposalsErrorCodes.REFIN901.name
            context.deny_description = ProposalsErrorCodes.REFIN901.value
            response = str(e)
        else:
            step_result = OffersResult.ACCEPTED

        context.set_step_result(self.step_name, step_result.name)

        logger.info(
            f"Finish {self.step_name} handler",
            extra={
                "props": {
                    "id": context.request_data.id,
                    "user_uuid": context.request_data.user_uuid,
                    "step_result": step_result.name,
                    "response": response
                }
            }
        )

        return response
