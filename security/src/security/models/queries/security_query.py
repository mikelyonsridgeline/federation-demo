"""Defines SampleQuery"""
from pinecone.model.communication.connection_query import ConnectionQuery
from pinecone.model.communication.query import Query
from pinecone.model.fields import TextField
from security.models.results.security_result import SecurityResult


class SecurityQuery(ConnectionQuery):
    """SampleQuery for getting a SampleAggregate by its id."""

    field_name = "securities"

    class Meta:
        node = SecurityResult

