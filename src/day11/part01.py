from src.day11.flashing_system import FlashingSystem
from src.shared import load_int_nparray_from_file


def get_part_one_result(file_name: str, num_steps: int) -> int:
    octopuses = load_int_nparray_from_file(file_name)
    system = FlashingSystem(octopuses)
    system.run_step_count(num_steps)
    return system.flash_count


if __name__ == "__main__":
    result = get_part_one_result("src/day11/input.txt", 100)
    print(result)
