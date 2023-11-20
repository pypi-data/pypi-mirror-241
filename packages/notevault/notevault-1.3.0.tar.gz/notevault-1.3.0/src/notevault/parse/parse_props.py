from parsy import regex, seq, string

year = regex("[0-9]{4}").map(int).desc("4 digit year")
month = regex("[0-9]{2}").map(int).desc("2 digit month")
day = regex("[0-9]{2}").map(int).desc("2 digit day")

# Utilities
whitespace = regex(r"\s*")  # consume any amount of whitespace, including none
lexeme = lambda p: p << whitespace  # noqa

# Punctuation
lbrace = lexeme(string("{"))
rbrace = lexeme(string("}"))
lbrack = lexeme(string("["))
rbrack = lexeme(string("]"))
colon = lexeme(string(":"))
comma = lexeme(string(","))
enumeration = lexeme(regex("^[-,*]"))

# Parser for property names (assumes property names are alphanumeric with no spaces)
identifier = regex(r"[a-zA-Z0-9_]+").map(str)

# Parser for integer values
int_value = regex(r"-?\d+").map(int)

# Parser for time to be before int_value
time_value = regex(r"\d{1,2}:\d{2}").map(str)

# (?=(?:.*\d){4,}):
# positive lookahead assertion: checks that there are at least 4 digits somewhere ahead in the string.
# It does not consume any characters itself.
# (?:.*\d){4,}: This non-capturing group (?:...) matches any character .* followed by a digit \d,
# and {5,} specifies that this group must occur at least five times.
datetime_value = regex(r"(?=(?:.*\d){4,})[\d:\-\. ]+").map(str)

# Parser for complex string values (handles commas within quotes)
string_value_naive = regex(r"[^,\"']*")
string_value_single = regex(r"'[^']*'").map(lambda s: s.strip("'"))
string_value_double = regex(r'"[^"]*"').map(lambda s: s.strip('"'))
string_value = string_value_single | string_value_double | string_value_naive

# Parser for general values
value = (
    time_value | datetime_value | int_value | string_value
)  # pre-emt the int_value matching by time_value

# # Parser for key-value pairs
key_value = seq(whitespace >> identifier << string(":").result(""), whitespace >> value)

# Parser for the entire string (separated by commas)
properties_parser = enumeration.optional() >> key_value.sep_by(comma)

if __name__ == "__main__":
    print(lbrace.parse(" { "))
