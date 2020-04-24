"""This module defines SampleResult."""
from pinecone.interface.graphql.federation import key
from pinecone.model.communication.result import Result
from pinecone.model.fields import TextField


@key(fields="aggregate_id")
class IndustryResult(Result):
    """A SampleResult"""

    aggregate_id: str
    sector: str

    class Meta:
        aggregate_id = TextField()
        sector = TextField()

    @staticmethod
    def resolve_reference():
        from industry.models.query_handlers.industry_by_id_handler import IndustryByIdHandler
        return IndustryByIdHandler

