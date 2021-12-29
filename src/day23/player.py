from __future__ import annotations
from enum import Enum
from attr import dataclass
from src.day23.walkable_location import WalkableLocation
from src.day23.constants import *


class PlayerType(Enum):
    AMBER = "A"
    BRONZE = "B"
    COPPER = "C"
    DESERT = "D"


@dataclass(eq=False, hash=False)
class Player:
    id: int
    type: PlayerType
    location: WalkableLocation

    def __eq__(self, other: Player):
        return self.id == other.id

    def __hash__(self):
        return hash((self.id, self.location))

    def move(self, location):
        self.location = location

    @property
    def home_room_x(self) -> int:
        match self.type:
            case PlayerType.AMBER:
                return AMBER_HOME_ROOM
            case PlayerType.BRONZE:
                return BRONZE_HOME_ROOM
            case PlayerType.COPPER:
                return COPPER_HOME_ROOM
            case PlayerType.DESERT:
                return DESERT_HOME_ROOM

    def is_home_room(self, location: WalkableLocation):
        return location.x == self.home_room_x

    @property
    def is_home(self):
        return self.is_home_room(self.location)


    @property
    def move_cost(self) -> int:
        match self.type:
            case PlayerType.AMBER:
                return AMBER_MOVE_COST
            case PlayerType.BRONZE:
                return BRONZE_MOVE_COST
            case PlayerType.COPPER:
                return COPPER_MOVE_COST
            case PlayerType.DESERT:
                return DESERT_MOVE_COST