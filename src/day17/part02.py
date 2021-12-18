from src.shared.point import Point
from src.shared.square import Square
from src.day17.common import load_target_from_file, get_max_y_velocity


def get_min_x_velocity(target: Square) -> int:
    position_x = 0
    velocity_x = 0
    while position_x < target.top_left.x:
        velocity_x += 1
        position_x += velocity_x
    return velocity_x


def get_all_possible_velocities(target: Square) -> list[Point]:
    min_y_velocity = target.bottom_right.y
    max_y_velocity = get_max_y_velocity(target)
    min_x_velocity = get_min_x_velocity(target)
    max_x_velocity = target.bottom_right.x

    success_velocities: list[Point] = []
    for velocity_y in range(min_y_velocity, max_y_velocity + 1):
        for velocity_x in range(min_x_velocity, max_x_velocity + 1):
            success = run_simulation(target, velocity_x, velocity_y)
            if success:
                success_velocities.append(Point(velocity_x, velocity_y))
    return success_velocities


def run_simulation(target: Square, initial_velocity_x: int, initial_velocity_y: int) -> bool:
    cur_x_position = 0
    cur_y_position = 0
    cur_x_velocity = initial_velocity_x
    cur_y_velocity = initial_velocity_y

    while True:
        cur_x_position += cur_x_velocity
        cur_y_position += cur_y_velocity

        cur_x_velocity = max(0, cur_x_velocity - 1)
        cur_y_velocity -= 1

        if target.contains(Point(cur_x_position, cur_y_position)):
            return True
        if cur_x_position > target.bottom_right.x or cur_y_position < target.bottom_right.y:
            return False


def get_part_two_result(file_name: str) -> int:
    target = load_target_from_file(file_name)
    velocities = get_all_possible_velocities(target)

    return len(velocities)


if __name__ == "__main__":
    result = get_part_two_result("src/day17/input.txt")
    print(result)

