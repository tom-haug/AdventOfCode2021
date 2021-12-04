import os
import sys
import pandas as pd


def load_int_list_from_file(file_name: str) -> list[int]:
    file_contents = load_text_file(file_name)
    return [int(line) for line in file_contents]


def load_int_data_frame_from_file(file_name: str) -> pd.DataFrame:
    file_contents = load_text_file(file_name)
    return pd.DataFrame([[int(char) for char in line] for line in file_contents])


def load_text_file(file_name: str) -> list[str]:
    file_path = os.path.join(sys.path[0], file_name)
    f = open(file_path, "r")
    file_contents = f.read()
    f.close()
    return file_contents.splitlines()


def bit_list_to_number(bit_list: list[int]):
    result = 0
    for bit in bit_list:
        result = (result << 1) | bit
    return result

