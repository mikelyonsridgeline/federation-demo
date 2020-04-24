"""Defines SampleQueryHandler"""
from industry.models.queries.industry_by_id import IndustryById
from pinecone.interface.handlers.connection_query_handler import ConnectionQueryHandler
from pinecone.interface.handlers.query_handler import QueryHandler
from pinecone.store import Repository

from industry.models.aggregates.industry_aggregate import IndustryAggregate


class IndustryByIdHandler(QueryHandler):
    """Defines SampleQueryHandler for handling SampleQuery"""

    @staticmethod
    def handle_query(query, repository: Repository, **kwargs):
        from industry.models.results.industry_result import IndustryResult
        """Handle a SampleQuery and return a SampleResult.

        Args:
            query (AllIndustriesQuery): A query communication object.
            repository (Repository): Pinecone persistence object.

        Returns:
            result (SampleResult): A result commuication object.
        """
        industry = repository.reader.get(aggregate_class=IndustryAggregate, aggregate_id=query.aggregate_id)
        try:
            result = IndustryResult(aggregate_id=industry.aggregate_id, sector=industry.sector)
            return result
        except AttributeError:
            return None

    @staticmethod
    def define_query_class():
        return IndustryById

    @staticmethod
    def define_output_type():
        from industry.models.results.industry_result import IndustryResult
        return IndustryResult


