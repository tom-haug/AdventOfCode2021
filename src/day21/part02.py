from __future__ import annotations

import copy
from functools import *
import itertools
import time
from collections import Counter
from functools import lru_cache

from attr import dataclass

from src.shared import load_text_file


@dataclass(frozen=True)
class Player:
    position: int
    score: int


@dataclass(frozen=True)
class GameState:
    cur_player: Player
    other_player: Player


@dataclass
class Wins:
    cur_player: int = 0
    other_player: int = 0


class Game:
    def __init__(self, die_size: int, num_rolls: int, num_positions: int):
        self.die_size = die_size
        self.num_rolls = num_rolls
        self.num_positions = num_positions
        self.rolls = roll_combinations(die_size, num_rolls)

    def play(self, players: list[Player]):
        initial_state = GameState(players[0], players[1])
        wins = self._play_round(initial_state)
        return wins

    @cache
    def _play_round(self, state: GameState) -> Wins:
        wins = Wins()

        if state.other_player.score >= 21:
            wins.other_player = 1
            return wins

        for roll in self.rolls:

            new_position = (state.cur_player.position + roll) % self.num_positions
            new_score = state.cur_player.score + new_position + 1
            new_Player = Player(new_position, new_score)

            subsequent_wins = self._play_round(GameState(state.other_player, new_Player))
            wins.cur_player += subsequent_wins.other_player
            wins.other_player += subsequent_wins.cur_player
        return wins


def roll_combinations(die_size: int, num_rolls: int) -> list[int]:
    die_values = range(1, die_size + 1)
    all_die_rolls = [sum(x) for x in itertools.product(die_values, repeat=num_rolls)]
    return all_die_rolls


def get_part_one_result(file_name: str) -> int:
    players = load_data_structures_from_file(file_name)
    game = Game(3, 3, 10)
    wins = game.play(players)
    return max(wins.cur_player, wins.other_player)


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
