import sys
from day01_common import reduce_three_measurement_sum, count_increasing_items
sys.path.append("..")
from shared.utils import load_int_list_from_file


def get_part_two_result(file_name: str):
    items = load_int_list_from_file(file_name)
    reduced_items = reduce_three_measurement_sum(items)
    result = count_increasing_items(reduced_items)
    return result


if __name__ == "__main__":
    result = get_part_two_result("input.txt")
    print(result)