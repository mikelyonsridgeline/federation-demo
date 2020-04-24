from datetime import date

from tools.rl_validator import RLValidator


def test_greater_than_schema_validation_success():
    schema = {"a": {"type": "date"}, "b": {"type": "date", "greater_than": "a"}}

    data = {"a": date(2019, 12, 31), "b": date(2020, 1, 1)}

    validator = RLValidator(schema)
    assert validator(data) is True


def test_greater_than_schema_validation_fail():
    schema = {"a": {"type": "date"}, "b": {"type": "date", "greater_than": "a"}}

    data = {"b": date(2019, 12, 31), "a": date(2020, 1, 1)}

    validator = RLValidator(schema)
    assert validator(data) is False
