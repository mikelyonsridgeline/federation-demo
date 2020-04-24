from pinecone.model.fields import TextField
from pinecone.utils.class_utils import get_user_defined_attributes
from pinecone.utils.model_factory import ModelFactory

from service_template.models.commands.sample_command import SampleCommand


def test_sample_command_meta():
    attributes = get_user_defined_attributes(SampleCommand.Meta)

    assert len(attributes) == 1

    assert isinstance(SampleCommand.Meta.sample_text_field, TextField)

    assert SampleCommand.Meta.sample_text_field.required

    assert not SampleCommand.Meta.sample_text_field.is_indexed


def test_sample_command_instantiate():
    model_factory = ModelFactory(SampleCommand)
    init_dict = model_factory.generate_init_dict()
    instance = SampleCommand(**init_dict)

    assert instance.sample_text_field == init_dict["sample_text_field"]
