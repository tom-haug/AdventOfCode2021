import numpy as np
from src.shared.utils import load_text_file, load_int_nparray_from_file


class FlashingSystem:
    def __init__(self, octopuses: np.ndarray):
        self.octopuses = octopuses
        self.already_flashed: np.ndarray
        self.flash_count = 0

    def run(self, num_steps: int):
        for step in range(num_steps):
            self._step()

    def _reset_already_flashed(self):
        self.already_flashed = np.full(self.octopuses.shape, False, dtype=bool)

    def _step(self):
        self._reset_already_flashed()
        self._increment_energy()
        self._flash_all()
        self._reset_energy_levels()

    def _increment_energy(self):
        rows, cols = self.octopuses.shape
        for row in range(rows):
            for col in range(cols):
                self.octopuses[row, col] += 1

    def _reset_energy_levels(self):
        rows, cols = self.octopuses.shape
        for row in range(rows):
            for col in range(cols):
                if self.octopuses[row, col] > 9:
                    self.octopuses[row, col] = 0

    def _flash_all(self):
        rows, cols = self.octopuses.shape
        for row in range(rows):
            for col in range(cols):
                self._check_flash(row, col)

    def _check_flash(self, row, col):
        if self.octopuses[row, col] > 9 and not self.already_flashed[row, col]:
            self._flash(row, col)

    def _flash(self, origin_row, origin_col):
        self.already_flashed[origin_row, origin_col] = True
        self.flash_count += 1

        rows, cols = self.octopuses.shape
        for row in range(origin_row - 1, origin_row + 2):
            for col in range(origin_col - 1, origin_col + 2):
                if 0 <= row < rows and 0 <= col < cols and (row, col) != (origin_row, origin_col):
                    self.octopuses[row, col] += 1
                    self._check_flash(row, col)


def get_part_one_result(file_name: str, num_steps: int) -> int:
    octopuses = load_int_nparray_from_file(file_name)
    system = FlashingSystem(octopuses)
    system.run(num_steps)
    return system.flash_count


if __name__ == "__main__":
    result = get_part_one_result("input.txt", 100)
    print(result)
