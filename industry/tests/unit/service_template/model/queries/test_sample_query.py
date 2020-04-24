from pinecone.model.fields import TextField
from pinecone.utils.class_utils import get_user_defined_attributes
from pinecone.utils.model_factory import ModelFactory

from service_template.models.queries.sample_query import SampleQuery


def test_sample_query_meta():
    attributes = get_user_defined_attributes(SampleQuery.Meta)

    assert len(attributes) == 1

    assert isinstance(SampleQuery.Meta.aggregate_id, TextField)

    assert SampleQuery.Meta.aggregate_id.required

    assert not SampleQuery.Meta.aggregate_id.is_indexed


def test_sample_query_instantiate():
    model_factory = ModelFactory(SampleQuery)
    init_dict = model_factory.generate_init_dict()
    instance = SampleQuery(**init_dict)

    assert instance.aggregate_id == init_dict["aggregate_id"]
