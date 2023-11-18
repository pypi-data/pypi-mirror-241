import pytest
from bs4 import BeautifulSoup

from notevault.parse.helper import get_top_heading_level

sections = [
    ("""
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
    """, 2),
    ("""
    <p>lorem ipsum dolor sit amet
    - lorem ipsum dolor sit amet
    - lorem ipsum dolor sit amet
    lorem ipsum dolor sit amet</p>
    """, 0),
]


# Parameterized test
@pytest.mark.parametrize("html_content, expected", sections)
def test_get_top_heading_level(html_content, expected):
    soup = BeautifulSoup(html_content, "html.parser")
    assert get_top_heading_level(soup) == expected


list_items = [
    "<li>name: item1, start: 07:30, duration: 1, breaks: 0:30</li>",
    "<h2>Meeting 1</h2>",
    "<h2>Meeting 1</h2>\n <ul>\n <li>start: 06:00</li>\n <li>duration: 1:00</li>\n </ul>\n "
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
