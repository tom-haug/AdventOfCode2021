from typing import Deque

from src.day10.symbols import Symbol, OPENING_SYMBOLS, CLOSING_SYMBOLS, compatible_symbols
from collections import deque


class Chunk:
    def __init__(self, code: str):
        self.code: list[Symbol] = [Symbol(char) for char in code]

    def is_valid(self) -> (bool, Symbol):
        opening_symbol_stack: Deque[Symbol] = deque()
        for idx, symbol in enumerate(self.code):
            if symbol in OPENING_SYMBOLS:
                opening_symbol_stack.append(symbol)
            elif symbol in CLOSING_SYMBOLS:
                if compatible_symbols(opening_symbol_stack[-1], symbol):
                    opening_symbol_stack.pop()
                else:
                    return False, symbol
            else:
                raise Exception("unknown symbol type")
        return True, None