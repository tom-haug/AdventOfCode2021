import sys
from day01_common import count_increasing_items
sys.path.append("..")
from shared.utils import load_int_list_from_file


def get_part_one_result(file_name: str):
    items = load_int_list_from_file(file_name)
    result = count_increasing_items(items)
    return result


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)