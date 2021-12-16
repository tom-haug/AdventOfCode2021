from typing import Callable

import numpy as np
from src.pyastar.interface import astar_graph
from src.pyastar.util.graph import WeightedGraph

from src.shared.utils import load_int_nparray_from_file


def to_graph(matrix: np.ndarray):
    """ copied from pyastar.utils.grid """
    G = WeightedGraph(undirected=True)
    height, width = matrix.shape

    for x in range(width):
        for y in range(height):
            G.add_node((x, y))
            cost = matrix[y, x]
            if x - 1 >= 0:
                G.add_edge((x - 1, y), (x, y), cost)
            if y + 1 < height:
                G.add_edge((x, y + 1), (x, y), cost)
            if x + 1 < width:
                G.add_edge((x + 1, y), (x, y), cost)
            if y - 1 >= 0:
                G.add_edge((x, y - 1), (x, y), cost)

    G.preprocess()
    return G


increment_rollover: Callable[[int], int] = lambda value: value + 1 if value < 9 else 1


def duplicate_matrix(input_matrix: np.ndarray, operation: Callable[[int], int]):
    new_matrix: np.ndarray = input_matrix.copy()
    height, width = new_matrix.shape
    for x in range(width):
        for y in range(height):
            new_matrix[y, x] = operation(new_matrix[y, x])
    return new_matrix


def extend_matrix(input_matrix: np.ndarray, matrix_multiplication_factor: int):
    input_height, input_width = input_matrix.shape
    output_matrix = np.full((input_height * matrix_multiplication_factor, input_width * matrix_multiplication_factor), 0, dtype=int)

    for factor_x in range(matrix_multiplication_factor):
        for factor_y in range(matrix_multiplication_factor):
            factor_total = factor_x + factor_y
            new_matrix = duplicate_matrix(input_matrix, lambda value: ((value + factor_total - 1) % 9) + 1)
            output_x = factor_x * input_width
            output_y = factor_y * input_height
            output_matrix[output_y: output_y + input_height, output_x: output_x + input_height] = new_matrix
    return output_matrix


def get_part_two_result(file_name: str, matrix_multiplication_factor: int):
    matrix = load_int_nparray_from_file(file_name)
    extended_matrix = extend_matrix(matrix, matrix_multiplication_factor)

    start = (0, 0)
    end = tuple(dimension - 1 for dimension in extended_matrix.shape)
    graph = to_graph(extended_matrix)

    ret = astar_graph(graph, start, end)
    cost = ret[1]
    print("Shortest Path:", ret[0])
    return cost


if __name__ == "__main__":
    result = get_part_two_result("src/day15/input.txt", 5)
    print(result)
