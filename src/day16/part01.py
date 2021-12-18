from src.day16.packet import Packet
from src.shared.utils import load_text_file, NumberSystem


def get_part_one_result(file_name: str):
    hex_input = load_text_file(file_name)[0]
    packet = Packet(hex_input, NumberSystem.HEXADECIMAL)
    packet.process()
    result = sum_versions(packet)
    return result


def sum_versions(packet: Packet) -> int:
    version_sum: int = packet.version
    for subpacket in packet.flattened_subpackets:
        version_sum += subpacket.version
    return version_sum


if __name__ == "__main__":
    result = get_part_one_result("src/day16/input.txt")
    print(result)
