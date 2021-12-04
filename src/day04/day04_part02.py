from bingo_board import BingoBoard
from bingo_game import BingoGame


class LastBoardStandingBingoGame(BingoGame):
    def _on_bingo_success(self, board: BingoBoard):
        if (len(self.game_boards)) == 1:
            self.winning_board = board
        else:
            self.game_boards.remove(board)


def get_part_two_result(file_name: str):
    return LastBoardStandingBingoGame(file_name, 5).play_game()


if __name__ == "__main__":
    result = get_part_two_result("input.txt")
    print(result)
