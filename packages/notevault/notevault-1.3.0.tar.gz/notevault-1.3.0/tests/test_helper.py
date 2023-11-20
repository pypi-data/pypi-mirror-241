import pytest

from notevault.helper import camel_to_snake, unslugify_header


@pytest.mark.parametrize(
    "slug, headings, expected",
    [
        ("h_prep", ["# Prep", "## Daily", "### one Two"], "# Prep"),
        ("hhh_one_two", ["# Prep", "## Daily", "### one Two"], "### one Two"),
    ],
)
def test_unslugify_header(slug, headings, expected):
    assert unslugify_header(slug, headings) == expected


# Parameterized test cases
@pytest.mark.parametrize(
    "input, expected",
    [
        ("CamelCase", "camel_case"),
        ("datetime", "datetime"),
        ("ThisIsATest", "this_is_a_test"),
        ("thisIsATest", "this_is_a_test"),
        ("this", "this"),
        ("This", "this"),
        ("", ""),
        ("snake_case", "snake_case"),
        ("Camel2Snake", "camel2_snake"),
        ("getHTTPResponseCode", "get_http_response_code"),
        ("get2HTTPResponseCode", "get2_http_response_code"),
        ("HTTPResponseCode", "http_response_code"),
        ("noHTTPS", "no_https"),
    ],
)
def test_camel_to_snake(input, expected):
    assert camel_to_snake(input) == expected
