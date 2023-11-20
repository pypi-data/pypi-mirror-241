import logging
from datetime import datetime
from pathlib import Path

import typer

from notevault import __version__
from notevault.entrypoints.main import Main
from notevault.environment import config
from notevault.helper import get_last_working_day, load_schema
from notevault.model.create_models import create_models
from notevault.model.orm import Orm
from notevault.validate_schema import validate_schema

log_fmt = r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
date_fmt = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(format=log_fmt, level=config.log_level, datefmt=date_fmt)
log = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def daily_many(no_interactive: bool = False):
    today = datetime.now().date()
    yesterday1 = get_last_working_day(today)
    yesterday2 = get_last_working_day(yesterday1)

    dailies = [
        f"{today.strftime('%Y-%m-%d')}.md",
        f"{yesterday1.strftime('%Y-%m-%d')}.md",
        f"{yesterday2.strftime('%Y-%m-%d')}.md",
    ]

    doc_schema = load_schema(config.notevault_doc_schema_path)
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    result = main.edit_and_parse_many(dailies, interactive=not no_interactive)
    for doc_name, (content, parsed_obj) in result.items():
        main.save(doc_name, content, parsed_obj)
        # main.create(doc_name, md_text)
        if main.exists(doc_name):
            print(f"Document found: {doc_name}.")


@app.command()
def daily(no_interactive: bool = False):
    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema(config.notevault_doc_schema_path)
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    content, parsed_obj = main.edit_and_parse(doc_name, interactive=not no_interactive)
    main.save(doc_name, content, parsed_obj)
    # main.create(doc_name, md_text)
    if main.exists(doc_name):
        print(f"Document found: {db_name}: {doc_name}.")
    # Cleanup null document_name rows
    main.delete_null_document_name_rows()


@app.command()
def export(name: str, force: bool = False):
    """ """
    if (Path.cwd() / f"{name}.md").exists() and not force:
        # write red typer error in color red
        typer.secho(f"Document exists: {name}. Use --force", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    if force:
        Path.cwd() / f"{name}.md".unlink(missing_ok=True)

    doc_schema = load_schema(config.notevault_doc_schema_path)
    db_name = doc_schema["Config"]["database"]
    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    main.export(name)


@app.command()
def show(name: str):
    """ """
    doc_schema = load_schema(config.notevault_doc_schema_path)
    db_name = doc_schema["Config"]["database"]
    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_schema, orm)
    main.show(name)


@app.command()
def version():
    """Show version and configuration"""
    logging.debug(f"{config=}")
    typer.echo(f"Version: {__version__}")
    typer.echo(f"Schema: {config.notevault_doc_schema_path}")
    doc_schema = load_schema(config.notevault_doc_schema_path)
    db_name = doc_schema["Config"]["database"]
    typer.echo(f"Database: {db_name}")


if __name__ == "__main__":
    # GOTCHA: script wrapper directly calls app, so logging config not working there
    log_fmt = (
        r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
    )
    date_fmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(format=log_fmt, level=config.log_level, datefmt=date_fmt)
    validate_schema(config.notevault_doc_schema_path)
    app()
