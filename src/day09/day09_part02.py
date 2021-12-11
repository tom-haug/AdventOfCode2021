import math
import operator
import numpy as np

from src.shared.point import Point
from src.shared.types import ComparerFunc
from src.shared.utils import load_text_file


class Basin:
    def __init__(self, basin_center: Point):
        self.basin_center = basin_center
        self.included_locations: list[Point] = []

    def has_location(self, location: Point):
        for included_location in self.included_locations:
            if included_location == location:
                return True
        return False

    def size(self):
        return len(self.included_locations)


class BasinProcessor:
    def __init__(self, height_map: np.ndarray):
        self.height_map = height_map

    def create_basins(self) -> list[Basin]:
        basins = self._find_basins()
        for basin in basins:
            self._fill_basin(basin)
        return basins

    def _find_basins(self) -> list[Basin]:
        width, height = self.height_map.shape
        Basins: list[Basin] = []
        for x in range(width):
            for y in range(height):
                if self._is_local_extreme(x, y, operator.lt):
                    Basins.append(Basin(Point(x, y)))
        return Basins

    def _is_local_extreme(self, x: int, y: int, comparer_func: ComparerFunc) -> bool:
        width, height = self.height_map.shape
        cur_value = self.height_map[x, y]
        if x > 0 and not comparer_func(cur_value, self.height_map[x - 1, y]):
            return False
        elif x < width - 1 and not comparer_func(cur_value, self.height_map[x + 1, y]):
            return False
        elif y > 0 and not comparer_func(cur_value, self.height_map[x, y - 1]):
            return False
        elif y < height - 1 and not comparer_func(cur_value, self.height_map[x, y + 1]):
            return False
        return True

    def _fill_basin(self, basin: Basin):
        self._spread(basin, basin.basin_center)

    def _spread(self, basin: Basin, location: Point):
        x, y = location.x, location.y
        width, height = self.height_map.shape

        # out of map bounds
        if x < 0 or x >= width or y < 0 or y >= height:
            return

        # already checked
        if basin.has_location(location):
            return

        # basin boundary
        if self.height_map[x, y] == 9:
            return

        basin.included_locations.append(Point(x, y))
        self._spread(basin, Point(x - 1, y))
        self._spread(basin, Point(x + 1, y))
        self._spread(basin, Point(x, y - 1))
        self._spread(basin, Point(x, y + 1))


def get_part_two_result(file_name: str) -> int:
    file_contents = load_text_file(file_name)
    height_map = np.array([[int(x) for x in list(line)] for line in file_contents])
    basin_factor = BasinProcessor(height_map)
    basins = basin_factor.create_basins()

    sorted_basin_sizes = sorted([basin.size() for basin in basins], reverse=True)
    top_three_basin_sizes = sorted_basin_sizes[:3]
    result = math.prod(top_three_basin_sizes)
    return result


if __name__ == "__main__":
    result = get_part_two_result("input.txt")
    print(result)
