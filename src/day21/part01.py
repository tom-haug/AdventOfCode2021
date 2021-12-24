from __future__ import annotations
import time

from attr import dataclass

from src.shared import load_text_file

@dataclass
class Player:
    position: int
    score: int


def get_part_one_result(file_name: str) -> int:
    players = load_data_structures_from_file(file_name)
    player_count = len(players)
    cur_die_roll = -1
    max_die_roll = 100

    while True:
        player_idx = ((cur_die_roll + 1) // 3) % player_count
        player = players[player_idx]
        for cur_die_roll in range(cur_die_roll + 1, cur_die_roll + 4):
            player.position = (player.position + (cur_die_roll % max_die_roll) + 1) % 10
        player.score += player.position + 1
        if player.score >= 1000:
            break

    num_rolls = cur_die_roll + 1
    loser = players[((num_rolls + 1) // 3) % player_count]
    result = num_rolls * loser.score
    return result


def load_data_structures_from_file(file_name: str) -> list[Player]:
    lines = load_text_file(file_name)
    players: list[Player] = []
    for line in lines:
        player_position = int(line.split(":")[1].strip()) - 1
        players.append(Player(player_position, 0))
    return players


if __name__ == "__main__":
    start = time.time()
    result = get_part_one_result("src/day21/input.txt")
    end = time.time()

    print(f"Running Time: {end - start}")
    print(result)
