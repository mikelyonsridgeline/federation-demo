"""This module defines SampleAggregate"""

from pinecone.model.domain.aggregate_root import AggregateRoot
from pinecone.model.fields import TextField


class IndustryAggregate(AggregateRoot):
    """A sample aggregate definition."""

    sector: str

    class Meta:
        sector = TextField(required=True)
