import pandas as pd
import numpy as np


class BingoBoard:
    def __init__(self, df_values: pd.DataFrame):
        self.df_values = df_values
        self.df_hits = pd.DataFrame(np.full(self.df_values.shape, False))

    def check_hit(self, search_value: int) -> bool:
        (rows, cols) = self.df_values.shape
        for row in range(rows):
            for col in range(cols):
                if self.df_values[col][row] == search_value:
                    self.df_hits[col][row] = True
                    return True
        return False

    def check_win(self):
        (rows, cols) = self.df_hits.shape
        for row in range(rows):
            if self._is_winning_series(self.df_hits.iloc[row]):
                return True
        for col in range(cols):
            if self._is_winning_series(self.df_hits[col]):
                return True
        return False

    def sum_values_for_hit_status(self, hit_status: bool) -> int:
        total = 0
        (rows, cols) = self.df_hits.shape
        for row in range(rows):
            for col in range(cols):
                if self.df_hits[col][row] == hit_status:
                    total += self.df_values[col][row]
        return total

    @staticmethod
    def _is_winning_series(series: pd.Series):
        return all(value is True for value in series)
