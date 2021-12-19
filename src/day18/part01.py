from src.day18.common import load_statements_from_file, add_statements


def get_part_one_result(file_name: str) -> int:
    statements = load_statements_from_file(file_name)
    master_statement = add_statements(statements)
    magnitude = master_statement.magnitude
    return magnitude


if __name__ == "__main__":
    result = get_part_one_result("src/day18/input.txt")
    print(result)
