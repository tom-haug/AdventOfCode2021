from attr import dataclass


@dataclass
class Point:
    x: int
    y: int

    def extend(self, new_x: int, new_y: int):
        if new_x > self.x:
            self.x = new_x
        if new_y > self.y:
            self.y = new_y


@dataclass
class Point3D(Point):
    z: int
