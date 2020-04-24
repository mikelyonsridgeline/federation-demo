from unittest.mock import MagicMock
from unittest.mock import call

from tools.rl_validator import RLValidator
from tools.rl_validator import ValidationException


def test_validate_greater_than_success():
    mock_validator = MagicMock()
    mock_validator.document = {"other_field": 0}

    RLValidator._validate_greater_than(mock_validator, "other_field", "this_field", 1)
    assert mock_validator.__error.call_count == 0


def test_validate_greater_than_field_not_present():
    mock_validator = MagicMock()
    mock_validator.document = {"not_other_field": 0}

    RLValidator._validate_greater_than(mock_validator, "other_field", "this_field", 1)
    assert mock_validator._error.call_count == 1
    assert mock_validator._error.mock_calls[0] == call(
        "this_field", "other_field is not in document"
    )


def test_validate_greater_than_this_field_not_greater_than_other_field():
    mock_validator = MagicMock()
    mock_validator.document = {"other_field": 1}

    RLValidator._validate_greater_than(mock_validator, "other_field", "this_field", 0)
    assert mock_validator._error.call_count == 1
    assert mock_validator._error.mock_calls[0] == call(
        "this_field", "not greater than other_field"
    )


def test_validation_exception_init():
    test_errors = ["test_error_1", "test_error_2"]
    test_validation_exception = ValidationException(test_errors)
    assert test_validation_exception.args[0] == "['test_error_1', 'test_error_2']"
