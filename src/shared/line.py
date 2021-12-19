from .point import Point


class Line:
    def __init__(self, begin: Point, end: Point):
        self.begin = begin
        self.end = end

    def is_horizontal(self):
        return self.begin.y == self.end.y

    def is_vertical(self):
        return self.begin.x == self.end.x

    def is_45_degree_angle(self):
        slope = self.slope()
        return slope is not None and abs(slope) == 1.0

    def slope(self):
        # protect divide by zero
        if self.is_vertical():
            return None
        return float(self.end.y - self.begin.y) / float(self.end.x - self.begin.x)

    def all_points_along_line(self) -> list[Point]:
        if not (self.is_horizontal() or self.is_vertical() or self.is_45_degree_angle()):
            raise Exception("getting the points for the slope of this line is not yet supported")

        all_points: list[Point] = []

        if self.is_vertical():
            x_increment = 0
        elif self.begin.x < self.end.x:
            x_increment = 1
        else:
            x_increment = -1

        if self.is_horizontal():
            y_increment = 0
        elif self.begin.y < self.end.y:
            y_increment = 1
        else:
            y_increment = -1

        cur_location = self.begin
        while True:
            all_points.append(cur_location)
            if cur_location == self.end:
                break
            cur_location = Point(cur_location.x + x_increment, cur_location.y + y_increment)

        return all_points
