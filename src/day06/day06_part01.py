from typing import Callable

from src.shared.utils import load_text_file


class Fish:
    def __init__(self, spawn_fish: Callable, timer=9):
        self.timer = timer
        self.spawn_fish = spawn_fish

    def increment(self):
        if self.timer == 0:
            self.timer = 6
            self.spawn_fish()
        else:
            self.timer -= 1


class FishContainer:
    def __init__(self, file_name: str):
        self.all_fish = self._load_fish_from_file(file_name)

    def _load_fish_from_file(self, file_name: str) -> list[Fish]:
        lines = load_text_file(file_name)
        fish_timer_list = lines[0].split(",")
        fish: list[Fish] = []
        for fish_timer in fish_timer_list:
            fish.append(Fish(self.spawn_fish, int(fish_timer)))
        return fish

    def next_day(self):
        for fish in self.all_fish:
            fish.increment()

    def spawn_fish(self):
        self.all_fish.append(Fish(self.spawn_fish))


def get_part_one_result(file_name: str) -> int:
    fish_container = FishContainer(file_name)
    print(f"beginning fish count:{len(fish_container.all_fish)}")
    for day in range(80):
        fish_container.next_day()
    fish_count = len(fish_container.all_fish)
    return fish_count


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)
