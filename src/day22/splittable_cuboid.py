from __future__ import annotations
from functools import reduce
from src.shared import RectCuboid, Point3D


class SplittableCuboid(RectCuboid):
    def split_y(self, y: int) -> list[SplittableCuboid]:
        if not self.bottom <= y < self.top:
            return [self]

        child1 = SplittableCuboid(Point3D(self.left, self.bottom, self.front), Point3D(self.right, y, self.back))
        child2 = SplittableCuboid(Point3D(self.left, y + 1, self.front), Point3D(self.right, self.top, self.back))
        return [child1, child2]

    def split_x(self, x: int) -> list[SplittableCuboid]:
        if not self.left <= x < self.right:
            return [self]

        child1 = SplittableCuboid(Point3D(self.left, self.bottom, self.front), Point3D(x, self.top, self.back))
        child2 = SplittableCuboid(Point3D(x + 1, self.bottom, self.front), Point3D(self.right, self.top, self.back))
        return [child1, child2]

    def split_z(self, z: int) -> list[SplittableCuboid]:
        if not self.front <= z < self.back:
            return [self]

        child1 = SplittableCuboid(Point3D(self.left, self.bottom, self.front), Point3D(self.right, self.top, z))
        child2 = SplittableCuboid(Point3D(self.left, self.bottom, z + 1), Point3D(self.right, self.top, self.back))
        return [child1, child2]

    def explode(self, other: SplittableCuboid) -> list[SplittableCuboid]:
        '''
        Splits current cuboid up based on intersection points of other cuboid and removes the overlapping region.
        Can produce up to 26 child cuboid.
        :return: list of child cuboids
        '''

        child_cuboids = [self]

        # split bottom
        child_cuboids = reduce(lambda prev, cur: prev + cur.split_y(other.bottom - 1), child_cuboids, [])

        # split top
        child_cuboids = reduce(lambda prev, cur: prev + cur.split_y(other.top), child_cuboids, [])

        # split left
        child_cuboids = reduce(lambda prev, cur: prev + cur.split_x(other.left - 1), child_cuboids, [])

        # split right
        child_cuboids = reduce(lambda prev, cur: prev + cur.split_x(other.right), child_cuboids, [])

        # split front
        child_cuboids = reduce(lambda prev, cur: prev + cur.split_z(other.front - 1), child_cuboids, [])

        # split back
        child_cuboids = reduce(lambda prev, cur: prev + cur.split_z(other.back), child_cuboids, [])

        # remove the completely overlapping section - there should always be just one
        child_cuboids = [cuboid for cuboid in child_cuboids if not cuboid.fully_contained_within(other)]

        return child_cuboids
