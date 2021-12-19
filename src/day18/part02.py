import copy

from src.day18.common import load_statements_from_file, add_statements
from src.day18.snail_statement import SnailStatement


def get_part_two_result(file_name: str) -> int:
    statements = load_statements_from_file(file_name)
    magnitude = find_max_pair_magnitude(statements)
    return magnitude


def find_max_pair_magnitude(statements: list[SnailStatement]):
    max_magnitude = 0
    for statement1 in statements:
        for statement2 in statements:
            if statement1 == statement2:
                continue
            combined = add_statements([copy.deepcopy(statement1), copy.deepcopy(statement2)])
            magnitude = combined.magnitude
            if magnitude > max_magnitude:
                max_magnitude = magnitude
    return max_magnitude


if __name__ == "__main__":
    result = get_part_two_result("src/day18/input.txt")
    print(result)

