from src.day11.flashing_system import FlashingSystem
from src.shared import load_int_nparray_from_file


def get_part_two_result(file_name: str) -> int:
    octopuses = load_int_nparray_from_file(file_name)
    system = FlashingSystem(octopuses)
    system.run_until_all_flash()
    return system.step_num


if __name__ == "__main__":
    result = get_part_two_result("src/day11/input_sample01.txt")
    print(result)
