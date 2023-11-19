import logging
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from notevault.entrypoints.main import Main
from notevault.environment import ROOT_DIR, config
from notevault.helper import load_schema
from notevault.model.create_models import create_models
from notevault.model.orm import Orm
from tests.test_main import TEST_DOC_FILENAME

log = logging.getLogger(__name__)
log_fmt = r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(format=log_fmt, level=logging.DEBUG, datefmt=datefmt)


@pytest.fixture
def main_instance():
    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
    db_name = doc_schema["Config"]["database"]
    Path(db_name).unlink(missing_ok=True)
    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    main.edit_and_parse(TEST_DOC_FILENAME, interactive=False)
    main.save(TEST_DOC_FILENAME)
    yield main
    Path(db_name).unlink(missing_ok=True)


# fixture for database session
@pytest.fixture
def session() -> Session:
    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
    db_name = doc_schema["Config"]["database"]
    engine = create_engine(f"sqlite:///{db_name}", echo=False)
    with sessionmaker(bind=engine)() as session:
        yield session
