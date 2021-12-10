import numpy as np

from src.shared.utils import load_text_file


def find_relative_minimums(height_map: np.ndarray):
    width, height = height_map.shape
    low_point_values: list[int] = []
    for x in range(width):
        for y in range(height):
            cur_value = height_map[x, y]
            is_minimum = True
            if x > 0 and cur_value >= height_map[x - 1, y]:
                is_minimum = False
            elif x < width - 1 and cur_value >= height_map[x + 1, y]:
                is_minimum = False
            elif y > 0 and cur_value >= height_map[x, y - 1]:
                is_minimum = False
            elif y < height - 1 and cur_value >= height_map[x, y + 1]:
                is_minimum = False

            if is_minimum:
                low_point_values.append(cur_value)
    return low_point_values


def risk_level(height: int):
    return height + 1


def get_part_one_result(file_name: str) -> int:
    file_contents = load_text_file(file_name)
    height_map = np.array([[int(x) for x in list(line)] for line in file_contents])
    low_point_values = find_relative_minimums(height_map)
    return sum([risk_level(value) for value in low_point_values])


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)

