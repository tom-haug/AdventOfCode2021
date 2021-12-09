from src.shared.utils import load_text_file


def get_part_one_result(file_name: str) -> int:
    file_contents = load_text_file(file_name)
    result = 0
    for line in file_contents:
        line_parts = line.split(" | ")
        signal_patterns = line_parts[0]
        output_values = line_parts[1].split(" ")
        filtered_output = list(filter(lambda value: len(value) in [2, 3, 4, 7], output_values))
        result += len(filtered_output)
    return result


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)
