import pytest

from aro import create_app
from aro.domain_layer.models import CreateOffersContext
from aro.domain_layer.ports import RefinOfferData
from aro.presentation_layer.mappings import CreateOffersRequestMapping


@pytest.fixture
def app():
    _app = create_app(deploy_env="Testing")

    with _app.app_context():
        yield _app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture
def api_credit_proposal_post_offer_payload():
    return {
        "id": "3aaf58bc-91ed-4f0e-a6dc-c482c90ec7f4",
        "user_uuid": "015c72fd902940c3aca39742494057e0",
        "offered_at": "2023-07-10",
        "expiration_at": "2023-07-11",
        "date_base_at": "2023-07-10",
        "iof_amount_cents": 3814,
        "cet_am": 5.7822506279127,
        "cet_aa": 98.1238172632,
        "tax_am": 4.43227378462,
        "tax_aa": 69.8796234963,
        "grace_period": 30,
        "deposit_amount_cents": 1000000,
        "installments": 12,
        "monthly_amount_cents": 43567,
        "refinanced_amount_cents": 1200000,
        "previous_contract_id": "L09525188UI",
        "previous_partner_contract_id": "123867123",
        "product_type": "REFIN",
        "previous_deposit_at": "2023-07-14",
        "with_discount": True,
        "trigger_at": "2023-7-10"
    }


@pytest.fixture
def refin_offer_data():
    return RefinOfferData(
        **{
            "id": "3aaf58bc-91ed-4f0e-a6dc-c482c90ec7f4",
            "user_uuid": "015c72fd902940c3aca39742494057e0",
            "offered_at": "2023-07-10",
            "expiration_at": "2023-07-11",
            "date_base_at": "2023-07-10",
            "iof_amount_cents": 3814,
            "cet_am": 5.7822506279127,
            "cet_aa": 98.1238172632,
            "tax_am": 4.43227378462,
            "tax_aa": 69.8796234963,
            "grace_period": 30,
            "deposit_amount_cents": 1000000,
            "installments": 12,
            "monthly_amount_cents": 43567,
            "refinanced_amount_cents": 1200000,
            "previous_contract_id": "L09525188UI",
            "previous_partner_contract_id": "123867123",
            "product_type": "REFIN",
            "previous_deposit_at": "2023-07-14",
            "with_disccount": True,
            "trigger_at": "2023-7-10"
        }
    )


@pytest.fixture
def api_credit_proposal_post_offer_url():
    return "http://api-credit-proposals-service.test.com/v1/refinancing/offers"


@pytest.fixture
def api_credit_proposal_post_offer_mapping(api_credit_proposal_post_offer_payload):
    return CreateOffersRequestMapping(payload=api_credit_proposal_post_offer_payload)


@pytest.fixture
def create_offers_context(api_credit_proposal_post_offer_mapping):
    return CreateOffersContext(request_data=api_credit_proposal_post_offer_mapping)
