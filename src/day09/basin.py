from src.shared.map_object import MapObject
from src.shared.point import Point


class Basin:
    def __init__(self, origin_location: Point, origin_value: int):
        self.origin = MapObject(origin_location, origin_value)
        self.included_locations: list[MapObject[int]] = []

    def add_location(self, location: Point, value: int):
        self.included_locations.append(MapObject(location, value))

    def has_location(self, location: Point):
        for included_location in self.included_locations:
            if included_location.location == location:
                return True
        return False

    def size(self):
        return len(self.included_locations)
