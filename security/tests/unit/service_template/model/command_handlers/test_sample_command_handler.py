from unittest.mock import MagicMock

from pinecone.store import Repository
from pinecone.testing_utils.constants import PineconeTestingConstants
from pinecone.utils.model_factory import ModelFactory

from service_template.models.aggregates.sample_aggregate import SampleAggregate
from service_template.models.command_handlers.sample_command_handler import (
    SampleCommandHandler,
)
from service_template.models.commands.sample_command import SampleCommand
from service_template.models.results.sample_result import SampleResult


def test_sample_command_handler_handle_command(mocker):
    model_factory = ModelFactory(SampleCommand)
    init_dict = model_factory.generate_init_dict()
    sample_command = SampleCommand(**init_dict)
    repository = Repository.get_instance()
    expected_aggregate_id = "mock_id"
    mocker.patch(
        PineconeTestingConstants.GENERATE_ID_PATH, return_value=expected_aggregate_id
    )
    repository.commit = MagicMock()
    repository.reader.get = MagicMock(
        return_value=SampleAggregate(
            **{
                "sample_text_field": sample_command.sample_text_field,
                "aggregate_id": expected_aggregate_id,
            }
        )
    )

    result = SampleCommandHandler.handle_command(sample_command, repository)
    assert isinstance(result, SampleResult)
    assert result.sample_text_field == init_dict["sample_text_field"]
    assert result.aggregate_id == expected_aggregate_id


def test_sample_command_handler_command_class():
    assert SampleCommandHandler.define_command_class() == SampleCommand


def test_sample_command_handler_define_output_type():
    assert SampleCommandHandler.define_output_type() == SampleResult
