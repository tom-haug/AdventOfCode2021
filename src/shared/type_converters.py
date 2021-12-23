from math import log2
from typing import Callable

from src.shared import NumberSystem


def bit_list_to_number(bit_list: list[int]):
    result = 0
    for bit in bit_list:
        result = (result << 1) | bit
    return result


def to_binary(value: str, number_base: NumberSystem) -> str:
    binary_string = ""
    bits_per_digit = int(log2(number_base.value))
    for char in value:
        binary_char_value = bin(int(char, number_base.value))[2:].zfill(bits_per_digit)
        binary_string += binary_char_value
    return binary_string


def str_to_binary_str(input: str, one_condition: Callable[[str], bool]):
    int_list = str_to_binary_int_list(input, one_condition)
    return "".join([str(digit) for digit in int_list])


def str_to_binary_int_list(input: str, one_condition: Callable[[str], bool]):
    return [1 if one_condition(char) else 0 for char in input]
