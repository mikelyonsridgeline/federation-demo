from pinecone.model.communication.connection_query import ConnectionQuery
from pinecone.model.communication.query import Query
from pinecone.model.fields import TextField, IDField


class IndustryById(Query):
    id: str
    sector: str

    class Meta:
        id = IDField(required=True)
        sector = TextField()
