import pytest
from pinecone.testing_utils.interface.graphql.unit import create_mock_graphql_client
from pinecone.testing_utils.store.session import dynamodb_sessionfinish
from pinecone.testing_utils.store.session import dynamodb_sessionstart

from industry.models import query_handlers


@pytest.fixture(name="client")
def graphql_client():
    return create_mock_graphql_client(
        query_package=query_handlers
    )


@pytest.fixture(scope="module", autouse=True)
def setup_teardown_dynamodb_session(request):
    """Setup and tear down a dynamodb session for each testing run.
    "scope" may be changed as desired.
    """
    dynamodb_sessionstart()

    def teardown():
        dynamodb_sessionfinish()

    request.addfinalizer(teardown)
