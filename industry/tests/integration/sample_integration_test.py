from unittest.mock import MagicMock

from industry.models.aggregates.industry_aggregate import IndustryAggregate
from industry.models.results.industry_result import IndustryResult
from pinecone.store import Repository

from tests.resources.gql_constants import GraphQLSignatures
from tests.resources.gql_constants import GraphQLVariables


def test_integration_graphql(client):
    # Example integration test code below
    signature = GraphQLSignatures.SIGNATURE_STUB
    #
    # # Note to Devs: be sure to use the 'variables' keyword arg here. Relying on
    # # position will lead to unexpected behavior.
    from handlers import handle_api_seeding_lambda
    handle_api_seeding_lambda(None, {})
    actual_output = client.execute(signature, variables={})
    expected_output = {}
    #
    assert expected_output == actual_output


def test_federation(client):
    # Example integration test code below
    signature = GraphQLSignatures.FED_STUB
    variables_dict = GraphQLVariables.VARIABLE_STUB
    #
    # # Note to Devs: be sure to use the 'variables' keyword arg here. Relying on
    # # position will lead to unexpected behavior.
    from handlers import handle_api_seeding_lambda
    results = [IndustryResult(aggregate_id='test:5678', sector='Testing'), IndustryResult(aggregate_id='test:1234', sector='Testing')]
    class repo:
        class reader:
            @staticmethod
            def get(*args, **kwargs):
                return results.pop()

    Repository.get_instance = repo
    actual_output = client.execute(signature, variables=variables_dict)
    expected_output = {}
    #
    assert expected_output == actual_output

