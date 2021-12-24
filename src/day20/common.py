import os

import numpy as np

from src.day20.image_enhancement_algorithm import ImageEnhancementAlgorithm
from src.shared import load_text_file, str_to_binary_int_list


def get_image_after_steps(file_name: str, num_steps: int, visualize: bool) -> (np.ndarray, int):
    algorithm, image = load_data_structures_from_file(file_name)
    image = resize_array(image, num_steps)

    for step in range(num_steps):
        image = algorithm.process(image, step)
        if visualize:
            pretty_print(step, image)
    num_pixels = np.count_nonzero(image)
    return image, num_pixels


def load_data_structures_from_file(file_name: str) -> (ImageEnhancementAlgorithm, np.ndarray):
    lines = load_text_file(file_name)
    binary_algorithm = str_to_binary_int_list(lines[0], is_hash)
    raw_binary_input_image = [str_to_binary_int_list(line, is_hash) for line in lines[2:]]

    algorithm = ImageEnhancementAlgorithm(binary_algorithm)
    image = np.array(raw_binary_input_image)

    return algorithm, image


def resize_array(array: np.ndarray, offset: int):
    orig_height, orig_width = array.shape
    new_array = np.zeros((orig_height + (2 * offset), orig_width + (2 * offset)), dtype=int)
    new_array[offset : -1 * offset, offset : -1 * offset] = array
    return new_array


def is_hash(char: str) -> bool:
    return char == "#"


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
