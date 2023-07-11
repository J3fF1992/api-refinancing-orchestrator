import pytest
import responses

from aro.application_layer.adapters import ApiCreditProposalsService
from aro.domain_layer.ports import ProposalsError


@responses.activate
def test_save_refin_offer_must_return_id_when_request_return_201(
    app,
    api_credit_proposal_post_offer_payload,
    api_credit_proposal_post_offer_url
):
    expected_response = {"id": api_credit_proposal_post_offer_payload["id"]}

    responses.add(
        responses.POST,
        api_credit_proposal_post_offer_url,
        json=expected_response,
        status=201
    )

    response = ApiCreditProposalsService.save_refin_offer(api_credit_proposal_post_offer_payload)
    assert expected_response == response


@responses.activate
@pytest.mark.parametrize(
    "status_code",
    [
        200, 400, 500
    ]
)
def test_save_refin_offer_must_raise_proposals_error_when_request_return_non_status_code_201(
    status_code,
    app,
    api_credit_proposal_post_offer_url,
    api_credit_proposal_post_offer_payload
):
    responses.add(
        responses.POST,
        api_credit_proposal_post_offer_url,
        json={},
        status=status_code
    )

    with pytest.raises(ProposalsError) as e:
        ApiCreditProposalsService.save_refin_offer(api_credit_proposal_post_offer_payload)

    assert f"Save Reffin Offer Error - status_code: {status_code}" == str(e.value)


@responses.activate
def test_save_refin_offer_must_raise_proposaals_error_when_some_unknown_exception_is_raised(
    app,
    api_credit_proposal_post_offer_url,
    api_credit_proposal_post_offer_payload
):
    responses.add(
        responses.POST,
        api_credit_proposal_post_offer_url,
        body=Exception("Mock Error")
    )

    with pytest.raises(ProposalsError) as e:
        ApiCreditProposalsService.save_refin_offer(api_credit_proposal_post_offer_payload)

    assert "Save Reffin Offer Exception - Mock Error" == str(e.value)
