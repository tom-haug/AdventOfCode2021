from enum import Enum

import numpy as np
from attr import dataclass

from src.shared.point import Point
from src.shared.utils import load_text_file


class FoldDirection(Enum):
    VERTICAL = 0
    HORIZONTAL = 1


@dataclass
class Fold:
    direction: FoldDirection
    position: int


def load_structures_from_file(file_name: str) -> (list[Point], list[Fold]):
    lines = load_text_file(file_name)

    # load points
    points: list[Point] = []
    while True:
        line = lines.pop(0)
        # division between file sections
        if len(line) == 0:
            break
        parts = line.split(",")
        x = int(parts[0])
        y = int(parts[1])
        points.append(Point(x, y))

    # load folds
    folds: list[Fold] = []
    for line in lines:
        line = line.removeprefix("fold along ")
        parts = line.split("=")
        direction = FoldDirection.HORIZONTAL if parts[0] == "x" else FoldDirection.VERTICAL
        position = int(parts[1])
        folds.append(Fold(direction, position))

    return points, folds


def build_sheet(points: list[Point]) -> np.ndarray:
    width = max([point.x for point in points]) + 1
    height = max([point.y for point in points]) + 1
    array = np.zeros((height, width), dtype=int)
    for point in points:
        array[point.y, point.x] = 1
    return array


def fold_sheet(sheet: np.ndarray, fold: Fold) -> np.ndarray:
    if fold.direction == FoldDirection.VERTICAL:
        top = np.array(sheet[:fold.position, ::])
        bottom = np.array(sheet[fold.position + 1:, ::])
        if top.shape != bottom.shape:
            delta = top.shape[0] - bottom.shape[0]
            if delta > 0:
                bottom = np.reshape(bottom, top.shape)
            elif delta < 0:
                reshaped_top = np.reshape(top, bottom.shape)
                top = np.roll(reshaped_top, abs(delta), axis=0)
        inverted_bottom = np.flipud(bottom)
        overlayed = np.array(np.add(top, inverted_bottom))
        return overlayed
    else:
        left = np.array(sheet[::, :fold.position])
        right = np.array(sheet[:, fold.position + 1:])
        if left.shape != right.shape:
            delta = left.shape[1] - right.shape[1]
            if delta > 0:
                right = np.reshape(right, left.shape)
            elif delta < 0:
                reshaped_left = np.reshape(left, right.shape)
                left = np.roll(reshaped_left, abs(delta), axis=1)
        inverted_left = np.fliplr(left)
        overlayed = np.array(np.add(inverted_left, right))
        return overlayed


def point_count(sheet: np.ndarray) -> int:
    return np.count_nonzero(sheet)


def get_part_one_result(file_name: str):
    points, folds = load_structures_from_file(file_name)
    sheet = build_sheet(points)
    print(sheet)
    for fold in folds:
        sheet = fold_sheet(sheet, fold)
        print(sheet)
        break
    result = point_count(sheet)
    return result

if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)

# 98 wrong