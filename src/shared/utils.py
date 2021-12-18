import os
import __main__
from enum import Enum
from math import log2

import numpy as np
import pandas as pd


def load_int_list_from_file(file_name: str) -> list[int]:
    file_contents = load_text_file(file_name)
    return [int(line) for line in file_contents]


def load_int_data_frame_from_file(file_name: str) -> pd.DataFrame:
    file_contents = load_text_file(file_name)
    return pd.DataFrame([[int(char) for char in line] for line in file_contents])


def load_int_nparray_from_file(file_name: str) -> np.ndarray:
    file_contents = load_text_file(file_name)
    return np.array([[int(x) for x in list(line)] for line in file_contents])


def load_text_file(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents.splitlines()


def bit_list_to_number(bit_list: list[int]):
    result = 0
    for bit in bit_list:
        result = (result << 1) | bit
    return result


def bitwise_not(number, num_bits):
    return (1 << num_bits) - 1 - number


def middle_item(items: list) -> int:
    length = len(items)
    if length % 2 == 0:
        raise Exception("cannot get middle item for an even number of items")
    middle_index = int((length - 1) / 2)
    return items[middle_index]


class NumberSystem(Enum):
    BINARY = 2
    DECIMAL = 10
    HEXADECIMAL = 26


def to_binary(value: str, number_base: NumberSystem) -> str:
    binary_string = ""
    bits_per_digit = int(log2(number_base.value))
    for char in value:
        binary_char_value = bin(int(char, number_base.value))[2:].zfill(bits_per_digit)
        binary_string += binary_char_value
    return binary_string
