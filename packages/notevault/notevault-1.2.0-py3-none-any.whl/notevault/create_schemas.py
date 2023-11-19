from datetime import date, datetime, time, timedelta
from typing import List, NewType, Optional, Type

from pydantic import BaseModel, create_model

Content = NewType("Content", str)


class DocumentSchema(BaseModel):
    content: Content
    schemas: list[BaseModel]


def generate_models_from_yaml(model_spec: dict) -> dict[str, Type[BaseModel]]:
    """Generate Pydantic classes from YAML specs"""
    generated_classes = {}

    for model_name, fields in model_spec.items():
        field_definitions = {}
        for field_name, field_spec in fields.items():
            # Determine if the field is nullable (Optional)
            python_type = type_mapper(field_spec)
            # Set the field to be optional if specified, else it is required
            field_definitions[field_name] = (
                (python_type, ...)
                if field_spec.get("nullable") is not True
                else (python_type, None)
            )

        model_class = create_model(model_name, **field_definitions)
        generated_classes[model_name] = model_class

    return generated_classes


def type_mapper(type_spec: dict) -> type:
    """function to map YAML type specifications to Python types with optional handling"""
    type_mappings = {
        "time": time,
        "timedelta": timedelta,
        "datetime": datetime,
        "date": date,
        "string": str,
        "int": int,
        "float": float,
        "array": List[
            str
        ],  # Assuming array will always contain strings for this context
    }
    py_type = type_mappings[type_spec["type"]]
    if type_spec.get("nullable"):
        return Optional[py_type]
    return py_type
