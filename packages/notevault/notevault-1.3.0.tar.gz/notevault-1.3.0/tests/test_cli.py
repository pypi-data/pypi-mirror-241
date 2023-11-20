from pathlib import Path

import pytest
from typer.testing import CliRunner

from notevault.entrypoints.cli import app
from notevault.entrypoints.main import Main
from notevault.environment import ROOT_DIR
from notevault.helper import load_schema
from notevault.model.create_models import create_models
from notevault.model.orm import Orm
from tests.test_main import TEST_DOC_FILENAME, TEST_DOC_NAME

runner = CliRunner()


@pytest.fixture
def main_instance():
    doc_schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
    db_name = doc_schema["Config"]["database"]
    Path(db_name).unlink(missing_ok=True)
    Document, Base = create_models()
    orm = Orm(db_name, Document, Base)

    main = Main(TEST_DOC_FILENAME, doc_schema, orm)
    main.edit_and_parse(interactive=False)
    main.save()
    yield main
    Path(db_name).unlink(missing_ok=True)


def test_daily():
    result = runner.invoke(app, ["daily", "--no-interactive"])
    assert result.exit_code == 0
    print(result.output)


def test_versiosn():
    result = runner.invoke(
        app,
        [
            "version",
        ],
    )
    assert result.exit_code == 0
    print(result.output)
    # assert "Hello Alice!" in result.stdout


def test_daily_many():
    result = runner.invoke(app, ["daily-many", "--no-interactive"])
    assert result.exit_code == 0
    print(result.output)
    # assert "Hello Alice!" in result.stdout


@pytest.mark.skip("not ready yet")
def test_export_file_exists_no_force(tmp_path, main_instance):
    # Setup - create a mock file
    mock_file = tmp_path / "mockfile.md"
    mock_file.touch()

    # Change to temporary directory
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["export", TEST_DOC_NAME])
        assert result.exit_code == 1
        assert "Document exists: mockfile. Use --force" in result.output


@pytest.mark.skip("not ready yet")
def test_export_file_exists_force(tmp_path):
    # Setup - create a mock file
    mock_file = tmp_path / "mockfile.md"
    mock_file.touch()

    # Change to temporary directory
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["export", "mockfile", "--force"])
        # Replace the following line with the appropriate assertion for your case
        assert result.exit_code == 0


@pytest.mark.skip("not ready yet")
def test_export_file_does_not_exist(tmp_path, main_instance):
    expected_file_path = tmp_path / f"{TEST_DOC_NAME}.md"
    assert not expected_file_path.exists()

    # Change to temporary directory
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["export", TEST_DOC_NAME])
        print(result.output)

        # Replace the following line with the appropriate assertion for your case
        assert result.exit_code == 0
        assert expected_file_path.exists()
