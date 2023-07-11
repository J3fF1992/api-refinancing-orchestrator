import pytest

from aro.domain_layer.ports import CreditProposalsService


def test_save_refin_offer_must_raise_not_implemented_error():
    with pytest.raises(NotImplementedError):
        CreditProposalsService.save_refin_offer(None)
