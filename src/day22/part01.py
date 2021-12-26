from __future__ import annotations
import time
from src.day22.common import get_final_on_volume


def get_part_one_result(file_name: str):
    return get_final_on_volume(file_name, True)


if __name__ == "__main__":
    start = time.time()
    result = get_part_one_result("src/day22/input.txt")
    end = time.time()

    print(f"Running Time: {end - start}")
    print(f"Result: {result}")
