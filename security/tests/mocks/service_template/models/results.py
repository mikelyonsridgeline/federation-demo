import pytest as ptest


@ptest.fixture()
def sample_result_dict():
    return {
        "aggregate_id": "test_aggregate_id",
        "sample_text_field": "test_sample_text_field",
    }
