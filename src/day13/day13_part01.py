import numpy as np
from src.day13.day13_common import get_folded_sheet_from_file


def point_count(sheet: np.ndarray) -> int:
    return np.count_nonzero(sheet)


def get_part_one_result(file_name: str, num_folds: int = None):
    sheet = get_folded_sheet_from_file(file_name, num_folds)
    result = point_count(sheet)
    return result


if __name__ == "__main__":
    result = get_part_one_result("input.txt", 1)
    print(result)
