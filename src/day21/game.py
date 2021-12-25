from __future__ import annotations
from functools import cache
from typing import Iterator
from attr import dataclass


class Game:
    def __init__(self, num_positions: int, die_roller: Iterator[list[int]], winning_score: int):
        self.num_positions = num_positions
        self.die_roller = die_roller
        self.winning_score = winning_score
        self.winning_state: GameState

    def play(self, player1: Player, player2: Player):
        initial_state = GameState(player1, player2)
        wins = self._play_round(initial_state)
        return wins

    @cache
    def _play_round(self, state: GameState) -> Wins:
        wins = Wins()

        if state.other_player.score >= self.winning_score:
            wins.other_player = 1
            self.winning_state = state
            return wins

        next_roll = next(self.die_roller)
        for roll in next_roll:
            new_position = (state.cur_player.position + roll) % self.num_positions
            new_score = state.cur_player.score + new_position + 1
            new_player = Player(new_position, new_score)

            subsequent_wins = self._play_round(GameState(state.other_player, new_player))
            wins.cur_player += subsequent_wins.other_player
            wins.other_player += subsequent_wins.cur_player
        return wins


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