from day02_common import Command, CommandType, create_command_list, issue_commands_to_submarine


class SubmarineV2:
    def __init__(self, horizontal: int, depth: int, aim: int):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    def issue_command(self, command: Command):
        match command:
            case Command(command_type=CommandType.forward, amount=amount):
                self.horizontal += amount
                self.depth += (amount * self.aim)
            case Command(command_type=CommandType.down, amount=amount):
                self.aim += amount
            case Command(command_type=CommandType.up, amount=amount):
                self.aim -= amount


def get_part_two_result(file_name: str):
    commands = create_command_list(file_name)
    submarine = SubmarineV2(0, 0, 0)
    issue_commands_to_submarine(submarine, commands)
    result = submarine.horizontal * submarine.depth
    return result


if __name__ == "__main__":
    result = get_part_two_result("input.txt")
    print(result)