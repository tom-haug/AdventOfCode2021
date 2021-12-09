from src.day08.segment_positions import SegmentPosition


class SegmentPositionWirePair:
    def __init__(self, segment_position: SegmentPosition, wire: str = None):
        self.segment_position = segment_position
        self.wire = wire


class DisplaySegment:
    def __init__(self):
        self.segment_wire_pairs = [SegmentPositionWirePair(segment_position) for segment_position in SegmentPosition.all()]

    @property
    def is_complete(self) -> bool:
        return len([x for x in self.segment_wire_pairs if x.wire is None]) == 0

    def connect_wire(self, segment_position: SegmentPosition, wire: str):
        segment_wire_pair = [x for x in self.segment_wire_pairs if x.segment_position == segment_position][0]
        segment_wire_pair.wire = wire

    def get_segment_wire_pairs(self, completed: bool) -> list[SegmentPositionWirePair]:
        return [x for x in self.segment_wire_pairs if (x.wire is not None) == completed]

    def has_wire(self, wire: str) -> bool:
        return len([x for x in self.segment_wire_pairs if x.wire == wire]) == 1
