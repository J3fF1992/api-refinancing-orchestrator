import uuid
from abc import ABC
from datetime import date
from typing import TypedDict


class ProposalsError(Exception):
    pass


class RefinOfferData(TypedDict):
    id: uuid
    user_uuid: str
    offered_at: date
    expiration_at: date
    date_base_at: date
    iof_amount_cents: int
    cet_am: float
    cet_aa: float
    tax_am: float
    tax_aa: float
    grace_period: int
    deposit_amount_cents: int
    installments: int
    monthly_amount_cents: int
    refinanced_amount_cents: int
    previous_contract_id: str
    previous_partner_contract_id: str
    product_type: str
    previous_deposit_date: date
    with_discount: bool
    trigger_at: date


class CreditProposalsService(ABC):
    @classmethod
    def save_refin_offer(cls, offer: RefinOfferData) -> dict:
        raise NotImplementedError
