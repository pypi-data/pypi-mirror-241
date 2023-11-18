# Mock YAML Specification
from datetime import datetime, time
from typing import Optional

import pytest
from pydantic import ValidationError

from notevault.create_schemas import generate_models_from_yaml


@pytest.fixture
def sample_yaml_spec():
    return {
        "General": {
            "start": {"type": "time", "nullable": True},
            "end": {"type": "time", "nullable": True},
            "breaks": {"type": "timedelta", "nullable": True},
            "timestamp": {"type": "datetime", "nullable": True},
            "date": {"type": "date", "nullable": True},
        },
        "Meeting": {
            "name": {"type": "string"},
            "start": {"type": "time"},
            "duration": {"type": "timedelta", "nullable": True},
            "minutes": {"type": "string", "nullable": True},
            "participants": {"type": "array", "nullable": True},
        },
    }


def test_correct_class_generation(sample_yaml_spec):
    generated_classes = generate_models_from_yaml(sample_yaml_spec)
    assert "General" in generated_classes
    assert "Meeting" in generated_classes


def test_field_type_mapping(sample_yaml_spec):
    generated_classes = generate_models_from_yaml(sample_yaml_spec)
    assert (
        str(generated_classes["General"].model_fields["start"].annotation)
        == "typing.Optional[datetime.time]"
    )
    assert (
        str(generated_classes["Meeting"].model_fields["name"].annotation)
        == "<class 'str'>"
    )


def test_nullable_fields(sample_yaml_spec):
    generated_classes = generate_models_from_yaml(sample_yaml_spec)
    assert generated_classes["General"].model_fields["start"].is_required() is False
    assert generated_classes["Meeting"].model_fields["name"].is_required()


def test_non_nullable_fields(sample_yaml_spec):
    generated_classes = generate_models_from_yaml(sample_yaml_spec)
    with pytest.raises(ValidationError):
        generated_classes["Meeting"](**{"name": None})  # Name is a non-nullable field
