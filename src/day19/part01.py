from __future__ import annotations

import copy
import math
import re
from enum import Enum

from attr import dataclass

from src.shared import load_text_file, Point3D

"""
silly arbitrary number obtained from trial and error
"""
SAME_BEACON_CONNECTION_THRESHOLD = 10


class RelativeDirection(Enum):
    FORWARD = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    REVERSE = 5


class Beacon(Point3D):
    distances_to_other_beacons: list[float] = []

    def rotate_relative_direction(self, direction: RelativeDirection):
        match direction:
            case RelativeDirection.FORWARD:
                ...
            case RelativeDirection.LEFT:
                orig_x = self.x
                self.x = self.z
                self.z = -1 * orig_x
            case RelativeDirection.RIGHT:
                orig_x = self.x
                self.x = -1 * self.z
                self.z = orig_x
            case RelativeDirection.REVERSE:
                self.x = -1 * self.x
                self.z = -1 * self.z
            case RelativeDirection.UP:
                orig_z = self.z
                self.z = self.y
                self.y = -1 * orig_z
            case RelativeDirection.DOWN:
                orig_z = self.z
                self.z = -1 * self.y
                self.y = orig_z

    def rotate_xy(self, degrees: int):
        for increment in range(0, degrees + 90, 90):
            orig_y = self.y
            self.y = self.x
            self.x = -1 * orig_y

    def __eq__(self, other: Beacon):
        return self.x == other.x and self.y == other.y and self.z == other.z


class Scanner:
    def __init__(self, id: int):
        self.id: int = id
        self.beacons: list[Beacon] = []

    def rotated_beacons_view(self, direction: RelativeDirection, xy_rotation: int) -> list[Beacon]:
        new_beacons: list[beacon] = []
        for beacon in self.beacons:
            new_beacon = Beacon(beacon.x, beacon.y, beacon.z)
            new_beacon.rotate_relative_direction(direction)
            new_beacon.rotate_xy(xy_rotation)
            new_beacons.append(new_beacon)
        return new_beacons

    def beacon_exists(self, beacon: Beacon):
        return len([x for x in self.beacons if x == beacon]) > 0

    def append_beacons(self, new_beacons: list[Beacon]):
        for new_beacon in new_beacons:
            if not self.beacon_exists(new_beacon):
                print("ADD BEACON")
                self.beacons.append(new_beacon)
        calculate_distance_between_beacons(self.beacons)


def calculate_distance_between_beacons(beacons: list[Beacon]):
    for beacon in beacons:
        beacon.distances_to_other_beacons = []

    for idx, beacon1 in enumerate(beacons):
        for beacon2 in beacons[idx + 1:]:
            distance = math.sqrt(
                math.pow(beacon2.x - beacon1.x, 2) +
                math.pow(beacon2.y - beacon1.y, 2) +
                math.pow(beacon2.z - beacon1.z, 2)
            )

            beacon1.distances_to_other_beacons.append(distance)
            beacon2.distances_to_other_beacons.append(distance)


def get_part_one_result(file_name: str) -> int:
    scanners = load_scanners_from_file(file_name)
    process(scanners)
    return


def process(scanners: list[Scanner]):
    keep_going = True
    while keep_going:
        print(f"Scanner Count: {len(scanners)}")
        keep_going = assimilate_more(scanners)
    [print(len(scanner.beacons)) for scanner in scanners]

def assimilate_more(scanners) -> bool:
    for idx, cur_scanner in enumerate(scanners):
        for other_scanner in scanners[idx + 1:]:
            same_beacons = find_beacons_with_same_distance_to_other_beacons(cur_scanner.beacons, other_scanner.beacons)
            print(f"Same Beacon Count: {len(same_beacons)}")
            if len(same_beacons) >= 12:
                print(f"id1: {cur_scanner.id}, id2:{other_scanner.id}, same beacons: {len(same_beacons)}")
                direction, xy_rotation = find_rotation(same_beacons[0], same_beacons[1])

                if direction is None or xy_rotation is None:
                    raise Exception("Cannot find rotation beacon. This should never happen")

                print("apply rotation to all")
                rotate_beacons(other_scanner.beacons, direction, xy_rotation)

                print("Rotated Same beacons: ")
                x_offset = same_beacons[0][0].x - same_beacons[0][1].x
                y_offset = same_beacons[0][0].y - same_beacons[0][1].y
                z_offset = same_beacons[0][0].z - same_beacons[0][1].z

                offset_beacons(other_scanner.beacons, x_offset, y_offset, z_offset)

                print("ADDING BEACONS")
                cur_scanner.append_beacons(other_scanner.beacons)
                scanners.remove(other_scanner)
                return True
    return False


