import pandas as pd
from abc import ABC, abstractmethod

from src.shared import load_text_file
from src.day04.bingo_board import BingoBoard


class BingoGame(ABC):
    def __init__(self, file_name: str, board_size: int):
        self.game_numbers, self.game_boards = self._load_game_numbers_and_boards_from_file(file_name, board_size)
        self.round_number = -1
        self.winning_board = None

    def play_game(self) -> int:
        while not self.winning_board:
            self._play_round()
        return self._calculate_winner_score()

    def _load_game_numbers_and_boards_from_file(self, file_name: str, board_size: int) -> (list[int], list[BingoBoard]):
        lines = load_text_file(file_name)
        game_numbers = [int(value) for value in lines[0].split(",")]
        boards_list = self._load_boards_from_input(lines[2:], board_size)
        return game_numbers, boards_list

    def _load_boards_from_input(self, lines: list[str], board_size: int):
        boards_list: list[BingoBoard] = []
        current_board: pd.DataFrame = pd.DataFrame(columns=range(board_size))
        for line in lines:
            if line == "":
                boards_list.append(BingoBoard(current_board))
                current_board = pd.DataFrame(columns=range(board_size))
                continue
            line = line.replace("  ", " ").strip()
            cell_values = [int(cell) for cell in line.split(" ")]
            series = pd.Series(cell_values)
            current_board = current_board.append(series, ignore_index=True)
        boards_list.append(BingoBoard(current_board))
        return boards_list

    def _play_round(self):
        self.round_number += 1
        game_number = self.game_numbers[self.round_number]
        for board in self.game_boards[::-1]:  # go in reverse to allow removing boards
            if board.check_hit(game_number):
                if board.check_win():
                    self._on_bingo_success(board)

    def _calculate_winner_score(self):
        if self.winning_board is None:
            raise Exception("Game is not yet won")

        unmarked_sum = self.winning_board.sum_values_for_hit_status(0)
        winning_game_number = self.game_numbers[self.round_number]
        total_score = unmarked_sum * winning_game_number
        return total_score

    @abstractmethod
    def _on_bingo_success(self, board: BingoBoard):
        ...
