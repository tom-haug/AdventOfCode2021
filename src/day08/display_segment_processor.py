from dataclasses import dataclass

from src.day08.digit_definitions import DigitDefinition
from src.day08.display_segment import DisplaySegment
from src.day08.segment_positions import SegmentPosition


@dataclass
class DisplaySegmentProcessor:
    wire_segments: list[str]
    digits: list[DigitDefinition]
    display_segment: DisplaySegment

    def process(self):
        self._add_wires_to_digits()
        self._solve_by_position_occurrence_count()

        while not self.display_segment.is_complete:
            self._remove_impossible_wire_sequences_from_digits()
            self._solve_by_only_wire_in_common()
            self._solve_by_only_remaining_wire()
        self._remove_impossible_wire_sequences_from_digits()

    def _add_wires_to_digits(self):
        for wires_segment in self.wire_segments:
            for digit in self.digits:
                digit.try_add_wire_sequence(wires_segment)

    def _solve_by_position_occurrence_count(self):
        """
        solve by determining all the positions with a unique count of digits that use them and then
        getting the only wire that occurs that many times
        """
        segment_position_digit_counts: list[tuple[SegmentPosition, int]] = []
        for segment_wire_pair in self.display_segment.get_segment_wire_pairs(False):
            digits_with_segment = len([digit for digit in self.digits if digit.contains_segment_position(segment_wire_pair.segment_position)])
            segment_position_digit_counts.append((segment_wire_pair.segment_position, digits_with_segment))

        for segment_position_digit_count in segment_position_digit_counts:
            if len([x for x in segment_position_digit_counts if x[1] == segment_position_digit_count[1]]) == 1:
                wire = self._get_wire_by_occurrence_count(segment_position_digit_count[1])
                self.display_segment.connect_wire(segment_position_digit_count[0], wire)

    def _solve_by_only_remaining_wire(self):
        """
        if there is only one unknown wire left, sometimes the other solvers cannot find the last one
        so we have to manually find and connect it
        """
        unknown_wire_pairs = self.display_segment.get_segment_wire_pairs(False)
        if len(unknown_wire_pairs) == 1:
            wire = [wire for wire in self._get_distinct_wires() if not self.display_segment.has_wire(wire)][0]
            self.display_segment.connect_wire(unknown_wire_pairs[0].segment_position, wire)

    def _solve_by_only_wire_in_common(self):
        """
        find a list of digits that contain the same segment position and then find the only wire in common with them
        """
        for unknown_segment_wire_pair in self.display_segment.get_segment_wire_pairs(False):
            digits = [digit for digit in self.digits if digit.contains_segment_position(unknown_segment_wire_pair.segment_position) and digit.wire_sequence_found]

            if len(digits) == 0:
                continue

            common_wires = digits[0].wire_sequence
            for digit in digits[1:]:
                for wire in common_wires[::-1]:
                    if wire not in digit.wire_sequence:
                        common_wires.remove(wire)

            if len(common_wires) == 1:
                self.display_segment.connect_wire(unknown_segment_wire_pair.segment_position, common_wires[0])

    def _remove_impossible_wire_sequences_from_digits(self):
        """ takes away wire sequences from digits based upon solved wire positions """
        for digit in self.digits:
            if not digit.wire_sequence_found:
                for wire_sequence in digit.possible_wire_sequences[::-1]:
                    self._remove_wire_when_invalid_segment_position(digit, wire_sequence)

    def _remove_wire_when_invalid_segment_position(self, digit: DigitDefinition, wire_sequence):
        for segment_wire_pair in self.display_segment.get_segment_wire_pairs(True):
            if segment_wire_pair.segment_position in digit.segment_positions():
                if segment_wire_pair.wire not in wire_sequence:
                    digit.remove_wire_sequence(wire_sequence)
                    return

    def _get_distinct_wires(self) -> list[str]:
        return list(set([wire for wire_segment in self.wire_segments for wire in wire_segment]))

    def _get_wire_by_occurrence_count(self, frequency: int):
        for wire in self._get_distinct_wires():
            if len([wire_segment for wire_segment in self.wire_segments if wire in wire_segment]) == frequency:
                return wire
        raise Exception("Could not find wire for frequency")

    def decode_digit(self, wire_segment: str):
        '''
        after all the wire positions have been solved, pass in a wire segment to get the corresponding digit
        '''
        sorted_wire_sequence = sorted([wire for wire in wire_segment])
        for digit in self.digits:
            sorted_digit_wire_sequence = sorted(digit.wire_sequence)
            if sorted_wire_sequence == sorted_digit_wire_sequence:
                return digit
        raise Exception(f"wire sequence {wire_segment} is not assigned to a digit")
