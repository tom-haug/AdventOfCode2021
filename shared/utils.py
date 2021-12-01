import os
import sys


def load_int_list_from_file(file_name: str) -> list[str]:
    file_contents = load_text_file(file_name)
    return [int(line) for line in file_contents]


def load_text_file(file_name: str) -> list[str]:
    file_path = os.path.join(sys.path[0], file_name)
    f = open(file_path, "r")
    file_contents = f.read()
    f.close()
    return file_contents.splitlines()
