import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, TypeVar

from pydantic import BaseModel

from notevault.create_schemas import Content, generate_models_from_yaml
from notevault.edit_content import edit_contents
from notevault.environment import ROOT_DIR, config
from notevault.helper import load_schema
from notevault.model.create_models import (
    SqlAlchemyModel,
    convert_instance_pydantic_to_sqlalchemy,
    create_models,
)
from notevault.model.orm import Orm
from notevault.parse.parse_md import parse_markdown

log = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class Main:
    def __init__(self, doc_schema: dict[str, Any], orm: Orm) -> None:
        schema = doc_schema
        self.document_spec = schema["DocumentStructure"]
        self.model_spec = schema["Model"]
        self.orm = orm
        self.template = schema["Config"]["template"]

        # Generate the models
        self.generated_schemas = generate_models_from_yaml(self.model_spec)
        self.sqlalchemy_models = self.orm.create_all(self.generated_schemas)

    def exists(self, name: str) -> bool:
        document = self.orm.load_document(name)
        if document:
            return True
        else:
            return False

    def read_or_init(self, name: str) -> Content:
        document = self.orm.load_document(name)
        if document:
            return document.content
        else:
            print(f"Document not found: {name}, using template: {self.template}.")
            with open(self.template, "r") as file:
                return Content(file.read())

    def edit_and_parse(
        self, name: str, interactive: bool = False
    ) -> tuple[Content, list[BaseModel]]:
        content = self.read_or_init(name)
        updated_contents = edit_contents({name: content}, interactive)
        updated_content = updated_contents[name]

        parsed_obj = parse_markdown(
            updated_content, self.document_spec, self.generated_schemas
        )
        return updated_content, parsed_obj

    def edit_and_parse_many(
        self, names: list[str], interactive: bool = False
    ) -> dict[str, tuple[Content, list[BaseModel]]]:
        contents = {}
        for name in names:
            contents[name] = self.read_or_init(name)

        updated_contents = edit_contents(contents, interactive)

        result = {}
        for name, updated_content in updated_contents.items():
            parsed_obj = parse_markdown(
                updated_content, self.document_spec, self.generated_schemas
            )
            result[name] = (updated_content, parsed_obj)

        return result

    def save(
        self, name: str, content: Content, parsed_objects: list[BaseModel]
    ) -> None:
        document = self.orm.load_document(name)
        if not document:
            document = self.orm.document_model(name=name, content=content)
            for obj in parsed_objects:
                obj_type = obj.__class__.__name__
                sqlalchemy_instance = convert_instance_pydantic_to_sqlalchemy(
                    obj, self.sqlalchemy_models[obj_type]
                )
                sqlalchemy_instance.document = document
            self.orm.session.add(document)
            _ = None
        else:
            print(f"Document loaded: {document.name}.")
            document.content = content

            # Build data dict with changes for document and related objects
            data = defaultdict(list)
            for obj in parsed_objects:
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

    def delete_null_document_name_rows(self) -> None:
        """
        Deletes rows from dynamically generated models where 'document_name' is NULL.
        """
        # Loop through the models
        for model_name, model_class in self.sqlalchemy_models.items():
            # Check if the model has 'document_name' attribute
            if hasattr(model_class, 'document_name'):
                self.orm.session.query(model_class).filter(model_class.document_name.is_(None)).delete(
                    synchronize_session='fetch')

        # Commit the changes to the database
        self.orm.session.commit()


if __name__ == "__main__":
    import logging

    log_fmt = (
        r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
    )
    datefmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(format=log_fmt, level=config.log_level, datefmt=datefmt)

    interactive = False
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

    main = Main(doc_schema, orm)
    content, parsed_obj = main.edit_and_parse(doc_name, interactive=interactive)
    main.save(doc_name, content, parsed_obj)
    # main.create(doc_name, md_text)
    if main.exists(doc_name):
        print(f"Document found: {doc_name}.")
