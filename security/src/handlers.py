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
from pinecone.lambda_handlers.handle_container_initialize import handle_container_initialize
from pinecone.lambda_handlers.handle_graphql import handle_graphql
from pinecone.lambda_handlers.handle_indexing import handle_indexing
from pinecone.lambda_handlers.handle_initialize import handle_initialize
from pinecone.store import Repository

from security.models import query_handlers

# ^^^ TODO DEV: Rename "security" to the name of your service above ^^^
from security.models.aggregates.security_aggregate import SecurityAggregate

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

from security import models
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


def handle_api_seeding_lambda(event, context):
    handle_initialize(event, context)
    securities = [
        SecurityAggregate(aggregate_id=SecurityAggregate.generate_id(), ticker="GOOG", industry_id="idty:industry:Ei3QrcCzT7GiEpGgbTdh4A=="),
        SecurityAggregate(aggregate_id=SecurityAggregate.generate_id(), ticker="FB", industry_id="idty:industry:Ei3QrcCzT7GiEpGgbTdh4A=="),
        SecurityAggregate(aggregate_id=SecurityAggregate.generate_id(), ticker="NFLX", industry_id="idty:industry:Ei3QrcCzT7GiEpGgbTdh4A=="),
        SecurityAggregate(aggregate_id=SecurityAggregate.generate_id(), ticker="OIL", industry_id="idty:industry:oKDFqSrNQfWqcQQZ6JxZYQ=="),
        SecurityAggregate(aggregate_id=SecurityAggregate.generate_id(), ticker="LULU", industry_id="idty:industry:rCIMEH7QTeCqzN9BVSRxFQ=="),
    ]

    LOGGER.info("Seeding Data Conversion Testing Service")
    repository = Repository.get_instance()
    repository.add_aggregates(securities)
    repository.commit()
    return success("Seeding successful.")

