from src.day21.game import Player
from src.shared import load_text_file


def load_data_structures_from_file(file_name: str) -> list[Player]:
    lines = load_text_file(file_name)
    players: list[Player] = []
    for line in lines:
        player_position = int(line.split(":")[1].strip()) - 1
        players.append(Player(player_position, 0))
    return players
