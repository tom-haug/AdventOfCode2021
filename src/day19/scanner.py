import math

from src.day19.beacon import Beacon, RelativeDirection


class Scanner:
    def __init__(self, id: int):
        self.id: int = id
        self._beacons: list[Beacon] = []

    @property
    def beacons(self):
        return self._beacons

    def rotated_beacons_view(self, direction: RelativeDirection, xy_rotation: int) -> list[Beacon]:
        new_beacons: list[Beacon] = []
        for beacon in self._beacons:
            new_beacon = Beacon(beacon.x, beacon.y, beacon.z)
            new_beacon.rotate_relative_direction(direction)
            new_beacon.rotate_xy(xy_rotation)
            new_beacons.append(new_beacon)
        return new_beacons

    def beacon_exists(self, beacon: Beacon):
        return len([x for x in self._beacons if x == beacon]) > 0

    def append_beacon(self, beacon: Beacon):
        if not self.beacon_exists(beacon):
            self._beacons.append(beacon)
            self._calculate_distances_to_beacon(beacon)

    def _calculate_distances_to_beacon(self, new_beacon: Beacon):
        new_beacon.distances_to_other_beacons = []

        for existing_beacon in self.beacons:
            distance = math.sqrt(
                math.pow(existing_beacon.x - new_beacon.x, 2) +
                math.pow(existing_beacon.y - new_beacon.y, 2) +
                math.pow(existing_beacon.z - new_beacon.z, 2)
            )
            new_beacon.distances_to_other_beacons.append(distance)
            existing_beacon.distances_to_other_beacons.append(distance)