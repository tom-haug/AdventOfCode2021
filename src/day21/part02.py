from __future__ import annotations
from itertools import repeat, product
import time
from src.day21.common import load_data_structures_from_file
from src.day21.game import Game


DIE_SIZE = 3
DIE_ROLLS = 3
NUM_GAME_POSITIONS = 10
WINNING_SCORE = 21


def get_part_two_result(file_name: str) -> int:
    players = load_data_structures_from_file(file_name)
    die_roller = repeat(roll_combinations(DIE_SIZE, DIE_ROLLS))
    game = Game(NUM_GAME_POSITIONS, die_roller, WINNING_SCORE)
    wins = game.play(players[0], players[1])
    return max(wins.cur_player, wins.other_player)


def roll_combinations(die_size: int, num_rolls: int) -> list[int]:
    die_values = range(1, die_size + 1)
    all_die_rolls = [sum(x) for x in product(die_values, repeat=num_rolls)]
    return all_die_rolls


if __name__ == "__main__":
    start = time.time()
    result = get_part_two_result("src/day21/input.txt")
    end = time.time()

    print(f"Running Time: {end - start}")
    print(result)
