from mock import mock

from aro.domain_layer.models import CreateOffersHandler
from aro.domain_layer.ports import (
    CreditProposalsService,
    ProposalsError,
    ProposalsErrorCodes
)


@mock.patch.object(CreditProposalsService, "save_refin_offer")
def test_create_refin_offers_must_call_save_refin_offer(
    mock_save_refin_offer,
    refin_offer_data
):
    expected_response = {"Mock result": "OK"}
    mock_save_refin_offer.return_value = expected_response

    create_offer_handler = CreateOffersHandler(api_credit_proposals_service=CreditProposalsService)
    response = create_offer_handler._create_refin_offers(offer=refin_offer_data)

    assert expected_response == response
    mock_save_refin_offer.assert_called_once_with(offer=refin_offer_data)


def test_prepare_offer_data_must_return_refin_offer_data(
    refin_offer_data,
    api_credit_proposal_post_offer_mapping
):
    create_offer_handler = CreateOffersHandler(api_credit_proposals_service=None)
    response = create_offer_handler._prepare_offer_data(offer=api_credit_proposal_post_offer_mapping)

    assert refin_offer_data == response


@mock.patch.object(CreateOffersHandler, "_prepare_offer_data")
def test_run_must_return_none_and_dont_run_implementation_when_deny_step_is_true(
    prepare_offer_data_mock,
    create_offers_context
):
    create_offers_context.handlers_history = {
        "step_1": "DENIED"
    }

    create_offer_handler = CreateOffersHandler(api_credit_proposals_service=None)
    response = create_offer_handler._run(context=create_offers_context)

    assert response is None
    prepare_offer_data_mock.assert_not_called()


@mock.patch.object(CreditProposalsService, "save_refin_offer")
def test_run_must_set_step_result_as_accepted_when_offer_is_saved_successfully(
    mock_save_refin_offer,
    create_offers_context,
    refin_offer_data
):
    expected_handler_history = {
        "create_offers": "ACCEPTED"
    }
    create_offer_handler = CreateOffersHandler(api_credit_proposals_service=CreditProposalsService)
    create_offer_handler._run(context=create_offers_context)

    assert create_offers_context.deny_description is None
    assert create_offers_context.deny_code is None
    assert expected_handler_history == create_offers_context.handlers_history
    mock_save_refin_offer.assert_called_once_with(offer=refin_offer_data)


@mock.patch.object(CreditProposalsService, "save_refin_offer")
def test_run_must_set_step_result_as_denied_when_proposals_error_is_raised(
    mock_save_refin_offer,
    create_offers_context,
    refin_offer_data
):
    expected_handler_history = {
        "create_offers": "DENIED"
    }
    mock_save_refin_offer.side_effect = ProposalsError("Oopsss")
    create_offer_handler = CreateOffersHandler(api_credit_proposals_service=CreditProposalsService)
    create_offer_handler._run(context=create_offers_context)

    assert ProposalsErrorCodes.REFIN901.value == create_offers_context.deny_description
    assert ProposalsErrorCodes.REFIN901.name == create_offers_context.deny_code
    assert expected_handler_history == create_offers_context.handlers_history
    mock_save_refin_offer.assert_called_once_with(offer=refin_offer_data)
