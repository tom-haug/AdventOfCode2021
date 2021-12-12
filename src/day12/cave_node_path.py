import collections
from abc import ABC, abstractmethod

from src.day12.cave_node import CaveNode


class CaveNodePath(ABC):
    def __init__(self):
        self.node_path: list[CaveNode] = []

    def __repr__(self):
        return ",".join([node.label for node in self.node_path])

    @abstractmethod
    def can_visit(self, node: CaveNode):
        ...

    def append(self, node):
        self.node_path.append(node)

    def __copy__(self):
        new_path = self.__class__()
        for node in self.node_path:
            new_path.append(node)
        return new_path

    def _visited_cave_count(self, node: CaveNode):
        return len([x for x in self.node_path if x == node])

    def revisited_small_cave_count(self):
        small_cave_labels = [node.label for node in self.node_path if node.is_small_cave]
        counter = collections.Counter(small_cave_labels)
        revisited_count = len([value for value in counter.values() if value > 1])
        return revisited_count

    @property
    def is_complete(self) -> bool:
        return self.node_path[-1].is_end