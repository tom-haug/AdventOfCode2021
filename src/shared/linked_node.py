from typing import TypeVar

T = TypeVar("T")

class LinkedNode:
    def __init__(self, label: str):
        self.label = label
        self.linked_nodes: list[LinkedNode] = []
        self.visit_count = 0

    def link(self, node: 'LinkedNode'):
        already_linked = len([x for x in self.linked_nodes if x.label == node.label]) > 0
        if not already_linked:
            self.linked_nodes.append(node)
