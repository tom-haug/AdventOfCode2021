from src.day01.common import count_increasing_items
from src.shared.utils import load_int_list_from_file


def get_part_one_result(file_name: str):
    items = load_int_list_from_file(file_name)
    result = count_increasing_items(items)
    return result


if __name__ == "__main__":
    result = get_part_one_result('src/day01/input.txt')
    print(result)
