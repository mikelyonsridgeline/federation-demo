"""Defines SampleQueryHandler"""
from typing import List

from pinecone.interface.handlers.connection_query_handler import ConnectionQueryHandler
from pinecone.interface.handlers.query_handler import QueryHandler
from pinecone.model.field_values.composite.composite import Composite
from pinecone.store import Repository

from security.models.aggregates.security_aggregate import SecurityAggregate
from security.models.queries.security_query import SecurityQuery
from security.models.results.security_result import SecurityResult


class SecurityQueryHandler(ConnectionQueryHandler):
    """Defines SampleQueryHandler for handling SampleQuery"""

    @staticmethod
    def handle_query(repository: Repository, **kwargs) -> List[SecurityResult]:
        """Handle a SampleQuery and return a SampleResult.

        Args:
            query (SecurityQuery): A query communication object.
            repository (Repository): Pinecone persistence object.

        Returns:
            result (SampleResult): A result commuication object.
        """
        securities = repository.reader.all(SecurityAggregate).all_results
        print(f"securities: {securities}")
        print(f"vars: {vars(securities[0])}")
        results = [
            SecurityResult(aggregate_id=security.aggregate_id,
                           ticker=security.ticker,
                           industry=Composite(aggregate_id=security.industry_id))
            for security in securities
        ]
        print(f"results: {results}")
        print(f"vars: {vars(results[0])}")
        return results

    @staticmethod
    def define_query_class():
        return SecurityQuery

    @staticmethod
    def define_output_type():
        return SecurityResult
