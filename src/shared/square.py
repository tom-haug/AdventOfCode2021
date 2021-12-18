from attr import dataclass

from src.shared.point import Point


@dataclass
class Square:
    top_left: Point
    bottom_right: Point

    def contains(self, point: Point) -> bool:
        return self.top_left.x <= point.x <= self.bottom_right.x \
               and self.bottom_right.y <= point.y <= self.top_left.y
