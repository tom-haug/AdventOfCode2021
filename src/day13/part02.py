from src.day13.common import get_folded_sheet_from_file


def get_part_two_result(file_name: str):
    return get_folded_sheet_from_file(file_name)


if __name__ == "__main__":
    sheet = get_part_two_result("src/day13/input.txt")
    print(sheet)
