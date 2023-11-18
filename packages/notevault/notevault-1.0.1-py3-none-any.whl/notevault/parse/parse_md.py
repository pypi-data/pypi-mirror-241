from enum import Enum
from typing import Dict, List, Type

from bs4 import BeautifulSoup
from markdown import markdown
from pydantic import BaseModel, ValidationError

from notevault.parse.helper import get_top_heading_level, extract_heading_section_html
from notevault.parse.parse_section import parse_section2


class ListSpecifierEnum(str, Enum):
    HEADING = "heading"
    LIST = "list"


def parse_markdown(
    md_text: str,
    document_structure: Dict,
    generated_classes: Dict[str, Type[BaseModel]],
) -> List[BaseModel]:
    soup = BeautifulSoup(markdown(md_text), "html.parser")
    parsed_models = []

    # Loop over every section
    for section_info in document_structure.get("Sections"):
        heading = section_info["section"]["heading"]
        class_name = section_info["section"]["type"]
        is_list = section_info["section"]["is_list"]

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

        model_class = generated_classes.get(class_name)
        if not model_class:
            print(f"Skipping section {class_name} because no model was found.")
            continue

        # Parse the section soup into a Pydantic model
        try:
            if is_list:
                list_specifier = ListSpecifierEnum(section_info["section"]["list_specifier"])  # TODO: check yaml validity
                if list_specifier == ListSpecifierEnum.HEADING:
                    sub_heading_level = f"h{get_top_heading_level(section_soup)}"  # h2
                    list_items = section_soup.find_all(sub_heading_level)
                elif list_specifier == ListSpecifierEnum.LIST:
                    list_items = soup.find_all("li")  # TODO: add numbered lists
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
                        list_item = BeautifulSoup(str(list_item) + str(section_soup), "html.parser")

                    model_instance = parse_section2(list_item, model_class)
                    parsed_models.append(model_instance)

            else:
                model_instance = parse_section2(section_soup, model_class)
                parsed_models.append(model_instance)
        except ValidationError as e:
            new_exception = RuntimeError(
                f"Data validation error for section {class_name}"
            )
            raise new_exception from e

    return parsed_models
