import functools
import math
from enum import Enum
from typing import Callable, Optional

from attr import dataclass

from src.day17.common import load_target_from_file, get_max_y_velocity
from src.shared.utils import load_text_file

OnExplode = Callable[['SnailStatement', Optional[int], Optional[int]], None]

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

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


    def __add__(self, other: 'SnailStatement') -> 'SnailStatement':
        result = SnailStatement("[]", self.on_explode)
        result.left_child = self
        result.right_child = other
        result.left_child.on_explode = result.propigate_explosion
        result.right_child.on_explode = result.propigate_explosion
        return result

    def __repr__(self):
        if self.is_literal:
            return str(self.literal_value)
        else:
            left_repr = str(self.left_child)
            right_repr = str(self.right_child)
            return f"[{left_repr},{right_repr}]"

    def explode(self):
        if not self.children_literal:
            raise Exception(f"Cannot explode statement: {str(self)}")
        self.literal_value = 0
        left_value = self.left_child.literal_value
        right_value = self.right_child.literal_value
        self.left_child = None
        self.right_child = None
        self.on_explode(self, left_value, right_value)

    def split(self):
        if not self.is_literal:
            raise Exception(f"Cannot split: {str(self)}")
        left_value = math.floor(self.literal_value / 2.0)
        right_value = math.ceil(self.literal_value / 2.0)

        self.literal_value = None
        self.left_child = SnailStatement(f"[{str(left_value)}]", self.propigate_explosion)
        self.right_child = SnailStatement(f"[{str(right_value)}]", self.propigate_explosion)

    def send_explosion(self, value: int, to_direction: Direction):
        if self.is_literal:
            self.literal_value += value
            return

        match to_direction:
            case Direction.LEFT:
                self.right_child.send_explosion(value, to_direction)
            case Direction.RIGHT:
                self.left_child.send_explosion(value, to_direction)

    def propigate_explosion(self, from_statement: 'SnailStatement', left_value: int = None, right_value: int = None):
        if from_statement == self.left_child and left_value is not None:
            self.on_explode(self, left_value, None)
        if from_statement == self.left_child and right_value is not None:
                self.right_child.send_explosion(right_value, Direction.RIGHT)
        if from_statement == self.right_child and right_value is not None:
            self.on_explode(self, None, right_value)
        if from_statement == self.right_child and left_value is not None:
                self.left_child.send_explosion(left_value, Direction.LEFT)

@dataclass
class SnailStatementAndDepth:
    statement: SnailStatement
    depth: int


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


def add_statements(statements: list[SnailStatement]) -> SnailStatement:
    master_statement = statements[0]
    for statement in statements[1:]:
        master_statement = master_statement + statement
        reduce_statement(master_statement)
    return master_statement

def reduce_statement(statement: SnailStatement):
    keep_going = True
    def exploding_criteria(statement: SnailStatement, depth: int): return statement.children_literal and depth > 3
    def splitting_criteria(statement: SnailStatement, _): return statement.is_literal and statement.literal_value >= 10
    while True:
        statement_to_explode = recursive_search(statement, 0, exploding_criteria)
        if statement_to_explode is not None:
            statement_to_explode.statement.explode()
            continue

        statement_to_split = recursive_search(statement, 0, splitting_criteria)
        if statement_to_split is not None:
            statement_to_split.statement.split()
            continue
        break

def recursive_search(statement: SnailStatement, current_depth: int, search_criteria: Callable[[SnailStatement, int], bool]) -> SnailStatementAndDepth:
    if search_criteria(statement, current_depth):
        return SnailStatementAndDepth(statement, current_depth)

    if not statement.is_literal:
        left_result = recursive_search(statement.left_child, current_depth + 1, search_criteria)
        if left_result is not None:
            return left_result

        right_result = recursive_search(statement.right_child, current_depth + 1, search_criteria)
        if right_result is not None:
            return right_result
    return None


def load_statements_from_file(file_name: str):
    lines = load_text_file(file_name)
    statements = [SnailStatement(line, lambda *_: None) for line in lines]
    master_statement = add_statements(statements)
    return master_statement


def get_part_one_result(file_name: str) -> int:
    master_statement = load_statements_from_file(file_name)
    magnitude = master_statement.magnitude
    return magnitude


if __name__ == "__main__":
    result = get_part_one_result("src/day18/input.txt")
    print(result)
