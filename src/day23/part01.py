from __future__ import annotations

import copy
import time
from enum import Enum
from functools import cache, cached_property

from attr import dataclass

from src.shared import load_text_file, LinkedNode, Point


class PlayerType(Enum):
    AMBER = "A"
    BRONZE = "B"
    COPPER = "C"
    DESERT = "D"


# @dataclass(eq=False)
class Player:
    id: int
    type: PlayerType
    location: Point
    energy_cost: int

    def __init__(self, id: int, type: PlayerType, location: Point, energy_cost: int):
        self.id = id
        self.type = type
        self.location = location
        self.energy_cost = energy_cost

    def __eq__(self, other: Player):
        return self.id == other.id

    def __hash__(self):
        return hash((self.id, self.location))

    def move(self, location):
        # move_distance = abs(self.location.x - location.x) + abs(self.location.y - location.y)
        self.location = location
        # return move_distance

    @property
    def goal_room_x(self):
        match self.type:
            case PlayerType.AMBER:
                return 3
            case PlayerType.BRONZE:
                return 5
            case PlayerType.COPPER:
                return 7
            case PlayerType.DESERT:
                return 9

@dataclass
class PlayerMove:
    player: Player
    new_location: Point
    distance_moved: int

    @cached_property
    def total_energy_cost(self):
        return self.distance_moved * self.player.energy_cost

# class FloorSegment(LinkedNode, MapObject):
#

class FloorMap(dict[Point, LinkedNode]):
    def append(self, location: Point):
        new_node = LinkedNode(str(location))
        self[location] = new_node

        # link up adjacent floor segments
        for other_location, other_node in self.items():
            if other_location.adjacent_to(location):
                other_node.linked_nodes.append(new_node)
                new_node.linked_nodes.append(other_node)

    def get_location(self, node: LinkedNode) -> Point:
        for key, value in self.items():
            if value == node:
                return key

@cache
# def next_move(game: Game, last_player: Player) -> int | None:
def next_move(game: Game) -> (int, list[PlayerMove]):
    # print("______________________")
    # print(f"round:{game.move_count}")
    # print("______________________")
    # print(game)

    if game.game_complete:
        return 0, []

    # don't keep going forever
    if game.move_count > 20:
        return None, None

    game.move_count += 1
    possible_moves = game.all_possible_moves()
    # if last_player is not None:
    #     possible_moves = [x for x in possible_moves if x.player != last_player]

    total_energy_spent: list[(int, list[PlayerMove])] = []
    for move in possible_moves:
        child_game = copy.deepcopy(game)
        child_game.move(move)
        future_energy_spent, future_moves = next_move(child_game)

        if future_energy_spent is not None:
            combined_energy_spent = move.total_energy_cost + future_energy_spent
            combined_moves = [move] + future_moves
            total_energy_spent.append((combined_energy_spent, combined_moves))

    if len(total_energy_spent) == 0:
        return None, None

    min_energy = min(total_energy_spent, key=lambda x: x[0])
    return min_energy


def is_location_hallway(location: Point):
    return location.y == 1

def is_location_room(location: Point):
    return not is_location_hallway(location)


def is_winning_location(player: Player, location: Point, other_players: list[Player]) -> bool:
    if location.x == player.goal_room_x:
        # in back of room
        if location.y == 3:
            return True

        # in front of room, but back is filled by correct type
        if location.y == 2:
            back_of_room_location = Point(location.x, 3)
            player_in_back_of_room = [x for x in other_players if x.location == back_of_room_location]
            if len(player_in_back_of_room) == 1 and player_in_back_of_room[0].location.x == player_in_back_of_room[0].goal_room_x:
                return True
    return False

