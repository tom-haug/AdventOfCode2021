from __future__ import annotations

import time
from enum import Enum
from functools import *

import numpy as np
from attr import dataclass

from src.shared import load_text_file, Point3D


class OperationType(Enum):
    ON = 0
    OFF = 1


@dataclass
class Cuboid:
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

    def intersects(self, other: Cuboid) -> bool:
        overlap_x = self.right >= other.left and self.left <= other.right
        overlap_y = self.top >= other.bottom and self.bottom <= other.top
        overlap_z = self.back >= other.front and self.front <= other.back
        return overlap_x and overlap_y and overlap_z
        # return (self.location1.x <= other.location1.x <= self.location2.x or
        #         self.location1.x <= other.location2.x <= self.location2.x
        #         ) and (self.location1.y <= other.location1.y <= self.location2.y or
        #                self.location1.y <= other.location2.y <= self.location2.y
        #                ) and (self.location1.z <= other.location1.z <= self.location2.z or
        #                       self.location1.z <= other.location2.z <= self.location2.z
        #                       )

    def split_above_y(self, y: int) -> list[Cuboid]:
        if not self.bottom <= y < self.top:
            return [self]

        child1 = Cuboid(Point3D(self.left, self.bottom, self.front), Point3D(self.right, y, self.back))
        child2 = Cuboid(Point3D(self.left, y + 1, self.front), Point3D(self.right, self.top, self.back))
        return [child1, child2]

    def split_right_x(self, x: int) -> list[Cuboid]:
        if not self.left <= x < self.right:
            return [self]

        child1 = Cuboid(Point3D(self.left, self.bottom, self.front), Point3D(x, self.top, self.back))
        child2 = Cuboid(Point3D(x + 1, self.bottom, self.front), Point3D(self.right, self.top, self.back))
        return [child1, child2]

    def split_behind_z(self, z: int) -> list[Cuboid]:
        if not self.front <= z < self.back:
            return [self]

        child1 = Cuboid(Point3D(self.left, self.bottom, self.front), Point3D(self.right, self.top, z))
        child2 = Cuboid(Point3D(self.left, self.bottom, z + 1), Point3D(self.right, self.top, self.back))
        return [child1, child2]

    def fully_contained_within(self, other: Cuboid) -> bool:
        return self.left >= other.left \
            and self.right <= other.right \
            and self.bottom >= other.bottom \
            and self.top <= other.top \
            and self.front >= other.front \
            and self.back <= other.back


@ dataclass
class Operation:
    type: OperationType
    region: Cuboid

    def perform(self, grid: np.ndarray):
        height, width, depth = grid.shape

        # for region in self.regions:
        for x in range(self.region.location1.x, self.region.location2.x + 1):
            if not (0 <= x < width):
                continue
            for y in range(self.region.location1.y, self.region.location2.y + 1):
                if not (0 <= y < height):
                    continue
                for z in range(self.region.location1.z, self.region.location2.z + 1):
                    if not (0 <= z < depth):
                        continue
                    grid[y, x, z] = True if self.type == OperationType.ON else False

    def explode(self, other: Operation) -> list[Operation]:
        # explode current operation based on intersection with other cube. can produce up to 27 child cubes
        #no intersection, no reason to explode
        if not self.region.intersects(other.region):
            return [self]

        top_margin = self.region.top - other.region.top
        bottom_margin = other.region.bottom - self.region.bottom
        left_margin = other.region.left - self.region.left
        right_margin = self.region.right - other.region.right
        front_margin = other.region.front - self.region.front
        back_margin = self.region.back - other.region.back

        child_regions = [self.region]

        if bottom_margin > 0:
            child_regions = reduce(lambda prev, cur: prev + cur.split_above_y(other.region.bottom - 1), child_regions, [])

        if top_margin > 0:
            child_regions = reduce(lambda prev, cur: prev + cur.split_above_y(other.region.top), child_regions, [])

        if left_margin > 0:
            child_regions = reduce(lambda prev, cur: prev + cur.split_right_x(other.region.left - 1), child_regions, [])

        if right_margin > 0:
            child_regions = reduce(lambda prev, cur: prev + cur.split_right_x(other.region.right), child_regions, [])

        if front_margin > 0:
            child_regions = reduce(lambda prev, cur: prev + cur.split_behind_z(other.region.front - 1), child_regions, [])

        if back_margin > 0:
            child_regions = reduce(lambda prev, cur: prev + cur.split_behind_z(other.region.back), child_regions, [])

        #remove the completely overlapping section - there should always be one
        other_child_regions = [region for region in child_regions if not region.fully_contained_within(other.region)]
        if len(other_child_regions) != len(child_regions) - 1:
            print("HELP")

        return [Operation(self.type, region) for region in other_child_regions]

def load_data_structures_from_file(file_name: str):
    lines = load_text_file(file_name)
    operations: list[Operation] = []
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    z_min: int
    z_max: int
    for line in lines:
        first_parts = line.split(" ")
        type = OperationType.ON if first_parts[0] == "on" else OperationType.OFF
        coordinate_parts = first_parts[1].split(",")
        x_parts = coordinate_parts[0].split("=")[1].split("..")
        y_parts = coordinate_parts[1].split("=")[1].split("..")
        z_parts = coordinate_parts[2].split("=")[1].split("..")
        location1 = Point3D(int(x_parts[0]), int(y_parts[0]), int(z_parts[0]))
        location2 = Point3D(int(x_parts[1]), int(y_parts[1]), int(z_parts[1]))
        operations.append(Operation(type, Cuboid(location1, location2)))
    return operations


def transpose_operations(operations: list[Operation], offset: int):
    for operation in operations:
        operation.region.location1.x += offset
        operation.region.location1.y += offset
        operation.region.location1.z += offset
        operation.region.location2.x += offset
        operation.region.location2.y += offset
        operation.region.location2.z += offset


def reduce_overlapping_operations(operations: list[Operation]):
    idx_higher_priority = len(operations)

    while idx_higher_priority >= 2:
        idx_higher_priority -= 1
        # print(f"reducing from: {idx_higher_priority}, total: {len(operations)}")
        operation_higher_priority = operations[idx_higher_priority]
        idx_lower_priority = idx_higher_priority
        while idx_lower_priority >= 1:
            idx_lower_priority -= 1
            operation_lower_priority = operations[idx_lower_priority]
            if not operation_lower_priority.region.intersects(operation_higher_priority.region):
                continue
            operations.remove(operation_lower_priority)
            new_operations = operation_lower_priority.explode(operation_higher_priority)
            for operation in new_operations:
                operations.insert(idx_lower_priority, operation)
        idx_higher_priority = operations.index(operation_higher_priority)

def count_on_locations(operations: list[Operation]) -> int:
    on_operations = [x for x in operations if x.type == OperationType.ON]
    on_volume = sum([x.region.volume for x in on_operations])
    return on_volume

if __name__ == "__main__":
    start = time.time()
    operations = load_data_structures_from_file("src/day22/input.txt")
    # operations = [x for x in operations if -50 <= x.region.left <= 50]
    reduce_overlapping_operations(operations)
    result = count_on_locations(operations)

    end = time.time()

    print(f"Running Time: {end - start}")
    print(f"Result: {result}")