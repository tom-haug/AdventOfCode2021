import day02_common as common


class SubmarineV1:
    def __init__(self, horizontal: int, depth: int):
        self.horizontal = horizontal
        self.depth = depth

    def issue_command(self, command: common.Command):
        match command:
            case common.Command(command_type=common.CommandType.forward, amount=amount):
                self.horizontal += amount
            case common.Command(command_type=common.CommandType.down, amount=amount):
                self.depth += amount
            case common.Command(command_type=common.CommandType.up, amount=amount):
                self.depth -= amount


def get_part_one_result(file_name: str):
    commands = common.create_command_list(file_name)
    submarine = SubmarineV1(0, 0)
    common.issue_commands_to_submarine(submarine, commands)
    result = submarine.horizontal * submarine.depth
    return result


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)