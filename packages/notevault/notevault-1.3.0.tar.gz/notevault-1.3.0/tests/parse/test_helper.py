from datetime import datetime

import pytest
from bs4 import BeautifulSoup

from notevault.helper import get_last_working_day
from notevault.parse.helper import get_top_heading_level

sections = [
    (
        """
    <h2>Meeting 1</h2>
    <ul>
    <li>start: 06:00</li>
    <li>duration: 1:00</li>
    </ul>
    <h2>Meeting 2</h2>
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
    """,
        2,
    ),
    (
        """
    <p>lorem ipsum dolor sit amet
    - lorem ipsum dolor sit amet
    - lorem ipsum dolor sit amet
    lorem ipsum dolor sit amet</p>
    """,
        0,
    ),
]


# Parameterized test
@pytest.mark.parametrize("html_content, expected", sections)
def test_get_top_heading_level(html_content, expected):
    soup = BeautifulSoup(html_content, "html.parser")
    assert get_top_heading_level(soup) == expected


list_items = [
    "<li>name: item1, start: 07:30, duration: 1, breaks: 0:30</li>",
    "<h2>Meeting 1</h2>",
    "<h2>Meeting 1</h2>\n <ul>\n <li>start: 06:00</li>\n <li>duration: 1:00</li>\n </ul>\n ",
]

heading_section = """
<ul>
<li>start: 06:00</li>
<li>duration: 1:00</li>
</ul>
"""


@pytest.mark.skip(reason="Not implemented yet")
def test_extract_heading_section_html():
    assert False


# Test cases: Each tuple contains the input date and the expected output date
test_data = [
    ("2023-03-15", "2023-03-14"),  # Regular weekday to weekday
    ("2023-03-13", "2023-03-10"),  # Monday to previous Friday
    ("2023-03-20", "2023-03-17"),  # Monday to previous Friday
    # Add more test cases as needed
]


@pytest.mark.parametrize("input_date, expected_output", test_data)
def test_get_last_working_day(input_date, expected_output):
    input_date = datetime.strptime(input_date, "%Y-%m-%d")
    expected_output = datetime.strptime(expected_output, "%Y-%m-%d")
    assert get_last_working_day(input_date) == expected_output
