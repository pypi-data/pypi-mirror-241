import logging
from datetime import date, datetime, time, timedelta
from types import GenericAlias
from typing import Any, Type, _GenericAlias, get_args

import parsy
from bs4 import BeautifulSoup, Tag
from dateutil import parser
from pydantic import BaseModel
from pydantic.fields import FieldInfo

from notevault.parse.helper import extract_heading_section_html
from notevault.parse.parse_props import properties_parser

log = logging.getLogger(__name__)


def parse_props_kv(field_name: str, text: str) -> str | int:
    try:
        parsed = properties_parser.parse(text)
    except parsy.ParseError:
        # text is not key-value pair but entire section data
        parsed = [[field_name, text]]
    data = {key: value for key, value in parsed}
    return data.get(field_name)


def parse_props(value_tag: Tag, field_name: str, field_info: FieldInfo) -> Any | None:
    field_type = field_info.annotation
    if isinstance(field_type, _GenericAlias):
        # Extract the actual type from Optional or other generic types
        field_type = get_args(field_type)[0]

    is_required = field_info.is_required()
    log.debug(f"{value_tag=}, {field_name=}, {field_type=}, {is_required=}")

    if value_tag.name.startswith("h"):  # noqa
        value = value_tag.text  # entire section is field value
    else:
        value = parse_props_kv(field_name, value_tag.text)
    if value is None or value == "":
        if is_required:
            raise ValueError(f"Required field {field_name} is missing.")
        return None

    if isinstance(field_type, _GenericAlias) or isinstance(field_type, GenericAlias):
        if "list" in str(field_type).lower():
            return [v.strip() for v in value.split(",")]
    elif isinstance(field_type, type):
        if issubclass(field_type, time):
            return datetime.strptime(value, "%H:%M").time()
        elif issubclass(field_type, datetime):
            return parser.parse(value)
        elif issubclass(field_type, date):
            return parser.parse(value).date()
        elif issubclass(field_type, timedelta):
            hours, minutes = map(int, value.split(":"))
            return timedelta(hours=hours, minutes=minutes)
        elif issubclass(field_type, int):
            return int(value)
        else:
            return str(value)
    else:
        raise ValueError(f"Invalid field type: {field_type}")


def do_parse(item: BeautifulSoup, schema: Type[BaseModel]) -> BaseModel:
    parsed: dict[str, Any] = {}
    for field_name, field_info in schema.model_fields.items():
        log.debug(f"field_name: {field_name}")

        # find the field name in the section soup
        field_content = item.find(
            string=lambda text: text and field_name in text.lower()
        )
        if field_content:
            # Get the sibling or parent tag that contains the actual field data
            value_tag = (
                field_content.find_next_sibling()
                if isinstance(field_content, Tag)
                else field_content.parent  # gets enclosing tag if field_content is a NavigableString
            )
            assert value_tag.name is not None

            if value_tag.name.startswith("h"):  # noqa
                value_tag = BeautifulSoup(
                    extract_heading_section_html(value_tag), "html.parser"
                )
            log.debug(f"{value_tag=}, {value_tag.text=}")
            # use parse composer for key/val, minutes are special
            parsed[field_name] = parse_props(value_tag, field_name, field_info)
    log.debug(f"{parsed=}")
    return schema(**parsed)
