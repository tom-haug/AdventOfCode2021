import operator
import numpy as np

from src.day09.basin import Basin
from src.shared import ComparerFunc, Point


class BasinProcessor:
    BASIN_BOUNDARY_VALUE = 9

    def __init__(self, height_map: np.ndarray):
        self.height_map = height_map

    def create_basins(self) -> list[Basin]:
        basins = self._find_basins()
        for basin in basins:
            self._fill_basin(basin)
        return basins

    def _find_basins(self) -> list[Basin]:
        width, height = self.height_map.shape
        basins: list[Basin] = []
        for x in range(width):
            for y in range(height):
                if self._is_local_extreme(x, y, operator.lt):
                    basins.append(Basin(Point(x, y), self.height_map[x, y]))
        return basins

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
        self._spread(basin, basin.origin.location)

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
        if self.height_map[x, y] == self.BASIN_BOUNDARY_VALUE:
            return

        basin.add_location(Point(x, y), self.height_map[x, y])
        self._spread(basin, Point(x - 1, y))
        self._spread(basin, Point(x + 1, y))
        self._spread(basin, Point(x, y - 1))
        self._spread(basin, Point(x, y + 1))
