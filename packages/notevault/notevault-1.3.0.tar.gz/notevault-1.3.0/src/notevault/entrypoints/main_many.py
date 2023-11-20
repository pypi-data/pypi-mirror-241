
from notevault.entrypoints.main import Main
from notevault.environment import ROOT_DIR, config
from notevault.helper import load_schema
from notevault.model.create_models import create_models
from notevault.model.orm import Orm

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

    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    result = main.edit_and_parse_many(["1.md", "2.md"], interactive=interactive)
    for doc_name, (content, parsed_obj) in result.items():
        main.save(doc_name, content, parsed_obj)
        # main.create(doc_name, md_text)
        if main.exists(doc_name):
            print(f"Document found: {doc_name}.")
