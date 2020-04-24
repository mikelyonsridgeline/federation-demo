import pytest

# from pinecone.testing_utils.interface.graphql.integration import gql_request
#
# from tests.resources.gql_constants import GraphQLSignatures
# from tests.resources.gql_constants import GraphQLVariables


@pytest.fixture
def url():
    # TODO: working with devs on a more elegant solution for this.
    # TODO Dev: Replace this url with the endpoint of your deployed service.
    return f"https://q6sdq9fjel.execute-api.us-east-1.amazonaws.com/stage/service-template/graphql"


def test_api_graphql(url, token):
    # Sample example of an api test below
    # signature = GraphQLSignatures.SIGNATURE_STUB
    # variables = GraphQLVariables.VARIABLE_STUB
    #
    # response = gql_request(url, token, signature, variables)
    # json_response = response.json()

    # assert json_response["data"]
    # And other asserts about the response.

    assert True
