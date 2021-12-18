from src.day16.packet import Packet
from src.shared.utils import load_text_file, NumberSystem


def get_part_two_result(file_name: str):
    hex_input = load_text_file(file_name)[0]
    packet = Packet(hex_input, NumberSystem.HEXADECIMAL)
    packet.process()
    result = packet.value
    return result


if __name__ == "__main__":
    result = get_part_two_result("src/day16/input.txt")
    print(result)
