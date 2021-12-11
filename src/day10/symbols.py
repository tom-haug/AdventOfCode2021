from enum import Enum


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


def compatible_symbols(opening_symbol: Symbol, closing_symbol: Symbol):
    return OPENING_SYMBOLS.index(opening_symbol) == CLOSING_SYMBOLS.index(closing_symbol)