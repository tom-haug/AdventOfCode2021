from __future__ import annotations
import time
from enum import Enum

import numpy as np
from attr import dataclass

from src.shared import load_text_file, Point3D


class OperationType(Enum):
    ON = 0
    OFF = 1


@dataclass
class Operation:
    type: OperationType
    location1: Point3D
    location2: Point3D

    def perform(self, grid: np.ndarray):
        height, width, depth = grid.shape

        for x in range(self.location1.x, self.location2.x + 1):
            if not (0 <= x < width):
                continue
            for y in range(self.location1.y, self.location2.y + 1):
                if not (0 <= y < height):
                    continue
                for z in range(self.location1.z, self.location2.z + 1):
                    if not (0 <= z < depth):
                        continue
                    grid[y, x, z] = True if self.type == OperationType.ON else False


def load_data_structures_from_file(file_name: str):
    lines = load_text_file(file_name)
    operations: list[Operation] = []
    for line in lines:
        first_parts = line.split(" ")
        type = OperationType.ON if first_parts[0] == "on" else OperationType.OFF
        coordinate_parts = first_parts[1].split(",")
        x_parts = coordinate_parts[0].split("=")[1].split("..")
        y_parts = coordinate_parts[1].split("=")[1].split("..")
        z_parts = coordinate_parts[2].split("=")[1].split("..")
        location1 = Point3D(int(x_parts[0]), int(y_parts[0]), int(z_parts[0]))
        location2 = Point3D(int(x_parts[1]), int(y_parts[1]), int(z_parts[1]))
        operations.append(Operation(type, location1, location2))
    return operations


def transpose_operations(operations: list[Operation], offset: int):
    for operation in operations:
        operation.location1.x += offset
        operation.location1.y += offset
        operation.location1.z += offset
        operation.location2.x += offset
        operation.location2.y += offset
        operation.location2.z += offset


def create_grid(size: int) -> np.ndarray:
        return np.full((size, size, size), False)


def perform_operations(operations: list[Operation], grid: np.ndarray):
    for operation in operations:
        operation.perform(grid)


if __name__ == "__main__":
    start = time.time()
    operations = load_data_structures_from_file("src/day22/input.txt")
    transpose_operations(operations, 50)
    grid = create_grid(101)
    perform_operations(operations, grid)
    result = np.count_nonzero(grid)

    end = time.time()

    print(f"Running Time: {end - start}")
    print(f"Result: {result}")