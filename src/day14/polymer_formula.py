from dataclasses import dataclass

from src.day14.polymer_pair import PolymerPair


@dataclass
class PolymerFormula:
    input: PolymerPair
    inserted: str

    def compute(self, count: int) -> (PolymerPair, PolymerPair, str):
        new_left = PolymerPair(self.input.left, self.inserted, count)
        new_right = PolymerPair(self.inserted, self.input.right, count)
        return new_left, new_right, self.inserted


class PolymerFormulaCollection(list[PolymerFormula]):
    def find(self, pair: PolymerPair):
        return next(iter([x for x in self if x.input == pair]), None)

    def compute(self, input_pair: PolymerPair) -> (PolymerPair, PolymerPair, str):
        input_formula = self.find(input_pair)
        return input_formula.compute(input_pair.count)

