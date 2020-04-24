from industry.models.results.industry_result import IndustryResult
from pinecone.model.communication.connection_query import ConnectionQuery
from pinecone.model.communication.query import Query
from pinecone.model.fields import TextField


class IndustryById(Query):


    class Meta:

        aggregate_id = TextField()
