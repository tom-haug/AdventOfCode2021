import sys

sys.path.append("..")
from shared.utils import load_int_list_from_file


def get_part_one_result(items: list[int]):
    total = 0
    for idx in range(1, len(items)):
        if items[idx] > items[idx - 1]:
            total += 1
    return total


if __name__ == "__main__":
    items = load_int_list_from_file("input.txt")
    print(items)
    result = get_part_one_result(items)
    print(result)