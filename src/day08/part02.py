from src.day08.digit_definitions import DigitDefinition
from src.day08.display_segment import DisplaySegment
from src.day08.display_segment_processor import DisplaySegmentProcessor
from src.shared import load_text_file


def get_part_two_result(file_name: str) -> int:
    file_contents = load_text_file(file_name)

    output_values_list: list[int] = []
    for line in file_contents:
        line_parts = line.split(" | ")
        puzzle_wire_segments = line_parts[0].split(" ")
        output_wire_segments = line_parts[1].split(" ")
        display_segment = DisplaySegment()

        processor = DisplaySegmentProcessor(puzzle_wire_segments, DigitDefinition.create_all(), display_segment)
        processor.process()

        digits = [processor.decode_digit(wire_segment) for wire_segment in output_wire_segments]
        output_values_list.append(int("".join([str(digit.value) for digit in digits])))

    return sum(output_values_list)


if __name__ == "__main__":
    result = get_part_two_result("src/day08/input.txt")
    print(result)
