from utils import FlexibleIterator

class UnExpectedSpaceToken(Exception):
    pass

PRIORITY_ORDER = (
    "IMPORT",
    "ENDL",
)

BOTH = (
    "SEMICOLON",
    "AS",
    "IMPORT",
    "DOUBLE_STAR",
    "DOT",
    "LEFT_SQUARE_BRACKET",
    "LEFT_PARENTHESIS",
    "STAR",
    "SLASH",
    "PERCENT",
    "DOUBLE_SLASH",
    "PLUS",
    "MINUS",
    "LEFT_SHIFT",
    "RIGHT_SHIFT",
    "AMPER",
    "CIRCUMFLEX",
    "VBAR",
    "LESS",
    "GREATER",
    "EQUAL_EQUAL",
    "LESS_EQUAL",
    "GREATER_EQUAL",
    "NOT_EQUAL",
    "IN",
    "IS",
    "NOT",
    "AND",
    "OR",
    "IF",
    "ELSE",
    "EQUAL",
    "PLUS_EQUAL",
    "MINUS_EQUAL",
    "STAR_EQUAL",
    "SLASH_EQUAL",
    "PERCENT_EQUAL",
    "AMPER_EQUAL",
    "VBAR_EQUAL",
    "CIRCUMFLEX_EQUAL",
    "LEFT_SHIFT_EQUAL",
    "RIGHT_SHIFT_EQUAL",
    "DOUBLE_STAR_EQUAL",
    "DOUBLE_SLASH_EQUAL",
    "ENDL",
    "COMMA",
    "FOR",
    "COLON",
    "STRING",
    "RAW_STRING",
    "UNICODE_STRING",
    "UNICODE_RAW_STRING",
    "BINARY_STRING",
    "BINARY_RAW_STRING",
    "BACKQUOTE",
)

GROUP_SPACE_BEFORE = BOTH + (
    "RIGHT_PARENTHESIS",
    "COMMENT",
)

GROUP_SPACE_AFTER = BOTH + (
    "FROM",
    "TILDE",
    "RETURN",
    "YIELD",
    "WITH",
    "DEL",
    "ASSERT",
    "RAISE",
    "EXEC",
    "GLOBAL",
    "PRINT",
    "INDENT",
    "WHILE",
    "ELIF",
    "EXCEPT",
    "DEF",
    "CLASS",
    "LAMBDA",
)

def less_prioritary_than(a, b):
    if b not in PRIORITY_ORDER:
        return False

    if a not in PRIORITY_ORDER:
        return True

    return PRIORITY_ORDER.index(a) < PRIORITY_ORDER.index(b)

def group(sequence):
    return list(group_generator(sequence))


def group_generator(sequence):
    iterator = FlexibleIterator(sequence)
    current = None, None
    while True:
        if iterator.end():
            return

        current = iterator.next()

        if current is None:
            return

        if current[0] in ("SPACE", "COMMENT") and iterator.show_next() and iterator.show_next()[0] in GROUP_SPACE_BEFORE:
            new_current = iterator.next()
            current = (new_current[0], new_current[1], [current])

        if current[0] in GROUP_SPACE_AFTER and\
            (iterator.show_next() and iterator.show_next()[0] in ("SPACE", "COMMENT")) and\
            (not iterator.show_next(2) or (iterator.show_next(2) and not less_prioritary_than(current[0], iterator.show_next(2)[0]))):
            after_space = iterator.next()
            current = (current[0], current[1], current[2] if len(current) > 2 else [], [after_space])

        yield current
