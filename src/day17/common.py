from src.shared.point import Point
from src.shared.square import Square
from src.shared.utils import load_text_file


def load_target_from_file(file_name: str) -> Square:
    line = load_text_file(file_name)[0]
    line = line.strip("target area: ")
    parts = line.split(", ")
    x_range = parts[0].strip("x=")
    y_range = parts[1].strip("y=")
    x1, x2 = x_range.split("..")
    y2, y1 = y_range.split("..")
    target = Square(Point(int(x1), int(y1)), Point(int(x2), int(y2)))
    return target


def get_max_y_velocity(target: Square) -> int:
    return (target.bottom_right.y * -1) - 1
