import pytest as ptest


@ptest.fixture()
def sample_command_dict():
    return {"sample_text_field": "test_sample_text_field"}
