from unittest.mock import MagicMock

from pinecone.store import Repository
from pinecone.testing_utils.constants import PineconeTestingConstants

from service_template.models.aggregates.sample_aggregate import SampleAggregate
from service_template.models.queries.sample_query import SampleQuery
from service_template.models.query_handlers.sample_query_handler import (
    SampleQueryHandler,
)
from service_template.models.results.sample_result import SampleResult


def test_sample_query_handler_handle_query(mocker):
    expected_aggregate_id = "mock_id"
    sample_query = SampleQuery(**{"aggregate_id": expected_aggregate_id})
    repository = Repository.get_instance()

    mocker.patch(
        PineconeTestingConstants.GENERATE_ID_PATH, return_value=expected_aggregate_id
    )
    repository.reader.get = MagicMock(
        return_value=SampleAggregate(
            **{
                "sample_text_field": "sample_text_field_value",
                "aggregate_id": expected_aggregate_id,
            }
        )
    )

    result = SampleQueryHandler.handle_query(sample_query, repository)
    assert isinstance(result, SampleResult)
    assert result.sample_text_field == "sample_text_field_value"
    assert result.aggregate_id == expected_aggregate_id


def test_sample_query_handler_query_class():
    assert SampleQueryHandler.define_query_class() == SampleQuery


def test_sample_query_handler_define_output_type():
    assert SampleQueryHandler.define_output_type() == SampleResult
