from __future__ import annotations
import time
import numpy as np

from src.shared import load_text_file, str_to_binary_int_list


class ImageEnhancementAlgorithm:
    def __init__(self, binary_code: list[int]):
        self.binary_code = binary_code

    def process(self, input_image: np.ndarray) -> np.ndarray:
        input_height, input_width = input_image.shape
        # make output one larger in every direction every time - find a better way to handle expansion
        output_height = input_height + 2
        output_width = input_width + 2
        output_image = np.zeros((output_height, output_width), dtype=int)

        for y in range(output_height):
            for x in range(output_width):
                code_index = self.get_code_index_for_coordinates(input_image, x - 1, y - 1)
                output_value = self.binary_code[code_index]
                output_image[y, x] = output_value
        return output_image

    def get_code_index_for_coordinates(self, image: np.ndarray, desired_x: int, desired_y: int):
        input_height, input_width = image.shape
        #  warning - x and y can be outside the bounds of the image here
        output_parts = np.zeros((0, 3), dtype=int)
        for y in range(desired_y - 1, desired_y + 2):
            output_part = np.zeros(3, dtype=int)
            if 0 <= y < input_height:
                for idx, x in enumerate(range(desired_x - 1, desired_x + 2)):
                    if 0 <= x < input_width:
                        value = image[y, x]
                        output_part[idx] = value
            output_parts = np.vstack((output_parts, output_part))
        flattened = [str(x) for x in output_parts.flatten()]
        value = int("".join(flattened), 2)
        return value


def get_part_one_result(file_name: str, num_steps: int) -> (np.ndarray, int):
    algorithm, image = load_data_structures_from_file(file_name)
    for step in range(num_steps):
        image = algorithm.process(image)
    result = np.count_nonzero(image)
    return image, result


def is_hash(char: str) -> bool:
    return char == "#"


def load_data_structures_from_file(file_name: str) -> (ImageEnhancementAlgorithm, np.ndarray):
    lines = load_text_file(file_name)
    binary_algorithm = str_to_binary_int_list(lines[0], is_hash)
    raw_binary_input_image = [str_to_binary_int_list(line, is_hash) for line in lines[2:]]

    algorithm = ImageEnhancementAlgorithm(binary_algorithm)
    image = np.array(raw_binary_input_image)

    return algorithm, image


def pretty_print(array: np.ndarray):
    width, height = array.shape
    for row in range(height):
        output = ""
        for col in range(width):
            output += "#" if array[row, col] > 0 else " "
        print(output)


if __name__ == "__main__":
    start = time.time()
    image, result = get_part_one_result("src/day20/input.txt", 2)
    end = time.time()

    print(f"Running Time: {end - start}")
    pretty_print(image)
    print(f"Result: {result}")
