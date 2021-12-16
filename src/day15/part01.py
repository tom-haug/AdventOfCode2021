import numpy as np
from src.pyastar.interface import astar_graph
from src.pyastar.util.graph import WeightedGraph

from src.shared.utils import load_int_nparray_from_file


def to_graph(matrix: np.ndarray):
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


def get_part_one_result(file_name: str):
    matrix = load_int_nparray_from_file(file_name)
    start = (0, 0)
    end = tuple(dimension - 1 for dimension in matrix.shape)
    graph = to_graph(matrix)

    ret = astar_graph(graph, start, end)
    cost = ret[1]
    print("Shortest Path:", ret[0])
    return cost


if __name__ == "__main__":
    result = get_part_one_result("src/day15/input.txt")
    print(result)
