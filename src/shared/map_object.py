from typing import TypeVar, Generic
from attr import dataclass
from src.shared import Point

T = TypeVar('T')

@dataclass
class MapObject(Generic[T]):
    location: Point
    value: T
