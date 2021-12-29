from src.day23.amphipod_game import AmphipodGame, next_move
from src.day23.floor_map import FloorMap
from src.day23.player import Player, PlayerType
from src.day23.walkable_location import WalkableLocation
from src.shared import load_text_file


def get_game_result(file_name: str):
    game = load_game_from_file(file_name)
    lowest_energy, movement_log = next_move(game)
    return lowest_energy, movement_log


def load_game_from_file(file_name: str) -> AmphipodGame:
    lines = load_text_file(file_name)
    floor_map = FloorMap()
    players: list[Player] = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            location = WalkableLocation(x, y)
            match char:
                case ".":
                    floor_map.append(location)
                case "A" | "B" | "C" | "D":
                    floor_map.append(location)
                    player = Player(len(players), PlayerType(char), location)
                    players.append(player)

    return AmphipodGame(floor_map, players, len(lines) - 3)

