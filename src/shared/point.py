from __future__ import annotations
from attr import dataclass


@dataclass(frozen=True, repr=False)
class Point:
    x: int
    y: int

    # def extend(self, new_x: int, new_y: int):
    #     if new_x > self.x:
    #         self.x = new_x
    #     if new_y > self.y:
    #         self.y = new_y
    def __repr__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"

    def adjacent_to(self, other: Point):
        delta_x = abs(self.x - other.x)
        delta_y = abs(self.y - other.y)
        return delta_x + delta_y == 1

@dataclass
class Point3D(Point):
    z: int
