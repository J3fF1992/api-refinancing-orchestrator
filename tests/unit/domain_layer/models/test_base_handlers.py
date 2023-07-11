import pytest
from mock import mock

from aro.domain_layer.models.base_handlers import Handler


def test_handler_set_next_must_set_handler_successfully():
    handler = Handler()
    next_handler = Handler()

    handler.set_next(next_handler=next_handler)

    assert next_handler == handler.next


def test_handler_run_must_raise_not_implemented_error():
    handler = Handler()

    with pytest.raises(NotImplementedError):
        handler._run()


@mock.patch.object(Handler, "_run")
def test_handler_handle_must_return_result_when_some_result_is_returned(run_mock):
    expected_response = {"Result": "OK"}
    run_mock.return_value = expected_response

    handle = Handler()
    handle_2 = Handler()

    handle.set_next(handle_2)
    result = handle.handle()

    assert expected_response == result
    run_mock.assert_called_once()


@mock.patch.object(Handler, "_run")
def test_handler_handle_must_be_called_3_times(run_mock):
    run_mock.return_value = None

    handle = Handler()
    handle_2 = Handler()
    handle_3 = Handler()

    handle.set_next(handle_2)
    handle_2.set_next(handle_3)
    result = handle.handle()

    assert result is None
    assert 3 == run_mock.call_count
