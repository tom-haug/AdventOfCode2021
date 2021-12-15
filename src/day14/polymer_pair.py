from dataclasses import dataclass


@dataclass(eq=False)
class PolymerPair:
    left: str
    right: str
    count: int = 0

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right


class PolymerPairCollection(list[PolymerPair]):
    def find(self, pair: PolymerPair):
        return next(iter([x for x in self if x == pair]), None)

    def merge(self, pair: PolymerPair):
        existing = self.find(pair)
        if existing is None:
            self.append(pair)
        else:
            existing.count += pair.count
