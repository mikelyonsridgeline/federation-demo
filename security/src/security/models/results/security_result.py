"""This module defines SampleResult."""
from graphene_federation import external
from pinecone.interface.graphql.federation import extend
from pinecone.model.communication.result import Result
from pinecone.model.fields import TextField, CompositeField


@extend(fields="aggregate_id")
class IndustryResultNode(CompositeField):
    """A SampleResult"""
    aggregate_id: str

    class Meta:
        aggregate_id = external(TextField())
        some_nique_field = TextField()


class SecurityResult(Result):
    """A SampleResult"""

    aggregate_id: str

    class Meta:
        aggregate_id = TextField(required=True)
        ticker = TextField()
        industry = IndustryResultNode()
