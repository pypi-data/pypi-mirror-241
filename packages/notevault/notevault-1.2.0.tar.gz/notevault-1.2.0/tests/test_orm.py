from typing import Optional

import pytest
from pydantic import BaseModel

from notevault.model.create_models import create_models
from notevault.model.orm import Orm

Document, Base = create_models()


@pytest.fixture(scope="function")
def orm():
    global Base
    global Document
    Document, Base = create_models()
    orm = Orm(":memory:", Document, Base)  # sqlite:///:memory:
    Base.metadata.create_all(orm.engine)
    yield orm
    Base.metadata.drop_all(orm.engine)


class MockModel(BaseModel):
    name: str
    value: Optional[int]


# Mock Pydantic models
class MockModelOne(BaseModel):
    name: str


class MockModelTwo(BaseModel):
    value: int


def test_create_all_with_mock_models(orm):
    # Document.__table__.create(bind=orm.engine)
    generated_classes = {"MockModel": MockModel}
    models = orm.create_all(generated_classes)

    # Assert that models were created and returned
    assert "MockModel" in models
    assert "Document" in models


def test_create_sqlalchemy_model_from_pydantic(orm):
    sqlalchemy_model = orm.create_sqlalchemy_model_from_pydantic(MockModel)

    # Assert checks for the SQLAlchemy model structure
    assert hasattr(sqlalchemy_model, "__tablename__")
    assert hasattr(sqlalchemy_model, "id")  # Auto-added primary key
    assert hasattr(sqlalchemy_model, "name")
    assert hasattr(sqlalchemy_model, "value")


def test_create_all_with_relationships(orm):
    generated_classes = {"MockModelOne": MockModelOne, "MockModelTwo": MockModelTwo}
    models = orm.create_all(generated_classes)

    # Assert that models were created and returned
    assert "MockModelOne" in models
    assert "MockModelTwo" in models
    assert "Document" in models

    # Assert that relationships are established
    # These assertions depend on how you've implemented relationship handling in create_all
    assert hasattr(models["MockModelOne"], "document")
    assert hasattr(models["MockModelTwo"], "document")
    assert issubclass(models["MockModelOne"], Base)
    assert issubclass(models["MockModelTwo"], Base)


def test_load_existing_document(orm):
    # Setup: Add a test document
    session = orm.session
    test_document = orm.document_model(name="name", content="Test Content")
    session.add(test_document)
    session.commit()

    # Test: Load the document
    loaded_document = orm.load_document("name")
    assert loaded_document is not None
    assert loaded_document.name == "name"


def test_load_nonexistent_document(orm):
    # Test: Attempt to load a document that doesn't exist
    loaded_document = orm.load_document("Nonexistent")
    assert loaded_document is None
