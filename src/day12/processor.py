import copy

from src.day12.cave_node import CaveNode
from src.day12.cave_node_path import CaveNodePath
from src.day12.cave_node_system import CaveNodeSystem


class Processor:
    def process(self, system: CaveNodeSystem, empty_path: CaveNodePath) -> list[CaveNodePath]:
        processed_paths = self._visit_nodes(system.start_node, empty_path)
        completed_paths = [path for path in processed_paths if path.is_complete]
        return completed_paths

    def _visit_nodes(self, node: CaveNode, input_path: CaveNodePath) -> list[CaveNodePath]:
        output_paths: list[CaveNodePath] = []
        new_path = copy.copy(input_path)
        new_path.append(node)
        if node.is_end:
            output_paths.append(new_path)
        else:
            for child_node in node.linked_nodes:
                if not new_path.can_visit(child_node):
                    continue
                child_returned_paths = self._visit_nodes(child_node, new_path)
                output_paths.extend(child_returned_paths)
        return output_paths
