from src.day14.common import process


def get_part_one_result(file_name: str, step_count: int):
    return process(file_name, step_count)


if __name__ == "__main__":
    result = get_part_one_result("src/day14/input.txt", 10)
    print(result)
