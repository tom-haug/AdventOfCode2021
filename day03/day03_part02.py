import pandas as pd
import sys
sys.path.append("..")
from shared.utils import load_text_file


def get_part_two_result(file_name: str) -> int:
    lines = load_text_file(file_name)
    df_all_values = pd.DataFrame([[int(char) for char in line] for line in lines])

    oxygen_generator_rating = calculate_rating(df_all_values, oxygen_generator)
    co2_scrubber_rating = calculate_rating(df_all_values, co2_scrubber)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    return life_support_rating


def calculate_rating(df_all_values: pd.DataFrame, comparer):
    df_filtered = filter_data_frame(df_all_values, 0, comparer)
    bit_list = df_filtered.values.tolist()[0]
    return bit_list_to_number(bit_list)


def filter_data_frame(df: pd.DataFrame, position: int, comparer):
    filter_value = most_common_value_at_position(df, position, comparer)
    df_filtered = df[df[position] == filter_value]
    if len(df_filtered) == 1:
        return df_filtered
    else:
        return filter_data_frame(df_filtered, position + 1, comparer)


def most_common_value_at_position(df: pd.DataFrame, position: int, comparer) -> int:
    groups = df.groupby(position).groups
    return comparer(groups[0].size, groups[1].size)


def oxygen_generator(num_zeros: int, num_ones: int):
    if num_ones >= num_zeros:
        return 1
    else:
        return 0


def co2_scrubber(num_zeros: int, num_ones: int):
    if num_ones < num_zeros:
        return 1
    else:
        return 0


def bit_list_to_number(bitlist: list[int]):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out


if __name__ == "__main__":
    life_support_rating = get_part_two_result("input.txt")
    print(life_support_rating)