from __future__ import annotations
import copy
from functools import cache
from attr import dataclass
from src.day23.floor_map import FloorMap
from src.day23.player import Player
from src.day23.player_move import PlayerMove
from src.day23.walkable_location import WalkableLocation


@dataclass(eq=False, hash=False, repr=False)
class AmphipodGame:
    floor_map: FloorMap
    players: list[Player]
    room_depth: int
    move_count: int = 0

    def __eq__(self, other: AmphipodGame):
        my_players = tuple(sorted((x.type.value, x.location.x, x.location.y) for x in self.players))
        other_players = tuple(sorted((x.type.value, x.location.x, x.location.y) for x in other.players))
        return my_players == other_players

    def __hash__(self):
        players = tuple(sorted((x.type.value, x.location.x, x.location.y) for x in self.players))
        return hash(players)

    def __repr__(self):
        output: list[list[str]] = []
        for row in range(5):
            output.append(["x" for _ in range(13)])
        for floor in self.floor_map.items():
            location = floor[0]
            output[location.y][location.x] = "."
        for player in self.players:
            location = player.location
            output[location.y][location.x] = str(player.type.value)
        result = "\n".join(["".join(line) for line in output])
        return result

    @property
    def game_complete(self) -> bool:
        for player in self.players:
            if not self.is_winning_location_for_player(player, player.location):
                return False
        return True

    def move(self, move: PlayerMove):
        # get the corresponding player in THIS copy of the game
        real_player = [x for x in self.players if x == move.player][0]
        real_player.move(move.new_location)

    def all_possible_moves(self) -> list[PlayerMove]:
        possible_moves: list[PlayerMove] = []
        for player in self.players:
            if self.is_winning_location_for_player(player, player.location):
                continue

            player_moves = self.possible_player_moves(player.location, [], player, -1)
            possible_moves += player_moves

        winning_moves = [x for x in possible_moves if self.is_winning_location_for_player(x.player, x.new_location)]
        if len(winning_moves) > 0:
            return winning_moves
        else:
            return possible_moves

    def possible_player_moves(self, cur_location: WalkableLocation, already_visited: list[WalkableLocation], player: Player, distance_moved: int) -> list[PlayerMove]:
        if not self.can_move_through_location(cur_location, already_visited, player):
            return []

        already_visited.append(cur_location)
        distance_moved += 1
        possible_moves: list[PlayerMove] = []

        if self.can_stop_at_location(cur_location, player, distance_moved):
            possible_moves.append(PlayerMove(player, cur_location, distance_moved))

        # get next move options and recurse
        cur_node = self.floor_map[cur_location]
        for next_node in cur_node.linked_nodes:
            next_node_location = self.floor_map.get_location(next_node)
            possible_moves += self.possible_player_moves(next_node_location, already_visited, player, distance_moved)

        return possible_moves

    def can_move_through_location(self, cur_location: WalkableLocation, already_visited: list[WalkableLocation], player: Player) -> bool:
        # don't double back in the same turn
        if cur_location in already_visited:
            return False

        # check if occupied
        if len([x for x in self.players if x.location == cur_location and x is not player]) > 0:
            return False

        # if we are about to go into a room
        if len(already_visited) > 0 and already_visited[-1].is_hallway and cur_location.is_room:
            # if this is the wrong room
            if not player.is_home_room(cur_location):
                return False

            # if the wrong player type if further back in the room
            for check_y in range(cur_location.y + 1, 6):
                check_location = WalkableLocation(cur_location.x, check_y)
                check_player = [x for x in self.players if x.location == check_location]
                if len(check_player) == 1 and not check_player[0].is_home_room(cur_location):
                    return False
        return True

    def can_stop_at_location(self, cur_location: WalkableLocation, player: Player, distance_moved: int) -> bool:
        # not the location directly outside a room
        if len(self.floor_map[cur_location].linked_nodes) == 3:
            return False

        # not the starting position
        if distance_moved == 0:
            return False

        # will not move from hallway to hallway
        if player.location.is_hallway and cur_location.is_hallway:
            return False

        # don't let player end within the same room
        if player.location.is_room and cur_location.is_room and player.location.x == cur_location.x:
            return False
        return True

    def is_winning_location_for_player(self, player: Player, location: WalkableLocation) -> bool:
        if player.is_home_room(location):
            # check if any players further back in room that this is not their home room
            for check_y in range(location.y + 1, self.room_depth + 2):
                check_location = WalkableLocation(location.x, check_y)
                check_player = [x for x in self.players if x.location == check_location]
                if not (len(check_player) == 1 and check_player[0].is_home):
                    return False
            return True
        return False


@cache
def next_move(game: AmphipodGame) -> (int, list[PlayerMove]):
    if game.game_complete:
        return 0, []

    game.move_count += 1
    possible_moves = game.all_possible_moves()
    future_move_results: list[(int, list[PlayerMove])] = []

    for move in possible_moves:
        child_game = copy.deepcopy(game)
        child_game.move(move)
        future_energy_spent, future_moves = next_move(child_game)

        if future_energy_spent is not None:
            combined_energy_spent = move.total_energy_cost + future_energy_spent
            combined_moves = [move] + future_moves
            future_move_results.append((combined_energy_spent, combined_moves))

    if len(future_move_results) == 0:
        return None, None

    min_energy_path = min(future_move_results, key=lambda x: x[0])
    return min_energy_path
