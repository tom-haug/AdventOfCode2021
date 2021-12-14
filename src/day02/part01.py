from src.day02.common import Command, CommandType, create_command_list, issue_commands_to_submarine


class SubmarineV1:
    def __init__(self, horizontal: int, depth: int):
        self.horizontal = horizontal
        self.depth = depth

    def issue_command(self, command: Command):
        match command:
            case Command(command_type=CommandType.forward, amount=amount):
                self.horizontal += amount
            case Command(command_type=CommandType.down, amount=amount):
                self.depth += amount
            case Command(command_type=CommandType.up, amount=amount):
                self.depth -= amount


def get_part_one_result(file_name: str):
    commands = create_command_list(file_name)
    submarine = SubmarineV1(0, 0)
    issue_commands_to_submarine(submarine, commands)
    result = submarine.horizontal * submarine.depth
    return result


if __name__ == "__main__":
    result = get_part_one_result("src/day02/input.txt")
    print(result)