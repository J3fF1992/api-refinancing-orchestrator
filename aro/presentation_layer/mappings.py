class PayloadMapping:
    def __init__(self, *, payload: dict) -> None:
        self.payload = payload


class CreateOffersRequestMapping(PayloadMapping):
    @property
    def id(self) -> str:
        return self.payload.get("id")

    @property
    def user_uuid(self) -> str:
        return self.payload.get("user_uuid")

    @property
    def offered_at(self) -> str:
        return self.payload.get("offered_at")

    @property
    def expiration_at(self) -> str:
        return self.payload.get("expiration_at")

    @property
    def date_base_at(self) -> str:
        return self.payload.get("date_base_at")

    @property
    def iof_amount_cents(self) -> int:
        return self.payload.get("iof_amount_cents")

    @property
    def cet_am(self) -> float:
        return self.payload.get("cet_am")

    @property
    def cet_aa(self) -> float:
        return self.payload.get("cet_aa")

    @property
    def tax_am(self) -> float:
        return self.payload.get("tax_am")

    @property
    def tax_aa(self) -> float:
        return self.payload.get("tax_aa")

    @property
    def grace_period(self) -> int:
        return self.payload.get("grace_period")

    @property
    def deposit_amount_cents(self) -> int:
        return self.payload.get("deposit_amount_cents")

    @property
    def installments(self) -> int:
        return self.payload.get("installments")

    @property
    def monthly_amount_cents(self) -> int:
        return self.payload.get("monthly_amount_cents")

    @property
    def refinanced_amount_cents(self) -> int:
        return self.payload.get("refinanced_amount_cents")

    @property
    def previous_contract_id(self) -> str:
        return self.payload.get("previous_contract_id")

    @property
    def previous_partner_contract_id(self) -> str:
        return self.payload.get("previous_partner_contract_id")

    @property
    def product_type(self) -> str:
        return self.payload.get("product_type")

    @property
    def previous_deposit_date(self) -> str:
        return self.payload.get("previous_deposit_date")

    @property
    def with_discount(self) -> bool:
        return self.payload.get("with_discount")

    @property
    def trigger_at(self) -> str:
        return self.payload.get("trigger_at")
