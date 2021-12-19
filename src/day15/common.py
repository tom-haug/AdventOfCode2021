from typing import Callable

import numpy as np
from src.pyastar.interface import astar_graph
from src.pyastar.util.graph import WeightedGraph

from src.shared import load_int_nparray_from_file


def process(file_name: str, matrix_multiplication_factor: int) -> int:
    original_matrix = load_int_nparray_from_file(file_name)
    extended_matrix = extend_matrix(original_matrix, matrix_multiplication_factor)

    start = (0, 0)
    end = tuple(dimension - 1 for dimension in extended_matrix.shape)
    graph = to_graph(extended_matrix)

    path_and_cost = astar_graph(graph, start, end)
    cost = path_and_cost[1]
    # print("Shortest Path:", path_and_cost[0])
    return cost


def extend_matrix(input_matrix: np.ndarray, matrix_multiplication_factor: int) -> np.ndarray:
    height, width = input_matrix.shape
    output_matrix = np.full((height * matrix_multiplication_factor, width * matrix_multiplication_factor), 0, dtype=int)

    for factor_x in range(matrix_multiplication_factor):
        for factor_y in range(matrix_multiplication_factor):
            factor_total = factor_x + factor_y
            new_matrix = duplicate_matrix(input_matrix, lambda value: ((value + factor_total - 1) % 9) + 1)
            output_x = factor_x * width
            output_y = factor_y * height
            output_matrix[output_y: output_y + height, output_x: output_x + height] = new_matrix
    return output_matrix


def duplicate_matrix(input_matrix: np.ndarray, element_operation: Callable[[int], int]) -> np.ndarray:
    new_matrix: np.ndarray = input_matrix.copy()
    height, width = new_matrix.shape
    for x in range(width):
        for y in range(height):
            new_matrix[y, x] = element_operation(new_matrix[y, x])
    return new_matrix


def to_graph(matrix: np.ndarray) -> WeightedGraph:
    """
    modified from pyastar.utils.grid to allow variable cost
    """

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
