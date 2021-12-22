from __future__ import annotations
from enum import Enum

from src.shared import Point3D


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
