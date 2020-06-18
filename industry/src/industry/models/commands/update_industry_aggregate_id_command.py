from pinecone.model.communication.command import Command
from pinecone.model.fields import TextField


class UpdateIndustryAggregateId(Command):

    class Meta:
        aggregate_id = TextField(required=True)
        new_id = TextField(required=True)
