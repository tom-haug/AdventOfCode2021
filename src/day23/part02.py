import time
from src.day23.common import get_game_result


if __name__ == "__main__":
    start = time.time()
    lowest_energy, movement_log = get_game_result("src/day23/input_sample02.txt")
    end = time.time()

    print(f"Running Time: {end - start}")
    print(f"Lowest Energy: {lowest_energy}")
    for move in movement_log:
        print(move)
