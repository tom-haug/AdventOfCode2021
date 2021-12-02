import day02_common as common


class SubmarineV2:
    def __init__(self, horizontal: int, depth: int, aim: int):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    def issue_command(self, command: common.Command):
        match command:
            case common.Command(command_type=common.CommandType.forward, amount=amount):
                self.horizontal += amount
                self.depth += (amount * self.aim)
            case common.Command(command_type=common.CommandType.down, amount=amount):
                self.aim += amount
            case common.Command(command_type=common.CommandType.up, amount=amount):
                self.aim -= amount


def get_part_two_result(file_name: str):
    commands = common.create_command_list(file_name)
    submarine = SubmarineV2(0, 0, 0)
    common.issue_commands_to_submarine(submarine, commands)
    result = submarine.horizontal * submarine.depth
    return result


if __name__ == "__main__":
    result = get_part_two_result("input.txt")
    print(result)