import logging
from datetime import datetime
from pathlib import Path
from typing import Union

import typer

from notevault import __version__
from notevault.create_models import create_models
from notevault.environment import ROOT_DIR, config
from notevault.helper import load_schema
from notevault.main import Main
from notevault.orm import Orm

app = typer.Typer()

log = logging.getLogger(__name__)


@app.command()
def version():
    """Show version and configuration"""
    typer.echo(f"Version: {__version__}")
    typer.echo(f"Schema: {config.notevault_doc_schema_path}")
    doc_schema = load_schema(config.notevault_doc_schema_path)
    db_name = doc_schema["Config"]["database"]
    typer.echo(f"Database: {db_name}")


@app.command()
def daily(no_interactive: bool = False):
    doc_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    doc_schema = load_schema(config.notevault_doc_schema_path)
    db_name = doc_schema["Config"]["database"]
    # Path(db_name).unlink(missing_ok=True)

    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(doc_name, doc_schema, orm)
    main.edit_and_parse(interactive=not no_interactive)
    main.save()
    # main.create(doc_name, md_text)
    if main.exists():
        print(f"Document found: {db_name}: {doc_name}.")


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

    main = Main(name, doc_schema, orm)
    main.export(name)


@app.command()
def show(name: str):
    """ """
    doc_schema = load_schema(config.notevault_doc_schema_path)
    db_name = doc_schema["Config"]["database"]
    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(name, doc_schema, orm)
    main.show(name)


if __name__ == "__main__":
    import logging

    log_fmt = (
        r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
    )
    datefmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(format=log_fmt, level=config.log_level, datefmt=datefmt)
    app()
