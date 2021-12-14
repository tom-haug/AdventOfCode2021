import math
from src.day09.common import get_basins_from_file


def get_part_two_result(file_name: str) -> int:
    basins = get_basins_from_file(file_name)

    sorted_basin_sizes = sorted([basin.size() for basin in basins], reverse=True)
    top_three_basin_sizes = sorted_basin_sizes[:3]
    result = math.prod(top_three_basin_sizes)
    return result


if __name__ == "__main__":
    result = get_part_two_result("src/day09/input.txt")
    print(result)
