import parsy
import pytest

from notevault.parse.parse_props import (
    datetime_value,
    enumeration,
    identifier,
    int_value,
    key_value,
    lbrace,
    properties_parser,
    string_value,
    string_value_double,
    string_value_naive,
    string_value_single,
    time_value,
    value,
)


def test_datetime():
    # assert datetime_value.parse("timestamp: 2020-01-01 07:30") == [["timestamp", "2020-01-01 07:30"]]
    assert datetime_value.parse("2020-01-01 07:30") == "2020-01-01 07:30"
    assert datetime_value.parse("2020-01-01") == "2020-01-01"
    assert datetime_value.parse("1.1.2000") == "1.1.2000"
    assert datetime_value.parse("2000") == "2000"

    with pytest.raises(parsy.ParseError):
        datetime_value.parse("1.1.2000, 1:0")
        datetime_value.parse("202-01-01")
        datetime_value.parse("03:10")
        datetime_value.parse("1 2 3 4")


def test_time_value():
    assert time_value.parse("18:30") == "18:30"


def test_key_value():
    # assert time_value.parse("18:30") == "18:30"
    assert key_value.parse("ddd: xxx") == ["ddd", "xxx"]
    assert key_value.parse("d: xxx") == ["d", "xxx"]
    assert key_value.parse(" d: xxx") == ["d", "xxx"]
    assert key_value.parse("ts: 2020-01-01 07:30") == ["ts", "2020-01-01 07:30"]
    assert key_value.parse("name: Meeting 1") == ["name", "Meeting 1"]


def test_parse_ok():
    assert lbrace.parse("{ ") == "{"
    assert enumeration.parse("-  ") == "-"
    assert enumeration.parse("* ") == "*"
    assert identifier.parse("hello") == "hello"
    assert string_value_naive.parse("18:30") == "18:30"
    assert string_value_single.parse("'complex, string'") == "complex, string"
    assert string_value_double.parse('"complex, string"') == "complex, string"
    assert string_value.parse('"complex, string"') == "complex, string"
    assert string_value.parse("hello") == "hello"
    assert int_value.parse("2") == 2
    assert value.parse("2") == 2
    assert value.parse("'complex 2, single quotes'") == "complex 2, single quotes"
    assert key_value.parse("prop1: 'value1'") == ["prop1", "value1"]
    assert key_value.parse("prop1: value1") == ["prop1", "value1"]
    assert properties_parser.parse("prop1: xxx, prop2: 2, prop3: 'complex, prop'") == [
        ["prop1", "xxx"],
        ["prop2", 2],
        ["prop3", "complex, prop"],
    ]
    assert properties_parser.parse("-prop1: xxx, prop2: 2, prop3: 'complex, prop'") == [
        ["prop1", "xxx"],
        ["prop2", 2],
        ["prop3", "complex, prop"],
    ]
    assert properties_parser.parse(
        "- prop1: xxx, prop2: 2, prop3: 'complex, prop'"
    ) == [["prop1", "xxx"], ["prop2", 2], ["prop3", "complex, prop"]]
    assert properties_parser.parse(
        "*  prop1: xxx, prop2: 2, prop3: 'complex, prop'"
    ) == [["prop1", "xxx"], ["prop2", 2], ["prop3", "complex, prop"]]

    assert properties_parser.parse(
        'start: 17:30, duration: 2, data: "adsfadfasdf, asdfasdf"'
    ) == [["start", "17:30"], ["duration", 2], ["data", "adsfadfasdf, asdfasdf"]]

    assert properties_parser.parse("ts: 2020-01-01 07:30, start: 17:30") == [
        ["ts", "2020-01-01 07:30"],
        ["start", "17:30"],
    ]


def test_parse_errors():
    with pytest.raises(parsy.ParseError):
        # lbrace.parse(" { ")
        identifier.parse("- hallo:")
        identifier.parse("- hallo")
        properties_parser.parse("**  prop1: xxx, prop2: 2, prop3: 'complex, prop'")
        string_value_naive.parse("18: 30")
