from __future__ import annotations

import math
import re

from src.day19.beacon import Beacon, RelativeDirection
from src.day19.scanner import Scanner
from src.shared import load_text_file, Point3D

# silly arbitrary number that seems to work
SAME_BEACON_CONNECTION_THRESHOLD = 10

SAME_SCANNER_BEACON_THRESHOLD = 12


def combine_scanners(scanners: list[Scanner]) -> (Scanner, list[Point3D]):
    keep_going = True
    scanner_locations: list[Point3D] = [Point3D(0, 0, 0)]
    while keep_going:
        removed_scanner_location = assimilate_next_scanner(scanners)
        if removed_scanner_location:
            scanner_locations.append(removed_scanner_location)
        else:
            break
    return scanners[0], scanner_locations


def assimilate_next_scanner(scanners) -> Point3D:
    for idx, cur_scanner in enumerate(scanners):
        for other_scanner in scanners[idx + 1:]:
            same_beacons = deduce_same_beacon_pairs(cur_scanner.beacons, other_scanner.beacons)
            if len(same_beacons) >= SAME_SCANNER_BEACON_THRESHOLD:
                direction, xy_rotation = find_beacon_transformation(same_beacons[0], same_beacons[1])
                rotate_beacons(other_scanner.beacons, direction, xy_rotation)

                x_offset = same_beacons[0][0].x - same_beacons[0][1].x
                y_offset = same_beacons[0][0].y - same_beacons[0][1].y
                z_offset = same_beacons[0][0].z - same_beacons[0][1].z

                offset_beacons(other_scanner.beacons, x_offset, y_offset, z_offset)

                for beacon in other_scanner.beacons:
                    cur_scanner.append_beacon(beacon)
                scanners.remove(other_scanner)

                return Point3D(x_offset, y_offset, z_offset)


def rotate_beacons(beacons: list[Beacon], direction: RelativeDirection, xy_rotation: int):
    for beacon in beacons:
        beacon.rotate_relative_direction(direction)
        beacon.rotate_xy(xy_rotation)


def offset_beacons(beacons: list[Beacon], x: int, y: int, z: int):
    for beacon in beacons:
        beacon.x += x
        beacon.y += y
        beacon.z += z


def find_beacon_transformation(beacon_pair1: tuple[Beacon, Beacon], beacon_pair2: tuple[Beacon, Beacon]) -> (
RelativeDirection, int):
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

    if (scanner1_delta_x, scanner1_delta_y, scanner1_delta_z) == (scanner2_delta_x, scanner2_delta_y, scanner2_delta_z):
        return True


def deduce_same_beacon_pairs(beacons1: list[Beacon], beacons2: list[Beacon]) -> list[tuple[Beacon, Beacon]]:
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
            id = int(id_regex.search(line).group(0))
            cur_scanner = Scanner(id)
            scanners.append(cur_scanner)
            continue

        parts = line.split(",")
        cur_scanner.append_beacon(Beacon(int(parts[0]), int(parts[1]), int(parts[2])))
    return scanners
