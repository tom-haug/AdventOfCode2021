from src.day17.common import load_target_from_file, get_max_y_velocity
from src.shared.square import Square


def get_part_one_result(file_name: str) -> int:
    target = load_target_from_file(file_name)
    max_y_position = get_max_y_position(target)
    return max_y_position


def get_max_y_position(target: Square) -> int:
    cur_y_velocity = get_max_y_velocity(target)
    cur_y_position = 0
    while True:
        cur_y_position += cur_y_velocity
        cur_y_velocity -= 1
        if cur_y_velocity == 0:
            return cur_y_position


if __name__ == "__main__":
    result = get_part_one_result("src/day17/input.txt")
    print(result)
