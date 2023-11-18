from datetime import date, datetime, time, timedelta
from typing import Any, List, Type, TypeVar, get_args, get_origin

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
    func,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.type_api import TypeEngine  # base class for all SQLAlchemy types

T = TypeVar("T", bound=BaseModel)
# Create a type alias for the declarative base class
DeclarativeBase = Type[declarative_base()]
SqlAlchemyModel = TypeVar("SqlAlchemyModel", bound=DeclarativeBase)


# Base class for our models
# Base = declarative_base()


def create_models() -> tuple[SqlAlchemyModel, DeclarativeBase]:
    Base = declarative_base()

    class Document(Base):
        __tablename__ = "document"
        name = Column(String, primary_key=True)
        content = Column(String)
        created = Column(DateTime, default=func.now())
        updated = Column(DateTime, default=func.now(), onupdate=func.now())

    return Document, Base


# class Document(Base):
#     __tablename__ = "document"
#     name = Column(String, primary_key=True)
#     content = Column(String)


# Mapping function
# Helper function to map SQLAlchemy types to Pydantic types
def sqlalchemy_type_to_pydantic_type(sqlalchemy_type):
    # This function should return a Pydantic-compatible type,
    # based on the provided SQLAlchemy column type
    # For simplicity, a direct map is shown here. This would need to be expanded
    # to handle all the types and edge cases properly.
    type_mapping = {
        Integer: int,
        String: str,
        Float: float,
        Boolean: bool,
        DateTime: datetime,
        Date: date,
        Time: time,
        Interval: timedelta,
        # Add more SQLAlchemy to Pydantic type mappings as needed
    }
    return type_mapping.get(type(sqlalchemy_type), str)  # Default to string


def pydantic_type_to_sqlalchemy_type(pydantic_type: Type[Any]) -> Type[TypeEngine]:
    """Convert Pydantic types to equivalent SQLAlchemy types.

    The function also handles generic types such as `typing.Optional` by extracting
    the base type. For unsupported types, it defaults to `String`.
    """
    type_mapping = {
        int: Integer,
        str: String,
        float: Float,
        bool: Boolean,
        datetime: DateTime,
        date: Date,
        time: Time,
        timedelta: Interval,
        List[str]: JSON,
    }
    # Extract base type for generic types like typing.Optional
    origin = get_origin(pydantic_type)
    if origin:
        # Get the first argument from the generic
        args = get_args(pydantic_type)
        if args:
            # Replace the original type with its base type
            pydantic_type = args[0]
            if (
                origin is list
            ):  # Check if the origin was list to return JSON for List types
                return JSON
    return type_mapping.get(
        pydantic_type, String
    )  # Default to String if type not found


def convert_instance_pydantic_to_sqlalchemy(
    pydantic_instance: BaseModel,
    sqlalchemy_model: DeclarativeBase,  # TODO: Type[Base]
):
    # Extract fields from the Pydantic instance
    field_values = pydantic_instance.model_dump()
    # Create a new SQLAlchemy instance with the fields
    sqlalchemy_instance = sqlalchemy_model(**field_values)
    return sqlalchemy_instance
