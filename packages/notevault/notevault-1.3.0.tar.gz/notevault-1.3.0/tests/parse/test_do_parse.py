from datetime import date, datetime, time, timedelta

import pytest
from bs4 import BeautifulSoup
from pydantic import BaseModel
from pydantic.fields import FieldInfo

from notevault.parse.do_parse import do_parse, parse_props, parse_props_kv


@pytest.mark.parametrize(
    ("field_name", "text", "expected"),
    [
        ("start", "start: 06:00", "06:00"),
        ("duration", "duration: 1:00", "1:00"),
        ("participants", "participants: '@user1, @user2'", "@user1, @user2"),
        ("minutes", "lorem ipsum dolor sit amet", "lorem ipsum dolor sit amet"),
        ("minutes", "lorem ipsum: dolor sit amet", "lorem ipsum: dolor sit amet"),
        ("name", "name: item1, start: 07:30, duration: 1, breaks: 0:30", "item1"),
        ("duration", "name: item1, start: 07:30, duration: 1, breaks: 0:30", str(1)),
        ("not_existent", "name: item1, start: 07:30, duration: 1, breaks: 0:30", None),
    ],
)
def test_parse_props_kv(field_name, text, expected):
    parsed = parse_props_kv(field_name, text)
    assert parsed == expected


@pytest.mark.parametrize(
    ("value_tag", "field_name", "field_info", "expected"),
    [
        (
            "<li>start: 07:30</li>",
            "start",
            FieldInfo(annotation=time, required=True),
            time(7, 30),
        ),
        (
            "<li>duration: 2:30</li>",
            "duration",
            FieldInfo(annotation=timedelta),
            timedelta(hours=2, minutes=30),
        ),
        (
            "<p>lorem ipsum dolor sit amet\n - lorem ipsum dolor sit amet</p>",
            "minutes",
            FieldInfo(annotation=str),
            "lorem ipsum dolor sit amet\n - lorem ipsum dolor sit amet",
        ),
        (
            "<li>participants: '@user1, @user2'</li>",
            "participants",
            FieldInfo(annotation=list[str]),
            ["@user1", "@user2"],
        ),
        (
            "<li>name: item1, start: 07:30, duration: 1, breaks: 0:30</li>",
            "name",
            FieldInfo(annotation=str),
            "item1",
        ),
        (
            "<li>name: item1, start: 07:30, duration: 1, breaks: 0:30</li>",
            "duration",
            FieldInfo(annotation=int),
            1,
        ),
    ],
)
def test_parse_props(value_tag, field_name, field_info, expected):
    parsed = parse_props(
        BeautifulSoup(value_tag, features="html.parser"), field_name, field_info
    )
    assert parsed == expected


def test_parse_heading_section():
    heading_section = """
    <p>name: Meeting 2</p>
    <ul>
    <li>start: 07:30</li>
    <li>duration: 2:30</li>
    <li>participants: '@user1, @user2'</li>
    </ul>
    <h3>Minutes</h3>
    <p>lorem ipsum dolor sit amet
    - lorem ipsum dolor sit amet
    - lorem ipsum dolor sit amet
    lorem ipsum dolor sit amet</p>
    """

    class Meeting(BaseModel):
        name: str
        start: time
        duration: timedelta = None
        minutes: str = None
        participants: list[str] = []

    parsed = do_parse(BeautifulSoup(heading_section, features="html.parser"), Meeting)
    assert isinstance(parsed, Meeting)
    assert parsed.name == "Meeting 2"
    assert parsed.start == time(7, 30)
    assert parsed.duration == timedelta(hours=2, minutes=30)
    assert parsed.participants == ["@user1", "@user2"]
    assert (
        parsed.minutes
        == """
lorem ipsum dolor sit amet
    - lorem ipsum dolor sit amet
    - lorem ipsum dolor sit amet
    lorem ipsum dolor sit amet
"""
    )


def test_parse_list_section():
    list_section = """
    <li>name: item1, start: 07:30, duration: 1, breaks: 0:30</li>
    """

    class List(BaseModel):
        name: str
        duration: int
        start: time = None
        breaks: timedelta = None

    parsed = do_parse(BeautifulSoup(list_section, features="html.parser"), List)
    assert isinstance(parsed, List)
    assert parsed.name == "item1"
    assert parsed.start == time(7, 30)
    assert parsed.duration == 1
    assert parsed.breaks == timedelta(minutes=30)


def test_parse_general_section():
    general_section = """
    <ul>
    <li>start: 07:30</li>
    <li>breaks: 0:30</li>
    <li>timestamp: 2020-01-01 07:30</li>
    <li>datum: 2020-01-01</li>
    </ul>
    """

    class General(BaseModel):
        start: time = None
        breaks: timedelta = None
        timestamp: datetime = None
        datum: date = None

    parsed = do_parse(BeautifulSoup(general_section, features="html.parser"), General)
    assert isinstance(parsed, General)
    assert parsed.start == time(7, 30)
    assert parsed.breaks == timedelta(minutes=30)
    assert parsed.timestamp == datetime(2020, 1, 1, 7, 30)
    assert parsed.datum == date(2020, 1, 1)
