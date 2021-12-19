import numpy as np
import pandas as pd

from src.shared import Line, Point, load_text_file


class VentMap:
    DANGEROUS_VENT_THRESHOLD = 2

    def __init__(self, file_name: str, load_diagonal: bool):
        self._load_vents_from_file(file_name, load_diagonal)

    def _load_vents_from_file(self, file_name: str, load_diagonal: bool):
        self.vents: list[Line] = []
        self.map_bound_bottom_right = Point(0, 0)
        lines = load_text_file(file_name)
        for input_line in lines:
            line_parts = input_line.split(" -> ")
            coord1_parts = line_parts[0].split(",")
            coord2_parts = line_parts[1].split(",")
            point1 = Point(int(coord1_parts[0]), int(coord1_parts[1]))
            point2 = Point(int(coord2_parts[0]), int(coord2_parts[1]))
            line = Line(point1, point2)
            if line.is_45_degree_angle() and not load_diagonal:
                continue
            self.map_bound_bottom_right.extend(point1.x, point1.y)
            self.map_bound_bottom_right.extend(point2.x, point2.y)
            self.vents.append(line)

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
                if df_vent_count[col][row] >= self.DANGEROUS_VENT_THRESHOLD:
                    dangerous_vent_count += 1
        return dangerous_vent_count
