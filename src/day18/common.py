from src.day18.snail_statement import SnailStatement
from src.shared import load_text_file


def add_statements(statements: list[SnailStatement]) -> SnailStatement:
    master_statement = statements[0]
    for statement in statements[1:]:
        master_statement = master_statement + statement
        reduce_statement(master_statement)
    return master_statement


def reduce_statement(statement: SnailStatement):
    while True:
        if statement.try_explode():
            continue

        if statement.try_split():
            continue
        break


def load_statements_from_file(file_name: str) -> list[SnailStatement]:
    lines = load_text_file(file_name)
    statements = [SnailStatement(line, lambda *_: None) for line in lines]
    return statements
