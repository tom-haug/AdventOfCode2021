import math
from enum import Enum
from typing import Callable, Optional

OnExplode = Callable[['SnailStatement', Optional[int], Optional[int]], None]


class Direction(Enum):
    LEFT = 1
    RIGHT = 2


def exploding_criteria(statement: 'SnailStatement', depth: int): return statement.children_literal and depth > 3
def splitting_criteria(statement: 'SnailStatement', _): return statement.is_literal and statement.literal_value >= 10


class SnailStatement:
    literal_value: Optional[int]
    left_child: Optional['SnailStatement']
    right_child: Optional['SnailStatement']

    def __init__(self, statement_text: str, on_explode: OnExplode):
        self.literal_value = None
        self.left_child = None
        self.right_child = None
        self.on_explode = on_explode
        self.parse(statement_text)

    @property
    def is_literal(self) -> bool:
        return self.literal_value is not None

    @property
    def children_literal(self) -> bool:
        return self.literal_value is None and self.left_child.is_literal and self.right_child.is_literal

    @property
    def magnitude(self) -> int:
        if self.is_literal:
            return self.literal_value
        else:
            return (self.left_child.magnitude * 3) + (self.right_child.magnitude * 2)

    def parse(self, statement_text: str):
        if statement_text[0] == "[":
            statement_text = statement_text[1:-1]
        if len(statement_text) == 0:
            return
        separator_idx = get_separator_idx(statement_text)
        if separator_idx == -1:
            self.literal_value = int(statement_text)
        else:
            left_statement_text = statement_text[: separator_idx]
            right_statement_text = statement_text[separator_idx + 1:]
            self.left_child = SnailStatement(left_statement_text, self.propigate_explosion)
            self.right_child = SnailStatement(right_statement_text, self.propigate_explosion)

    def __add__(self, other: 'SnailStatement') -> 'SnailStatement':
        result = SnailStatement("[]", self.on_explode)
        result.left_child = self
        result.right_child = other
        result.left_child.on_explode = result.propigate_explosion
        result.right_child.on_explode = result.propigate_explosion
        return result

    def __repr__(self) -> str:
        if self.is_literal:
            return str(self.literal_value)
        else:
            left_repr = str(self.left_child)
            right_repr = str(self.right_child)
            return f"[{left_repr},{right_repr}]"

    def try_explode(self) -> bool:
        found_statement = self._recursive_search(0, exploding_criteria)

        if found_statement is not None:
            found_statement._explode()
            return True

    def try_split(self) -> bool:
        found_statement = self._recursive_search(0, splitting_criteria)

        if found_statement is not None:
            found_statement._split()
            return True

    def _explode(self):
        if not self.children_literal:
            raise Exception(f"Cannot explode statement: {str(self)}")

        self.literal_value = 0
        left_value = self.left_child.literal_value
        right_value = self.right_child.literal_value
        self.left_child = None
        self.right_child = None
        self.on_explode(self, left_value, right_value)

    def _split(self):
        if not self.is_literal:
            raise Exception(f"Cannot split: {str(self)}")
        left_value = math.floor(self.literal_value / 2.0)
        right_value = math.ceil(self.literal_value / 2.0)

        self.literal_value = None
        self.left_child = SnailStatement(f"[{str(left_value)}]", self.propigate_explosion)
        self.right_child = SnailStatement(f"[{str(right_value)}]", self.propigate_explosion)

    def send_explosion(self, value: int, send_direction: Direction):
        if self.is_literal:
            self.literal_value += value
            return

        match send_direction:
            case Direction.LEFT:
                self.right_child.send_explosion(value, send_direction)
            case Direction.RIGHT:
                self.left_child.send_explosion(value, send_direction)

    def propigate_explosion(self, from_statement: 'SnailStatement', left_value: int = None, right_value: int = None):
        if from_statement == self.left_child and left_value is not None:
            self.on_explode(self, left_value, None)
        if from_statement == self.left_child and right_value is not None:
            self.right_child.send_explosion(right_value, Direction.RIGHT)
        if from_statement == self.right_child and right_value is not None:
            self.on_explode(self, None, right_value)
        if from_statement == self.right_child and left_value is not None:
            self.left_child.send_explosion(left_value, Direction.LEFT)

    def _recursive_search(self, current_depth: int, search_criteria: Callable[['SnailStatement', int], bool]) -> 'SnailStatement':
        if search_criteria(self, current_depth):
            return self

        if not self.is_literal:
            left_result = self.left_child._recursive_search(current_depth + 1, search_criteria)
            if left_result is not None:
                return left_result

            right_result = self.right_child._recursive_search(current_depth + 1, search_criteria)
            if right_result is not None:
                return right_result
        return None


def get_separator_idx(statement_text: str) -> int:
    open_count = 0
    for idx, char in enumerate(statement_text):
        match char:
            case "[":
                open_count += 1
            case "]":
                open_count -= 1
            case ",":
                if open_count == 0:
                    return idx
    return -1
