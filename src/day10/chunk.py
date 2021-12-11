from typing import Deque

from src.day10.symbols import Symbol, OPENING_SYMBOLS, CLOSING_SYMBOLS, compatible_symbols
from collections import deque


class Chunk:
    def __init__(self, code: str):
        self.code: list[Symbol] = [Symbol(char) for char in code]

    def parse(self) -> (bool, Symbol, list[Symbol]):
        opening_symbols: Deque[Symbol] = deque()
        for idx, symbol in enumerate(self.code):
            if symbol in OPENING_SYMBOLS:
                opening_symbols.append(symbol)
            elif symbol in CLOSING_SYMBOLS:
                if compatible_symbols(opening_symbols[-1], symbol):
                    opening_symbols.pop()
                else:
                    return False, symbol, opening_symbols
            else:
                raise Exception("unknown symbol type")
        return True, None, list(opening_symbols)

    def __repr__(self):
        return "".join([symbol.value for symbol in self.code])
