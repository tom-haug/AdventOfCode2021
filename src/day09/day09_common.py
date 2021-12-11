import numpy as np

from src.day09.basin import Basin
from src.day09.basin_processor import BasinProcessor
from src.shared.utils import load_text_file


def get_basins_from_file(file_name: str) -> list[Basin]:
    file_contents = load_text_file(file_name)
    height_map = np.array([[int(x) for x in list(line)] for line in file_contents])
    basin_processor = BasinProcessor(height_map)
    basins = basin_processor.create_basins()
    return basins
