from pinecone.model.fields import TextField
from pinecone.utils.class_utils import get_user_defined_attributes
from pinecone.utils.model_factory import ModelFactory

from service_template.models.results.sample_result import SampleResult


def test_sample_result_meta():
    attributes = get_user_defined_attributes(SampleResult.Meta)

    assert len(attributes) == 2

    assert isinstance(SampleResult.Meta.aggregate_id, TextField)
    assert isinstance(SampleResult.Meta.sample_text_field, TextField)

    assert SampleResult.Meta.aggregate_id.required
    assert SampleResult.Meta.sample_text_field.required

    assert not SampleResult.Meta.aggregate_id.is_indexed
    assert not SampleResult.Meta.sample_text_field.is_indexed


def test_sample_result_instantiate():
    model_factory = ModelFactory(SampleResult)
    init_dict = model_factory.generate_init_dict()
    instance = SampleResult(**init_dict)

    assert instance.aggregate_id == init_dict["aggregate_id"]
    assert instance.sample_text_field == init_dict["sample_text_field"]
