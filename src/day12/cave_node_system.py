from src.day12.cave_node import CaveNode
from src.shared import load_text_file


class CaveNodeSystem:
    def __init__(self, file_name: str):
        self.nodes: list[CaveNode] = []
        self.start_node: CaveNode
        self.end_node: CaveNode
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

    def _try_add_node(self, label: str) -> CaveNode:
        existing_node = [node for node in self.nodes if node.label == label]
        if len(existing_node) > 0:
            return existing_node[0]
        else:
            node = CaveNode(label)
            self.nodes.append(node)
            if node.is_start:
                self.start_node = node
            elif node.is_end:
                self.end_node = node
            return node
