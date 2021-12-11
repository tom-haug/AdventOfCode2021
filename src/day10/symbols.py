from enum import Enum
from functools import reduce


class Symbol(Enum):
    OPEN_PARENTHESIS = '('
    OPEN_SQUARE_BRACKET = '['
    OPEN_CURLY_BRACKET = '{'
    OPEN_ANGLE_BRACKET = '<'
    CLOSE_PARENTHESIS = ')'
    CLOSE_SQUARE_BRACKET = ']'
    CLOSE_CURLY_BRACKET = '}'
    CLOSE_ANGLE_BRACKET = '>'


OPENING_SYMBOLS = [Symbol.OPEN_PARENTHESIS, Symbol.OPEN_SQUARE_BRACKET, Symbol.OPEN_CURLY_BRACKET, Symbol.OPEN_ANGLE_BRACKET]
CLOSING_SYMBOLS = [Symbol.CLOSE_PARENTHESIS, Symbol.CLOSE_SQUARE_BRACKET, Symbol.CLOSE_CURLY_BRACKET, Symbol.CLOSE_ANGLE_BRACKET]

ILLEGAL_SYMBOL_POINTS: dict[Symbol, int] = {
    Symbol.CLOSE_PARENTHESIS: 3,
    Symbol.CLOSE_SQUARE_BRACKET: 57,
    Symbol.CLOSE_CURLY_BRACKET: 1197,
    Symbol.CLOSE_ANGLE_BRACKET: 25137,
}

COMPLETION_SYMBOL_POINTS: dict[Symbol, int] = {
    Symbol.OPEN_PARENTHESIS: 1,
    Symbol.OPEN_SQUARE_BRACKET: 2,
    Symbol.OPEN_CURLY_BRACKET: 3,
    Symbol.OPEN_ANGLE_BRACKET: 4,
}

SYMBOL_PAIRS = {
    OPENING_SYMBOLS[0]: CLOSING_SYMBOLS[0],
    OPENING_SYMBOLS[1]: CLOSING_SYMBOLS[1],
    OPENING_SYMBOLS[2]: CLOSING_SYMBOLS[2],
    OPENING_SYMBOLS[3]: CLOSING_SYMBOLS[3]
}


def compatible_symbols(opening_symbol: Symbol, closing_symbol: Symbol):
    return SYMBOL_PAIRS[opening_symbol] == closing_symbol


def get_matching_symbols(opening_symbols: list[Symbol]) -> list[Symbol]:
    return [SYMBOL_PAIRS[symbol] for symbol in opening_symbols]


def completion_points(opening_symbols: list[Symbol]):
    point_values = [COMPLETION_SYMBOL_POINTS[symbol] for symbol in opening_symbols[::-1]]
    return reduce(lambda prev, cur: (prev * 5) + cur, point_values, 0)
