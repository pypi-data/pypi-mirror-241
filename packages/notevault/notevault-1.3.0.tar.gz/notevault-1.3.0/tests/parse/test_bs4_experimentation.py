import pytest
from bs4 import BeautifulSoup
from markdown import markdown

from notevault.create_schemas import generate_models_from_yaml
from notevault.environment import ROOT_DIR
from notevault.helper import load_schema
from notevault.parse.helper import extract_heading_section_html

schema = load_schema(f"{ROOT_DIR}/tests/resources/schema.yaml")
document_structure = schema["DocumentStructure"]
model_spec = schema["Model"]

with open(f"{ROOT_DIR}/tests/resources/daily_meeting.md", "r") as file:
    md_text = file.read()

# Generate the models
generated_classes = generate_models_from_yaml(model_spec)

GeneralModel = generated_classes["General"]
MeetingModel = generated_classes["Meeting"]
ListModel = generated_classes["List"]


class TestBs4Experimentation:
    # The fixture for BeautifulSoup object with markdown content
    @pytest.fixture
    def markdown_soup(self):
        markdown_html = """
        <h1>General</h1>
        <p>Some general information here.</p>
        <h1>Meetings</h1>
        <p>Meeting details here.</p>
        <h2>Subsection</h2>
        <p>Subsection content.</p>
        <h1>Another Section</h1>
        <p>Content of another section.</p>
        """
        soup = BeautifulSoup(markdown_html, "html.parser")
        return soup

    # Test if the function correctly extracts a section without subsections
    def test_extract_section_without_subsections(self, markdown_soup):
        section_heading = markdown_soup.find("h1", string="General")
        section_soup = BeautifulSoup(
            extract_heading_section_html(section_heading), "html.parser"
        )
        # Expect only the <p> under "General" to be included
        assert section_soup.find("p").text == "Some general information here."
        assert section_soup.find("h2") is None

    # Test if the function correctly skips other sections
    def test_extract_section_with_subsection_skips_others(self, markdown_soup):
        section_heading = markdown_soup.find("h1", string="Meetings")
        section_soup = BeautifulSoup(
            extract_heading_section_html(section_heading), "html.parser"
        )
        # Expect the <p> and <h2> under "Meetings" to be included, but not "Another Section"
        assert section_soup.find("p").text == "Meeting details here."
        assert section_soup.find("h2").text == "Subsection"
        assert section_soup.find("h1", string="Another Section") is None

    # Test if the function handles the end of document correctly
    def test_extract_section_end_of_document(self, markdown_soup):
        section_heading = markdown_soup.find("h1", string="Another Section")
        section_soup = BeautifulSoup(
            extract_heading_section_html(section_heading), "html.parser"
        )
        # Expect the <p> and <h2> under "Meetings" to be included, but not "Another Section"
        # Expect only the <p> under "Another Section" to be included
        assert section_soup.find("p").text == "Content of another section."
        assert section_soup.find("h1", string="General") is None


@pytest.mark.skip(reason="experimentation")
class TestExperimentation:
    md_text = """
    # General
    - start: 07:30
    - end: 18:00
    - breaks: 0:30
    - timestamp: 2020-01-01 07:30
    - date: 2020-01-01

    # Irrelevant part
    lorem ipsum dolor sit amet
    continue testing

    # Meetings
    ## Meeting 1
    - start: 07:30
    - duration: 2:30
    - participants: @user1, @user2
    ### Minutes

    lorem ipsum dolor sit amet

    - lorem ipsum dolor sit amet
    - lorem ipsum dolor sit amet
    lorem ipsum dolor sit amet

    ## Meeting 2
    - start: 07:30
    """

    def test_parse_markdown(self):
        m = markdown(self.md_text)
        soup = BeautifulSoup(m, "html.parser")
        print(soup.prettify())
        h = soup.find_all("h1")
        _ = None
