from datetime import datetime
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from notevault.entrypoints.main import Main
from notevault.environment import ROOT_DIR
from notevault.helper import load_schema
from notevault.model.create_models import create_models
from notevault.model.orm import Orm

TEST_DOC_NAME = "daily.md"
TEST_DOC_FILENAME = f"{TEST_DOC_NAME}.md"


@pytest.fixture(autouse=True)
def init_db():
    Path("test_daily.db").unlink(missing_ok=True)


@pytest.fixture
def doc_path():
    (Path.cwd() / TEST_DOC_FILENAME).unlink(missing_ok=True)
    yield Path.cwd() / TEST_DOC_FILENAME
    (Path.cwd() / TEST_DOC_FILENAME).unlink(missing_ok=True)


@pytest.mark.skip("fixit")
def test_export_success(main_instance):
    main_instance.export(TEST_DOC_NAME)

    # Assert that file is created and content is correct
    export_path = Path.cwd() / TEST_DOC_FILENAME
    assert export_path.exists()
    with open(export_path, "r") as file:
        assert "lorem ipsum" in file.read()


@pytest.mark.skip("fixit")
def test_export_non_existent(main_instance, capsys):
    main_instance.export("non_existent_doc")

    # Capture stdout and assert correct message
    captured = capsys.readouterr()
    assert "Document not found: non_existent_doc" in captured.out


def test_daily_list():
    interactive = False

    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema_list.yaml")
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    content, parsed_obj = main.edit_and_parse(doc_name, interactive=interactive)
    main.save(doc_name, content, parsed_obj)
    # main.create(doc_name, md_text)
    if main.exists(doc_name):
        print(f"Document found: {doc_name}.")

    # Asserting the result of the join query
    engine = create_engine(f"sqlite:///{db_name}", echo=False)
    with sessionmaker(bind=engine)() as session:
        query = """
        SELECT * FROM list
        JOIN document ON list.document_name = document.name
        """
        results = session.execute(text(query)).fetchall()
        assert len(results) == 2
        for result in results:
            print(result)


def test_daily_meetings():
    interactive = False

    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema_meetings.yaml")
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    content, parsed_obj = main.edit_and_parse(doc_name, interactive=interactive)
    main.save(doc_name, content, parsed_obj)
    # main.create(doc_name, md_text)
    if main.exists(doc_name):
        print(f"Document found: {doc_name}.")

    # Asserting the result of the join query
    engine = create_engine(f"sqlite:///{db_name}", echo=False)
    with sessionmaker(bind=engine)() as session:
        query = """
        SELECT * FROM meeting
        JOIN document ON meeting.document_name = document.name
        """
        results = session.execute(text(query)).fetchall()
        assert len(results) == 2
        for result in results:
            print(result)


def test_daily_general(session):
    interactive = False

    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema_general.yaml")
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    content, parsed_obj = main.edit_and_parse(doc_name, interactive=interactive)
    main.save(doc_name, content, parsed_obj)
    # main.create(doc_name, md_text)
    if main.exists(doc_name):
        print(f"Document found: {doc_name}.")

    # Asserting the result of the join query
    query = """
    SELECT * FROM general
    JOIN document ON general.document_name = document.name
    """
    results = session.execute(text(query)).fetchall()
    assert len(results) == 1
    for result in results:
        print(result)


def test_daily(session):
    interactive = False

    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    content, parsed_obj = main.edit_and_parse(doc_name, interactive=interactive)
    main.save(doc_name, content, parsed_obj)
    # main.create(doc_name, md_text)
    if main.exists(doc_name):
        print(f"Document found: {doc_name}.")

    # Asserting the result of the join query
    query = """
    SELECT * FROM document
    JOIN general ON general.document_name = document.name
    JOIN meeting ON general.document_name = document.name
    """
    results = session.execute(text(query)).fetchall()
    # assert len(results) == 1
    for result in results:
        print(result)


@pytest.mark.skip("experimentation")
def test_daily_xxx(session):
    interactive = False

    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema(f"{ROOT_DIR}/schemas/daily.yaml")
    # doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/general.yaml")
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    content, parsed_obj = main.edit_and_parse(doc_name, interactive=interactive)
    main.save(doc_name, content, parsed_obj)
    # main.create(doc_name, md_text)
    if main.exists(doc_name):
        print(f"Document found: {doc_name}.")

    # Asserting the result of the join query
    # query = """
    # SELECT * FROM document
    # JOIN general ON general.document_name = document.name
    # JOIN meeting ON general.document_name = document.name
    # """
    # results = session.execute(text(query)).fetchall()
    # # assert len(results) == 1
    # for result in results:
    #     print(result)


def test_delete_null_document_name_rows(session):
    interactive = False

    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    content, parsed_obj = main.edit_and_parse(doc_name, interactive=interactive)
    main.save(doc_name, content, parsed_obj)
    # main.create(doc_name, md_text)
    if main.exists(doc_name):
        print(f"Document found: {doc_name}.")

    # main = Main(doc_schema, orm)
    content, parsed_obj = main.edit_and_parse(doc_name, interactive=interactive)
    main.save(doc_name, content, parsed_obj)
    # main.create(doc_name, md_text)
    if main.exists(doc_name):
        print(f"Document found: {doc_name}.")


    # Asserting the result of the join query
    query = """
    SELECT count(*) FROM meeting
    """
    results = session.execute(text(query)).fetchall()
    assert results[0][0] == 4

    main.delete_null_document_name_rows()
    results = session.execute(text(query)).fetchall()
    assert results[0][0] == 2
