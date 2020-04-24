"""Defines SampleQuery"""
from pinecone.model.communication.connection_query import ConnectionQuery

from industry.models.results.industry_result import IndustryResult
from pinecone.model.communication.query import Query
from pinecone.model.fields import TextField


class AllIndustriesQuery(ConnectionQuery):
    """SampleQuery for getting a SampleAggregate by its id."""

    field_name = "industries"

    class Meta:
        node = IndustryResult


class IndustryById(Query):

    class Meta:
        aggregate_id = TextField()
