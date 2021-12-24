from __future__ import annotations

import os
import time
import numpy as np

from src.shared import load_text_file, str_to_binary_int_list


class ImageEnhancementAlgorithm:
    def __init__(self, binary_code: list[int]):
        self.binary_code = binary_code

    def process(self, input_image: np.ndarray, step: int) -> np.ndarray:
        height, width = input_image.shape

        background_value = 0 if step % 2 == 0 else 1

        output_image = np.zeros((height, width), dtype=int)

        for y in range(height):
            for x in range(width):
                code_index = self.get_code_index_for_coordinates(input_image, x, y, background_value)
                output_value = self.binary_code[code_index]
                output_image[y, x] = output_value
        return output_image

    def get_code_index_for_coordinates(self, image: np.ndarray, desired_x: int, desired_y: int, background_value: int):
        input_height, input_width = image.shape
        output_parts: list[str] = []
        for y in range(desired_y - 1, desired_y + 2):
            if 0 <= y < input_height:
                for x in range(desired_x - 1, desired_x + 2):
                    if 0 <= x < input_width:
                        value = image[y, x]
                        output_parts.append(str(value))
                    else:
                        output_parts.append(str(background_value))
            else:
                output_parts = output_parts + [str(background_value) for x in range(3)]
        value = int("".join(output_parts), 2)
        return value


def resize_array(array: np.ndarray, offset: int):
    orig_height, orig_width = array.shape
    new_array = np.zeros((orig_height + (2 * offset), orig_width + (2 * offset)), dtype=int)
    new_array[offset : -1 * offset, offset : -1 * offset] = array
    return new_array

def get_part_one_result(file_name: str, num_steps: int) -> (np.ndarray, int):
    algorithm, image = load_data_structures_from_file(file_name)
    image = resize_array(image, num_steps)
    for step in range(num_steps):
        image = algorithm.process(image, step)
        pretty_print(step, image)
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


def pretty_print(step: int, array: np.ndarray):
    width, height = array.shape
    os.system("cls")
    print("===========================================")
    print(f"Step: {step}")
    for row in range(height):
        output = ""
        for col in range(width):
            output += "#" if array[row, col] > 0 else " "
        print(output)





if __name__ == "__main__":
    start = time.time()
    image, result = get_part_one_result("src/day20/input.txt", 50)
    end = time.time()

    print(f"Running Time: {end - start}")
    print(f"Result: {result}")


# 20330 too high
# 19661 too high
18732