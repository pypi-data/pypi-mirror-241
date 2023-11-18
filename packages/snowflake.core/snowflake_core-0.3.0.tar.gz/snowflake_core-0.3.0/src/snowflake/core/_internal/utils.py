from re import compile
from typing import Any, Dict, List, Optional, Union


MODE_MAPPING = {
    k.lower(): k
    for k in (
        "errorIfExists",
        "orReplace",
        "ifNotExists",
        "ifExists",
    )
}


# The following code is copied from snowpark's code /snowflake/snowpark/_internal/utils.py to avoid being broken
# when snowpark changes the code.
# We'll need to move the code to a common place.
# Another solution is to move snowpark to the mono repo so the merge gate will find the breaking changes.
# To address later.

EMPTY_STRING = ""
DOUBLE_QUOTE = '"'
ALREADY_QUOTED = compile('^(".+")$')
UNQUOTED_CASE_INSENSITIVE = compile("^([_A-Za-z]+[_A-Za-z0-9$]*)$")
# https://docs.snowflake.com/en/sql-reference/identifiers-syntax.html
SNOWFLAKE_UNQUOTED_ID_PATTERN = r"([a-zA-Z_][\w\$]{0,255})"
SNOWFLAKE_QUOTED_ID_PATTERN = '("([^"]|""){1,255}")'
SNOWFLAKE_ID_PATTERN = (
    f"({SNOWFLAKE_UNQUOTED_ID_PATTERN}|{SNOWFLAKE_QUOTED_ID_PATTERN})"
)
SNOWFLAKE_OBJECT_RE_PATTERN = compile(
    f"^(({SNOWFLAKE_ID_PATTERN}\\.){{0,2}}|({SNOWFLAKE_ID_PATTERN}\\.\\.)){SNOWFLAKE_ID_PATTERN}$"
)


def validate_object_name(name: str) -> None:
    if not SNOWFLAKE_OBJECT_RE_PATTERN.match(name):
        raise ValueError(f"The object name '{name}' is invalid.")


def validate_quoted_name(name: str) -> str:
    if DOUBLE_QUOTE in name[1:-1].replace(DOUBLE_QUOTE + DOUBLE_QUOTE, EMPTY_STRING):
        raise ValueError(f"Invalid Identifier {name}. "
                         f"The inside double quotes need to be escaped when the name itself is double quoted.")
    else:
        return name


def escape_quotes(unescaped: str) -> str:
    return unescaped.replace(DOUBLE_QUOTE, DOUBLE_QUOTE + DOUBLE_QUOTE)


def normalize_name(name: str) -> str:
    if ALREADY_QUOTED.match(name):
        return validate_quoted_name(name)
    elif UNQUOTED_CASE_INSENSITIVE.match(name):
        return escape_quotes(name.upper())
    else:
        return DOUBLE_QUOTE + escape_quotes(name) + DOUBLE_QUOTE


def try_single_quote_value(value: Any) -> str:
    """Single quote the value if the value is a string and not single quoted yet."""
    if value is None:
        return ""
    if (not isinstance(value, str)) or (value[0] == "'" and value[-1] == "'"):
        return str(value)
    return f"""'{value.replace("'", "''")}'"""


try:
    from snowflake.snowpark._internal.utils import parse_table_name
except ImportError:
    # Snowpark doesn't have parse_table_name until 1.5.0.
    # The following code was copied from snowpark 1.5.0.
    def parse_table_name(table_name: str) -> List[str]:
        validate_object_name(table_name)
        str_len = len(table_name)
        ret = []

        in_double_quotes = False
        i = 0
        cur_word_start_idx = 0

        while i < str_len:
            cur_char = table_name[i]
            if cur_char == '"':
                if in_double_quotes:
                    # we have to check whether this `"` is the ending of a double-quoted identifier
                    # or it's an escaping double quote
                    # to achieve this, we need to preload one more char
                    if i < str_len - 1 and table_name[i + 1] == '"':
                        # two consecutive '"', this is an escaping double quotes
                        # the pointer just keeps moving forward
                        i += 1
                    else:
                        # the double quotes indicates the ending of an identifier
                        in_double_quotes = False
                        # it should be followed by a '.' for splitting, or it should reach the end of the str
                else:
                    # this is the beginning of another double-quoted identifier
                    in_double_quotes = True
            elif cur_char == ".":
                if not in_double_quotes:
                    # this dot is to split db.schema.database
                    # we concatenate the processed chars into a string
                    # and append the string to the return list, and set our cur_word_start_idx to position after the dot
                    ret.append(table_name[cur_word_start_idx:i])
                    cur_word_start_idx = i + 1
                # else dot is part of the table name
            # else cur_char is part of the name
            i += 1

        ret.append(table_name[cur_word_start_idx:i])
        return ret


def double_quote_name(name: str) -> str:
    return DOUBLE_QUOTE + escape_quotes(name) + DOUBLE_QUOTE if name else name


def _retrieve_parameter_value(p: Dict[str, Optional[str]]) -> Optional[Union[int, bool, str, float]]:
    datatype = p["type"]
    value = p["value"]
    if datatype is None:
        raise ValueError("Data is wrong. Datatype shouldn't be None.")
    if datatype == "NUMBER":
        return int(value) if value is not None and value != "" else None
    elif datatype.startswith("NUMBER"):
        return float(value) if value is not None and value != "" else None
    elif datatype == "BOOLEAN":
        if value in (True, "true"):
            return True
        if value in ("", None):
            return None
        return False
    elif datatype == "STRING":
        return value if value != '' else None
    raise ValueError(f"datatype {datatype} isn't processed.")
