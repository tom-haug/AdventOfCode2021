from __future__ import annotations
import time
from itertools import cycle
from typing import Generator
from src.day21.common import load_data_structures_from_file
from src.day21.game import Game

DIE_SIZE = 100
DIE_ROLLS = 3
NUM_GAME_POSITIONS = 10
WINNING_SCORE = 1000


def get_part_one_result(file_name: str) -> int:
    players = load_data_structures_from_file(file_name)
    die_roller = DieRoller()

    game = Game(NUM_GAME_POSITIONS, die_roller.roll_sum(), WINNING_SCORE)
    game.play(players[0], players[1])

    final_state = game.winning_state
    total_die_rolls = die_roller.roll_count
    losing_score = min(final_state.cur_player.score, final_state.other_player.score)

    return losing_score * total_die_rolls


class DieRoller:
    def __init__(self):
        self.roll_count = 0
        self.roll_die = cycle(range(1, DIE_SIZE + 1))

    def roll_sum(self) -> Generator[list[int], None, None]:
        while True:
            self.roll_count += 3
            yield [sum(next(self.roll_die) for _ in range(DIE_ROLLS))]


if __name__ == "__main__":
    start = time.time()
    result = get_part_one_result("src/day21/input.txt")
    end = time.time()

    print(f"Running Time: {end - start}")
    print(result)
