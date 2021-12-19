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