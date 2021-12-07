import numpy as np
from src.shared.utils import load_text_file


def load_state_from_file(file_name: str) -> np.ndarray:
    initial_day = np.zeros(9, dtype=np.ulonglong)
    initial_fish_state = [int(fish) for fish in load_text_file(file_name)[0].split(",")]

    for fish_state in initial_fish_state:
        initial_day[fish_state] += 1

    state = initial_day.reshape([1, 9])
    return state


def add_day(state: np.ndarray):
    most_recent_day = state[-1]
    next_day = np.zeros(9, dtype=np.ulonglong)
    for fish_cycle in range(8):
        next_day[fish_cycle] = most_recent_day[fish_cycle + 1]
    next_day[6] += most_recent_day[0]
    next_day[8] = most_recent_day[0]
    return np.append(state, [next_day], axis=0)


def get_fish_count_after_days(file_name: str, num_days: int) -> int:
    state = load_state_from_file(file_name)

    for day in range(num_days):
        state = add_day(state)

    last_day = state[-1]
    total_fish = last_day.sum()
    return total_fish
