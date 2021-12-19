from src.day10.chunk import Chunk
from src.day10.symbols import ILLEGAL_SYMBOL_POINTS
from src.shared import load_text_file


def load_chunks_from_file(file_name: str) -> list[Chunk]:
    file_contents = load_text_file(file_name)
    chunks: list[Chunk] = []
    for line in file_contents:
        chunks.append(Chunk(line))
    return chunks


def get_part_one_result(file_name: str) -> int:
    chunks = load_chunks_from_file(file_name)
    total_points = 0
    for chunk in chunks:
        valid, last_symbol, _ = chunk.parse()
        if not valid:
            total_points += ILLEGAL_SYMBOL_POINTS[last_symbol]
    return total_points


if __name__ == "__main__":
    result = get_part_one_result("src/day10/input.txt")
    print(result)
