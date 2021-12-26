from __future__ import annotations
from functools import *
from attr import dataclass

from src.shared import Point3D


@dataclass
class RectCuboid:
    location1: Point3D
    location2: Point3D

    @cached_property
    def top(self) -> int:
        return max(self.location1.y, self.location2.y)

    @cached_property
    def bottom(self) -> int:
        return min(self.location1.y, self.location2.y)

    @cached_property
    def left(self) -> int:
        return min(self.location1.x, self.location2.x)

    @cached_property
    def right(self) -> int:
        return max(self.location1.x, self.location2.x)

    @cached_property
    def front(self) -> int:
        return min(self.location1.z, self.location2.z)

    @cached_property
    def back(self) -> int:
        return max(self.location1.z, self.location2.z)

    @cached_property
    def width(self) -> int:
        return self.right - self.left + 1

    @cached_property
    def height(self) -> int:
        return self.top - self.bottom + 1

    @cached_property
    def depth(self) -> int:
        return self.back - self.front + 1

    @cached_property
    def volume(self) -> int:
        return self.width * self.height * self.depth

    def intersects(self, other: RectCuboid) -> bool:
        overlap_x = self.right >= other.left and self.left <= other.right
        overlap_y = self.top >= other.bottom and self.bottom <= other.top
        overlap_z = self.back >= other.front and self.front <= other.back
        return overlap_x and overlap_y and overlap_z

    def fully_contained_within(self, other: RectCuboid) -> bool:
        return self.left >= other.left \
            and self.right <= other.right \
            and self.bottom >= other.bottom \
            and self.top <= other.top \
            and self.front >= other.front \
            and self.back <= other.back
