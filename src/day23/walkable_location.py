from functools import cached_property
from src.day23.constants import *
from src.shared import Point


class WalkableLocation(Point):
    @cached_property
    def is_hallway(self) -> bool:
        return self.y == HALLWAY_Y

    @cached_property
    def is_room(self) -> bool:
        return not self.is_hallway
