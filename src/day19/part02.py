from __future__ import annotations

from src.day19.common import load_scanners_from_file, combine_scanners
from src.shared import Point3D


def get_part_two_result(file_name: str) -> int:
    scanners = load_scanners_from_file(file_name)
    combined_scanner, scanner_locations = combine_scanners(scanners)
    furthest_distance = calculate_furthest_manhattan_distance(scanner_locations)
    return furthest_distance


def calculate_furthest_manhattan_distance(scanner_locations: list[Point3D]) -> int:
    cur_max_distance = 0
    for idx, location1 in enumerate(scanner_locations):
        for location2 in scanner_locations[idx+1:]:
            delta_x = abs(location1.x - location2.x)
            delta_y = abs(location1.y - location2.y)
            delta_z = abs(location1.z - location2.z)
            distance = delta_x + delta_y + delta_z
            if distance > cur_max_distance:
                cur_max_distance = distance
    return cur_max_distance


if __name__ == "__main__":
    result = get_part_two_result("src/day19/input.txt")
    print(result)
