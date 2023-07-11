import pytest
from mock import mock

from aro.application_layer.use_cases import OffersUseCase
from aro.application_layer.adapters import ApiCreditProposalsService
from aro.domain_layer.ports import (
    OffersResult,
    ProposalsError,
    ProposalsErrorCodes
)


@mock.patch.object(ApiCreditProposalsService, "save_refin_offer")
def test_create_refin_offers_must_return_accepted_when_offer_is_created_successfully(
    save_refin_offer_mock,
    app,
    api_credit_proposal_post_offer_mapping
):
    expected_data_response = {"id": "3aaf58bc-91ed-4f0e-a6dc-c482c90ec7f4"}
    save_refin_offer_mock.return_value = expected_data_response

    response_status, response_data = OffersUseCase.create_refin_offers(api_credit_proposal_post_offer_mapping)

    assert OffersResult.ACCEPTED == response_status
    assert expected_data_response == response_data
    save_refin_offer_mock.assert_called_once()


@mock.patch.object(ApiCreditProposalsService, "save_refin_offer")
def test_create_refin_offers_must_return_denied_when_offer_is_not_created(
    save_refin_offer_mock,
    app,
    api_credit_proposal_post_offer_mapping
):
    expected_data_response = {
        "code": ProposalsErrorCodes.REFIN901.name,
        "message": ProposalsErrorCodes.REFIN901.value
    }
    save_refin_offer_mock.side_effect = ProposalsError("Mock Error")

    response_status, response_data = OffersUseCase.create_refin_offers(api_credit_proposal_post_offer_mapping)

    assert OffersResult.DENIED == response_status
    assert expected_data_response == response_data
    save_refin_offer_mock.assert_called_once()


@mock.patch.object(ApiCreditProposalsService, "save_refin_offer")
def test_create_refin_offers_must_raise_exception_when_some_unknown_exception_is_raised(
    save_refin_offer_mock,
    app,
    api_credit_proposal_post_offer_mapping
):
    save_refin_offer_mock.side_effect = Exception("Oooohh Nooo")

    with pytest.raises(Exception) as e:
        OffersUseCase.create_refin_offers(api_credit_proposal_post_offer_mapping)

    assert "Oooohh Nooo" == str(e.value)
