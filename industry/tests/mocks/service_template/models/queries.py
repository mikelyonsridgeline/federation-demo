import pytest as ptest


@ptest.fixture()
def sample_query_dict():
    return {"aggregate_id": "test_aggregate_id"}
