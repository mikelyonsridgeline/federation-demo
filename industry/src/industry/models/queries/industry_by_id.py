from pinecone.model.communication.connection_query import ConnectionQuery
from pinecone.model.communication.query import Query
from pinecone.model.fields import TextField


class IndustryById(Query):
    aggregate_id: str
    sector: str

    class Meta:
        aggregate_id = TextField()
        sector = TextField()
