"""This module acts as an entry point for all lambda handlers defined in
serverless.yml. These handler functions should avoid including any business
logic directly. Instead, import and invoke functions from other areas here.
For performance reasons, it is also better to set any global state here, for
anything that requires IO connections. AWS will cache global vars defined
here and reuse them across all of the lambdas during runtime.
"""

import logging
import os

from http_responses import success
from http_responses.graphql.handle_response import handle_response
from pinecone.lambda_handlers.handle_container_initialize import (
    handle_container_initialize,
)
from pinecone.lambda_handlers.handle_graphql import handle_graphql
from pinecone.lambda_handlers.handle_indexing import handle_indexing
# ^^^ TODO DEV: Rename "industry" to the name of your service above ^^^
from pinecone.lambda_handlers.handle_initialize import handle_initialize
from pinecone.store import Repository

from industry import models
from industry.models import query_handlers
from industry.models.aggregates.industry_aggregate import IndustryAggregate

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
LOGGER.info("booting up")


handle_container_initialize(models)


def handle_graphql_lambda(event, context):
    result = handle_graphql(event, context, [query_handlers])
    return handle_response(result, LOGGER)


def handle_indexing_lambda(event, context):
    return handle_indexing(event, context)


# pylint: disable=unused-argument
def handle_health(event, context):
    """
    Handler for responding to health requests.  Update the env variable STATUS to failover
    """
    LOGGER.info("Received event in handle_health:")
    response = {"statusCode": os.environ["STATUS"]}
    return response


def make_tables():
    repository = Repository.get_instance()
    atts = [
        {"AttributeName": "pk", "AttributeType": "S"},
        {"AttributeName": "sk", "AttributeType": "S"},
    ]
    key_schema = [
        {"AttributeName": "pk", "KeyType": "HASH"},
        {"AttributeName": "sk", "KeyType": "RANGE"},
    ]
    repository._repository._dynamo_client.create_table(
        TableName="IndustryFed-mikelyons-projections",
        AttributeDefinitions=atts,
        KeySchema=key_schema,
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
    )

    atts = [
        {"AttributeName": "pk", "AttributeType": "S"},
        {"AttributeName": "sk", "AttributeType": "S"},
    ]
    key_schema = [
        {"AttributeName": "pk", "KeyType": "HASH"},
        {"AttributeName": "sk", "KeyType": "RANGE"},
    ]
    print(f"AttributeDefinitions: {atts} KeySchema: {key_schema}")
    repository._repository._dynamo_client.create_table(
        TableName="IndustryFed-mikelyons-events",
        AttributeDefinitions=atts,
        KeySchema=key_schema,
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
    )
    print(f"made tables")


def handle_api_seeding_lambda(event, context):
    handle_initialize(event, context)
    try:
        make_tables()
    except Exception as e:
        print(f"exception: {e}")
    industries = [
        IndustryAggregate(aggregate_id=IndustryAggregate.generate_id(), sector=i)
        for i in """
       Energy
       Materials
       Industrials
       Consumer
       Discretionary
       Consumer
       Staples
       Health
       Care
       Financials
       Information
       Technology
       Telecommunication
       Services
       Utilities
       Real
       Estate
       """.split()
    ]
    LOGGER.info("Seeding Data Conversion Testing Service")
    repository = Repository.get_instance()
    repository.add_aggregates(industries)
    repository.commit()
    return success("Seeding successful.")
