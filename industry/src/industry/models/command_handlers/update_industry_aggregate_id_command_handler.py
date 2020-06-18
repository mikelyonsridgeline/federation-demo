"""Defines SampleCommandHandler to handle SampleCommand."""
from industry.models.aggregates.industry_aggregate import IndustryAggregate
from industry.models.commands.update_industry_aggregate_id_command import UpdateIndustryAggregateId
from industry.models.results.industry_result import IndustryResult
from pinecone.interface.handlers.command_handler import CommandHandler
from pinecone.store import Repository


class UpdateIndustryAggregateIdCommandHandler(CommandHandler):
    """SampleCommandHandler to handle SampleCommmand"""

    @classmethod
    def handle_command(
        cls, command: UpdateIndustryAggregateId, repository: Repository
    ) -> IndustryResult:
        """Handle a SampleCommand and return a SampleResult.
        Args:
            command (SampleCommand): A command communication object.
            repository (Repository): Pinecone persistence object.
        Returns:
            result (Result): A result commuication object.
        """
        industry = repository.reader.get(aggregate_class=IndustryAggregate, aggregate_id=command.aggregate_id)
        industry.aggregate_id = command.new_id
        repository.update_aggregate(industry)
        repository.commit()

        return IndustryResult(**vars(industry))

    @staticmethod
    def define_command_class():
        return UpdateIndustryAggregateId

    @staticmethod
    def define_output_type():
        return IndustryResult