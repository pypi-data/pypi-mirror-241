from enum import Enum
from typing import Any, Dict, List, Type

from bs4 import BeautifulSoup
from markdown import markdown
from pydantic import BaseModel, ValidationError

from notevault.parse.do_parse import do_parse
from notevault.parse.helper import extract_heading_section_html, get_top_heading_level


class ListSpecifierEnum(str, Enum):
    HEADING = "heading"
    LIST = "list"


def parse_markdown(
    md_text: str,
    document_structure: Dict,
    generated_schemas: Dict[str, Type[BaseModel]],
) -> List[BaseModel]:
    soup = BeautifulSoup(markdown(md_text), "html.parser")
    parsed_models = []

    # Loop over every section
    for section_info in document_structure.get("Sections"):
        heading = section_info["section"]["heading"]
        class_name = section_info["section"]["type"]

        # Find the heading in the markdown
        heading_level = f"h{heading.count('#')}"  # h1
        section_heading = soup.find(heading_level, string=heading.strip("# ").strip())

        if section_heading is None:
            print(f"Skipping section {class_name} because no heading was found.")
            continue

        # Get section soup: HTML of the section defined by the heading level
        section_soup = BeautifulSoup(
            extract_heading_section_html(section_heading), "html.parser"
        )

        model_schema = generated_schemas.get(class_name)
        if not model_schema:
            print(f"Skipping section {class_name} because no model was found.")
            continue

        parse_section(model_schema, parsed_models, section_info, section_soup)

    return parsed_models


def parse_section(
    model_schema: Type[BaseModel],
    parsed_models: list[BaseModel],
    section_info: dict[str, Any],
    section_soup: BeautifulSoup,
) -> None:
    """Parse the section soup into a Pydantic model"""
    is_list = section_info["section"]["is_list"]
    class_name = section_info["section"]["type"]
    try:
        if is_list:
            list_specifier = ListSpecifierEnum(
                section_info["section"]["list_specifier"]
            )  # TODO: check yaml validity
            if list_specifier == ListSpecifierEnum.HEADING:
                sub_heading_level = f"h{get_top_heading_level(section_soup)}"  # h2
                list_items = section_soup.find_all(sub_heading_level)
            elif list_specifier == ListSpecifierEnum.LIST:
                list_items = section_soup.find_all("li")  # TODO: add numbered lists
            else:
                raise ValueError(f"Invalid list_specifier: {list_specifier}")

            for list_item in list_items:
                # build complete list item with heading sub-sections
                if list_item.name.startswith("h"):
                    section_soup = BeautifulSoup(
                        extract_heading_section_html(list_item), "html.parser"
                    )
                    # inject heading_field as <p> into the heading for parsing as field
                    heading_field = section_info["section"]["heading_field"]
                    list_item.string = f"{heading_field}: {list_item.string}"
                    list_item.name = "p"
                    list_item = BeautifulSoup(
                        str(list_item) + str(section_soup), "html.parser"
                    )

                model_instance = do_parse(list_item, model_schema)
                parsed_models.append(model_instance)

        else:
            model_instance = do_parse(section_soup, model_schema)
            parsed_models.append(model_instance)
    except ValidationError as e:
        new_exception = RuntimeError(f"Data validation error for section {class_name}")
        raise new_exception from e