# @dataclass(hash=False, repr=False)
class Game:
    floor_map: FloorMap
    players: list[Player]
    move_count: int = 0

    def __init__(self, floor_map: FloorMap, players: list[Player]):
        self.floor_map = floor_map
        self.players = players
        self.move_count = 0

    def __eq__(self, other: Game):
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
            if not is_winning_location(player, player.location, self.players):
                return False
        return True

    def move(self, move: PlayerMove):
        # get the corresponding player in THIS copy of the game
        real_player = [x for x in self.players if x == move.player][0]
        real_player.move(move.new_location)

    def all_possible_moves(self) -> list[PlayerMove]:
        possible_moves: list[PlayerMove] = []
        for player in self.players:
            if is_winning_location(player, player.location, self.players):
                continue

            player_moves = self.possible_player_moves(player.location, [], player, -1)
            possible_moves += player_moves

        winning_moves = [x for x in possible_moves if is_winning_location(x.player, x.new_location, self.players)]
        if len(winning_moves) > 0:
            return winning_moves
        else:
            return possible_moves


    def possible_player_moves(self, cur_location: Point, already_visited: list[Point], player: Player, distance_moved: int) -> list[PlayerMove]:

        # don't double back in the same turn
        if cur_location in already_visited:
            return []

        # check if occupied
        if len([x for x in self.players if x.location == cur_location and x is not player]) > 0:
            return []

        # player has reached the goal
        # if is_winning_location(player, ):
        #     return []

        # if we are about to go into a room
        if len(already_visited) > 0 and is_location_hallway(already_visited[-1]) and is_location_room(cur_location):
        # if is_location_room(cur_location) and len(already_visited) > 0:
            # if this is the wrong room
            if player.goal_room_x != cur_location.x:
                return []

            # if this is the right room, but the wrong player is in the back of the room
            back_of_room_location = Point(cur_location.x, cur_location.y + 1)
            player_in_back_of_room = [x for x in self.players if x.location == back_of_room_location]
            if len(player_in_back_of_room) == 1:
                if player_in_back_of_room[0].goal_room_x != cur_location.x:
                    return []

        already_visited.append(cur_location)
        distance_moved += 1

        possible_moves: list[PlayerMove] = []

        # not the location directly outside a room
        if len(self.floor_map[cur_location].linked_nodes) == 3:
            ...
        # not the starting position
        elif distance_moved == 0:
            ...
        # will not move from hallway to hallway
        elif is_location_hallway(player.location) and is_location_hallway(cur_location):
            ...
        # don't let player move within the same room
        elif is_location_room(player.location) and is_location_room(cur_location) and player.location.x == cur_location.x:
            ...
        else:
            possible_moves.append(PlayerMove(player, cur_location, distance_moved))

        cur_node = self.floor_map[cur_location]
        for next_node in cur_node.linked_nodes:
            next_node_location = self.floor_map.get_location(next_node)
            possible_moves += self.possible_player_moves(next_node_location, already_visited, player, distance_moved)

        return possible_moves


def load_data_structures_from_file(file_name: str) -> Game:
    lines = load_text_file(file_name)
    height, width = len(lines), len(lines[0])
    floor_map = FloorMap()
    players: list[Player] = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            location = Point(x, y)
            match char:
                case ".":
                    floor_map.append(location)
                case "A":
                    floor_map.append(location)
                    player = Player(len(players), PlayerType(char), location, 1)
                    players.append(player)
                case "B":
                    floor_map.append(location)
                    player = Player(len(players), PlayerType(char), location, 10)
                    players.append(player)
                case "C":
                    floor_map.append(location)
                    player = Player(len(players), PlayerType(char), location, 100)
                    players.append(player)
                case "D":
                    floor_map.append(location)
                    player = Player(len(players), PlayerType(char), location, 1000)
                    players.append(player)

    return Game(floor_map, players)


def get_part_one_result(file_name: str):
    game = load_data_structures_from_file(file_name)
    lowest_energy, lowest_energy_path = next_move(game)
    return lowest_energy



if __name__ == "__main__":
    start = time.time()
    result = get_part_one_result("src/day23/input.txt")
    end = time.time()

    print(f"Running Time: {end - start}")
    print(f"Result: {result}")


# 12521 too low