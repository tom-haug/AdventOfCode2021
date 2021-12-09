from abc import ABC, abstractmethod

from src.day08.segment_positions import SegmentPosition


class DigitDefinition(ABC):
    def __init__(self):
        self.possible_wire_sequences: list[str] = []

    @staticmethod
    def create_all():
        return [DigitZero(), DigitOne(), DigitTwo(), DigitThree(), DigitFour(), DigitFive(), DigitSix(), DigitSeven(),
         DigitEight(), DigitNine()]

    @property
    @abstractmethod
    def value(self) -> int:
        ...

    @property
    def wire_sequence_found(self):
        return len(self.possible_wire_sequences) == 1

    @property
    def wire_sequence(self) -> list[str]:
        if not self.wire_sequence_found:
            raise Exception("Multiple wire sequence possibilities exist")
        return [wire for wire in self.possible_wire_sequences[0]]

    @abstractmethod
    def segment_positions(self) -> list[SegmentPosition]:
        ...

    def try_add_wire_sequence(self, wire_sequence: str):
        if self._is_wire_sequence_possible(wire_sequence):
            self.possible_wire_sequences.append(wire_sequence)

    def remove_wire_sequence(self, wire_sequence: str):
        self.possible_wire_sequences.remove(wire_sequence)

    def contains_segment_position(self, segment_position: SegmentPosition) -> bool:
        return segment_position in self.segment_positions()

    def _is_wire_sequence_possible(self, wire_sequence: str):
        return len(wire_sequence) == len(self.segment_positions())


class DigitZero(DigitDefinition):
    @property
    def value(self):
        return 0

    def segment_positions(self):
        return [SegmentPosition.top, SegmentPosition.top_left, SegmentPosition.top_right, SegmentPosition.bottom,
                SegmentPosition.bottom_left, SegmentPosition.bottom_right]


class DigitOne(DigitDefinition):
    @property
    def value(self):
        return 1

    def segment_positions(self):
        return [SegmentPosition.top_right, SegmentPosition.bottom_right]


class DigitTwo(DigitDefinition):
    @property
    def value(self):
        return 2

    def segment_positions(self):
        return [SegmentPosition.top, SegmentPosition.top_right, SegmentPosition.middle, SegmentPosition.bottom_left,
                SegmentPosition.bottom]


class DigitThree(DigitDefinition):
    @property
    def value(self):
        return 3

    def segment_positions(self):
        return [SegmentPosition.top, SegmentPosition.top_right, SegmentPosition.bottom, SegmentPosition.bottom_right,
                SegmentPosition.middle]


class DigitFour(DigitDefinition):
    @property
    def value(self):
        return 4

    def segment_positions(self):
        return [SegmentPosition.top_left, SegmentPosition.top_right, SegmentPosition.bottom_right,
                SegmentPosition.middle]


class DigitFive(DigitDefinition):
    @property
    def value(self):
        return 5

    def segment_positions(self):
        return [SegmentPosition.top, SegmentPosition.top_left, SegmentPosition.bottom, SegmentPosition.bottom_right,
                SegmentPosition.middle]


class DigitSix(DigitDefinition):
    @property
    def value(self):
        return 6

    def segment_positions(self):
        return [SegmentPosition.top, SegmentPosition.top_left, SegmentPosition.bottom, SegmentPosition.bottom_left,
                SegmentPosition.bottom_right, SegmentPosition.middle]


class DigitSeven(DigitDefinition):
    @property
    def value(self):
        return 7

    def segment_positions(self):
        return [SegmentPosition.top, SegmentPosition.top_right, SegmentPosition.bottom_right]


class DigitEight(DigitDefinition):
    @property
    def value(self):
        return 8

    def segment_positions(self):
        return [SegmentPosition.top, SegmentPosition.top_left, SegmentPosition.top_right, SegmentPosition.bottom,
                SegmentPosition.bottom_left, SegmentPosition.bottom_right, SegmentPosition.middle]


class DigitNine(DigitDefinition):
    @property
    def value(self):
        return 9

    def segment_positions(self):
        return [SegmentPosition.top, SegmentPosition.top_left, SegmentPosition.top_right, SegmentPosition.bottom,
                SegmentPosition.bottom_right, SegmentPosition.middle]

