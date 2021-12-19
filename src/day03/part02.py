import pandas as pd
import operator

from src.shared import ComparerFunc, load_int_data_frame_from_file, bit_list_to_number


class RatingCalculator:
    def __init__(self, comparer_func: ComparerFunc):
        self.comparer_func = comparer_func

    def calculate_rating(self, df_all_values: pd.DataFrame) -> int:
        df_filtered = self._filter_data_frame(df_all_values, 0)
        bit_list = df_filtered.values.tolist()[0]
        return bit_list_to_number(bit_list)

    def _filter_data_frame(self, df: pd.DataFrame, position: int) -> pd.DataFrame:
        filter_value = self._calculate_value_at_position(df, position)
        df_filtered = df[df[position] == filter_value]
        if len(df_filtered) == 1:
            return df_filtered
        else:
            return self._filter_data_frame(df_filtered, position + 1)

    def _calculate_value_at_position(self, df: pd.DataFrame, position: int) -> int:
        groups = df.groupby(position).groups
        return 1 if self.comparer_func(groups[1].size, groups[0].size) else 0


oxygen_rating_calculator = RatingCalculator(operator.ge)
co2_scrubber_calculator = RatingCalculator(operator.lt)


def get_part_two_result(file_name: str) -> int:
    df_all_values = load_int_data_frame_from_file(file_name)
    oxygen_generator_rating = oxygen_rating_calculator.calculate_rating(df_all_values)
    co2_scrubber_rating = co2_scrubber_calculator.calculate_rating(df_all_values)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    return life_support_rating


if __name__ == "__main__":
    life_support_rating = get_part_two_result("src/day03/input.txt")
    print(life_support_rating)