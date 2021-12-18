import functools
import math
from collections import deque
from enum import Enum
from math import log2
from typing import TypeVar

from src.shared.utils import load_text_file


class PacketType(Enum):
    UNKNOWN = -1
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL = 7


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
    def __init__(self, value: str = "", number_base: int = 2, literal_value: int = None):
        self.literal_value: int = literal_value if literal_value is not None else 0
        if number_base != 2:
            value = self._to_binary(value, number_base)
        super().__init__(value)
        self.version: int = -1
        self.packet_type: PacketType = PacketType.UNKNOWN
        self.subpackets: list[Packet] = []

    def process(self) -> str:
        self.version = self.pop_left_int(BitLength.VERSION)
        self.packet_type = PacketType(self.pop_left_int(BitLength.TYPE_ID))
        if self.packet_type == PacketType.LITERAL:
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

    def pop_left_str(self, count: int):
        binary_string = "".join([self.popleft() for x in range(count)])
        return binary_string

    def pop_left_int(self, count: int):
        binary_string = self.pop_left_str(count)
        return int(binary_string, 2)

    def pop_literal_value(self) -> int:
        binary_value = ""
        keep_going = True
        while keep_going and len(self) >= 5:
            keep_going = self.popleft() == "1"
            binary_value += self.pop_left_str(4)
        return int(binary_value, 2)

    def pop_subpackets_by_length(self, subpacket_length) -> list['Packet']:
        subpackets: list[Packet] = []
        while len(self) >= subpacket_length:
            subpacket = Packet(self.pop_left_str(subpacket_length), 2)
            subpackets.append(subpacket)
        return subpackets

    @staticmethod
    def _to_binary(value: str, number_base: int) -> str:
        binary_string = ""
        bits_per_digit = int(log2(number_base))
        for char in value:
            binary_char_value = bin(int(char, number_base))[2:].zfill(bits_per_digit)
            binary_string += binary_char_value
        return binary_string

    @property
    def flattened_subpackets(self) -> list['Packet']:
        all_subpackets: list['Packet'] = []
        for subpacket in self.subpackets:
            all_subpackets.append(subpacket)
            all_subpackets += subpacket.flattened_subpackets
        return all_subpackets


    def __repr__(self):
        return "".join([x for x in self])

    def __add__(self, other: 'Packet') -> 'Packet':
        return Packet(literal_value=self.value + other.value)

    def __radd__(self, other: 'Packet') -> 'Packet':
        return self if other is None else self.__add__(other)

    def __mul__(self, other: 'Packet') -> 'Packet':
        return self if other is None else Packet(literal_value=self.value * other.value)

    def __lt__(self, other: 'Packet') -> bool:
        return self.value < other.value

    def __eq__(self, other: 'Packet') -> bool:
        return self.value == other.value

    def __gt__(self, other: 'Packet') -> bool:
        return self.value > other.value


    @property
    def value(self) -> int:
        match self.packet_type:
            case PacketType.UNKNOWN:
                return self.literal_value
            case PacketType.LITERAL:
                return self.literal_value
            case PacketType.SUM:
                return sum(self.subpackets).value
            case PacketType.PRODUCT:
                return product(self.subpackets).value
            case PacketType.MINIMUM:
                return min(self.subpackets).value
            case PacketType.MAXIMUM:
                return max(self.subpackets).value
            case PacketType.GREATER_THAN:
                return 1 if self.subpackets[0] > self.subpackets[1] else 0
            case PacketType.LESS_THAN:
                return 1 if self.subpackets[0] < self.subpackets[1] else 0
            case PacketType.EQUAL:
                return 1 if self.subpackets[0] == self.subpackets[1] else 0


T = TypeVar('T')


def product(items: list[Packet]) -> Packet:
    return functools.reduce(lambda prev, cur: prev * cur, items, Packet(literal_value=1))


def sum(items: list[Packet]) -> Packet:
    return functools.reduce(lambda prev, cur: prev + cur, items, Packet(literal_value=0))


def get_part_two_result(file_name: str):
    hex_input = load_text_file(file_name)[0]
    packet = Packet(hex_input, 16)
    packet.process()
    result = packet.value
    return result


def get_version_sum(packet: Packet) -> int:
    version_sum: int = packet.version
    for subpacket in packet.flattened_subpackets:
        version_sum += subpacket.version
    return version_sum


if __name__ == "__main__":
    result = get_part_one_result("src/day16/input.txt")
    print(result)
