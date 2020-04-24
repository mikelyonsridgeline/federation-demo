"""This module defines SampleAggregate"""

from pinecone.model.domain.aggregate_root import AggregateRoot
from pinecone.model.fields import TextField


class SecurityAggregate(AggregateRoot):
    """A sample aggregate definition."""

    ticker: str

    class Meta:
        ticker = TextField()
        industry_id = TextField()  # think about how to better do this
