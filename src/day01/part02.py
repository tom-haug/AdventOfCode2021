from src.day01.common import reduce_three_measurement_sum, count_increasing_items
from src.shared import load_int_list_from_file


def get_part_two_result(file_name: str):
    items = load_int_list_from_file(file_name)
    reduced_items = reduce_three_measurement_sum(items)
    result = count_increasing_items(reduced_items)
    return result


if __name__ == "__main__":
    result = get_part_two_result("src/day01/input.txt")
    print(result)