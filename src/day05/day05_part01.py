import pandas as pd
import numpy as np
from src.shared.utils import load_text_file


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def extend(self, new_x: int, new_y: int):
        if new_x > self.x:
            self.x = new_x
        if new_y > self.y:
            self.y = new_y

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


class Line:
    def __init__(self, begin: Point, end: Point):
        self.begin = begin
        self.end = end

    def all_points_along_line(self):
        all_points: list[Point] = []
        if self.begin.x == self.end.x:
            x = self.begin.x
            min_y = min(self.begin.y, self.end.y)
            max_y = max(self.begin.y, self.end.y)
            for y in range(min_y, max_y + 1):
                all_points.append(Point(x, y))
        elif self.begin.y == self.end.y:
            y = self.begin.y
            min_x = min(self.begin.x, self.end.x)
            max_x = max(self.begin.x, self.end.x)
            for x in range(min_x, max_x + 1):
                all_points.append(Point(x, y))
        return all_points


class VentMap:
    def __init__(self, file_name: str):
        self.vents: list[Line] = []
        self.map_bound_bottom_right = Point(0, 0)
        lines = load_text_file(file_name)
        for input_line in lines:
            line_parts = input_line.split(" -> ")
            coord1_parts = line_parts[0].split(",")
            coord2_parts = line_parts[1].split(",")
            point1 = Point(int(coord1_parts[0]), int(coord1_parts[1]))
            point2 = Point(int(coord2_parts[0]), int(coord2_parts[1]))
            self.map_bound_bottom_right.extend(point1.x, point1.y)
            self.map_bound_bottom_right.extend(point2.x, point2.y)
            self.vents.append(Line(point1, point2))

    def get_vent_count_matrix(self) -> pd.DataFrame:
        vent_count_map = pd.DataFrame(np.zeros((self.map_bound_bottom_right.y + 1, self.map_bound_bottom_right.x + 1), dtype=int))
        for vent in self.vents:
            points = vent.all_points_along_line()
            for point in points:
                vent_count_map[point.x][point.y] += 1
        return vent_count_map

    def get_dangerous_vent_count(self):
        df_vent_count = self.get_vent_count_matrix()
        (rows, cols) = df_vent_count.shape
        dangerous_vent_count = 0
        for row in range(rows):
            for col in range(cols):
                if df_vent_count[col][row] > 1:
                    dangerous_vent_count += 1
        return dangerous_vent_count


def get_part_one_result(file_name: str):
    vent_map = VentMap(file_name)
    return vent_map.get_dangerous_vent_count()


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)

# 1176 too low
# 6225 correct