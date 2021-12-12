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

    def link(self, node: 'LinkedNode'):
        already_linked = len([x for x in self.linked_nodes if x.label == node.label]) > 0
        if not already_linked:
            self.linked_nodes.append(node)