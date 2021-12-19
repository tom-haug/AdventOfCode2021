import collections

from src.day14.polymer_formula import PolymerFormulaCollection, PolymerFormula
from src.day14.polymer_pair import PolymerPair, PolymerPairCollection
from src.shared import load_text_file


def process(file_name: str, step_count: int):
    polymer_template, formulas = load_data_structures_from_file(file_name)

    output_pairs = get_pairs_from_template(polymer_template)
    polymer_counter = collections.Counter(polymer_template)

    for step in range(step_count):
        input_pairs = output_pairs
        output_pairs = PolymerPairCollection()

        for pair in input_pairs:
            output1, output2, inserted = formulas.compute(pair)
            output_pairs.merge(output1)
            output_pairs.merge(output2)
            polymer_counter.update({inserted: pair.count})

    return calculate_result_from_counter(polymer_counter)


def load_data_structures_from_file(file_name: str) -> (str, PolymerFormulaCollection):
    file_contents = load_text_file(file_name)
    initial_polymers = file_contents[0]
    formulas = PolymerFormulaCollection()

    for line in file_contents[2:]:
        parts = line.split(" -> ")
        input_parts = [x for x in parts[0]]
        inserted = parts[1]
        formula = PolymerFormula(PolymerPair(input_parts[0], input_parts[1]), inserted)
        formulas.append(formula)

    return initial_polymers, formulas


def get_pairs_from_template(polymer_template: str) -> PolymerPairCollection:
    pairs = PolymerPairCollection()
    for idx, left in enumerate(polymer_template[:-1]):
        right = polymer_template[idx + 1]
        pairs.append(PolymerPair(left, right, 1))
    return pairs


def calculate_result_from_counter(counter: collections.Counter) -> int:
    most_common = counter.most_common()[0]
    least_common = counter.most_common()[-1]
    return most_common[1] - least_common[1]



