from src.day07.day07_common import get_min_fuel_cost


def increasing_fuel_cost(position1: int, position2: int):
    distance = abs(position1 - position2)
    fuel_cost = 0
    for position in range(distance):
        fuel_cost += position + 1
    return fuel_cost


def get_part_two_result(file_name: str) -> int:
    return get_min_fuel_cost(file_name, increasing_fuel_cost)


if __name__ == "__main__":
    total_fuel = get_part_two_result("input.txt")
    print(total_fuel)
