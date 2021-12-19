from enum import Enum
from src.shared import load_text_file


class CommandType(Enum):
    forward = 1
    down = 2
    up = 3


class Command:
    def __init__(self, command_type: CommandType, amount: int):
        self.command_type = command_type
        self.amount = amount


def create_command_list(file_name: str) -> list[Command]:
    lines = load_text_file(file_name)
    commands: list[Command] = []
    for line in lines:
        line_parts = line.split(' ')
        command_type = CommandType[line_parts[0]]
        amount = int(line_parts[1])
        commands.append(Command(command_type, amount))
    return commands


def issue_commands_to_submarine(submarine, commands: list[Command]):
    for command in commands:
        submarine.issue_command(command)
