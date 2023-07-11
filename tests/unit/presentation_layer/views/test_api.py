from aro.presentation_layer.views.api import (
    Index,
    VERSION,
    DOC
)


def test_health_check_must_return_a_dict_and_status_code_200():
    expected_response = {
        "service": DOC,
        "version": VERSION
    }, 200

    result = Index().get()

    assert expected_response == result
