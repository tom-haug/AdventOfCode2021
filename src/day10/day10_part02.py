from src.day10.chunk import Chunk
from src.day10.symbols import Symbol, completion_points
from src.shared.utils import load_text_file, middle_item


def load_chunks_from_file(file_name: str) -> list[Chunk]:
    file_contents = load_text_file(file_name)
    chunks: list[Chunk] = []
    for line in file_contents:
        chunks.append(Chunk(line))
    return chunks


def get_part_two_result(file_name: str) -> int:
    chunks = load_chunks_from_file(file_name)
    incomplete_opening_symbols: list[list[Symbol]] = []
    for chunk in chunks:
        valid, _, symbols = chunk.parse()
        if valid:
            incomplete_opening_symbols.append(symbols)

    scores = sorted([completion_points(x) for x in incomplete_opening_symbols])
    middle_score = middle_item(scores)
    return middle_score


if __name__ == "__main__":
    result = get_part_two_result("input.txt")
    print(result)
