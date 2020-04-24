import pytest as ptest


@ptest.fixture()
def sample_aggregate_dict():
    return {"sample_text_field": "test_sample_text_field"}
