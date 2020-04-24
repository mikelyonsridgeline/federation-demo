"""Defines SampleQueryHandler"""
from pinecone.interface.handlers.connection_query_handler import ConnectionQueryHandler
from pinecone.store import Repository

from industry.models.aggregates.industry_aggregate import IndustryAggregate
from industry.models.queries.all_industries_query import AllIndustriesQuery
from industry.models.results.industry_result import IndustryResult


class AllIndustriesQueryHandler(ConnectionQueryHandler):
    """Defines SampleQueryHandler for handling SampleQuery"""

    @staticmethod
    def handle_query(repository: Repository, **kwargs) -> IndustryResult:
        """Handle a SampleQuery and return a SampleResult.

        Args:
            query (AllIndustriesQuery): A query communication object.
            repository (Repository): Pinecone persistence object.

        Returns:
            result (SampleResult): A result commuication object.
        """
        industries = repository.reader.all(IndustryAggregate).all_results
        print(f"industries: {industries}")
        return [
            IndustryResult(aggregate_id=industry.aggregate_id, sector=industry.sector)
            for industry in industries
        ]


    @staticmethod
    def define_query_class():
        return AllIndustriesQuery

    @staticmethod
    def define_output_type():
        return IndustryResult


