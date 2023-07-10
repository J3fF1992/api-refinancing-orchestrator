from abc import ABC
from enum import auto, Enum
from typing import TypedDict


class ProposalsError(Exception):
    pass


class ProposalsErrorCodes(Enum):
    REFIN901 = "Request error to Proposals Service"


class OffersResult(Enum):
    ACCEPTED = auto()
    DENIED = auto()


class RefinOfferData(TypedDict):
    id: str
    user_uuid: str
    offered_at: str
    expiration_at: str
    date_base_at: str
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
    previous_deposit_at: str
    with_disccount: bool
    trigger_at: str


class CreditProposalsService(ABC):
    @classmethod
    def save_refin_offer(cls, offer: RefinOfferData) -> dict:
        raise NotImplementedError
