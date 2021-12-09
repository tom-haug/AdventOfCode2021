from enum import Enum


class SegmentPosition(Enum):
    top = 1
    top_left = 2
    top_right = 3
    bottom = 4
    bottom_left = 5
    bottom_right = 6
    middle = 7

    @staticmethod
    def all():
        return [SegmentPosition.top, SegmentPosition.top_left, SegmentPosition.top_right, SegmentPosition.bottom,
                SegmentPosition.bottom_left, SegmentPosition.bottom_right, SegmentPosition.middle]
