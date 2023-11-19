from typing import Any, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.orm import declarative_base

T = TypeVar("T", bound=BaseModel)
# Create a type alias for the declarative base class
DeclarativeBase = Type[declarative_base()]
SqlAlchemyModel = TypeVar("SqlAlchemyModel", bound=DeclarativeBase)


def create_models() -> tuple[SqlAlchemyModel, DeclarativeBase]:
    Base = declarative_base()

    class Document(Base):
        __tablename__ = "document"
        name = Column(String, primary_key=True)
        content = Column(String)
        created = Column(DateTime, default=func.now())
        updated = Column(DateTime, default=func.now(), onupdate=func.now())

    return Document, Base


def convert_instance_pydantic_to_sqlalchemy(
    pydantic_instance: BaseModel,
    sqlalchemy_model: DeclarativeBase,  # TODO: Type[Base]
) -> Any:
    # Extract fields from the Pydantic instance
    field_values = pydantic_instance.model_dump()
    # Create a new SQLAlchemy instance with the fields
    sqlalchemy_instance = sqlalchemy_model(**field_values)
    return sqlalchemy_instance
