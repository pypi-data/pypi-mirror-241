from datetime import date, datetime, time, timedelta
from typing import Any, List, Optional, Type, get_args, get_origin

from pydantic import BaseModel
from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Interval,
    String,
    Time,
    create_engine,
)
from sqlalchemy.orm import joinedload, relationship, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.sql.type_api import TypeEngine

from notevault.model.create_models import DeclarativeBase, SqlAlchemyModel, T


class Orm:
    def __init__(
        self, db_path: str, document_model: SqlAlchemyModel, decl_base: DeclarativeBase
    ) -> None:
        self.engine = create_engine(f"sqlite:///{db_path}", echo=False)
        self.session = sessionmaker(bind=self.engine)()
        self.document_model = document_model
        self.decl_base = decl_base

    def create_all(self, generated_classes: dict[str, Type[T]]) -> dict:
        # Create SQLAlchemy models from Pydantic models
        sqlalchemy_models = {
            name: self.create_sqlalchemy_model_from_pydantic(model)
            for name, model in generated_classes.items()
        }
        # Define relationships on the Document class
        # Assuming sqlalchemy_models is a list of model classes and not names
        for model_name, model_class in sqlalchemy_models.items():
            relationship_name = model_name.lower() + "s"
            # Establish relationship on Document for each related class
            setattr(
                self.document_model,
                relationship_name,
                relationship(model_class, back_populates="document"),
            )
        # Add Document to sqlalchemy_models for completeness
        sqlalchemy_models["Document"] = self.document_model
        # Step 6: Create all tables in the database.
        self.decl_base.metadata.create_all(self.engine)
        return sqlalchemy_models

    def create_sqlalchemy_model_from_pydantic(
        self, pydantic_model: Type[BaseModel]
    ) -> SqlAlchemyModel:
        attrs = {}
        primary_key_found = False

        # Check if a primary key is already defined
        for field_name, field_type in pydantic_model.__annotations__.items():
            is_nullable = "None" in str(field_type) or "Optional" in str(
                field_type
            )  # TODO: wrong
            # TODO: mapping not working with Optional
            column_type = self.pydantic_type_to_sqlalchemy_type(field_type)
            # if column_type == Time:  # TODO Sqlite does not support time
            #     column_type = String
            column_args = {}
            if not is_nullable:
                column_args["nullable"] = False

            if hasattr(column_type, "__primary_key__"):
                primary_key_found = True
                column_args["primary_key"] = True

            attrs[field_name] = Column(column_type, **column_args)

        # If no primary key was found, add one. This can be adjusted as needed.
        if not primary_key_found:
            attrs["id"] = Column(Integer, primary_key=True, autoincrement=True)

        # Add foreign key to the document to link to master table Document
        attrs["document_name"] = Column(String, ForeignKey("document.name"))
        # add relationship to the document
        attrs["document"] = relationship(
            "Document", back_populates=pydantic_model.__name__.lower() + "s"
        )

        attrs["created"] = Column(DateTime, default=func.now())
        attrs["updated"] = Column(DateTime, default=func.now(), onupdate=func.now())

        attrs["__tablename__"] = pydantic_model.__name__.lower()
        # attrs["__table_args__"] = {"extend_existing": True}  # fix testing
        sqlalchemy_model = type(pydantic_model.__name__, (self.decl_base,), attrs)
        return sqlalchemy_model

    def load_document(self, document_name: str) -> Optional[SqlAlchemyModel]:
        """Load a saved Document from the SQLite database by its name with all relationships eagerly loaded."""
        return (
            self.session.query(self.document_model)
            .options(joinedload("*"))  # type: ignore
            .filter(self.document_model.name == document_name)
            .first()
        )

    @staticmethod
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

