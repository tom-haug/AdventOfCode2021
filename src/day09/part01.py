from src.day09.common import get_basins_from_file


def risk_level(height: int):
    return height + 1


def get_part_one_result(file_name: str) -> int:
    basins = get_basins_from_file(file_name)
    return sum([risk_level(basin.origin.value) for basin in basins])


if __name__ == "__main__":
    result = get_part_one_result("src/day09/input.txt")
    print(result)

