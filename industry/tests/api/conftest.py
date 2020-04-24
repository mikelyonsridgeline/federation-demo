import pytest
from pinecone.testing_utils.interface.graphql.integration import bearer_token


@pytest.fixture(scope="session", autouse=True)
def token():
    return bearer_token()
