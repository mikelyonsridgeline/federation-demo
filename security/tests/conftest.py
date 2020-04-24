import os
from unittest.mock import MagicMock

import pytest
from aws_xray_sdk.core import xray_recorder
from pinecone.model.domain import SERVICE_ID
from pinecone.store import Repository
from pinecone.store._dynamo import ENDPOINT_URL
from pinecone.store._dynamo import EVENT_STORE
from pinecone.store._dynamo import PROJECTION_STORE
from pinecone.store._dynamo import REGION_NAME
from svalbard.dynamo_client import SvalbardDynamoClient
from svalbard.mocks.mock_lambda_context import mock_lambda_context

from tests.mocks.service_template.models.aggregates import *  # NOQA
from tests.mocks.service_template.models.commands import *  # NOQA
from tests.mocks.service_template.models.composite_fields import *  # NOQA
from tests.mocks.service_template.models.queries import *  # NOQA
from tests.mocks.service_template.models.results import *  # NOQA


@pytest.fixture()
def mock_svalbard_client(mocker):
    def mocked_init(self, context, region, endpoint_url=None):
        self._boto3_client = MagicMock()
        self._context = context
        return None

    mocker.patch.object(SvalbardDynamoClient, "__init__", mocked_init)
    context = mock_lambda_context()
    return SvalbardDynamoClient(context, os.environ[REGION_NAME])


@pytest.fixture(autouse=True, scope="session")
def mock_xray(request):
    xray_recorder.begin_segment("mock_segment")
    xray_recorder.begin_subsegment("mock_subsegment")

    def xray_teardown():
        xray_recorder.end_subsegment()
        xray_recorder.end_segment()

    request.addfinalizer(xray_teardown)


@pytest.fixture(autouse=True, scope="session")
def disable_xray(mock_xray):
    xray_recorder.configure(context_missing="LOG_ERROR")


@pytest.fixture(autouse=True, scope="session")
def mock_os_environ_variables():
    """Mocks the OS environ variables set by deploying onto AWS through
    the Serverless Framework.
    """
    os.environ["AWS_XRAY_SDK_ENABLED"] = "false"
    os.environ[PROJECTION_STORE] = "test_projection_store"
    os.environ[EVENT_STORE] = "test_event_store"
    os.environ[REGION_NAME] = "us-east-1"
    os.environ[ENDPOINT_URL] = "http://localhost:8000"
    os.environ[SERVICE_ID] = "srvc"


@pytest.fixture(autouse=True, scope="session")
def init_repository_with_mock_context(mock_os_environ_variables):

    try:
        Repository.get_instance()
    except Exception:
        context = mock_lambda_context()
        Repository(context)
