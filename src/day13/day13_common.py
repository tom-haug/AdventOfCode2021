import numpy as np
from enum import Enum
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


def load_data_structures_from_file(file_name: str) -> (list[Point], list[Fold]):
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
        top = np.array(sheet[:fold.position, :])
        bottom = np.array(sheet[fold.position + 1:, :])
        inverted_bottom = np.flipud(bottom)
        overlaid = np.array(np.add(top, inverted_bottom))
        return overlaid
    else:
        left = np.array(sheet[:, :fold.position])
        right = np.array(sheet[:, fold.position + 1:])
        inverted_left = np.fliplr(left)
        overlaid = np.array(np.add(inverted_left, right))
        return overlaid


def get_folded_sheet_from_file(file_name: str, num_folds: int = None):
    points, folds = load_data_structures_from_file(file_name)
    sheet = build_sheet(points)
    print(sheet)
    for idx, fold in enumerate(folds):
        sheet = fold_sheet(sheet, fold)
        if num_folds is not None and num_folds <= idx + 1:
            break
    oriented_sheet = np.fliplr(sheet)
    return oriented_sheet
