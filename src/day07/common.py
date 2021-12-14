from typing import Callable
from src.shared.utils import load_text_file


FuelCostCalculation = Callable[[int, int], int]


def get_min_fuel_cost(file_name: str, fuel_cost: FuelCostCalculation) -> int:
    file_contents = load_text_file(file_name)
    crab_positions = [int(position) for position in file_contents[0].split(",")]

    fuel_costs: list[int] = []
    for check_position in range(max(crab_positions)):
        cur_fuel_cost = 0
        for crab_position in crab_positions:
            cur_fuel_cost += fuel_cost(crab_position, check_position)
        fuel_costs.append(cur_fuel_cost)

    return min(fuel_costs)
