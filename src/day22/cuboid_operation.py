from __future__ import annotations
from enum import Enum
from attr import dataclass
from src.day22.splittable_cuboid import SplittableCuboid


class OperationType(Enum):
    ON = 0
    OFF = 1


@ dataclass
class CuboidOperation:
    type: OperationType
    region: SplittableCuboid

    def explode(self, other: CuboidOperation) -> list[CuboidOperation]:
        child_cuboids = self.region.explode(other.region)
        return [CuboidOperation(self.type, region) for region in child_cuboids]
