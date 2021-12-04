from src.shared.utils import load_text_file
import pandas as pd
import numpy as np

class GameBoard:
    def __init__(self, df_values: pd.DataFrame):
        self.df_values = df_values
        self.df_hits = pd.DataFrame(np.zeros(self.df_values.shape, dtype=int))

    def check_hit(self, search_value: int) -> bool:
        (rows, cols) = self.df_values.shape
        for row in range(rows):
            for col in range(cols):
                if self.df_values[col][row] == search_value:
                    self.df_hits[col][row] = 1
                    return True
        return False

    def check_win(self):
        (rows, cols) = self.df_hits.shape
        for row in range(rows):
            values = self.df_hits.iloc[row]
            win = True
            for value in values:
                if value != 1:
                    win = False
                    break
            if win:
                return True
        for col in range(cols):
            values = self.df_hits[col]
            win = True
            for value in values:
                if value != 1:
                    win = False
                    break
            if win:
                return True

    def sum_values_for_hit_status(self, hit_status: int) -> int:
        total = 0
        (rows, cols) = self.df_hits.shape
        for row in range(rows):
            for col in range(cols):
                if self.df_hits[col][row] == hit_status:
                    total += self.df_values[col][row]
        return total


def get_part_two_result(file_name: str):
    board_size = 5
    lines = load_text_file(file_name)
    game_numbers = [int(value) for value in lines[0].split(",")]
    boards_list = load_boards_from_input(lines[2:], board_size)
    for search_value in game_numbers:
        for idx, board in list(enumerate(boards_list))[::-1]:
            found = board.check_hit(int(search_value))
            if found:
                win = board.check_win()
                if win:
                    if len(boards_list) == 1:
                        unmarked_sum = board.sum_values_for_hit_status(0)
                        total_score = unmarked_sum * search_value
                        return total_score

                    boards_list.remove(board)
                    continue

def load_boards_from_input(lines: list[str], board_size: int):
    boards_list: list[GameBoard] = []
    current_board: pd.DataFrame = pd.DataFrame(columns=range(board_size))
    for line in lines:
        if line == "":
            boards_list.append(GameBoard(current_board))
            current_board = pd.DataFrame(columns=range(board_size))
            continue
        line = line.replace("  ", " ").strip()
        cell_values = [int(cell) for cell in line.split(" ")]
        series = pd.Series(cell_values, index = current_board.columns)
        current_board = current_board.append(series, ignore_index=True)
    boards_list.append(GameBoard(current_board))
    return boards_list


if __name__ == "__main__":
    result = get_part_two_result("input.txt")
    print(result)
