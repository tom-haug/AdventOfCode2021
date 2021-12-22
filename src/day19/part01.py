from __future__ import annotations
import time

from src.day19.common import load_scanners_from_file, combine_scanners


def get_part_one_result(file_name: str) -> int:
    scanners = load_scanners_from_file(file_name)
    combined_scanner = combine_scanners(scanners)
    return len(combined_scanner[0].beacons)


if __name__ == "__main__":
    start = time.time()
    result = get_part_one_result("src/day19/input.txt")
    end = time.time()

    print(f"Running Time: {end - start}")
    print(result)
