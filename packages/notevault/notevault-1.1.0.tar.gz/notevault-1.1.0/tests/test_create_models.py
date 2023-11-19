from datetime import date, datetime, time, timedelta
from typing import List, Optional

import pytest
from pydantic import BaseModel
from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    Integer,
    Interval,
    String,
    Time,
)
from sqlalchemy.orm import declarative_base

from notevault.model.create_models import convert_instance_pydantic_to_sqlalchemy
from notevault.model.orm import Orm

# Test cases as (input, expected_output)
test_cases = [
    (int, Integer),
    (str, String),
    (float, Float),
    (bool, Boolean),
    (datetime, DateTime),
    (date, Date),
    (time, Time),
    (timedelta, Interval),
    (List[str], JSON),
    (Optional[int], Integer),  # Test generic type Optional
    (Optional[str], String),  # Another generic type
    (Optional[List[str]], JSON),  # Nested generic type
]


@pytest.mark.parametrize("pydantic_type, expected_type", test_cases)
def test_pydantic_type_to_sqlalchemy_type(pydantic_type, expected_type):
    assert Orm.pydantic_type_to_sqlalchemy_type(pydantic_type) == expected_type


# Define a sample Pydantic model
class SamplePydanticModel(BaseModel):
    id: int
    name: str


# Define a corresponding SQLAlchemy model
Base = declarative_base()


class SampleSQLAlchemyModel(Base):
    __tablename__ = "sample"

    id = Column(Integer, primary_key=True)
    name = Column(String)


# Test for correct conversion
def test_convert_instance_pydantic_to_sqlalchemy():
    # Create a Pydantic instance
    pydantic_instance = SamplePydanticModel(id=1, name="Test")

    # Convert to SQLAlchemy instance
    sqlalchemy_instance = convert_instance_pydantic_to_sqlalchemy(
        pydantic_instance, SampleSQLAlchemyModel
    )

    # Assertions to verify the conversion
    assert sqlalchemy_instance.id == pydantic_instance.id
    assert sqlalchemy_instance.name == pydantic_instance.name
    assert isinstance(sqlalchemy_instance, SampleSQLAlchemyModel)


# Test for error handling (example)
def test_conversion_with_incompatible_models():
    # Create a Pydantic instance with unexpected fields
    class IncompatiblePydanticModel(BaseModel):
        unexpected_field: str

    pydantic_instance = IncompatiblePydanticModel(unexpected_field="Unexpected")

    # Test that an error is raised when incompatible models are used
    with pytest.raises(TypeError):
        convert_instance_pydantic_to_sqlalchemy(
            pydantic_instance, SampleSQLAlchemyModel
        )
