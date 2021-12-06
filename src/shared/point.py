class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def extend(self, new_x: int, new_y: int):
        if new_x > self.x:
            self.x = new_x
        if new_y > self.y:
            self.y = new_y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