def rotate_beacons(beacons: list[Beacon], direction: RelativeDirection, xy_rotation: int):
    for beacon in beacons:
        beacon.rotate_relative_direction(direction)
        beacon.rotate_xy(xy_rotation)


def offset_beacons(beacons: list[Beacon], x: int, y: int, z: int):
    for beacon in beacons:
        beacon.x += x
        beacon.y += y
        beacon.z += z


def find_rotation(beacon_pair1: tuple[Beacon, Beacon], beacon_pair2: tuple[Beacon, Beacon]) -> (RelativeDirection, int):
    for direction in RelativeDirection:
        for xy_rotation in range(0, 360, 90):
            test_beacon1 = Beacon(beacon_pair1[1].x, beacon_pair1[1].y, beacon_pair1[1].z)
            test_beacon1.rotate_relative_direction(direction)
            test_beacon1.rotate_xy(xy_rotation)
            test_beacon2 = Beacon(beacon_pair2[1].x, beacon_pair2[1].y, beacon_pair2[1].z)
            test_beacon2.rotate_relative_direction(direction)
            test_beacon2.rotate_xy(xy_rotation)
            if are_same_orientation((beacon_pair1[0], test_beacon1), (beacon_pair2[0], test_beacon2)):
                return direction, xy_rotation


def are_same_orientation(beacon_pair1: tuple[Beacon, Beacon], beacon_pair2: tuple[Beacon, Beacon]):
    scanner1_delta_x = beacon_pair1[0].x - beacon_pair2[0].x
    scanner2_delta_x = beacon_pair1[1].x - beacon_pair2[1].x

    scanner1_delta_y = beacon_pair1[0].y - beacon_pair2[0].y
    scanner2_delta_y = beacon_pair1[1].y - beacon_pair2[1].y

    scanner1_delta_z = beacon_pair1[0].z - beacon_pair2[0].z
    scanner2_delta_z = beacon_pair1[1].z - beacon_pair2[1].z

    print(f"scanner1_delta_x:{scanner1_delta_x}, scanner2_delta_x:{scanner2_delta_x}, scanner1_delta_y:{scanner1_delta_y},scanner2_delta_y:{scanner2_delta_y},scanner1_delta_z:{scanner1_delta_z},scanner2_delta_z:{scanner2_delta_z}")
    if scanner1_delta_x == scanner2_delta_x and \
        scanner1_delta_y == scanner2_delta_y and \
        scanner1_delta_z == scanner2_delta_z:
        return True


def find_beacons_with_same_distance_to_other_beacons(beacons1: list[Beacon], beacons2: list[Beacon]) -> list[tuple[Beacon, Beacon]]:
    same_beacons: list[tuple[Beacon, Beacon]] = []
    for beacon1 in beacons1:
        for beacon2 in beacons2:
            if is_same_beacon(beacon1, beacon2):
                same_beacons.append((beacon1, beacon2))
                break
    return same_beacons


def is_same_beacon(beacon1: Beacon, beacon2: Beacon) -> bool:
    found_connection_count = 0
    for beacon1_connection in beacon1.distances_to_other_beacons:
        for beacon2_connection in beacon2.distances_to_other_beacons:
            if math.isclose(beacon1_connection, beacon2_connection):
                found_connection_count += 1
                if found_connection_count >= SAME_BEACON_CONNECTION_THRESHOLD:
                    return True


def load_scanners_from_file(file_name: str) -> list[Scanner]:
    lines = load_text_file(file_name)
    id_regex = re.compile(r"(?<=scanner\s)\d+")
    scanners: list[Scanner] = []
    cur_scanner: Scanner = Scanner(-1)
    for line in lines:
        if len(line) == 0:
            continue
        if line[0:3] == "---":
            calculate_distance_between_beacons(cur_scanner.beacons)

            id = int(id_regex.search(line).group(0))
            cur_scanner = Scanner(id)
            scanners.append(cur_scanner)
            continue

        parts = line.split(",")
        cur_scanner.beacons.append(Beacon(int(parts[0]), int(parts[1]), int(parts[2])))

    calculate_distance_between_beacons(cur_scanner.beacons)
    return scanners


if __name__ == "__main__":
    result = get_part_one_result("src/day19/input_sample01.txt")
    print(result)
