from src.day07.common import get_min_fuel_cost


def linear_fuel_cost(position1: int, position2: int):
    distance = abs(position1 - position2)
    return distance


def get_part_one_result(file_name: str) -> int:
    return get_min_fuel_cost(file_name, linear_fuel_cost)


if __name__ == "__main__":
    total_fuel = get_part_one_result("src/day07/input.txt")
    print(total_fuel)
