from http import HTTPStatus

import responses
from mock import mock

from aro.application_layer.use_cases import OffersUseCase
from aro.domain_layer.ports import ProposalsErrorCodes


CREATE_OFFERS_ENDPOINT = "/v1/offers"


@responses.activate
def test_post_offers_must_return_offer_id_and_status_200_when_offer_is_created_successfully(
    client,
    api_credit_proposal_post_offer_payload,
    api_credit_proposal_post_offer_url
):
    expected_data = {"id": api_credit_proposal_post_offer_payload["id"]}

    responses.add(
        responses.POST,
        api_credit_proposal_post_offer_url,
        status=201,
        json=expected_data
    )

    response = client.post(
        CREATE_OFFERS_ENDPOINT,
        json=api_credit_proposal_post_offer_payload
    )

    assert HTTPStatus.OK == response.status_code
    assert expected_data == response.json


@responses.activate
def test_post_offers_must_return_code_refin901_status_400_when_offer_is_not_created_successfully(
    client,
    api_credit_proposal_post_offer_payload,
    api_credit_proposal_post_offer_url
):
    expected_data = {
        "code": ProposalsErrorCodes.REFIN901.name,
        "message": ProposalsErrorCodes.REFIN901.value
    }

    responses.add(
        responses.POST,
        api_credit_proposal_post_offer_url,
        status=400,
        json={}
    )

    response = client.post(
        CREATE_OFFERS_ENDPOINT,
        json=api_credit_proposal_post_offer_payload
    )

    assert HTTPStatus.BAD_REQUEST == response.status_code
    assert expected_data == response.json


@mock.patch.object(OffersUseCase, "create_refin_offers")
def test_post_offers_must_return_code_400_status_400_when_some_unknown_exception_is_raised(
    create_refin_offers_mock,
    client,
    api_credit_proposal_post_offer_payload
):
    create_refin_offers_mock.side_effect = Exception("Affff")
    expected_data = {
        "code": "400",
        "message": "Affff"
    }

    response = client.post(
        CREATE_OFFERS_ENDPOINT,
        json=api_credit_proposal_post_offer_payload
    )

    assert HTTPStatus.BAD_REQUEST == response.status_code
    assert expected_data == response.json
    create_refin_offers_mock.assert_called_once()
