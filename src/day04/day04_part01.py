from bingo_board import BingoBoard
from bingo_game import BingoGame


class FirstBingoWinsBingoGame(BingoGame):
    def _on_bingo_success(self, board: BingoBoard):
        self.winning_board = board


def get_part_one_result(file_name: str):
    return FirstBingoWinsBingoGame(file_name, 5).play_game()


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)
