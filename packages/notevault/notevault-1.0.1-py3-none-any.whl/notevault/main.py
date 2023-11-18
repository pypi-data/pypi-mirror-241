import logging
import os
import subprocess
import tempfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, TypeVar

from pydantic import BaseModel

from notevault.create_models import (
    SqlAlchemyModel,
    convert_instance_pydantic_to_sqlalchemy,
    create_models,
)
from notevault.create_schemas import generate_models_from_yaml
from notevault.environment import ROOT_DIR, config
from notevault.helper import load_schema
from notevault.orm import Orm
from notevault.parse.parse_md import parse_markdown

log = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class Main:
    def __init__(self, name: str, doc_schema: dict[str, Any], orm: Orm) -> None:
        self.name = name
        self.content: str = ""
        schema = doc_schema
        self.document_spec = schema["DocumentStructure"]
        self.model_spec = schema["Model"]
        self.orm = orm
        self.template = schema["Config"]["template"]

        # Generate the models
        self.generated_schemas = generate_models_from_yaml(self.model_spec)
        self.sqlalchemy_models = self.orm.create_all(self.generated_schemas)
        self.parsed_objects: list[BaseModel] = []

    def exists(self) -> bool:
        document = self.orm.load_document(self.name)
        if document:
            return True
        else:
            return False

    def read_or_init(self) -> None:
        document = self.orm.load_document(self.name)
        if document:
            self.content = document.content
        else:
            print(f"Document not found: {self.name}, using template: {self.template}.")
            with open(self.template, "r") as file:
                self.content = file.read()

    def edit_and_parse(self, interactive: bool = False) -> None:
        self.read_or_init()
        tmp_path = self._edit_content(interactive)
        self._parse_content(tmp_path)

    def _edit_content(self, interactive: bool) -> str:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as tmp:
            tmp.write(self.content.encode("utf-8"))
            tmp_path = tmp.name

        if interactive:
            editor = os.environ.get("EDITOR", "vim")
            subprocess.call([editor, tmp_path])

        return tmp_path

    def _parse_content(self, tmp_path: str) -> None:
        with open(tmp_path, "r") as file:
            self.content = file.read()

        self.parsed_objects = parse_markdown(
            self.content, self.document_spec, self.generated_schemas
        )

    def save(self):
        document = self.orm.load_document(self.name)
        if not document:
            document = self.orm.document_model(name=self.name, content=self.content)
            for obj in self.parsed_objects:
                obj_type = obj.__class__.__name__
                sqlalchemy_instance = convert_instance_pydantic_to_sqlalchemy(
                    obj, self.sqlalchemy_models[obj_type]
                )
                sqlalchemy_instance.document = document
            self.orm.session.add(document)
            _ = None
        else:
            print(f"Document loaded: {document.name}.")
            document.content = self.content

            # Build data dict with changes for document and related objects
            data = defaultdict(list)
            for obj in self.parsed_objects:
                obj_type = obj.__class__.__name__
                sqlalchemy_instance = convert_instance_pydantic_to_sqlalchemy(
                    obj, self.sqlalchemy_models[obj_type]
                )
                sqlalchemy_instance.document = document

                instrumented_list = obj_type.lower() + "s"  # document field name
                data[instrumented_list].append(sqlalchemy_instance)
            # Save changes on document
            for instrumented_list, values in data.items():
                setattr(document, instrumented_list, values)

        self.orm.session.commit()

    def export(self, name: str) -> None:
        document = self.orm.load_document(name)
        if not document:
            print(f"Document not found: {name}")
            return

        file_path = Path.cwd() / f"{name}"
        with open(file_path, "w") as file:
            file.write(document.content)
        print(f"Document exported to {file_path}")

    def show(self, name: str) -> SqlAlchemyModel:
        document = self.orm.load_document(name)
        if not document:
            print(f"Document not found: {name}")
            return
        print(document.content)
        return document


if __name__ == "__main__":
    import logging

    log_fmt = (
        r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
    )
    datefmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(format=log_fmt, level=config.log_level, datefmt=datefmt)

    interactive = True
    if interactive:
        # Attach debugger
        user_input = input("Please enter some data: ")
        # print("You entered:", user_input)

    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_name, doc_schema, orm)
    main.edit_and_parse(interactive=interactive)
    main.save()
    # main.create(doc_name, md_text)
    if main.exists():
        print(f"Document found: {doc_name}.")
