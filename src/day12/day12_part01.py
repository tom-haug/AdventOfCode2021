import copy
from abc import abstractmethod, ABC
from typing import TypeVar, Generic, Type

from attr import dataclass

from src.shared.utils import load_text_file

START_LABEL = "start"
END_LABEL = "end"


class LinkedNode:
    def __init__(self, label: str):
        self._label = label
        self._linked_nodes: list[LinkedNode] = []
        self.visit_count = 0

    @property
    def linked_nodes(self) -> list['LinkedNode']:
        return self._linked_nodes

    @property
    def label(self):
        return self._label

    @property
    def can_visit_multiple(self):
        return self.label.isupper()

    def link(self, node: 'LinkedNode'):
        already_linked = len([x for x in self.linked_nodes if x.label == node.label]) > 0
        if not already_linked:
            self.linked_nodes.append(node)


class LinkedNodeSystem:
    def __init__(self, file_name: str):
        self.nodes: list[LinkedNode] = []
        self.start_node: LinkedNode
        self.end_node: LinkedNode
        self._load_from_file(file_name)

    def _load_from_file(self, file_name):
        file_contents = load_text_file(file_name)
        for line in file_contents:
            parts = line.split("-")
            label1 = parts[0]
            label2 = parts[1]
            self._add_linked_nodes_by_label(label1, label2)

    def _add_linked_nodes_by_label(self, label1: str, label2: str):
        node1 = self._try_add_node(label1)
        node2 = self._try_add_node(label2)
        node1.link(node2)
        node2.link(node1)

    def _try_add_node(self, label: str) -> LinkedNode:
        existing_nodes = [node for node in self.nodes if node.label == label]
        node = existing_nodes[0] if len(existing_nodes) > 0 else None
        if node is None:
            node = LinkedNode(label)
            self.nodes.append(node)
            if label == START_LABEL:
                self.start_node = node
            elif label == END_LABEL:
                self.end_node = node
        return node


class LinkedNodePath:
    def __init__(self):
        self.node_path: list[LinkedNode] = []

    def can_visit(self, node: LinkedNode):
        if node.label.isupper():
            return True
        else:
            return len([x for x in self.node_path if x.label == node.label]) == 0

    def append(self, node):
        self.node_path.append(node)

    def __copy__(self):
        new_path = LinkedNodePath()
        for node in self.node_path:
            new_path.append(node)
        return new_path

    @property
    def is_complete(self) -> bool:
        return self.node_path[-1].label == END_LABEL


class Processor:
    def __init__(self, system: LinkedNodeSystem):
        self.system = system

    def process(self) -> list[LinkedNodePath]:
        initial_path = LinkedNodePath()
        processed_paths = self._visit_nodes(self.system.start_node, initial_path)
        completed_paths = [path for path in processed_paths if path.is_complete]
        return completed_paths

    def _visit_nodes(self, node: LinkedNode, input_path: LinkedNodePath) -> list[LinkedNodePath]:
        output_paths: list[LinkedNodePath] = []
        ending_here_path = copy.copy(input_path)
        ending_here_path.append(node)
        output_paths.append(ending_here_path)

        if node.label != END_LABEL:
            for child_node in node.linked_nodes:
                if not input_path.can_visit(child_node):
                    continue

                new_path = copy.copy(input_path)
                new_path.append(node)
                child_returned_paths = self._visit_nodes(child_node, new_path)
                output_paths.extend(child_returned_paths)
        else:
            ...
        return output_paths


def get_part_one_result(file_name: str) -> int:
    system = LinkedNodeSystem(file_name)
    processor = Processor(system)
    completed_paths = processor.process()
    return len(completed_paths)


if __name__ == "__main__":
    result = get_part_one_result("input.txt")
    print(result)

