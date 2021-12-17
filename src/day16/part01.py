from collections import deque
from enum import Enum
from math import log2

from src.shared.utils import load_text_file


class PacketType(Enum):
    LITERAL = 4


class SubpacketLengthType:
    TOTAL_SUBPACKETS = 0
    COUNT_SUBPACKETS = 1


class BitLength:
    VERSION = 3
    TYPE_ID = 3
    SUBPACKET_LENGTH_TYPE_ID = 1
    SUBPACKET_LENGTH = 15
    SUBPACKET_COUNT = 11


class Packet(deque):
    def __init__(self, value: str, number_base: int):
        if number_base != 2:
            value = self._to_binary(value, number_base)
        super().__init__(value)
        self.version: int = -1
        self.type_id: int = -1
        self.literal_value: str = ""
        self.subpackets: list[Packet] = []

    def process(self) -> str:
        self.version = self.pop_left_int(BitLength.VERSION)
        self.type_id = self.pop_left_int(BitLength.TYPE_ID)
        if self.type_id == PacketType.LITERAL.value:
            self.literal_value = self.pop_literal_value()
        else: # operator
            length_type_id = self.pop_left_int(BitLength.SUBPACKET_LENGTH_TYPE_ID)
            if length_type_id == SubpacketLengthType.TOTAL_SUBPACKETS:
                subpacket_length = self.pop_left_int(BitLength.SUBPACKET_LENGTH)
                subpacket_content = self.pop_left_str(subpacket_length)
                while len(subpacket_content) > 0:
                    subpacket = Packet(subpacket_content, 2)
                    self.subpackets.append(subpacket)
                    subpacket_content = subpacket.process()
            elif length_type_id == SubpacketLengthType.COUNT_SUBPACKETS:
                subpacket_count = self.pop_left_int(BitLength.SUBPACKET_COUNT)
                cur_count = 0
                subpacket_content = str(self)
                while cur_count < subpacket_count:
                    subpacket = Packet(subpacket_content, 2)
                    self.subpackets.append(subpacket)
                    remaining_content = subpacket.process()
                    self.pop_left_str(len(subpacket_content) - len(remaining_content))
                    subpacket_content = remaining_content
                    cur_count += 1
        return self.pop_left_str(len(self))

    def pop_left_str(self, count: int, fixed_width: int = 0):
        binary_string = "".join([self.popleft() for x in range(count)])
        # int_value = int(binary_string, 2)
        # binary_char_value = bin(int_value)[2:].zfill(fixed_width)
        return binary_string

    def pop_left_int(self, count: int):
        binary_string = self.pop_left_str(count)
        return int(binary_string, 2)

    def pop_literal_value(self) -> str:
        binary_value = ""
        keep_going = True
        while keep_going and len(self) >= 5:
            keep_going = self.popleft() == "1"
            binary_value += self.pop_left_str(4)
        return binary_value

    def pop_subpackets_by_length(self, subpacket_length) -> list['Packet']:
        subpackets: list[Packet] = []
        while len(self) >= subpacket_length:
            subpacket = Packet(self.pop_left_str(subpacket_length), 2)
            subpackets.append(subpacket)
        return subpackets

    @property
    def flattened_subpackets(self) -> list['Packet']:
        all_subpackets: list['Packet'] = []
        for subpacket in self.subpackets:
            all_subpackets.append(subpacket)
            all_subpackets += subpacket.flattened_subpackets
        return all_subpackets

    @property
    def int_literal_value(self):
        return int(self.literal_value, 2)

    def __repr__(self):
        return "".join([x for x in self])

    @staticmethod
    def _to_binary(value: str, number_base: int) -> str:
        binary_string = ""
        bits_per_digit = int(log2(number_base))
        for char in value:
            binary_char_value = bin(int(char, number_base))[2:].zfill(bits_per_digit)
            binary_string += binary_char_value
        return binary_string


def get_part_one_result(file_name: str):
    hex_input = load_text_file(file_name)[0]
    packet = Packet(hex_input, 16)
    packet.process()
    result = get_version_sum(packet)
    return result


def get_version_sum(packet: Packet) -> int:
    version_sum: int = packet.version
    for subpacket in packet.flattened_subpackets:
        version_sum += subpacket.version
    return version_sum


if __name__ == "__main__":
    result = get_part_one_result("src/day16/input.txt")
    print(result)
