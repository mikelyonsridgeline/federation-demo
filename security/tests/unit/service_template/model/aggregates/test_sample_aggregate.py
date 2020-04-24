from pinecone.model.fields import TextField
from pinecone.utils.class_utils import get_user_defined_attributes
from pinecone.utils.model_factory import ModelFactory

from service_template.models.aggregates.sample_aggregate import SampleAggregate


def test_sample_aggregate_meta():
    attributes = get_user_defined_attributes(SampleAggregate.Meta)

    assert len(attributes) == 1

    assert isinstance(SampleAggregate.Meta.sample_text_field, TextField)
    assert not SampleAggregate.Meta.sample_text_field.required
    assert not SampleAggregate.Meta.sample_text_field.is_indexed


def test_sample_aggregate_instantiate():
    model_factory = ModelFactory(SampleAggregate)
    init_dict = model_factory.generate_init_dict()
    init_dict["aggregate_id"] = SampleAggregate.generate_id()
    instance = SampleAggregate(**init_dict)

    assert instance.sample_text_field == init_dict["sample_text_field"]
