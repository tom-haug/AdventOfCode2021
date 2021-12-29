from functools import cached_property
from attr import dataclass
from src.day23.player import Player
from src.day23.walkable_location import WalkableLocation


@dataclass(repr=False)
class PlayerMove:
    player: Player
    new_location: WalkableLocation
    distance_moved: int

    @cached_property
    def total_energy_cost(self) -> int:
        return self.distance_moved * self.player.move_cost

    def __repr__(self) -> str:
        return f"{self.player.id}({self.player.type.value}): move to {self.new_location}, dist: {self.distance_moved}"